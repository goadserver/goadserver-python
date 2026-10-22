# coding: utf-8

"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner import ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest(BaseModel):
    """
    ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
    """ # noqa: E501
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    destinationurl: Optional[StrictStr] = Field(default=None, description="Click URL. Alias: destination_url.")
    displayurl: Optional[StrictStr] = Field(default=None, description="Display URL (required content for native / push / offer ads). Alias: display_url.")
    previewurl: Optional[StrictStr] = Field(default=None, description="Alias: preview_url.")
    bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Currency units of your account currency, like the panel (see the bid endpoint for the floor and the bid_unit contract).")
    isactive: Optional[StrictInt] = Field(default=None, description="Alias: is_active (boolean accepted). Prefer PATCH …/active, which also runs the publisher-approval and notification side effects.")
    sort_weight: Optional[StrictInt] = None
    position: Optional[StrictInt] = None
    displaytype: Optional[StrictStr] = Field(default=None, description="Video ads: comma-separated placements (1 pre-roll, 2 mid-roll, 3 post-roll, 4 in-video slider, 5 interstitial, 6 in-page, 7 video carousel); \"0\" = all.")
    properties: Optional[StrictStr] = None
    url_poolid: Optional[StrictInt] = Field(default=None, description="Click-URL rotation pool (0 = none). Alias: url_pool_id.")
    creative_id: Optional[StrictInt] = None
    icon_id: Optional[StrictInt] = Field(default=None, description="Push icon creative (with icon_type=creative).")
    use_imptracking: Optional[StrictBool] = None
    imptrackingurl: Optional[StrictStr] = None
    usekeywords: Optional[StrictBool] = None
    keywords: Optional[StrictStr] = Field(default=None, description="Comma- or newline-separated. Trimmed, lowercased and deduplicated on save.")
    ad_options: Optional[Dict[str, Any]] = Field(default=None, description="SmartAds `{fixed_position, smart_options}`; `chat` {followup, price} for AI chat ads (set those with chat_followup / chat_price); `keyword_preference` for Search Ads (set with keyword_mode).")
    smart_network_id: Optional[StrictInt] = None
    chat_followup: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="Search Ads (adtype 42) ron ads: a sponsored follow-up question for AI chat zones (chat_followups > 0); picking it asks the chat that question and counts as a click. Stored in ad_options.chat.followup (merged — other ad_options keys are kept); empty string clears.")
    chat_price: Optional[Annotated[str, Field(strict=True, max_length=24)]] = Field(default=None, description="Search Ads ron ads: the price on AI chat product cards (chat_style products). Stored in ad_options.chat.price; product feeds fill it.")
    keyword_mode: Optional[StrictStr] = Field(default='specific', description="Search Ads (adtype 42) ron ads: how the ad's own keywords (usekeywords + keywords) act on a search. specific = shown only when a keyword matches the search; preference = shown for any search and ranked first when a keyword matches, at most 6 keywords (422 on keywords otherwise). Stored as ad_options.keyword_preference (true, or absent = specific); other ad_options keys are kept. Other zone types always treat ad keywords as specific.")
    video_overlays: Optional[Annotated[List[ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner], Field(max_length=8)]] = Field(default=None, description="Shoppable video (ron video ads, adtype 4 / 20): timed hotspots and product cards over the ad. A click counts as the ad's click and lands on the overlay's url (empty = the ad's destination). Served to goCtrl's video players and in VAST (Extension goadserver-overlays + a SIMID InteractiveCreativeFile, VAST 4.1). Stored in ad_options.overlays (merged — other ad_options keys are kept); [] clears. Per-overlay shown / clicks: GET /campaigns/{type}/{campaignId}/ads/{adId}/overlay-stats.")
    creatives: Optional[Dict[str, Any]] = Field(default=None, description="The creative blob verbatim (object or JSON string).")
    banner_type: Optional[StrictStr] = None
    banner_url: Optional[StrictStr] = None
    banner_iframe_url: Optional[StrictStr] = None
    banner_html: Optional[StrictStr] = None
    banner_pool_id: Optional[StrictInt] = None
    image_type: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    image_pool_id: Optional[StrictInt] = None
    video_type: Optional[StrictStr] = None
    video_url: Optional[StrictStr] = None
    companion_url: Optional[StrictStr] = Field(default=None, description="Audio ads (adtype 43): an https companion image shown while the ad plays (VAST CompanionAds; the goCtrl audio plugin's bar). Stored as creatives.image {type: url}.")
    companion_width: Optional[StrictInt] = 300
    companion_height: Optional[StrictInt] = 250
    video_pool_id: Optional[StrictInt] = None
    html_code: Optional[StrictStr] = None
    html_total_items: Optional[StrictInt] = None
    icon_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["title", "description", "destinationurl", "displayurl", "previewurl", "bid", "isactive", "sort_weight", "position", "displaytype", "properties", "url_poolid", "creative_id", "icon_id", "use_imptracking", "imptrackingurl", "usekeywords", "keywords", "ad_options", "smart_network_id", "chat_followup", "chat_price", "keyword_mode", "video_overlays", "creatives", "banner_type", "banner_url", "banner_iframe_url", "banner_html", "banner_pool_id", "image_type", "image_url", "image_pool_id", "video_type", "video_url", "companion_url", "companion_width", "companion_height", "video_pool_id", "html_code", "html_total_items", "icon_type"]

    @field_validator('isactive')
    def isactive_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('keyword_mode')
    def keyword_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['specific', 'preference']):
            raise ValueError("must be one of enum values ('specific', 'preference')")
        return value

    @field_validator('banner_type')
    def banner_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creative', 'pool', 'hotlink_image', 'hotlink_video', 'iframe', 'html']):
            raise ValueError("must be one of enum values ('creative', 'pool', 'hotlink_image', 'hotlink_video', 'iframe', 'html')")
        return value

    @field_validator('image_type')
    def image_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creative', 'pool', 'html', 'none']):
            raise ValueError("must be one of enum values ('creative', 'pool', 'html', 'none')")
        return value

    @field_validator('video_type')
    def video_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['url', 'xml', 'html', 'creative', 'pool']):
            raise ValueError("must be one of enum values ('url', 'xml', 'html', 'creative', 'pool')")
        return value

    @field_validator('icon_type')
    def icon_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creative']):
            raise ValueError("must be one of enum values ('creative')")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in video_overlays (list)
        _items = []
        if self.video_overlays:
            for _item_video_overlays in self.video_overlays:
                if _item_video_overlays:
                    _items.append(_item_video_overlays.to_dict())
            _dict['video_overlays'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "destinationurl": obj.get("destinationurl"),
            "displayurl": obj.get("displayurl"),
            "previewurl": obj.get("previewurl"),
            "bid": obj.get("bid"),
            "isactive": obj.get("isactive"),
            "sort_weight": obj.get("sort_weight"),
            "position": obj.get("position"),
            "displaytype": obj.get("displaytype"),
            "properties": obj.get("properties"),
            "url_poolid": obj.get("url_poolid"),
            "creative_id": obj.get("creative_id"),
            "icon_id": obj.get("icon_id"),
            "use_imptracking": obj.get("use_imptracking"),
            "imptrackingurl": obj.get("imptrackingurl"),
            "usekeywords": obj.get("usekeywords"),
            "keywords": obj.get("keywords"),
            "ad_options": obj.get("ad_options"),
            "smart_network_id": obj.get("smart_network_id"),
            "chat_followup": obj.get("chat_followup"),
            "chat_price": obj.get("chat_price"),
            "keyword_mode": obj.get("keyword_mode") if obj.get("keyword_mode") is not None else 'specific',
            "video_overlays": [ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner.from_dict(_item) for _item in obj["video_overlays"]] if obj.get("video_overlays") is not None else None,
            "creatives": obj.get("creatives"),
            "banner_type": obj.get("banner_type"),
            "banner_url": obj.get("banner_url"),
            "banner_iframe_url": obj.get("banner_iframe_url"),
            "banner_html": obj.get("banner_html"),
            "banner_pool_id": obj.get("banner_pool_id"),
            "image_type": obj.get("image_type"),
            "image_url": obj.get("image_url"),
            "image_pool_id": obj.get("image_pool_id"),
            "video_type": obj.get("video_type"),
            "video_url": obj.get("video_url"),
            "companion_url": obj.get("companion_url"),
            "companion_width": obj.get("companion_width") if obj.get("companion_width") is not None else 300,
            "companion_height": obj.get("companion_height") if obj.get("companion_height") is not None else 250,
            "video_pool_id": obj.get("video_pool_id"),
            "html_code": obj.get("html_code"),
            "html_total_items": obj.get("html_total_items"),
            "icon_type": obj.get("icon_type")
        })
        return _obj



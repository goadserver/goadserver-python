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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from goadserver.models.ssp_campaign_write_slots_inner import SspCampaignWriteSlotsInner
from goadserver.models.ssp_campaign_write_zoneurls_inner import SspCampaignWriteZoneurlsInner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SspCampaignWrite(BaseModel):
    """
    SspCampaignWrite
    """ # noqa: E501
    name: StrictStr
    adtype: Optional[StrictInt] = Field(default=None, description="Ad type id (setup-data `ad_types[].id`).")
    ssptype: Optional[StrictStr] = 'ssp'
    rtbtype: Optional[StrictStr] = Field(default='openrtb', description="openrtb or a legacy XML/JSON template type, per setup-data.")
    header_bidding: Optional[StrictBool] = Field(default=None, description="external/exchange only; locked after create.")
    rtb_network: Optional[StrictInt] = Field(default=None, description="RTB network id (setup-data `rtb_networks`). Required for ssptype=ssp.")
    ssp_pct: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = Field(default=80, description="Revenue share in percent (required 1-100 for exchange).")
    siteid: Optional[StrictInt] = Field(default=None, description="One of your sites. Required for external and header bidding.")
    slots: Optional[List[SspCampaignWriteSlotsInner]] = Field(default=None, description="Header-bidding slots.")
    request_url: Optional[StrictStr] = Field(default=None, description="Partner endpoint (ssptype=ssp, use_type 0).")
    use_type: Optional[StrictInt] = Field(default=None, description="ssp only: 0 = one URL, 1 = per-ad-zone URLs, 2 = smart-zone RTB feed.")
    zoneurls: Optional[List[SspCampaignWriteZoneurlsInner]] = Field(default=None, description="use_type 1: per-zone URLs (your own ad zones only; others are dropped).")
    p_type: Optional[StrictInt] = None
    adm_response_type: Optional[StrictStr] = 'html'
    rtb_tpl_id: Optional[StrictInt] = 1
    bid_action: Optional[StrictInt] = 1
    device_type_ids: Optional[List[StrictInt]] = Field(default=None, description="Empty = all. A comma-separated string is accepted too (same for every list below).")
    osids: Optional[List[StrictInt]] = None
    browserids: Optional[List[StrictInt]] = None
    regionids: Optional[List[StrictInt]] = None
    browserlanguages: Optional[List[StrictStr]] = None
    connection_types: Optional[List[StrictInt]] = None
    ssp_ids: Optional[List[StrictInt]] = None
    wl_ron_campaign_ids: Optional[List[StrictInt]] = Field(default=None, description="From GET .../wl-ron-campaigns.")
    rtb_categories: Optional[List[StrictStr]] = None
    dsp_ids: Optional[List[StrictInt]] = Field(default=None, description="Admin only (ignored for API keys).")
    displayoptions: Optional[StrictStr] = '0'
    log_skipped: Optional[StrictInt] = None
    use_adscan: Optional[StrictInt] = None
    bill_on_burl: Optional[StrictInt] = Field(default=None, description="Bill on the OpenRTB burl (external/exchange, openrtb).")
    use_optimiser: Optional[StrictInt] = None
    optimiser_data: Optional[Dict[str, Any]] = Field(default=None, description="{disc_rules: [...]}, external/exchange only.")
    use_api: Optional[StrictInt] = None
    api_data: Optional[Dict[str, Any]] = Field(default=None, description="Partner reporting-API credentials (ssp/external).")
    __properties: ClassVar[List[str]] = ["name", "adtype", "ssptype", "rtbtype", "header_bidding", "rtb_network", "ssp_pct", "siteid", "slots", "request_url", "use_type", "zoneurls", "p_type", "adm_response_type", "rtb_tpl_id", "bid_action", "device_type_ids", "osids", "browserids", "regionids", "browserlanguages", "connection_types", "ssp_ids", "wl_ron_campaign_ids", "rtb_categories", "dsp_ids", "displayoptions", "log_skipped", "use_adscan", "bill_on_burl", "use_optimiser", "optimiser_data", "use_api", "api_data"]

    @field_validator('ssptype')
    def ssptype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ssp', 'external', 'exchange']):
            raise ValueError("must be one of enum values ('ssp', 'external', 'exchange')")
        return value

    @field_validator('use_type')
    def use_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2]):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    @field_validator('log_skipped')
    def log_skipped_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('use_adscan')
    def use_adscan_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('bill_on_burl')
    def bill_on_burl_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('use_optimiser')
    def use_optimiser_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('use_api')
    def use_api_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
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
        """Create an instance of SspCampaignWrite from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in slots (list)
        _items = []
        if self.slots:
            for _item_slots in self.slots:
                if _item_slots:
                    _items.append(_item_slots.to_dict())
            _dict['slots'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zoneurls (list)
        _items = []
        if self.zoneurls:
            for _item_zoneurls in self.zoneurls:
                if _item_zoneurls:
                    _items.append(_item_zoneurls.to_dict())
            _dict['zoneurls'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SspCampaignWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "adtype": obj.get("adtype"),
            "ssptype": obj.get("ssptype") if obj.get("ssptype") is not None else 'ssp',
            "rtbtype": obj.get("rtbtype") if obj.get("rtbtype") is not None else 'openrtb',
            "header_bidding": obj.get("header_bidding"),
            "rtb_network": obj.get("rtb_network"),
            "ssp_pct": obj.get("ssp_pct") if obj.get("ssp_pct") is not None else 80,
            "siteid": obj.get("siteid"),
            "slots": [SspCampaignWriteSlotsInner.from_dict(_item) for _item in obj["slots"]] if obj.get("slots") is not None else None,
            "request_url": obj.get("request_url"),
            "use_type": obj.get("use_type"),
            "zoneurls": [SspCampaignWriteZoneurlsInner.from_dict(_item) for _item in obj["zoneurls"]] if obj.get("zoneurls") is not None else None,
            "p_type": obj.get("p_type"),
            "adm_response_type": obj.get("adm_response_type") if obj.get("adm_response_type") is not None else 'html',
            "rtb_tpl_id": obj.get("rtb_tpl_id") if obj.get("rtb_tpl_id") is not None else 1,
            "bid_action": obj.get("bid_action") if obj.get("bid_action") is not None else 1,
            "device_type_ids": obj.get("device_type_ids"),
            "osids": obj.get("osids"),
            "browserids": obj.get("browserids"),
            "regionids": obj.get("regionids"),
            "browserlanguages": obj.get("browserlanguages"),
            "connection_types": obj.get("connection_types"),
            "ssp_ids": obj.get("ssp_ids"),
            "wl_ron_campaign_ids": obj.get("wl_ron_campaign_ids"),
            "rtb_categories": obj.get("rtb_categories"),
            "dsp_ids": obj.get("dsp_ids"),
            "displayoptions": obj.get("displayoptions") if obj.get("displayoptions") is not None else '0',
            "log_skipped": obj.get("log_skipped"),
            "use_adscan": obj.get("use_adscan"),
            "bill_on_burl": obj.get("bill_on_burl"),
            "use_optimiser": obj.get("use_optimiser"),
            "optimiser_data": obj.get("optimiser_data"),
            "use_api": obj.get("use_api"),
            "api_data": obj.get("api_data")
        })
        return _obj



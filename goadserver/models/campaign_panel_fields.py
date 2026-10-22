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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from goadserver.models.campaign_panel_fields_about_settings import CampaignPanelFieldsAboutSettings
from goadserver.models.campaign_panel_fields_av_check import CampaignPanelFieldsAvCheck
from goadserver.models.campaign_panel_fields_booster_settings import CampaignPanelFieldsBoosterSettings
from goadserver.models.campaign_panel_fields_conversion_capping import CampaignPanelFieldsConversionCapping
from goadserver.models.campaign_panel_fields_day_parting import CampaignPanelFieldsDayParting
from goadserver.models.campaign_panel_fields_domain_mask import CampaignPanelFieldsDomainMask
from goadserver.models.campaign_panel_fields_feed_settings import CampaignPanelFieldsFeedSettings
from goadserver.models.campaign_panel_fields_priority import CampaignPanelFieldsPriority
from goadserver.models.campaign_panel_fields_screens import CampaignPanelFieldsScreens
from goadserver.models.campaign_panel_fields_suggestions import CampaignPanelFieldsSuggestions
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CampaignPanelFields(BaseModel):
    """
    Campaign-form fields for `ron` / `cpm` / `rtb` campaigns, writable on `POST /api/v1/campaigns/{type}` and `PATCH /api/v1/campaigns/{type}/{id}` and returned by list / show (option fields when stored). Which of them a campaign takes depends on its type, the network's modules, its ad type and its pay type — `GET /api/v1/campaigns/{type}/_schema` lists exactly the ones available to you (`?ad_type=` narrows it), with `ad_types` / `selling_types` restrictions. Sending one that is not available is a `422` naming the field (for example `\"orientation applies only to ad type(s) 3, 22.\"`), not a silent drop. Object fields merge on PATCH: keys you omit keep their stored value. Money is in main currency units (not cents). 
    """ # noqa: E501
    groupid: Optional[StrictStr] = Field(default=None, description="Campaign tags / groups: comma-separated group ids (\"0\" = none). A JSON array is accepted.")
    display_options: Optional[StrictStr] = Field(default=None, description="Display options for the ad type (e.g. video roll position), comma-separated ids.")
    min_rank: Optional[StrictInt] = Field(default=None, description="Minimum ad zone quality rank (flat campaigns on networks that rank ad zones). Not the same as `priority`.")
    fx_rating: Optional[StrictInt] = Field(default=None, description="Fixed rating flag (advanced).")
    mail_campaign_budget: Optional[StrictBool] = Field(default=None, description="ron/cpm: email the account when `total_budget` is reached. Where the network offers lifetime budgets.")
    use_dynamic_costs: Optional[StrictBool] = Field(default=None, description="ron CPC/CPM (`selling_type` 0/1): let the bid rise automatically by up to `dynamic_costs_increase` percent.")
    dynamic_costs_increase: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Maximum dynamic-cost increase in percent.")
    conversion_capping: Optional[CampaignPanelFieldsConversionCapping] = None
    fix_cpa: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="ron/cpm CPA goal in main currency. After create only your account manager changes it, except on AdManager networks (a PATCH with a different value is a 422; the same value is a no-op).")
    fix_cpa_conv_types: Optional[StrictStr] = Field(default=None, description="Conversion type ids the CPA goal counts (empty = all). A JSON array is accepted.")
    booster: Optional[StrictBool] = Field(default=None, description="ron CPA (`selling_type` 2): AdBooster, where the network licenses it.")
    booster_settings: Optional[CampaignPanelFieldsBoosterSettings] = None
    default_bid_type: Optional[StrictInt] = Field(default=None, description="ron: smart bidding on (1) / off (0), for CPC or CPM where the network lets users switch it on.")
    sort_type: Optional[StrictInt] = Field(default=None, description="ron: ad sorting — 0 = eCPM, 1 = random, 2 = weighted. Any pay type (CPC/CPM: random or weighted skips smart-bid repricing). Not for offers.")
    as_failover: Optional[StrictBool] = Field(default=None, description="ron (AdManager networks, not flat): serve only as failover.")
    day_parting: Optional[CampaignPanelFieldsDayParting] = None
    screens: Optional[CampaignPanelFieldsScreens] = None
    display_times: Optional[StrictStr] = Field(default=None, description="Legacy daily time windows (pipe-separated; overlaps merged). Superseded by `day_parting`.")
    display_days: Optional[StrictStr] = Field(default=None, description="Legacy weekday list (\"0\" = every day). Superseded by `day_parting`.")
    site_languages: Optional[StrictStr] = Field(default=None, description="Website language codes (\"0\" = all). A JSON array is accepted.")
    connection_types: Optional[StrictStr] = Field(default=None, description="Connection type ids (\"0\" = all). A JSON array is accepted.")
    carrier_ids: Optional[StrictStr] = Field(default=None, description="ron: mobile carrier ids (\"0\" = all); meaningful with `connection_types` = \"2\" and no IP pool.")
    rating_id: Optional[StrictInt] = Field(default=None, description="Content rating id, where the network uses ratings.")
    orientation: Optional[StrictStr] = Field(default=None, description="ron/cpm ad types 3 and 22.")
    site_mode: Optional[StrictInt] = Field(default=None, description="ron: 0 = RON (all sites), 1 = Premium sites (display only; may need a minimum balance). Read back with the admin-set `sites_locked`.")
    only_tagged_zones: Optional[StrictBool] = Field(default=None, description="ron/cpm on AdManager networks: only run on ad zones sharing one of the campaign's groups.")
    skip_low_quality: Optional[StrictInt] = Field(default=None, description="ron/cpm (not flat): low-quality traffic 0 = accept, 1 = block, 2 = target only.")
    ip_whitelist: Optional[StrictStr] = Field(default=None, description="IP allow list, one entry per line (IPv4/IPv6, CIDR or `a|b` ranges); each line is validated. A JSON array is accepted.")
    ip_blacklist: Optional[StrictStr] = Field(default=None, description="IP deny list, same syntax. An IP on both lists is blocked.")
    av_check: Optional[CampaignPanelFieldsAvCheck] = None
    email_type: Optional[StrictInt] = Field(default=None, description="ron/rtb email ads (ad type 15): 0 = accept all, 1 = email only, 2 = non-email only.")
    use_subscription_age: Optional[StrictBool] = Field(default=None, description="ron push ads (ad type 7).")
    subscription_age: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    instant_impression: Optional[StrictBool] = Field(default=None, description="ron video (ad type 4) on AdManager networks.")
    subid_list: Optional[StrictStr] = Field(default=None, description="ron/cpm (not flat): SubIDs to filter on, one per line or comma-separated (empty clears). Stored as the campaign's SubID filter.")
    subid_list_mode: Optional[StrictStr] = None
    source_optimizer_ids: Optional[StrictStr] = Field(default=None, description="ron: your own active source optimizers, at most one per filter type; ids that are not yours are dropped. \"0\" detaches all.")
    wl_zone_ids: Optional[StrictStr] = Field(default=None, description="cpm: ad zone ids the campaign is pinned to (empty = all).")
    feed_id: Optional[StrictInt] = Field(default=None, description="ron ad types 3 / 22: one of your XML feeds (0 = none).")
    feed_settings: Optional[CampaignPanelFieldsFeedSettings] = None
    priority: Optional[CampaignPanelFieldsPriority] = None
    suggestions: Optional[CampaignPanelFieldsSuggestions] = None
    hide_referrer: Optional[StrictBool] = Field(default=None, description="ron/rtb on AdManager networks (options): JS redirect so the landing page sees the ad server as referrer.")
    log_conv_as_paid: Optional[StrictBool] = Field(default=None, description="ron on AdManager networks where you own an SSP campaign (options): book spend as Traffic Cost and conversions as Paid. Defaults to true on new campaigns there.")
    about_settings: Optional[CampaignPanelFieldsAboutSettings] = None
    use_live_feed: Optional[StrictBool] = Field(default=None, description="ron video (ad type 4): live HLS feed, where the network offers it (not on AdNetwork networks).")
    live_feed_parent_id: Optional[StrictInt] = Field(default=None, description="One of your master-feed video campaigns (0 = this campaign is a master feed).")
    live_feed_settings: Optional[Dict[str, Any]] = Field(default=None, description="{hls_provider, campaign, gender, resize_to, bid, desturl_macro, desturl_type, use_logo}. hls_provider: chaturbate, bongacams or camsoda; campaign: the provider's affiliate/campaign id (CamSoda: your affiliate id); gender: f, m, t or c; desturl_type (chat_room_url or chat_room_url_revshare) is Chaturbate only; desturl_macro fills the link's tracking slot (CamSoda: appended to the link as query text, e.g. sub_id={clickid}).")
    offer_type_id: Optional[StrictInt] = Field(default=None, description="ron offers (ad type 21).")
    description: Optional[StrictStr] = Field(default=None, description="ron offers (ad type 21): the offer description (stored on the offer's ad).")
    destination_url: Optional[StrictStr] = Field(default=None, description="ron offers (ad type 21): http(s) destination URL (include `{tracking}` for CPA offers).")
    preview_url: Optional[StrictStr] = Field(default=None, description="ron offers (ad type 21): http(s) preview URL.")
    rtb_network_id: Optional[StrictInt] = Field(default=None, description="rtb: an active RTB network of this tenant. Ignored when your account is locked to one network.")
    rtb_type: Optional[StrictStr] = Field(default=None, description="rtb protocol; json / xml only for ad types 7, 11, 15.")
    use_type: Optional[StrictInt] = Field(default=None, description="rtb: 0 = one `request_url`; 1 = a URL per zone in `zone_urls` (then `request_url` is optional).")
    zone_urls: Optional[List[Dict[str, Any]]] = Field(default=None, description="rtb URLs per zone (use_type 1).")
    bid_action: Optional[StrictInt] = Field(default=None, description="rtb OpenRTB auction: 1 = first price, 2 = second price.")
    use_qps: Optional[StrictBool] = None
    qps: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    rtb_categories: Optional[StrictStr] = Field(default=None, description="rtb OpenRTB content categories. A JSON array is accepted.")
    use_api: Optional[StrictBool] = Field(default=None, description="rtb: pull the partner's stats through its reporting API.")
    api_data: Optional[Dict[str, Any]] = Field(default=None, description="rtb per-network stats-API credentials.")
    log_skipped: Optional[StrictBool] = Field(default=None, description="rtb: log no-bid responses in the stats.")
    domain_mask: Optional[CampaignPanelFieldsDomainMask] = None
    rtb_xml_markup: Optional[StrictBool] = Field(default=None, description="rtb banner (ad type 2), stored as options.rtb.xml_markup: ask the bidder for XML ad markup.")
    __properties: ClassVar[List[str]] = ["groupid", "display_options", "min_rank", "fx_rating", "mail_campaign_budget", "use_dynamic_costs", "dynamic_costs_increase", "conversion_capping", "fix_cpa", "fix_cpa_conv_types", "booster", "booster_settings", "default_bid_type", "sort_type", "as_failover", "day_parting", "screens", "display_times", "display_days", "site_languages", "connection_types", "carrier_ids", "rating_id", "orientation", "site_mode", "only_tagged_zones", "skip_low_quality", "ip_whitelist", "ip_blacklist", "av_check", "email_type", "use_subscription_age", "subscription_age", "instant_impression", "subid_list", "subid_list_mode", "source_optimizer_ids", "wl_zone_ids", "feed_id", "feed_settings", "priority", "suggestions", "hide_referrer", "log_conv_as_paid", "about_settings", "use_live_feed", "live_feed_parent_id", "live_feed_settings", "offer_type_id", "description", "destination_url", "preview_url", "rtb_network_id", "rtb_type", "use_type", "zone_urls", "bid_action", "use_qps", "qps", "rtb_categories", "use_api", "api_data", "log_skipped", "domain_mask", "rtb_xml_markup"]

    @field_validator('default_bid_type')
    def default_bid_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('orientation')
    def orientation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['landscape', 'portrait', 'square']):
            raise ValueError("must be one of enum values ('landscape', 'portrait', 'square')")
        return value

    @field_validator('site_mode')
    def site_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('skip_low_quality')
    def skip_low_quality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2]):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    @field_validator('email_type')
    def email_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2]):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    @field_validator('subid_list_mode')
    def subid_list_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['whitelist', 'blacklist']):
            raise ValueError("must be one of enum values ('whitelist', 'blacklist')")
        return value

    @field_validator('rtb_type')
    def rtb_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['openrtb', 'json', 'xml']):
            raise ValueError("must be one of enum values ('openrtb', 'json', 'xml')")
        return value

    @field_validator('use_type')
    def use_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('bid_action')
    def bid_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, 2]):
            raise ValueError("must be one of enum values (1, 2)")
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
        """Create an instance of CampaignPanelFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversion_capping
        if self.conversion_capping:
            _dict['conversion_capping'] = self.conversion_capping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of booster_settings
        if self.booster_settings:
            _dict['booster_settings'] = self.booster_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of day_parting
        if self.day_parting:
            _dict['day_parting'] = self.day_parting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of screens
        if self.screens:
            _dict['screens'] = self.screens.to_dict()
        # override the default output from pydantic by calling `to_dict()` of av_check
        if self.av_check:
            _dict['av_check'] = self.av_check.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feed_settings
        if self.feed_settings:
            _dict['feed_settings'] = self.feed_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of suggestions
        if self.suggestions:
            _dict['suggestions'] = self.suggestions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of about_settings
        if self.about_settings:
            _dict['about_settings'] = self.about_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_mask
        if self.domain_mask:
            _dict['domain_mask'] = self.domain_mask.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignPanelFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupid": obj.get("groupid"),
            "display_options": obj.get("display_options"),
            "min_rank": obj.get("min_rank"),
            "fx_rating": obj.get("fx_rating"),
            "mail_campaign_budget": obj.get("mail_campaign_budget"),
            "use_dynamic_costs": obj.get("use_dynamic_costs"),
            "dynamic_costs_increase": obj.get("dynamic_costs_increase"),
            "conversion_capping": CampaignPanelFieldsConversionCapping.from_dict(obj["conversion_capping"]) if obj.get("conversion_capping") is not None else None,
            "fix_cpa": obj.get("fix_cpa"),
            "fix_cpa_conv_types": obj.get("fix_cpa_conv_types"),
            "booster": obj.get("booster"),
            "booster_settings": CampaignPanelFieldsBoosterSettings.from_dict(obj["booster_settings"]) if obj.get("booster_settings") is not None else None,
            "default_bid_type": obj.get("default_bid_type"),
            "sort_type": obj.get("sort_type"),
            "as_failover": obj.get("as_failover"),
            "day_parting": CampaignPanelFieldsDayParting.from_dict(obj["day_parting"]) if obj.get("day_parting") is not None else None,
            "screens": CampaignPanelFieldsScreens.from_dict(obj["screens"]) if obj.get("screens") is not None else None,
            "display_times": obj.get("display_times"),
            "display_days": obj.get("display_days"),
            "site_languages": obj.get("site_languages"),
            "connection_types": obj.get("connection_types"),
            "carrier_ids": obj.get("carrier_ids"),
            "rating_id": obj.get("rating_id"),
            "orientation": obj.get("orientation"),
            "site_mode": obj.get("site_mode"),
            "only_tagged_zones": obj.get("only_tagged_zones"),
            "skip_low_quality": obj.get("skip_low_quality"),
            "ip_whitelist": obj.get("ip_whitelist"),
            "ip_blacklist": obj.get("ip_blacklist"),
            "av_check": CampaignPanelFieldsAvCheck.from_dict(obj["av_check"]) if obj.get("av_check") is not None else None,
            "email_type": obj.get("email_type"),
            "use_subscription_age": obj.get("use_subscription_age"),
            "subscription_age": obj.get("subscription_age"),
            "instant_impression": obj.get("instant_impression"),
            "subid_list": obj.get("subid_list"),
            "subid_list_mode": obj.get("subid_list_mode"),
            "source_optimizer_ids": obj.get("source_optimizer_ids"),
            "wl_zone_ids": obj.get("wl_zone_ids"),
            "feed_id": obj.get("feed_id"),
            "feed_settings": CampaignPanelFieldsFeedSettings.from_dict(obj["feed_settings"]) if obj.get("feed_settings") is not None else None,
            "priority": CampaignPanelFieldsPriority.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "suggestions": CampaignPanelFieldsSuggestions.from_dict(obj["suggestions"]) if obj.get("suggestions") is not None else None,
            "hide_referrer": obj.get("hide_referrer"),
            "log_conv_as_paid": obj.get("log_conv_as_paid"),
            "about_settings": CampaignPanelFieldsAboutSettings.from_dict(obj["about_settings"]) if obj.get("about_settings") is not None else None,
            "use_live_feed": obj.get("use_live_feed"),
            "live_feed_parent_id": obj.get("live_feed_parent_id"),
            "live_feed_settings": obj.get("live_feed_settings"),
            "offer_type_id": obj.get("offer_type_id"),
            "description": obj.get("description"),
            "destination_url": obj.get("destination_url"),
            "preview_url": obj.get("preview_url"),
            "rtb_network_id": obj.get("rtb_network_id"),
            "rtb_type": obj.get("rtb_type"),
            "use_type": obj.get("use_type"),
            "zone_urls": obj.get("zone_urls"),
            "bid_action": obj.get("bid_action"),
            "use_qps": obj.get("use_qps"),
            "qps": obj.get("qps"),
            "rtb_categories": obj.get("rtb_categories"),
            "use_api": obj.get("use_api"),
            "api_data": obj.get("api_data"),
            "log_skipped": obj.get("log_skipped"),
            "domain_mask": CampaignPanelFieldsDomainMask.from_dict(obj["domain_mask"]) if obj.get("domain_mask") is not None else None,
            "rtb_xml_markup": obj.get("rtb_xml_markup")
        })
        return _obj



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
from goadserver.models.adspace_create_banner_settings import AdspaceCreateBannerSettings
from goadserver.models.adspace_create_bot_settings import AdspaceCreateBotSettings
from goadserver.models.adspace_create_email_settings import AdspaceCreateEmailSettings
from goadserver.models.adspace_create_screen_settings import AdspaceCreateScreenSettings
from goadserver.models.adspace_create_search_settings import AdspaceCreateSearchSettings
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AdspaceCreate(BaseModel):
    """
    Adspace create body. The fields below are the common top-level keys every type accepts; the type-specific settings block goes under the body key returned in `settings_block.name` from `GET /api/v1/adspaces/{type}/_schema` (e.g. `banner_settings`, `pop_settings`, `native_settings`, `player_settings`).  Per-type details — including which `*_settings` block to send and the legal fields inside it — live at the runtime `_schema` endpoint, since they vary by tenant config. 
    """ # noqa: E501
    name: StrictStr
    siteid: StrictInt = Field(description="Parent website id from /api/v1/sites.")
    description: Optional[StrictStr] = None
    ratingid: Optional[StrictInt] = 0
    main_catid: Optional[StrictInt] = 0
    catid: Optional[StrictInt] = 0
    locationid: Optional[StrictInt] = 0
    adsizeid: Optional[StrictInt] = Field(default=0, description="Banner size id (banner-flavored types only). Also accepted as banner_settings.sizeid.")
    autoapprove: Optional[StrictBool] = False
    isvisible: Optional[StrictBool] = True
    sendmails: Optional[StrictBool] = False
    useownbanners: Optional[StrictBool] = False
    usealtbanner: Optional[StrictBool] = False
    usecpmbuys: Optional[StrictBool] = True
    allow_iframes: Optional[StrictBool] = True
    allow_animation: Optional[StrictBool] = True
    skip_ron_if_cpm: Optional[StrictBool] = False
    no_promotion: Optional[StrictBool] = False
    run_rtb_after_smartzone: Optional[StrictBool] = False
    use_pixel_log: Optional[StrictBool] = False
    show_about: Optional[StrictBool] = False
    hidecopy: Optional[StrictBool] = Field(default=False, description="Hide the \"Ads by\" copy. Stored as json_settings.hideadsby; `hideadsby` is accepted as an alias and wins when both are sent.")
    hideadsby: Optional[StrictBool] = Field(default=None, description="Alias of hidecopy (the stored name).")
    useflatbuys: Optional[StrictBool] = Field(default=True, description="Accept flat bookings on this zone.")
    parentid: Optional[StrictInt] = Field(default=0, description="Parent ad zone (another live zone of yours) — in-video sub-zones hang under their player zone. 0 = top level.")
    display_type: Optional[StrictInt] = Field(default=0, description="Banner zones: 0 = inline, 1 = floater (send floater_settings). Forced to 1 for types 17, 19, 20, 22.")
    new_zoneid: Optional[StrictInt] = Field(default=0, description="Banner zones: forward unfilled traffic to this ad zone id. 0 = off.")
    only_wl_campaigns: Optional[StrictBool] = Field(default=False, description="Serve only the whitelisted campaigns. Ad Manager tenants only — dropped elsewhere.")
    only_tagged_campaigns: Optional[StrictBool] = Field(default=False, description="Serve only campaigns in the zone's campaign groups (`tags`). Only where campaign-group targeting is enabled — dropped elsewhere.")
    force_wl_targeting: Optional[StrictBool] = Field(default=False, description="Apply the whitelisted campaigns' own targeting. Also written by PUT /wl-campaigns.")
    skip_rtb_when_wl: Optional[StrictBool] = Field(default=False, description="Skip RTB when a whitelisted campaign can fill. Stored in json_settings.options.")
    use_fixed_payouts: Optional[StrictBool] = Field(default=False, description="Fixed payout instead of revenue share (alias `fixed_payouts`). Only where modules.publisher.adzones.options.use_fixed_payouts is on and the tenant is Ad Manager; dropped silently otherwise.")
    fixed_payouts: Optional[StrictBool] = Field(default=None, description="Alias of use_fixed_payouts (the name the panel sends).")
    fixed_payout_data: Optional[Dict[str, Any]] = Field(default=None, description="{type: cpc|cpm, amount (currency units), enddate, amounts: per-country overrides}. Only with use_fixed_payouts.")
    rtb_name: Optional[StrictStr] = Field(default=None, description="Name the zone is reported under to RTB partners.")
    tags: Optional[List[StrictInt]] = Field(default=None, description="Campaign-group ids (campaign_groups). Empty = inherit the site's groups.")
    excl_catids: Optional[StrictStr] = Field(default=None, description="Comma-separated category ids to exclude.")
    exclproperties: Optional[StrictStr] = None
    use_subid_list: Optional[StrictBool] = False
    subid_list: Optional[StrictStr] = Field(default=None, description="Comma-separated subid allowlist (use_subid_list=true required).")
    use_domain_list: Optional[StrictBool] = False
    domain_list: Optional[List[StrictStr]] = None
    use_costs: Optional[StrictBool] = False
    costs_data: Optional[Dict[str, Any]] = None
    use_dynamic_costs: Optional[StrictBool] = False
    use_fallback_campaign: Optional[StrictBool] = False
    fallback_campaignid: Optional[StrictInt] = 0
    quality_rank: Optional[StrictInt] = 0
    banner_settings: Optional[AdspaceCreateBannerSettings] = None
    native_settings: Optional[Dict[str, Any]] = Field(default=None, description="Native-flavored zones (nativeads, interstitial_native, creator_widget, search_ads, bot_ads — search_ads and bot_ads read only `orientation`). nativeads also takes the infinite content feed: `infinite` (boolean; switches GET /api/v1/adspaces/{id}/code to goCtrl's feed plugin), `feed_rss` (your RSS feed: http(s) URL or a path such as /feed/; anything else 422 `native_settings.feed_rss`), `feed_ad_every` (organic cards before each ad, 0-10, default 2), `feed_max_pages` (1-30, default 10), `feed_title`, `feed_label` (plain text). Ad impressions in the feed are counted when the card is at least half on screen. Full field list: GET /api/v1/adspaces/nativeads/_schema.")
    search_settings: Optional[AdspaceCreateSearchSettings] = None
    email_settings: Optional[AdspaceCreateEmailSettings] = None
    bot_settings: Optional[AdspaceCreateBotSettings] = None
    screen_settings: Optional[AdspaceCreateScreenSettings] = None
    player_settings: Optional[Dict[str, Any]] = Field(default=None, description="Video zones (videoads, interstitial_video, videoslider). videoads also takes rewarded web ads: `rewarded` (boolean; GET /api/v1/adspaces/{id}/code then returns goCtrl's rewarded plugin plus an example button), `reward_min_seconds` (5-120, default 10), `reward_callback` (your server's http(s) URL, GET with {uid} {sid} {campaignid} {ts} {token}; anything else 422 `player_settings.reward_callback`), `reward_secret` (64 hex, generated when rewarded is switched on; the reward token is `<base64url(payload)>.<hex HMAC-SHA256(reward_secret, payload)>`, payload `<sid>.<campaignid>.<uid>.<unix time>`). CTV / streaming (videoads and audioads): `pod_size` (1-6, ads per VAST answer as an ad pod, never the same campaign or advertiser twice; a player can also send &pod=N), `pod_max_seconds` (0-600, 0 = no limit), `midroll_offsets` (up to 20 seconds into the stream, array or \"600, 1200\"; out of range 422), `vmap_no_preroll`, `vmap_postroll`, `pause_zone_id` (0 or one of your own banner zones, else 422 `player_settings.pause_zone_id`), `ssai` (allow server-side ad insertion). The player URLs are in the code answer's `ctv` block. Full field list: GET /api/v1/adspaces/videoads/_schema.")
    pop_settings: Optional[Dict[str, Any]] = Field(default=None, description="Pop zones (popads). `fpa_zoneid` is the full-page-ad zone served instead of the pop to visitors whose browser is in `bl_browsers`: 0 = none, otherwise one of YOUR OWN full-page zones (`fullpageads`, type 12) — another publisher's zone, a deleted zone or another type is refused with 422 (`pop_settings.fpa_zoneid`). Full field list: GET /api/v1/adspaces/popads/_schema.")
    fpa_settings: Optional[Dict[str, Any]] = Field(default=None, description="Full-page ad zones (fullpageads). Shown when the visitor clicks a link, before the link opens. `link_scope`: empty = any link, `internal` = vignette (only links to the same site; anything else is refused with 422 `fpa_settings.link_scope`). `start_at` / `repeat_at` count link clicks, `refreshtime` caps it to once per N seconds. Full field list: GET /api/v1/adspaces/fullpageads/_schema.")
    redirect_settings: Optional[Dict[str, Any]] = Field(default=None, description="Direct-URL zones: redirects (10), legacy types 14/15 and hard links 1-5 (35-39).")
    im_settings: Optional[Dict[str, Any]] = Field(default=None, description="In-message popup zones (impopup).")
    fixim_banner_settings: Optional[Dict[str, Any]] = Field(default=None, description="Fixed-position banner zones (fixim_banner).")
    native_bar_settings: Optional[Dict[str, Any]] = Field(default=None, description="Native bar zones (native_bar). position: top_left | top_right | left_middle | right_middle (the positions the native bar plugin draws); totalitems; topmargin (px, top positions); css. Full field list: GET /api/v1/adspaces/native_bar/_schema.")
    native_webpush_settings: Optional[Dict[str, Any]] = Field(default=None, description="Native webpush zones (native_webpush). position: top_left | top_right | center | bottom_left | bottom_right; totalitems; topmargin; css (classic card only); skin: \"\" (classic card) | chat | call | alert — the social bar styles; delay_seconds 0-120 before the first message. Other skins or delays are refused with 422. Full field list: GET /api/v1/adspaces/native_webpush/_schema.")
    text_settings: Optional[Dict[str, Any]] = Field(default=None, description="Text-list zones (textads).")
    floater_settings: Optional[Dict[str, Any]] = Field(default=None, description="Floater wrapper for interstitial-flavored zones (interstitialads, interstitial_banner, interstitial_native, interstitial_video). `trigger`: empty = as usual, `exit` = exit intent (desktop: the mouse leaves the page towards the tab bar; touch: a fast scroll back up after reading at least a screen; never in the first 5 seconds) — banner and native interstitials (17, 20, 21); anything else is refused with 422 `floater_settings.trigger`. Floating banners (bannerads with display_type 1, interstitialads) also take `anchor` (full-width bottom/top strip with a collapse tab), `refresh_seconds` (0, or 30-600 seconds on screen), `min_width` / `max_width` (screen-width range in px, 0 = no limit; e.g. side rails = left-middle / right-middle with min_width 1200) — out-of-range values are refused with 422. Full field list: GET /api/v1/adspaces/interstitial_banner/_schema.")
    videoslider_settings: Optional[Dict[str, Any]] = Field(default=None, description="Video-slider zones (videoslider).")
    invideo_settings: Optional[Dict[str, Any]] = Field(default=None, description="In-video plugin zones (invideo_plugin, type 16): roll slots, the zone each serves, pop-on-close/play. See `_schema`.")
    dyn_adsettings: Optional[Dict[str, Any]] = Field(default=None, description="Dynamic iframe zones (dyn_iframes).")
    inpage_videosettings: Optional[Dict[str, Any]] = Field(default=None, description="In-page video zones (inpage_video).")
    carousel_videosettings: Optional[Dict[str, Any]] = Field(default=None, description="Video carousel zones (video_carousel).")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "siteid", "description", "ratingid", "main_catid", "catid", "locationid", "adsizeid", "autoapprove", "isvisible", "sendmails", "useownbanners", "usealtbanner", "usecpmbuys", "allow_iframes", "allow_animation", "skip_ron_if_cpm", "no_promotion", "run_rtb_after_smartzone", "use_pixel_log", "show_about", "hidecopy", "hideadsby", "useflatbuys", "parentid", "display_type", "new_zoneid", "only_wl_campaigns", "only_tagged_campaigns", "force_wl_targeting", "skip_rtb_when_wl", "use_fixed_payouts", "fixed_payouts", "fixed_payout_data", "rtb_name", "tags", "excl_catids", "exclproperties", "use_subid_list", "subid_list", "use_domain_list", "domain_list", "use_costs", "costs_data", "use_dynamic_costs", "use_fallback_campaign", "fallback_campaignid", "quality_rank", "banner_settings", "native_settings", "search_settings", "email_settings", "bot_settings", "screen_settings", "player_settings", "pop_settings", "fpa_settings", "redirect_settings", "im_settings", "fixim_banner_settings", "native_bar_settings", "native_webpush_settings", "text_settings", "floater_settings", "videoslider_settings", "invideo_settings", "dyn_adsettings", "inpage_videosettings", "carousel_videosettings"]

    @field_validator('display_type')
    def display_type_validate_enum(cls, value):
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
        """Create an instance of AdspaceCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of banner_settings
        if self.banner_settings:
            _dict['banner_settings'] = self.banner_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_settings
        if self.search_settings:
            _dict['search_settings'] = self.search_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email_settings
        if self.email_settings:
            _dict['email_settings'] = self.email_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bot_settings
        if self.bot_settings:
            _dict['bot_settings'] = self.bot_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of screen_settings
        if self.screen_settings:
            _dict['screen_settings'] = self.screen_settings.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdspaceCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "siteid": obj.get("siteid"),
            "description": obj.get("description"),
            "ratingid": obj.get("ratingid") if obj.get("ratingid") is not None else 0,
            "main_catid": obj.get("main_catid") if obj.get("main_catid") is not None else 0,
            "catid": obj.get("catid") if obj.get("catid") is not None else 0,
            "locationid": obj.get("locationid") if obj.get("locationid") is not None else 0,
            "adsizeid": obj.get("adsizeid") if obj.get("adsizeid") is not None else 0,
            "autoapprove": obj.get("autoapprove") if obj.get("autoapprove") is not None else False,
            "isvisible": obj.get("isvisible") if obj.get("isvisible") is not None else True,
            "sendmails": obj.get("sendmails") if obj.get("sendmails") is not None else False,
            "useownbanners": obj.get("useownbanners") if obj.get("useownbanners") is not None else False,
            "usealtbanner": obj.get("usealtbanner") if obj.get("usealtbanner") is not None else False,
            "usecpmbuys": obj.get("usecpmbuys") if obj.get("usecpmbuys") is not None else True,
            "allow_iframes": obj.get("allow_iframes") if obj.get("allow_iframes") is not None else True,
            "allow_animation": obj.get("allow_animation") if obj.get("allow_animation") is not None else True,
            "skip_ron_if_cpm": obj.get("skip_ron_if_cpm") if obj.get("skip_ron_if_cpm") is not None else False,
            "no_promotion": obj.get("no_promotion") if obj.get("no_promotion") is not None else False,
            "run_rtb_after_smartzone": obj.get("run_rtb_after_smartzone") if obj.get("run_rtb_after_smartzone") is not None else False,
            "use_pixel_log": obj.get("use_pixel_log") if obj.get("use_pixel_log") is not None else False,
            "show_about": obj.get("show_about") if obj.get("show_about") is not None else False,
            "hidecopy": obj.get("hidecopy") if obj.get("hidecopy") is not None else False,
            "hideadsby": obj.get("hideadsby"),
            "useflatbuys": obj.get("useflatbuys") if obj.get("useflatbuys") is not None else True,
            "parentid": obj.get("parentid") if obj.get("parentid") is not None else 0,
            "display_type": obj.get("display_type") if obj.get("display_type") is not None else 0,
            "new_zoneid": obj.get("new_zoneid") if obj.get("new_zoneid") is not None else 0,
            "only_wl_campaigns": obj.get("only_wl_campaigns") if obj.get("only_wl_campaigns") is not None else False,
            "only_tagged_campaigns": obj.get("only_tagged_campaigns") if obj.get("only_tagged_campaigns") is not None else False,
            "force_wl_targeting": obj.get("force_wl_targeting") if obj.get("force_wl_targeting") is not None else False,
            "skip_rtb_when_wl": obj.get("skip_rtb_when_wl") if obj.get("skip_rtb_when_wl") is not None else False,
            "use_fixed_payouts": obj.get("use_fixed_payouts") if obj.get("use_fixed_payouts") is not None else False,
            "fixed_payouts": obj.get("fixed_payouts"),
            "fixed_payout_data": obj.get("fixed_payout_data"),
            "rtb_name": obj.get("rtb_name"),
            "tags": obj.get("tags"),
            "excl_catids": obj.get("excl_catids"),
            "exclproperties": obj.get("exclproperties"),
            "use_subid_list": obj.get("use_subid_list") if obj.get("use_subid_list") is not None else False,
            "subid_list": obj.get("subid_list"),
            "use_domain_list": obj.get("use_domain_list") if obj.get("use_domain_list") is not None else False,
            "domain_list": obj.get("domain_list"),
            "use_costs": obj.get("use_costs") if obj.get("use_costs") is not None else False,
            "costs_data": obj.get("costs_data"),
            "use_dynamic_costs": obj.get("use_dynamic_costs") if obj.get("use_dynamic_costs") is not None else False,
            "use_fallback_campaign": obj.get("use_fallback_campaign") if obj.get("use_fallback_campaign") is not None else False,
            "fallback_campaignid": obj.get("fallback_campaignid") if obj.get("fallback_campaignid") is not None else 0,
            "quality_rank": obj.get("quality_rank") if obj.get("quality_rank") is not None else 0,
            "banner_settings": AdspaceCreateBannerSettings.from_dict(obj["banner_settings"]) if obj.get("banner_settings") is not None else None,
            "native_settings": obj.get("native_settings"),
            "search_settings": AdspaceCreateSearchSettings.from_dict(obj["search_settings"]) if obj.get("search_settings") is not None else None,
            "email_settings": AdspaceCreateEmailSettings.from_dict(obj["email_settings"]) if obj.get("email_settings") is not None else None,
            "bot_settings": AdspaceCreateBotSettings.from_dict(obj["bot_settings"]) if obj.get("bot_settings") is not None else None,
            "screen_settings": AdspaceCreateScreenSettings.from_dict(obj["screen_settings"]) if obj.get("screen_settings") is not None else None,
            "player_settings": obj.get("player_settings"),
            "pop_settings": obj.get("pop_settings"),
            "fpa_settings": obj.get("fpa_settings"),
            "redirect_settings": obj.get("redirect_settings"),
            "im_settings": obj.get("im_settings"),
            "fixim_banner_settings": obj.get("fixim_banner_settings"),
            "native_bar_settings": obj.get("native_bar_settings"),
            "native_webpush_settings": obj.get("native_webpush_settings"),
            "text_settings": obj.get("text_settings"),
            "floater_settings": obj.get("floater_settings"),
            "videoslider_settings": obj.get("videoslider_settings"),
            "invideo_settings": obj.get("invideo_settings"),
            "dyn_adsettings": obj.get("dyn_adsettings"),
            "inpage_videosettings": obj.get("inpage_videosettings"),
            "carousel_videosettings": obj.get("carousel_videosettings")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from goadserver.models.adspace_network_binding import AdspaceNetworkBinding
from goadserver.models.adspace_site import AdspaceSite
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Adspace(BaseModel):
    """
    Full adspace record returned by `GET /api/v1/adspaces/{id}` and the create/update endpoints. Shape mirrors `AdspaceCreate` so round-trips work without translation, plus a few read-only identity fields (`id`, `uniq_name`, `adspace_type`, `is_active`, `date_added`, `time_changed`) and the parsed `json_settings`. 
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    uniq_name: Optional[StrictStr] = Field(default=None, description="MD5 of (name, type, system, site) — internal dedupe key.")
    site: Optional[AdspaceSite] = None
    siteid: Optional[StrictInt] = None
    adspace_type: Optional[StrictStr] = Field(default=None, description="Type config key (e.g. bannerads).")
    adzone_typeid: Optional[StrictInt] = None
    adtype_id: Optional[StrictInt] = None
    ad_type: Optional[StrictInt] = Field(default=None, description="Backward-compat alias for adtype_id.")
    adsizeid: Optional[StrictInt] = None
    display_type: Optional[StrictInt] = None
    ratingid: Optional[StrictInt] = None
    main_catid: Optional[StrictInt] = None
    catid: Optional[StrictInt] = None
    locationid: Optional[StrictInt] = None
    quality_rank: Optional[StrictInt] = None
    is_active: Optional[StrictBool] = Field(default=None, description="Derived from publisher_adzones.isinuse — true when at least one campaign-spot link exists.")
    autoapprove: Optional[StrictBool] = None
    isvisible: Optional[StrictBool] = None
    sendmails: Optional[StrictBool] = None
    useownbanners: Optional[StrictBool] = None
    usealtbanner: Optional[StrictBool] = None
    usecpmbuys: Optional[StrictBool] = None
    allow_iframes: Optional[StrictBool] = None
    allow_animation: Optional[StrictBool] = None
    run_rtb_after_smartzone: Optional[StrictBool] = None
    use_pixel_log: Optional[StrictBool] = None
    show_about: Optional[StrictBool] = None
    skip_ron_if_cpm: Optional[StrictBool] = None
    no_promotion: Optional[StrictBool] = None
    hidecopy: Optional[StrictBool] = None
    use_subid_list: Optional[StrictBool] = None
    subid_list: Optional[StrictStr] = None
    use_domain_list: Optional[StrictBool] = None
    domain_list: Optional[List[StrictStr]] = None
    use_costs: Optional[StrictBool] = None
    costs_data: Optional[Dict[str, Any]] = None
    use_dynamic_costs: Optional[StrictBool] = None
    use_fixed_payouts: Optional[StrictBool] = None
    fixed_payout_data: Optional[Dict[str, Any]] = None
    use_fallback_campaign: Optional[StrictBool] = None
    fallback_campaignid: Optional[StrictInt] = None
    excl_catids: Optional[StrictStr] = None
    exclproperties: Optional[StrictStr] = None
    tags: Optional[List[StrictInt]] = None
    rtb_name: Optional[StrictStr] = None
    date_added: Optional[datetime] = None
    time_changed: Optional[StrictInt] = Field(default=None, description="Unix seconds of last update.")
    useflatbuys: Optional[StrictBool] = None
    only_wl_campaigns: Optional[StrictBool] = None
    only_tagged_campaigns: Optional[StrictBool] = None
    force_wl_targeting: Optional[StrictBool] = None
    skip_rtb_when_wl: Optional[StrictBool] = Field(default=None, description="From json_settings.options.")
    parentid: Optional[StrictInt] = None
    new_zoneid: Optional[StrictInt] = None
    network_binding: Optional[AdspaceNetworkBinding] = None
    json_settings: Optional[Dict[str, Any]] = Field(default=None, description="Raw assembled blob — unioned hoisted to top level for convenience.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "description", "uniq_name", "site", "siteid", "adspace_type", "adzone_typeid", "adtype_id", "ad_type", "adsizeid", "display_type", "ratingid", "main_catid", "catid", "locationid", "quality_rank", "is_active", "autoapprove", "isvisible", "sendmails", "useownbanners", "usealtbanner", "usecpmbuys", "allow_iframes", "allow_animation", "run_rtb_after_smartzone", "use_pixel_log", "show_about", "skip_ron_if_cpm", "no_promotion", "hidecopy", "use_subid_list", "subid_list", "use_domain_list", "domain_list", "use_costs", "costs_data", "use_dynamic_costs", "use_fixed_payouts", "fixed_payout_data", "use_fallback_campaign", "fallback_campaignid", "excl_catids", "exclproperties", "tags", "rtb_name", "date_added", "time_changed", "useflatbuys", "only_wl_campaigns", "only_tagged_campaigns", "force_wl_targeting", "skip_rtb_when_wl", "parentid", "new_zoneid", "network_binding", "json_settings"]

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
        """Create an instance of Adspace from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of site
        if self.site:
            _dict['site'] = self.site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_binding
        if self.network_binding:
            _dict['network_binding'] = self.network_binding.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Adspace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "uniq_name": obj.get("uniq_name"),
            "site": AdspaceSite.from_dict(obj["site"]) if obj.get("site") is not None else None,
            "siteid": obj.get("siteid"),
            "adspace_type": obj.get("adspace_type"),
            "adzone_typeid": obj.get("adzone_typeid"),
            "adtype_id": obj.get("adtype_id"),
            "ad_type": obj.get("ad_type"),
            "adsizeid": obj.get("adsizeid"),
            "display_type": obj.get("display_type"),
            "ratingid": obj.get("ratingid"),
            "main_catid": obj.get("main_catid"),
            "catid": obj.get("catid"),
            "locationid": obj.get("locationid"),
            "quality_rank": obj.get("quality_rank"),
            "is_active": obj.get("is_active"),
            "autoapprove": obj.get("autoapprove"),
            "isvisible": obj.get("isvisible"),
            "sendmails": obj.get("sendmails"),
            "useownbanners": obj.get("useownbanners"),
            "usealtbanner": obj.get("usealtbanner"),
            "usecpmbuys": obj.get("usecpmbuys"),
            "allow_iframes": obj.get("allow_iframes"),
            "allow_animation": obj.get("allow_animation"),
            "run_rtb_after_smartzone": obj.get("run_rtb_after_smartzone"),
            "use_pixel_log": obj.get("use_pixel_log"),
            "show_about": obj.get("show_about"),
            "skip_ron_if_cpm": obj.get("skip_ron_if_cpm"),
            "no_promotion": obj.get("no_promotion"),
            "hidecopy": obj.get("hidecopy"),
            "use_subid_list": obj.get("use_subid_list"),
            "subid_list": obj.get("subid_list"),
            "use_domain_list": obj.get("use_domain_list"),
            "domain_list": obj.get("domain_list"),
            "use_costs": obj.get("use_costs"),
            "costs_data": obj.get("costs_data"),
            "use_dynamic_costs": obj.get("use_dynamic_costs"),
            "use_fixed_payouts": obj.get("use_fixed_payouts"),
            "fixed_payout_data": obj.get("fixed_payout_data"),
            "use_fallback_campaign": obj.get("use_fallback_campaign"),
            "fallback_campaignid": obj.get("fallback_campaignid"),
            "excl_catids": obj.get("excl_catids"),
            "exclproperties": obj.get("exclproperties"),
            "tags": obj.get("tags"),
            "rtb_name": obj.get("rtb_name"),
            "date_added": obj.get("date_added"),
            "time_changed": obj.get("time_changed"),
            "useflatbuys": obj.get("useflatbuys"),
            "only_wl_campaigns": obj.get("only_wl_campaigns"),
            "only_tagged_campaigns": obj.get("only_tagged_campaigns"),
            "force_wl_targeting": obj.get("force_wl_targeting"),
            "skip_rtb_when_wl": obj.get("skip_rtb_when_wl"),
            "parentid": obj.get("parentid"),
            "new_zoneid": obj.get("new_zoneid"),
            "network_binding": AdspaceNetworkBinding.from_dict(obj["network_binding"]) if obj.get("network_binding") is not None else None,
            "json_settings": obj.get("json_settings")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



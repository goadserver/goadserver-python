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
from goadserver.models.media_buying_policy_test_phase import MediaBuyingPolicyTestPhase
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MediaBuyingPolicy(BaseModel):
    """
    The buying policy of one ad zone (docs/MEDIA_BUYING.md). On PUT every field is optional: a field left out keeps its stored value; out-of-range values are clamped. Nothing scheduled acts on the zone until `enabled` is true.
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=None, description="The zone's master switch. Off (the default): no scheduled job acts on the zone whatever the modes say; the report and your own actions still work.")
    mode: Optional[StrictStr] = Field(default=None, description="off | advise | auto")
    zone_slot: Optional[StrictStr] = Field(default=None, description="Stats slot holding the source zone id")
    revenue_metric: Optional[StrictStr] = Field(default=None, description="paid | earned")
    window_days: Optional[StrictInt] = Field(default=None, description="Days judged, 1-30")
    min_spend: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Judge a zone only after this cost (main currency)")
    min_volume: Optional[StrictInt] = Field(default=None, description="Judge a zone only after this much traffic too (clicks or impressions, per ad type).")
    target_margin_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Block below this margin; null = not used")
    max_cpa: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Block above this cost per conversion; null = not used")
    max_blocks_per_day: Optional[StrictInt] = Field(default=None, description="Auto mode: blocks the policy may apply per day")
    judging: Optional[StrictStr] = Field(default=None, description="fixed | confidence")
    confidence_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="70-99")
    pooling: Optional[StrictStr] = Field(default=None, description="off | buy | country")
    pool_strength: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The group counts as this many paid events, 0-20")
    ip_preblock_mode: Optional[StrictStr] = Field(default=None, description="off | advise | auto")
    ip_preblock_hosting: Optional[StrictBool] = Field(default=None, description="Also data centre / VPN ranges and ASNs")
    ip_preblock_max: Optional[StrictInt] = Field(default=None, description="Entries on the list, 1-1000")
    ip_preblock_ttl_days: Optional[StrictInt] = Field(default=None, description="Take an entry off after this many days unseen")
    attribution: Optional[StrictStr] = Field(default=None, description="Which day a conversion's revenue counts on: `conversion` (the day it arrives, default) | `click` (the day of the visit that led to it; needs the source id in subid).")
    report: Optional[StrictStr] = Field(default=None, description="`off` | `daily` (08:00 tenant time) | `weekly` (Mondays 08:00) report by email / Telegram / Slack and the `media_buying.report` event.")
    min_delivery_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Block below this % delivered; null = off")
    min_network_count: Optional[StrictInt] = Field(default=None, description="Judge delivery only after this many network impressions/clicks")
    max_offgeo_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Block a zone whose visitors come from outside the campaign's countries more than this share; null = off.")
    min_geo_volume: Optional[StrictInt] = Field(default=None, description="Judge geo only after this many visits (or clicks)")
    budget_reserve_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Goadserver: stop buying when a linked campaign has < this % of its day budget left")
    min_switch_minutes: Optional[StrictInt] = Field(default=None, description="Goadserver: no re-activation within this many minutes of the last switch")
    max_daily_source_spend: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Hold the source once today's external cost reaches this")
    stop_loss: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Hold the source once today's profit on the adzone is below -this")
    bid_mode: Optional[StrictStr] = Field(default=None, description="off | advise | auto (auto only on networks with absolute bids)")
    bid_step_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Size of one change, 1-30 %")
    bid_band_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Margin dead-zone around the target, in points")
    bid_min_spend: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Judge only once the window cost reaches this")
    min_bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never lower below (network bid units)")
    max_bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never raise above; no raise at all without it")
    bid_cooldown_hours: Optional[StrictInt] = Field(default=None, description="At most one change (or open proposal) per this many hours")
    agent_mode: Optional[StrictStr] = Field(default=None, description="off | advise | auto")
    agent_every_hours: Optional[StrictInt] = Field(default=None, description="Legacy: the agent interval in hours; read only when agent_every_minutes is unset.")
    agent_every_minutes: Optional[StrictInt] = Field(default=None, description="How often the buying agent reviews the zone, 15-10080 minutes.")
    agent_interval_auto: Optional[StrictBool] = Field(default=None, description="Pick the agent interval from the zone's traffic instead of agent_every_minutes.")
    agent_max_actions: Optional[StrictInt] = Field(default=None, description="Actions kept per run, 1-50")
    agent_notes: Optional[StrictStr] = Field(default=None, description="The buyer's own instructions, max 1000 characters")
    control_for: Optional[StrictInt] = Field(default=None, description="Make this buy the untouched control of buy N (another of your connected ad zones / tracking links), e.g. a campaign left to the network's own optimiser: saving it switches `enabled` off. 0 = not a control. Compare the two with GET …/media-buying/compare.")
    start_preset: Optional[StrictStr] = Field(default=None, description="Set by a launch with `preset`: the zone switches on with this preset when the network approves the campaign, then it is cleared. An unknown value is dropped.")
    test_phase: Optional[MediaBuyingPolicyTestPhase] = None
    budget_mode: Optional[StrictStr] = Field(default=None, description="Network daily budget (level E): off | advise | auto. Decided once a day; written only where the network has a budget API.")
    budget_headroom_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Added on top of the computed network budget, 0-100 %")
    min_network_budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never set the network budget below this (network currency); null = no floor")
    max_network_budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never set the network budget above this (network currency); null = no ceiling")
    budget_pace_hours: Optional[StrictInt] = Field(default=None, description="Even pacing: spread the day budget over at least this many hours — the network's hourly budget is set to day budget / hours, in the same update as the daily budget (networks with `supports_hourly_budget` in the overview, today Adsterra). 0 = off (default), else 4-24. Switching it off leaves the network's hourly budget as it is.")
    segment_mode: Optional[StrictStr] = Field(default=None, description="Segment exclusions (levels B/C): off | advise | auto")
    segment_min_spend: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Judge a segment only after this cost (main currency); estimated segments need twice this")
    segment_window_days: Optional[StrictInt] = Field(default=None, description="Full days a segment is judged on, 3-28 (weekday: always 28)")
    mirror_advertiser_blocks: Optional[StrictBool] = Field(default=None, description="When the zone feeds exactly one campaign and its source ids arrive as subid: subids that campaign's advertiser blocks are blocked at the network too.")
    zone_bid_mode: Optional[StrictStr] = Field(default=None, description="off | advise | auto")
    zone_bid_step_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Size of one change, 1-30 %")
    zone_bid_band_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Margin band above the target, in points")
    zone_bid_floor_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never below this % of the country base bid")
    zone_bid_ceiling_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Never above this % of the country base bid")
    inherit_blocks: Optional[Dict[str, Any]] = Field(default=None, description="Set by an ad zone clone: a pending carry-over of another zone's blocks (`from`, `kind`, `done`). Read-only; send it back unchanged or leave it out.")
    __properties: ClassVar[List[str]] = ["enabled", "mode", "zone_slot", "revenue_metric", "window_days", "min_spend", "min_volume", "target_margin_pct", "max_cpa", "max_blocks_per_day", "judging", "confidence_pct", "pooling", "pool_strength", "ip_preblock_mode", "ip_preblock_hosting", "ip_preblock_max", "ip_preblock_ttl_days", "attribution", "report", "min_delivery_pct", "min_network_count", "max_offgeo_pct", "min_geo_volume", "budget_reserve_pct", "min_switch_minutes", "max_daily_source_spend", "stop_loss", "bid_mode", "bid_step_pct", "bid_band_pct", "bid_min_spend", "min_bid", "max_bid", "bid_cooldown_hours", "agent_mode", "agent_every_hours", "agent_every_minutes", "agent_interval_auto", "agent_max_actions", "agent_notes", "control_for", "start_preset", "test_phase", "budget_mode", "budget_headroom_pct", "min_network_budget", "max_network_budget", "budget_pace_hours", "segment_mode", "segment_min_spend", "segment_window_days", "mirror_advertiser_blocks", "zone_bid_mode", "zone_bid_step_pct", "zone_bid_band_pct", "zone_bid_floor_pct", "zone_bid_ceiling_pct", "inherit_blocks"]

    @field_validator('start_preset')
    def start_preset_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['conservative', 'balanced', 'aggressive']):
            raise ValueError("must be one of enum values ('conservative', 'balanced', 'aggressive')")
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
        """Create an instance of MediaBuyingPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "inherit_blocks",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of test_phase
        if self.test_phase:
            _dict['test_phase'] = self.test_phase.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaBuyingPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabled": obj.get("enabled"),
            "mode": obj.get("mode"),
            "zone_slot": obj.get("zone_slot"),
            "revenue_metric": obj.get("revenue_metric"),
            "window_days": obj.get("window_days"),
            "min_spend": obj.get("min_spend"),
            "min_volume": obj.get("min_volume"),
            "target_margin_pct": obj.get("target_margin_pct"),
            "max_cpa": obj.get("max_cpa"),
            "max_blocks_per_day": obj.get("max_blocks_per_day"),
            "judging": obj.get("judging"),
            "confidence_pct": obj.get("confidence_pct"),
            "pooling": obj.get("pooling"),
            "pool_strength": obj.get("pool_strength"),
            "ip_preblock_mode": obj.get("ip_preblock_mode"),
            "ip_preblock_hosting": obj.get("ip_preblock_hosting"),
            "ip_preblock_max": obj.get("ip_preblock_max"),
            "ip_preblock_ttl_days": obj.get("ip_preblock_ttl_days"),
            "attribution": obj.get("attribution"),
            "report": obj.get("report"),
            "min_delivery_pct": obj.get("min_delivery_pct"),
            "min_network_count": obj.get("min_network_count"),
            "max_offgeo_pct": obj.get("max_offgeo_pct"),
            "min_geo_volume": obj.get("min_geo_volume"),
            "budget_reserve_pct": obj.get("budget_reserve_pct"),
            "min_switch_minutes": obj.get("min_switch_minutes"),
            "max_daily_source_spend": obj.get("max_daily_source_spend"),
            "stop_loss": obj.get("stop_loss"),
            "bid_mode": obj.get("bid_mode"),
            "bid_step_pct": obj.get("bid_step_pct"),
            "bid_band_pct": obj.get("bid_band_pct"),
            "bid_min_spend": obj.get("bid_min_spend"),
            "min_bid": obj.get("min_bid"),
            "max_bid": obj.get("max_bid"),
            "bid_cooldown_hours": obj.get("bid_cooldown_hours"),
            "agent_mode": obj.get("agent_mode"),
            "agent_every_hours": obj.get("agent_every_hours"),
            "agent_every_minutes": obj.get("agent_every_minutes"),
            "agent_interval_auto": obj.get("agent_interval_auto"),
            "agent_max_actions": obj.get("agent_max_actions"),
            "agent_notes": obj.get("agent_notes"),
            "control_for": obj.get("control_for"),
            "start_preset": obj.get("start_preset"),
            "test_phase": MediaBuyingPolicyTestPhase.from_dict(obj["test_phase"]) if obj.get("test_phase") is not None else None,
            "budget_mode": obj.get("budget_mode"),
            "budget_headroom_pct": obj.get("budget_headroom_pct"),
            "min_network_budget": obj.get("min_network_budget"),
            "max_network_budget": obj.get("max_network_budget"),
            "budget_pace_hours": obj.get("budget_pace_hours"),
            "segment_mode": obj.get("segment_mode"),
            "segment_min_spend": obj.get("segment_min_spend"),
            "segment_window_days": obj.get("segment_window_days"),
            "mirror_advertiser_blocks": obj.get("mirror_advertiser_blocks"),
            "zone_bid_mode": obj.get("zone_bid_mode"),
            "zone_bid_step_pct": obj.get("zone_bid_step_pct"),
            "zone_bid_band_pct": obj.get("zone_bid_band_pct"),
            "zone_bid_floor_pct": obj.get("zone_bid_floor_pct"),
            "zone_bid_ceiling_pct": obj.get("zone_bid_ceiling_pct"),
            "inherit_blocks": obj.get("inherit_blocks")
        })
        return _obj



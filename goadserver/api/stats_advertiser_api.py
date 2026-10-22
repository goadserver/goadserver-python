"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated
from goadserver.models.stats_response import StatsResponse

from goadserver.api_client import ApiClient, RequestSerialized
from goadserver.api_response import ApiResponse
from goadserver.rest import RESTResponseType


class StatsAdvertiserApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_v1_advertiser_stats_get(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. ")] = None,
        filter_campaign_id: Annotated[Optional[StrictStr], Field(description="Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.")] = None,
        filter_ad_id: Annotated[Optional[StrictStr], Field(description="Ad ID, or a comma-separated list.")] = None,
        filter_tag_id: Annotated[Optional[StrictStr], Field(description="Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. ")] = None,
        filter_ad_type: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. ")] = None,
        filter_selling_type: Annotated[Optional[StrictStr], Field(description="Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) ")] = None,
        filter_adzone_type: Annotated[Optional[StrictStr], Field(description="Adzone (placement) type id, or a comma-separated list.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_site_id: Annotated[Optional[StrictStr], Field(description="Comma-separated site IDs. Look up via `GET /api/v1/sites`.")] = None,
        filter_network_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="RTB network ID.")] = None,
        filter_bidruleset_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).")] = None,
        filter_bidrule_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid rule ID inside a ruleset — only traffic that rule priced.")] = None,
        filter_creative_pool_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool ID.")] = None,
        filter_creative_pool_ad_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool item ID.")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. ")] = None,
        min: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. ")] = None,
        max: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.")] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` turns an unknown metric name into a 422 instead of ignoring it.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StatsResponse:
        """Display, native and CPM/RON campaign stats.

        Aggregated performance for the advertiser's campaigns. Pick the dimensions to group by, the metrics you want returned, and any filters — the form below auto-builds the query.  The numbers are the panel's Stats screen numbers: the same aggregate and the same formulas (revenue, profit, ROI, CPA, CR, eCPC, traffic cost and the bot breakdown included), over `userstats_daily` (or `userstats_daily_details` when a grouped dimension or filter needs it).  **Money unit:** every money metric (`paid`, `cpm_paid`, `cpc_paid`, `ecpm`, `ecpc`, `conv_*_earned`, `revenue`, `profit`, `cpa`, `traffic_cost`) is in the account currency's **main unit** (dollars/euros, not cents), rounded to 4 decimals. `ctr`, `cr`, `roi` and the `bot_*_pct` metrics are percentages.  **Dates:** `from` and `to` are used only when *both* are given and valid; otherwise the range is the last 7 days ending today (a lone `from` is ignored). Max range 92 days.  A key made by a team member whose role is limited to their own campaigns sees only those campaigns, as in the panel. A key pinned to campaigns sees only those campaigns.  **Several values:** `filter[ad_type]`, `filter[device]` and `filter[country]` also take a comma-separated list (`filter[country]=NL,DE`), matching any of them — the panel's multi-select filters send the same. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. 
        :type group_by: List[str]
        :param metrics: Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. 
        :type metrics: List[str]
        :param filter_campaign_id: Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.
        :type filter_campaign_id: str
        :param filter_ad_id: Ad ID, or a comma-separated list.
        :type filter_ad_id: str
        :param filter_tag_id: Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. 
        :type filter_tag_id: str
        :param filter_ad_type: Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. 
        :type filter_ad_type: int
        :param filter_selling_type: Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) 
        :type filter_selling_type: str
        :param filter_adzone_type: Adzone (placement) type id, or a comma-separated list.
        :type filter_adzone_type: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_site_id: Comma-separated site IDs. Look up via `GET /api/v1/sites`.
        :type filter_site_id: str
        :param filter_network_id: RTB network ID.
        :type filter_network_id: int
        :param filter_bidruleset_id: Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).
        :type filter_bidruleset_id: int
        :param filter_bidrule_id: Bid rule ID inside a ruleset — only traffic that rule priced.
        :type filter_bidrule_id: int
        :param filter_creative_pool_id: Creative pool ID.
        :type filter_creative_pool_id: int
        :param filter_creative_pool_ad_id: Creative pool item ID.
        :type filter_creative_pool_ad_id: int
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. 
        :type sort: str
        :param min: Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. 
        :type min: Dict[str, float]
        :param max: Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.
        :type max: Dict[str, float]
        :param strict: `1` turns an unknown metric name into a 422 instead of ignoring it.
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_advertiser_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_campaign_id=filter_campaign_id,
            filter_ad_id=filter_ad_id,
            filter_tag_id=filter_tag_id,
            filter_ad_type=filter_ad_type,
            filter_selling_type=filter_selling_type,
            filter_adzone_type=filter_adzone_type,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_adzone_id=filter_adzone_id,
            filter_site_id=filter_site_id,
            filter_network_id=filter_network_id,
            filter_bidruleset_id=filter_bidruleset_id,
            filter_bidrule_id=filter_bidrule_id,
            filter_creative_pool_id=filter_creative_pool_id,
            filter_creative_pool_ad_id=filter_creative_pool_ad_id,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            min=min,
            max=max,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
            '401': "Error",
            '403': "Error",
            '422': None,
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_advertiser_stats_get_with_http_info(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. ")] = None,
        filter_campaign_id: Annotated[Optional[StrictStr], Field(description="Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.")] = None,
        filter_ad_id: Annotated[Optional[StrictStr], Field(description="Ad ID, or a comma-separated list.")] = None,
        filter_tag_id: Annotated[Optional[StrictStr], Field(description="Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. ")] = None,
        filter_ad_type: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. ")] = None,
        filter_selling_type: Annotated[Optional[StrictStr], Field(description="Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) ")] = None,
        filter_adzone_type: Annotated[Optional[StrictStr], Field(description="Adzone (placement) type id, or a comma-separated list.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_site_id: Annotated[Optional[StrictStr], Field(description="Comma-separated site IDs. Look up via `GET /api/v1/sites`.")] = None,
        filter_network_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="RTB network ID.")] = None,
        filter_bidruleset_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).")] = None,
        filter_bidrule_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid rule ID inside a ruleset — only traffic that rule priced.")] = None,
        filter_creative_pool_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool ID.")] = None,
        filter_creative_pool_ad_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool item ID.")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. ")] = None,
        min: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. ")] = None,
        max: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.")] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` turns an unknown metric name into a 422 instead of ignoring it.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StatsResponse]:
        """Display, native and CPM/RON campaign stats.

        Aggregated performance for the advertiser's campaigns. Pick the dimensions to group by, the metrics you want returned, and any filters — the form below auto-builds the query.  The numbers are the panel's Stats screen numbers: the same aggregate and the same formulas (revenue, profit, ROI, CPA, CR, eCPC, traffic cost and the bot breakdown included), over `userstats_daily` (or `userstats_daily_details` when a grouped dimension or filter needs it).  **Money unit:** every money metric (`paid`, `cpm_paid`, `cpc_paid`, `ecpm`, `ecpc`, `conv_*_earned`, `revenue`, `profit`, `cpa`, `traffic_cost`) is in the account currency's **main unit** (dollars/euros, not cents), rounded to 4 decimals. `ctr`, `cr`, `roi` and the `bot_*_pct` metrics are percentages.  **Dates:** `from` and `to` are used only when *both* are given and valid; otherwise the range is the last 7 days ending today (a lone `from` is ignored). Max range 92 days.  A key made by a team member whose role is limited to their own campaigns sees only those campaigns, as in the panel. A key pinned to campaigns sees only those campaigns.  **Several values:** `filter[ad_type]`, `filter[device]` and `filter[country]` also take a comma-separated list (`filter[country]=NL,DE`), matching any of them — the panel's multi-select filters send the same. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. 
        :type group_by: List[str]
        :param metrics: Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. 
        :type metrics: List[str]
        :param filter_campaign_id: Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.
        :type filter_campaign_id: str
        :param filter_ad_id: Ad ID, or a comma-separated list.
        :type filter_ad_id: str
        :param filter_tag_id: Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. 
        :type filter_tag_id: str
        :param filter_ad_type: Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. 
        :type filter_ad_type: int
        :param filter_selling_type: Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) 
        :type filter_selling_type: str
        :param filter_adzone_type: Adzone (placement) type id, or a comma-separated list.
        :type filter_adzone_type: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_site_id: Comma-separated site IDs. Look up via `GET /api/v1/sites`.
        :type filter_site_id: str
        :param filter_network_id: RTB network ID.
        :type filter_network_id: int
        :param filter_bidruleset_id: Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).
        :type filter_bidruleset_id: int
        :param filter_bidrule_id: Bid rule ID inside a ruleset — only traffic that rule priced.
        :type filter_bidrule_id: int
        :param filter_creative_pool_id: Creative pool ID.
        :type filter_creative_pool_id: int
        :param filter_creative_pool_ad_id: Creative pool item ID.
        :type filter_creative_pool_ad_id: int
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. 
        :type sort: str
        :param min: Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. 
        :type min: Dict[str, float]
        :param max: Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.
        :type max: Dict[str, float]
        :param strict: `1` turns an unknown metric name into a 422 instead of ignoring it.
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_advertiser_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_campaign_id=filter_campaign_id,
            filter_ad_id=filter_ad_id,
            filter_tag_id=filter_tag_id,
            filter_ad_type=filter_ad_type,
            filter_selling_type=filter_selling_type,
            filter_adzone_type=filter_adzone_type,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_adzone_id=filter_adzone_id,
            filter_site_id=filter_site_id,
            filter_network_id=filter_network_id,
            filter_bidruleset_id=filter_bidruleset_id,
            filter_bidrule_id=filter_bidrule_id,
            filter_creative_pool_id=filter_creative_pool_id,
            filter_creative_pool_ad_id=filter_creative_pool_ad_id,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            min=min,
            max=max,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
            '401': "Error",
            '403': "Error",
            '422': None,
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_advertiser_stats_get_without_preload_content(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. ")] = None,
        filter_campaign_id: Annotated[Optional[StrictStr], Field(description="Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.")] = None,
        filter_ad_id: Annotated[Optional[StrictStr], Field(description="Ad ID, or a comma-separated list.")] = None,
        filter_tag_id: Annotated[Optional[StrictStr], Field(description="Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. ")] = None,
        filter_ad_type: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. ")] = None,
        filter_selling_type: Annotated[Optional[StrictStr], Field(description="Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) ")] = None,
        filter_adzone_type: Annotated[Optional[StrictStr], Field(description="Adzone (placement) type id, or a comma-separated list.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_site_id: Annotated[Optional[StrictStr], Field(description="Comma-separated site IDs. Look up via `GET /api/v1/sites`.")] = None,
        filter_network_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="RTB network ID.")] = None,
        filter_bidruleset_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).")] = None,
        filter_bidrule_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Bid rule ID inside a ruleset — only traffic that rule priced.")] = None,
        filter_creative_pool_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool ID.")] = None,
        filter_creative_pool_ad_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Creative pool item ID.")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. ")] = None,
        min: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. ")] = None,
        max: Annotated[Optional[Dict[str, Dict[str, Union[StrictFloat, StrictInt]]]], Field(description="Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.")] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` turns an unknown metric name into a 422 instead of ignoring it.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Display, native and CPM/RON campaign stats.

        Aggregated performance for the advertiser's campaigns. Pick the dimensions to group by, the metrics you want returned, and any filters — the form below auto-builds the query.  The numbers are the panel's Stats screen numbers: the same aggregate and the same formulas (revenue, profit, ROI, CPA, CR, eCPC, traffic cost and the bot breakdown included), over `userstats_daily` (or `userstats_daily_details` when a grouped dimension or filter needs it).  **Money unit:** every money metric (`paid`, `cpm_paid`, `cpc_paid`, `ecpm`, `ecpc`, `conv_*_earned`, `revenue`, `profit`, `cpa`, `traffic_cost`) is in the account currency's **main unit** (dollars/euros, not cents), rounded to 4 decimals. `ctr`, `cr`, `roi` and the `bot_*_pct` metrics are percentages.  **Dates:** `from` and `to` are used only when *both* are given and valid; otherwise the range is the last 7 days ending today (a lone `from` is ignored). Max range 92 days.  A key made by a team member whose role is limited to their own campaigns sees only those campaigns, as in the panel. A key pinned to campaigns sees only those campaigns.  **Several values:** `filter[ad_type]`, `filter[device]` and `filter[country]` also take a comma-separated list (`filter[country]=NL,DE`), matching any of them — the panel's multi-select filters send the same. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id. 
        :type group_by: List[str]
        :param metrics: Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422. 
        :type metrics: List[str]
        :param filter_campaign_id: Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`.
        :type filter_campaign_id: str
        :param filter_ad_id: Ad ID, or a comma-separated list.
        :type filter_ad_id: str
        :param filter_tag_id: Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing. 
        :type filter_tag_id: str
        :param filter_ad_type: Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system. 
        :type filter_ad_type: int
        :param filter_selling_type: Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.) 
        :type filter_selling_type: str
        :param filter_adzone_type: Adzone (placement) type id, or a comma-separated list.
        :type filter_adzone_type: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_site_id: Comma-separated site IDs. Look up via `GET /api/v1/sites`.
        :type filter_site_id: str
        :param filter_network_id: RTB network ID.
        :type filter_network_id: int
        :param filter_bidruleset_id: Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`).
        :type filter_bidruleset_id: int
        :param filter_bidrule_id: Bid rule ID inside a ruleset — only traffic that rule priced.
        :type filter_bidrule_id: int
        :param filter_creative_pool_id: Creative pool ID.
        :type filter_creative_pool_id: int
        :param filter_creative_pool_ad_id: Creative pool item ID.
        :type filter_creative_pool_ad_id: int
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`. 
        :type sort: str
        :param min: Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422. 
        :type min: Dict[str, float]
        :param max: Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`.
        :type max: Dict[str, float]
        :param strict: `1` turns an unknown metric name into a 422 instead of ignoring it.
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_advertiser_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_campaign_id=filter_campaign_id,
            filter_ad_id=filter_ad_id,
            filter_tag_id=filter_tag_id,
            filter_ad_type=filter_ad_type,
            filter_selling_type=filter_selling_type,
            filter_adzone_type=filter_adzone_type,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_adzone_id=filter_adzone_id,
            filter_site_id=filter_site_id,
            filter_network_id=filter_network_id,
            filter_bidruleset_id=filter_bidruleset_id,
            filter_bidrule_id=filter_bidrule_id,
            filter_creative_pool_id=filter_creative_pool_id,
            filter_creative_pool_ad_id=filter_creative_pool_ad_id,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            min=min,
            max=max,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
            '401': "Error",
            '403': "Error",
            '422': None,
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_advertiser_stats_get_serialize(
        self,
        var_from,
        to,
        interval,
        group_by,
        metrics,
        filter_campaign_id,
        filter_ad_id,
        filter_tag_id,
        filter_ad_type,
        filter_selling_type,
        filter_adzone_type,
        filter_device,
        filter_country,
        filter_adzone_id,
        filter_site_id,
        filter_network_id,
        filter_bidruleset_id,
        filter_bidrule_id,
        filter_creative_pool_id,
        filter_creative_pool_ad_id,
        format,
        page,
        per_page,
        sort,
        min,
        max,
        strict,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'group_by': 'csv',
            'metrics': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if var_from is not None:
            if isinstance(var_from, date):
                _query_params.append(
                    (
                        'from',
                        var_from.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('from', var_from))
            
        if to is not None:
            if isinstance(to, date):
                _query_params.append(
                    (
                        'to',
                        to.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('to', to))
            
        if interval is not None:
            
            _query_params.append(('interval', interval))
            
        if group_by is not None:
            
            _query_params.append(('group_by', group_by))
            
        if metrics is not None:
            
            _query_params.append(('metrics', metrics))
            
        if filter_campaign_id is not None:
            
            _query_params.append(('filter[campaign_id]', filter_campaign_id))
            
        if filter_ad_id is not None:
            
            _query_params.append(('filter[ad_id]', filter_ad_id))
            
        if filter_tag_id is not None:
            
            _query_params.append(('filter[tag_id]', filter_tag_id))
            
        if filter_ad_type is not None:
            
            _query_params.append(('filter[ad_type]', filter_ad_type))
            
        if filter_selling_type is not None:
            
            _query_params.append(('filter[selling_type]', filter_selling_type))
            
        if filter_adzone_type is not None:
            
            _query_params.append(('filter[adzone_type]', filter_adzone_type))
            
        if filter_device is not None:
            
            _query_params.append(('filter[device]', filter_device))
            
        if filter_country is not None:
            
            _query_params.append(('filter[country]', filter_country))
            
        if filter_adzone_id is not None:
            
            _query_params.append(('filter[adzone_id]', filter_adzone_id))
            
        if filter_site_id is not None:
            
            _query_params.append(('filter[site_id]', filter_site_id))
            
        if filter_network_id is not None:
            
            _query_params.append(('filter[network_id]', filter_network_id))
            
        if filter_bidruleset_id is not None:
            
            _query_params.append(('filter[bidruleset_id]', filter_bidruleset_id))
            
        if filter_bidrule_id is not None:
            
            _query_params.append(('filter[bidrule_id]', filter_bidrule_id))
            
        if filter_creative_pool_id is not None:
            
            _query_params.append(('filter[creative_pool_id]', filter_creative_pool_id))
            
        if filter_creative_pool_ad_id is not None:
            
            _query_params.append(('filter[creative_pool_ad_id]', filter_creative_pool_ad_id))
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if min is not None:
            
            _query_params.append(('min', min))
            
        if max is not None:
            
            _query_params.append(('max', max))
            
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/advertiser/stats',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



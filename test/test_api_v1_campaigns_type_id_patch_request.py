# coding: utf-8

"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from goadserver.models.api_v1_campaigns_type_id_patch_request import ApiV1CampaignsTypeIdPatchRequest

class TestApiV1CampaignsTypeIdPatchRequest(unittest.TestCase):
    """ApiV1CampaignsTypeIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1CampaignsTypeIdPatchRequest:
        """Test ApiV1CampaignsTypeIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1CampaignsTypeIdPatchRequest`
        """
        model = ApiV1CampaignsTypeIdPatchRequest()
        if include_optional:
            return ApiV1CampaignsTypeIdPatchRequest(
                groupid = '3,7',
                display_options = '7',
                min_rank = 56,
                fx_rating = 56,
                mail_campaign_budget = True,
                use_dynamic_costs = True,
                dynamic_costs_increase = 0,
                conversion_capping = goadserver.models.campaign_panel_fields_conversion_capping.CampaignPanelFields_conversion_capping(
                    inuse = True, 
                    conv_type = 56, 
                    cap_type = 'daily', 
                    max = 56, ),
                fix_cpa = 0,
                fix_cpa_conv_types = '0,2',
                booster = True,
                booster_settings = goadserver.models.campaign_panel_fields_booster_settings.CampaignPanelFields_booster_settings(
                    startdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    enddate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    pct = 1.337, 
                    ecpm = 1.337, ),
                default_bid_type = 0,
                sort_type = 56,
                as_failover = True,
                day_parting = {true=true, half_hours=false, ranges={1-09:00=1, 1-10:00=1}},
                screens = {true=true, only=true, venues=[mall, transit], lat=52.3676, lon=4.9041, radius_km=25},
                display_times = '08:00-12:00|14:00-18:00',
                display_days = '1,2,3,4,5',
                site_languages = 'en,de',
                connection_types = '2',
                carrier_ids = '15,22',
                rating_id = 56,
                orientation = 'landscape',
                site_mode = 0,
                only_tagged_zones = True,
                skip_low_quality = 0,
                ip_whitelist = '',
                ip_blacklist = '',
                av_check = goadserver.models.campaign_panel_fields_av_check.CampaignPanelFields_av_check(
                    true = True, 
                    target = 0, 
                    auto = True, 
                    allow_verified = True, 
                    countries = [
                        null
                        ], 
                    us_regions = [
                        null
                        ], ),
                email_type = 0,
                use_subscription_age = True,
                subscription_age = 0,
                instant_impression = True,
                subid_list = '1001
1002',
                subid_list_mode = 'whitelist',
                source_optimizer_ids = '12,15',
                wl_zone_ids = '1024,2048',
                feed_id = 56,
                feed_settings = goadserver.models.campaign_panel_fields_feed_settings.CampaignPanelFields_feed_settings(
                    deactivate_items = 0, 
                    mincpm = 1.337, ),
                priority = {"true":true,"order":1},
                suggestions = goadserver.models.campaign_panel_fields_suggestions.CampaignPanelFields_suggestions(
                    true = True, 
                    campaign_id = 56, ),
                hide_referrer = True,
                log_conv_as_paid = True,
                about_settings = goadserver.models.campaign_panel_fields_about_settings.CampaignPanelFields_about_settings(
                    inuse = 0, 
                    name = '', ),
                use_live_feed = True,
                live_feed_parent_id = 56,
                live_feed_settings = { },
                offer_type_id = 56,
                description = '',
                destination_url = '',
                preview_url = '',
                rtb_network_id = 56,
                rtb_type = 'openrtb',
                use_type = 0,
                zone_urls = [
                    None
                    ],
                bid_action = 1,
                use_qps = True,
                qps = 0,
                rtb_categories = 'IAB1,IAB9-30',
                use_api = True,
                api_data = { },
                log_skipped = True,
                domain_mask = goadserver.models.campaign_panel_fields_domain_mask.CampaignPanelFields_domain_mask(
                    true = True, 
                    value = '', ),
                rtb_xml_markup = True,
                name = '',
                request_url = '',
                banner_size_ids = None,
                daily_budget = 1.337,
                total_budget = 1.337,
                use_campaign_budget = True,
                selling_type = 56,
                use_daily_budget = True,
                use_budget_spreading = True,
                use_maxday_impressions = True,
                maxday_impressions = 100000,
                use_maxtotal_impressions = True,
                maxtotal_impressions = 1000000,
                select_pct = 50,
                use_start_date = True,
                start_date = '2026-11-01',
                use_end_date = True,
                end_date = '2026-11-30',
                location_ids = '1,3',
                webview = 0,
                adblock = 0,
                use_keywords = True,
                keywords = 'casino,poker',
                languages = '1,2,5',
                categories = '17,42',
                main_catid = 56,
                device_type_ids = '1,2',
                browser_ids = '1,3',
                os_ids = '1,5',
                isp_ids = '12,34',
                site_types = '1,4',
                regions = '528006,840001',
                use_capping = True,
                capping_hours = 56,
                capping_minutes = 56,
                capping_visitors = 56,
                cap_type = 0,
                capping_type = 56,
                capping_level = 56,
                domain_filter_id = 56,
                whitelist_id = 56,
                rt_include_id = 56,
                rt_exclude_id = 56,
                ip_pool_id = 56,
                fx_minprice = 1.337,
                is_paused = True,
                bidruleset_id = 56
            )
        else:
            return ApiV1CampaignsTypeIdPatchRequest(
        )
        """

    def testApiV1CampaignsTypeIdPatchRequest(self):
        """Test ApiV1CampaignsTypeIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

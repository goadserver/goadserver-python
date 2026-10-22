# coding: utf-8

# flake8: noqa

"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.0"

# Define package exports
__all__ = [
    "AIAssistantApi",
    "AccountApi",
    "AccountBillingApi",
    "AccountNotificationsApi",
    "AdScannerApi",
    "AdShopApi",
    "AdsApi",
    "AdspacesApi",
    "AgenticMediaBuyingApi",
    "BidRulesetsApi",
    "CampaignsApi",
    "CleanupApi",
    "CouponsApi",
    "CreativePoolsApi",
    "CreativesApi",
    "DirectDealsApi",
    "EventLogApi",
    "FiltersApi",
    "FundsApi",
    "LookupsApi",
    "MarketDataApi",
    "MarketplaceApi",
    "OAuthApi",
    "OffersApi",
    "PayoutsApi",
    "ProductFeedsApi",
    "PublicApi",
    "PublisherFiltersApi",
    "PushAudienceApi",
    "PushCampaignsApi",
    "RetargetingApi",
    "SSPCampaignsApi",
    "SharedReportsApi",
    "SitesApi",
    "SmartZonesApi",
    "SourceOptimizersApi",
    "StatsAdvertiserApi",
    "StatsAdvertiserOffersApi",
    "StatsAdvertiserRTBApi",
    "StatsAffiliateApi",
    "StatsPublisherApi",
    "StatsPublisherSSPApi",
    "StatsPublisherSmartZonesApi",
    "TagsApi",
    "TrackerAutomationApi",
    "TrackerConversionsApi",
    "TrackerNetworksApi",
    "TrackerOffersApi",
    "TrackerReportsApi",
    "TrackerSettingsApi",
    "TrackerSourcesApi",
    "TrackerTrackingLinksApi",
    "TrackingApi",
    "URLPoolsApi",
    "WebhooksEventsApi",
    "XMLFeedsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "Adspace",
    "AdspaceCreate",
    "AdspaceCreateBannerSettings",
    "AdspaceCreateBotSettings",
    "AdspaceCreateEmailSettings",
    "AdspaceCreateScreenSettings",
    "AdspaceCreateSearchSettings",
    "AdspaceCreateSearchSettingsBlockedTerms",
    "AdspaceFieldMeta",
    "AdspaceNetworkBinding",
    "AdspaceSchema",
    "AdspaceSettingsBlock",
    "AdspaceSite",
    "AdspaceTypeItem",
    "AdspaceTypeOption",
    "ApiKeyDetails",
    "ApiKeyDetailsCreated",
    "ApiPublicDemoGet200Response",
    "ApiPublicDemoGet200ResponseDataInner",
    "ApiPublicIntegrationsHooksTokenPost200Response",
    "ApiPublicOauthIntrospectPost200Response",
    "ApiPublicOauthTokenPost200Response",
    "ApiPublicOfferwallIdGet200Response",
    "ApiPublicOfferwallIdGet200ResponseOffersInner",
    "ApiV1AccountBillingAveragesGet200Response",
    "ApiV1AccountBillingAveragesGet200ResponseModulesInner",
    "ApiV1AccountBillingAveragesGet200ResponseOverchargesValue",
    "ApiV1AccountBillingInvoicesGet200Response",
    "ApiV1AccountBillingInvoicesGet200ResponseResultsInner",
    "ApiV1AccountGet200Response",
    "ApiV1AccountGet200ResponseApiKey",
    "ApiV1AccountNotificationDestinationsPostRequest",
    "ApiV1AccountNotificationPreferencesPutRequest",
    "ApiV1AccountNotificationsReadPostRequest",
    "ApiV1AccountPreferencesKeyPutRequest",
    "ApiV1AccountUiLayoutsScopePutRequest",
    "ApiV1AccountUiLayoutsScopePutRequestData",
    "ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner",
    "ApiV1AdScannerIdIgnoreDomainPutRequest",
    "ApiV1AdScannerIdManualItemsItemIdStatePutRequest",
    "ApiV1AdScannerIdManualItemsPostRequest",
    "ApiV1AdScannerIdPutRequest",
    "ApiV1AdScannerIdToggleActivePutRequest",
    "ApiV1AdScannerPostRequest",
    "ApiV1AdScannerPostRequestTags",
    "ApiV1AdShopCartPostRequest",
    "ApiV1AdShopConfirmPostRequest",
    "ApiV1AdShopGroupSummaryPostRequest",
    "ApiV1AdShopGroupSummaryPostRequestFilters",
    "ApiV1AdspacesAddMultiplePostRequest",
    "ApiV1AdspacesExportCodesGet200ResponseInner",
    "ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner",
    "ApiV1AdspacesGet200Response",
    "ApiV1AdspacesGet200ResponseDataInner",
    "ApiV1AdspacesIdClonePostRequest",
    "ApiV1AdspacesIdCodeGet200Response",
    "ApiV1AdspacesIdCodeGet200ResponseAmp",
    "ApiV1AdspacesIdCodeGet200ResponseCtv",
    "ApiV1AdspacesIdCodeGet200ResponseLayoutsInner",
    "ApiV1AdspacesIdCodeGet200ResponseScreen",
    "ApiV1AdspacesIdCodeGet200ResponseSite",
    "ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest",
    "ApiV1AdspacesIdMediaBuyingBlockPostRequest",
    "ApiV1AdspacesIdMediaBuyingIpsPostRequest",
    "ApiV1AdspacesIdMediaBuyingLaunchPostRequest",
    "ApiV1AdspacesIdMediaBuyingReportPostRequest",
    "ApiV1AdspacesIdMediaBuyingSourceBidPutRequest",
    "ApiV1AdspacesIdMediaBuyingTargetingPutRequest",
    "ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner",
    "ApiV1AdspacesIdNetworkBindingPutRequest",
    "ApiV1AdspacesIdOwnAdsMassActionPostRequest",
    "ApiV1AdspacesIdPatch200Response",
    "ApiV1AdspacesIdPricesTypePostRequest",
    "ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner",
    "ApiV1AdspacesIdWlCampaignsPutRequest",
    "ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner",
    "ApiV1AdspacesMassDeletePostRequest",
    "ApiV1AdspacesMassRecoverPostRequest",
    "ApiV1AdspacesTemplatesGet200ResponseInner",
    "ApiV1AdspacesTemplatesIdPutRequest",
    "ApiV1AdspacesTemplatesPostRequest",
    "ApiV1BidRulesetsGet200Response",
    "ApiV1BidRulesetsIdClonePostRequest",
    "ApiV1BidRulesetsIdDelete200Response",
    "ApiV1BidRulesetsIdDelete422Response",
    "ApiV1BidRulesetsIdPatchRequest",
    "ApiV1BidRulesetsPostRequest",
    "ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest",
    "ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest",
    "ApiV1CampaignsGet200Response",
    "ApiV1CampaignsGet200ResponseDataInner",
    "ApiV1CampaignsMassDeletePostRequest",
    "ApiV1CampaignsMassTogglePutRequest",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200ResponseZoneBidsInner",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequestZoneBidsInner",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response",
    "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest",
    "ApiV1CampaignsRonIdSiteListSiteIdPutRequest",
    "ApiV1CampaignsRonIdZonesGet200Response",
    "ApiV1CampaignsRonIdZonesGet200ResponseDataInner",
    "ApiV1CampaignsSaveCategoriesPutRequest",
    "ApiV1CampaignsSaveTagsPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response",
    "ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest",
    "ApiV1CampaignsTypeCampaignIdAdsGet200Response",
    "ApiV1CampaignsTypeCampaignIdAdsGet200ResponseMeta",
    "ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest",
    "ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest",
    "ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest",
    "ApiV1CampaignsTypeCampaignIdAdsPostRequest",
    "ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner",
    "ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest",
    "ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest",
    "ApiV1CampaignsTypeIdActivePatch200Response",
    "ApiV1CampaignsTypeIdActivePatchRequest",
    "ApiV1CampaignsTypeIdBidsPatch200Response",
    "ApiV1CampaignsTypeIdBidsPatchRequest",
    "ApiV1CampaignsTypeIdBudgetPatch200Response",
    "ApiV1CampaignsTypeIdBudgetPatchRequest",
    "ApiV1CampaignsTypeIdClonePost201Response",
    "ApiV1CampaignsTypeIdClonePost201ResponseCopied",
    "ApiV1CampaignsTypeIdClonePostRequest",
    "ApiV1CampaignsTypeIdDelete200Response",
    "ApiV1CampaignsTypeIdFiltersGet200Response",
    "ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner",
    "ApiV1CampaignsTypeIdFiltersPost200Response",
    "ApiV1CampaignsTypeIdFiltersPostRequest",
    "ApiV1CampaignsTypeIdMinBidGet200Response",
    "ApiV1CampaignsTypeIdPatchRequest",
    "ApiV1CampaignsTypeIdPatchRequestAllOfBannerSizeIds",
    "ApiV1CampaignsTypeIdZonesPostRequest",
    "ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest",
    "ApiV1CampaignsTypePostRequest",
    "ApiV1CampaignsTypePostRequestAllOfBannerSizeIds",
    "ApiV1CampaignsTypePostRequestAllOfPriority",
    "ApiV1CampaignsTypeSchemaAdsGet200Response",
    "ApiV1CampaignsTypeSchemaGet200Response",
    "ApiV1CampaignsTypeSchemaGet200ResponseFieldsInner",
    "ApiV1CouponsSetsIdGeneratePostRequest",
    "ApiV1CouponsSetsIdPutRequest",
    "ApiV1CouponsSetsPostRequest",
    "ApiV1CreativeFoldersIdPutRequest",
    "ApiV1CreativeFoldersPostRequest",
    "ApiV1CreativePoolsGet200Response",
    "ApiV1CreativePoolsGet200ResponseDataInner",
    "ApiV1CreativePoolsGetPerPageParameter",
    "ApiV1CreativePoolsIdAddCreativesPostRequest",
    "ApiV1CreativePoolsIdAddUrlsPostRequest",
    "ApiV1CreativePoolsIdClonePost201Response",
    "ApiV1CreativePoolsIdDelete200Response",
    "ApiV1CreativePoolsIdDelete409Response",
    "ApiV1CreativePoolsIdGet200Response",
    "ApiV1CreativePoolsIdItemsItemIdPut409Response",
    "ApiV1CreativePoolsIdItemsItemIdPutRequest",
    "ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt",
    "ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt",
    "ApiV1CreativePoolsIdItemsMassActionPutRequest",
    "ApiV1CreativePoolsIdItemsPostRequest",
    "ApiV1CreativePoolsIdItemsRecoverPostRequest",
    "ApiV1CreativePoolsIdPutRequest",
    "ApiV1CreativePoolsIdUsedInGet200Response",
    "ApiV1CreativePoolsPostRequest",
    "ApiV1CreativesBulkDeletePostRequest",
    "ApiV1CreativesBulkMovePostRequest",
    "ApiV1CreativesBulkUndeletePostRequest",
    "ApiV1CreativesGet200Response",
    "ApiV1CreativesGetPerPageParameter",
    "ApiV1CreativesIdNamePutRequest",
    "ApiV1CreativesIdPutRequest",
    "ApiV1CreativesIdPutRequestTags",
    "ApiV1CreativesIdTagsPutRequest",
    "ApiV1DomainsIdNotesPutRequest",
    "ApiV1DomainsPostRequest",
    "ApiV1EventLogExportsPostRequest",
    "ApiV1EventsGet200Response",
    "ApiV1FiltersGet200Response",
    "ApiV1FiltersMassActionPostRequest",
    "ApiV1FiltersMassActionPostRequestFiltersInner",
    "ApiV1FiltersPostRequest",
    "ApiV1FiltersTypeIdActivePatch200Response",
    "ApiV1FiltersTypeIdItemsItemDelete200Response",
    "ApiV1FiltersTypeIdItemsPost200Response",
    "ApiV1FiltersTypeIdItemsPostRequest",
    "ApiV1FiltersTypeIdPutRequest",
    "ApiV1FundsBalanceSettingsPutRequest",
    "ApiV1FundsDepositTypeFidGet200Response",
    "ApiV1FundsDepositTypePost200Response",
    "ApiV1FundsDepositTypePostRequest",
    "ApiV1FundsDepositsIdProofPost200Response",
    "ApiV1FundsDepositsIdTxnHashPost200Response",
    "ApiV1FundsDepositsIdTxnHashPostRequest",
    "ApiV1FundsGet200Response",
    "ApiV1FundsPayTypesGet200Response",
    "ApiV1FundsPayTypesGet200ResponsePayTypesInner",
    "ApiV1FundsTransactionsGet200Response",
    "ApiV1FundsTransactionsGet200ResponseDataInner",
    "ApiV1FundsTransferPostRequest",
    "ApiV1LookupsAdspaceTypesGet200Response",
    "ApiV1LookupsBannerSizesGet200Response",
    "ApiV1LookupsBannerSizesGet200ResponseItemsInner",
    "ApiV1LookupsBrowsersGet200Response",
    "ApiV1LookupsCarriersGet200Response",
    "ApiV1LookupsCarriersGet200ResponseDataInner",
    "ApiV1LookupsCategoriesGet200Response",
    "ApiV1LookupsCategoriesGet200ResponseItemsInner",
    "ApiV1LookupsDeviceTypesGet200Response",
    "ApiV1LookupsRegionsGet200Response",
    "ApiV1LookupsRegionsGet200ResponseRegionsInner",
    "ApiV1LookupsWebsiteLanguagesGet200Response",
    "ApiV1LookupsWebsiteLanguagesGet200ResponseItemsInner",
    "ApiV1MarketplaceFlatRequestsRenewPostRequest",
    "ApiV1McpPost200Response",
    "ApiV1McpPost200ResponseError",
    "ApiV1McpPost200ResponseId",
    "ApiV1McpPostRequest",
    "ApiV1McpPostRequestId",
    "ApiV1OffersGet200Response",
    "ApiV1OffersGet200ResponseDataInner",
    "ApiV1ProductFeedsPostRequest",
    "ApiV1ProductFeedsPreviewPostRequest",
    "ApiV1ProductFeedsPreviewPostRequestProduct",
    "ApiV1PublisherFiltersGet200Response",
    "ApiV1PublisherFiltersGet200ResponseCategoriesInner",
    "ApiV1PublisherFiltersGet200ResponseUrlsInner",
    "ApiV1PublisherFiltersUrlsDelete200Response",
    "ApiV1PublisherFiltersUrlsDeleteRequest",
    "ApiV1PublisherFiltersUrlsPost201Response",
    "ApiV1PublisherFiltersUrlsPostRequest",
    "ApiV1PublisherFinanceEarningsGet200Response",
    "ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner",
    "ApiV1PublisherFinanceEarningsGet200ResponsePeriod",
    "ApiV1PublisherFinanceEarningsGet200ResponseSummary",
    "ApiV1PublisherFinanceGet200Response",
    "ApiV1PublisherFinanceGet200ResponseBalance",
    "ApiV1PublisherFinanceMonthEarningsGet200ResponseInner",
    "ApiV1PublisherFinancePayoutRequestPost201Response",
    "ApiV1PublisherFinancePayoutRequestPost201ResponsePayout",
    "ApiV1PublisherFinancePayoutRequestPostRequest",
    "ApiV1PublisherFinancePayoutTypesGet200ResponseInner",
    "ApiV1PublisherFinancePayoutsGet200Response",
    "ApiV1PublisherFinancePayoutsGet200ResponseDataInner",
    "ApiV1PublisherFinancePayoutsGet200ResponseMeta",
    "ApiV1PublisherFinanceSettingsGet200Response",
    "ApiV1PublisherFinanceSettingsGet200ResponseData",
    "ApiV1PublisherFinanceSettingsPutRequest",
    "ApiV1PublisherFinanceTransactionsGet200Response",
    "ApiV1PublisherFinanceTransactionsGet200ResponseDataInner",
    "ApiV1PublisherFinanceTransactionsIdGet200Response",
    "ApiV1PublisherFinanceTransferToAdvertiserPost200Response",
    "ApiV1PublisherFinanceTransferToAdvertiserPostRequest",
    "ApiV1PublisherOffersPostbackLogGet200Response",
    "ApiV1PublisherOffersPostbackLogGet200ResponseDataInner",
    "ApiV1PublisherPushCampaignsGet200Response",
    "ApiV1PublisherPushCampaignsIdDelete200Response",
    "ApiV1PublisherPushCampaignsIdDelete200ResponseData",
    "ApiV1PublisherPushCampaignsIdSendPost200Response",
    "ApiV1PublisherPushCampaignsIdSendPost200ResponseData",
    "ApiV1PublisherPushCampaignsPost200Response",
    "ApiV1PublisherPushCampaignsPostRequest",
    "ApiV1PublisherPushDeliveryRulesGet200Response",
    "ApiV1PublisherPushDeliveryRulesIdPutRequest",
    "ApiV1PublisherPushDeliveryRulesPostRequest",
    "ApiV1PublisherPushSegmentsGet200Response",
    "ApiV1PublisherPushSegmentsIdPutRequest",
    "ApiV1PublisherPushSegmentsPostRequest",
    "ApiV1PublisherPushSetupGet200Response",
    "ApiV1PublisherPushSetupGet200ResponseData",
    "ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner",
    "ApiV1PublisherPushStatsGet200Response",
    "ApiV1PublisherPushStatsGet200ResponseData",
    "ApiV1PublisherPushStatsGet200ResponseDataDailyInner",
    "ApiV1PublisherPushStatsGet200ResponseDataGrowthInner",
    "ApiV1PublisherPushStatsGet200ResponseDataSummary",
    "ApiV1PublisherPushSubscribersActionPost200Response",
    "ApiV1PublisherPushSubscribersActionPost200ResponseData",
    "ApiV1PublisherPushSubscribersActionPostRequest",
    "ApiV1PublisherPushSubscribersGet200Response",
    "ApiV1PublisherPushSubscribersGet200ResponseData",
    "ApiV1PublisherSmartzonesIdPutRequest",
    "ApiV1PublisherSmartzonesIdPutRequestIsActive",
    "ApiV1PublisherSmartzonesIdPutRequestUniqueOnly",
    "ApiV1PublisherSmartzonesImportPostRequest",
    "ApiV1PublisherSmartzonesImportPostRequestZonesInner",
    "ApiV1PublisherSmartzonesNetworksPostRequest",
    "ApiV1PublisherSmartzonesPostRequest",
    "ApiV1PublisherSspCampaignsIdTestRtbPostRequest",
    "ApiV1PublisherSspCampaignsIdToggleDeletePutRequest",
    "ApiV1PublisherSspCampaignsIdTogglePausePutRequest",
    "ApiV1PublisherSspSellerDisclosurePutRequest",
    "ApiV1RetargetingPixelsGet200Response",
    "ApiV1RetargetingPixelsIdActivePatch200Response",
    "ApiV1RetargetingPixelsIdDelete200Response",
    "ApiV1RtbTestRtbPostRequest",
    "ApiV1SharedReportsIdPutRequest",
    "ApiV1SharedReportsIdPutRequestCampaignsInner",
    "ApiV1SharedReportsIdPutRequestSitesInner",
    "ApiV1SitesGet200Response",
    "ApiV1SitesGet200ResponseDataInner",
    "ApiV1SitesIdClonePostRequest",
    "ApiV1SitesSchemaGet200Response",
    "ApiV1SitesSchemaGet200ResponseFieldsInner",
    "ApiV1TagsIdPutRequest",
    "ApiV1TagsMassDeletePostRequest",
    "ApiV1TagsPostRequest",
    "ApiV1ToolsReplaceDomainPutRequest",
    "ApiV1TrackerAdNetworksDeleteReportsPutRequest",
    "ApiV1TrackerAdNetworksIdPutRequest",
    "ApiV1TrackerAdNetworksPostRequest",
    "ApiV1TrackerAffiliateNetworksGet200Response",
    "ApiV1TrackerAffiliateNetworksIdPutRequest",
    "ApiV1TrackerAffiliateNetworksPostRequest",
    "ApiV1TrackerConversionLoggingPutRequest",
    "ApiV1TrackerConversionTypesPutRequest",
    "ApiV1TrackerConversionsGet200Response",
    "ApiV1TrackerConversionsGet200ResponseSummary",
    "ApiV1TrackerConversionsIdStatePutRequest",
    "ApiV1TrackerCustomParamsPutRequest",
    "ApiV1TrackerCustomParamsPutRequestSlotsInner",
    "ApiV1TrackerOffersBulkPostRequest",
    "ApiV1TrackerOffersGet200Response",
    "ApiV1TrackerOffersIdGet200Response",
    "ApiV1TrackerOffersIdPutRequest",
    "ApiV1TrackerOffersIdUrlsPostRequest",
    "ApiV1TrackerOffersIdUrlsUrlIdPutRequest",
    "ApiV1TrackerOffersPostRequest",
    "ApiV1TrackerOffersPostRequestUrlsInner",
    "ApiV1TrackerReportSchedulesGet200Response",
    "ApiV1TrackerReportSchedulesIdGet200Response",
    "ApiV1TrackerReportSchedulesIdPutRequest",
    "ApiV1TrackerReportSchedulesPostRequest",
    "ApiV1TrackerRulesGet200Response",
    "ApiV1TrackerRulesIdGet200Response",
    "ApiV1TrackerRulesIdPutRequest",
    "ApiV1TrackerRulesPostRequest",
    "ApiV1TrackerSourceAccountsGet200Response",
    "ApiV1TrackerSourceAccountsIdGet200Response",
    "ApiV1TrackerSourceAccountsIdPutRequest",
    "ApiV1TrackerSourceAccountsPostRequest",
    "ApiV1TrackerSourcesGet200Response",
    "ApiV1TrackerSourcesIdPutRequest",
    "ApiV1TrackerSourcesPostRequest",
    "ApiV1TrackerTrackingLinksBulkPostRequest",
    "ApiV1TrackerTrackingLinksGet200Response",
    "ApiV1TrackerTrackingLinksIdBlocklistPostRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest",
    "ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest",
    "ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest",
    "ApiV1TrackerTrackingLinksIdPutRequest",
    "ApiV1TrackerTrackingLinksIdToggleActivePost200Response",
    "ApiV1TrackerTrackingLinksIdToggleActivePost200ResponseData",
    "ApiV1TrackerTrackingLinksIdZoneCostsGet200Response",
    "ApiV1TrackerTrackingLinksPostRequest",
    "ApiV1TrackingConversionTypesGet200Response",
    "ApiV1TrackingConversionTypesGet200ResponseConversionTypesInner",
    "ApiV1TrackingConversionTypesPut200Response",
    "ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner",
    "ApiV1TrackingConversionTypesPutRequest",
    "ApiV1TrackingConversionTypesPutRequestTypesInner",
    "ApiV1TrackingPixelsGet200Response",
    "ApiV1TrackingPixelsIdPutRequest",
    "ApiV1TrackingPixelsPostRequest",
    "ApiV1UrlPoolsIdPutRequest",
    "ApiV1UrlPoolsIdUrlsPostRequest",
    "ApiV1UrlPoolsIdUrlsUrlIdPutRequest",
    "ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest",
    "ApiV1UrlPoolsPostRequest",
    "ApiV1UrlPoolsReplaceUrlPutRequest",
    "ApiV1WebhooksGet200Response",
    "ApiV1WebhooksIdDelete200Response",
    "ApiV1WebhooksIdDeliveriesGet200Response",
    "ApiV1WebhooksIdDeliveriesGet200ResponseDataInner",
    "ApiV1WebhooksIdPatchRequest",
    "ApiV1WebhooksIdRotateSecretPostRequest",
    "ApiV1WebhooksIdTestPost200Response",
    "ApiV1WebhooksIdTestPost200ResponseData",
    "ApiV1WebhooksPost201Response",
    "ApiV1WebhooksPostRequest",
    "ApiV1XmlFeedsIdPutRequest",
    "ApiV1XmlFeedsPostRequest",
    "BidRule",
    "BidRuleConditions",
    "BidRuleset",
    "BidRulesetListItem",
    "CampaignPanelFields",
    "CampaignPanelFieldsAboutSettings",
    "CampaignPanelFieldsAvCheck",
    "CampaignPanelFieldsBoosterSettings",
    "CampaignPanelFieldsConversionCapping",
    "CampaignPanelFieldsDayParting",
    "CampaignPanelFieldsDomainMask",
    "CampaignPanelFieldsFeedSettings",
    "CampaignPanelFieldsPriority",
    "CampaignPanelFieldsScreens",
    "CampaignPanelFieldsSuggestions",
    "CpaOptimizerBody",
    "CpmOptimizerBody",
    "Error",
    "FilterDetail",
    "FilterDetailAllOfRanges",
    "FilterSummary",
    "FilterType",
    "FundsDepositProof",
    "FundsTxnClaim",
    "ListMeta",
    "MediaBuyingPolicy",
    "MediaBuyingPolicyTestPhase",
    "OwnAdWrite",
    "PushCampaign",
    "PushDeliveryRule",
    "PushSegment",
    "PushSubscriber",
    "ResourceFilter",
    "RetargetingPixel",
    "RetargetingPixelWrite",
    "RtbTestRequest",
    "RtbTestResult",
    "SharedReportAdjust",
    "SharedReportBody",
    "SharedReportBodyCampaignsInner",
    "SharedReportBodyOptions",
    "SharedReportBodySettings",
    "Site",
    "SiteCreate",
    "SiteSnippetWrite",
    "SiteSnippetWriteConditions",
    "SspCampaignWrite",
    "SspCampaignWriteSlotsInner",
    "SspCampaignWriteZoneurlsInner",
    "StatsResponse",
    "TrackerAffiliateNetwork",
    "TrackerConversion",
    "TrackerOffer",
    "TrackerReportSchedule",
    "TrackerRule",
    "TrackerSource",
    "TrackerSourceAccount",
    "TrackingLink",
    "TrackingPixel",
    "UserEvent",
    "UserEventType",
    "UserWebhook",
]

# import apis into sdk package
from goadserver.api.ai_assistant_api import AIAssistantApi as AIAssistantApi
from goadserver.api.account_api import AccountApi as AccountApi
from goadserver.api.account_billing_api import AccountBillingApi as AccountBillingApi
from goadserver.api.account_notifications_api import AccountNotificationsApi as AccountNotificationsApi
from goadserver.api.ad_scanner_api import AdScannerApi as AdScannerApi
from goadserver.api.ad_shop_api import AdShopApi as AdShopApi
from goadserver.api.ads_api import AdsApi as AdsApi
from goadserver.api.adspaces_api import AdspacesApi as AdspacesApi
from goadserver.api.agentic_media_buying_api import AgenticMediaBuyingApi as AgenticMediaBuyingApi
from goadserver.api.bid_rulesets_api import BidRulesetsApi as BidRulesetsApi
from goadserver.api.campaigns_api import CampaignsApi as CampaignsApi
from goadserver.api.cleanup_api import CleanupApi as CleanupApi
from goadserver.api.coupons_api import CouponsApi as CouponsApi
from goadserver.api.creative_pools_api import CreativePoolsApi as CreativePoolsApi
from goadserver.api.creatives_api import CreativesApi as CreativesApi
from goadserver.api.direct_deals_api import DirectDealsApi as DirectDealsApi
from goadserver.api.event_log_api import EventLogApi as EventLogApi
from goadserver.api.filters_api import FiltersApi as FiltersApi
from goadserver.api.funds_api import FundsApi as FundsApi
from goadserver.api.lookups_api import LookupsApi as LookupsApi
from goadserver.api.market_data_api import MarketDataApi as MarketDataApi
from goadserver.api.marketplace_api import MarketplaceApi as MarketplaceApi
from goadserver.api.o_auth_api import OAuthApi as OAuthApi
from goadserver.api.offers_api import OffersApi as OffersApi
from goadserver.api.payouts_api import PayoutsApi as PayoutsApi
from goadserver.api.product_feeds_api import ProductFeedsApi as ProductFeedsApi
from goadserver.api.public_api import PublicApi as PublicApi
from goadserver.api.publisher_filters_api import PublisherFiltersApi as PublisherFiltersApi
from goadserver.api.push_audience_api import PushAudienceApi as PushAudienceApi
from goadserver.api.push_campaigns_api import PushCampaignsApi as PushCampaignsApi
from goadserver.api.retargeting_api import RetargetingApi as RetargetingApi
from goadserver.api.ssp_campaigns_api import SSPCampaignsApi as SSPCampaignsApi
from goadserver.api.shared_reports_api import SharedReportsApi as SharedReportsApi
from goadserver.api.sites_api import SitesApi as SitesApi
from goadserver.api.smart_zones_api import SmartZonesApi as SmartZonesApi
from goadserver.api.source_optimizers_api import SourceOptimizersApi as SourceOptimizersApi
from goadserver.api.stats_advertiser_api import StatsAdvertiserApi as StatsAdvertiserApi
from goadserver.api.stats_advertiser_offers_api import StatsAdvertiserOffersApi as StatsAdvertiserOffersApi
from goadserver.api.stats_advertiser_rtb_api import StatsAdvertiserRTBApi as StatsAdvertiserRTBApi
from goadserver.api.stats_affiliate_api import StatsAffiliateApi as StatsAffiliateApi
from goadserver.api.stats_publisher_api import StatsPublisherApi as StatsPublisherApi
from goadserver.api.stats_publisher_ssp_api import StatsPublisherSSPApi as StatsPublisherSSPApi
from goadserver.api.stats_publisher_smart_zones_api import StatsPublisherSmartZonesApi as StatsPublisherSmartZonesApi
from goadserver.api.tags_api import TagsApi as TagsApi
from goadserver.api.tracker_automation_api import TrackerAutomationApi as TrackerAutomationApi
from goadserver.api.tracker_conversions_api import TrackerConversionsApi as TrackerConversionsApi
from goadserver.api.tracker_networks_api import TrackerNetworksApi as TrackerNetworksApi
from goadserver.api.tracker_offers_api import TrackerOffersApi as TrackerOffersApi
from goadserver.api.tracker_reports_api import TrackerReportsApi as TrackerReportsApi
from goadserver.api.tracker_settings_api import TrackerSettingsApi as TrackerSettingsApi
from goadserver.api.tracker_sources_api import TrackerSourcesApi as TrackerSourcesApi
from goadserver.api.tracker_tracking_links_api import TrackerTrackingLinksApi as TrackerTrackingLinksApi
from goadserver.api.tracking_api import TrackingApi as TrackingApi
from goadserver.api.url_pools_api import URLPoolsApi as URLPoolsApi
from goadserver.api.webhooks_events_api import WebhooksEventsApi as WebhooksEventsApi
from goadserver.api.xml_feeds_api import XMLFeedsApi as XMLFeedsApi

# import ApiClient
from goadserver.api_response import ApiResponse as ApiResponse
from goadserver.api_client import ApiClient as ApiClient
from goadserver.configuration import Configuration as Configuration
from goadserver.exceptions import OpenApiException as OpenApiException
from goadserver.exceptions import ApiTypeError as ApiTypeError
from goadserver.exceptions import ApiValueError as ApiValueError
from goadserver.exceptions import ApiKeyError as ApiKeyError
from goadserver.exceptions import ApiAttributeError as ApiAttributeError
from goadserver.exceptions import ApiException as ApiException

# import models into sdk package
from goadserver.models.adspace import Adspace as Adspace
from goadserver.models.adspace_create import AdspaceCreate as AdspaceCreate
from goadserver.models.adspace_create_banner_settings import AdspaceCreateBannerSettings as AdspaceCreateBannerSettings
from goadserver.models.adspace_create_bot_settings import AdspaceCreateBotSettings as AdspaceCreateBotSettings
from goadserver.models.adspace_create_email_settings import AdspaceCreateEmailSettings as AdspaceCreateEmailSettings
from goadserver.models.adspace_create_screen_settings import AdspaceCreateScreenSettings as AdspaceCreateScreenSettings
from goadserver.models.adspace_create_search_settings import AdspaceCreateSearchSettings as AdspaceCreateSearchSettings
from goadserver.models.adspace_create_search_settings_blocked_terms import AdspaceCreateSearchSettingsBlockedTerms as AdspaceCreateSearchSettingsBlockedTerms
from goadserver.models.adspace_field_meta import AdspaceFieldMeta as AdspaceFieldMeta
from goadserver.models.adspace_network_binding import AdspaceNetworkBinding as AdspaceNetworkBinding
from goadserver.models.adspace_schema import AdspaceSchema as AdspaceSchema
from goadserver.models.adspace_settings_block import AdspaceSettingsBlock as AdspaceSettingsBlock
from goadserver.models.adspace_site import AdspaceSite as AdspaceSite
from goadserver.models.adspace_type_item import AdspaceTypeItem as AdspaceTypeItem
from goadserver.models.adspace_type_option import AdspaceTypeOption as AdspaceTypeOption
from goadserver.models.api_key_details import ApiKeyDetails as ApiKeyDetails
from goadserver.models.api_key_details_created import ApiKeyDetailsCreated as ApiKeyDetailsCreated
from goadserver.models.api_public_demo_get200_response import ApiPublicDemoGet200Response as ApiPublicDemoGet200Response
from goadserver.models.api_public_demo_get200_response_data_inner import ApiPublicDemoGet200ResponseDataInner as ApiPublicDemoGet200ResponseDataInner
from goadserver.models.api_public_integrations_hooks_token_post200_response import ApiPublicIntegrationsHooksTokenPost200Response as ApiPublicIntegrationsHooksTokenPost200Response
from goadserver.models.api_public_oauth_introspect_post200_response import ApiPublicOauthIntrospectPost200Response as ApiPublicOauthIntrospectPost200Response
from goadserver.models.api_public_oauth_token_post200_response import ApiPublicOauthTokenPost200Response as ApiPublicOauthTokenPost200Response
from goadserver.models.api_public_offerwall_id_get200_response import ApiPublicOfferwallIdGet200Response as ApiPublicOfferwallIdGet200Response
from goadserver.models.api_public_offerwall_id_get200_response_offers_inner import ApiPublicOfferwallIdGet200ResponseOffersInner as ApiPublicOfferwallIdGet200ResponseOffersInner
from goadserver.models.api_v1_account_billing_averages_get200_response import ApiV1AccountBillingAveragesGet200Response as ApiV1AccountBillingAveragesGet200Response
from goadserver.models.api_v1_account_billing_averages_get200_response_modules_inner import ApiV1AccountBillingAveragesGet200ResponseModulesInner as ApiV1AccountBillingAveragesGet200ResponseModulesInner
from goadserver.models.api_v1_account_billing_averages_get200_response_overcharges_value import ApiV1AccountBillingAveragesGet200ResponseOverchargesValue as ApiV1AccountBillingAveragesGet200ResponseOverchargesValue
from goadserver.models.api_v1_account_billing_invoices_get200_response import ApiV1AccountBillingInvoicesGet200Response as ApiV1AccountBillingInvoicesGet200Response
from goadserver.models.api_v1_account_billing_invoices_get200_response_results_inner import ApiV1AccountBillingInvoicesGet200ResponseResultsInner as ApiV1AccountBillingInvoicesGet200ResponseResultsInner
from goadserver.models.api_v1_account_get200_response import ApiV1AccountGet200Response as ApiV1AccountGet200Response
from goadserver.models.api_v1_account_get200_response_api_key import ApiV1AccountGet200ResponseApiKey as ApiV1AccountGet200ResponseApiKey
from goadserver.models.api_v1_account_notification_destinations_post_request import ApiV1AccountNotificationDestinationsPostRequest as ApiV1AccountNotificationDestinationsPostRequest
from goadserver.models.api_v1_account_notification_preferences_put_request import ApiV1AccountNotificationPreferencesPutRequest as ApiV1AccountNotificationPreferencesPutRequest
from goadserver.models.api_v1_account_notifications_read_post_request import ApiV1AccountNotificationsReadPostRequest as ApiV1AccountNotificationsReadPostRequest
from goadserver.models.api_v1_account_preferences_key_put_request import ApiV1AccountPreferencesKeyPutRequest as ApiV1AccountPreferencesKeyPutRequest
from goadserver.models.api_v1_account_ui_layouts_scope_put_request import ApiV1AccountUiLayoutsScopePutRequest as ApiV1AccountUiLayoutsScopePutRequest
from goadserver.models.api_v1_account_ui_layouts_scope_put_request_data import ApiV1AccountUiLayoutsScopePutRequestData as ApiV1AccountUiLayoutsScopePutRequestData
from goadserver.models.api_v1_account_ui_layouts_scope_put_request_data_patches_inner import ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner as ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner
from goadserver.models.api_v1_ad_scanner_id_ignore_domain_put_request import ApiV1AdScannerIdIgnoreDomainPutRequest as ApiV1AdScannerIdIgnoreDomainPutRequest
from goadserver.models.api_v1_ad_scanner_id_manual_items_item_id_state_put_request import ApiV1AdScannerIdManualItemsItemIdStatePutRequest as ApiV1AdScannerIdManualItemsItemIdStatePutRequest
from goadserver.models.api_v1_ad_scanner_id_manual_items_post_request import ApiV1AdScannerIdManualItemsPostRequest as ApiV1AdScannerIdManualItemsPostRequest
from goadserver.models.api_v1_ad_scanner_id_put_request import ApiV1AdScannerIdPutRequest as ApiV1AdScannerIdPutRequest
from goadserver.models.api_v1_ad_scanner_id_toggle_active_put_request import ApiV1AdScannerIdToggleActivePutRequest as ApiV1AdScannerIdToggleActivePutRequest
from goadserver.models.api_v1_ad_scanner_post_request import ApiV1AdScannerPostRequest as ApiV1AdScannerPostRequest
from goadserver.models.api_v1_ad_scanner_post_request_tags import ApiV1AdScannerPostRequestTags as ApiV1AdScannerPostRequestTags
from goadserver.models.api_v1_ad_shop_cart_post_request import ApiV1AdShopCartPostRequest as ApiV1AdShopCartPostRequest
from goadserver.models.api_v1_ad_shop_confirm_post_request import ApiV1AdShopConfirmPostRequest as ApiV1AdShopConfirmPostRequest
from goadserver.models.api_v1_ad_shop_group_summary_post_request import ApiV1AdShopGroupSummaryPostRequest as ApiV1AdShopGroupSummaryPostRequest
from goadserver.models.api_v1_ad_shop_group_summary_post_request_filters import ApiV1AdShopGroupSummaryPostRequestFilters as ApiV1AdShopGroupSummaryPostRequestFilters
from goadserver.models.api_v1_adspaces_add_multiple_post_request import ApiV1AdspacesAddMultiplePostRequest as ApiV1AdspacesAddMultiplePostRequest
from goadserver.models.api_v1_adspaces_export_codes_get200_response_inner import ApiV1AdspacesExportCodesGet200ResponseInner as ApiV1AdspacesExportCodesGet200ResponseInner
from goadserver.models.api_v1_adspaces_export_codes_get200_response_inner_codes_inner import ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner as ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner
from goadserver.models.api_v1_adspaces_get200_response import ApiV1AdspacesGet200Response as ApiV1AdspacesGet200Response
from goadserver.models.api_v1_adspaces_get200_response_data_inner import ApiV1AdspacesGet200ResponseDataInner as ApiV1AdspacesGet200ResponseDataInner
from goadserver.models.api_v1_adspaces_id_clone_post_request import ApiV1AdspacesIdClonePostRequest as ApiV1AdspacesIdClonePostRequest
from goadserver.models.api_v1_adspaces_id_code_get200_response import ApiV1AdspacesIdCodeGet200Response as ApiV1AdspacesIdCodeGet200Response
from goadserver.models.api_v1_adspaces_id_code_get200_response_amp import ApiV1AdspacesIdCodeGet200ResponseAmp as ApiV1AdspacesIdCodeGet200ResponseAmp
from goadserver.models.api_v1_adspaces_id_code_get200_response_ctv import ApiV1AdspacesIdCodeGet200ResponseCtv as ApiV1AdspacesIdCodeGet200ResponseCtv
from goadserver.models.api_v1_adspaces_id_code_get200_response_layouts_inner import ApiV1AdspacesIdCodeGet200ResponseLayoutsInner as ApiV1AdspacesIdCodeGet200ResponseLayoutsInner
from goadserver.models.api_v1_adspaces_id_code_get200_response_screen import ApiV1AdspacesIdCodeGet200ResponseScreen as ApiV1AdspacesIdCodeGet200ResponseScreen
from goadserver.models.api_v1_adspaces_id_code_get200_response_site import ApiV1AdspacesIdCodeGet200ResponseSite as ApiV1AdspacesIdCodeGet200ResponseSite
from goadserver.models.api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request import ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest as ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest
from goadserver.models.api_v1_adspaces_id_media_buying_block_post_request import ApiV1AdspacesIdMediaBuyingBlockPostRequest as ApiV1AdspacesIdMediaBuyingBlockPostRequest
from goadserver.models.api_v1_adspaces_id_media_buying_ips_post_request import ApiV1AdspacesIdMediaBuyingIpsPostRequest as ApiV1AdspacesIdMediaBuyingIpsPostRequest
from goadserver.models.api_v1_adspaces_id_media_buying_launch_post_request import ApiV1AdspacesIdMediaBuyingLaunchPostRequest as ApiV1AdspacesIdMediaBuyingLaunchPostRequest
from goadserver.models.api_v1_adspaces_id_media_buying_report_post_request import ApiV1AdspacesIdMediaBuyingReportPostRequest as ApiV1AdspacesIdMediaBuyingReportPostRequest
from goadserver.models.api_v1_adspaces_id_media_buying_source_bid_put_request import ApiV1AdspacesIdMediaBuyingSourceBidPutRequest as ApiV1AdspacesIdMediaBuyingSourceBidPutRequest
from goadserver.models.api_v1_adspaces_id_media_buying_targeting_put_request import ApiV1AdspacesIdMediaBuyingTargetingPutRequest as ApiV1AdspacesIdMediaBuyingTargetingPutRequest
from goadserver.models.api_v1_adspaces_id_media_buying_targeting_put_request_zones_inner import ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner as ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner
from goadserver.models.api_v1_adspaces_id_network_binding_put_request import ApiV1AdspacesIdNetworkBindingPutRequest as ApiV1AdspacesIdNetworkBindingPutRequest
from goadserver.models.api_v1_adspaces_id_own_ads_mass_action_post_request import ApiV1AdspacesIdOwnAdsMassActionPostRequest as ApiV1AdspacesIdOwnAdsMassActionPostRequest
from goadserver.models.api_v1_adspaces_id_patch200_response import ApiV1AdspacesIdPatch200Response as ApiV1AdspacesIdPatch200Response
from goadserver.models.api_v1_adspaces_id_prices_type_post_request import ApiV1AdspacesIdPricesTypePostRequest as ApiV1AdspacesIdPricesTypePostRequest
from goadserver.models.api_v1_adspaces_id_prices_type_post_request_cpm_price_inner import ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner as ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner
from goadserver.models.api_v1_adspaces_id_wl_campaigns_put_request import ApiV1AdspacesIdWlCampaignsPutRequest as ApiV1AdspacesIdWlCampaignsPutRequest
from goadserver.models.api_v1_adspaces_id_wl_campaigns_put_request_campaigns_inner import ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner as ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner
from goadserver.models.api_v1_adspaces_mass_delete_post_request import ApiV1AdspacesMassDeletePostRequest as ApiV1AdspacesMassDeletePostRequest
from goadserver.models.api_v1_adspaces_mass_recover_post_request import ApiV1AdspacesMassRecoverPostRequest as ApiV1AdspacesMassRecoverPostRequest
from goadserver.models.api_v1_adspaces_templates_get200_response_inner import ApiV1AdspacesTemplatesGet200ResponseInner as ApiV1AdspacesTemplatesGet200ResponseInner
from goadserver.models.api_v1_adspaces_templates_id_put_request import ApiV1AdspacesTemplatesIdPutRequest as ApiV1AdspacesTemplatesIdPutRequest
from goadserver.models.api_v1_adspaces_templates_post_request import ApiV1AdspacesTemplatesPostRequest as ApiV1AdspacesTemplatesPostRequest
from goadserver.models.api_v1_bid_rulesets_get200_response import ApiV1BidRulesetsGet200Response as ApiV1BidRulesetsGet200Response
from goadserver.models.api_v1_bid_rulesets_id_clone_post_request import ApiV1BidRulesetsIdClonePostRequest as ApiV1BidRulesetsIdClonePostRequest
from goadserver.models.api_v1_bid_rulesets_id_delete200_response import ApiV1BidRulesetsIdDelete200Response as ApiV1BidRulesetsIdDelete200Response
from goadserver.models.api_v1_bid_rulesets_id_delete422_response import ApiV1BidRulesetsIdDelete422Response as ApiV1BidRulesetsIdDelete422Response
from goadserver.models.api_v1_bid_rulesets_id_patch_request import ApiV1BidRulesetsIdPatchRequest as ApiV1BidRulesetsIdPatchRequest
from goadserver.models.api_v1_bid_rulesets_post_request import ApiV1BidRulesetsPostRequest as ApiV1BidRulesetsPostRequest
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest as ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest as ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
from goadserver.models.api_v1_campaigns_get200_response import ApiV1CampaignsGet200Response as ApiV1CampaignsGet200Response
from goadserver.models.api_v1_campaigns_get200_response_data_inner import ApiV1CampaignsGet200ResponseDataInner as ApiV1CampaignsGet200ResponseDataInner
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest as ApiV1CampaignsMassDeletePostRequest
from goadserver.models.api_v1_campaigns_mass_toggle_put_request import ApiV1CampaignsMassTogglePutRequest as ApiV1CampaignsMassTogglePutRequest
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get200_response_zone_bids_inner import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200ResponseZoneBidsInner as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200ResponseZoneBidsInner
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request_zone_bids_inner import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequestZoneBidsInner as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequestZoneBidsInner
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest as ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
from goadserver.models.api_v1_campaigns_ron_id_site_list_site_id_put_request import ApiV1CampaignsRonIdSiteListSiteIdPutRequest as ApiV1CampaignsRonIdSiteListSiteIdPutRequest
from goadserver.models.api_v1_campaigns_ron_id_zones_get200_response import ApiV1CampaignsRonIdZonesGet200Response as ApiV1CampaignsRonIdZonesGet200Response
from goadserver.models.api_v1_campaigns_ron_id_zones_get200_response_data_inner import ApiV1CampaignsRonIdZonesGet200ResponseDataInner as ApiV1CampaignsRonIdZonesGet200ResponseDataInner
from goadserver.models.api_v1_campaigns_save_categories_put_request import ApiV1CampaignsSaveCategoriesPutRequest as ApiV1CampaignsSaveCategoriesPutRequest
from goadserver.models.api_v1_campaigns_save_tags_put_request import ApiV1CampaignsSaveTagsPutRequest as ApiV1CampaignsSaveTagsPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response as ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response as ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest as ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest as ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner import ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner as ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response as ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest as ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest as ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_csv_import_post200_response import ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response as ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_from_pool_post_request import ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest as ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response import ApiV1CampaignsTypeCampaignIdAdsGet200Response as ApiV1CampaignsTypeCampaignIdAdsGet200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response_meta import ApiV1CampaignsTypeCampaignIdAdsGet200ResponseMeta as ApiV1CampaignsTypeCampaignIdAdsGet200ResponseMeta
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request import ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest as ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request import ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest as ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request import ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest as ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request import ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest as ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request import ApiV1CampaignsTypeCampaignIdAdsPostRequest as ApiV1CampaignsTypeCampaignIdAdsPostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner import ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner as ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest as ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest as ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest as ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_weight_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest as ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response as ApiV1CampaignsTypeIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest as ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_campaigns_type_id_bids_patch200_response import ApiV1CampaignsTypeIdBidsPatch200Response as ApiV1CampaignsTypeIdBidsPatch200Response
from goadserver.models.api_v1_campaigns_type_id_bids_patch_request import ApiV1CampaignsTypeIdBidsPatchRequest as ApiV1CampaignsTypeIdBidsPatchRequest
from goadserver.models.api_v1_campaigns_type_id_budget_patch200_response import ApiV1CampaignsTypeIdBudgetPatch200Response as ApiV1CampaignsTypeIdBudgetPatch200Response
from goadserver.models.api_v1_campaigns_type_id_budget_patch_request import ApiV1CampaignsTypeIdBudgetPatchRequest as ApiV1CampaignsTypeIdBudgetPatchRequest
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response import ApiV1CampaignsTypeIdClonePost201Response as ApiV1CampaignsTypeIdClonePost201Response
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response_copied import ApiV1CampaignsTypeIdClonePost201ResponseCopied as ApiV1CampaignsTypeIdClonePost201ResponseCopied
from goadserver.models.api_v1_campaigns_type_id_clone_post_request import ApiV1CampaignsTypeIdClonePostRequest as ApiV1CampaignsTypeIdClonePostRequest
from goadserver.models.api_v1_campaigns_type_id_delete200_response import ApiV1CampaignsTypeIdDelete200Response as ApiV1CampaignsTypeIdDelete200Response
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response import ApiV1CampaignsTypeIdFiltersGet200Response as ApiV1CampaignsTypeIdFiltersGet200Response
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response_filters_inner import ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner as ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner
from goadserver.models.api_v1_campaigns_type_id_filters_post200_response import ApiV1CampaignsTypeIdFiltersPost200Response as ApiV1CampaignsTypeIdFiltersPost200Response
from goadserver.models.api_v1_campaigns_type_id_filters_post_request import ApiV1CampaignsTypeIdFiltersPostRequest as ApiV1CampaignsTypeIdFiltersPostRequest
from goadserver.models.api_v1_campaigns_type_id_min_bid_get200_response import ApiV1CampaignsTypeIdMinBidGet200Response as ApiV1CampaignsTypeIdMinBidGet200Response
from goadserver.models.api_v1_campaigns_type_id_patch_request import ApiV1CampaignsTypeIdPatchRequest as ApiV1CampaignsTypeIdPatchRequest
from goadserver.models.api_v1_campaigns_type_id_patch_request_all_of_banner_size_ids import ApiV1CampaignsTypeIdPatchRequestAllOfBannerSizeIds as ApiV1CampaignsTypeIdPatchRequestAllOfBannerSizeIds
from goadserver.models.api_v1_campaigns_type_id_zones_post_request import ApiV1CampaignsTypeIdZonesPostRequest as ApiV1CampaignsTypeIdZonesPostRequest
from goadserver.models.api_v1_campaigns_type_id_zones_zone_id_weight_put_request import ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest as ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
from goadserver.models.api_v1_campaigns_type_post_request import ApiV1CampaignsTypePostRequest as ApiV1CampaignsTypePostRequest
from goadserver.models.api_v1_campaigns_type_post_request_all_of_banner_size_ids import ApiV1CampaignsTypePostRequestAllOfBannerSizeIds as ApiV1CampaignsTypePostRequestAllOfBannerSizeIds
from goadserver.models.api_v1_campaigns_type_post_request_all_of_priority import ApiV1CampaignsTypePostRequestAllOfPriority as ApiV1CampaignsTypePostRequestAllOfPriority
from goadserver.models.api_v1_campaigns_type_schema_ads_get200_response import ApiV1CampaignsTypeSchemaAdsGet200Response as ApiV1CampaignsTypeSchemaAdsGet200Response
from goadserver.models.api_v1_campaigns_type_schema_get200_response import ApiV1CampaignsTypeSchemaGet200Response as ApiV1CampaignsTypeSchemaGet200Response
from goadserver.models.api_v1_campaigns_type_schema_get200_response_fields_inner import ApiV1CampaignsTypeSchemaGet200ResponseFieldsInner as ApiV1CampaignsTypeSchemaGet200ResponseFieldsInner
from goadserver.models.api_v1_coupons_sets_id_generate_post_request import ApiV1CouponsSetsIdGeneratePostRequest as ApiV1CouponsSetsIdGeneratePostRequest
from goadserver.models.api_v1_coupons_sets_id_put_request import ApiV1CouponsSetsIdPutRequest as ApiV1CouponsSetsIdPutRequest
from goadserver.models.api_v1_coupons_sets_post_request import ApiV1CouponsSetsPostRequest as ApiV1CouponsSetsPostRequest
from goadserver.models.api_v1_creative_folders_id_put_request import ApiV1CreativeFoldersIdPutRequest as ApiV1CreativeFoldersIdPutRequest
from goadserver.models.api_v1_creative_folders_post_request import ApiV1CreativeFoldersPostRequest as ApiV1CreativeFoldersPostRequest
from goadserver.models.api_v1_creative_pools_get200_response import ApiV1CreativePoolsGet200Response as ApiV1CreativePoolsGet200Response
from goadserver.models.api_v1_creative_pools_get200_response_data_inner import ApiV1CreativePoolsGet200ResponseDataInner as ApiV1CreativePoolsGet200ResponseDataInner
from goadserver.models.api_v1_creative_pools_get_per_page_parameter import ApiV1CreativePoolsGetPerPageParameter as ApiV1CreativePoolsGetPerPageParameter
from goadserver.models.api_v1_creative_pools_id_add_creatives_post_request import ApiV1CreativePoolsIdAddCreativesPostRequest as ApiV1CreativePoolsIdAddCreativesPostRequest
from goadserver.models.api_v1_creative_pools_id_add_urls_post_request import ApiV1CreativePoolsIdAddUrlsPostRequest as ApiV1CreativePoolsIdAddUrlsPostRequest
from goadserver.models.api_v1_creative_pools_id_clone_post201_response import ApiV1CreativePoolsIdClonePost201Response as ApiV1CreativePoolsIdClonePost201Response
from goadserver.models.api_v1_creative_pools_id_delete200_response import ApiV1CreativePoolsIdDelete200Response as ApiV1CreativePoolsIdDelete200Response
from goadserver.models.api_v1_creative_pools_id_delete409_response import ApiV1CreativePoolsIdDelete409Response as ApiV1CreativePoolsIdDelete409Response
from goadserver.models.api_v1_creative_pools_id_get200_response import ApiV1CreativePoolsIdGet200Response as ApiV1CreativePoolsIdGet200Response
from goadserver.models.api_v1_creative_pools_id_items_item_id_put409_response import ApiV1CreativePoolsIdItemsItemIdPut409Response as ApiV1CreativePoolsIdItemsItemIdPut409Response
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request import ApiV1CreativePoolsIdItemsItemIdPutRequest as ApiV1CreativePoolsIdItemsItemIdPutRequest
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request_end_at import ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt as ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request_start_at import ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt as ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt
from goadserver.models.api_v1_creative_pools_id_items_mass_action_put_request import ApiV1CreativePoolsIdItemsMassActionPutRequest as ApiV1CreativePoolsIdItemsMassActionPutRequest
from goadserver.models.api_v1_creative_pools_id_items_post_request import ApiV1CreativePoolsIdItemsPostRequest as ApiV1CreativePoolsIdItemsPostRequest
from goadserver.models.api_v1_creative_pools_id_items_recover_post_request import ApiV1CreativePoolsIdItemsRecoverPostRequest as ApiV1CreativePoolsIdItemsRecoverPostRequest
from goadserver.models.api_v1_creative_pools_id_put_request import ApiV1CreativePoolsIdPutRequest as ApiV1CreativePoolsIdPutRequest
from goadserver.models.api_v1_creative_pools_id_used_in_get200_response import ApiV1CreativePoolsIdUsedInGet200Response as ApiV1CreativePoolsIdUsedInGet200Response
from goadserver.models.api_v1_creative_pools_post_request import ApiV1CreativePoolsPostRequest as ApiV1CreativePoolsPostRequest
from goadserver.models.api_v1_creatives_bulk_delete_post_request import ApiV1CreativesBulkDeletePostRequest as ApiV1CreativesBulkDeletePostRequest
from goadserver.models.api_v1_creatives_bulk_move_post_request import ApiV1CreativesBulkMovePostRequest as ApiV1CreativesBulkMovePostRequest
from goadserver.models.api_v1_creatives_bulk_undelete_post_request import ApiV1CreativesBulkUndeletePostRequest as ApiV1CreativesBulkUndeletePostRequest
from goadserver.models.api_v1_creatives_get200_response import ApiV1CreativesGet200Response as ApiV1CreativesGet200Response
from goadserver.models.api_v1_creatives_get_per_page_parameter import ApiV1CreativesGetPerPageParameter as ApiV1CreativesGetPerPageParameter
from goadserver.models.api_v1_creatives_id_name_put_request import ApiV1CreativesIdNamePutRequest as ApiV1CreativesIdNamePutRequest
from goadserver.models.api_v1_creatives_id_put_request import ApiV1CreativesIdPutRequest as ApiV1CreativesIdPutRequest
from goadserver.models.api_v1_creatives_id_put_request_tags import ApiV1CreativesIdPutRequestTags as ApiV1CreativesIdPutRequestTags
from goadserver.models.api_v1_creatives_id_tags_put_request import ApiV1CreativesIdTagsPutRequest as ApiV1CreativesIdTagsPutRequest
from goadserver.models.api_v1_domains_id_notes_put_request import ApiV1DomainsIdNotesPutRequest as ApiV1DomainsIdNotesPutRequest
from goadserver.models.api_v1_domains_post_request import ApiV1DomainsPostRequest as ApiV1DomainsPostRequest
from goadserver.models.api_v1_event_log_exports_post_request import ApiV1EventLogExportsPostRequest as ApiV1EventLogExportsPostRequest
from goadserver.models.api_v1_events_get200_response import ApiV1EventsGet200Response as ApiV1EventsGet200Response
from goadserver.models.api_v1_filters_get200_response import ApiV1FiltersGet200Response as ApiV1FiltersGet200Response
from goadserver.models.api_v1_filters_mass_action_post_request import ApiV1FiltersMassActionPostRequest as ApiV1FiltersMassActionPostRequest
from goadserver.models.api_v1_filters_mass_action_post_request_filters_inner import ApiV1FiltersMassActionPostRequestFiltersInner as ApiV1FiltersMassActionPostRequestFiltersInner
from goadserver.models.api_v1_filters_post_request import ApiV1FiltersPostRequest as ApiV1FiltersPostRequest
from goadserver.models.api_v1_filters_type_id_active_patch200_response import ApiV1FiltersTypeIdActivePatch200Response as ApiV1FiltersTypeIdActivePatch200Response
from goadserver.models.api_v1_filters_type_id_items_item_delete200_response import ApiV1FiltersTypeIdItemsItemDelete200Response as ApiV1FiltersTypeIdItemsItemDelete200Response
from goadserver.models.api_v1_filters_type_id_items_post200_response import ApiV1FiltersTypeIdItemsPost200Response as ApiV1FiltersTypeIdItemsPost200Response
from goadserver.models.api_v1_filters_type_id_items_post_request import ApiV1FiltersTypeIdItemsPostRequest as ApiV1FiltersTypeIdItemsPostRequest
from goadserver.models.api_v1_filters_type_id_put_request import ApiV1FiltersTypeIdPutRequest as ApiV1FiltersTypeIdPutRequest
from goadserver.models.api_v1_funds_balance_settings_put_request import ApiV1FundsBalanceSettingsPutRequest as ApiV1FundsBalanceSettingsPutRequest
from goadserver.models.api_v1_funds_deposit_type_fid_get200_response import ApiV1FundsDepositTypeFidGet200Response as ApiV1FundsDepositTypeFidGet200Response
from goadserver.models.api_v1_funds_deposit_type_post200_response import ApiV1FundsDepositTypePost200Response as ApiV1FundsDepositTypePost200Response
from goadserver.models.api_v1_funds_deposit_type_post_request import ApiV1FundsDepositTypePostRequest as ApiV1FundsDepositTypePostRequest
from goadserver.models.api_v1_funds_deposits_id_proof_post200_response import ApiV1FundsDepositsIdProofPost200Response as ApiV1FundsDepositsIdProofPost200Response
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post200_response import ApiV1FundsDepositsIdTxnHashPost200Response as ApiV1FundsDepositsIdTxnHashPost200Response
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post_request import ApiV1FundsDepositsIdTxnHashPostRequest as ApiV1FundsDepositsIdTxnHashPostRequest
from goadserver.models.api_v1_funds_get200_response import ApiV1FundsGet200Response as ApiV1FundsGet200Response
from goadserver.models.api_v1_funds_pay_types_get200_response import ApiV1FundsPayTypesGet200Response as ApiV1FundsPayTypesGet200Response
from goadserver.models.api_v1_funds_pay_types_get200_response_pay_types_inner import ApiV1FundsPayTypesGet200ResponsePayTypesInner as ApiV1FundsPayTypesGet200ResponsePayTypesInner
from goadserver.models.api_v1_funds_transactions_get200_response import ApiV1FundsTransactionsGet200Response as ApiV1FundsTransactionsGet200Response
from goadserver.models.api_v1_funds_transactions_get200_response_data_inner import ApiV1FundsTransactionsGet200ResponseDataInner as ApiV1FundsTransactionsGet200ResponseDataInner
from goadserver.models.api_v1_funds_transfer_post_request import ApiV1FundsTransferPostRequest as ApiV1FundsTransferPostRequest
from goadserver.models.api_v1_lookups_adspace_types_get200_response import ApiV1LookupsAdspaceTypesGet200Response as ApiV1LookupsAdspaceTypesGet200Response
from goadserver.models.api_v1_lookups_banner_sizes_get200_response import ApiV1LookupsBannerSizesGet200Response as ApiV1LookupsBannerSizesGet200Response
from goadserver.models.api_v1_lookups_banner_sizes_get200_response_items_inner import ApiV1LookupsBannerSizesGet200ResponseItemsInner as ApiV1LookupsBannerSizesGet200ResponseItemsInner
from goadserver.models.api_v1_lookups_browsers_get200_response import ApiV1LookupsBrowsersGet200Response as ApiV1LookupsBrowsersGet200Response
from goadserver.models.api_v1_lookups_carriers_get200_response import ApiV1LookupsCarriersGet200Response as ApiV1LookupsCarriersGet200Response
from goadserver.models.api_v1_lookups_carriers_get200_response_data_inner import ApiV1LookupsCarriersGet200ResponseDataInner as ApiV1LookupsCarriersGet200ResponseDataInner
from goadserver.models.api_v1_lookups_categories_get200_response import ApiV1LookupsCategoriesGet200Response as ApiV1LookupsCategoriesGet200Response
from goadserver.models.api_v1_lookups_categories_get200_response_items_inner import ApiV1LookupsCategoriesGet200ResponseItemsInner as ApiV1LookupsCategoriesGet200ResponseItemsInner
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response as ApiV1LookupsDeviceTypesGet200Response
from goadserver.models.api_v1_lookups_regions_get200_response import ApiV1LookupsRegionsGet200Response as ApiV1LookupsRegionsGet200Response
from goadserver.models.api_v1_lookups_regions_get200_response_regions_inner import ApiV1LookupsRegionsGet200ResponseRegionsInner as ApiV1LookupsRegionsGet200ResponseRegionsInner
from goadserver.models.api_v1_lookups_website_languages_get200_response import ApiV1LookupsWebsiteLanguagesGet200Response as ApiV1LookupsWebsiteLanguagesGet200Response
from goadserver.models.api_v1_lookups_website_languages_get200_response_items_inner import ApiV1LookupsWebsiteLanguagesGet200ResponseItemsInner as ApiV1LookupsWebsiteLanguagesGet200ResponseItemsInner
from goadserver.models.api_v1_marketplace_flat_requests_renew_post_request import ApiV1MarketplaceFlatRequestsRenewPostRequest as ApiV1MarketplaceFlatRequestsRenewPostRequest
from goadserver.models.api_v1_mcp_post200_response import ApiV1McpPost200Response as ApiV1McpPost200Response
from goadserver.models.api_v1_mcp_post200_response_error import ApiV1McpPost200ResponseError as ApiV1McpPost200ResponseError
from goadserver.models.api_v1_mcp_post200_response_id import ApiV1McpPost200ResponseId as ApiV1McpPost200ResponseId
from goadserver.models.api_v1_mcp_post_request import ApiV1McpPostRequest as ApiV1McpPostRequest
from goadserver.models.api_v1_mcp_post_request_id import ApiV1McpPostRequestId as ApiV1McpPostRequestId
from goadserver.models.api_v1_offers_get200_response import ApiV1OffersGet200Response as ApiV1OffersGet200Response
from goadserver.models.api_v1_offers_get200_response_data_inner import ApiV1OffersGet200ResponseDataInner as ApiV1OffersGet200ResponseDataInner
from goadserver.models.api_v1_product_feeds_post_request import ApiV1ProductFeedsPostRequest as ApiV1ProductFeedsPostRequest
from goadserver.models.api_v1_product_feeds_preview_post_request import ApiV1ProductFeedsPreviewPostRequest as ApiV1ProductFeedsPreviewPostRequest
from goadserver.models.api_v1_product_feeds_preview_post_request_product import ApiV1ProductFeedsPreviewPostRequestProduct as ApiV1ProductFeedsPreviewPostRequestProduct
from goadserver.models.api_v1_publisher_filters_get200_response import ApiV1PublisherFiltersGet200Response as ApiV1PublisherFiltersGet200Response
from goadserver.models.api_v1_publisher_filters_get200_response_categories_inner import ApiV1PublisherFiltersGet200ResponseCategoriesInner as ApiV1PublisherFiltersGet200ResponseCategoriesInner
from goadserver.models.api_v1_publisher_filters_get200_response_urls_inner import ApiV1PublisherFiltersGet200ResponseUrlsInner as ApiV1PublisherFiltersGet200ResponseUrlsInner
from goadserver.models.api_v1_publisher_filters_urls_delete200_response import ApiV1PublisherFiltersUrlsDelete200Response as ApiV1PublisherFiltersUrlsDelete200Response
from goadserver.models.api_v1_publisher_filters_urls_delete_request import ApiV1PublisherFiltersUrlsDeleteRequest as ApiV1PublisherFiltersUrlsDeleteRequest
from goadserver.models.api_v1_publisher_filters_urls_post201_response import ApiV1PublisherFiltersUrlsPost201Response as ApiV1PublisherFiltersUrlsPost201Response
from goadserver.models.api_v1_publisher_filters_urls_post_request import ApiV1PublisherFiltersUrlsPostRequest as ApiV1PublisherFiltersUrlsPostRequest
from goadserver.models.api_v1_publisher_finance_earnings_get200_response import ApiV1PublisherFinanceEarningsGet200Response as ApiV1PublisherFinanceEarningsGet200Response
from goadserver.models.api_v1_publisher_finance_earnings_get200_response_earnings_inner import ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner as ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner
from goadserver.models.api_v1_publisher_finance_earnings_get200_response_period import ApiV1PublisherFinanceEarningsGet200ResponsePeriod as ApiV1PublisherFinanceEarningsGet200ResponsePeriod
from goadserver.models.api_v1_publisher_finance_earnings_get200_response_summary import ApiV1PublisherFinanceEarningsGet200ResponseSummary as ApiV1PublisherFinanceEarningsGet200ResponseSummary
from goadserver.models.api_v1_publisher_finance_get200_response import ApiV1PublisherFinanceGet200Response as ApiV1PublisherFinanceGet200Response
from goadserver.models.api_v1_publisher_finance_get200_response_balance import ApiV1PublisherFinanceGet200ResponseBalance as ApiV1PublisherFinanceGet200ResponseBalance
from goadserver.models.api_v1_publisher_finance_month_earnings_get200_response_inner import ApiV1PublisherFinanceMonthEarningsGet200ResponseInner as ApiV1PublisherFinanceMonthEarningsGet200ResponseInner
from goadserver.models.api_v1_publisher_finance_payout_request_post201_response import ApiV1PublisherFinancePayoutRequestPost201Response as ApiV1PublisherFinancePayoutRequestPost201Response
from goadserver.models.api_v1_publisher_finance_payout_request_post201_response_payout import ApiV1PublisherFinancePayoutRequestPost201ResponsePayout as ApiV1PublisherFinancePayoutRequestPost201ResponsePayout
from goadserver.models.api_v1_publisher_finance_payout_request_post_request import ApiV1PublisherFinancePayoutRequestPostRequest as ApiV1PublisherFinancePayoutRequestPostRequest
from goadserver.models.api_v1_publisher_finance_payout_types_get200_response_inner import ApiV1PublisherFinancePayoutTypesGet200ResponseInner as ApiV1PublisherFinancePayoutTypesGet200ResponseInner
from goadserver.models.api_v1_publisher_finance_payouts_get200_response import ApiV1PublisherFinancePayoutsGet200Response as ApiV1PublisherFinancePayoutsGet200Response
from goadserver.models.api_v1_publisher_finance_payouts_get200_response_data_inner import ApiV1PublisherFinancePayoutsGet200ResponseDataInner as ApiV1PublisherFinancePayoutsGet200ResponseDataInner
from goadserver.models.api_v1_publisher_finance_payouts_get200_response_meta import ApiV1PublisherFinancePayoutsGet200ResponseMeta as ApiV1PublisherFinancePayoutsGet200ResponseMeta
from goadserver.models.api_v1_publisher_finance_settings_get200_response import ApiV1PublisherFinanceSettingsGet200Response as ApiV1PublisherFinanceSettingsGet200Response
from goadserver.models.api_v1_publisher_finance_settings_get200_response_data import ApiV1PublisherFinanceSettingsGet200ResponseData as ApiV1PublisherFinanceSettingsGet200ResponseData
from goadserver.models.api_v1_publisher_finance_settings_put_request import ApiV1PublisherFinanceSettingsPutRequest as ApiV1PublisherFinanceSettingsPutRequest
from goadserver.models.api_v1_publisher_finance_transactions_get200_response import ApiV1PublisherFinanceTransactionsGet200Response as ApiV1PublisherFinanceTransactionsGet200Response
from goadserver.models.api_v1_publisher_finance_transactions_get200_response_data_inner import ApiV1PublisherFinanceTransactionsGet200ResponseDataInner as ApiV1PublisherFinanceTransactionsGet200ResponseDataInner
from goadserver.models.api_v1_publisher_finance_transactions_id_get200_response import ApiV1PublisherFinanceTransactionsIdGet200Response as ApiV1PublisherFinanceTransactionsIdGet200Response
from goadserver.models.api_v1_publisher_finance_transfer_to_advertiser_post200_response import ApiV1PublisherFinanceTransferToAdvertiserPost200Response as ApiV1PublisherFinanceTransferToAdvertiserPost200Response
from goadserver.models.api_v1_publisher_finance_transfer_to_advertiser_post_request import ApiV1PublisherFinanceTransferToAdvertiserPostRequest as ApiV1PublisherFinanceTransferToAdvertiserPostRequest
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response import ApiV1PublisherOffersPostbackLogGet200Response as ApiV1PublisherOffersPostbackLogGet200Response
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response_data_inner import ApiV1PublisherOffersPostbackLogGet200ResponseDataInner as ApiV1PublisherOffersPostbackLogGet200ResponseDataInner
from goadserver.models.api_v1_publisher_push_campaigns_get200_response import ApiV1PublisherPushCampaignsGet200Response as ApiV1PublisherPushCampaignsGet200Response
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response as ApiV1PublisherPushCampaignsIdDelete200Response
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response_data import ApiV1PublisherPushCampaignsIdDelete200ResponseData as ApiV1PublisherPushCampaignsIdDelete200ResponseData
from goadserver.models.api_v1_publisher_push_campaigns_id_send_post200_response import ApiV1PublisherPushCampaignsIdSendPost200Response as ApiV1PublisherPushCampaignsIdSendPost200Response
from goadserver.models.api_v1_publisher_push_campaigns_id_send_post200_response_data import ApiV1PublisherPushCampaignsIdSendPost200ResponseData as ApiV1PublisherPushCampaignsIdSendPost200ResponseData
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response as ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_campaigns_post_request import ApiV1PublisherPushCampaignsPostRequest as ApiV1PublisherPushCampaignsPostRequest
from goadserver.models.api_v1_publisher_push_delivery_rules_get200_response import ApiV1PublisherPushDeliveryRulesGet200Response as ApiV1PublisherPushDeliveryRulesGet200Response
from goadserver.models.api_v1_publisher_push_delivery_rules_id_put_request import ApiV1PublisherPushDeliveryRulesIdPutRequest as ApiV1PublisherPushDeliveryRulesIdPutRequest
from goadserver.models.api_v1_publisher_push_delivery_rules_post_request import ApiV1PublisherPushDeliveryRulesPostRequest as ApiV1PublisherPushDeliveryRulesPostRequest
from goadserver.models.api_v1_publisher_push_segments_get200_response import ApiV1PublisherPushSegmentsGet200Response as ApiV1PublisherPushSegmentsGet200Response
from goadserver.models.api_v1_publisher_push_segments_id_put_request import ApiV1PublisherPushSegmentsIdPutRequest as ApiV1PublisherPushSegmentsIdPutRequest
from goadserver.models.api_v1_publisher_push_segments_post_request import ApiV1PublisherPushSegmentsPostRequest as ApiV1PublisherPushSegmentsPostRequest
from goadserver.models.api_v1_publisher_push_setup_get200_response import ApiV1PublisherPushSetupGet200Response as ApiV1PublisherPushSetupGet200Response
from goadserver.models.api_v1_publisher_push_setup_get200_response_data import ApiV1PublisherPushSetupGet200ResponseData as ApiV1PublisherPushSetupGet200ResponseData
from goadserver.models.api_v1_publisher_push_setup_get200_response_data_adzones_inner import ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner as ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner
from goadserver.models.api_v1_publisher_push_stats_get200_response import ApiV1PublisherPushStatsGet200Response as ApiV1PublisherPushStatsGet200Response
from goadserver.models.api_v1_publisher_push_stats_get200_response_data import ApiV1PublisherPushStatsGet200ResponseData as ApiV1PublisherPushStatsGet200ResponseData
from goadserver.models.api_v1_publisher_push_stats_get200_response_data_daily_inner import ApiV1PublisherPushStatsGet200ResponseDataDailyInner as ApiV1PublisherPushStatsGet200ResponseDataDailyInner
from goadserver.models.api_v1_publisher_push_stats_get200_response_data_growth_inner import ApiV1PublisherPushStatsGet200ResponseDataGrowthInner as ApiV1PublisherPushStatsGet200ResponseDataGrowthInner
from goadserver.models.api_v1_publisher_push_stats_get200_response_data_summary import ApiV1PublisherPushStatsGet200ResponseDataSummary as ApiV1PublisherPushStatsGet200ResponseDataSummary
from goadserver.models.api_v1_publisher_push_subscribers_action_post200_response import ApiV1PublisherPushSubscribersActionPost200Response as ApiV1PublisherPushSubscribersActionPost200Response
from goadserver.models.api_v1_publisher_push_subscribers_action_post200_response_data import ApiV1PublisherPushSubscribersActionPost200ResponseData as ApiV1PublisherPushSubscribersActionPost200ResponseData
from goadserver.models.api_v1_publisher_push_subscribers_action_post_request import ApiV1PublisherPushSubscribersActionPostRequest as ApiV1PublisherPushSubscribersActionPostRequest
from goadserver.models.api_v1_publisher_push_subscribers_get200_response import ApiV1PublisherPushSubscribersGet200Response as ApiV1PublisherPushSubscribersGet200Response
from goadserver.models.api_v1_publisher_push_subscribers_get200_response_data import ApiV1PublisherPushSubscribersGet200ResponseData as ApiV1PublisherPushSubscribersGet200ResponseData
from goadserver.models.api_v1_publisher_smartzones_id_put_request import ApiV1PublisherSmartzonesIdPutRequest as ApiV1PublisherSmartzonesIdPutRequest
from goadserver.models.api_v1_publisher_smartzones_id_put_request_is_active import ApiV1PublisherSmartzonesIdPutRequestIsActive as ApiV1PublisherSmartzonesIdPutRequestIsActive
from goadserver.models.api_v1_publisher_smartzones_id_put_request_unique_only import ApiV1PublisherSmartzonesIdPutRequestUniqueOnly as ApiV1PublisherSmartzonesIdPutRequestUniqueOnly
from goadserver.models.api_v1_publisher_smartzones_import_post_request import ApiV1PublisherSmartzonesImportPostRequest as ApiV1PublisherSmartzonesImportPostRequest
from goadserver.models.api_v1_publisher_smartzones_import_post_request_zones_inner import ApiV1PublisherSmartzonesImportPostRequestZonesInner as ApiV1PublisherSmartzonesImportPostRequestZonesInner
from goadserver.models.api_v1_publisher_smartzones_networks_post_request import ApiV1PublisherSmartzonesNetworksPostRequest as ApiV1PublisherSmartzonesNetworksPostRequest
from goadserver.models.api_v1_publisher_smartzones_post_request import ApiV1PublisherSmartzonesPostRequest as ApiV1PublisherSmartzonesPostRequest
from goadserver.models.api_v1_publisher_ssp_campaigns_id_test_rtb_post_request import ApiV1PublisherSspCampaignsIdTestRtbPostRequest as ApiV1PublisherSspCampaignsIdTestRtbPostRequest
from goadserver.models.api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request import ApiV1PublisherSspCampaignsIdToggleDeletePutRequest as ApiV1PublisherSspCampaignsIdToggleDeletePutRequest
from goadserver.models.api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request import ApiV1PublisherSspCampaignsIdTogglePausePutRequest as ApiV1PublisherSspCampaignsIdTogglePausePutRequest
from goadserver.models.api_v1_publisher_ssp_seller_disclosure_put_request import ApiV1PublisherSspSellerDisclosurePutRequest as ApiV1PublisherSspSellerDisclosurePutRequest
from goadserver.models.api_v1_retargeting_pixels_get200_response import ApiV1RetargetingPixelsGet200Response as ApiV1RetargetingPixelsGet200Response
from goadserver.models.api_v1_retargeting_pixels_id_active_patch200_response import ApiV1RetargetingPixelsIdActivePatch200Response as ApiV1RetargetingPixelsIdActivePatch200Response
from goadserver.models.api_v1_retargeting_pixels_id_delete200_response import ApiV1RetargetingPixelsIdDelete200Response as ApiV1RetargetingPixelsIdDelete200Response
from goadserver.models.api_v1_rtb_test_rtb_post_request import ApiV1RtbTestRtbPostRequest as ApiV1RtbTestRtbPostRequest
from goadserver.models.api_v1_shared_reports_id_put_request import ApiV1SharedReportsIdPutRequest as ApiV1SharedReportsIdPutRequest
from goadserver.models.api_v1_shared_reports_id_put_request_campaigns_inner import ApiV1SharedReportsIdPutRequestCampaignsInner as ApiV1SharedReportsIdPutRequestCampaignsInner
from goadserver.models.api_v1_shared_reports_id_put_request_sites_inner import ApiV1SharedReportsIdPutRequestSitesInner as ApiV1SharedReportsIdPutRequestSitesInner
from goadserver.models.api_v1_sites_get200_response import ApiV1SitesGet200Response as ApiV1SitesGet200Response
from goadserver.models.api_v1_sites_get200_response_data_inner import ApiV1SitesGet200ResponseDataInner as ApiV1SitesGet200ResponseDataInner
from goadserver.models.api_v1_sites_id_clone_post_request import ApiV1SitesIdClonePostRequest as ApiV1SitesIdClonePostRequest
from goadserver.models.api_v1_sites_schema_get200_response import ApiV1SitesSchemaGet200Response as ApiV1SitesSchemaGet200Response
from goadserver.models.api_v1_sites_schema_get200_response_fields_inner import ApiV1SitesSchemaGet200ResponseFieldsInner as ApiV1SitesSchemaGet200ResponseFieldsInner
from goadserver.models.api_v1_tags_id_put_request import ApiV1TagsIdPutRequest as ApiV1TagsIdPutRequest
from goadserver.models.api_v1_tags_mass_delete_post_request import ApiV1TagsMassDeletePostRequest as ApiV1TagsMassDeletePostRequest
from goadserver.models.api_v1_tags_post_request import ApiV1TagsPostRequest as ApiV1TagsPostRequest
from goadserver.models.api_v1_tools_replace_domain_put_request import ApiV1ToolsReplaceDomainPutRequest as ApiV1ToolsReplaceDomainPutRequest
from goadserver.models.api_v1_tracker_ad_networks_delete_reports_put_request import ApiV1TrackerAdNetworksDeleteReportsPutRequest as ApiV1TrackerAdNetworksDeleteReportsPutRequest
from goadserver.models.api_v1_tracker_ad_networks_id_put_request import ApiV1TrackerAdNetworksIdPutRequest as ApiV1TrackerAdNetworksIdPutRequest
from goadserver.models.api_v1_tracker_ad_networks_post_request import ApiV1TrackerAdNetworksPostRequest as ApiV1TrackerAdNetworksPostRequest
from goadserver.models.api_v1_tracker_affiliate_networks_get200_response import ApiV1TrackerAffiliateNetworksGet200Response as ApiV1TrackerAffiliateNetworksGet200Response
from goadserver.models.api_v1_tracker_affiliate_networks_id_put_request import ApiV1TrackerAffiliateNetworksIdPutRequest as ApiV1TrackerAffiliateNetworksIdPutRequest
from goadserver.models.api_v1_tracker_affiliate_networks_post_request import ApiV1TrackerAffiliateNetworksPostRequest as ApiV1TrackerAffiliateNetworksPostRequest
from goadserver.models.api_v1_tracker_conversion_logging_put_request import ApiV1TrackerConversionLoggingPutRequest as ApiV1TrackerConversionLoggingPutRequest
from goadserver.models.api_v1_tracker_conversion_types_put_request import ApiV1TrackerConversionTypesPutRequest as ApiV1TrackerConversionTypesPutRequest
from goadserver.models.api_v1_tracker_conversions_get200_response import ApiV1TrackerConversionsGet200Response as ApiV1TrackerConversionsGet200Response
from goadserver.models.api_v1_tracker_conversions_get200_response_summary import ApiV1TrackerConversionsGet200ResponseSummary as ApiV1TrackerConversionsGet200ResponseSummary
from goadserver.models.api_v1_tracker_conversions_id_state_put_request import ApiV1TrackerConversionsIdStatePutRequest as ApiV1TrackerConversionsIdStatePutRequest
from goadserver.models.api_v1_tracker_custom_params_put_request import ApiV1TrackerCustomParamsPutRequest as ApiV1TrackerCustomParamsPutRequest
from goadserver.models.api_v1_tracker_custom_params_put_request_slots_inner import ApiV1TrackerCustomParamsPutRequestSlotsInner as ApiV1TrackerCustomParamsPutRequestSlotsInner
from goadserver.models.api_v1_tracker_offers_bulk_post_request import ApiV1TrackerOffersBulkPostRequest as ApiV1TrackerOffersBulkPostRequest
from goadserver.models.api_v1_tracker_offers_get200_response import ApiV1TrackerOffersGet200Response as ApiV1TrackerOffersGet200Response
from goadserver.models.api_v1_tracker_offers_id_get200_response import ApiV1TrackerOffersIdGet200Response as ApiV1TrackerOffersIdGet200Response
from goadserver.models.api_v1_tracker_offers_id_put_request import ApiV1TrackerOffersIdPutRequest as ApiV1TrackerOffersIdPutRequest
from goadserver.models.api_v1_tracker_offers_id_urls_post_request import ApiV1TrackerOffersIdUrlsPostRequest as ApiV1TrackerOffersIdUrlsPostRequest
from goadserver.models.api_v1_tracker_offers_id_urls_url_id_put_request import ApiV1TrackerOffersIdUrlsUrlIdPutRequest as ApiV1TrackerOffersIdUrlsUrlIdPutRequest
from goadserver.models.api_v1_tracker_offers_post_request import ApiV1TrackerOffersPostRequest as ApiV1TrackerOffersPostRequest
from goadserver.models.api_v1_tracker_offers_post_request_urls_inner import ApiV1TrackerOffersPostRequestUrlsInner as ApiV1TrackerOffersPostRequestUrlsInner
from goadserver.models.api_v1_tracker_report_schedules_get200_response import ApiV1TrackerReportSchedulesGet200Response as ApiV1TrackerReportSchedulesGet200Response
from goadserver.models.api_v1_tracker_report_schedules_id_get200_response import ApiV1TrackerReportSchedulesIdGet200Response as ApiV1TrackerReportSchedulesIdGet200Response
from goadserver.models.api_v1_tracker_report_schedules_id_put_request import ApiV1TrackerReportSchedulesIdPutRequest as ApiV1TrackerReportSchedulesIdPutRequest
from goadserver.models.api_v1_tracker_report_schedules_post_request import ApiV1TrackerReportSchedulesPostRequest as ApiV1TrackerReportSchedulesPostRequest
from goadserver.models.api_v1_tracker_rules_get200_response import ApiV1TrackerRulesGet200Response as ApiV1TrackerRulesGet200Response
from goadserver.models.api_v1_tracker_rules_id_get200_response import ApiV1TrackerRulesIdGet200Response as ApiV1TrackerRulesIdGet200Response
from goadserver.models.api_v1_tracker_rules_id_put_request import ApiV1TrackerRulesIdPutRequest as ApiV1TrackerRulesIdPutRequest
from goadserver.models.api_v1_tracker_rules_post_request import ApiV1TrackerRulesPostRequest as ApiV1TrackerRulesPostRequest
from goadserver.models.api_v1_tracker_source_accounts_get200_response import ApiV1TrackerSourceAccountsGet200Response as ApiV1TrackerSourceAccountsGet200Response
from goadserver.models.api_v1_tracker_source_accounts_id_get200_response import ApiV1TrackerSourceAccountsIdGet200Response as ApiV1TrackerSourceAccountsIdGet200Response
from goadserver.models.api_v1_tracker_source_accounts_id_put_request import ApiV1TrackerSourceAccountsIdPutRequest as ApiV1TrackerSourceAccountsIdPutRequest
from goadserver.models.api_v1_tracker_source_accounts_post_request import ApiV1TrackerSourceAccountsPostRequest as ApiV1TrackerSourceAccountsPostRequest
from goadserver.models.api_v1_tracker_sources_get200_response import ApiV1TrackerSourcesGet200Response as ApiV1TrackerSourcesGet200Response
from goadserver.models.api_v1_tracker_sources_id_put_request import ApiV1TrackerSourcesIdPutRequest as ApiV1TrackerSourcesIdPutRequest
from goadserver.models.api_v1_tracker_sources_post_request import ApiV1TrackerSourcesPostRequest as ApiV1TrackerSourcesPostRequest
from goadserver.models.api_v1_tracker_tracking_links_bulk_post_request import ApiV1TrackerTrackingLinksBulkPostRequest as ApiV1TrackerTrackingLinksBulkPostRequest
from goadserver.models.api_v1_tracker_tracking_links_get200_response import ApiV1TrackerTrackingLinksGet200Response as ApiV1TrackerTrackingLinksGet200Response
from goadserver.models.api_v1_tracker_tracking_links_id_blocklist_post_request import ApiV1TrackerTrackingLinksIdBlocklistPostRequest as ApiV1TrackerTrackingLinksIdBlocklistPostRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest as ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_block_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest as ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_ips_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest as ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_report_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest as ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request import ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest as ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_targeting_put_request import ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest as ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest
from goadserver.models.api_v1_tracker_tracking_links_id_network_binding_put_request import ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest as ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest
from goadserver.models.api_v1_tracker_tracking_links_id_put_request import ApiV1TrackerTrackingLinksIdPutRequest as ApiV1TrackerTrackingLinksIdPutRequest
from goadserver.models.api_v1_tracker_tracking_links_id_toggle_active_post200_response import ApiV1TrackerTrackingLinksIdToggleActivePost200Response as ApiV1TrackerTrackingLinksIdToggleActivePost200Response
from goadserver.models.api_v1_tracker_tracking_links_id_toggle_active_post200_response_data import ApiV1TrackerTrackingLinksIdToggleActivePost200ResponseData as ApiV1TrackerTrackingLinksIdToggleActivePost200ResponseData
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response as ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
from goadserver.models.api_v1_tracker_tracking_links_post_request import ApiV1TrackerTrackingLinksPostRequest as ApiV1TrackerTrackingLinksPostRequest
from goadserver.models.api_v1_tracking_conversion_types_get200_response import ApiV1TrackingConversionTypesGet200Response as ApiV1TrackingConversionTypesGet200Response
from goadserver.models.api_v1_tracking_conversion_types_get200_response_conversion_types_inner import ApiV1TrackingConversionTypesGet200ResponseConversionTypesInner as ApiV1TrackingConversionTypesGet200ResponseConversionTypesInner
from goadserver.models.api_v1_tracking_conversion_types_put200_response import ApiV1TrackingConversionTypesPut200Response as ApiV1TrackingConversionTypesPut200Response
from goadserver.models.api_v1_tracking_conversion_types_put200_response_conversion_types_inner import ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner as ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner
from goadserver.models.api_v1_tracking_conversion_types_put_request import ApiV1TrackingConversionTypesPutRequest as ApiV1TrackingConversionTypesPutRequest
from goadserver.models.api_v1_tracking_conversion_types_put_request_types_inner import ApiV1TrackingConversionTypesPutRequestTypesInner as ApiV1TrackingConversionTypesPutRequestTypesInner
from goadserver.models.api_v1_tracking_pixels_get200_response import ApiV1TrackingPixelsGet200Response as ApiV1TrackingPixelsGet200Response
from goadserver.models.api_v1_tracking_pixels_id_put_request import ApiV1TrackingPixelsIdPutRequest as ApiV1TrackingPixelsIdPutRequest
from goadserver.models.api_v1_tracking_pixels_post_request import ApiV1TrackingPixelsPostRequest as ApiV1TrackingPixelsPostRequest
from goadserver.models.api_v1_url_pools_id_put_request import ApiV1UrlPoolsIdPutRequest as ApiV1UrlPoolsIdPutRequest
from goadserver.models.api_v1_url_pools_id_urls_post_request import ApiV1UrlPoolsIdUrlsPostRequest as ApiV1UrlPoolsIdUrlsPostRequest
from goadserver.models.api_v1_url_pools_id_urls_url_id_put_request import ApiV1UrlPoolsIdUrlsUrlIdPutRequest as ApiV1UrlPoolsIdUrlsUrlIdPutRequest
from goadserver.models.api_v1_url_pools_id_urls_url_id_weight_put_request import ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest as ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest
from goadserver.models.api_v1_url_pools_post_request import ApiV1UrlPoolsPostRequest as ApiV1UrlPoolsPostRequest
from goadserver.models.api_v1_url_pools_replace_url_put_request import ApiV1UrlPoolsReplaceUrlPutRequest as ApiV1UrlPoolsReplaceUrlPutRequest
from goadserver.models.api_v1_webhooks_get200_response import ApiV1WebhooksGet200Response as ApiV1WebhooksGet200Response
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response as ApiV1WebhooksIdDelete200Response
from goadserver.models.api_v1_webhooks_id_deliveries_get200_response import ApiV1WebhooksIdDeliveriesGet200Response as ApiV1WebhooksIdDeliveriesGet200Response
from goadserver.models.api_v1_webhooks_id_deliveries_get200_response_data_inner import ApiV1WebhooksIdDeliveriesGet200ResponseDataInner as ApiV1WebhooksIdDeliveriesGet200ResponseDataInner
from goadserver.models.api_v1_webhooks_id_patch_request import ApiV1WebhooksIdPatchRequest as ApiV1WebhooksIdPatchRequest
from goadserver.models.api_v1_webhooks_id_rotate_secret_post_request import ApiV1WebhooksIdRotateSecretPostRequest as ApiV1WebhooksIdRotateSecretPostRequest
from goadserver.models.api_v1_webhooks_id_test_post200_response import ApiV1WebhooksIdTestPost200Response as ApiV1WebhooksIdTestPost200Response
from goadserver.models.api_v1_webhooks_id_test_post200_response_data import ApiV1WebhooksIdTestPost200ResponseData as ApiV1WebhooksIdTestPost200ResponseData
from goadserver.models.api_v1_webhooks_post201_response import ApiV1WebhooksPost201Response as ApiV1WebhooksPost201Response
from goadserver.models.api_v1_webhooks_post_request import ApiV1WebhooksPostRequest as ApiV1WebhooksPostRequest
from goadserver.models.api_v1_xml_feeds_id_put_request import ApiV1XmlFeedsIdPutRequest as ApiV1XmlFeedsIdPutRequest
from goadserver.models.api_v1_xml_feeds_post_request import ApiV1XmlFeedsPostRequest as ApiV1XmlFeedsPostRequest
from goadserver.models.bid_rule import BidRule as BidRule
from goadserver.models.bid_rule_conditions import BidRuleConditions as BidRuleConditions
from goadserver.models.bid_ruleset import BidRuleset as BidRuleset
from goadserver.models.bid_ruleset_list_item import BidRulesetListItem as BidRulesetListItem
from goadserver.models.campaign_panel_fields import CampaignPanelFields as CampaignPanelFields
from goadserver.models.campaign_panel_fields_about_settings import CampaignPanelFieldsAboutSettings as CampaignPanelFieldsAboutSettings
from goadserver.models.campaign_panel_fields_av_check import CampaignPanelFieldsAvCheck as CampaignPanelFieldsAvCheck
from goadserver.models.campaign_panel_fields_booster_settings import CampaignPanelFieldsBoosterSettings as CampaignPanelFieldsBoosterSettings
from goadserver.models.campaign_panel_fields_conversion_capping import CampaignPanelFieldsConversionCapping as CampaignPanelFieldsConversionCapping
from goadserver.models.campaign_panel_fields_day_parting import CampaignPanelFieldsDayParting as CampaignPanelFieldsDayParting
from goadserver.models.campaign_panel_fields_domain_mask import CampaignPanelFieldsDomainMask as CampaignPanelFieldsDomainMask
from goadserver.models.campaign_panel_fields_feed_settings import CampaignPanelFieldsFeedSettings as CampaignPanelFieldsFeedSettings
from goadserver.models.campaign_panel_fields_priority import CampaignPanelFieldsPriority as CampaignPanelFieldsPriority
from goadserver.models.campaign_panel_fields_screens import CampaignPanelFieldsScreens as CampaignPanelFieldsScreens
from goadserver.models.campaign_panel_fields_suggestions import CampaignPanelFieldsSuggestions as CampaignPanelFieldsSuggestions
from goadserver.models.cpa_optimizer_body import CpaOptimizerBody as CpaOptimizerBody
from goadserver.models.cpm_optimizer_body import CpmOptimizerBody as CpmOptimizerBody
from goadserver.models.error import Error as Error
from goadserver.models.filter_detail import FilterDetail as FilterDetail
from goadserver.models.filter_detail_all_of_ranges import FilterDetailAllOfRanges as FilterDetailAllOfRanges
from goadserver.models.filter_summary import FilterSummary as FilterSummary
from goadserver.models.filter_type import FilterType as FilterType
from goadserver.models.funds_deposit_proof import FundsDepositProof as FundsDepositProof
from goadserver.models.funds_txn_claim import FundsTxnClaim as FundsTxnClaim
from goadserver.models.list_meta import ListMeta as ListMeta
from goadserver.models.media_buying_policy import MediaBuyingPolicy as MediaBuyingPolicy
from goadserver.models.media_buying_policy_test_phase import MediaBuyingPolicyTestPhase as MediaBuyingPolicyTestPhase
from goadserver.models.own_ad_write import OwnAdWrite as OwnAdWrite
from goadserver.models.push_campaign import PushCampaign as PushCampaign
from goadserver.models.push_delivery_rule import PushDeliveryRule as PushDeliveryRule
from goadserver.models.push_segment import PushSegment as PushSegment
from goadserver.models.push_subscriber import PushSubscriber as PushSubscriber
from goadserver.models.resource_filter import ResourceFilter as ResourceFilter
from goadserver.models.retargeting_pixel import RetargetingPixel as RetargetingPixel
from goadserver.models.retargeting_pixel_write import RetargetingPixelWrite as RetargetingPixelWrite
from goadserver.models.rtb_test_request import RtbTestRequest as RtbTestRequest
from goadserver.models.rtb_test_result import RtbTestResult as RtbTestResult
from goadserver.models.shared_report_adjust import SharedReportAdjust as SharedReportAdjust
from goadserver.models.shared_report_body import SharedReportBody as SharedReportBody
from goadserver.models.shared_report_body_campaigns_inner import SharedReportBodyCampaignsInner as SharedReportBodyCampaignsInner
from goadserver.models.shared_report_body_options import SharedReportBodyOptions as SharedReportBodyOptions
from goadserver.models.shared_report_body_settings import SharedReportBodySettings as SharedReportBodySettings
from goadserver.models.site import Site as Site
from goadserver.models.site_create import SiteCreate as SiteCreate
from goadserver.models.site_snippet_write import SiteSnippetWrite as SiteSnippetWrite
from goadserver.models.site_snippet_write_conditions import SiteSnippetWriteConditions as SiteSnippetWriteConditions
from goadserver.models.ssp_campaign_write import SspCampaignWrite as SspCampaignWrite
from goadserver.models.ssp_campaign_write_slots_inner import SspCampaignWriteSlotsInner as SspCampaignWriteSlotsInner
from goadserver.models.ssp_campaign_write_zoneurls_inner import SspCampaignWriteZoneurlsInner as SspCampaignWriteZoneurlsInner
from goadserver.models.stats_response import StatsResponse as StatsResponse
from goadserver.models.tracker_affiliate_network import TrackerAffiliateNetwork as TrackerAffiliateNetwork
from goadserver.models.tracker_conversion import TrackerConversion as TrackerConversion
from goadserver.models.tracker_offer import TrackerOffer as TrackerOffer
from goadserver.models.tracker_report_schedule import TrackerReportSchedule as TrackerReportSchedule
from goadserver.models.tracker_rule import TrackerRule as TrackerRule
from goadserver.models.tracker_source import TrackerSource as TrackerSource
from goadserver.models.tracker_source_account import TrackerSourceAccount as TrackerSourceAccount
from goadserver.models.tracking_link import TrackingLink as TrackingLink
from goadserver.models.tracking_pixel import TrackingPixel as TrackingPixel
from goadserver.models.user_event import UserEvent as UserEvent
from goadserver.models.user_event_type import UserEventType as UserEventType
from goadserver.models.user_webhook import UserWebhook as UserWebhook


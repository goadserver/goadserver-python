# goadserver-sdk

> Official Python client for the REST API of [GoAdserver](https://www.goadserver.com), the hosted ad server. API documentation and how to create an API key: [GoAdserver API docs](https://www.goadserver.com/docs/api-keys/).
Public REST API for advertisers and publishers on the GoAdServer platform.

**Authentication.** All endpoints (except `/api/public/*`) require an API
key passed as `Authorization: Bearer gas_live_…`. Create and manage keys
in your account settings — each key has its own scopes, optional resource
pinning, optional IP allowlist, and per-key rate limit.

**Apps (OAuth 2.0).** A tool other people connect uses an app token
instead: authorization code + PKCE at `/oauth/authorize`, tokens from
`/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the
same endpoints with the same scopes. See the
[Build an integration](/api/docs/integrations) guide.

**System rules apply over API rules.** The public API never lets a key
bypass restrictions the same user faces in the panel:

- **Source names** (`stats_source_names` right). When the user lacks
  this right, advertiser stats responses return `{id, name}` with
  `name` equal to the id — no human label leaks through.
- **SubID encoding** (`modules.global.subid_encoding`). When enabled
  for the system, the user only ever sees encoded SubIDs in the panel.
  The API mirrors this both ways: `subid_excl`/`subid_incl` filter
  endpoints accept the encoded form on write (decoded server-side
  before storage) and emit the encoded form on read. A plain SubID
  sent on write is stored as sent — a value is decoded only when it is
  a genuine encoded token.
- **Module gating.** Endpoints whose module is disabled for the
  tenant don't appear in the spec or routes.txt at all.

**Rate limits.** Every response to an API key or app token carries the
caller's budget for the current one-minute window:

| Header | Meaning |
|---|---|
| `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). |
| `X-RateLimit-Remaining` | Calls left in the current window. |
| `X-RateLimit-Reset` | Unix seconds at which the window resets. |
| `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |

Windows are fixed and start with the first call, so `Reset` is exact. The
MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own
bucket (default 240/min), and its response headers report that bucket; an
exhausted MCP bucket answers the tool call with an error result rather than
an HTTP 429, and the HTTP response then carries `Retry-After`.

**Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII
characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe.
For 24 hours per key (per app installation for app tokens):

- the first request runs and its response — status, body, `Content-Type`,
  `Location`, `ETag` — is stored;
- the same key with the same method, path, query and body replays that
  response without running anything, adding `Idempotent-Replayed: true`;
- the same key with a different request is `422 idempotency_key_reused`;
- the same key while the first request is still running is
  `409 idempotency_key_in_progress` (with `Retry-After: 1`).

`5xx` results are not stored — the key is released and a retry runs again.
Bodies over 32 MB cannot carry the header (`413`). An invalid key is
`400 invalid_idempotency_key`.

**Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to
1 MB) carries a weak `ETag`, a hash of the body. Send it back:

- `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged;
- `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the
  resource's current representation (the `GET` of the same path, or of the
  nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is
  checked against `GET …/campaigns/ron/7`) and answers
  `412 precondition_failed` when it no longer matches, with the current tag in
  `ETag` and `current_etag`. `If-Match: *` only requires the resource to
  exist. A resource with no readable representation is also `412`.

The check is optimistic, not a lock: it closes the read-modify-write window
two agents (or an agent and a person in the panel) would otherwise race in.
Fields that change on their own (live spend counters) change the tag too —
re-read and retry. A write response carries no new ETag; `GET` again.

**Strict fields.** Unknown body fields are a client error, not something to
ignore: a request that sends a field the endpoint does not accept gets
`422 unknown_fields` naming it. This is the default for keys created from
2026-10-12 (the key's `strict_fields` setting, shown on the key screen);
older keys keep ignoring unknown fields (except on the few endpoints that
have always refused them — the budget and on/off toggles). Override per
request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App
tokens default to ignoring unknown fields; `?strict=1` opts in.

**Errors.** Every non-2xx response has the same shape:

```json
{ \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } }
```

`error` is a stable machine-readable code — branch on it, never on
`message`. `errors` (field → messages) appears on field-level validation
failures; some codes add their own members (`scope`, `accepted_scopes`,
`unknown_fields`, `current_etag`). Codes:

| Status | Codes |
|---|---|
| 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` |
| 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` |
| 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` |
| 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) |
| 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept |
| 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) |
| 412 | `precondition_failed` |
| 413 | `payload_too_large` |
| 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` |
| 429 | `rate_limited` |
| 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |

Endpoint-specific codes are listed on the endpoint. A response that would
otherwise lack a code gets the generic one for its status from this table.

**Client SDKs.** Each SDK is generated from this spec and published as
a public GitHub repository under the `goadserver` organization. The
same tarball is also embedded in the API server and downloadable from
`/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.

> **Per-network host.** The default `https://up.go-adserver.com`
> baked into the published SDKs is a reference host. Every white-label
> tenant runs on its own panel domain — override the host on first use
> (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the
> spec from your own tenant (`/api/public/openapi.yaml` returns it with
> *your* hostname as the default) and regenerate the SDK locally — the
> regenerated client has your URL baked in.

- **PHP** — `github.com/goadserver/goadserver-php`
  (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).

  ```bash
  composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php
  composer require goadserver/sdk:dev-main
  ```

  ```php
  $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()
          ->setHost('https://up.go-adserver.com')
          ->setAccessToken('gas_live_…');
  $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);
  $me  = $api->apiV1AccountGet();
  ```

- **Go** — `github.com/goadserver/goadserver-go`.

  ```bash
  go get github.com/goadserver/goadserver-go@latest
  ```

  ```go
  import gas \"github.com/goadserver/goadserver-go\"

  cfg := gas.NewConfiguration()
  cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}
  cli := gas.NewAPIClient(cfg)
  ctx := context.WithValue(context.Background(),
      gas.ContextAccessToken, \"gas_live_…\")
  me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()
  ```

- **Python** — `github.com/goadserver/goadserver-python` (package
  `goadserver`). Pulls `pydantic` + `urllib3` automatically.

  ```bash
  pip install git+https://github.com/goadserver/goadserver-python.git
  ```

  ```python
  from goadserver import ApiClient, Configuration
  from goadserver.api import AccountApi, CampaignsApi

  cfg = Configuration(host=\"https://up.go-adserver.com\")
  cfg.access_token = \"gas_live_…\"
  client = ApiClient(cfg)

  me = AccountApi(client).api_v1_account_get()
  camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)
  ```

- **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`
  (npm name `goadserver-sdk`, generator `typescript-fetch`).

  ```bash
  npm install github:goadserver/goadserver-js
  ```

  ```ts
  import { Configuration, AccountApi, CampaignsApi }
    from \"goadserver-sdk\";

  const cfg = new Configuration({
    basePath: \"https://up.go-adserver.com\",
    accessToken: \"gas_live_…\",
  });

  const me   = await new AccountApi(cfg).apiV1AccountGet();
  const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });
  ```

  The CJS build is broadly compatible (Node + bundlers); the ESM
  build is missing trailing `.js` extensions in its imports, a known
  `typescript-fetch` quirk — most consumers use CJS.

**Offline / firewalled install.** If the customer's network can't
reach GitHub, every SDK's source is also served as a tarball from the
API host:

```bash
curl -O https://up.go-adserver.com/api/public/sdk/python.tgz
tar xzf python.tgz && pip install ./python
```

Round-trip smoke tests for all four SDKs live at `clients/_smoke/`
in the platform repo.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.1.0
- Generator version: 7.21.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/goadserver/goadserver-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/goadserver/goadserver-python.git`)

Then import the package:
```python
import goadserver
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import goadserver
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AIAssistantApi(api_client)
    api_v1_mcp_post_request = goadserver.ApiV1McpPostRequest() # ApiV1McpPostRequest | 

    try:
        # MCP endpoint — connect an AI assistant to this account.
        api_response = api_instance.api_v1_mcp_post(api_v1_mcp_post_request)
        print("The response of AIAssistantApi->api_v1_mcp_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIAssistantApi->api_v1_mcp_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://up.go-adserver.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AIAssistantApi* | [**api_v1_mcp_post**](docs/AIAssistantApi.md#api_v1_mcp_post) | **POST** /api/v1/mcp | MCP endpoint — connect an AI assistant to this account.
*AccountApi* | [**api_v1_account_features_get**](docs/AccountApi.md#api_v1_account_features_get) | **GET** /api/v1/account/features | Self-service features and their state.
*AccountApi* | [**api_v1_account_get**](docs/AccountApi.md#api_v1_account_get) | **GET** /api/v1/account | Identity check — returns the authenticated user + scopes of the calling key.
*AccountApi* | [**api_v1_account_memberships_get**](docs/AccountApi.md#api_v1_account_memberships_get) | **GET** /api/v1/account/memberships | Accounts this login can act on.
*AccountApi* | [**api_v1_account_notices_get**](docs/AccountApi.md#api_v1_account_notices_get) | **GET** /api/v1/account/notices | Account notices.
*AccountApi* | [**api_v1_account_pending_changes_get**](docs/AccountApi.md#api_v1_account_pending_changes_get) | **GET** /api/v1/account/pending-changes | Profile changes awaiting verification.
*AccountApi* | [**api_v1_account_preferences_get**](docs/AccountApi.md#api_v1_account_preferences_get) | **GET** /api/v1/account/preferences | Per-member preferences.
*AccountApi* | [**api_v1_account_preferences_key_put**](docs/AccountApi.md#api_v1_account_preferences_key_put) | **PUT** /api/v1/account/preferences/{key} | Set one preference.
*AccountApi* | [**api_v1_account_profile_get**](docs/AccountApi.md#api_v1_account_profile_get) | **GET** /api/v1/account/profile | The account&#39;s contact and company details.
*AccountApi* | [**api_v1_account_sales_referrals_get**](docs/AccountApi.md#api_v1_account_sales_referrals_get) | **GET** /api/v1/account/sales-referrals | Your sales referrals — clients assigned to you, their deposits and your commission.
*AccountApi* | [**api_v1_account_settings_get**](docs/AccountApi.md#api_v1_account_settings_get) | **GET** /api/v1/account/settings | Account settings.
*AccountApi* | [**api_v1_account_ui_layouts_get**](docs/AccountApi.md#api_v1_account_ui_layouts_get) | **GET** /api/v1/account/ui-layouts | Saved menu layouts.
*AccountApi* | [**api_v1_account_ui_layouts_scope_delete**](docs/AccountApi.md#api_v1_account_ui_layouts_scope_delete) | **DELETE** /api/v1/account/ui-layouts/{scope} | Reset a menu layout.
*AccountApi* | [**api_v1_account_ui_layouts_scope_put**](docs/AccountApi.md#api_v1_account_ui_layouts_scope_put) | **PUT** /api/v1/account/ui-layouts/{scope} | Save a menu layout.
*AccountApi* | [**api_v1_account_usage_get**](docs/AccountApi.md#api_v1_account_usage_get) | **GET** /api/v1/account/usage | Metered usage for a period.
*AccountApi* | [**api_v1_account_usage_summary_get**](docs/AccountApi.md#api_v1_account_usage_summary_get) | **GET** /api/v1/account/usage-summary | Inventory counts at a glance.
*AccountBillingApi* | [**api_v1_account_billing_affiliated_payments_get**](docs/AccountBillingApi.md#api_v1_account_billing_affiliated_payments_get) | **GET** /api/v1/account/billing/affiliated-payments | Payments made to affiliated accounts.
*AccountBillingApi* | [**api_v1_account_billing_averages_get**](docs/AccountBillingApi.md#api_v1_account_billing_averages_get) | **GET** /api/v1/account/billing/averages | Average costs and overcharges.
*AccountBillingApi* | [**api_v1_account_billing_invoices_get**](docs/AccountBillingApi.md#api_v1_account_billing_invoices_get) | **GET** /api/v1/account/billing/invoices | List invoices.
*AccountBillingApi* | [**api_v1_account_billing_invoices_id_pdf_get**](docs/AccountBillingApi.md#api_v1_account_billing_invoices_id_pdf_get) | **GET** /api/v1/account/billing/invoices/{id}/pdf | Download an invoice PDF.
*AccountBillingApi* | [**api_v1_account_billing_settings_get**](docs/AccountBillingApi.md#api_v1_account_billing_settings_get) | **GET** /api/v1/account/billing/settings | The account&#39;s billing plan.
*AccountNotificationsApi* | [**api_v1_account_notification_destinations_get**](docs/AccountNotificationsApi.md#api_v1_account_notification_destinations_get) | **GET** /api/v1/account/notification-destinations | The account&#39;s notification destinations.
*AccountNotificationsApi* | [**api_v1_account_notification_destinations_id_delete**](docs/AccountNotificationsApi.md#api_v1_account_notification_destinations_id_delete) | **DELETE** /api/v1/account/notification-destinations/{id} | Delete a notification destination.
*AccountNotificationsApi* | [**api_v1_account_notification_destinations_id_status_get**](docs/AccountNotificationsApi.md#api_v1_account_notification_destinations_id_status_get) | **GET** /api/v1/account/notification-destinations/{id}/status | Whether a destination is linked.
*AccountNotificationsApi* | [**api_v1_account_notification_destinations_id_test_post**](docs/AccountNotificationsApi.md#api_v1_account_notification_destinations_id_test_post) | **POST** /api/v1/account/notification-destinations/{id}/test | Send a test message to a destination.
*AccountNotificationsApi* | [**api_v1_account_notification_destinations_post**](docs/AccountNotificationsApi.md#api_v1_account_notification_destinations_post) | **POST** /api/v1/account/notification-destinations | Add a notification destination.
*AccountNotificationsApi* | [**api_v1_account_notification_preferences_get**](docs/AccountNotificationsApi.md#api_v1_account_notification_preferences_get) | **GET** /api/v1/account/notification-preferences | Per-event channel preferences.
*AccountNotificationsApi* | [**api_v1_account_notification_preferences_put**](docs/AccountNotificationsApi.md#api_v1_account_notification_preferences_put) | **PUT** /api/v1/account/notification-preferences | Save channel preferences.
*AccountNotificationsApi* | [**api_v1_account_notifications_get**](docs/AccountNotificationsApi.md#api_v1_account_notifications_get) | **GET** /api/v1/account/notifications | The in-app notification feed.
*AccountNotificationsApi* | [**api_v1_account_notifications_read_post**](docs/AccountNotificationsApi.md#api_v1_account_notifications_read_post) | **POST** /api/v1/account/notifications/read | Mark notifications read.
*AccountNotificationsApi* | [**api_v1_account_notifications_unread_count_get**](docs/AccountNotificationsApi.md#api_v1_account_notifications_unread_count_get) | **GET** /api/v1/account/notifications/unread-count | Unread notification count.
*AdScannerApi* | [**api_v1_ad_scanner_get**](docs/AdScannerApi.md#api_v1_ad_scanner_get) | **GET** /api/v1/ad-scanner | List scan tasks.
*AdScannerApi* | [**api_v1_ad_scanner_id_delete**](docs/AdScannerApi.md#api_v1_ad_scanner_id_delete) | **DELETE** /api/v1/ad-scanner/{id} | Delete a scan task.
*AdScannerApi* | [**api_v1_ad_scanner_id_ignore_domain_put**](docs/AdScannerApi.md#api_v1_ad_scanner_id_ignore_domain_put) | **PUT** /api/v1/ad-scanner/{id}/ignore-domain | Ignore (or un-ignore) a flagged domain on a task.
*AdScannerApi* | [**api_v1_ad_scanner_id_manual_items_get**](docs/AdScannerApi.md#api_v1_ad_scanner_id_manual_items_get) | **GET** /api/v1/ad-scanner/{id}/manual-items | List a manual task&#39;s items.
*AdScannerApi* | [**api_v1_ad_scanner_id_manual_items_item_id_state_put**](docs/AdScannerApi.md#api_v1_ad_scanner_id_manual_items_item_id_state_put) | **PUT** /api/v1/ad-scanner/{id}/manual-items/{itemId}/state | Pause, resume or delete a manual item.
*AdScannerApi* | [**api_v1_ad_scanner_id_manual_items_post**](docs/AdScannerApi.md#api_v1_ad_scanner_id_manual_items_post) | **POST** /api/v1/ad-scanner/{id}/manual-items | Add or edit a manual item.
*AdScannerApi* | [**api_v1_ad_scanner_id_put**](docs/AdScannerApi.md#api_v1_ad_scanner_id_put) | **PUT** /api/v1/ad-scanner/{id} | Replace a task&#39;s name, tags and config.
*AdScannerApi* | [**api_v1_ad_scanner_id_toggle_active_put**](docs/AdScannerApi.md#api_v1_ad_scanner_id_toggle_active_put) | **PUT** /api/v1/ad-scanner/{id}/toggle-active | Start or stop a scan task.
*AdScannerApi* | [**api_v1_ad_scanner_post**](docs/AdScannerApi.md#api_v1_ad_scanner_post) | **POST** /api/v1/ad-scanner | Create a scan task.
*AdScannerApi* | [**api_v1_ad_scanner_report_hash_get**](docs/AdScannerApi.md#api_v1_ad_scanner_report_hash_get) | **GET** /api/v1/ad-scanner/report/{hash} | One scan&#39;s full report.
*AdScannerApi* | [**api_v1_ad_scanner_reports_get**](docs/AdScannerApi.md#api_v1_ad_scanner_reports_get) | **GET** /api/v1/ad-scanner/reports | List scan results.
*AdScannerApi* | [**api_v1_ad_scanner_stats_get**](docs/AdScannerApi.md#api_v1_ad_scanner_stats_get) | **GET** /api/v1/ad-scanner/stats | Scan volume and proxy bandwidth.
*AdScannerApi* | [**api_v1_ad_scanner_tags_get**](docs/AdScannerApi.md#api_v1_ad_scanner_tags_get) | **GET** /api/v1/ad-scanner/tags | Tags used on the account&#39;s scan tasks.
*AdShopApi* | [**api_v1_ad_shop_cart_get**](docs/AdShopApi.md#api_v1_ad_shop_cart_get) | **GET** /api/v1/ad-shop/cart | Read the draft cart.
*AdShopApi* | [**api_v1_ad_shop_cart_post**](docs/AdShopApi.md#api_v1_ad_shop_cart_post) | **POST** /api/v1/ad-shop/cart | Replace the draft cart.
*AdShopApi* | [**api_v1_ad_shop_confirm_post**](docs/AdShopApi.md#api_v1_ad_shop_confirm_post) | **POST** /api/v1/ad-shop/confirm | Check out the cart — creates the campaigns.
*AdShopApi* | [**api_v1_ad_shop_filter_options_get**](docs/AdShopApi.md#api_v1_ad_shop_filter_options_get) | **GET** /api/v1/ad-shop/filter-options | Filter values present in the current snapshot.
*AdShopApi* | [**api_v1_ad_shop_group_summary_post**](docs/AdShopApi.md#api_v1_ad_shop_group_summary_post) | **POST** /api/v1/ad-shop/group-summary | Group the catalog by targeting dimensions.
*AdShopApi* | [**api_v1_ad_shop_opportunities_get**](docs/AdShopApi.md#api_v1_ad_shop_opportunities_get) | **GET** /api/v1/ad-shop/opportunities | Browse Ad Shop opportunities.
*AdShopApi* | [**api_v1_ad_shop_plan_get**](docs/AdShopApi.md#api_v1_ad_shop_plan_get) | **GET** /api/v1/ad-shop/plan | Preview how the cart becomes campaigns.
*AdsApi* | [**api_v1_campaigns_type_campaign_id_ads_mass_undelete_post**](docs/AdsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_undelete_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-undelete | Restore archived ads of a campaign.
*AdspacesApi* | [**api_v1_adspaces_add_multiple_post**](docs/AdspacesApi.md#api_v1_adspaces_add_multiple_post) | **POST** /api/v1/adspaces/add-multiple | Create several ad zones of one type on one site.
*AdspacesApi* | [**api_v1_adspaces_export_codes_get**](docs/AdspacesApi.md#api_v1_adspaces_export_codes_get) | **GET** /api/v1/adspaces/export-codes | Embed codes for many ad zones at once, grouped by site.
*AdspacesApi* | [**api_v1_adspaces_get**](docs/AdspacesApi.md#api_v1_adspaces_get) | **GET** /api/v1/adspaces | List ad zones owned by the caller.
*AdspacesApi* | [**api_v1_adspaces_id_blocked_advertisers_get**](docs/AdspacesApi.md#api_v1_adspaces_id_blocked_advertisers_get) | **GET** /api/v1/adspaces/{id}/blocked-advertisers | Advertiser block filters that exclude this ad zone.
*AdspacesApi* | [**api_v1_adspaces_id_children_get**](docs/AdspacesApi.md#api_v1_adspaces_id_children_get) | **GET** /api/v1/adspaces/{id}/children | List an ad zone&#39;s child zones.
*AdspacesApi* | [**api_v1_adspaces_id_clone_post**](docs/AdspacesApi.md#api_v1_adspaces_id_clone_post) | **POST** /api/v1/adspaces/{id}/clone | Duplicate an ad zone.
*AdspacesApi* | [**api_v1_adspaces_id_code_get**](docs/AdspacesApi.md#api_v1_adspaces_id_code_get) | **GET** /api/v1/adspaces/{id}/code | Embed-code snippets for an adspace.
*AdspacesApi* | [**api_v1_adspaces_id_delete**](docs/AdspacesApi.md#api_v1_adspaces_id_delete) | **DELETE** /api/v1/adspaces/{id} | Soft-delete an adspace.
*AdspacesApi* | [**api_v1_adspaces_id_get**](docs/AdspacesApi.md#api_v1_adspaces_id_get) | **GET** /api/v1/adspaces/{id} | Get a single adspace.
*AdspacesApi* | [**api_v1_adspaces_id_network_binding_delete**](docs/AdspacesApi.md#api_v1_adspaces_id_network_binding_delete) | **DELETE** /api/v1/adspaces/{id}/network-binding | Remove the zone&#39;s network binding.
*AdspacesApi* | [**api_v1_adspaces_id_network_binding_put**](docs/AdspacesApi.md#api_v1_adspaces_id_network_binding_put) | **PUT** /api/v1/adspaces/{id}/network-binding | Bind the zone to a campaign on an external ad network (the Source tab).
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_ad_id_delete**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_delete) | **DELETE** /api/v1/adspaces/{id}/own-ads/{adId} | Delete an own ad.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_ad_id_get**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_get) | **GET** /api/v1/adspaces/{id}/own-ads/{adId} | Get one own ad.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_ad_id_put**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_put) | **PUT** /api/v1/adspaces/{id}/own-ads/{adId} | Update an own ad.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_ad_id_toggle_put**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_toggle_put) | **PUT** /api/v1/adspaces/{id}/own-ads/{adId}/toggle | Switch an own ad on/off.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_get**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_get) | **GET** /api/v1/adspaces/{id}/own-ads | List the zone&#39;s own (house / fallback) ads.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_mass_action_post**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_mass_action_post) | **POST** /api/v1/adspaces/{id}/own-ads/mass-action | Activate, deactivate or delete several own ads.
*AdspacesApi* | [**api_v1_adspaces_id_own_ads_post**](docs/AdspacesApi.md#api_v1_adspaces_id_own_ads_post) | **POST** /api/v1/adspaces/{id}/own-ads | Add an own ad.
*AdspacesApi* | [**api_v1_adspaces_id_patch**](docs/AdspacesApi.md#api_v1_adspaces_id_patch) | **PATCH** /api/v1/adspaces/{id} | Update an existing adspace.
*AdspacesApi* | [**api_v1_adspaces_id_prices_type_get**](docs/AdspacesApi.md#api_v1_adspaces_id_prices_type_get) | **GET** /api/v1/adspaces/{id}/prices/{type} | Minimum (floor) prices per country for one device type.
*AdspacesApi* | [**api_v1_adspaces_id_prices_type_post**](docs/AdspacesApi.md#api_v1_adspaces_id_prices_type_post) | **POST** /api/v1/adspaces/{id}/prices/{type} | Replace the floor prices for one device type.
*AdspacesApi* | [**api_v1_adspaces_id_recover_post**](docs/AdspacesApi.md#api_v1_adspaces_id_recover_post) | **POST** /api/v1/adspaces/{id}/recover | Reverse a soft-delete on an adspace.
*AdspacesApi* | [**api_v1_adspaces_id_wl_campaigns_get**](docs/AdspacesApi.md#api_v1_adspaces_id_wl_campaigns_get) | **GET** /api/v1/adspaces/{id}/wl-campaigns | Campaigns that can be whitelisted on this zone, and the current whitelist.
*AdspacesApi* | [**api_v1_adspaces_id_wl_campaigns_put**](docs/AdspacesApi.md#api_v1_adspaces_id_wl_campaigns_put) | **PUT** /api/v1/adspaces/{id}/wl-campaigns | Replace the zone&#39;s whitelisted campaigns.
*AdspacesApi* | [**api_v1_adspaces_mass_delete_post**](docs/AdspacesApi.md#api_v1_adspaces_mass_delete_post) | **POST** /api/v1/adspaces/mass-delete | Soft-delete several ad zones.
*AdspacesApi* | [**api_v1_adspaces_mass_recover_post**](docs/AdspacesApi.md#api_v1_adspaces_mass_recover_post) | **POST** /api/v1/adspaces/mass-recover | Recover several soft-deleted ad zones.
*AdspacesApi* | [**api_v1_adspaces_templates_get**](docs/AdspacesApi.md#api_v1_adspaces_templates_get) | **GET** /api/v1/adspaces/templates | List your saved ad zone templates.
*AdspacesApi* | [**api_v1_adspaces_templates_id_delete**](docs/AdspacesApi.md#api_v1_adspaces_templates_id_delete) | **DELETE** /api/v1/adspaces/templates/{id} | Delete a template.
*AdspacesApi* | [**api_v1_adspaces_templates_id_put**](docs/AdspacesApi.md#api_v1_adspaces_templates_id_put) | **PUT** /api/v1/adspaces/templates/{id} | Replace a template&#39;s data.
*AdspacesApi* | [**api_v1_adspaces_templates_post**](docs/AdspacesApi.md#api_v1_adspaces_templates_post) | **POST** /api/v1/adspaces/templates | Save an ad zone template.
*AdspacesApi* | [**api_v1_adspaces_type_post**](docs/AdspacesApi.md#api_v1_adspaces_type_post) | **POST** /api/v1/adspaces/{type} | Create a new adspace.
*AdspacesApi* | [**api_v1_adspaces_type_schema_get**](docs/AdspacesApi.md#api_v1_adspaces_type_schema_get) | **GET** /api/v1/adspaces/{type}/_schema | Field metadata for create/update of one adspace type.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_actions_action_id_decide_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_actions_action_id_decide_post) | **POST** /api/v1/adspaces/{id}/media-buying/actions/{actionId}/decide | Approve or reject a proposal.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_actions_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_actions_get) | **GET** /api/v1/adspaces/{id}/media-buying/actions | Activity log: every block, bid, budget and other change, and open proposals.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_agent_run_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_agent_run_post) | **POST** /api/v1/adspaces/{id}/media-buying/agent/run | Run the buying agent now.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_agent_runs_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_agent_runs_get) | **GET** /api/v1/adspaces/{id}/media-buying/agent/runs | The buying agent&#39;s recent runs with their summaries and proposals.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_block_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_block_post) | **POST** /api/v1/adspaces/{id}/media-buying/block | Block or unblock one source zone at the network.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_compare_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_compare_get) | **GET** /api/v1/adspaces/{id}/media-buying/compare | Compare with another buy (A/B, e.g. against a control left to the network&#39;s own optimiser).
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_get) | **GET** /api/v1/adspaces/{id}/media-buying | Overview: the connected network, what it supports, the policy and open proposals.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_ips_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_ips_get) | **GET** /api/v1/adspaces/{id}/media-buying/ips | The IP preblock list: ranges on the network&#39;s exclusion list and proposals.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_ips_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_ips_post) | **POST** /api/v1/adspaces/{id}/media-buying/ips | Change the IP preblock list.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_launch_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_get) | **GET** /api/v1/adspaces/{id}/media-buying/launch | What a new campaign can be launched with (unconnected ad zones).
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_launch_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_post) | **POST** /api/v1/adspaces/{id}/media-buying/launch | Launch a new campaign at the network for this ad zone.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_launch_templates_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_templates_get) | **GET** /api/v1/adspaces/{id}/media-buying/launch/templates | Existing campaigns that can be cloned for a launch.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_network_budget_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_network_budget_get) | **GET** /api/v1/adspaces/{id}/media-buying/network-budget | The campaign&#39;s daily budget at the network.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_policy_put**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_policy_put) | **PUT** /api/v1/adspaces/{id}/media-buying/policy | Save the buying policy (any subset of its fields).
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_policy_suggest_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_policy_suggest_get) | **GET** /api/v1/adspaces/{id}/media-buying/policy/suggest | Suggested policy from the zone&#39;s own traffic, with a reason per field.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_report_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_report_post) | **POST** /api/v1/adspaces/{id}/media-buying/report | Send the media buying report now.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_segments_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_segments_get) | **GET** /api/v1/adspaces/{id}/media-buying/segments | Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_source_bid_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_bid_get) | **GET** /api/v1/adspaces/{id}/media-buying/source/bid | The campaign&#39;s current bid at the network.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_source_bid_put**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_bid_put) | **PUT** /api/v1/adspaces/{id}/media-buying/source/bid | Set the campaign&#39;s bid at the network.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_source_retry_post**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_retry_post) | **POST** /api/v1/adspaces/{id}/media-buying/source/retry | Retry the connection to the source campaign.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_targeting_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_get) | **GET** /api/v1/adspaces/{id}/media-buying/targeting | The campaign&#39;s placement targeting (all, or an allow-list).
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_targeting_put**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_put) | **PUT** /api/v1/adspaces/{id}/media-buying/targeting | Switch to / edit the allow-list, or back to all placements.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_targeting_suggest_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_suggest_get) | **GET** /api/v1/adspaces/{id}/media-buying/targeting/suggest | Suggested allow-list: the profitable placements of the policy window.
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_track_record_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_track_record_get) | **GET** /api/v1/adspaces/{id}/media-buying/track-record | Track record: did each change do what it was meant to?
*AgenticMediaBuyingApi* | [**api_v1_adspaces_id_media_buying_zones_get**](docs/AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_zones_get) | **GET** /api/v1/adspaces/{id}/media-buying/zones | Source-zone report: revenue against cost per placement.
*AgenticMediaBuyingApi* | [**api_v1_media_buying_portfolio_get**](docs/AgenticMediaBuyingApi.md#api_v1_media_buying_portfolio_get) | **GET** /api/v1/media-buying/portfolio | Every buy side by side: margin against target, spend, proposals, the agent&#39;s latest summary.
*AgenticMediaBuyingApi* | [**api_v1_tracker_media_buying_portfolio_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_media_buying_portfolio_get) | **GET** /api/v1/tracker/media-buying/portfolio | Every buy side by side (tracker accounts — the same overview): margin against target, spend, proposals, the agent&#39;s latest summary.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/actions/{actionId}/decide | Approve or reject a proposal.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_actions_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_actions_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/actions | Activity log: every block, bid, budget and other change, and open proposals.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_agent_run_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_agent_run_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/agent/run | Run the buying agent now.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_agent_runs_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_agent_runs_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/agent/runs | The buying agent&#39;s recent runs with their summaries and proposals.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_block_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_block_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/block | Block or unblock one source zone at the network.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_compare_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_compare_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/compare | Compare with another buy (A/B, e.g. against a control left to the network&#39;s own optimiser).
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying | Overview: the connected network, what it supports, the policy and open proposals.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_ips_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_ips_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/ips | The IP preblock list: ranges on the network&#39;s exclusion list and proposals.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_ips_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_ips_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/ips | Change the IP preblock list.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_network_budget_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_network_budget_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/network-budget | The campaign&#39;s daily budget at the network.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_policy_put**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_policy_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/policy | Save the buying policy (any subset of its fields).
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/policy/suggest | Suggested policy from the zone&#39;s own traffic, with a reason per field.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_report_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_report_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/report | Send the media buying report now.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_segments_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_segments_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/segments | Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_source_bid_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_bid_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/source/bid | The campaign&#39;s current bid at the network.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_source_bid_put**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_bid_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/source/bid | Set the campaign&#39;s bid at the network.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_source_retry_post**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_retry_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/source/retry | Retry the connection to the source campaign.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_targeting_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/targeting | The campaign&#39;s placement targeting (all, or an allow-list).
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_targeting_put**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/targeting | Switch to / edit the allow-list, or back to all placements.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/targeting/suggest | Suggested allow-list: the profitable placements of the policy window.
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_track_record_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_track_record_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/track-record | Track record: did each change do what it was meant to?
*AgenticMediaBuyingApi* | [**api_v1_tracker_tracking_links_id_media_buying_zones_get**](docs/AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_zones_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/zones | Source-zone report: revenue against cost per placement.
*BidRulesetsApi* | [**api_v1_bid_rulesets_get**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_get) | **GET** /api/v1/bid-rulesets | List the caller&#39;s bid rulesets (lightweight rows).
*BidRulesetsApi* | [**api_v1_bid_rulesets_id_clone_post**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_id_clone_post) | **POST** /api/v1/bid-rulesets/{id}/clone | Clone a ruleset with all its rules.
*BidRulesetsApi* | [**api_v1_bid_rulesets_id_delete**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_id_delete) | **DELETE** /api/v1/bid-rulesets/{id} | Soft-delete a ruleset.
*BidRulesetsApi* | [**api_v1_bid_rulesets_id_get**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_id_get) | **GET** /api/v1/bid-rulesets/{id} | Show one ruleset, including all rules.
*BidRulesetsApi* | [**api_v1_bid_rulesets_id_patch**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_id_patch) | **PATCH** /api/v1/bid-rulesets/{id} | Update a ruleset&#39;s metadata and/or replace its rules.
*BidRulesetsApi* | [**api_v1_bid_rulesets_post**](docs/BidRulesetsApi.md#api_v1_bid_rulesets_post) | **POST** /api/v1/bid-rulesets | Create a new bid ruleset (with rules in one shot).
*CampaignsApi* | [**api_v1_campaigns_cpm_campaign_id_spots_space_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_delete) | **DELETE** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Remove an ad zone from a CPM campaign.
*CampaignsApi* | [**api_v1_campaigns_cpm_campaign_id_spots_space_id_post**](docs/CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_post) | **POST** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Add an ad zone to a CPM campaign (or re-price it).
*CampaignsApi* | [**api_v1_campaigns_cpm_campaign_id_spots_space_id_put**](docs/CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_put) | **PUT** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Switch a CPM campaign&#39;s zone spot on or off.
*CampaignsApi* | [**api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put**](docs/CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put) | **PUT** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}/{type} | Set a CPM zone spot&#39;s bid or state.
*CampaignsApi* | [**api_v1_campaigns_get**](docs/CampaignsApi.md#api_v1_campaigns_get) | **GET** /api/v1/campaigns | List the caller&#39;s campaigns across all types (or one type).
*CampaignsApi* | [**api_v1_campaigns_mass_delete_post**](docs/CampaignsApi.md#api_v1_campaigns_mass_delete_post) | **POST** /api/v1/campaigns/mass-delete | Soft-delete many campaigns.
*CampaignsApi* | [**api_v1_campaigns_mass_toggle_put**](docs/CampaignsApi.md#api_v1_campaigns_mass_toggle_put) | **PUT** /api/v1/campaigns/mass-toggle | Pause or resume many campaigns at once.
*CampaignsApi* | [**api_v1_campaigns_mass_undelete_post**](docs/CampaignsApi.md#api_v1_campaigns_mass_undelete_post) | **POST** /api/v1/campaigns/mass-undelete | Restore soft-deleted campaigns.
*CampaignsApi* | [**api_v1_campaigns_purge_post**](docs/CampaignsApi.md#api_v1_campaigns_purge_post) | **POST** /api/v1/campaigns/purge | Permanently delete soft-deleted campaigns and their ads.
*CampaignsApi* | [**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get**](docs/CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get) | **GET** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | List per-zone bid overrides for a RON ad.
*CampaignsApi* | [**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put**](docs/CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put) | **PUT** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | Replace the per-zone bid overrides on a RON ad.
*CampaignsApi* | [**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete) | **DELETE** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/{zoneId} | Clear a single per-zone bid override.
*CampaignsApi* | [**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put**](docs/CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put) | **PUT** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/zones-only | Switch \&quot;only these zones\&quot; mode for a RON ad&#39;s per-zone bids.
*CampaignsApi* | [**api_v1_campaigns_ron_id_site_list_get**](docs/CampaignsApi.md#api_v1_campaigns_ron_id_site_list_get) | **GET** /api/v1/campaigns/ron/{id}/site-list | The Premium-sites box of a RON campaign.
*CampaignsApi* | [**api_v1_campaigns_ron_id_site_list_site_id_put**](docs/CampaignsApi.md#api_v1_campaigns_ron_id_site_list_site_id_put) | **PUT** /api/v1/campaigns/ron/{id}/site-list/{siteId} | Set one site of the Premium-sites box active or blocked.
*CampaignsApi* | [**api_v1_campaigns_ron_id_zones_get**](docs/CampaignsApi.md#api_v1_campaigns_ron_id_zones_get) | **GET** /api/v1/campaigns/ron/{id}/zones | List the zones a RON campaign is linked to.
*CampaignsApi* | [**api_v1_campaigns_rtb_id_test_rtb_get**](docs/CampaignsApi.md#api_v1_campaigns_rtb_id_test_rtb_get) | **GET** /api/v1/campaigns/rtb/{id}/test-rtb | Context for testing an RTB campaign&#39;s endpoint.
*CampaignsApi* | [**api_v1_campaigns_rtb_id_test_rtb_post**](docs/CampaignsApi.md#api_v1_campaigns_rtb_id_test_rtb_post) | **POST** /api/v1/campaigns/rtb/{id}/test-rtb | Fire a test bid request at an RTB campaign&#39;s endpoint.
*CampaignsApi* | [**api_v1_campaigns_save_categories_put**](docs/CampaignsApi.md#api_v1_campaigns_save_categories_put) | **PUT** /api/v1/campaigns/save-categories | Assign categories to many campaigns.
*CampaignsApi* | [**api_v1_campaigns_save_tags_put**](docs/CampaignsApi.md#api_v1_campaigns_save_tags_put) | **PUT** /api/v1/campaigns/save-tags | Assign tags (campaign groups) to many campaigns.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/active | Pause or unpause a single ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bid | Set a single ad&#39;s bid.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bids-per-geo | Set per-country bids for a RON ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/clone | Clone a single ad within a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/countries | Set per-ad country targeting for a RON ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_delete) | **DELETE** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Soft-delete an ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_get**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Show one ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/overlay-stats | Shoppable video — shown and clicks per overlay.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Update an ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/restore | Restore a deleted RON ad.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_copy_targets_get**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_copy_targets_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/copy-targets | Campaigns this campaign&#39;s ads can be copied into.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_csv_import_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_csv_import_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/csv-import | Import native ads from a CSV — one ad per row, or one ad per group.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_from_pool_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_from_pool_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/from-pool | Create ads from a creative pool.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_get**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads | List ads on a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_mass_clone_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_clone_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-clone | Copy many ads of a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_mass_delete_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_delete_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-delete | Soft-delete many ads of a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_mass_toggle_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_toggle_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/mass-toggle | Activate or pause many ads of a campaign at once.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_multi_upload_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_multi_upload_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/multi-upload | Bulk-upload ads — one ad per creative file.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_post**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads | Create an ad on a campaign (smart-default).
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_update_pool_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_pool_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-pool | Point many ads at a different creative pool.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_update_url_pool_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_url_pool_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-url-pool | Point many ads at a URL pool, or detach it.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_update_url_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_url_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-url | Rewrite the destination URL of many ads at once.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_ads_update_weight_put**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_weight_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-weight | Set the rotation weight of one or more RON ads.
*CampaignsApi* | [**api_v1_campaigns_type_campaign_id_schema_ads_get**](docs/CampaignsApi.md#api_v1_campaigns_type_campaign_id_schema_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/_schema/ads | Field metadata for ad creation, scoped to a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_active_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/active | Pause or unpause a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_available_zones_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_available_zones_get) | **GET** /api/v1/campaigns/{type}/{id}/available-zones | List your ad zones that can be attached to a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_bids_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_id_bids_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/bids | Mass update bids on every ad in a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_budget_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_id_budget_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/budget | Update a campaign&#39;s total and/or daily budget.
*CampaignsApi* | [**api_v1_campaigns_type_id_clone_post**](docs/CampaignsApi.md#api_v1_campaigns_type_id_clone_post) | **POST** /api/v1/campaigns/{type}/{id}/clone | Clone a campaign — everything, or the parts you pick.
*CampaignsApi* | [**api_v1_campaigns_type_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_type_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id} | Soft-delete a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_filters_filter_type_filter_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_type_id_filters_filter_type_filter_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id}/filters/{filter_type}/{filter_id} | Detach a filter from this campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_filters_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_filters_get) | **GET** /api/v1/campaigns/{type}/{id}/filters | List filters attached to this campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_filters_post**](docs/CampaignsApi.md#api_v1_campaigns_type_id_filters_post) | **POST** /api/v1/campaigns/{type}/{id}/filters | Attach a filter to this campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_get) | **GET** /api/v1/campaigns/{type}/{id} | Get a single campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_min_bid_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_min_bid_get) | **GET** /api/v1/campaigns/{type}/{id}/min-bid | Get the campaign&#39;s minimum acceptable CPC bid.
*CampaignsApi* | [**api_v1_campaigns_type_id_patch**](docs/CampaignsApi.md#api_v1_campaigns_type_id_patch) | **PATCH** /api/v1/campaigns/{type}/{id} | Partially update a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_reset_max_budget_put**](docs/CampaignsApi.md#api_v1_campaigns_type_id_reset_max_budget_put) | **PUT** /api/v1/campaigns/{type}/{id}/reset-max-budget | Reset a campaign&#39;s lifetime-budget spend.
*CampaignsApi* | [**api_v1_campaigns_type_id_sites_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_sites_get) | **GET** /api/v1/campaigns/{type}/{id}/sites | Your sites that have zones attachable to a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_whitelist_zones_get**](docs/CampaignsApi.md#api_v1_campaigns_type_id_whitelist_zones_get) | **GET** /api/v1/campaigns/{type}/{id}/whitelist-zones | List the ad zones attached to a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_zones_post**](docs/CampaignsApi.md#api_v1_campaigns_type_id_zones_post) | **POST** /api/v1/campaigns/{type}/{id}/zones | Attach ad zones to a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_zones_zone_id_delete**](docs/CampaignsApi.md#api_v1_campaigns_type_id_zones_zone_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id}/zones/{zoneId} | Detach an ad zone from a campaign.
*CampaignsApi* | [**api_v1_campaigns_type_id_zones_zone_id_weight_put**](docs/CampaignsApi.md#api_v1_campaigns_type_id_zones_zone_id_weight_put) | **PUT** /api/v1/campaigns/{type}/{id}/zones/{zoneId}/weight | Set an attached zone&#39;s weight for this campaign.
*CampaignsApi* | [**api_v1_campaigns_type_post**](docs/CampaignsApi.md#api_v1_campaigns_type_post) | **POST** /api/v1/campaigns/{type} | Create a new campaign (smart-default).
*CampaignsApi* | [**api_v1_campaigns_type_schema_ads_get**](docs/CampaignsApi.md#api_v1_campaigns_type_schema_ads_get) | **GET** /api/v1/campaigns/{type}/_schema/ads | Field metadata for ad creation.
*CampaignsApi* | [**api_v1_campaigns_type_schema_get**](docs/CampaignsApi.md#api_v1_campaigns_type_schema_get) | **GET** /api/v1/campaigns/{type}/_schema | Field metadata for create/update.
*CampaignsApi* | [**api_v1_rtb_test_rtb_context_get**](docs/CampaignsApi.md#api_v1_rtb_test_rtb_context_get) | **GET** /api/v1/rtb/test-rtb/context | Context for testing an endpoint before the campaign exists.
*CampaignsApi* | [**api_v1_rtb_test_rtb_post**](docs/CampaignsApi.md#api_v1_rtb_test_rtb_post) | **POST** /api/v1/rtb/test-rtb | Fire a test bid request at any endpoint URL.
*CampaignsApi* | [**api_v1_tools_replace_domain_put**](docs/CampaignsApi.md#api_v1_tools_replace_domain_put) | **PUT** /api/v1/tools/replace-domain | Replace the landing domain across your RON ads.
*CleanupApi* | [**api_v1_cleanup_advertiser_archived_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_archived_get) | **GET** /api/v1/cleanup/advertiser/archived | Archived advertiser items that can be purged.
*CleanupApi* | [**api_v1_cleanup_advertiser_export_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_export_get) | **GET** /api/v1/cleanup/advertiser/export | Download the advertiser cleanup candidates.
*CleanupApi* | [**api_v1_cleanup_advertiser_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_get) | **GET** /api/v1/cleanup/advertiser | List advertiser items that no longer serve.
*CleanupApi* | [**api_v1_cleanup_advertiser_linked_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_linked_get) | **GET** /api/v1/cleanup/advertiser/linked | What still uses advertiser cleanup rows.
*CleanupApi* | [**api_v1_cleanup_advertiser_purge_post**](docs/CleanupApi.md#api_v1_cleanup_advertiser_purge_post) | **POST** /api/v1/cleanup/advertiser/purge | Purge archived advertiser items for good.
*CleanupApi* | [**api_v1_cleanup_advertiser_runs_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_runs_get) | **GET** /api/v1/cleanup/advertiser/runs | Recent advertiser cleanup runs.
*CleanupApi* | [**api_v1_cleanup_advertiser_runs_id_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_runs_id_get) | **GET** /api/v1/cleanup/advertiser/runs/{id} | One advertiser cleanup run with its items.
*CleanupApi* | [**api_v1_cleanup_advertiser_runs_id_undone_post**](docs/CleanupApi.md#api_v1_cleanup_advertiser_runs_id_undone_post) | **POST** /api/v1/cleanup/advertiser/runs/{id}/undone | Mark a advertiser cleanup run as undone.
*CleanupApi* | [**api_v1_cleanup_advertiser_runs_post**](docs/CleanupApi.md#api_v1_cleanup_advertiser_runs_post) | **POST** /api/v1/cleanup/advertiser/runs | Record a advertiser cleanup run.
*CleanupApi* | [**api_v1_cleanup_advertiser_summary_get**](docs/CleanupApi.md#api_v1_cleanup_advertiser_summary_get) | **GET** /api/v1/cleanup/advertiser/summary | Count the advertiser cleanup candidates per kind.
*CleanupApi* | [**api_v1_cleanup_publisher_archived_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_archived_get) | **GET** /api/v1/cleanup/publisher/archived | Archived publisher items that can be purged.
*CleanupApi* | [**api_v1_cleanup_publisher_export_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_export_get) | **GET** /api/v1/cleanup/publisher/export | Download the publisher cleanup candidates.
*CleanupApi* | [**api_v1_cleanup_publisher_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_get) | **GET** /api/v1/cleanup/publisher | List publisher items that no longer serve.
*CleanupApi* | [**api_v1_cleanup_publisher_linked_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_linked_get) | **GET** /api/v1/cleanup/publisher/linked | What still uses publisher cleanup rows.
*CleanupApi* | [**api_v1_cleanup_publisher_purge_post**](docs/CleanupApi.md#api_v1_cleanup_publisher_purge_post) | **POST** /api/v1/cleanup/publisher/purge | Purge archived publisher items for good.
*CleanupApi* | [**api_v1_cleanup_publisher_runs_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_runs_get) | **GET** /api/v1/cleanup/publisher/runs | Recent publisher cleanup runs.
*CleanupApi* | [**api_v1_cleanup_publisher_runs_id_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_runs_id_get) | **GET** /api/v1/cleanup/publisher/runs/{id} | One publisher cleanup run with its items.
*CleanupApi* | [**api_v1_cleanup_publisher_runs_id_undone_post**](docs/CleanupApi.md#api_v1_cleanup_publisher_runs_id_undone_post) | **POST** /api/v1/cleanup/publisher/runs/{id}/undone | Mark a publisher cleanup run as undone.
*CleanupApi* | [**api_v1_cleanup_publisher_runs_post**](docs/CleanupApi.md#api_v1_cleanup_publisher_runs_post) | **POST** /api/v1/cleanup/publisher/runs | Record a publisher cleanup run.
*CleanupApi* | [**api_v1_cleanup_publisher_summary_get**](docs/CleanupApi.md#api_v1_cleanup_publisher_summary_get) | **GET** /api/v1/cleanup/publisher/summary | Count the publisher cleanup candidates per kind.
*CouponsApi* | [**api_v1_coupons_sets_get**](docs/CouponsApi.md#api_v1_coupons_sets_get) | **GET** /api/v1/coupons/sets | List coupon sets.
*CouponsApi* | [**api_v1_coupons_sets_id_delete**](docs/CouponsApi.md#api_v1_coupons_sets_id_delete) | **DELETE** /api/v1/coupons/sets/{id} | Delete a set and all its codes.
*CouponsApi* | [**api_v1_coupons_sets_id_export_get**](docs/CouponsApi.md#api_v1_coupons_sets_id_export_get) | **GET** /api/v1/coupons/sets/{id}/export | Export a set&#39;s codes as CSV.
*CouponsApi* | [**api_v1_coupons_sets_id_generate_post**](docs/CouponsApi.md#api_v1_coupons_sets_id_generate_post) | **POST** /api/v1/coupons/sets/{id}/generate | Generate codes in a set.
*CouponsApi* | [**api_v1_coupons_sets_id_put**](docs/CouponsApi.md#api_v1_coupons_sets_id_put) | **PUT** /api/v1/coupons/sets/{id} | Rename a set or move its end date.
*CouponsApi* | [**api_v1_coupons_sets_post**](docs/CouponsApi.md#api_v1_coupons_sets_post) | **POST** /api/v1/coupons/sets | Create a coupon set.
*CouponsApi* | [**api_v1_coupons_sets_set_id_coupons_get**](docs/CouponsApi.md#api_v1_coupons_sets_set_id_coupons_get) | **GET** /api/v1/coupons/sets/{setId}/coupons | List the codes in a set.
*CreativePoolsApi* | [**api_v1_creative_pools_get**](docs/CreativePoolsApi.md#api_v1_creative_pools_get) | **GET** /api/v1/creative-pools | List creative pools.
*CreativePoolsApi* | [**api_v1_creative_pools_id_add_creatives_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_add_creatives_post) | **POST** /api/v1/creative-pools/{id}/add-creatives | Add media-bank creatives to a pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_add_urls_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_add_urls_post) | **POST** /api/v1/creative-pools/{id}/add-urls | Add hotlinked image / video / HTML URLs to a pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_clone_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_clone_post) | **POST** /api/v1/creative-pools/{id}/clone | Clone a creative pool with all its items.
*CreativePoolsApi* | [**api_v1_creative_pools_id_delete**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_delete) | **DELETE** /api/v1/creative-pools/{id} | Soft-delete a creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_get**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_get) | **GET** /api/v1/creative-pools/{id} | Show a single creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_export_get**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_export_get) | **GET** /api/v1/creative-pools/{id}/items/export | Download pool items&#39; creative files as a ZIP.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_get**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_get) | **GET** /api/v1/creative-pools/{id}/items | List items in a creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_item_id_delete**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_delete) | **DELETE** /api/v1/creative-pools/{id}/items/{itemId} | Soft-delete a single pool item.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_item_id_put**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId} | Update a single pool item.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_item_id_toggle_put**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_toggle_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId}/toggle | Toggle a pool item on / off.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_mass_action_put**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_mass_action_put) | **PUT** /api/v1/creative-pools/{id}/items/mass-action | Bulk-change items of a creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_post) | **POST** /api/v1/creative-pools/{id}/items | Add an item to a creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_items_recover_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_items_recover_post) | **POST** /api/v1/creative-pools/{id}/items/recover | Put removed items back into a creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_put**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_put) | **PUT** /api/v1/creative-pools/{id} | Update creative pool meta.
*CreativePoolsApi* | [**api_v1_creative_pools_id_recover_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_recover_post) | **POST** /api/v1/creative-pools/{id}/recover | Restore an archived creative pool.
*CreativePoolsApi* | [**api_v1_creative_pools_id_used_in_get**](docs/CreativePoolsApi.md#api_v1_creative_pools_id_used_in_get) | **GET** /api/v1/creative-pools/{id}/used-in | List campaigns / ads that reference this pool.
*CreativePoolsApi* | [**api_v1_creative_pools_post**](docs/CreativePoolsApi.md#api_v1_creative_pools_post) | **POST** /api/v1/creative-pools | Create a creative pool.
*CreativePoolsApi* | [**api_v1_creatives_bulk_delete_post**](docs/CreativePoolsApi.md#api_v1_creatives_bulk_delete_post) | **POST** /api/v1/creatives/bulk-delete | Soft-delete many media-bank creatives.
*CreativePoolsApi* | [**api_v1_creatives_bulk_undelete_post**](docs/CreativePoolsApi.md#api_v1_creatives_bulk_undelete_post) | **POST** /api/v1/creatives/bulk-undelete | Restore many deleted creatives.
*CreativePoolsApi* | [**api_v1_creatives_id_undelete_put**](docs/CreativePoolsApi.md#api_v1_creatives_id_undelete_put) | **PUT** /api/v1/creatives/{id}/undelete | Restore one deleted creative.
*CreativesApi* | [**api_v1_creative_folders_get**](docs/CreativesApi.md#api_v1_creative_folders_get) | **GET** /api/v1/creative-folders | List media-bank folders.
*CreativesApi* | [**api_v1_creative_folders_id_delete**](docs/CreativesApi.md#api_v1_creative_folders_id_delete) | **DELETE** /api/v1/creative-folders/{id} | Delete a folder.
*CreativesApi* | [**api_v1_creative_folders_id_put**](docs/CreativesApi.md#api_v1_creative_folders_id_put) | **PUT** /api/v1/creative-folders/{id} | Rename or move a folder.
*CreativesApi* | [**api_v1_creative_folders_post**](docs/CreativesApi.md#api_v1_creative_folders_post) | **POST** /api/v1/creative-folders | Create a folder.
*CreativesApi* | [**api_v1_creatives_bulk_move_post**](docs/CreativesApi.md#api_v1_creatives_bulk_move_post) | **POST** /api/v1/creatives/bulk-move | File creatives into a folder.
*CreativesApi* | [**api_v1_creatives_get**](docs/CreativesApi.md#api_v1_creatives_get) | **GET** /api/v1/creatives | List the creative library.
*CreativesApi* | [**api_v1_creatives_id_delete**](docs/CreativesApi.md#api_v1_creatives_id_delete) | **DELETE** /api/v1/creatives/{id} | Delete a creative.
*CreativesApi* | [**api_v1_creatives_id_get**](docs/CreativesApi.md#api_v1_creatives_id_get) | **GET** /api/v1/creatives/{id} | Show one creative.
*CreativesApi* | [**api_v1_creatives_id_name_put**](docs/CreativesApi.md#api_v1_creatives_id_name_put) | **PUT** /api/v1/creatives/{id}/name | Rename a creative (panel inline edit).
*CreativesApi* | [**api_v1_creatives_id_put**](docs/CreativesApi.md#api_v1_creatives_id_put) | **PUT** /api/v1/creatives/{id} | Rename and/or re-tag a creative.
*CreativesApi* | [**api_v1_creatives_id_tags_put**](docs/CreativesApi.md#api_v1_creatives_id_tags_put) | **PUT** /api/v1/creatives/{id}/tags | Replace a creative&#39;s tags (panel inline edit).
*CreativesApi* | [**api_v1_creatives_id_used_in_get**](docs/CreativesApi.md#api_v1_creatives_id_used_in_get) | **GET** /api/v1/creatives/{id}/used-in | List ads / pools referencing this creative.
*CreativesApi* | [**api_v1_creatives_upload_post**](docs/CreativesApi.md#api_v1_creatives_upload_post) | **POST** /api/v1/creatives/upload | Upload creative files.
*DirectDealsApi* | [**api_v1_campaigns_directdeal_id_cancel_put**](docs/DirectDealsApi.md#api_v1_campaigns_directdeal_id_cancel_put) | **PUT** /api/v1/campaigns/directdeal/{id}/cancel | Cancel a direct deal.
*DirectDealsApi* | [**api_v1_direct_deals_adzones_get**](docs/DirectDealsApi.md#api_v1_direct_deals_adzones_get) | **GET** /api/v1/direct-deals/adzones | Ad zones a direct deal can be booked on.
*DirectDealsApi* | [**api_v1_direct_deals_get**](docs/DirectDealsApi.md#api_v1_direct_deals_get) | **GET** /api/v1/direct-deals | List direct deals with their derived status.
*EventLogApi* | [**api_v1_event_log_exports_get**](docs/EventLogApi.md#api_v1_event_log_exports_get) | **GET** /api/v1/event-log/exports | Your event log exports, newest first.
*EventLogApi* | [**api_v1_event_log_exports_id_download_get**](docs/EventLogApi.md#api_v1_event_log_exports_id_download_get) | **GET** /api/v1/event-log/exports/{id}/download | Download a finished export (.csv.gz).
*EventLogApi* | [**api_v1_event_log_exports_post**](docs/EventLogApi.md#api_v1_event_log_exports_post) | **POST** /api/v1/event-log/exports | Queue a CSV export of your events.
*EventLogApi* | [**api_v1_event_log_get**](docs/EventLogApi.md#api_v1_event_log_get) | **GET** /api/v1/event-log | Your raw events — impressions and clicks with IP and user agent (90 days).
*FiltersApi* | [**api_v1_filters_get**](docs/FiltersApi.md#api_v1_filters_get) | **GET** /api/v1/filters | List all filters across types.
*FiltersApi* | [**api_v1_filters_ip_id_ranges_range_id_delete**](docs/FiltersApi.md#api_v1_filters_ip_id_ranges_range_id_delete) | **DELETE** /api/v1/filters/ip/{id}/ranges/{rangeId} | Delete one range from an IP pool.
*FiltersApi* | [**api_v1_filters_ip_id_ranges_range_id_toggle_put**](docs/FiltersApi.md#api_v1_filters_ip_id_ranges_range_id_toggle_put) | **PUT** /api/v1/filters/ip/{id}/ranges/{rangeId}/toggle | Pause / resume one range of an IP pool.
*FiltersApi* | [**api_v1_filters_mass_action_post**](docs/FiltersApi.md#api_v1_filters_mass_action_post) | **POST** /api/v1/filters/mass-action | Activate, deactivate or delete many filters.
*FiltersApi* | [**api_v1_filters_post**](docs/FiltersApi.md#api_v1_filters_post) | **POST** /api/v1/filters | Create a filter and populate it with items.
*FiltersApi* | [**api_v1_filters_type_id_active_patch**](docs/FiltersApi.md#api_v1_filters_type_id_active_patch) | **PATCH** /api/v1/filters/{type}/{id}/active | Activate or deactivate a filter (exclusion types only).
*FiltersApi* | [**api_v1_filters_type_id_delete**](docs/FiltersApi.md#api_v1_filters_type_id_delete) | **DELETE** /api/v1/filters/{type}/{id} | Delete a filter (and its items, for IP pools).
*FiltersApi* | [**api_v1_filters_type_id_get**](docs/FiltersApi.md#api_v1_filters_type_id_get) | **GET** /api/v1/filters/{type}/{id} | Get a single filter with its items.
*FiltersApi* | [**api_v1_filters_type_id_items_item_delete**](docs/FiltersApi.md#api_v1_filters_type_id_items_item_delete) | **DELETE** /api/v1/filters/{type}/{id}/items/{item} | Remove a single item from a filter.
*FiltersApi* | [**api_v1_filters_type_id_items_post**](docs/FiltersApi.md#api_v1_filters_type_id_items_post) | **POST** /api/v1/filters/{type}/{id}/items | Add items to an existing filter.
*FiltersApi* | [**api_v1_filters_type_id_put**](docs/FiltersApi.md#api_v1_filters_type_id_put) | **PUT** /api/v1/filters/{type}/{id} | Edit a filter (rename, replace items, change scope).
*FundsApi* | [**api_v1_funds_balance_settings_put**](docs/FundsApi.md#api_v1_funds_balance_settings_put) | **PUT** /api/v1/funds/balance-settings | Set the low-balance warning.
*FundsApi* | [**api_v1_funds_deposit_type_fid_get**](docs/FundsApi.md#api_v1_funds_deposit_type_fid_get) | **GET** /api/v1/funds/deposit/{type}/{fid} | Checkout data for an open deposit — or its paid state.
*FundsApi* | [**api_v1_funds_deposit_type_post**](docs/FundsApi.md#api_v1_funds_deposit_type_post) | **POST** /api/v1/funds/deposit/{type} | Open a deposit (or redeem a bonus / coupon code).
*FundsApi* | [**api_v1_funds_deposits_id_delete**](docs/FundsApi.md#api_v1_funds_deposits_id_delete) | **DELETE** /api/v1/funds/deposits/{id} | Cancel an unpaid deposit.
*FundsApi* | [**api_v1_funds_deposits_id_proof_get**](docs/FundsApi.md#api_v1_funds_deposits_id_proof_get) | **GET** /api/v1/funds/deposits/{id}/proof | Download the proof of payment you uploaded on a deposit.
*FundsApi* | [**api_v1_funds_deposits_id_proof_post**](docs/FundsApi.md#api_v1_funds_deposits_id_proof_post) | **POST** /api/v1/funds/deposits/{id}/proof | Upload the proof of payment of an open bank or Wise deposit.
*FundsApi* | [**api_v1_funds_deposits_id_txn_hash_post**](docs/FundsApi.md#api_v1_funds_deposits_id_txn_hash_post) | **POST** /api/v1/funds/deposits/{id}/txn-hash | Attach the transaction hash of a manual crypto deposit, or the transaction ID of a Payoneer deposit.
*FundsApi* | [**api_v1_funds_get**](docs/FundsApi.md#api_v1_funds_get) | **GET** /api/v1/funds | Current advertiser balance + pending deposits.
*FundsApi* | [**api_v1_funds_pay_types_get**](docs/FundsApi.md#api_v1_funds_pay_types_get) | **GET** /api/v1/funds/pay-types | Payment methods this account can deposit with.
*FundsApi* | [**api_v1_funds_transactions_get**](docs/FundsApi.md#api_v1_funds_transactions_get) | **GET** /api/v1/funds/transactions | Funds ledger — deposits, bonuses, transfers, refunds.
*FundsApi* | [**api_v1_funds_transfer_post**](docs/FundsApi.md#api_v1_funds_transfer_post) | **POST** /api/v1/funds/transfer | Move balance to a connected advertiser account.
*LookupsApi* | [**api_v1_lookups_adspace_types_get**](docs/LookupsApi.md#api_v1_lookups_adspace_types_get) | **GET** /api/v1/lookups/adspace-types | Adspace types the caller can publish on this tenant.
*LookupsApi* | [**api_v1_lookups_adzone_locations_get**](docs/LookupsApi.md#api_v1_lookups_adzone_locations_get) | **GET** /api/v1/lookups/adzone-locations | Adzone locations for the tenant.
*LookupsApi* | [**api_v1_lookups_adzones_get**](docs/LookupsApi.md#api_v1_lookups_adzones_get) | **GET** /api/v1/lookups/adzones | Find adzone ids (for adzone filters).
*LookupsApi* | [**api_v1_lookups_banner_sizes_get**](docs/LookupsApi.md#api_v1_lookups_banner_sizes_get) | **GET** /api/v1/lookups/banner-sizes | Banner sizes for banner-flavored adspaces.
*LookupsApi* | [**api_v1_lookups_browsers_get**](docs/LookupsApi.md#api_v1_lookups_browsers_get) | **GET** /api/v1/lookups/browsers | Browser ids (optionally scoped by device type).
*LookupsApi* | [**api_v1_lookups_carriers_get**](docs/LookupsApi.md#api_v1_lookups_carriers_get) | **GET** /api/v1/lookups/carriers | Mobile carriers (ids for carrier targeting).
*LookupsApi* | [**api_v1_lookups_categories_get**](docs/LookupsApi.md#api_v1_lookups_categories_get) | **GET** /api/v1/lookups/categories | Active sub-categories (optionally scoped to a main).
*LookupsApi* | [**api_v1_lookups_device_types_get**](docs/LookupsApi.md#api_v1_lookups_device_types_get) | **GET** /api/v1/lookups/device-types | Active device types for this tenant.
*LookupsApi* | [**api_v1_lookups_domains_get**](docs/LookupsApi.md#api_v1_lookups_domains_get) | **GET** /api/v1/lookups/domains | Resolve domains to the ids domain filters store.
*LookupsApi* | [**api_v1_lookups_isps_get**](docs/LookupsApi.md#api_v1_lookups_isps_get) | **GET** /api/v1/lookups/isps | Find ISP ids (for ISP filters).
*LookupsApi* | [**api_v1_lookups_link_types_get**](docs/LookupsApi.md#api_v1_lookups_link_types_get) | **GET** /api/v1/lookups/link-types | Active link types for the tenant.
*LookupsApi* | [**api_v1_lookups_main_categories_get**](docs/LookupsApi.md#api_v1_lookups_main_categories_get) | **GET** /api/v1/lookups/main-categories | Active main categories for the tenant.
*LookupsApi* | [**api_v1_lookups_operating_systems_get**](docs/LookupsApi.md#api_v1_lookups_operating_systems_get) | **GET** /api/v1/lookups/operating-systems | Operating-system ids (optionally scoped by device type).
*LookupsApi* | [**api_v1_lookups_publishers_get**](docs/LookupsApi.md#api_v1_lookups_publishers_get) | **GET** /api/v1/lookups/publishers | Find publisher ids (for publisher_excl filters).
*LookupsApi* | [**api_v1_lookups_ratings_get**](docs/LookupsApi.md#api_v1_lookups_ratings_get) | **GET** /api/v1/lookups/ratings | Active content ratings for the tenant.
*LookupsApi* | [**api_v1_lookups_reel_types_get**](docs/LookupsApi.md#api_v1_lookups_reel_types_get) | **GET** /api/v1/lookups/reel-types | Active reel types for the tenant.
*LookupsApi* | [**api_v1_lookups_regions_get**](docs/LookupsApi.md#api_v1_lookups_regions_get) | **GET** /api/v1/lookups/regions | Walk the geo region tree (one level per call).
*LookupsApi* | [**api_v1_lookups_website_languages_get**](docs/LookupsApi.md#api_v1_lookups_website_languages_get) | **GET** /api/v1/lookups/website-languages | Supported website languages (ISO codes).
*LookupsApi* | [**api_v1_lookups_website_types_get**](docs/LookupsApi.md#api_v1_lookups_website_types_get) | **GET** /api/v1/lookups/website-types | Active website types for the tenant.
*MarketDataApi* | [**api_v1_pricing_filters_get**](docs/MarketDataApi.md#api_v1_pricing_filters_get) | **GET** /api/v1/pricing/filters | Labels for the pricing table&#39;s ids.
*MarketDataApi* | [**api_v1_pricing_get**](docs/MarketDataApi.md#api_v1_pricing_get) | **GET** /api/v1/pricing | Network floor prices (minimum bids).
*MarketDataApi* | [**api_v1_smart_networks_get**](docs/MarketDataApi.md#api_v1_smart_networks_get) | **GET** /api/v1/smart-networks | List the network&#39;s active smart networks.
*MarketDataApi* | [**api_v1_smart_networks_id_get**](docs/MarketDataApi.md#api_v1_smart_networks_id_get) | **GET** /api/v1/smart-networks/{id} | One smart network.
*MarketDataApi* | [**api_v1_volumes_filters_get**](docs/MarketDataApi.md#api_v1_volumes_filters_get) | **GET** /api/v1/volumes/filters | Option lists for the volume query.
*MarketDataApi* | [**api_v1_volumes_get**](docs/MarketDataApi.md#api_v1_volumes_get) | **GET** /api/v1/volumes | Available traffic volume per country (traffic estimate).
*MarketplaceApi* | [**api_v1_marketplace_filters_get**](docs/MarketplaceApi.md#api_v1_marketplace_filters_get) | **GET** /api/v1/marketplace/filters | Filter vocabulary for the marketplace.
*MarketplaceApi* | [**api_v1_marketplace_flat_requests_get**](docs/MarketplaceApi.md#api_v1_marketplace_flat_requests_get) | **GET** /api/v1/marketplace/flat-requests | List my flat-deal requests.
*MarketplaceApi* | [**api_v1_marketplace_flat_requests_id_cancel_post**](docs/MarketplaceApi.md#api_v1_marketplace_flat_requests_id_cancel_post) | **POST** /api/v1/marketplace/flat-requests/{id}/cancel | Withdraw a pending flat-deal request.
*MarketplaceApi* | [**api_v1_marketplace_flat_requests_renew_post**](docs/MarketplaceApi.md#api_v1_marketplace_flat_requests_renew_post) | **POST** /api/v1/marketplace/flat-requests/renew | Propose one more flat deal on a live flat campaign.
*MarketplaceApi* | [**api_v1_marketplace_get**](docs/MarketplaceApi.md#api_v1_marketplace_get) | **GET** /api/v1/marketplace | List marketplace sites.
*MarketplaceApi* | [**api_v1_marketplace_id_get**](docs/MarketplaceApi.md#api_v1_marketplace_id_get) | **GET** /api/v1/marketplace/{id} | Ad zones of one marketplace site, with starting prices.
*OAuthApi* | [**api_public_integrations_hooks_token_post**](docs/OAuthApi.md#api_public_integrations_hooks_token_post) | **POST** /api/public/integrations/hooks/{token} | Incoming webhook — create a lead, contact or task from JSON.
*OAuthApi* | [**api_public_oauth_introspect_post**](docs/OAuthApi.md#api_public_oauth_introspect_post) | **POST** /api/public/oauth/introspect | Introspect one of the calling app&#39;s tokens (RFC 7662).
*OAuthApi* | [**api_public_oauth_metadata_get**](docs/OAuthApi.md#api_public_oauth_metadata_get) | **GET** /api/public/oauth/metadata | Authorization server metadata (RFC 8414) for this host.
*OAuthApi* | [**api_public_oauth_revoke_post**](docs/OAuthApi.md#api_public_oauth_revoke_post) | **POST** /api/public/oauth/revoke | Revoke an access or refresh token (RFC 7009).
*OAuthApi* | [**api_public_oauth_token_post**](docs/OAuthApi.md#api_public_oauth_token_post) | **POST** /api/public/oauth/token | Exchange an authorization code, or rotate a refresh token.
*OffersApi* | [**api_v1_offers_get**](docs/OffersApi.md#api_v1_offers_get) | **GET** /api/v1/offers | List available offers.
*PayoutsApi* | [**api_v1_publisher_finance_earnings_get**](docs/PayoutsApi.md#api_v1_publisher_finance_earnings_get) | **GET** /api/v1/publisher/finance/earnings | Earnings per day, week or month.
*PayoutsApi* | [**api_v1_publisher_finance_get**](docs/PayoutsApi.md#api_v1_publisher_finance_get) | **GET** /api/v1/publisher/finance | Publisher balance and payout rules.
*PayoutsApi* | [**api_v1_publisher_finance_month_earnings_get**](docs/PayoutsApi.md#api_v1_publisher_finance_month_earnings_get) | **GET** /api/v1/publisher/finance/month-earnings | Monthly earnings statements.
*PayoutsApi* | [**api_v1_publisher_finance_payout_request_post**](docs/PayoutsApi.md#api_v1_publisher_finance_payout_request_post) | **POST** /api/v1/publisher/finance/payout-request | Request a payout of the balance.
*PayoutsApi* | [**api_v1_publisher_finance_payout_types_get**](docs/PayoutsApi.md#api_v1_publisher_finance_payout_types_get) | **GET** /api/v1/publisher/finance/payout-types | Payout methods this account may choose.
*PayoutsApi* | [**api_v1_publisher_finance_payouts_get**](docs/PayoutsApi.md#api_v1_publisher_finance_payouts_get) | **GET** /api/v1/publisher/finance/payouts | List payout requests and payouts.
*PayoutsApi* | [**api_v1_publisher_finance_settings_get**](docs/PayoutsApi.md#api_v1_publisher_finance_settings_get) | **GET** /api/v1/publisher/finance/settings | Payout method and payment details.
*PayoutsApi* | [**api_v1_publisher_finance_settings_put**](docs/PayoutsApi.md#api_v1_publisher_finance_settings_put) | **PUT** /api/v1/publisher/finance/settings | Change the payout method or payment details.
*PayoutsApi* | [**api_v1_publisher_finance_transactions_get**](docs/PayoutsApi.md#api_v1_publisher_finance_transactions_get) | **GET** /api/v1/publisher/finance/transactions | List payout transactions (with USD totals).
*PayoutsApi* | [**api_v1_publisher_finance_transactions_id_get**](docs/PayoutsApi.md#api_v1_publisher_finance_transactions_id_get) | **GET** /api/v1/publisher/finance/transactions/{id} | One payout transaction.
*PayoutsApi* | [**api_v1_publisher_finance_transactions_id_invoice_pdf_get**](docs/PayoutsApi.md#api_v1_publisher_finance_transactions_id_invoice_pdf_get) | **GET** /api/v1/publisher/finance/transactions/{id}/invoice-pdf | Download the self-billing invoice PDF of a paid payout.
*PayoutsApi* | [**api_v1_publisher_finance_transfer_to_advertiser_post**](docs/PayoutsApi.md#api_v1_publisher_finance_transfer_to_advertiser_post) | **POST** /api/v1/publisher/finance/transfer-to-advertiser | Move publisher balance to the advertiser budget.
*ProductFeedsApi* | [**api_v1_product_feeds_get**](docs/ProductFeedsApi.md#api_v1_product_feeds_get) | **GET** /api/v1/product-feeds | List product feeds.
*ProductFeedsApi* | [**api_v1_product_feeds_id_delete**](docs/ProductFeedsApi.md#api_v1_product_feeds_id_delete) | **DELETE** /api/v1/product-feeds/{id} | Delete a product feed.
*ProductFeedsApi* | [**api_v1_product_feeds_id_get**](docs/ProductFeedsApi.md#api_v1_product_feeds_id_get) | **GET** /api/v1/product-feeds/{id} | Show a product feed.
*ProductFeedsApi* | [**api_v1_product_feeds_id_items_get**](docs/ProductFeedsApi.md#api_v1_product_feeds_id_items_get) | **GET** /api/v1/product-feeds/{id}/items | The feed&#39;s products and their ads.
*ProductFeedsApi* | [**api_v1_product_feeds_id_patch**](docs/ProductFeedsApi.md#api_v1_product_feeds_id_patch) | **PATCH** /api/v1/product-feeds/{id} | Change a product feed.
*ProductFeedsApi* | [**api_v1_product_feeds_id_sync_post**](docs/ProductFeedsApi.md#api_v1_product_feeds_id_sync_post) | **POST** /api/v1/product-feeds/{id}/sync | Sync a product feed now.
*ProductFeedsApi* | [**api_v1_product_feeds_post**](docs/ProductFeedsApi.md#api_v1_product_feeds_post) | **POST** /api/v1/product-feeds | Add a product feed.
*ProductFeedsApi* | [**api_v1_product_feeds_preview_post**](docs/ProductFeedsApi.md#api_v1_product_feeds_preview_post) | **POST** /api/v1/product-feeds/preview | Preview a dynamic banner.
*PublicApi* | [**api_public_demo_get**](docs/PublicApi.md#api_public_demo_get) | **GET** /api/public/demo | The network&#39;s ad format demo pages.
*PublicApi* | [**api_public_demo_slug_get**](docs/PublicApi.md#api_public_demo_slug_get) | **GET** /api/public/demo/{slug} | One ad format demo page (HTML).
*PublicApi* | [**api_public_offerwall_id_get**](docs/PublicApi.md#api_public_offerwall_id_get) | **GET** /api/public/offerwall/{id} | Offerwall list of an offer zone.
*PublicApi* | [**api_public_openapi_json_get**](docs/PublicApi.md#api_public_openapi_json_get) | **GET** /api/public/openapi.json | OpenAPI spec as JSON.
*PublicApi* | [**api_public_openapi_yaml_get**](docs/PublicApi.md#api_public_openapi_yaml_get) | **GET** /api/public/openapi.yaml | Raw OpenAPI spec (this document).
*PublicApi* | [**api_public_routes_txt_get**](docs/PublicApi.md#api_public_routes_txt_get) | **GET** /api/public/routes.txt | Flat list of public routes — agent-friendly.
*PublisherFiltersApi* | [**api_v1_publisher_filters_get**](docs/PublisherFiltersApi.md#api_v1_publisher_filters_get) | **GET** /api/v1/publisher/filters | List the publisher&#39;s URL block list.
*PublisherFiltersApi* | [**api_v1_publisher_filters_urls_delete**](docs/PublisherFiltersApi.md#api_v1_publisher_filters_urls_delete) | **DELETE** /api/v1/publisher/filters/urls | Remove one or more URLs from the block list.
*PublisherFiltersApi* | [**api_v1_publisher_filters_urls_post**](docs/PublisherFiltersApi.md#api_v1_publisher_filters_urls_post) | **POST** /api/v1/publisher/filters/urls | Add one or more URLs to the block list.
*PushAudienceApi* | [**api_v1_publisher_push_delivery_rules_get**](docs/PushAudienceApi.md#api_v1_publisher_push_delivery_rules_get) | **GET** /api/v1/publisher/push-delivery-rules | List standing delivery rules.
*PushAudienceApi* | [**api_v1_publisher_push_delivery_rules_id_delete**](docs/PushAudienceApi.md#api_v1_publisher_push_delivery_rules_id_delete) | **DELETE** /api/v1/publisher/push-delivery-rules/{id} | Delete a delivery rule.
*PushAudienceApi* | [**api_v1_publisher_push_delivery_rules_id_put**](docs/PushAudienceApi.md#api_v1_publisher_push_delivery_rules_id_put) | **PUT** /api/v1/publisher/push-delivery-rules/{id} | Update a delivery rule.
*PushAudienceApi* | [**api_v1_publisher_push_delivery_rules_post**](docs/PushAudienceApi.md#api_v1_publisher_push_delivery_rules_post) | **POST** /api/v1/publisher/push-delivery-rules | Create a delivery rule.
*PushAudienceApi* | [**api_v1_publisher_push_segments_get**](docs/PushAudienceApi.md#api_v1_publisher_push_segments_get) | **GET** /api/v1/publisher/push-segments | List saved audience segments.
*PushAudienceApi* | [**api_v1_publisher_push_segments_id_delete**](docs/PushAudienceApi.md#api_v1_publisher_push_segments_id_delete) | **DELETE** /api/v1/publisher/push-segments/{id} | Delete an audience segment.
*PushAudienceApi* | [**api_v1_publisher_push_segments_id_put**](docs/PushAudienceApi.md#api_v1_publisher_push_segments_id_put) | **PUT** /api/v1/publisher/push-segments/{id} | Update an audience segment.
*PushAudienceApi* | [**api_v1_publisher_push_segments_post**](docs/PushAudienceApi.md#api_v1_publisher_push_segments_post) | **POST** /api/v1/publisher/push-segments | Create an audience segment.
*PushAudienceApi* | [**api_v1_publisher_push_setup_get**](docs/PushAudienceApi.md#api_v1_publisher_push_setup_get) | **GET** /api/v1/publisher/push-setup | Collector setup facts for the opt-in script.
*PushAudienceApi* | [**api_v1_publisher_push_stats_get**](docs/PushAudienceApi.md#api_v1_publisher_push_stats_get) | **GET** /api/v1/publisher/push-stats | Push delivery performance.
*PushAudienceApi* | [**api_v1_publisher_push_subscribers_action_post**](docs/PushAudienceApi.md#api_v1_publisher_push_subscribers_action_post) | **POST** /api/v1/publisher/push-subscribers/action | Activate, deactivate or delete subscribers in bulk.
*PushAudienceApi* | [**api_v1_publisher_push_subscribers_get**](docs/PushAudienceApi.md#api_v1_publisher_push_subscribers_get) | **GET** /api/v1/publisher/push-subscribers | List captured push subscribers.
*PushCampaignsApi* | [**api_v1_publisher_push_campaigns_get**](docs/PushCampaignsApi.md#api_v1_publisher_push_campaigns_get) | **GET** /api/v1/publisher/push-campaigns | List the caller&#39;s push campaigns.
*PushCampaignsApi* | [**api_v1_publisher_push_campaigns_id_delete**](docs/PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_delete) | **DELETE** /api/v1/publisher/push-campaigns/{id} | Delete a push campaign.
*PushCampaignsApi* | [**api_v1_publisher_push_campaigns_id_put**](docs/PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_put) | **PUT** /api/v1/publisher/push-campaigns/{id} | Update a push campaign&#39;s notification content.
*PushCampaignsApi* | [**api_v1_publisher_push_campaigns_id_send_post**](docs/PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_send_post) | **POST** /api/v1/publisher/push-campaigns/{id}/send | Queue a push campaign for delivery.
*PushCampaignsApi* | [**api_v1_publisher_push_campaigns_post**](docs/PushCampaignsApi.md#api_v1_publisher_push_campaigns_post) | **POST** /api/v1/publisher/push-campaigns | Create a push campaign.
*RetargetingApi* | [**api_v1_retargeting_pixels_get**](docs/RetargetingApi.md#api_v1_retargeting_pixels_get) | **GET** /api/v1/retargeting/pixels | List the caller&#39;s retargeting pixels.
*RetargetingApi* | [**api_v1_retargeting_pixels_id_active_patch**](docs/RetargetingApi.md#api_v1_retargeting_pixels_id_active_patch) | **PATCH** /api/v1/retargeting/pixels/{id}/active | Activate or deactivate a retargeting pixel.
*RetargetingApi* | [**api_v1_retargeting_pixels_id_delete**](docs/RetargetingApi.md#api_v1_retargeting_pixels_id_delete) | **DELETE** /api/v1/retargeting/pixels/{id} | Soft-delete a retargeting pixel and clear its captured visitors.
*RetargetingApi* | [**api_v1_retargeting_pixels_id_get**](docs/RetargetingApi.md#api_v1_retargeting_pixels_id_get) | **GET** /api/v1/retargeting/pixels/{id} | Get one retargeting pixel.
*RetargetingApi* | [**api_v1_retargeting_pixels_id_put**](docs/RetargetingApi.md#api_v1_retargeting_pixels_id_put) | **PUT** /api/v1/retargeting/pixels/{id} | Update a retargeting pixel (name and visitor windows).
*RetargetingApi* | [**api_v1_retargeting_pixels_post**](docs/RetargetingApi.md#api_v1_retargeting_pixels_post) | **POST** /api/v1/retargeting/pixels | Create a retargeting pixel.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_get) | **GET** /api/v1/publisher/ssp/campaigns | List SSP campaigns (feeds).
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_clone_post**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_clone_post) | **POST** /api/v1/publisher/ssp/campaigns/{id}/clone | Clone an SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_get) | **GET** /api/v1/publisher/ssp/campaigns/{id} | Get one SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_put**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id} | Update an SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_test_rtb_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_test_rtb_get) | **GET** /api/v1/publisher/ssp/campaigns/{id}/test-rtb | Context for an RTB test request.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_test_rtb_post**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_test_rtb_post) | **POST** /api/v1/publisher/ssp/campaigns/{id}/test-rtb | Send one test bid request to the feed&#39;s endpoint.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_toggle_delete_put**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_toggle_delete_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id}/toggle-delete | Delete or restore an SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_toggle_pause_put**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_toggle_pause_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id}/toggle-pause | Pause or resume an SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get) | **GET** /api/v1/publisher/ssp/campaigns/{id}/wl-ron-campaigns | RON campaigns that can be whitelisted on a feed.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_post**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_post) | **POST** /api/v1/publisher/ssp/campaigns | Create an SSP campaign.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_campaigns_setup_data_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_setup_data_get) | **GET** /api/v1/publisher/ssp/campaigns/setup-data | Lookups for the SSP campaign form.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_filters_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_filters_get) | **GET** /api/v1/publisher/ssp/filters | Filter values for the SSP campaign list.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_networks_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_networks_get) | **GET** /api/v1/publisher/ssp/networks | RTB networks your SSP campaigns use.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_seller_disclosure_put**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_seller_disclosure_put) | **PUT** /api/v1/publisher/ssp/seller-disclosure | Publish or hide your name in sellers.json.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_sites_id_ads_txt_check_post**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_sites_id_ads_txt_check_post) | **POST** /api/v1/publisher/ssp/sites/{id}/ads-txt-check | Re-check a site&#39;s ads.txt now.
*SSPCampaignsApi* | [**api_v1_publisher_ssp_sites_id_ads_txt_status_get**](docs/SSPCampaignsApi.md#api_v1_publisher_ssp_sites_id_ads_txt_status_get) | **GET** /api/v1/publisher/ssp/sites/{id}/ads-txt-status | Last stored ads.txt check for a site.
*SharedReportsApi* | [**api_v1_shared_reports_get**](docs/SharedReportsApi.md#api_v1_shared_reports_get) | **GET** /api/v1/shared-reports | List shared reports.
*SharedReportsApi* | [**api_v1_shared_reports_id_delete**](docs/SharedReportsApi.md#api_v1_shared_reports_id_delete) | **DELETE** /api/v1/shared-reports/{id} | Delete a shared report.
*SharedReportsApi* | [**api_v1_shared_reports_id_get**](docs/SharedReportsApi.md#api_v1_shared_reports_id_get) | **GET** /api/v1/shared-reports/{id} | Show a shared report.
*SharedReportsApi* | [**api_v1_shared_reports_id_put**](docs/SharedReportsApi.md#api_v1_shared_reports_id_put) | **PUT** /api/v1/shared-reports/{id} | Update a shared report.
*SharedReportsApi* | [**api_v1_shared_reports_id_toggle_active_put**](docs/SharedReportsApi.md#api_v1_shared_reports_id_toggle_active_put) | **PUT** /api/v1/shared-reports/{id}/toggle-active | Switch a report&#39;s link on or off.
*SharedReportsApi* | [**api_v1_shared_reports_post**](docs/SharedReportsApi.md#api_v1_shared_reports_post) | **POST** /api/v1/shared-reports | Create a shared report.
*SharedReportsApi* | [**api_v1_shared_reports_setup_data_get**](docs/SharedReportsApi.md#api_v1_shared_reports_setup_data_get) | **GET** /api/v1/shared-reports/setup-data | Campaigns and sites a report can cover.
*SitesApi* | [**api_v1_domains_get**](docs/SitesApi.md#api_v1_domains_get) | **GET** /api/v1/domains | List your custom domains (Domain Manager).
*SitesApi* | [**api_v1_domains_id_delete**](docs/SitesApi.md#api_v1_domains_id_delete) | **DELETE** /api/v1/domains/{id} | Delete a custom domain.
*SitesApi* | [**api_v1_domains_id_get**](docs/SitesApi.md#api_v1_domains_id_get) | **GET** /api/v1/domains/{id} | Show one custom domain.
*SitesApi* | [**api_v1_domains_id_notes_put**](docs/SitesApi.md#api_v1_domains_id_notes_put) | **PUT** /api/v1/domains/{id}/notes | Set your notes on a domain.
*SitesApi* | [**api_v1_domains_id_redo_post**](docs/SitesApi.md#api_v1_domains_id_redo_post) | **POST** /api/v1/domains/{id}/redo | Retry setting up a domain (DNS / certificate check again).
*SitesApi* | [**api_v1_domains_id_toggle_active_post**](docs/SitesApi.md#api_v1_domains_id_toggle_active_post) | **POST** /api/v1/domains/{id}/toggle-active | Switch a custom domain on or off.
*SitesApi* | [**api_v1_domains_post**](docs/SitesApi.md#api_v1_domains_post) | **POST** /api/v1/domains | Add a custom domain.
*SitesApi* | [**api_v1_sites_get**](docs/SitesApi.md#api_v1_sites_get) | **GET** /api/v1/sites | List the caller&#39;s websites.
*SitesApi* | [**api_v1_sites_id_clone_post**](docs/SitesApi.md#api_v1_sites_id_clone_post) | **POST** /api/v1/sites/{id}/clone | Duplicate a site under a new name and URL, with its ad zones.
*SitesApi* | [**api_v1_sites_id_delete**](docs/SitesApi.md#api_v1_sites_id_delete) | **DELETE** /api/v1/sites/{id} | Soft-delete a site.
*SitesApi* | [**api_v1_sites_id_get**](docs/SitesApi.md#api_v1_sites_id_get) | **GET** /api/v1/sites/{id} | Get a single site.
*SitesApi* | [**api_v1_sites_id_patch**](docs/SitesApi.md#api_v1_sites_id_patch) | **PATCH** /api/v1/sites/{id} | Update a site.
*SitesApi* | [**api_v1_sites_id_recover_post**](docs/SitesApi.md#api_v1_sites_id_recover_post) | **POST** /api/v1/sites/{id}/recover | Reverse a soft-delete on a site.
*SitesApi* | [**api_v1_sites_id_snippets_get**](docs/SitesApi.md#api_v1_sites_id_snippets_get) | **GET** /api/v1/sites/{id}/snippets | List the site&#39;s HTML snippets.
*SitesApi* | [**api_v1_sites_id_snippets_post**](docs/SitesApi.md#api_v1_sites_id_snippets_post) | **POST** /api/v1/sites/{id}/snippets | Add an HTML snippet.
*SitesApi* | [**api_v1_sites_id_snippets_snippet_id_delete**](docs/SitesApi.md#api_v1_sites_id_snippets_snippet_id_delete) | **DELETE** /api/v1/sites/{id}/snippets/{snippetId} | Delete an HTML snippet.
*SitesApi* | [**api_v1_sites_id_snippets_snippet_id_put**](docs/SitesApi.md#api_v1_sites_id_snippets_snippet_id_put) | **PUT** /api/v1/sites/{id}/snippets/{snippetId} | Replace an HTML snippet.
*SitesApi* | [**api_v1_sites_id_verify_post**](docs/SitesApi.md#api_v1_sites_id_verify_post) | **POST** /api/v1/sites/{id}/verify | Trigger HTTP re-check of the site verification meta tag.
*SitesApi* | [**api_v1_sites_post**](docs/SitesApi.md#api_v1_sites_post) | **POST** /api/v1/sites | Create a new website.
*SitesApi* | [**api_v1_sites_schema_get**](docs/SitesApi.md#api_v1_sites_schema_get) | **GET** /api/v1/sites/_schema | Field metadata for site create/update.
*SmartZonesApi* | [**api_v1_publisher_smartzones_distribution_adspaces_id_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_distribution_adspaces_id_get) | **GET** /api/v1/publisher/smartzones/distribution/adspaces/{id} | Network split for one ad zone.
*SmartZonesApi* | [**api_v1_publisher_smartzones_distribution_per_site_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_distribution_per_site_get) | **GET** /api/v1/publisher/smartzones/distribution/per-site | Traffic and earnings split across networks for one site.
*SmartZonesApi* | [**api_v1_publisher_smartzones_distribution_sites_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_distribution_sites_get) | **GET** /api/v1/publisher/smartzones/distribution/sites | Sites that carry smart zones.
*SmartZonesApi* | [**api_v1_publisher_smartzones_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_get) | **GET** /api/v1/publisher/smartzones | List smart zones.
*SmartZonesApi* | [**api_v1_publisher_smartzones_id_delete**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_id_delete) | **DELETE** /api/v1/publisher/smartzones/{id} | Delete a smart zone.
*SmartZonesApi* | [**api_v1_publisher_smartzones_id_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_id_get) | **GET** /api/v1/publisher/smartzones/{id} | Get one smart zone.
*SmartZonesApi* | [**api_v1_publisher_smartzones_id_put**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_id_put) | **PUT** /api/v1/publisher/smartzones/{id} | Update a smart zone.
*SmartZonesApi* | [**api_v1_publisher_smartzones_import_post**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_import_post) | **POST** /api/v1/publisher/smartzones/import | Bulk import smart zones.
*SmartZonesApi* | [**api_v1_publisher_smartzones_networks_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_networks_get) | **GET** /api/v1/publisher/smartzones/networks | List your smart network accounts.
*SmartZonesApi* | [**api_v1_publisher_smartzones_networks_id_delete**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_networks_id_delete) | **DELETE** /api/v1/publisher/smartzones/networks/{id} | Remove a smart network account.
*SmartZonesApi* | [**api_v1_publisher_smartzones_networks_post**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_networks_post) | **POST** /api/v1/publisher/smartzones/networks | Add or update a smart network account.
*SmartZonesApi* | [**api_v1_publisher_smartzones_post**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_post) | **POST** /api/v1/publisher/smartzones | Create a smart zone.
*SmartZonesApi* | [**api_v1_publisher_smartzones_setup_data_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_setup_data_get) | **GET** /api/v1/publisher/smartzones/setup-data | Lookups for the smart-zone form.
*SmartZonesApi* | [**api_v1_publisher_smartzones_ssp_campaigns_get**](docs/SmartZonesApi.md#api_v1_publisher_smartzones_ssp_campaigns_get) | **GET** /api/v1/publisher/smartzones/ssp-campaigns | SSP campaigns usable as a smart zone&#39;s RTB feed.
*SourceOptimizersApi* | [**api_v1_cpa_optimizers_get**](docs/SourceOptimizersApi.md#api_v1_cpa_optimizers_get) | **GET** /api/v1/cpa-optimizers | List CPA optimizers.
*SourceOptimizersApi* | [**api_v1_cpa_optimizers_id_delete**](docs/SourceOptimizersApi.md#api_v1_cpa_optimizers_id_delete) | **DELETE** /api/v1/cpa-optimizers/{id} | Delete a CPA optimizer.
*SourceOptimizersApi* | [**api_v1_cpa_optimizers_id_get**](docs/SourceOptimizersApi.md#api_v1_cpa_optimizers_id_get) | **GET** /api/v1/cpa-optimizers/{id} | Show a CPA optimizer.
*SourceOptimizersApi* | [**api_v1_cpa_optimizers_id_put**](docs/SourceOptimizersApi.md#api_v1_cpa_optimizers_id_put) | **PUT** /api/v1/cpa-optimizers/{id} | Replace a CPA optimizer.
*SourceOptimizersApi* | [**api_v1_cpa_optimizers_post**](docs/SourceOptimizersApi.md#api_v1_cpa_optimizers_post) | **POST** /api/v1/cpa-optimizers | Create a CPA optimizer.
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_active_get**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_active_get) | **GET** /api/v1/cpm-optimizers/active | Does the account have any CPM optimizer?
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_get**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_get) | **GET** /api/v1/cpm-optimizers | List CPM optimizers.
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_id_delete**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_id_delete) | **DELETE** /api/v1/cpm-optimizers/{id} | Delete a CPM optimizer.
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_id_get**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_id_get) | **GET** /api/v1/cpm-optimizers/{id} | Show a CPM optimizer.
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_id_put**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_id_put) | **PUT** /api/v1/cpm-optimizers/{id} | Replace a CPM optimizer.
*SourceOptimizersApi* | [**api_v1_cpm_optimizers_post**](docs/SourceOptimizersApi.md#api_v1_cpm_optimizers_post) | **POST** /api/v1/cpm-optimizers | Create a CPM optimizer.
*SourceOptimizersApi* | [**api_v1_source_optimizer_config_get**](docs/SourceOptimizersApi.md#api_v1_source_optimizer_config_get) | **GET** /api/v1/source-optimizer/config | Option values for the optimizer forms.
*StatsAdvertiserApi* | [**api_v1_advertiser_stats_get**](docs/StatsAdvertiserApi.md#api_v1_advertiser_stats_get) | **GET** /api/v1/advertiser/stats | Display, native and CPM/RON campaign stats.
*StatsAdvertiserOffersApi* | [**api_v1_advertiser_offers_stats_get**](docs/StatsAdvertiserOffersApi.md#api_v1_advertiser_offers_stats_get) | **GET** /api/v1/advertiser/offers/stats | CPA / affiliate offer performance — advertiser side.
*StatsAdvertiserRTBApi* | [**api_v1_advertiser_rtb_stats_get**](docs/StatsAdvertiserRTBApi.md#api_v1_advertiser_rtb_stats_get) | **GET** /api/v1/advertiser/rtb/stats | DSP / RTB-side stats.
*StatsAffiliateApi* | [**api_v1_publisher_offers_postback_log_get**](docs/StatsAffiliateApi.md#api_v1_publisher_offers_postback_log_get) | **GET** /api/v1/publisher/offers/postback-log | Postback log — the conversion postbacks fired to your URLs.
*StatsAffiliateApi* | [**api_v1_publisher_offers_stats_get**](docs/StatsAffiliateApi.md#api_v1_publisher_offers_stats_get) | **GET** /api/v1/publisher/offers/stats | Affiliate / smartlink offer performance — publisher side.
*StatsPublisherApi* | [**api_v1_publisher_stats_get**](docs/StatsPublisherApi.md#api_v1_publisher_stats_get) | **GET** /api/v1/publisher/stats | Publisher earnings (sites / adzones).
*StatsPublisherSSPApi* | [**api_v1_publisher_ssp_stats_details_get**](docs/StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_details_get) | **GET** /api/v1/publisher/ssp/stats/details | SSP report broken down by one dimension.
*StatsPublisherSSPApi* | [**api_v1_publisher_ssp_stats_filters_get**](docs/StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_filters_get) | **GET** /api/v1/publisher/ssp/stats/filters | Filter values for the SSP reports.
*StatsPublisherSSPApi* | [**api_v1_publisher_ssp_stats_flat_get**](docs/StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_flat_get) | **GET** /api/v1/publisher/ssp/stats/flat | SSP report grouped by several dimensions.
*StatsPublisherSSPApi* | [**api_v1_publisher_ssp_stats_get**](docs/StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_get) | **GET** /api/v1/publisher/ssp/stats | SSP / smart-campaign earnings.
*StatsPublisherSmartZonesApi* | [**api_v1_publisher_smartzones_stats_filters_get**](docs/StatsPublisherSmartZonesApi.md#api_v1_publisher_smartzones_stats_filters_get) | **GET** /api/v1/publisher/smartzones/stats/filters | Filter values for smart-zone stats.
*StatsPublisherSmartZonesApi* | [**api_v1_publisher_smartzones_stats_get**](docs/StatsPublisherSmartZonesApi.md#api_v1_publisher_smartzones_stats_get) | **GET** /api/v1/publisher/smartzones/stats | SmartZone (waterfall) earnings.
*TagsApi* | [**api_v1_tags_get**](docs/TagsApi.md#api_v1_tags_get) | **GET** /api/v1/tags | List tags.
*TagsApi* | [**api_v1_tags_id_delete**](docs/TagsApi.md#api_v1_tags_id_delete) | **DELETE** /api/v1/tags/{id} | Delete a tag.
*TagsApi* | [**api_v1_tags_id_get**](docs/TagsApi.md#api_v1_tags_id_get) | **GET** /api/v1/tags/{id} | Show a tag.
*TagsApi* | [**api_v1_tags_id_put**](docs/TagsApi.md#api_v1_tags_id_put) | **PUT** /api/v1/tags/{id} | Rename or move a tag.
*TagsApi* | [**api_v1_tags_mass_delete_post**](docs/TagsApi.md#api_v1_tags_mass_delete_post) | **POST** /api/v1/tags/mass-delete | Delete several tags.
*TagsApi* | [**api_v1_tags_post**](docs/TagsApi.md#api_v1_tags_post) | **POST** /api/v1/tags | Create a tag.
*TrackerAutomationApi* | [**api_v1_tracker_export_type_get**](docs/TrackerAutomationApi.md#api_v1_tracker_export_type_get) | **GET** /api/v1/tracker/export/{type} | Export tracker entities as CSV.
*TrackerAutomationApi* | [**api_v1_tracker_import_type_post**](docs/TrackerAutomationApi.md#api_v1_tracker_import_type_post) | **POST** /api/v1/tracker/import/{type} | Bulk-import offers from CSV.
*TrackerAutomationApi* | [**api_v1_tracker_report_schedules_get**](docs/TrackerAutomationApi.md#api_v1_tracker_report_schedules_get) | **GET** /api/v1/tracker/report-schedules | List scheduled report deliveries.
*TrackerAutomationApi* | [**api_v1_tracker_report_schedules_id_delete**](docs/TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_delete) | **DELETE** /api/v1/tracker/report-schedules/{id} | Delete a report schedule.
*TrackerAutomationApi* | [**api_v1_tracker_report_schedules_id_get**](docs/TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_get) | **GET** /api/v1/tracker/report-schedules/{id} | Get one report schedule.
*TrackerAutomationApi* | [**api_v1_tracker_report_schedules_id_put**](docs/TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_put) | **PUT** /api/v1/tracker/report-schedules/{id} | Update a report schedule.
*TrackerAutomationApi* | [**api_v1_tracker_report_schedules_post**](docs/TrackerAutomationApi.md#api_v1_tracker_report_schedules_post) | **POST** /api/v1/tracker/report-schedules | Schedule a recurring report.
*TrackerAutomationApi* | [**api_v1_tracker_rules_get**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_get) | **GET** /api/v1/tracker/rules | List automation rules.
*TrackerAutomationApi* | [**api_v1_tracker_rules_id_delete**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_id_delete) | **DELETE** /api/v1/tracker/rules/{id} | Delete a rule.
*TrackerAutomationApi* | [**api_v1_tracker_rules_id_executions_get**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_id_executions_get) | **GET** /api/v1/tracker/rules/{id}/executions | Execution history for one rule.
*TrackerAutomationApi* | [**api_v1_tracker_rules_id_get**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_id_get) | **GET** /api/v1/tracker/rules/{id} | Get one rule.
*TrackerAutomationApi* | [**api_v1_tracker_rules_id_put**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_id_put) | **PUT** /api/v1/tracker/rules/{id} | Update a rule.
*TrackerAutomationApi* | [**api_v1_tracker_rules_id_run_post**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_id_run_post) | **POST** /api/v1/tracker/rules/{id}/run | Run a rule now.
*TrackerAutomationApi* | [**api_v1_tracker_rules_post**](docs/TrackerAutomationApi.md#api_v1_tracker_rules_post) | **POST** /api/v1/tracker/rules | Create an automation rule.
*TrackerConversionsApi* | [**api_v1_tracker_conversion_logging_get**](docs/TrackerConversionsApi.md#api_v1_tracker_conversion_logging_get) | **GET** /api/v1/tracker/conversion-logging | Get conversion-logging settings.
*TrackerConversionsApi* | [**api_v1_tracker_conversion_logging_put**](docs/TrackerConversionsApi.md#api_v1_tracker_conversion_logging_put) | **PUT** /api/v1/tracker/conversion-logging | Change conversion-logging settings.
*TrackerConversionsApi* | [**api_v1_tracker_conversion_types_get**](docs/TrackerConversionsApi.md#api_v1_tracker_conversion_types_get) | **GET** /api/v1/tracker/conversion-types | Get the conversion-type labels.
*TrackerConversionsApi* | [**api_v1_tracker_conversion_types_put**](docs/TrackerConversionsApi.md#api_v1_tracker_conversion_types_put) | **PUT** /api/v1/tracker/conversion-types | Rename the conversion types.
*TrackerConversionsApi* | [**api_v1_tracker_conversions_clickid_postbacks_get**](docs/TrackerConversionsApi.md#api_v1_tracker_conversions_clickid_postbacks_get) | **GET** /api/v1/tracker/conversions/{clickid}/postbacks | Outbound postbacks fired for one conversion.
*TrackerConversionsApi* | [**api_v1_tracker_conversions_get**](docs/TrackerConversionsApi.md#api_v1_tracker_conversions_get) | **GET** /api/v1/tracker/conversions | List incoming conversions.
*TrackerConversionsApi* | [**api_v1_tracker_conversions_id_state_put**](docs/TrackerConversionsApi.md#api_v1_tracker_conversions_id_state_put) | **PUT** /api/v1/tracker/conversions/{id}/state | Approve or reject one conversion.
*TrackerConversionsApi* | [**api_v1_tracker_conversions_rejected_get**](docs/TrackerConversionsApi.md#api_v1_tracker_conversions_rejected_get) | **GET** /api/v1/tracker/conversions/rejected | List refused inbound postbacks.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_delete_reports_put**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_delete_reports_put) | **PUT** /api/v1/tracker/ad-networks/delete-reports | Delete pulled spend reports.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_get**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_get) | **GET** /api/v1/tracker/ad-networks | List ad networks.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_id_campaigns_get**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_campaigns_get) | **GET** /api/v1/tracker/ad-networks/{id}/campaigns | Campaigns known on one ad network.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_id_delete**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_delete) | **DELETE** /api/v1/tracker/ad-networks/{id} | Delete an ad network.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_id_get**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_get) | **GET** /api/v1/tracker/ad-networks/{id} | Get one ad network.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_id_put**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_put) | **PUT** /api/v1/tracker/ad-networks/{id} | Update an ad network.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_post**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_post) | **POST** /api/v1/tracker/ad-networks | Create an ad network.
*TrackerNetworksApi* | [**api_v1_tracker_ad_networks_reports_get**](docs/TrackerNetworksApi.md#api_v1_tracker_ad_networks_reports_get) | **GET** /api/v1/tracker/ad-networks/reports | Spend reports pulled from the ad networks.
*TrackerNetworksApi* | [**api_v1_tracker_affiliate_network_templates_get**](docs/TrackerNetworksApi.md#api_v1_tracker_affiliate_network_templates_get) | **GET** /api/v1/tracker/affiliate-network-templates | List affiliate-network templates.
*TrackerNetworksApi* | [**api_v1_tracker_affiliate_networks_get**](docs/TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_get) | **GET** /api/v1/tracker/affiliate-networks | List affiliate networks.
*TrackerNetworksApi* | [**api_v1_tracker_affiliate_networks_id_delete**](docs/TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_id_delete) | **DELETE** /api/v1/tracker/affiliate-networks/{id} | Delete an affiliate network.
*TrackerNetworksApi* | [**api_v1_tracker_affiliate_networks_id_put**](docs/TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_id_put) | **PUT** /api/v1/tracker/affiliate-networks/{id} | Update an affiliate network.
*TrackerNetworksApi* | [**api_v1_tracker_affiliate_networks_post**](docs/TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_post) | **POST** /api/v1/tracker/affiliate-networks | Create an affiliate network.
*TrackerOffersApi* | [**api_v1_tracker_offers_bulk_post**](docs/TrackerOffersApi.md#api_v1_tracker_offers_bulk_post) | **POST** /api/v1/tracker/offers/bulk | Pause, activate or delete many offers.
*TrackerOffersApi* | [**api_v1_tracker_offers_get**](docs/TrackerOffersApi.md#api_v1_tracker_offers_get) | **GET** /api/v1/tracker/offers | List tracker offers.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_delete**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_delete) | **DELETE** /api/v1/tracker/offers/{id} | Delete an offer.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_get**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_get) | **GET** /api/v1/tracker/offers/{id} | Get one offer.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_put**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_put) | **PUT** /api/v1/tracker/offers/{id} | Update an offer.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_urls_post**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_urls_post) | **POST** /api/v1/tracker/offers/{id}/urls | Add a landing URL to an offer.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_urls_url_id_delete**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_urls_url_id_delete) | **DELETE** /api/v1/tracker/offers/{id}/urls/{urlId} | Delete one landing URL.
*TrackerOffersApi* | [**api_v1_tracker_offers_id_urls_url_id_put**](docs/TrackerOffersApi.md#api_v1_tracker_offers_id_urls_url_id_put) | **PUT** /api/v1/tracker/offers/{id}/urls/{urlId} | Update one landing URL.
*TrackerOffersApi* | [**api_v1_tracker_offers_post**](docs/TrackerOffersApi.md#api_v1_tracker_offers_post) | **POST** /api/v1/tracker/offers | Create an offer.
*TrackerReportsApi* | [**api_v1_tracker_cost_summary_get**](docs/TrackerReportsApi.md#api_v1_tracker_cost_summary_get) | **GET** /api/v1/tracker/cost-summary | Spend against revenue.
*TrackerReportsApi* | [**api_v1_tracker_daily_stats_get**](docs/TrackerReportsApi.md#api_v1_tracker_daily_stats_get) | **GET** /api/v1/tracker/daily-stats | Daily performance, filtered.
*TrackerReportsApi* | [**api_v1_tracker_inline_stats_get**](docs/TrackerReportsApi.md#api_v1_tracker_inline_stats_get) | **GET** /api/v1/tracker/inline-stats | Per-row performance for a listing.
*TrackerReportsApi* | [**api_v1_tracker_player_ltv_get**](docs/TrackerReportsApi.md#api_v1_tracker_player_ltv_get) | **GET** /api/v1/tracker/player-ltv | Lifetime value by cohort.
*TrackerReportsApi* | [**api_v1_tracker_postbacks_stats_get**](docs/TrackerReportsApi.md#api_v1_tracker_postbacks_stats_get) | **GET** /api/v1/tracker/postbacks/stats | Outbound postback firing log.
*TrackerReportsApi* | [**api_v1_tracker_recent_clicks_get**](docs/TrackerReportsApi.md#api_v1_tracker_recent_clicks_get) | **GET** /api/v1/tracker/recent-clicks | The most recent clicks.
*TrackerSettingsApi* | [**api_v1_tracker_countries_get**](docs/TrackerSettingsApi.md#api_v1_tracker_countries_get) | **GET** /api/v1/tracker/countries | List countries seen in the caller&#39;s traffic.
*TrackerSettingsApi* | [**api_v1_tracker_custom_params_get**](docs/TrackerSettingsApi.md#api_v1_tracker_custom_params_get) | **GET** /api/v1/tracker/custom-params | Get the custom-parameter slots.
*TrackerSettingsApi* | [**api_v1_tracker_custom_params_put**](docs/TrackerSettingsApi.md#api_v1_tracker_custom_params_put) | **PUT** /api/v1/tracker/custom-params | Name the custom-parameter slots.
*TrackerSettingsApi* | [**api_v1_tracker_settings_get**](docs/TrackerSettingsApi.md#api_v1_tracker_settings_get) | **GET** /api/v1/tracker/settings | Tracker settings for this account.
*TrackerSettingsApi* | [**api_v1_tracker_source_templates_get**](docs/TrackerSettingsApi.md#api_v1_tracker_source_templates_get) | **GET** /api/v1/tracker/source-templates | List traffic-source templates.
*TrackerSettingsApi* | [**api_v1_tracker_tokens_get**](docs/TrackerSettingsApi.md#api_v1_tracker_tokens_get) | **GET** /api/v1/tracker/tokens | List the macro tokens.
*TrackerSourcesApi* | [**api_v1_tracker_cost_drivers_get**](docs/TrackerSourcesApi.md#api_v1_tracker_cost_drivers_get) | **GET** /api/v1/tracker/cost-drivers | List available cost drivers.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_get**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_get) | **GET** /api/v1/tracker/source-accounts | List connected ad accounts.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_id_campaigns_get**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_campaigns_get) | **GET** /api/v1/tracker/source-accounts/{id}/campaigns | Campaigns visible in a connected ad account.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_id_delete**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_delete) | **DELETE** /api/v1/tracker/source-accounts/{id} | Disconnect an ad account.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_id_get**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_get) | **GET** /api/v1/tracker/source-accounts/{id} | Get one connected ad account.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_id_put**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_put) | **PUT** /api/v1/tracker/source-accounts/{id} | Update a connected ad account.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_id_sync_post**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_sync_post) | **POST** /api/v1/tracker/source-accounts/{id}/sync | Pull spend from a connected ad account now.
*TrackerSourcesApi* | [**api_v1_tracker_source_accounts_post**](docs/TrackerSourcesApi.md#api_v1_tracker_source_accounts_post) | **POST** /api/v1/tracker/source-accounts | Connect an ad account.
*TrackerSourcesApi* | [**api_v1_tracker_sources_get**](docs/TrackerSourcesApi.md#api_v1_tracker_sources_get) | **GET** /api/v1/tracker/sources | List traffic sources.
*TrackerSourcesApi* | [**api_v1_tracker_sources_id_delete**](docs/TrackerSourcesApi.md#api_v1_tracker_sources_id_delete) | **DELETE** /api/v1/tracker/sources/{id} | Delete a traffic source.
*TrackerSourcesApi* | [**api_v1_tracker_sources_id_put**](docs/TrackerSourcesApi.md#api_v1_tracker_sources_id_put) | **PUT** /api/v1/tracker/sources/{id} | Update a traffic source.
*TrackerSourcesApi* | [**api_v1_tracker_sources_post**](docs/TrackerSourcesApi.md#api_v1_tracker_sources_post) | **POST** /api/v1/tracker/sources | Create a traffic source.
*TrackerSourcesApi* | [**api_v1_tracker_sources_siteid_campaigns_get**](docs/TrackerSourcesApi.md#api_v1_tracker_sources_siteid_campaigns_get) | **GET** /api/v1/tracker/sources/{siteid}/campaigns | Campaigns reported by a source&#39;s connected ad account.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_bulk_post**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_bulk_post) | **POST** /api/v1/tracker/tracking-links/bulk | Delete many tracking links.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_get**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_get) | **GET** /api/v1/tracker/tracking-links | List tracking links.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_blocklist_get**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_get) | **GET** /api/v1/tracker/tracking-links/{id}/blocklist | List zones blocked on one link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_blocklist_post**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_post) | **POST** /api/v1/tracker/tracking-links/{id}/blocklist | Block a zone on one link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_blocklist_zone_id_delete**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_zone_id_delete) | **DELETE** /api/v1/tracker/tracking-links/{id}/blocklist/{zoneId} | Unblock a zone on one link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_delete**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_delete) | **DELETE** /api/v1/tracker/tracking-links/{id} | Delete a tracking link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_network_binding_delete**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_network_binding_delete) | **DELETE** /api/v1/tracker/tracking-links/{id}/network-binding | Unbind a tracking link from its ad-network campaign.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_network_binding_put**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_network_binding_put) | **PUT** /api/v1/tracker/tracking-links/{id}/network-binding | Bind a tracking link to an ad-network campaign.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_put**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_put) | **PUT** /api/v1/tracker/tracking-links/{id} | Update a tracking link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_toggle_active_post**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_toggle_active_post) | **POST** /api/v1/tracker/tracking-links/{id}/toggle-active | Pause or resume the bound network campaign.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_id_zone_costs_get**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_zone_costs_get) | **GET** /api/v1/tracker/tracking-links/{id}/zone-costs | Per-zone cost and performance for one link.
*TrackerTrackingLinksApi* | [**api_v1_tracker_tracking_links_post**](docs/TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_post) | **POST** /api/v1/tracker/tracking-links | Create a tracking link.
*TrackingApi* | [**api_v1_tracking_conversion_types_get**](docs/TrackingApi.md#api_v1_tracking_conversion_types_get) | **GET** /api/v1/tracking/conversion-types | Available conversion types for the caller&#39;s account.
*TrackingApi* | [**api_v1_tracking_conversion_types_put**](docs/TrackingApi.md#api_v1_tracking_conversion_types_put) | **PUT** /api/v1/tracking/conversion-types | Name conversion-type slots and set the click-id dedup opt-outs.
*TrackingApi* | [**api_v1_tracking_pixels_get**](docs/TrackingApi.md#api_v1_tracking_pixels_get) | **GET** /api/v1/tracking/pixels | Deprecated: List the caller&#39;s conversion-tracking pixels.
*TrackingApi* | [**api_v1_tracking_pixels_id_delete**](docs/TrackingApi.md#api_v1_tracking_pixels_id_delete) | **DELETE** /api/v1/tracking/pixels/{id} | Deprecated: Delete a pixel.
*TrackingApi* | [**api_v1_tracking_pixels_id_get**](docs/TrackingApi.md#api_v1_tracking_pixels_id_get) | **GET** /api/v1/tracking/pixels/{id} | Deprecated: Get one pixel.
*TrackingApi* | [**api_v1_tracking_pixels_id_put**](docs/TrackingApi.md#api_v1_tracking_pixels_id_put) | **PUT** /api/v1/tracking/pixels/{id} | Deprecated: Update a pixel&#39;s name or conversion type.
*TrackingApi* | [**api_v1_tracking_pixels_post**](docs/TrackingApi.md#api_v1_tracking_pixels_post) | **POST** /api/v1/tracking/pixels | Deprecated: Create a new tracking pixel.
*URLPoolsApi* | [**api_v1_url_pools_get**](docs/URLPoolsApi.md#api_v1_url_pools_get) | **GET** /api/v1/url-pools | List URL pools.
*URLPoolsApi* | [**api_v1_url_pools_id_clone_post**](docs/URLPoolsApi.md#api_v1_url_pools_id_clone_post) | **POST** /api/v1/url-pools/{id}/clone | Clone a URL pool with all its URLs.
*URLPoolsApi* | [**api_v1_url_pools_id_delete**](docs/URLPoolsApi.md#api_v1_url_pools_id_delete) | **DELETE** /api/v1/url-pools/{id} | Soft-delete a URL pool.
*URLPoolsApi* | [**api_v1_url_pools_id_get**](docs/URLPoolsApi.md#api_v1_url_pools_id_get) | **GET** /api/v1/url-pools/{id} | Show one URL pool.
*URLPoolsApi* | [**api_v1_url_pools_id_put**](docs/URLPoolsApi.md#api_v1_url_pools_id_put) | **PUT** /api/v1/url-pools/{id} | Update URL pool meta.
*URLPoolsApi* | [**api_v1_url_pools_id_recover_post**](docs/URLPoolsApi.md#api_v1_url_pools_id_recover_post) | **POST** /api/v1/url-pools/{id}/recover | Restore an archived url pool.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_get**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_get) | **GET** /api/v1/url-pools/{id}/urls | List URLs in a pool.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_post**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_post) | **POST** /api/v1/url-pools/{id}/urls | Add a URL to a pool.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_clone_post**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_clone_post) | **POST** /api/v1/url-pools/{id}/urls/{urlId}/clone | Clone a single URL within the same pool.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_delete**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_delete) | **DELETE** /api/v1/url-pools/{id}/urls/{urlId} | Soft-delete a single URL.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_get**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_get) | **GET** /api/v1/url-pools/{id}/urls/{urlId} | Show a single URL.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_put**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId} | Update a single URL.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_toggle_put**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_toggle_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId}/toggle | Toggle a URL on / off.
*URLPoolsApi* | [**api_v1_url_pools_id_urls_url_id_weight_put**](docs/URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_weight_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId}/weight | Set a URL&#39;s rotation weight.
*URLPoolsApi* | [**api_v1_url_pools_id_used_in_get**](docs/URLPoolsApi.md#api_v1_url_pools_id_used_in_get) | **GET** /api/v1/url-pools/{id}/used-in | List campaigns / ads that reference this URL pool.
*URLPoolsApi* | [**api_v1_url_pools_post**](docs/URLPoolsApi.md#api_v1_url_pools_post) | **POST** /api/v1/url-pools | Create a URL pool.
*URLPoolsApi* | [**api_v1_url_pools_replace_url_put**](docs/URLPoolsApi.md#api_v1_url_pools_replace_url_put) | **PUT** /api/v1/url-pools/replace-url | Search &amp; replace text across your URL-pool URLs.
*WebhooksEventsApi* | [**api_v1_events_get**](docs/WebhooksEventsApi.md#api_v1_events_get) | **GET** /api/v1/events | Read the account&#39;s event feed.
*WebhooksEventsApi* | [**api_v1_webhooks_get**](docs/WebhooksEventsApi.md#api_v1_webhooks_get) | **GET** /api/v1/webhooks | List webhooks.
*WebhooksEventsApi* | [**api_v1_webhooks_id_delete**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_delete) | **DELETE** /api/v1/webhooks/{id} | Remove a webhook.
*WebhooksEventsApi* | [**api_v1_webhooks_id_deliveries_delivery_redeliver_post**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_deliveries_delivery_redeliver_post) | **POST** /api/v1/webhooks/{id}/deliveries/{delivery}/redeliver | Send a delivery again.
*WebhooksEventsApi* | [**api_v1_webhooks_id_deliveries_get**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_deliveries_get) | **GET** /api/v1/webhooks/{id}/deliveries | List a webhook&#39;s deliveries.
*WebhooksEventsApi* | [**api_v1_webhooks_id_get**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_get) | **GET** /api/v1/webhooks/{id} | Get one webhook.
*WebhooksEventsApi* | [**api_v1_webhooks_id_patch**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_patch) | **PATCH** /api/v1/webhooks/{id} | Edit, pause or resume a webhook.
*WebhooksEventsApi* | [**api_v1_webhooks_id_rotate_secret_post**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_rotate_secret_post) | **POST** /api/v1/webhooks/{id}/rotate-secret | Issue a new signing secret.
*WebhooksEventsApi* | [**api_v1_webhooks_id_test_post**](docs/WebhooksEventsApi.md#api_v1_webhooks_id_test_post) | **POST** /api/v1/webhooks/{id}/test | Send a test ping.
*WebhooksEventsApi* | [**api_v1_webhooks_post**](docs/WebhooksEventsApi.md#api_v1_webhooks_post) | **POST** /api/v1/webhooks | Create a webhook.
*XMLFeedsApi* | [**api_v1_xml_feeds_get**](docs/XMLFeedsApi.md#api_v1_xml_feeds_get) | **GET** /api/v1/xml-feeds | List XML feeds.
*XMLFeedsApi* | [**api_v1_xml_feeds_id_clone_post**](docs/XMLFeedsApi.md#api_v1_xml_feeds_id_clone_post) | **POST** /api/v1/xml-feeds/{id}/clone | Clone an XML feed.
*XMLFeedsApi* | [**api_v1_xml_feeds_id_delete**](docs/XMLFeedsApi.md#api_v1_xml_feeds_id_delete) | **DELETE** /api/v1/xml-feeds/{id} | Delete an XML feed.
*XMLFeedsApi* | [**api_v1_xml_feeds_id_get**](docs/XMLFeedsApi.md#api_v1_xml_feeds_id_get) | **GET** /api/v1/xml-feeds/{id} | Show an XML feed.
*XMLFeedsApi* | [**api_v1_xml_feeds_id_put**](docs/XMLFeedsApi.md#api_v1_xml_feeds_id_put) | **PUT** /api/v1/xml-feeds/{id} | Update an XML feed.
*XMLFeedsApi* | [**api_v1_xml_feeds_id_toggle_put**](docs/XMLFeedsApi.md#api_v1_xml_feeds_id_toggle_put) | **PUT** /api/v1/xml-feeds/{id}/toggle | Flip an XML feed active / paused.
*XMLFeedsApi* | [**api_v1_xml_feeds_post**](docs/XMLFeedsApi.md#api_v1_xml_feeds_post) | **POST** /api/v1/xml-feeds | Create an XML feed.


## Documentation For Models

 - [Adspace](docs/Adspace.md)
 - [AdspaceCreate](docs/AdspaceCreate.md)
 - [AdspaceCreateBannerSettings](docs/AdspaceCreateBannerSettings.md)
 - [AdspaceCreateBotSettings](docs/AdspaceCreateBotSettings.md)
 - [AdspaceCreateEmailSettings](docs/AdspaceCreateEmailSettings.md)
 - [AdspaceCreateScreenSettings](docs/AdspaceCreateScreenSettings.md)
 - [AdspaceCreateSearchSettings](docs/AdspaceCreateSearchSettings.md)
 - [AdspaceCreateSearchSettingsBlockedTerms](docs/AdspaceCreateSearchSettingsBlockedTerms.md)
 - [AdspaceFieldMeta](docs/AdspaceFieldMeta.md)
 - [AdspaceNetworkBinding](docs/AdspaceNetworkBinding.md)
 - [AdspaceSchema](docs/AdspaceSchema.md)
 - [AdspaceSettingsBlock](docs/AdspaceSettingsBlock.md)
 - [AdspaceSite](docs/AdspaceSite.md)
 - [AdspaceTypeItem](docs/AdspaceTypeItem.md)
 - [AdspaceTypeOption](docs/AdspaceTypeOption.md)
 - [ApiKeyDetails](docs/ApiKeyDetails.md)
 - [ApiKeyDetailsCreated](docs/ApiKeyDetailsCreated.md)
 - [ApiPublicDemoGet200Response](docs/ApiPublicDemoGet200Response.md)
 - [ApiPublicDemoGet200ResponseDataInner](docs/ApiPublicDemoGet200ResponseDataInner.md)
 - [ApiPublicIntegrationsHooksTokenPost200Response](docs/ApiPublicIntegrationsHooksTokenPost200Response.md)
 - [ApiPublicOauthIntrospectPost200Response](docs/ApiPublicOauthIntrospectPost200Response.md)
 - [ApiPublicOauthTokenPost200Response](docs/ApiPublicOauthTokenPost200Response.md)
 - [ApiPublicOfferwallIdGet200Response](docs/ApiPublicOfferwallIdGet200Response.md)
 - [ApiPublicOfferwallIdGet200ResponseOffersInner](docs/ApiPublicOfferwallIdGet200ResponseOffersInner.md)
 - [ApiV1AccountBillingAveragesGet200Response](docs/ApiV1AccountBillingAveragesGet200Response.md)
 - [ApiV1AccountBillingAveragesGet200ResponseModulesInner](docs/ApiV1AccountBillingAveragesGet200ResponseModulesInner.md)
 - [ApiV1AccountBillingAveragesGet200ResponseOverchargesValue](docs/ApiV1AccountBillingAveragesGet200ResponseOverchargesValue.md)
 - [ApiV1AccountBillingInvoicesGet200Response](docs/ApiV1AccountBillingInvoicesGet200Response.md)
 - [ApiV1AccountBillingInvoicesGet200ResponseResultsInner](docs/ApiV1AccountBillingInvoicesGet200ResponseResultsInner.md)
 - [ApiV1AccountGet200Response](docs/ApiV1AccountGet200Response.md)
 - [ApiV1AccountGet200ResponseApiKey](docs/ApiV1AccountGet200ResponseApiKey.md)
 - [ApiV1AccountNotificationDestinationsPostRequest](docs/ApiV1AccountNotificationDestinationsPostRequest.md)
 - [ApiV1AccountNotificationPreferencesPutRequest](docs/ApiV1AccountNotificationPreferencesPutRequest.md)
 - [ApiV1AccountNotificationsReadPostRequest](docs/ApiV1AccountNotificationsReadPostRequest.md)
 - [ApiV1AccountPreferencesKeyPutRequest](docs/ApiV1AccountPreferencesKeyPutRequest.md)
 - [ApiV1AccountUiLayoutsScopePutRequest](docs/ApiV1AccountUiLayoutsScopePutRequest.md)
 - [ApiV1AccountUiLayoutsScopePutRequestData](docs/ApiV1AccountUiLayoutsScopePutRequestData.md)
 - [ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner](docs/ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner.md)
 - [ApiV1AdScannerIdIgnoreDomainPutRequest](docs/ApiV1AdScannerIdIgnoreDomainPutRequest.md)
 - [ApiV1AdScannerIdManualItemsItemIdStatePutRequest](docs/ApiV1AdScannerIdManualItemsItemIdStatePutRequest.md)
 - [ApiV1AdScannerIdManualItemsPostRequest](docs/ApiV1AdScannerIdManualItemsPostRequest.md)
 - [ApiV1AdScannerIdPutRequest](docs/ApiV1AdScannerIdPutRequest.md)
 - [ApiV1AdScannerIdToggleActivePutRequest](docs/ApiV1AdScannerIdToggleActivePutRequest.md)
 - [ApiV1AdScannerPostRequest](docs/ApiV1AdScannerPostRequest.md)
 - [ApiV1AdScannerPostRequestTags](docs/ApiV1AdScannerPostRequestTags.md)
 - [ApiV1AdShopCartPostRequest](docs/ApiV1AdShopCartPostRequest.md)
 - [ApiV1AdShopConfirmPostRequest](docs/ApiV1AdShopConfirmPostRequest.md)
 - [ApiV1AdShopGroupSummaryPostRequest](docs/ApiV1AdShopGroupSummaryPostRequest.md)
 - [ApiV1AdShopGroupSummaryPostRequestFilters](docs/ApiV1AdShopGroupSummaryPostRequestFilters.md)
 - [ApiV1AdspacesAddMultiplePostRequest](docs/ApiV1AdspacesAddMultiplePostRequest.md)
 - [ApiV1AdspacesExportCodesGet200ResponseInner](docs/ApiV1AdspacesExportCodesGet200ResponseInner.md)
 - [ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner](docs/ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner.md)
 - [ApiV1AdspacesGet200Response](docs/ApiV1AdspacesGet200Response.md)
 - [ApiV1AdspacesGet200ResponseDataInner](docs/ApiV1AdspacesGet200ResponseDataInner.md)
 - [ApiV1AdspacesIdClonePostRequest](docs/ApiV1AdspacesIdClonePostRequest.md)
 - [ApiV1AdspacesIdCodeGet200Response](docs/ApiV1AdspacesIdCodeGet200Response.md)
 - [ApiV1AdspacesIdCodeGet200ResponseAmp](docs/ApiV1AdspacesIdCodeGet200ResponseAmp.md)
 - [ApiV1AdspacesIdCodeGet200ResponseCtv](docs/ApiV1AdspacesIdCodeGet200ResponseCtv.md)
 - [ApiV1AdspacesIdCodeGet200ResponseLayoutsInner](docs/ApiV1AdspacesIdCodeGet200ResponseLayoutsInner.md)
 - [ApiV1AdspacesIdCodeGet200ResponseScreen](docs/ApiV1AdspacesIdCodeGet200ResponseScreen.md)
 - [ApiV1AdspacesIdCodeGet200ResponseSite](docs/ApiV1AdspacesIdCodeGet200ResponseSite.md)
 - [ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest](docs/ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest.md)
 - [ApiV1AdspacesIdMediaBuyingBlockPostRequest](docs/ApiV1AdspacesIdMediaBuyingBlockPostRequest.md)
 - [ApiV1AdspacesIdMediaBuyingIpsPostRequest](docs/ApiV1AdspacesIdMediaBuyingIpsPostRequest.md)
 - [ApiV1AdspacesIdMediaBuyingLaunchPostRequest](docs/ApiV1AdspacesIdMediaBuyingLaunchPostRequest.md)
 - [ApiV1AdspacesIdMediaBuyingReportPostRequest](docs/ApiV1AdspacesIdMediaBuyingReportPostRequest.md)
 - [ApiV1AdspacesIdMediaBuyingSourceBidPutRequest](docs/ApiV1AdspacesIdMediaBuyingSourceBidPutRequest.md)
 - [ApiV1AdspacesIdMediaBuyingTargetingPutRequest](docs/ApiV1AdspacesIdMediaBuyingTargetingPutRequest.md)
 - [ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner](docs/ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner.md)
 - [ApiV1AdspacesIdNetworkBindingPutRequest](docs/ApiV1AdspacesIdNetworkBindingPutRequest.md)
 - [ApiV1AdspacesIdOwnAdsMassActionPostRequest](docs/ApiV1AdspacesIdOwnAdsMassActionPostRequest.md)
 - [ApiV1AdspacesIdPatch200Response](docs/ApiV1AdspacesIdPatch200Response.md)
 - [ApiV1AdspacesIdPricesTypePostRequest](docs/ApiV1AdspacesIdPricesTypePostRequest.md)
 - [ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner](docs/ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner.md)
 - [ApiV1AdspacesIdWlCampaignsPutRequest](docs/ApiV1AdspacesIdWlCampaignsPutRequest.md)
 - [ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner](docs/ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner.md)
 - [ApiV1AdspacesMassDeletePostRequest](docs/ApiV1AdspacesMassDeletePostRequest.md)
 - [ApiV1AdspacesMassRecoverPostRequest](docs/ApiV1AdspacesMassRecoverPostRequest.md)
 - [ApiV1AdspacesTemplatesGet200ResponseInner](docs/ApiV1AdspacesTemplatesGet200ResponseInner.md)
 - [ApiV1AdspacesTemplatesIdPutRequest](docs/ApiV1AdspacesTemplatesIdPutRequest.md)
 - [ApiV1AdspacesTemplatesPostRequest](docs/ApiV1AdspacesTemplatesPostRequest.md)
 - [ApiV1BidRulesetsGet200Response](docs/ApiV1BidRulesetsGet200Response.md)
 - [ApiV1BidRulesetsIdClonePostRequest](docs/ApiV1BidRulesetsIdClonePostRequest.md)
 - [ApiV1BidRulesetsIdDelete200Response](docs/ApiV1BidRulesetsIdDelete200Response.md)
 - [ApiV1BidRulesetsIdDelete422Response](docs/ApiV1BidRulesetsIdDelete422Response.md)
 - [ApiV1BidRulesetsIdPatchRequest](docs/ApiV1BidRulesetsIdPatchRequest.md)
 - [ApiV1BidRulesetsPostRequest](docs/ApiV1BidRulesetsPostRequest.md)
 - [ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest](docs/ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest.md)
 - [ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest](docs/ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest.md)
 - [ApiV1CampaignsGet200Response](docs/ApiV1CampaignsGet200Response.md)
 - [ApiV1CampaignsGet200ResponseDataInner](docs/ApiV1CampaignsGet200ResponseDataInner.md)
 - [ApiV1CampaignsMassDeletePostRequest](docs/ApiV1CampaignsMassDeletePostRequest.md)
 - [ApiV1CampaignsMassTogglePutRequest](docs/ApiV1CampaignsMassTogglePutRequest.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200ResponseZoneBidsInner](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200ResponseZoneBidsInner.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequestZoneBidsInner](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequestZoneBidsInner.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response.md)
 - [ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest](docs/ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest.md)
 - [ApiV1CampaignsRonIdSiteListSiteIdPutRequest](docs/ApiV1CampaignsRonIdSiteListSiteIdPutRequest.md)
 - [ApiV1CampaignsRonIdZonesGet200Response](docs/ApiV1CampaignsRonIdZonesGet200Response.md)
 - [ApiV1CampaignsRonIdZonesGet200ResponseDataInner](docs/ApiV1CampaignsRonIdZonesGet200ResponseDataInner.md)
 - [ApiV1CampaignsSaveCategoriesPutRequest](docs/ApiV1CampaignsSaveCategoriesPutRequest.md)
 - [ApiV1CampaignsSaveTagsPutRequest](docs/ApiV1CampaignsSaveTagsPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response](docs/ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response.md)
 - [ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest](docs/ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsGet200Response](docs/ApiV1CampaignsTypeCampaignIdAdsGet200Response.md)
 - [ApiV1CampaignsTypeCampaignIdAdsGet200ResponseMeta](docs/ApiV1CampaignsTypeCampaignIdAdsGet200ResponseMeta.md)
 - [ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest](docs/ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest](docs/ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest](docs/ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsPostRequest](docs/ApiV1CampaignsTypeCampaignIdAdsPostRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner](docs/ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner.md)
 - [ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest.md)
 - [ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest](docs/ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest.md)
 - [ApiV1CampaignsTypeIdActivePatch200Response](docs/ApiV1CampaignsTypeIdActivePatch200Response.md)
 - [ApiV1CampaignsTypeIdActivePatchRequest](docs/ApiV1CampaignsTypeIdActivePatchRequest.md)
 - [ApiV1CampaignsTypeIdBidsPatch200Response](docs/ApiV1CampaignsTypeIdBidsPatch200Response.md)
 - [ApiV1CampaignsTypeIdBidsPatchRequest](docs/ApiV1CampaignsTypeIdBidsPatchRequest.md)
 - [ApiV1CampaignsTypeIdBudgetPatch200Response](docs/ApiV1CampaignsTypeIdBudgetPatch200Response.md)
 - [ApiV1CampaignsTypeIdBudgetPatchRequest](docs/ApiV1CampaignsTypeIdBudgetPatchRequest.md)
 - [ApiV1CampaignsTypeIdClonePost201Response](docs/ApiV1CampaignsTypeIdClonePost201Response.md)
 - [ApiV1CampaignsTypeIdClonePost201ResponseCopied](docs/ApiV1CampaignsTypeIdClonePost201ResponseCopied.md)
 - [ApiV1CampaignsTypeIdClonePostRequest](docs/ApiV1CampaignsTypeIdClonePostRequest.md)
 - [ApiV1CampaignsTypeIdDelete200Response](docs/ApiV1CampaignsTypeIdDelete200Response.md)
 - [ApiV1CampaignsTypeIdFiltersGet200Response](docs/ApiV1CampaignsTypeIdFiltersGet200Response.md)
 - [ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner](docs/ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner.md)
 - [ApiV1CampaignsTypeIdFiltersPost200Response](docs/ApiV1CampaignsTypeIdFiltersPost200Response.md)
 - [ApiV1CampaignsTypeIdFiltersPostRequest](docs/ApiV1CampaignsTypeIdFiltersPostRequest.md)
 - [ApiV1CampaignsTypeIdMinBidGet200Response](docs/ApiV1CampaignsTypeIdMinBidGet200Response.md)
 - [ApiV1CampaignsTypeIdPatchRequest](docs/ApiV1CampaignsTypeIdPatchRequest.md)
 - [ApiV1CampaignsTypeIdPatchRequestAllOfBannerSizeIds](docs/ApiV1CampaignsTypeIdPatchRequestAllOfBannerSizeIds.md)
 - [ApiV1CampaignsTypeIdZonesPostRequest](docs/ApiV1CampaignsTypeIdZonesPostRequest.md)
 - [ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest](docs/ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest.md)
 - [ApiV1CampaignsTypePostRequest](docs/ApiV1CampaignsTypePostRequest.md)
 - [ApiV1CampaignsTypePostRequestAllOfBannerSizeIds](docs/ApiV1CampaignsTypePostRequestAllOfBannerSizeIds.md)
 - [ApiV1CampaignsTypePostRequestAllOfPriority](docs/ApiV1CampaignsTypePostRequestAllOfPriority.md)
 - [ApiV1CampaignsTypeSchemaAdsGet200Response](docs/ApiV1CampaignsTypeSchemaAdsGet200Response.md)
 - [ApiV1CampaignsTypeSchemaGet200Response](docs/ApiV1CampaignsTypeSchemaGet200Response.md)
 - [ApiV1CampaignsTypeSchemaGet200ResponseFieldsInner](docs/ApiV1CampaignsTypeSchemaGet200ResponseFieldsInner.md)
 - [ApiV1CouponsSetsIdGeneratePostRequest](docs/ApiV1CouponsSetsIdGeneratePostRequest.md)
 - [ApiV1CouponsSetsIdPutRequest](docs/ApiV1CouponsSetsIdPutRequest.md)
 - [ApiV1CouponsSetsPostRequest](docs/ApiV1CouponsSetsPostRequest.md)
 - [ApiV1CreativeFoldersIdPutRequest](docs/ApiV1CreativeFoldersIdPutRequest.md)
 - [ApiV1CreativeFoldersPostRequest](docs/ApiV1CreativeFoldersPostRequest.md)
 - [ApiV1CreativePoolsGet200Response](docs/ApiV1CreativePoolsGet200Response.md)
 - [ApiV1CreativePoolsGet200ResponseDataInner](docs/ApiV1CreativePoolsGet200ResponseDataInner.md)
 - [ApiV1CreativePoolsGetPerPageParameter](docs/ApiV1CreativePoolsGetPerPageParameter.md)
 - [ApiV1CreativePoolsIdAddCreativesPostRequest](docs/ApiV1CreativePoolsIdAddCreativesPostRequest.md)
 - [ApiV1CreativePoolsIdAddUrlsPostRequest](docs/ApiV1CreativePoolsIdAddUrlsPostRequest.md)
 - [ApiV1CreativePoolsIdClonePost201Response](docs/ApiV1CreativePoolsIdClonePost201Response.md)
 - [ApiV1CreativePoolsIdDelete200Response](docs/ApiV1CreativePoolsIdDelete200Response.md)
 - [ApiV1CreativePoolsIdDelete409Response](docs/ApiV1CreativePoolsIdDelete409Response.md)
 - [ApiV1CreativePoolsIdGet200Response](docs/ApiV1CreativePoolsIdGet200Response.md)
 - [ApiV1CreativePoolsIdItemsItemIdPut409Response](docs/ApiV1CreativePoolsIdItemsItemIdPut409Response.md)
 - [ApiV1CreativePoolsIdItemsItemIdPutRequest](docs/ApiV1CreativePoolsIdItemsItemIdPutRequest.md)
 - [ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt](docs/ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt.md)
 - [ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt](docs/ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt.md)
 - [ApiV1CreativePoolsIdItemsMassActionPutRequest](docs/ApiV1CreativePoolsIdItemsMassActionPutRequest.md)
 - [ApiV1CreativePoolsIdItemsPostRequest](docs/ApiV1CreativePoolsIdItemsPostRequest.md)
 - [ApiV1CreativePoolsIdItemsRecoverPostRequest](docs/ApiV1CreativePoolsIdItemsRecoverPostRequest.md)
 - [ApiV1CreativePoolsIdPutRequest](docs/ApiV1CreativePoolsIdPutRequest.md)
 - [ApiV1CreativePoolsIdUsedInGet200Response](docs/ApiV1CreativePoolsIdUsedInGet200Response.md)
 - [ApiV1CreativePoolsPostRequest](docs/ApiV1CreativePoolsPostRequest.md)
 - [ApiV1CreativesBulkDeletePostRequest](docs/ApiV1CreativesBulkDeletePostRequest.md)
 - [ApiV1CreativesBulkMovePostRequest](docs/ApiV1CreativesBulkMovePostRequest.md)
 - [ApiV1CreativesBulkUndeletePostRequest](docs/ApiV1CreativesBulkUndeletePostRequest.md)
 - [ApiV1CreativesGet200Response](docs/ApiV1CreativesGet200Response.md)
 - [ApiV1CreativesGetPerPageParameter](docs/ApiV1CreativesGetPerPageParameter.md)
 - [ApiV1CreativesIdNamePutRequest](docs/ApiV1CreativesIdNamePutRequest.md)
 - [ApiV1CreativesIdPutRequest](docs/ApiV1CreativesIdPutRequest.md)
 - [ApiV1CreativesIdPutRequestTags](docs/ApiV1CreativesIdPutRequestTags.md)
 - [ApiV1CreativesIdTagsPutRequest](docs/ApiV1CreativesIdTagsPutRequest.md)
 - [ApiV1DomainsIdNotesPutRequest](docs/ApiV1DomainsIdNotesPutRequest.md)
 - [ApiV1DomainsPostRequest](docs/ApiV1DomainsPostRequest.md)
 - [ApiV1EventLogExportsPostRequest](docs/ApiV1EventLogExportsPostRequest.md)
 - [ApiV1EventsGet200Response](docs/ApiV1EventsGet200Response.md)
 - [ApiV1FiltersGet200Response](docs/ApiV1FiltersGet200Response.md)
 - [ApiV1FiltersMassActionPostRequest](docs/ApiV1FiltersMassActionPostRequest.md)
 - [ApiV1FiltersMassActionPostRequestFiltersInner](docs/ApiV1FiltersMassActionPostRequestFiltersInner.md)
 - [ApiV1FiltersPostRequest](docs/ApiV1FiltersPostRequest.md)
 - [ApiV1FiltersTypeIdActivePatch200Response](docs/ApiV1FiltersTypeIdActivePatch200Response.md)
 - [ApiV1FiltersTypeIdItemsItemDelete200Response](docs/ApiV1FiltersTypeIdItemsItemDelete200Response.md)
 - [ApiV1FiltersTypeIdItemsPost200Response](docs/ApiV1FiltersTypeIdItemsPost200Response.md)
 - [ApiV1FiltersTypeIdItemsPostRequest](docs/ApiV1FiltersTypeIdItemsPostRequest.md)
 - [ApiV1FiltersTypeIdPutRequest](docs/ApiV1FiltersTypeIdPutRequest.md)
 - [ApiV1FundsBalanceSettingsPutRequest](docs/ApiV1FundsBalanceSettingsPutRequest.md)
 - [ApiV1FundsDepositTypeFidGet200Response](docs/ApiV1FundsDepositTypeFidGet200Response.md)
 - [ApiV1FundsDepositTypePost200Response](docs/ApiV1FundsDepositTypePost200Response.md)
 - [ApiV1FundsDepositTypePostRequest](docs/ApiV1FundsDepositTypePostRequest.md)
 - [ApiV1FundsDepositsIdProofPost200Response](docs/ApiV1FundsDepositsIdProofPost200Response.md)
 - [ApiV1FundsDepositsIdTxnHashPost200Response](docs/ApiV1FundsDepositsIdTxnHashPost200Response.md)
 - [ApiV1FundsDepositsIdTxnHashPostRequest](docs/ApiV1FundsDepositsIdTxnHashPostRequest.md)
 - [ApiV1FundsGet200Response](docs/ApiV1FundsGet200Response.md)
 - [ApiV1FundsPayTypesGet200Response](docs/ApiV1FundsPayTypesGet200Response.md)
 - [ApiV1FundsPayTypesGet200ResponsePayTypesInner](docs/ApiV1FundsPayTypesGet200ResponsePayTypesInner.md)
 - [ApiV1FundsTransactionsGet200Response](docs/ApiV1FundsTransactionsGet200Response.md)
 - [ApiV1FundsTransactionsGet200ResponseDataInner](docs/ApiV1FundsTransactionsGet200ResponseDataInner.md)
 - [ApiV1FundsTransferPostRequest](docs/ApiV1FundsTransferPostRequest.md)
 - [ApiV1LookupsAdspaceTypesGet200Response](docs/ApiV1LookupsAdspaceTypesGet200Response.md)
 - [ApiV1LookupsBannerSizesGet200Response](docs/ApiV1LookupsBannerSizesGet200Response.md)
 - [ApiV1LookupsBannerSizesGet200ResponseItemsInner](docs/ApiV1LookupsBannerSizesGet200ResponseItemsInner.md)
 - [ApiV1LookupsBrowsersGet200Response](docs/ApiV1LookupsBrowsersGet200Response.md)
 - [ApiV1LookupsCarriersGet200Response](docs/ApiV1LookupsCarriersGet200Response.md)
 - [ApiV1LookupsCarriersGet200ResponseDataInner](docs/ApiV1LookupsCarriersGet200ResponseDataInner.md)
 - [ApiV1LookupsCategoriesGet200Response](docs/ApiV1LookupsCategoriesGet200Response.md)
 - [ApiV1LookupsCategoriesGet200ResponseItemsInner](docs/ApiV1LookupsCategoriesGet200ResponseItemsInner.md)
 - [ApiV1LookupsDeviceTypesGet200Response](docs/ApiV1LookupsDeviceTypesGet200Response.md)
 - [ApiV1LookupsRegionsGet200Response](docs/ApiV1LookupsRegionsGet200Response.md)
 - [ApiV1LookupsRegionsGet200ResponseRegionsInner](docs/ApiV1LookupsRegionsGet200ResponseRegionsInner.md)
 - [ApiV1LookupsWebsiteLanguagesGet200Response](docs/ApiV1LookupsWebsiteLanguagesGet200Response.md)
 - [ApiV1LookupsWebsiteLanguagesGet200ResponseItemsInner](docs/ApiV1LookupsWebsiteLanguagesGet200ResponseItemsInner.md)
 - [ApiV1MarketplaceFlatRequestsRenewPostRequest](docs/ApiV1MarketplaceFlatRequestsRenewPostRequest.md)
 - [ApiV1McpPost200Response](docs/ApiV1McpPost200Response.md)
 - [ApiV1McpPost200ResponseError](docs/ApiV1McpPost200ResponseError.md)
 - [ApiV1McpPost200ResponseId](docs/ApiV1McpPost200ResponseId.md)
 - [ApiV1McpPostRequest](docs/ApiV1McpPostRequest.md)
 - [ApiV1McpPostRequestId](docs/ApiV1McpPostRequestId.md)
 - [ApiV1OffersGet200Response](docs/ApiV1OffersGet200Response.md)
 - [ApiV1OffersGet200ResponseDataInner](docs/ApiV1OffersGet200ResponseDataInner.md)
 - [ApiV1ProductFeedsPostRequest](docs/ApiV1ProductFeedsPostRequest.md)
 - [ApiV1ProductFeedsPreviewPostRequest](docs/ApiV1ProductFeedsPreviewPostRequest.md)
 - [ApiV1ProductFeedsPreviewPostRequestProduct](docs/ApiV1ProductFeedsPreviewPostRequestProduct.md)
 - [ApiV1PublisherFiltersGet200Response](docs/ApiV1PublisherFiltersGet200Response.md)
 - [ApiV1PublisherFiltersGet200ResponseCategoriesInner](docs/ApiV1PublisherFiltersGet200ResponseCategoriesInner.md)
 - [ApiV1PublisherFiltersGet200ResponseUrlsInner](docs/ApiV1PublisherFiltersGet200ResponseUrlsInner.md)
 - [ApiV1PublisherFiltersUrlsDelete200Response](docs/ApiV1PublisherFiltersUrlsDelete200Response.md)
 - [ApiV1PublisherFiltersUrlsDeleteRequest](docs/ApiV1PublisherFiltersUrlsDeleteRequest.md)
 - [ApiV1PublisherFiltersUrlsPost201Response](docs/ApiV1PublisherFiltersUrlsPost201Response.md)
 - [ApiV1PublisherFiltersUrlsPostRequest](docs/ApiV1PublisherFiltersUrlsPostRequest.md)
 - [ApiV1PublisherFinanceEarningsGet200Response](docs/ApiV1PublisherFinanceEarningsGet200Response.md)
 - [ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner](docs/ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner.md)
 - [ApiV1PublisherFinanceEarningsGet200ResponsePeriod](docs/ApiV1PublisherFinanceEarningsGet200ResponsePeriod.md)
 - [ApiV1PublisherFinanceEarningsGet200ResponseSummary](docs/ApiV1PublisherFinanceEarningsGet200ResponseSummary.md)
 - [ApiV1PublisherFinanceGet200Response](docs/ApiV1PublisherFinanceGet200Response.md)
 - [ApiV1PublisherFinanceGet200ResponseBalance](docs/ApiV1PublisherFinanceGet200ResponseBalance.md)
 - [ApiV1PublisherFinanceMonthEarningsGet200ResponseInner](docs/ApiV1PublisherFinanceMonthEarningsGet200ResponseInner.md)
 - [ApiV1PublisherFinancePayoutRequestPost201Response](docs/ApiV1PublisherFinancePayoutRequestPost201Response.md)
 - [ApiV1PublisherFinancePayoutRequestPost201ResponsePayout](docs/ApiV1PublisherFinancePayoutRequestPost201ResponsePayout.md)
 - [ApiV1PublisherFinancePayoutRequestPostRequest](docs/ApiV1PublisherFinancePayoutRequestPostRequest.md)
 - [ApiV1PublisherFinancePayoutTypesGet200ResponseInner](docs/ApiV1PublisherFinancePayoutTypesGet200ResponseInner.md)
 - [ApiV1PublisherFinancePayoutsGet200Response](docs/ApiV1PublisherFinancePayoutsGet200Response.md)
 - [ApiV1PublisherFinancePayoutsGet200ResponseDataInner](docs/ApiV1PublisherFinancePayoutsGet200ResponseDataInner.md)
 - [ApiV1PublisherFinancePayoutsGet200ResponseMeta](docs/ApiV1PublisherFinancePayoutsGet200ResponseMeta.md)
 - [ApiV1PublisherFinanceSettingsGet200Response](docs/ApiV1PublisherFinanceSettingsGet200Response.md)
 - [ApiV1PublisherFinanceSettingsGet200ResponseData](docs/ApiV1PublisherFinanceSettingsGet200ResponseData.md)
 - [ApiV1PublisherFinanceSettingsPutRequest](docs/ApiV1PublisherFinanceSettingsPutRequest.md)
 - [ApiV1PublisherFinanceTransactionsGet200Response](docs/ApiV1PublisherFinanceTransactionsGet200Response.md)
 - [ApiV1PublisherFinanceTransactionsGet200ResponseDataInner](docs/ApiV1PublisherFinanceTransactionsGet200ResponseDataInner.md)
 - [ApiV1PublisherFinanceTransactionsIdGet200Response](docs/ApiV1PublisherFinanceTransactionsIdGet200Response.md)
 - [ApiV1PublisherFinanceTransferToAdvertiserPost200Response](docs/ApiV1PublisherFinanceTransferToAdvertiserPost200Response.md)
 - [ApiV1PublisherFinanceTransferToAdvertiserPostRequest](docs/ApiV1PublisherFinanceTransferToAdvertiserPostRequest.md)
 - [ApiV1PublisherOffersPostbackLogGet200Response](docs/ApiV1PublisherOffersPostbackLogGet200Response.md)
 - [ApiV1PublisherOffersPostbackLogGet200ResponseDataInner](docs/ApiV1PublisherOffersPostbackLogGet200ResponseDataInner.md)
 - [ApiV1PublisherPushCampaignsGet200Response](docs/ApiV1PublisherPushCampaignsGet200Response.md)
 - [ApiV1PublisherPushCampaignsIdDelete200Response](docs/ApiV1PublisherPushCampaignsIdDelete200Response.md)
 - [ApiV1PublisherPushCampaignsIdDelete200ResponseData](docs/ApiV1PublisherPushCampaignsIdDelete200ResponseData.md)
 - [ApiV1PublisherPushCampaignsIdSendPost200Response](docs/ApiV1PublisherPushCampaignsIdSendPost200Response.md)
 - [ApiV1PublisherPushCampaignsIdSendPost200ResponseData](docs/ApiV1PublisherPushCampaignsIdSendPost200ResponseData.md)
 - [ApiV1PublisherPushCampaignsPost200Response](docs/ApiV1PublisherPushCampaignsPost200Response.md)
 - [ApiV1PublisherPushCampaignsPostRequest](docs/ApiV1PublisherPushCampaignsPostRequest.md)
 - [ApiV1PublisherPushDeliveryRulesGet200Response](docs/ApiV1PublisherPushDeliveryRulesGet200Response.md)
 - [ApiV1PublisherPushDeliveryRulesIdPutRequest](docs/ApiV1PublisherPushDeliveryRulesIdPutRequest.md)
 - [ApiV1PublisherPushDeliveryRulesPostRequest](docs/ApiV1PublisherPushDeliveryRulesPostRequest.md)
 - [ApiV1PublisherPushSegmentsGet200Response](docs/ApiV1PublisherPushSegmentsGet200Response.md)
 - [ApiV1PublisherPushSegmentsIdPutRequest](docs/ApiV1PublisherPushSegmentsIdPutRequest.md)
 - [ApiV1PublisherPushSegmentsPostRequest](docs/ApiV1PublisherPushSegmentsPostRequest.md)
 - [ApiV1PublisherPushSetupGet200Response](docs/ApiV1PublisherPushSetupGet200Response.md)
 - [ApiV1PublisherPushSetupGet200ResponseData](docs/ApiV1PublisherPushSetupGet200ResponseData.md)
 - [ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner](docs/ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner.md)
 - [ApiV1PublisherPushStatsGet200Response](docs/ApiV1PublisherPushStatsGet200Response.md)
 - [ApiV1PublisherPushStatsGet200ResponseData](docs/ApiV1PublisherPushStatsGet200ResponseData.md)
 - [ApiV1PublisherPushStatsGet200ResponseDataDailyInner](docs/ApiV1PublisherPushStatsGet200ResponseDataDailyInner.md)
 - [ApiV1PublisherPushStatsGet200ResponseDataGrowthInner](docs/ApiV1PublisherPushStatsGet200ResponseDataGrowthInner.md)
 - [ApiV1PublisherPushStatsGet200ResponseDataSummary](docs/ApiV1PublisherPushStatsGet200ResponseDataSummary.md)
 - [ApiV1PublisherPushSubscribersActionPost200Response](docs/ApiV1PublisherPushSubscribersActionPost200Response.md)
 - [ApiV1PublisherPushSubscribersActionPost200ResponseData](docs/ApiV1PublisherPushSubscribersActionPost200ResponseData.md)
 - [ApiV1PublisherPushSubscribersActionPostRequest](docs/ApiV1PublisherPushSubscribersActionPostRequest.md)
 - [ApiV1PublisherPushSubscribersGet200Response](docs/ApiV1PublisherPushSubscribersGet200Response.md)
 - [ApiV1PublisherPushSubscribersGet200ResponseData](docs/ApiV1PublisherPushSubscribersGet200ResponseData.md)
 - [ApiV1PublisherSmartzonesIdPutRequest](docs/ApiV1PublisherSmartzonesIdPutRequest.md)
 - [ApiV1PublisherSmartzonesIdPutRequestIsActive](docs/ApiV1PublisherSmartzonesIdPutRequestIsActive.md)
 - [ApiV1PublisherSmartzonesIdPutRequestUniqueOnly](docs/ApiV1PublisherSmartzonesIdPutRequestUniqueOnly.md)
 - [ApiV1PublisherSmartzonesImportPostRequest](docs/ApiV1PublisherSmartzonesImportPostRequest.md)
 - [ApiV1PublisherSmartzonesImportPostRequestZonesInner](docs/ApiV1PublisherSmartzonesImportPostRequestZonesInner.md)
 - [ApiV1PublisherSmartzonesNetworksPostRequest](docs/ApiV1PublisherSmartzonesNetworksPostRequest.md)
 - [ApiV1PublisherSmartzonesPostRequest](docs/ApiV1PublisherSmartzonesPostRequest.md)
 - [ApiV1PublisherSspCampaignsIdTestRtbPostRequest](docs/ApiV1PublisherSspCampaignsIdTestRtbPostRequest.md)
 - [ApiV1PublisherSspCampaignsIdToggleDeletePutRequest](docs/ApiV1PublisherSspCampaignsIdToggleDeletePutRequest.md)
 - [ApiV1PublisherSspCampaignsIdTogglePausePutRequest](docs/ApiV1PublisherSspCampaignsIdTogglePausePutRequest.md)
 - [ApiV1PublisherSspSellerDisclosurePutRequest](docs/ApiV1PublisherSspSellerDisclosurePutRequest.md)
 - [ApiV1RetargetingPixelsGet200Response](docs/ApiV1RetargetingPixelsGet200Response.md)
 - [ApiV1RetargetingPixelsIdActivePatch200Response](docs/ApiV1RetargetingPixelsIdActivePatch200Response.md)
 - [ApiV1RetargetingPixelsIdDelete200Response](docs/ApiV1RetargetingPixelsIdDelete200Response.md)
 - [ApiV1RtbTestRtbPostRequest](docs/ApiV1RtbTestRtbPostRequest.md)
 - [ApiV1SharedReportsIdPutRequest](docs/ApiV1SharedReportsIdPutRequest.md)
 - [ApiV1SharedReportsIdPutRequestCampaignsInner](docs/ApiV1SharedReportsIdPutRequestCampaignsInner.md)
 - [ApiV1SharedReportsIdPutRequestSitesInner](docs/ApiV1SharedReportsIdPutRequestSitesInner.md)
 - [ApiV1SitesGet200Response](docs/ApiV1SitesGet200Response.md)
 - [ApiV1SitesGet200ResponseDataInner](docs/ApiV1SitesGet200ResponseDataInner.md)
 - [ApiV1SitesIdClonePostRequest](docs/ApiV1SitesIdClonePostRequest.md)
 - [ApiV1SitesSchemaGet200Response](docs/ApiV1SitesSchemaGet200Response.md)
 - [ApiV1SitesSchemaGet200ResponseFieldsInner](docs/ApiV1SitesSchemaGet200ResponseFieldsInner.md)
 - [ApiV1TagsIdPutRequest](docs/ApiV1TagsIdPutRequest.md)
 - [ApiV1TagsMassDeletePostRequest](docs/ApiV1TagsMassDeletePostRequest.md)
 - [ApiV1TagsPostRequest](docs/ApiV1TagsPostRequest.md)
 - [ApiV1ToolsReplaceDomainPutRequest](docs/ApiV1ToolsReplaceDomainPutRequest.md)
 - [ApiV1TrackerAdNetworksDeleteReportsPutRequest](docs/ApiV1TrackerAdNetworksDeleteReportsPutRequest.md)
 - [ApiV1TrackerAdNetworksIdPutRequest](docs/ApiV1TrackerAdNetworksIdPutRequest.md)
 - [ApiV1TrackerAdNetworksPostRequest](docs/ApiV1TrackerAdNetworksPostRequest.md)
 - [ApiV1TrackerAffiliateNetworksGet200Response](docs/ApiV1TrackerAffiliateNetworksGet200Response.md)
 - [ApiV1TrackerAffiliateNetworksIdPutRequest](docs/ApiV1TrackerAffiliateNetworksIdPutRequest.md)
 - [ApiV1TrackerAffiliateNetworksPostRequest](docs/ApiV1TrackerAffiliateNetworksPostRequest.md)
 - [ApiV1TrackerConversionLoggingPutRequest](docs/ApiV1TrackerConversionLoggingPutRequest.md)
 - [ApiV1TrackerConversionTypesPutRequest](docs/ApiV1TrackerConversionTypesPutRequest.md)
 - [ApiV1TrackerConversionsGet200Response](docs/ApiV1TrackerConversionsGet200Response.md)
 - [ApiV1TrackerConversionsGet200ResponseSummary](docs/ApiV1TrackerConversionsGet200ResponseSummary.md)
 - [ApiV1TrackerConversionsIdStatePutRequest](docs/ApiV1TrackerConversionsIdStatePutRequest.md)
 - [ApiV1TrackerCustomParamsPutRequest](docs/ApiV1TrackerCustomParamsPutRequest.md)
 - [ApiV1TrackerCustomParamsPutRequestSlotsInner](docs/ApiV1TrackerCustomParamsPutRequestSlotsInner.md)
 - [ApiV1TrackerOffersBulkPostRequest](docs/ApiV1TrackerOffersBulkPostRequest.md)
 - [ApiV1TrackerOffersGet200Response](docs/ApiV1TrackerOffersGet200Response.md)
 - [ApiV1TrackerOffersIdGet200Response](docs/ApiV1TrackerOffersIdGet200Response.md)
 - [ApiV1TrackerOffersIdPutRequest](docs/ApiV1TrackerOffersIdPutRequest.md)
 - [ApiV1TrackerOffersIdUrlsPostRequest](docs/ApiV1TrackerOffersIdUrlsPostRequest.md)
 - [ApiV1TrackerOffersIdUrlsUrlIdPutRequest](docs/ApiV1TrackerOffersIdUrlsUrlIdPutRequest.md)
 - [ApiV1TrackerOffersPostRequest](docs/ApiV1TrackerOffersPostRequest.md)
 - [ApiV1TrackerOffersPostRequestUrlsInner](docs/ApiV1TrackerOffersPostRequestUrlsInner.md)
 - [ApiV1TrackerReportSchedulesGet200Response](docs/ApiV1TrackerReportSchedulesGet200Response.md)
 - [ApiV1TrackerReportSchedulesIdGet200Response](docs/ApiV1TrackerReportSchedulesIdGet200Response.md)
 - [ApiV1TrackerReportSchedulesIdPutRequest](docs/ApiV1TrackerReportSchedulesIdPutRequest.md)
 - [ApiV1TrackerReportSchedulesPostRequest](docs/ApiV1TrackerReportSchedulesPostRequest.md)
 - [ApiV1TrackerRulesGet200Response](docs/ApiV1TrackerRulesGet200Response.md)
 - [ApiV1TrackerRulesIdGet200Response](docs/ApiV1TrackerRulesIdGet200Response.md)
 - [ApiV1TrackerRulesIdPutRequest](docs/ApiV1TrackerRulesIdPutRequest.md)
 - [ApiV1TrackerRulesPostRequest](docs/ApiV1TrackerRulesPostRequest.md)
 - [ApiV1TrackerSourceAccountsGet200Response](docs/ApiV1TrackerSourceAccountsGet200Response.md)
 - [ApiV1TrackerSourceAccountsIdGet200Response](docs/ApiV1TrackerSourceAccountsIdGet200Response.md)
 - [ApiV1TrackerSourceAccountsIdPutRequest](docs/ApiV1TrackerSourceAccountsIdPutRequest.md)
 - [ApiV1TrackerSourceAccountsPostRequest](docs/ApiV1TrackerSourceAccountsPostRequest.md)
 - [ApiV1TrackerSourcesGet200Response](docs/ApiV1TrackerSourcesGet200Response.md)
 - [ApiV1TrackerSourcesIdPutRequest](docs/ApiV1TrackerSourcesIdPutRequest.md)
 - [ApiV1TrackerSourcesPostRequest](docs/ApiV1TrackerSourcesPostRequest.md)
 - [ApiV1TrackerTrackingLinksBulkPostRequest](docs/ApiV1TrackerTrackingLinksBulkPostRequest.md)
 - [ApiV1TrackerTrackingLinksGet200Response](docs/ApiV1TrackerTrackingLinksGet200Response.md)
 - [ApiV1TrackerTrackingLinksIdBlocklistPostRequest](docs/ApiV1TrackerTrackingLinksIdBlocklistPostRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest.md)
 - [ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest](docs/ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest.md)
 - [ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest](docs/ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest.md)
 - [ApiV1TrackerTrackingLinksIdPutRequest](docs/ApiV1TrackerTrackingLinksIdPutRequest.md)
 - [ApiV1TrackerTrackingLinksIdToggleActivePost200Response](docs/ApiV1TrackerTrackingLinksIdToggleActivePost200Response.md)
 - [ApiV1TrackerTrackingLinksIdToggleActivePost200ResponseData](docs/ApiV1TrackerTrackingLinksIdToggleActivePost200ResponseData.md)
 - [ApiV1TrackerTrackingLinksIdZoneCostsGet200Response](docs/ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)
 - [ApiV1TrackerTrackingLinksPostRequest](docs/ApiV1TrackerTrackingLinksPostRequest.md)
 - [ApiV1TrackingConversionTypesGet200Response](docs/ApiV1TrackingConversionTypesGet200Response.md)
 - [ApiV1TrackingConversionTypesGet200ResponseConversionTypesInner](docs/ApiV1TrackingConversionTypesGet200ResponseConversionTypesInner.md)
 - [ApiV1TrackingConversionTypesPut200Response](docs/ApiV1TrackingConversionTypesPut200Response.md)
 - [ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner](docs/ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner.md)
 - [ApiV1TrackingConversionTypesPutRequest](docs/ApiV1TrackingConversionTypesPutRequest.md)
 - [ApiV1TrackingConversionTypesPutRequestTypesInner](docs/ApiV1TrackingConversionTypesPutRequestTypesInner.md)
 - [ApiV1TrackingPixelsGet200Response](docs/ApiV1TrackingPixelsGet200Response.md)
 - [ApiV1TrackingPixelsIdPutRequest](docs/ApiV1TrackingPixelsIdPutRequest.md)
 - [ApiV1TrackingPixelsPostRequest](docs/ApiV1TrackingPixelsPostRequest.md)
 - [ApiV1UrlPoolsIdPutRequest](docs/ApiV1UrlPoolsIdPutRequest.md)
 - [ApiV1UrlPoolsIdUrlsPostRequest](docs/ApiV1UrlPoolsIdUrlsPostRequest.md)
 - [ApiV1UrlPoolsIdUrlsUrlIdPutRequest](docs/ApiV1UrlPoolsIdUrlsUrlIdPutRequest.md)
 - [ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest](docs/ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest.md)
 - [ApiV1UrlPoolsPostRequest](docs/ApiV1UrlPoolsPostRequest.md)
 - [ApiV1UrlPoolsReplaceUrlPutRequest](docs/ApiV1UrlPoolsReplaceUrlPutRequest.md)
 - [ApiV1WebhooksGet200Response](docs/ApiV1WebhooksGet200Response.md)
 - [ApiV1WebhooksIdDelete200Response](docs/ApiV1WebhooksIdDelete200Response.md)
 - [ApiV1WebhooksIdDeliveriesGet200Response](docs/ApiV1WebhooksIdDeliveriesGet200Response.md)
 - [ApiV1WebhooksIdDeliveriesGet200ResponseDataInner](docs/ApiV1WebhooksIdDeliveriesGet200ResponseDataInner.md)
 - [ApiV1WebhooksIdPatchRequest](docs/ApiV1WebhooksIdPatchRequest.md)
 - [ApiV1WebhooksIdRotateSecretPostRequest](docs/ApiV1WebhooksIdRotateSecretPostRequest.md)
 - [ApiV1WebhooksIdTestPost200Response](docs/ApiV1WebhooksIdTestPost200Response.md)
 - [ApiV1WebhooksIdTestPost200ResponseData](docs/ApiV1WebhooksIdTestPost200ResponseData.md)
 - [ApiV1WebhooksPost201Response](docs/ApiV1WebhooksPost201Response.md)
 - [ApiV1WebhooksPostRequest](docs/ApiV1WebhooksPostRequest.md)
 - [ApiV1XmlFeedsIdPutRequest](docs/ApiV1XmlFeedsIdPutRequest.md)
 - [ApiV1XmlFeedsPostRequest](docs/ApiV1XmlFeedsPostRequest.md)
 - [BidRule](docs/BidRule.md)
 - [BidRuleConditions](docs/BidRuleConditions.md)
 - [BidRuleset](docs/BidRuleset.md)
 - [BidRulesetListItem](docs/BidRulesetListItem.md)
 - [CampaignPanelFields](docs/CampaignPanelFields.md)
 - [CampaignPanelFieldsAboutSettings](docs/CampaignPanelFieldsAboutSettings.md)
 - [CampaignPanelFieldsAvCheck](docs/CampaignPanelFieldsAvCheck.md)
 - [CampaignPanelFieldsBoosterSettings](docs/CampaignPanelFieldsBoosterSettings.md)
 - [CampaignPanelFieldsConversionCapping](docs/CampaignPanelFieldsConversionCapping.md)
 - [CampaignPanelFieldsDayParting](docs/CampaignPanelFieldsDayParting.md)
 - [CampaignPanelFieldsDomainMask](docs/CampaignPanelFieldsDomainMask.md)
 - [CampaignPanelFieldsFeedSettings](docs/CampaignPanelFieldsFeedSettings.md)
 - [CampaignPanelFieldsPriority](docs/CampaignPanelFieldsPriority.md)
 - [CampaignPanelFieldsScreens](docs/CampaignPanelFieldsScreens.md)
 - [CampaignPanelFieldsSuggestions](docs/CampaignPanelFieldsSuggestions.md)
 - [CpaOptimizerBody](docs/CpaOptimizerBody.md)
 - [CpmOptimizerBody](docs/CpmOptimizerBody.md)
 - [Error](docs/Error.md)
 - [FilterDetail](docs/FilterDetail.md)
 - [FilterDetailAllOfRanges](docs/FilterDetailAllOfRanges.md)
 - [FilterSummary](docs/FilterSummary.md)
 - [FilterType](docs/FilterType.md)
 - [FundsDepositProof](docs/FundsDepositProof.md)
 - [FundsTxnClaim](docs/FundsTxnClaim.md)
 - [ListMeta](docs/ListMeta.md)
 - [MediaBuyingPolicy](docs/MediaBuyingPolicy.md)
 - [MediaBuyingPolicyTestPhase](docs/MediaBuyingPolicyTestPhase.md)
 - [OwnAdWrite](docs/OwnAdWrite.md)
 - [PushCampaign](docs/PushCampaign.md)
 - [PushDeliveryRule](docs/PushDeliveryRule.md)
 - [PushSegment](docs/PushSegment.md)
 - [PushSubscriber](docs/PushSubscriber.md)
 - [ResourceFilter](docs/ResourceFilter.md)
 - [RetargetingPixel](docs/RetargetingPixel.md)
 - [RetargetingPixelWrite](docs/RetargetingPixelWrite.md)
 - [RtbTestRequest](docs/RtbTestRequest.md)
 - [RtbTestResult](docs/RtbTestResult.md)
 - [SharedReportAdjust](docs/SharedReportAdjust.md)
 - [SharedReportBody](docs/SharedReportBody.md)
 - [SharedReportBodyCampaignsInner](docs/SharedReportBodyCampaignsInner.md)
 - [SharedReportBodyOptions](docs/SharedReportBodyOptions.md)
 - [SharedReportBodySettings](docs/SharedReportBodySettings.md)
 - [Site](docs/Site.md)
 - [SiteCreate](docs/SiteCreate.md)
 - [SiteSnippetWrite](docs/SiteSnippetWrite.md)
 - [SiteSnippetWriteConditions](docs/SiteSnippetWriteConditions.md)
 - [SspCampaignWrite](docs/SspCampaignWrite.md)
 - [SspCampaignWriteSlotsInner](docs/SspCampaignWriteSlotsInner.md)
 - [SspCampaignWriteZoneurlsInner](docs/SspCampaignWriteZoneurlsInner.md)
 - [StatsResponse](docs/StatsResponse.md)
 - [TrackerAffiliateNetwork](docs/TrackerAffiliateNetwork.md)
 - [TrackerConversion](docs/TrackerConversion.md)
 - [TrackerOffer](docs/TrackerOffer.md)
 - [TrackerReportSchedule](docs/TrackerReportSchedule.md)
 - [TrackerRule](docs/TrackerRule.md)
 - [TrackerSource](docs/TrackerSource.md)
 - [TrackerSourceAccount](docs/TrackerSourceAccount.md)
 - [TrackingLink](docs/TrackingLink.md)
 - [TrackingPixel](docs/TrackingPixel.md)
 - [UserEvent](docs/UserEvent.md)
 - [UserEventType](docs/UserEventType.md)
 - [UserWebhook](docs/UserWebhook.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: Bearer authentication (gas_live_<32 chars>)

<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /oauth/authorize
- **Scopes**: 
 - **campaigns.read**: View campaigns
 - **campaigns.write**: View and change campaigns
 - **stats.read**: View stats
 - **sites.read**: View sites
 - **adspaces.read**: View adspaces
 - **payouts.read**: View publisher earnings and payouts
 - **billing.read**: View billing
 - **webhooks.read**: View webhooks and the event feed
 - **webhooks.write**: Manage webhooks


## Author





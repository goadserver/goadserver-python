# goadserver.AccountApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_account_features_get**](AccountApi.md#api_v1_account_features_get) | **GET** /api/v1/account/features | Self-service features and their state.
[**api_v1_account_get**](AccountApi.md#api_v1_account_get) | **GET** /api/v1/account | Identity check — returns the authenticated user + scopes of the calling key.
[**api_v1_account_memberships_get**](AccountApi.md#api_v1_account_memberships_get) | **GET** /api/v1/account/memberships | Accounts this login can act on.
[**api_v1_account_notices_get**](AccountApi.md#api_v1_account_notices_get) | **GET** /api/v1/account/notices | Account notices.
[**api_v1_account_pending_changes_get**](AccountApi.md#api_v1_account_pending_changes_get) | **GET** /api/v1/account/pending-changes | Profile changes awaiting verification.
[**api_v1_account_preferences_get**](AccountApi.md#api_v1_account_preferences_get) | **GET** /api/v1/account/preferences | Per-member preferences.
[**api_v1_account_preferences_key_put**](AccountApi.md#api_v1_account_preferences_key_put) | **PUT** /api/v1/account/preferences/{key} | Set one preference.
[**api_v1_account_profile_get**](AccountApi.md#api_v1_account_profile_get) | **GET** /api/v1/account/profile | The account&#39;s contact and company details.
[**api_v1_account_sales_referrals_get**](AccountApi.md#api_v1_account_sales_referrals_get) | **GET** /api/v1/account/sales-referrals | Your sales referrals — clients assigned to you, their deposits and your commission.
[**api_v1_account_settings_get**](AccountApi.md#api_v1_account_settings_get) | **GET** /api/v1/account/settings | Account settings.
[**api_v1_account_ui_layouts_get**](AccountApi.md#api_v1_account_ui_layouts_get) | **GET** /api/v1/account/ui-layouts | Saved menu layouts.
[**api_v1_account_ui_layouts_scope_delete**](AccountApi.md#api_v1_account_ui_layouts_scope_delete) | **DELETE** /api/v1/account/ui-layouts/{scope} | Reset a menu layout.
[**api_v1_account_ui_layouts_scope_put**](AccountApi.md#api_v1_account_ui_layouts_scope_put) | **PUT** /api/v1/account/ui-layouts/{scope} | Save a menu layout.
[**api_v1_account_usage_get**](AccountApi.md#api_v1_account_usage_get) | **GET** /api/v1/account/usage | Metered usage for a period.
[**api_v1_account_usage_summary_get**](AccountApi.md#api_v1_account_usage_summary_get) | **GET** /api/v1/account/usage-summary | Inventory counts at a glance.


# **api_v1_account_features_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_features_get()

Self-service features and their state.

Which optional features the account has switched on. Read-only: turning
one on changes what the account is billed for, so activation stays in the
panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Self-service features and their state.
        api_response = api_instance.api_v1_account_features_get()
        print("The response of AccountApi->api_v1_account_features_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_features_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_get**
> ApiV1AccountGet200Response api_v1_account_get()

Identity check — returns the authenticated user + scopes of the calling key.

Minimal identity payload. Use this to verify a key is alive,
discover which user it belongs to, and inspect what scopes the key
was granted. No PII beyond name/email/company.

Key management (create/list/revoke) is **not** exposed via the
public API — it requires a browser session. Visit MyAccount →
API access in the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_get200_response import ApiV1AccountGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Identity check — returns the authenticated user + scopes of the calling key.
        api_response = api_instance.api_v1_account_get()
        print("The response of AccountApi->api_v1_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1AccountGet200Response**](ApiV1AccountGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user identity (and key context if authenticated by API key) |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_memberships_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_memberships_get()

Accounts this login can act on.

Every account the authenticated user is an owner or member of, which of
them is active, and the scopes the membership grants. An API key is
pinned to one account, so this reports rather than switches — the panel's
account switch is not on the public API.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Accounts this login can act on.
        api_response = api_instance.api_v1_account_memberships_get()
        print("The response of AccountApi->api_v1_account_memberships_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_memberships_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_notices_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notices_get()

Account notices.

Standing notices about the account — verification still outstanding, a
field awaiting review, a credential that needs attention.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Account notices.
        api_response = api_instance.api_v1_account_notices_get()
        print("The response of AccountApi->api_v1_account_notices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_notices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_pending_changes_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_pending_changes_get()

Profile changes awaiting verification.

Changes submitted in the panel that are waiting on an emailed code.
Read-only, and account-admin only — the same gate the panel applies.
Cancelling or completing one is part of the verification flow and is not
exposed here.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Profile changes awaiting verification.
        api_response = api_instance.api_v1_account_pending_changes_get()
        print("The response of AccountApi->api_v1_account_pending_changes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_pending_changes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | The key&#39;s account role may not read pending changes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_preferences_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_preferences_get()

Per-member preferences.

The key-value preferences this membership has set — the default dashboard
and similar per-person choices. Scoped to the member, not the account.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Per-member preferences.
        api_response = api_instance.api_v1_account_preferences_get()
        print("The response of AccountApi->api_v1_account_preferences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_preferences_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_preferences_key_put**
> ApiV1WebhooksIdDelete200Response api_v1_account_preferences_key_put(key, api_v1_account_preferences_key_put_request)

Set one preference.

Upserts a single key. Values are opaque to the API.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_preferences_key_put_request import ApiV1AccountPreferencesKeyPutRequest
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response
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
    api_instance = goadserver.AccountApi(api_client)
    key = 'key_example' # str | Preference key.
    api_v1_account_preferences_key_put_request = goadserver.ApiV1AccountPreferencesKeyPutRequest() # ApiV1AccountPreferencesKeyPutRequest | 

    try:
        # Set one preference.
        api_response = api_instance.api_v1_account_preferences_key_put(key, api_v1_account_preferences_key_put_request)
        print("The response of AccountApi->api_v1_account_preferences_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_preferences_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Preference key. | 
 **api_v1_account_preferences_key_put_request** | [**ApiV1AccountPreferencesKeyPutRequest**](ApiV1AccountPreferencesKeyPutRequest.md)|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_profile_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_profile_get()

The account's contact and company details.

Name, company, address, language and contact fields. Read-only here —
changing them goes through the panel's verification flow, which the
public API deliberately does not expose.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # The account's contact and company details.
        api_response = api_instance.api_v1_account_profile_get()
        print("The response of AccountApi->api_v1_account_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_profile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_sales_referrals_get**
> api_v1_account_sales_referrals_get()

Your sales referrals — clients assigned to you, their deposits and your commission.

For an account the network marked as a sales man (sales-referral
module). `data.is_active: false` when it is not. Otherwise `data`
carries `pct` (your commission %), `referral_url` (your signup link:
an account registered through it is assigned to you automatically),
`clients[]` (`userid`, `name`, `company`, `assigned_at`, `deposits`,
`commission`, `currency`), `commissions[]` (one per paid deposit:
`deposit_id`, `client_id`, `name`, `company`, `paid_date`, `deposit`, `pct`,
`commission`, `currency`) and `totals[]` per currency (`commission`,
`commission_month`, `deposits`). Read-only; the network pays commission out
itself. Same handler as the panel's Referrals tab.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Your sales referrals — clients assigned to you, their deposits and your commission.
        api_instance.api_v1_account_sales_referrals_get()
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_sales_referrals_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing or invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_settings_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_settings_get()

Account settings.

Currency, payout preferences, email opt-ins and the account's default
tracking parameters.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Account settings.
        api_response = api_instance.api_v1_account_settings_get()
        print("The response of AccountApi->api_v1_account_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_ui_layouts_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_ui_layouts_get()

Saved menu layouts.

Returns the tenant's layout, this member's own overrides, and whether the
caller may edit the tenant-wide one. See docs/UI_LAYOUT.md.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Saved menu layouts.
        api_response = api_instance.api_v1_account_ui_layouts_get()
        print("The response of AccountApi->api_v1_account_ui_layouts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_ui_layouts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_ui_layouts_scope_delete**
> ApiV1WebhooksIdDelete200Response api_v1_account_ui_layouts_scope_delete(scope)

Reset a menu layout.

Drops the override so the scope falls back to the tenant default.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response
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
    api_instance = goadserver.AccountApi(api_client)
    scope = 'scope_example' # str | Layout scope. `nav.user` — the only scope this API accepts.

    try:
        # Reset a menu layout.
        api_response = api_instance.api_v1_account_ui_layouts_scope_delete(scope)
        print("The response of AccountApi->api_v1_account_ui_layouts_scope_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_ui_layouts_scope_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Layout scope. &#x60;nav.user&#x60; — the only scope this API accepts. | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_ui_layouts_scope_put**
> ApiV1WebhooksIdDelete200Response api_v1_account_ui_layouts_scope_put(scope, api_v1_account_ui_layouts_scope_put_request)

Save a menu layout.

Writes the layout for one scope. Saving the tenant-wide layout needs
the right the panel checks — `can_edit_tenant` in the read tells you
whether this call will be accepted.

`scope` is a registry value, not free text: `nav.user` is the only one
this API accepts. `nav.admin` exists in the same table but belongs to
the admin panel, and the account API refuses it (400 `invalid_scope`)
so a member cannot reach into the admin menu.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_ui_layouts_scope_put_request import ApiV1AccountUiLayoutsScopePutRequest
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response
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
    api_instance = goadserver.AccountApi(api_client)
    scope = 'scope_example' # str | Layout scope, e.g. the panel area the menu belongs to.
    api_v1_account_ui_layouts_scope_put_request = goadserver.ApiV1AccountUiLayoutsScopePutRequest() # ApiV1AccountUiLayoutsScopePutRequest | 

    try:
        # Save a menu layout.
        api_response = api_instance.api_v1_account_ui_layouts_scope_put(scope, api_v1_account_ui_layouts_scope_put_request)
        print("The response of AccountApi->api_v1_account_ui_layouts_scope_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_ui_layouts_scope_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Layout scope, e.g. the panel area the menu belongs to. | 
 **api_v1_account_ui_layouts_scope_put_request** | [**ApiV1AccountUiLayoutsScopePutRequest**](ApiV1AccountUiLayoutsScopePutRequest.md)|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | invalid_scope — unknown scope, or one that belongs to the admin panel. |  -  |
**422** | invalid_layout — the patch list is malformed; the message names the offending patch. |  -  |
**403** | Not allowed to write this scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_usage_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_usage_get(datestart=datestart, dateend=dateend, date_group=date_group)

Metered usage for a period.

What the account has consumed of the metered features it is billed for.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)
    datestart = '2013-10-20' # date | First day (YYYY-MM-DD). Default: 6 days ago. (optional)
    dateend = '2013-10-20' # date | Last day (YYYY-MM-DD). Default: today. (optional)
    date_group = day # str | One row per day / month / year, or one total row for the whole range. (optional) (default to day)

    try:
        # Metered usage for a period.
        api_response = api_instance.api_v1_account_usage_get(datestart=datestart, dateend=dateend, date_group=date_group)
        print("The response of AccountApi->api_v1_account_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datestart** | **date**| First day (YYYY-MM-DD). Default: 6 days ago. | [optional] 
 **dateend** | **date**| Last day (YYYY-MM-DD). Default: today. | [optional] 
 **date_group** | **str**| One row per day / month / year, or one total row for the whole range. | [optional] [default to day]

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_usage_summary_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_usage_summary_get()

Inventory counts at a glance.

Campaign, website and ad-zone counts plus which roles the account holds —
the cheapest way to size an account before pulling its listings.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Inventory counts at a glance.
        api_response = api_instance.api_v1_account_usage_summary_get()
        print("The response of AccountApi->api_v1_account_usage_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_usage_summary_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


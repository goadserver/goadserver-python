# goadserver.AdShopApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_ad_shop_cart_get**](AdShopApi.md#api_v1_ad_shop_cart_get) | **GET** /api/v1/ad-shop/cart | Read the draft cart.
[**api_v1_ad_shop_cart_post**](AdShopApi.md#api_v1_ad_shop_cart_post) | **POST** /api/v1/ad-shop/cart | Replace the draft cart.
[**api_v1_ad_shop_confirm_post**](AdShopApi.md#api_v1_ad_shop_confirm_post) | **POST** /api/v1/ad-shop/confirm | Check out the cart — creates the campaigns.
[**api_v1_ad_shop_filter_options_get**](AdShopApi.md#api_v1_ad_shop_filter_options_get) | **GET** /api/v1/ad-shop/filter-options | Filter values present in the current snapshot.
[**api_v1_ad_shop_group_summary_post**](AdShopApi.md#api_v1_ad_shop_group_summary_post) | **POST** /api/v1/ad-shop/group-summary | Group the catalog by targeting dimensions.
[**api_v1_ad_shop_opportunities_get**](AdShopApi.md#api_v1_ad_shop_opportunities_get) | **GET** /api/v1/ad-shop/opportunities | Browse Ad Shop opportunities.
[**api_v1_ad_shop_plan_get**](AdShopApi.md#api_v1_ad_shop_plan_get) | **GET** /api/v1/ad-shop/plan | Preview how the cart becomes campaigns.


# **api_v1_ad_shop_cart_get**
> api_v1_ad_shop_cart_get()

Read the draft cart.

The current draft cart of the person acting (one for the account owner, and a separate one for each team member, so nobody confirms items someone else picked). Same handler as the panel.

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
    api_instance = goadserver.AdShopApi(api_client)

    try:
        # Read the draft cart.
        api_instance.api_v1_ad_shop_cart_get()
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_cart_get: %s\n" % e)
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
**200** | Cart (empty when none). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_cart_post**
> api_v1_ad_shop_cart_post(api_v1_ad_shop_cart_post_request)

Replace the draft cart.

Stores the full list of picked opportunity ids for a snapshot (replaces, not appends). Same handler as the panel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_shop_cart_post_request import ApiV1AdShopCartPostRequest
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
    api_instance = goadserver.AdShopApi(api_client)
    api_v1_ad_shop_cart_post_request = {"snapshot_id":"20261012-0400","opportunity_ids":[77120,77121]} # ApiV1AdShopCartPostRequest | 

    try:
        # Replace the draft cart.
        api_instance.api_v1_ad_shop_cart_post(api_v1_ad_shop_cart_post_request)
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_cart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_ad_shop_cart_post_request** | [**ApiV1AdShopCartPostRequest**](ApiV1AdShopCartPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved cart. |  -  |
**400** | &#x60;bad_request&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_confirm_post**
> api_v1_ad_shop_confirm_post(api_v1_ad_shop_confirm_post_request)

Check out the cart — creates the campaigns.

Creates the RON campaigns of the plan (live and able to spend once
they have ads) and records an order. `idempotency_key` is
required: a retry with the same key returns the first order
(`reused: true`) instead of buying twice; keys are per account.
Lines that need manual sourcing go to the network's fulfilment
queue and the admins are alerted. With a flat window, a zone
already booked in it fails the whole order (422). Keys pinned to
campaigns cannot confirm (403): the new campaigns would be outside
the pin. A team member with read-only campaign access gets 403
`forbidden` (also on `POST /api/v1/ad-shop/cart`). The campaigns
are recorded as created by, and managed by, whoever confirms, so a
team member limited to their own campaigns can open them afterwards.
Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_shop_confirm_post_request import ApiV1AdShopConfirmPostRequest
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
    api_instance = goadserver.AdShopApi(api_client)
    api_v1_ad_shop_confirm_post_request = {"idempotency_key":"9b2f1c3e-order-1"} # ApiV1AdShopConfirmPostRequest | 

    try:
        # Check out the cart — creates the campaigns.
        api_instance.api_v1_ad_shop_confirm_post(api_v1_ad_shop_confirm_post_request)
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_ad_shop_confirm_post_request** | [**ApiV1AdShopConfirmPostRequest**](ApiV1AdShopConfirmPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order. |  -  |
**400** | &#x60;bad_request&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | &#x60;confirm_failed&#x60; — missing key, empty cart, inventory gone, or flat window already booked (message says which). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_filter_options_get**
> api_v1_ad_shop_filter_options_get()

Filter values present in the current snapshot.

Formats, pay types, countries, devices and categories that occur in the latest snapshot. Same handler as the panel.

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
    api_instance = goadserver.AdShopApi(api_client)

    try:
        # Filter values present in the current snapshot.
        api_instance.api_v1_ad_shop_filter_options_get()
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_filter_options_get: %s\n" % e)
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
**200** | Option lists (empty arrays when there is no snapshot). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_group_summary_post**
> api_v1_ad_shop_group_summary_post(api_v1_ad_shop_group_summary_post_request)

Group the catalog by targeting dimensions.

Read-only (POST only because the filter set is large). Nests the
filtered snapshot by up to 4 of `format`, `country`, `device`,
`category`, `paytype`, with available views / clicks per group
and, for `selected_ids`, the selected totals. Same handler as the
panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_shop_group_summary_post_request import ApiV1AdShopGroupSummaryPostRequest
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
    api_instance = goadserver.AdShopApi(api_client)
    api_v1_ad_shop_group_summary_post_request = {"groups":["country","format"],"filters":{"payTypes":[1]},"selected_ids":[77120]} # ApiV1AdShopGroupSummaryPostRequest | 

    try:
        # Group the catalog by targeting dimensions.
        api_instance.api_v1_ad_shop_group_summary_post(api_v1_ad_shop_group_summary_post_request)
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_group_summary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_ad_shop_group_summary_post_request** | [**ApiV1AdShopGroupSummaryPostRequest**](ApiV1AdShopGroupSummaryPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group tree. |  -  |
**400** | &#x60;bad_request&#x60; — body is not JSON. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | &#x60;bad_group&#x60; — no or more than 4 dimensions, or an unknown one. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_opportunities_get**
> api_v1_ad_shop_opportunities_get(formats=formats, pay_types=pay_types, categories=categories, devices=devices, countries=countries, search=search, sort=sort, direction=direction, page=page, per_page=per_page)

Browse Ad Shop opportunities.

Inventory lines from the tenant's latest opportunity snapshot,
shopped by targeting (format × country × device × category × pay
type) — never by site or zone. `rate` is the advertiser rate in
**currency units** (per click for CPC, per 1000 views for CPM);
`flat_price` (currency units) applies to flat lines.
`availability_status`: available, reserved, manual_confirmation,
auction, unavailable, expired. Same handler as the panel. 404 when
the tenant's Ad Shop module is off.


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
    api_instance = goadserver.AdShopApi(api_client)
    formats = [56] # List[int] | Ad zone type or ad type ids (GET …/filter-options → formats). (optional)
    pay_types = [56] # List[int] | 0 CPC, 1 CPM, 5 flat. (optional)
    categories = [56] # List[int] |  (optional)
    devices = [56] # List[int] |  (optional)
    countries = ['countries_example'] # List[str] |  (optional)
    search = 'search_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    direction = 'direction_example' # str | `hot` with sort=status puts hot lines first. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # Browse Ad Shop opportunities.
        api_instance.api_v1_ad_shop_opportunities_get(formats=formats, pay_types=pay_types, categories=categories, devices=devices, countries=countries, search=search, sort=sort, direction=direction, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_opportunities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formats** | [**List[int]**](int.md)| Ad zone type or ad type ids (GET …/filter-options → formats). | [optional] 
 **pay_types** | [**List[int]**](int.md)| 0 CPC, 1 CPM, 5 flat. | [optional] 
 **categories** | [**List[int]**](int.md)|  | [optional] 
 **devices** | [**List[int]**](int.md)|  | [optional] 
 **countries** | [**List[str]**](str.md)|  | [optional] 
 **search** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **direction** | **str**| &#x60;hot&#x60; with sort&#x3D;status puts hot lines first. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

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
**200** | Lines of the current snapshot. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_shop_plan_get**
> api_v1_ad_shop_plan_get(flat_start=flat_start, flat_end=flat_end)

Preview how the cart becomes campaigns.

No writes. Splits the cart into the campaigns confirm would create
(one per format × pay type …). `bid` and `flat_price` are in
currency units. With a flat window (`flat_start` + `flat_end`) the
lines are priced as flat bookings and `conflicts` lists zones
already booked in that window. Same handler as the panel.


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
    api_instance = goadserver.AdShopApi(api_client)
    flat_start = '2013-10-20' # date |  (optional)
    flat_end = '2013-10-20' # date |  (optional)

    try:
        # Preview how the cart becomes campaigns.
        api_instance.api_v1_ad_shop_plan_get(flat_start=flat_start, flat_end=flat_end)
    except Exception as e:
        print("Exception when calling AdShopApi->api_v1_ad_shop_plan_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flat_start** | **date**|  | [optional] 
 **flat_end** | **date**|  | [optional] 

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
**200** | Plan. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | &#x60;plan_failed&#x60; (message says why, e.g. empty cart). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


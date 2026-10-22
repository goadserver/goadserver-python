# goadserver.MarketplaceApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_marketplace_filters_get**](MarketplaceApi.md#api_v1_marketplace_filters_get) | **GET** /api/v1/marketplace/filters | Filter vocabulary for the marketplace.
[**api_v1_marketplace_flat_requests_get**](MarketplaceApi.md#api_v1_marketplace_flat_requests_get) | **GET** /api/v1/marketplace/flat-requests | List my flat-deal requests.
[**api_v1_marketplace_flat_requests_id_cancel_post**](MarketplaceApi.md#api_v1_marketplace_flat_requests_id_cancel_post) | **POST** /api/v1/marketplace/flat-requests/{id}/cancel | Withdraw a pending flat-deal request.
[**api_v1_marketplace_flat_requests_renew_post**](MarketplaceApi.md#api_v1_marketplace_flat_requests_renew_post) | **POST** /api/v1/marketplace/flat-requests/renew | Propose one more flat deal on a live flat campaign.
[**api_v1_marketplace_get**](MarketplaceApi.md#api_v1_marketplace_get) | **GET** /api/v1/marketplace | List marketplace sites.
[**api_v1_marketplace_id_get**](MarketplaceApi.md#api_v1_marketplace_id_get) | **GET** /api/v1/marketplace/{id} | Ad zones of one marketplace site, with starting prices.


# **api_v1_marketplace_filters_get**
> api_v1_marketplace_filters_get()

Filter vocabulary for the marketplace.

Ad types, ad zone types, countries, banner sizes, device types,
operating systems, browsers and main categories the marketplace
filters accept, plus `flat_request_min_total` (the tenant minimum
for a flat-deal amount, in currency units). Same handler as the
panel.


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
    api_instance = goadserver.MarketplaceApi(api_client)

    try:
        # Filter vocabulary for the marketplace.
        api_instance.api_v1_marketplace_filters_get()
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_filters_get: %s\n" % e)
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
**200** | Option lists. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_marketplace_flat_requests_get**
> api_v1_marketplace_flat_requests_get()

List my flat-deal requests.

The account's flat-deal requests, newest first (max 200). A request
is created by booking a flat deal in the panel's campaign wizard
from a marketplace zone — that create path (`flat_request: 1`) is
not exposed on `POST /api/v1/campaigns` yet. `accepted_campaignid`
is the flat campaign the request created (set from the start, not
only after acceptance). `status`: pending, accepted, rejected,
cancelled. Account-wide: refused (403) for campaign-pinned keys.


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
    api_instance = goadserver.MarketplaceApi(api_client)

    try:
        # List my flat-deal requests.
        api_instance.api_v1_marketplace_flat_requests_get()
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_flat_requests_get: %s\n" % e)
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
**200** | Requests. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_marketplace_flat_requests_id_cancel_post**
> api_v1_marketplace_flat_requests_id_cancel_post(id)

Withdraw a pending flat-deal request.

Only a `pending` request of your own. Also soft-deletes the
(never-served) flat campaign the request created, and tells the
network admins the request is withdrawn. Pinned keys / own-scoped
members are checked against that campaign. Same handler as the
panel. No body.


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
    api_instance = goadserver.MarketplaceApi(api_client)
    id = 56 # int | 

    try:
        # Withdraw a pending flat-deal request.
        api_instance.api_v1_marketplace_flat_requests_id_cancel_post(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_flat_requests_id_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**200** | Cancelled. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found, not yours, or no longer pending (&#x60;{error: ...}&#x60;). |  -  |
**422** | Invalid id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_marketplace_flat_requests_renew_post**
> api_v1_marketplace_flat_requests_renew_post(api_v1_marketplace_flat_requests_renew_post_request)

Propose one more flat deal on a live flat campaign.

Appends a deal (new date window + price) to a flat campaign
(`paytype` 5) that already has an accepted deal, and files it in
the admin's Accept / Reject queue (`deal_state` 0 = pending). Only
one renewal may be pending at a time and the window must start
after the last deal's end and not in the past. `total_costs` is
the deal amount in **currency units** and must be ≥ the tenant's
`flat_request_min_total` (GET /api/v1/marketplace/filters). Same
handler as the panel; campaign pin and member own-scope apply.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_marketplace_flat_requests_renew_post_request import ApiV1MarketplaceFlatRequestsRenewPostRequest
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
    api_instance = goadserver.MarketplaceApi(api_client)
    api_v1_marketplace_flat_requests_renew_post_request = {"campaign_id":90412,"date_start":"2026-11-01","date_end":"2026-11-30","total_costs":1500} # ApiV1MarketplaceFlatRequestsRenewPostRequest | 

    try:
        # Propose one more flat deal on a live flat campaign.
        api_instance.api_v1_marketplace_flat_requests_renew_post(api_v1_marketplace_flat_requests_renew_post_request)
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_flat_requests_renew_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_marketplace_flat_requests_renew_post_request** | [**ApiV1MarketplaceFlatRequestsRenewPostRequest**](ApiV1MarketplaceFlatRequestsRenewPostRequest.md)|  | 

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
**200** | Filed. |  -  |
**403** | Not a flat campaign, or key / member not permitted. |  -  |
**404** | Campaign not found. |  -  |
**409** | &#x60;renewal_pending&#x60;, &#x60;campaign_not_live&#x60; (no accepted deal yet) or &#x60;no_flat_block&#x60;. |  -  |
**422** | Invalid campaign / dates (past start, end before start, overlaps the last deal) or &#x60;total_costs&#x60; below the minimum. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_marketplace_get**
> api_v1_marketplace_get(adtype=adtype, format=format, adzone_type=adzone_type, main_category=main_category, countries=countries, device_type=device_type, search=search, include_ad_shop=include_ad_shop, per_page=per_page)

List marketplace sites.

Publisher sites the network admin put in the marketplace
(`marketplace_websites`), each with its matching zone count and
last-period views / clicks. Offer zones (ad type 21) never appear.
Same handler as the panel. All matching sites are returned in one
page (`last_page` is always 1).


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
    api_instance = goadserver.MarketplaceApi(api_client)
    adtype = 56 # int | Ad type id (GET /api/v1/marketplace/filters → ad_types). (optional)
    format = 56 # int | Banner size id; only with adtype=2. (optional)
    adzone_type = 56 # int | Ad zone type id; implies its ad type when adtype is not sent. (optional)
    main_category = 56 # int |  (optional)
    countries = ['countries_example'] # List[str] | ISO-2 codes; narrows the traffic stats. (optional)
    device_type = 56 # int |  (optional)
    search = 'search_example' # str | Site name / URL substring. (optional)
    include_ad_shop = 'include_ad_shop_example' # str | Also list sites the Ad Shop generator found eligible traffic on. (optional)
    per_page = 40 # int |  (optional) (default to 40)

    try:
        # List marketplace sites.
        api_instance.api_v1_marketplace_get(adtype=adtype, format=format, adzone_type=adzone_type, main_category=main_category, countries=countries, device_type=device_type, search=search, include_ad_shop=include_ad_shop, per_page=per_page)
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adtype** | **int**| Ad type id (GET /api/v1/marketplace/filters → ad_types). | [optional] 
 **format** | **int**| Banner size id; only with adtype&#x3D;2. | [optional] 
 **adzone_type** | **int**| Ad zone type id; implies its ad type when adtype is not sent. | [optional] 
 **main_category** | **int**|  | [optional] 
 **countries** | [**List[str]**](str.md)| ISO-2 codes; narrows the traffic stats. | [optional] 
 **device_type** | **int**|  | [optional] 
 **search** | **str**| Site name / URL substring. | [optional] 
 **include_ad_shop** | **str**| Also list sites the Ad Shop generator found eligible traffic on. | [optional] 
 **per_page** | **int**|  | [optional] [default to 40]

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
**200** | Sites. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_marketplace_id_get**
> api_v1_marketplace_id_get(id, adtype=adtype, format=format, adzone_type=adzone_type, countries=countries, device_type=device_type, os=os, browser=browser, include_ad_shop=include_ad_shop)

Ad zones of one marketplace site, with starting prices.

The zones the admin exposed on the site, filtered by ad type /
format, each with its traffic (`stats`: clicks for click ad types,
views otherwise — see `stat_type`) and a starting price
`min_price`. `min_price` is in **cents** (the panel shows
`min_price / 100` in the account currency); for CPM zones it is
per 1000 views. It comes from recent market rates, else the zone's
own per-country floor (when `countries[]` matches), else the
network floor, else a built-in default. Same handler as the panel.


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
    api_instance = goadserver.MarketplaceApi(api_client)
    id = 56 # int | Site id from GET /api/v1/marketplace.
    adtype = 56 # int |  (optional)
    format = 56 # int |  (optional)
    adzone_type = 56 # int |  (optional)
    countries = ['countries_example'] # List[str] |  (optional)
    device_type = 56 # int |  (optional)
    os = [56] # List[int] |  (optional)
    browser = [56] # List[int] |  (optional)
    include_ad_shop = 'include_ad_shop_example' # str |  (optional)

    try:
        # Ad zones of one marketplace site, with starting prices.
        api_instance.api_v1_marketplace_id_get(id, adtype=adtype, format=format, adzone_type=adzone_type, countries=countries, device_type=device_type, os=os, browser=browser, include_ad_shop=include_ad_shop)
    except Exception as e:
        print("Exception when calling MarketplaceApi->api_v1_marketplace_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site id from GET /api/v1/marketplace. | 
 **adtype** | **int**|  | [optional] 
 **format** | **int**|  | [optional] 
 **adzone_type** | **int**|  | [optional] 
 **countries** | [**List[str]**](str.md)|  | [optional] 
 **device_type** | **int**|  | [optional] 
 **os** | [**List[int]**](int.md)|  | [optional] 
 **browser** | [**List[int]**](int.md)|  | [optional] 
 **include_ad_shop** | **str**|  | [optional] 

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
**200** | Zones. |  -  |
**400** | &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Site not in the marketplace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


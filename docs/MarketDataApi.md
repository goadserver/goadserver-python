# goadserver.MarketDataApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_pricing_filters_get**](MarketDataApi.md#api_v1_pricing_filters_get) | **GET** /api/v1/pricing/filters | Labels for the pricing table&#39;s ids.
[**api_v1_pricing_get**](MarketDataApi.md#api_v1_pricing_get) | **GET** /api/v1/pricing | Network floor prices (minimum bids).
[**api_v1_smart_networks_get**](MarketDataApi.md#api_v1_smart_networks_get) | **GET** /api/v1/smart-networks | List the network&#39;s active smart networks.
[**api_v1_smart_networks_id_get**](MarketDataApi.md#api_v1_smart_networks_id_get) | **GET** /api/v1/smart-networks/{id} | One smart network.
[**api_v1_volumes_filters_get**](MarketDataApi.md#api_v1_volumes_filters_get) | **GET** /api/v1/volumes/filters | Option lists for the volume query.
[**api_v1_volumes_get**](MarketDataApi.md#api_v1_volumes_get) | **GET** /api/v1/volumes | Available traffic volume per country (traffic estimate).


# **api_v1_pricing_filters_get**
> api_v1_pricing_filters_get()

Labels for the pricing table's ids.

Ad types (with the pay types each sells), countries, device / connection types, languages, ISPs, ad zone types and locations. Same handler as the panel.

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
    api_instance = goadserver.MarketDataApi(api_client)

    try:
        # Labels for the pricing table's ids.
        api_instance.api_v1_pricing_filters_get()
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_pricing_filters_get: %s\n" % e)
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
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_pricing_get**
> api_v1_pricing_get()

Network floor prices (minimum bids).

Every `min_prices_ron` row of the network — the minimum bid per ad
type × pay type × device × connection × country × language × ISP
× display type × ad zone location. Unfiltered (the panel filters
client-side). `price` is returned as stored, in the network's main
currency units, exactly as the panel's Pricing page shows it.
`paytype`: 0 CPC, 1 CPM. 404 when the tenant's pricing page module
is off. Same handler as the panel.


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
    api_instance = goadserver.MarketDataApi(api_client)

    try:
        # Network floor prices (minimum bids).
        api_instance.api_v1_pricing_get()
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_pricing_get: %s\n" % e)
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
**200** | Floors. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_smart_networks_get**
> api_v1_smart_networks_get(search=search, filter_id=filter_id, filter_name=filter_name, sort=sort, page=page, per_page=per_page)

List the network's active smart networks.

The `rtb_networks` partners SmartAds campaigns buy through (active, not deleted) — the ids behind `smart_network_id` on ads. Same handler as the panel.

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
    api_instance = goadserver.MarketDataApi(api_client)
    search = 'search_example' # str |  (optional)
    filter_id = 56 # int |  (optional)
    filter_name = 'filter_name_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 56 # int |  (optional)

    try:
        # List the network's active smart networks.
        api_instance.api_v1_smart_networks_get(search=search, filter_id=filter_id, filter_name=filter_name, sort=sort, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_smart_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_name** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] 

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
**200** | Networks. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_smart_networks_id_get**
> api_v1_smart_networks_id_get(id)

One smart network.

`endpoint` and `bid_type` are always empty (kept for shape compatibility). Same handler as the panel.

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
    api_instance = goadserver.MarketDataApi(api_client)
    id = 56 # int | 

    try:
        # One smart network.
        api_instance.api_v1_smart_networks_id_get(id)
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_smart_networks_id_get: %s\n" % e)
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
**200** | Network. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_volumes_filters_get**
> api_v1_volumes_filters_get()

Option lists for the volume query.

Ad types (in the network's own ad type order), device types, connection types (and whether the network filters by them) and the pay types the network has volume rows for. Same handler as the panel.

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
    api_instance = goadserver.MarketDataApi(api_client)

    try:
        # Option lists for the volume query.
        api_instance.api_v1_volumes_filters_get()
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_volumes_filters_get: %s\n" % e)
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
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_volumes_get**
> api_v1_volumes_get(adtypeid, device_typeid, connection_typeid, paytype=paytype)

Available traffic volume per country (traffic estimate).

The network's quoted traffic volume (`volume_data`) for one ad
type × device type × connection type, summed per country, largest
first. Without `paytype` CPC and CPM rows are summed. Same handler
as the panel's Volumes page; 404 when its module is off.


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
    api_instance = goadserver.MarketDataApi(api_client)
    adtypeid = 56 # int | 
    device_typeid = 56 # int | 
    connection_typeid = 56 # int | 
    paytype = 56 # int | 0 CPC, 1 CPM (GET /api/v1/volumes/filters → pay_types). (optional)

    try:
        # Available traffic volume per country (traffic estimate).
        api_instance.api_v1_volumes_get(adtypeid, device_typeid, connection_typeid, paytype=paytype)
    except Exception as e:
        print("Exception when calling MarketDataApi->api_v1_volumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adtypeid** | **int**|  | 
 **device_typeid** | **int**|  | 
 **connection_typeid** | **int**|  | 
 **paytype** | **int**| 0 CPC, 1 CPM (GET /api/v1/volumes/filters → pay_types). | [optional] 

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
**200** | Volume per country. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | paytype is not 0 or 1. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


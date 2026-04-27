# goadserver.FiltersApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_filters_get**](FiltersApi.md#api_v1_filters_get) | **GET** /api/v1/filters | List all filters across types.
[**api_v1_filters_post**](FiltersApi.md#api_v1_filters_post) | **POST** /api/v1/filters | Create a filter and populate it with items.
[**api_v1_filters_type_id_active_patch**](FiltersApi.md#api_v1_filters_type_id_active_patch) | **PATCH** /api/v1/filters/{type}/{id}/active | Activate or deactivate a filter (exclusion types only).
[**api_v1_filters_type_id_delete**](FiltersApi.md#api_v1_filters_type_id_delete) | **DELETE** /api/v1/filters/{type}/{id} | Delete a filter (and its items, for IP pools).
[**api_v1_filters_type_id_get**](FiltersApi.md#api_v1_filters_type_id_get) | **GET** /api/v1/filters/{type}/{id} | Get a single filter with its items.
[**api_v1_filters_type_id_items_item_delete**](FiltersApi.md#api_v1_filters_type_id_items_item_delete) | **DELETE** /api/v1/filters/{type}/{id}/items/{item} | Remove a single item from a filter.
[**api_v1_filters_type_id_items_post**](FiltersApi.md#api_v1_filters_type_id_items_post) | **POST** /api/v1/filters/{type}/{id}/items | Add items to an existing filter.


# **api_v1_filters_get**
> ApiV1FiltersGet200Response api_v1_filters_get(type=type)

List all filters across types.

Each filter has a **type** and may apply globally or to specific
campaigns. Types:

| type          | meaning                          | toggleable |
|---------------|----------------------------------|:----------:|
| `domain_excl` | Block these domains              | yes |
| `domain_incl` | Only allow these domains         | no |
| `adzone_excl` | Block these ad zones             | yes |
| `adzone_incl` | Only allow these ad zones        | no |
| `isp_excl`    | Block these ISPs                 | yes |
| `subid_excl`  | Block these SubIDs               | yes |
| `subid_incl`  | Only allow these SubIDs          | no |
| `ip`          | IP-pool blocking                 | no |


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_get200_response import ApiV1FiltersGet200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | Filter to one type. (optional)

    try:
        # List all filters across types.
        api_response = api_instance.api_v1_filters_get(type=type)
        print("The response of FiltersApi->api_v1_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter to one type. | [optional] 

### Return type

[**ApiV1FiltersGet200Response**](ApiV1FiltersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter list across types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_post**
> FilterDetail api_v1_filters_post(api_v1_filters_post_request)

Create a filter and populate it with items.

For `domain_excl` / `domain_incl`: items can be domain URLs
(`"https://evil.com/x"`) — automatically resolved to internal
domain IDs — or numeric domain IDs as strings.
For `adzone_excl` / `adzone_incl` / `isp_excl`: items must be
numeric IDs.
For `subid_excl` / `subid_incl`: items are raw SubID strings.
IP pool creation is not yet exposed via the public API.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_post_request import ApiV1FiltersPostRequest
from goadserver.models.filter_detail import FilterDetail
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    api_v1_filters_post_request = goadserver.ApiV1FiltersPostRequest() # ApiV1FiltersPostRequest | 

    try:
        # Create a filter and populate it with items.
        api_response = api_instance.api_v1_filters_post(api_v1_filters_post_request)
        print("The response of FiltersApi->api_v1_filters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_filters_post_request** | [**ApiV1FiltersPostRequest**](ApiV1FiltersPostRequest.md)|  | 

### Return type

[**FilterDetail**](FilterDetail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Filter created |  -  |
**422** | Validation error / duplicate name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_active_patch**
> ApiV1FiltersTypeIdActivePatch200Response api_v1_filters_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)

Activate or deactivate a filter (exclusion types only).

Only `*_excl` filters have an active/inactive state. Inclusion
filters and IP pools always apply when a campaign references them
— disable by removing the reference instead.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_filters_type_id_active_patch200_response import ApiV1FiltersTypeIdActivePatch200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Activate or deactivate a filter (exclusion types only).
        api_response = api_instance.api_v1_filters_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of FiltersApi->api_v1_filters_type_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1FiltersTypeIdActivePatch200Response**](ApiV1FiltersTypeIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state |  -  |
**422** | Filter type not toggleable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_delete**
> api_v1_filters_type_id_delete(type, id)

Delete a filter (and its items, for IP pools).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Delete a filter (and its items, for IP pools).
        api_instance.api_v1_filters_type_id_delete(type, id)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_get**
> FilterDetail api_v1_filters_type_id_get(type, id)

Get a single filter with its items.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.filter_detail import FilterDetail
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Get a single filter with its items.
        api_response = api_instance.api_v1_filters_type_id_get(type, id)
        print("The response of FiltersApi->api_v1_filters_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**FilterDetail**](FilterDetail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter details |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_items_item_delete**
> ApiV1FiltersTypeIdItemsItemDelete200Response api_v1_filters_type_id_items_item_delete(type, id, item)

Remove a single item from a filter.

`{item}` is the stored value — domain ID, adzone ID, ISP ID, or SubID string. URL-encode special characters.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_type_id_items_item_delete200_response import ApiV1FiltersTypeIdItemsItemDelete200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    item = 'item_example' # str | 

    try:
        # Remove a single item from a filter.
        api_response = api_instance.api_v1_filters_type_id_items_item_delete(type, id, item)
        print("The response of FiltersApi->api_v1_filters_type_id_items_item_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_items_item_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **item** | **str**|  | 

### Return type

[**ApiV1FiltersTypeIdItemsItemDelete200Response**](ApiV1FiltersTypeIdItemsItemDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removed |  -  |
**404** | Item not present in this filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_items_post**
> ApiV1FiltersTypeIdItemsPost200Response api_v1_filters_type_id_items_post(type, id, api_v1_filters_type_id_items_post_request)

Add items to an existing filter.

Same input format as creating a filter — domain URLs are
auto-resolved to IDs for domain filters, numeric IDs required
for adzone/ISP filters, raw strings for SubID filters.
Already-present items are deduplicated silently.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_type_id_items_post200_response import ApiV1FiltersTypeIdItemsPost200Response
from goadserver.models.api_v1_filters_type_id_items_post_request import ApiV1FiltersTypeIdItemsPostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.FiltersApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_filters_type_id_items_post_request = goadserver.ApiV1FiltersTypeIdItemsPostRequest() # ApiV1FiltersTypeIdItemsPostRequest | 

    try:
        # Add items to an existing filter.
        api_response = api_instance.api_v1_filters_type_id_items_post(type, id, api_v1_filters_type_id_items_post_request)
        print("The response of FiltersApi->api_v1_filters_type_id_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_filters_type_id_items_post_request** | [**ApiV1FiltersTypeIdItemsPostRequest**](ApiV1FiltersTypeIdItemsPostRequest.md)|  | 

### Return type

[**ApiV1FiltersTypeIdItemsPost200Response**](ApiV1FiltersTypeIdItemsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New item set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


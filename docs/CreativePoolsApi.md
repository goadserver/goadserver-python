# goadserver.CreativePoolsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_creative_pools_get**](CreativePoolsApi.md#api_v1_creative_pools_get) | **GET** /api/v1/creative-pools | List creative pools.
[**api_v1_creative_pools_id_clone_post**](CreativePoolsApi.md#api_v1_creative_pools_id_clone_post) | **POST** /api/v1/creative-pools/{id}/clone | Clone a creative pool with all its items.
[**api_v1_creative_pools_id_delete**](CreativePoolsApi.md#api_v1_creative_pools_id_delete) | **DELETE** /api/v1/creative-pools/{id} | Soft-delete a creative pool.
[**api_v1_creative_pools_id_get**](CreativePoolsApi.md#api_v1_creative_pools_id_get) | **GET** /api/v1/creative-pools/{id} | Show a single creative pool.
[**api_v1_creative_pools_id_items_get**](CreativePoolsApi.md#api_v1_creative_pools_id_items_get) | **GET** /api/v1/creative-pools/{id}/items | List items in a creative pool.
[**api_v1_creative_pools_id_items_item_id_delete**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_delete) | **DELETE** /api/v1/creative-pools/{id}/items/{itemId} | Soft-delete a single pool item.
[**api_v1_creative_pools_id_items_item_id_put**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId} | Update a single pool item.
[**api_v1_creative_pools_id_items_item_id_toggle_put**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_toggle_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId}/toggle | Toggle a pool item on / off.
[**api_v1_creative_pools_id_put**](CreativePoolsApi.md#api_v1_creative_pools_id_put) | **PUT** /api/v1/creative-pools/{id} | Update creative pool meta.
[**api_v1_creative_pools_id_used_in_get**](CreativePoolsApi.md#api_v1_creative_pools_id_used_in_get) | **GET** /api/v1/creative-pools/{id}/used-in | List campaigns / ads that reference this pool.
[**api_v1_creative_pools_post**](CreativePoolsApi.md#api_v1_creative_pools_post) | **POST** /api/v1/creative-pools | Create a creative pool.


# **api_v1_creative_pools_get**
> ApiV1CreativePoolsGet200Response api_v1_creative_pools_get(type=type, title=title, page=page, per_page=per_page, sort=sort)

List creative pools.

Returns every creative pool owned by the caller. Each row carries
`items_count` (live items, `is_deleted=0`) and `total_sizes` (count
of distinct banner sizes). Tags are returned both as the raw CSV
string (`tags`) and as an array (`tagids`).

Supports `name`/`title`/`type`/`id` filter params plus the standard
`page`, `per_page`, `sort`, `direction`, `q` search.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_get200_response import ApiV1CreativePoolsGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    type = 'type_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)
    sort = id # str |  (optional) (default to id)

    try:
        # List creative pools.
        api_response = api_instance.api_v1_creative_pools_get(type=type, title=title, page=page, per_page=per_page, sort=sort)
        print("The response of CreativePoolsApi->api_v1_creative_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]
 **sort** | **str**|  | [optional] [default to id]

### Return type

[**ApiV1CreativePoolsGet200Response**](ApiV1CreativePoolsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pools. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_clone_post**
> ApiV1CreativePoolsIdClonePost201Response api_v1_creative_pools_id_clone_post(id)

Clone a creative pool with all its items.

Duplicates the pool row and every live item (`is_deleted=0`).
Cloned items share the same underlying `creative_id`, so the
binary creative file is not re-uploaded — both pools reference
the same row in the `creatives` table. The new pool's title is
suffixed with " (Copy)".


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_clone_post201_response import ApiV1CreativePoolsIdClonePost201Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Clone a creative pool with all its items.
        api_response = api_instance.api_v1_creative_pools_id_clone_post(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdClonePost201Response**](ApiV1CreativePoolsIdClonePost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pool cloned. |  -  |
**404** | Source pool not found. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_delete**
> ApiV1CreativePoolsIdDelete200Response api_v1_creative_pools_id_delete(id)

Soft-delete a creative pool.

Deletes the pool **and** every item that is not currently used by an
ad. If any items are still referenced by live ads the call returns
409 with the per-item count and the pool itself is left intact —
unhook the ads first, then retry.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_delete200_response import ApiV1CreativePoolsIdDelete200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a creative pool.
        api_response = api_instance.api_v1_creative_pools_id_delete(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdDelete200Response**](ApiV1CreativePoolsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pool deleted. |  -  |
**409** | Some items are still in use; pool not deleted. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_get**
> ApiV1CreativePoolsIdGet200Response api_v1_creative_pools_id_get(id)

Show a single creative pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_get200_response import ApiV1CreativePoolsIdGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Show a single creative pool.
        api_response = api_instance.api_v1_creative_pools_id_get(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdGet200Response**](ApiV1CreativePoolsIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pool detail. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_get**
> ApiV1CampaignsTypeCampaignIdAdsGet200Response api_v1_creative_pools_id_items_get(id, page=page, per_page=per_page)

List items in a creative pool.

Returns every banner / video / native item in the pool with size,
creative metadata and lifetime stats (views, clicks, ctr, conv).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response import ApiV1CampaignsTypeCampaignIdAdsGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # List items in a creative pool.
        api_response = api_instance.api_v1_creative_pools_id_items_get(id, page=page, per_page=per_page)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsGet200Response**](ApiV1CampaignsTypeCampaignIdAdsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Items. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_delete**
> api_v1_creative_pools_id_items_item_id_delete(id, item_id)

Soft-delete a single pool item.

Refuses if the item is still referenced by a live ad — unhook
the ad first.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 

    try:
        # Soft-delete a single pool item.
        api_instance.api_v1_creative_pools_id_items_item_id_delete(id, item_id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 

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
**200** | Deleted. |  -  |
**409** | Item still used in a live ad. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_put**
> api_v1_creative_pools_id_items_item_id_put(id, item_id, api_v1_creative_pools_id_items_item_id_put_request)

Update a single pool item.

Editable fields: `title`, `lang`, `properties`, `ratingid`,
`url_prefix`. Active state is toggled via the `/toggle` endpoint
below.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request import ApiV1CreativePoolsIdItemsItemIdPutRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 
    api_v1_creative_pools_id_items_item_id_put_request = goadserver.ApiV1CreativePoolsIdItemsItemIdPutRequest() # ApiV1CreativePoolsIdItemsItemIdPutRequest | 

    try:
        # Update a single pool item.
        api_instance.api_v1_creative_pools_id_items_item_id_put(id, item_id, api_v1_creative_pools_id_items_item_id_put_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 
 **api_v1_creative_pools_id_items_item_id_put_request** | [**ApiV1CreativePoolsIdItemsItemIdPutRequest**](ApiV1CreativePoolsIdItemsItemIdPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_toggle_put**
> api_v1_creative_pools_id_items_item_id_toggle_put(id, item_id)

Toggle a pool item on / off.

Flips `isactive` between 0 and 1. Inactive items are skipped by the
ad-server when picking a creative from the pool.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 

    try:
        # Toggle a pool item on / off.
        api_instance.api_v1_creative_pools_id_items_item_id_toggle_put(id, item_id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 

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
**200** | Toggled. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_put**
> api_v1_creative_pools_id_put(id, api_v1_creative_pools_id_put_request)

Update creative pool meta.

Updates `title`, `sort_type`, `conv_type`, `tags`, or `type`.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_put_request import ApiV1CreativePoolsIdPutRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_put_request = goadserver.ApiV1CreativePoolsIdPutRequest() # ApiV1CreativePoolsIdPutRequest | 

    try:
        # Update creative pool meta.
        api_instance.api_v1_creative_pools_id_put(id, api_v1_creative_pools_id_put_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_put_request** | [**ApiV1CreativePoolsIdPutRequest**](ApiV1CreativePoolsIdPutRequest.md)|  | 

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
**200** | Updated. |  -  |
**404** | Pool not found. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_used_in_get**
> ApiV1CreativePoolsIdUsedInGet200Response api_v1_creative_pools_id_used_in_get(id)

List campaigns / ads that reference this pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_used_in_get200_response import ApiV1CreativePoolsIdUsedInGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # List campaigns / ads that reference this pool.
        api_response = api_instance.api_v1_creative_pools_id_used_in_get(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_used_in_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_used_in_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdUsedInGet200Response**](ApiV1CreativePoolsIdUsedInGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | References. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_creative_pools_post(api_v1_creative_pools_post_request)

Create a creative pool.

Creates an empty pool. Add items via the panel uploader (not yet
exposed via API) or import-by-id endpoints once available. Title
collisions are auto-suffixed with `_<unix>`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_creative_pools_post_request import ApiV1CreativePoolsPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    api_v1_creative_pools_post_request = goadserver.ApiV1CreativePoolsPostRequest() # ApiV1CreativePoolsPostRequest | 

    try:
        # Create a creative pool.
        api_response = api_instance.api_v1_creative_pools_post(api_v1_creative_pools_post_request)
        print("The response of CreativePoolsApi->api_v1_creative_pools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creative_pools_post_request** | [**ApiV1CreativePoolsPostRequest**](ApiV1CreativePoolsPostRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


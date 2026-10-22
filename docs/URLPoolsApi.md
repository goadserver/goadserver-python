# goadserver.URLPoolsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_url_pools_get**](URLPoolsApi.md#api_v1_url_pools_get) | **GET** /api/v1/url-pools | List URL pools.
[**api_v1_url_pools_id_clone_post**](URLPoolsApi.md#api_v1_url_pools_id_clone_post) | **POST** /api/v1/url-pools/{id}/clone | Clone a URL pool with all its URLs.
[**api_v1_url_pools_id_delete**](URLPoolsApi.md#api_v1_url_pools_id_delete) | **DELETE** /api/v1/url-pools/{id} | Soft-delete a URL pool.
[**api_v1_url_pools_id_get**](URLPoolsApi.md#api_v1_url_pools_id_get) | **GET** /api/v1/url-pools/{id} | Show one URL pool.
[**api_v1_url_pools_id_put**](URLPoolsApi.md#api_v1_url_pools_id_put) | **PUT** /api/v1/url-pools/{id} | Update URL pool meta.
[**api_v1_url_pools_id_recover_post**](URLPoolsApi.md#api_v1_url_pools_id_recover_post) | **POST** /api/v1/url-pools/{id}/recover | Restore an archived url pool.
[**api_v1_url_pools_id_urls_get**](URLPoolsApi.md#api_v1_url_pools_id_urls_get) | **GET** /api/v1/url-pools/{id}/urls | List URLs in a pool.
[**api_v1_url_pools_id_urls_post**](URLPoolsApi.md#api_v1_url_pools_id_urls_post) | **POST** /api/v1/url-pools/{id}/urls | Add a URL to a pool.
[**api_v1_url_pools_id_urls_url_id_clone_post**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_clone_post) | **POST** /api/v1/url-pools/{id}/urls/{urlId}/clone | Clone a single URL within the same pool.
[**api_v1_url_pools_id_urls_url_id_delete**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_delete) | **DELETE** /api/v1/url-pools/{id}/urls/{urlId} | Soft-delete a single URL.
[**api_v1_url_pools_id_urls_url_id_get**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_get) | **GET** /api/v1/url-pools/{id}/urls/{urlId} | Show a single URL.
[**api_v1_url_pools_id_urls_url_id_put**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId} | Update a single URL.
[**api_v1_url_pools_id_urls_url_id_toggle_put**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_toggle_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId}/toggle | Toggle a URL on / off.
[**api_v1_url_pools_id_urls_url_id_weight_put**](URLPoolsApi.md#api_v1_url_pools_id_urls_url_id_weight_put) | **PUT** /api/v1/url-pools/{id}/urls/{urlId}/weight | Set a URL&#39;s rotation weight.
[**api_v1_url_pools_id_used_in_get**](URLPoolsApi.md#api_v1_url_pools_id_used_in_get) | **GET** /api/v1/url-pools/{id}/used-in | List campaigns / ads that reference this URL pool.
[**api_v1_url_pools_post**](URLPoolsApi.md#api_v1_url_pools_post) | **POST** /api/v1/url-pools | Create a URL pool.
[**api_v1_url_pools_replace_url_put**](URLPoolsApi.md#api_v1_url_pools_replace_url_put) | **PUT** /api/v1/url-pools/replace-url | Search &amp; replace text across your URL-pool URLs.


# **api_v1_url_pools_get**
> ApiV1CreativesGet200Response api_v1_url_pools_get(select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, filter_id=filter_id, filter_title=filter_title, filter_name=filter_name, state=state, search=search, sort_by=sort_by, sort_dir=sort_dir)

List URL pools.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_get200_response import ApiV1CreativesGet200Response
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
    api_instance = goadserver.URLPoolsApi(api_client)
    select_stats = 'select_stats_example' # str | 1 = add clicks per pool for the from / to window (default the last 7 days). (optional)
    var_from = '2013-10-20' # date | With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. (optional)
    to = '2013-10-20' # date | With select_stats=1: last day of the stats window (YYYY-MM-DD). (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    filter_id = 56 # int |  (optional)
    filter_title = 'filter_title_example' # str | Title contains. (optional)
    filter_name = 'filter_name_example' # str | Same as filter_title. (optional)
    state = live # str | deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list. (optional) (default to live)
    search = 'search_example' # str | Title contains. (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)

    try:
        # List URL pools.
        api_response = api_instance.api_v1_url_pools_get(select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, filter_id=filter_id, filter_title=filter_title, filter_name=filter_name, state=state, search=search, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of URLPoolsApi->api_v1_url_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_stats** | **str**| 1 &#x3D; add clicks per pool for the from / to window (default the last 7 days). | [optional] 
 **var_from** | **date**| With select_stats&#x3D;1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. | [optional] 
 **to** | **date**| With select_stats&#x3D;1: last day of the stats window (YYYY-MM-DD). | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **filter_id** | **int**|  | [optional] 
 **filter_title** | **str**| Title contains. | [optional] 
 **filter_name** | **str**| Same as filter_title. | [optional] 
 **state** | **str**| deleted &#x3D; the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list. | [optional] [default to live]
 **search** | **str**| Title contains. | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]

### Return type

[**ApiV1CreativesGet200Response**](ApiV1CreativesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pools. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_clone_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_url_pools_id_clone_post(id)

Clone a URL pool with all its URLs.

Duplicates the pool row and every URL in it (`isdeleted=0`).
New pool title is suffixed with " (Copy)".


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # Clone a URL pool with all its URLs.
        api_response = api_instance.api_v1_url_pools_id_clone_post(id)
        print("The response of URLPoolsApi->api_v1_url_pools_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_delete**
> api_v1_url_pools_id_delete(id)

Soft-delete a URL pool.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a URL pool.
        api_instance.api_v1_url_pools_id_delete(id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_delete: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_get**
> api_v1_url_pools_id_get(id)

Show one URL pool.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # Show one URL pool.
        api_instance.api_v1_url_pools_id_get(id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_get: %s\n" % e)
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
**200** | Pool detail. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_put**
> api_v1_url_pools_id_put(id, api_v1_url_pools_id_put_request)

Update URL pool meta.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_url_pools_id_put_request import ApiV1UrlPoolsIdPutRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    api_v1_url_pools_id_put_request = goadserver.ApiV1UrlPoolsIdPutRequest() # ApiV1UrlPoolsIdPutRequest | 

    try:
        # Update URL pool meta.
        api_instance.api_v1_url_pools_id_put(id, api_v1_url_pools_id_put_request)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_url_pools_id_put_request** | [**ApiV1UrlPoolsIdPutRequest**](ApiV1UrlPoolsIdPutRequest.md)|  | 

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
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_recover_post**
> api_v1_url_pools_id_recover_post(id)

Restore an archived url pool.

Reverses the soft delete of DELETE /url-pools/{id} (and of Cleanup's
Archive): the pool is listed and usable again. Its URLs were never removed, so they are all there.
404 when the pool does not exist, is not archived, or was purged.


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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # Restore an archived url pool.
        api_instance.api_v1_url_pools_id_recover_post(id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_recover_post: %s\n" % e)
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
**200** | Restored. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found, not archived or purged. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_get**
> api_v1_url_pools_id_urls_get(id, filter_url=filter_url, filter_isactive=filter_isactive, search=search, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page, select_stats=select_stats, var_from=var_from, to=to)

List URLs in a pool.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    filter_url = 'filter_url_example' # str | URL contains. (optional)
    filter_isactive = 56 # int |  (optional)
    search = 'search_example' # str | Matches URL, title or keywords. (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    select_stats = 'select_stats_example' # str | 1 = add stats per URL for the from / to window (default the last 7 days). (optional)
    var_from = '2013-10-20' # date | With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. (optional)
    to = '2013-10-20' # date | With select_stats=1: last day of the stats window (YYYY-MM-DD). (optional)

    try:
        # List URLs in a pool.
        api_instance.api_v1_url_pools_id_urls_get(id, filter_url=filter_url, filter_isactive=filter_isactive, search=search, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page, select_stats=select_stats, var_from=var_from, to=to)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **filter_url** | **str**| URL contains. | [optional] 
 **filter_isactive** | **int**|  | [optional] 
 **search** | **str**| Matches URL, title or keywords. | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **select_stats** | **str**| 1 &#x3D; add stats per URL for the from / to window (default the last 7 days). | [optional] 
 **var_from** | **date**| With select_stats&#x3D;1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. | [optional] 
 **to** | **date**| With select_stats&#x3D;1: last day of the stats window (YYYY-MM-DD). | [optional] 

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
**200** | URLs. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_url_pools_id_urls_post(id, api_v1_url_pools_id_urls_post_request)

Add a URL to a pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_url_pools_id_urls_post_request import ApiV1UrlPoolsIdUrlsPostRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    api_v1_url_pools_id_urls_post_request = goadserver.ApiV1UrlPoolsIdUrlsPostRequest() # ApiV1UrlPoolsIdUrlsPostRequest | 

    try:
        # Add a URL to a pool.
        api_response = api_instance.api_v1_url_pools_id_urls_post(id, api_v1_url_pools_id_urls_post_request)
        print("The response of URLPoolsApi->api_v1_url_pools_id_urls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_url_pools_id_urls_post_request** | [**ApiV1UrlPoolsIdUrlsPostRequest**](ApiV1UrlPoolsIdUrlsPostRequest.md)|  | 

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
**422** | Validation error — title / url, or &#x60;start_at&#x60; / &#x60;end_at&#x60; (bad format, end not after start). |  -  |
**201** | URL added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_clone_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_url_pools_id_urls_url_id_clone_post(id, url_id)

Clone a single URL within the same pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 

    try:
        # Clone a single URL within the same pool.
        api_response = api_instance.api_v1_url_pools_id_urls_url_id_clone_post(id, url_id)
        print("The response of URLPoolsApi->api_v1_url_pools_id_urls_url_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | URL cloned. |  -  |
**404** | URL not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_delete**
> api_v1_url_pools_id_urls_url_id_delete(id, url_id)

Soft-delete a single URL.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 

    try:
        # Soft-delete a single URL.
        api_instance.api_v1_url_pools_id_urls_url_id_delete(id, url_id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 

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
**404** | URL not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_get**
> api_v1_url_pools_id_urls_url_id_get(id, url_id)

Show a single URL.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 

    try:
        # Show a single URL.
        api_instance.api_v1_url_pools_id_urls_url_id_get(id, url_id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 

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
**200** | URL detail. |  -  |
**404** | URL not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_put**
> api_v1_url_pools_id_urls_url_id_put(id, url_id, api_v1_url_pools_id_urls_url_id_put_request)

Update a single URL.

Editable fields — `url`, `title`, `weight`, `properties`, `keywords`,
`is_fallback`, `start_at`, `end_at`.

**Scheduling.** `start_at` / `end_at` make the URL serve only inside
`[start_at, end_at)`. Send unix seconds or an RFC 3339 time with its
offset (`2026-10-20T09:00:00-04:00` = 9:00 AM New York); `null`, `0`
or `""` clears that side. The ad servers pick up an edit within a
minute and then switch on the exact second.

**Backup** (`is_fallback: true`): the URL is used only while no other
URL of the pool is live — mark the regular lander as backup and
schedule the promo lander; the regular one steps aside while the promo
runs and returns when it ends. Keyword targeting then applies within
whichever set is live. Not to be confused with a keyword *fallback*
URL (one without keywords).

A change that would leave a pool still used by campaign ads with no URL
to serve at some moment is refused with 409
`SCHEDULE_LEAVES_POOL_EMPTY` (`gap_at` = first uncovered unix second).
Pausing or deleting a URL runs the same check over the other URLs'
schedules.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_url_pools_id_urls_url_id_put_request import ApiV1UrlPoolsIdUrlsUrlIdPutRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 
    api_v1_url_pools_id_urls_url_id_put_request = {"is_fallback":false,"start_at":"2026-10-20T09:00:00-04:00","end_at":"2026-10-27T09:00:00-04:00"} # ApiV1UrlPoolsIdUrlsUrlIdPutRequest | 

    try:
        # Update a single URL.
        api_instance.api_v1_url_pools_id_urls_url_id_put(id, url_id, api_v1_url_pools_id_urls_url_id_put_request)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 
 **api_v1_url_pools_id_urls_url_id_put_request** | [**ApiV1UrlPoolsIdUrlsUrlIdPutRequest**](ApiV1UrlPoolsIdUrlsUrlIdPutRequest.md)|  | 

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
**404** | URL not found. |  -  |
**409** | &#x60;SCHEDULE_LEAVES_POOL_EMPTY&#x60; — the schedule would leave an in-use pool with no URL to serve. |  -  |
**422** | Validation error on &#x60;url&#x60; / &#x60;title&#x60; / &#x60;start_at&#x60; / &#x60;end_at&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_toggle_put**
> api_v1_url_pools_id_urls_url_id_toggle_put(id, url_id)

Toggle a URL on / off.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 

    try:
        # Toggle a URL on / off.
        api_instance.api_v1_url_pools_id_urls_url_id_toggle_put(id, url_id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 

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
**404** | URL not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_urls_url_id_weight_put**
> api_v1_url_pools_id_urls_url_id_weight_put(id, url_id, api_v1_url_pools_id_urls_url_id_weight_put_request)

Set a URL's rotation weight.

Higher weight = more traffic share when `sort_type=wr`. Has no
effect for `rnd`, `ctr` and `cr` sort modes.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_url_pools_id_urls_url_id_weight_put_request import ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 
    api_v1_url_pools_id_urls_url_id_weight_put_request = goadserver.ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest() # ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest | 

    try:
        # Set a URL's rotation weight.
        api_instance.api_v1_url_pools_id_urls_url_id_weight_put(id, url_id, api_v1_url_pools_id_urls_url_id_weight_put_request)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_url_id_weight_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **url_id** | **int**|  | 
 **api_v1_url_pools_id_urls_url_id_weight_put_request** | [**ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest**](ApiV1UrlPoolsIdUrlsUrlIdWeightPutRequest.md)|  | 

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
**400** | &#x60;invalid_weight&#x60; — not a whole number 0–1000000. |  -  |
**404** | URL not found. |  -  |
**422** | &#x60;weight&#x60; missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_id_used_in_get**
> api_v1_url_pools_id_used_in_get(id)

List campaigns / ads that reference this URL pool.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # List campaigns / ads that reference this URL pool.
        api_instance.api_v1_url_pools_id_used_in_get(id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_used_in_get: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | References. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_url_pools_post(api_v1_url_pools_post_request)

Create a URL pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_url_pools_post_request import ApiV1UrlPoolsPostRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    api_v1_url_pools_post_request = goadserver.ApiV1UrlPoolsPostRequest() # ApiV1UrlPoolsPostRequest | 

    try:
        # Create a URL pool.
        api_response = api_instance.api_v1_url_pools_post(api_v1_url_pools_post_request)
        print("The response of URLPoolsApi->api_v1_url_pools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_url_pools_post_request** | [**ApiV1UrlPoolsPostRequest**](ApiV1UrlPoolsPostRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_url_pools_replace_url_put**
> api_v1_url_pools_replace_url_put(api_v1_url_pools_replace_url_put_request)

Search & replace text across your URL-pool URLs.

Replaces the first occurrence of `search` with `replace` in every
matching URL of your URL pools — e.g. swap a tracker domain or an
offer id. Narrow with `poolids` and/or `urlids`; both empty = every
URL of every pool you own. `dry_run: true` returns the matches
(old → new) without writing — recommended first. Logged to the
account's action log. A key pinned to campaigns is refused (URL
pools feed ads of any campaign). Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_url_pools_replace_url_put_request import ApiV1UrlPoolsReplaceUrlPutRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    api_v1_url_pools_replace_url_put_request = {"search":"old-tracker.com","replace":"new-tracker.com","dry_run":true} # ApiV1UrlPoolsReplaceUrlPutRequest | 

    try:
        # Search & replace text across your URL-pool URLs.
        api_instance.api_v1_url_pools_replace_url_put(api_v1_url_pools_replace_url_put_request)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_replace_url_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_url_pools_replace_url_put_request** | [**ApiV1UrlPoolsReplaceUrlPutRequest**](ApiV1UrlPoolsReplaceUrlPutRequest.md)|  | 

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
**200** | Preview (dry_run) or result. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;search&#x60; missing, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.URLPoolsApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_url_pools_get**](URLPoolsApi.md#api_v1_url_pools_get) | **GET** /api/v1/url-pools | List URL pools.
[**api_v1_url_pools_id_clone_post**](URLPoolsApi.md#api_v1_url_pools_id_clone_post) | **POST** /api/v1/url-pools/{id}/clone | Clone a URL pool with all its URLs.
[**api_v1_url_pools_id_delete**](URLPoolsApi.md#api_v1_url_pools_id_delete) | **DELETE** /api/v1/url-pools/{id} | Soft-delete a URL pool.
[**api_v1_url_pools_id_get**](URLPoolsApi.md#api_v1_url_pools_id_get) | **GET** /api/v1/url-pools/{id} | Show one URL pool.
[**api_v1_url_pools_id_put**](URLPoolsApi.md#api_v1_url_pools_id_put) | **PUT** /api/v1/url-pools/{id} | Update URL pool meta.
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


# **api_v1_url_pools_get**
> ApiV1CampaignsTypeCampaignIdAdsGet200Response api_v1_url_pools_get(page=page, per_page=per_page)

List URL pools.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response import ApiV1CampaignsTypeCampaignIdAdsGet200Response
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
    api_instance = goadserver.URLPoolsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # List URL pools.
        api_response = api_instance.api_v1_url_pools_get(page=page, per_page=per_page)
        print("The response of URLPoolsApi->api_v1_url_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_v1_url_pools_id_urls_get**
> api_v1_url_pools_id_urls_get(id)

List URLs in a pool.

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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 

    try:
        # List URLs in a pool.
        api_instance.api_v1_url_pools_id_urls_get(id)
    except Exception as e:
        print("Exception when calling URLPoolsApi->api_v1_url_pools_id_urls_get: %s\n" % e)
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

Editable fields — `url`, `title`, `weight`, `properties`.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_url_pools_id_urls_url_id_put_request import ApiV1UrlPoolsIdUrlsUrlIdPutRequest
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
    api_instance = goadserver.URLPoolsApi(api_client)
    id = 56 # int | 
    url_id = 56 # int | 
    api_v1_url_pools_id_urls_url_id_put_request = goadserver.ApiV1UrlPoolsIdUrlsUrlIdPutRequest() # ApiV1UrlPoolsIdUrlsUrlIdPutRequest | 

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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**404** | URL not found. |  -  |

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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**404** | URL not found. |  -  |

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


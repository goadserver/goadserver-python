# goadserver.RetargetingApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_retargeting_pixels_get**](RetargetingApi.md#api_v1_retargeting_pixels_get) | **GET** /api/v1/retargeting/pixels | List the caller&#39;s retargeting pixels.
[**api_v1_retargeting_pixels_id_active_patch**](RetargetingApi.md#api_v1_retargeting_pixels_id_active_patch) | **PATCH** /api/v1/retargeting/pixels/{id}/active | Activate or deactivate a retargeting pixel.
[**api_v1_retargeting_pixels_id_delete**](RetargetingApi.md#api_v1_retargeting_pixels_id_delete) | **DELETE** /api/v1/retargeting/pixels/{id} | Soft-delete a retargeting pixel and clear its captured visitors.
[**api_v1_retargeting_pixels_id_get**](RetargetingApi.md#api_v1_retargeting_pixels_id_get) | **GET** /api/v1/retargeting/pixels/{id} | Get one retargeting pixel.
[**api_v1_retargeting_pixels_id_put**](RetargetingApi.md#api_v1_retargeting_pixels_id_put) | **PUT** /api/v1/retargeting/pixels/{id} | Rename a retargeting pixel.
[**api_v1_retargeting_pixels_post**](RetargetingApi.md#api_v1_retargeting_pixels_post) | **POST** /api/v1/retargeting/pixels | Create a retargeting pixel.


# **api_v1_retargeting_pixels_get**
> ApiV1RetargetingPixelsGet200Response api_v1_retargeting_pixels_get()

List the caller's retargeting pixels.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_retargeting_pixels_get200_response import ApiV1RetargetingPixelsGet200Response
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
    api_instance = goadserver.RetargetingApi(api_client)

    try:
        # List the caller's retargeting pixels.
        api_response = api_instance.api_v1_retargeting_pixels_get()
        print("The response of RetargetingApi->api_v1_retargeting_pixels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1RetargetingPixelsGet200Response**](ApiV1RetargetingPixelsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pixel list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_retargeting_pixels_id_active_patch**
> ApiV1RetargetingPixelsIdActivePatch200Response api_v1_retargeting_pixels_id_active_patch(id, api_v1_campaigns_type_id_active_patch_request)

Activate or deactivate a retargeting pixel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_retargeting_pixels_id_active_patch200_response import ApiV1RetargetingPixelsIdActivePatch200Response
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
    api_instance = goadserver.RetargetingApi(api_client)
    id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Activate or deactivate a retargeting pixel.
        api_response = api_instance.api_v1_retargeting_pixels_id_active_patch(id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of RetargetingApi->api_v1_retargeting_pixels_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1RetargetingPixelsIdActivePatch200Response**](ApiV1RetargetingPixelsIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_retargeting_pixels_id_delete**
> api_v1_retargeting_pixels_id_delete(id)

Soft-delete a retargeting pixel and clear its captured visitors.

Sets `isdeleted=1` in MySQL and asynchronously deletes the
pixel's rows from ClickHouse `rt_final`. Captured visitor IDs
are gone — re-creating with the same name will start fresh.


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
    api_instance = goadserver.RetargetingApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a retargeting pixel and clear its captured visitors.
        api_instance.api_v1_retargeting_pixels_id_delete(id)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_id_delete: %s\n" % e)
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
**200** | Deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_retargeting_pixels_id_get**
> RetargetingPixel api_v1_retargeting_pixels_id_get(id)

Get one retargeting pixel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.retargeting_pixel import RetargetingPixel
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
    api_instance = goadserver.RetargetingApi(api_client)
    id = 56 # int | 

    try:
        # Get one retargeting pixel.
        api_response = api_instance.api_v1_retargeting_pixels_id_get(id)
        print("The response of RetargetingApi->api_v1_retargeting_pixels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RetargetingPixel**](RetargetingPixel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pixel |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_retargeting_pixels_id_put**
> api_v1_retargeting_pixels_id_put(id, api_v1_retargeting_pixels_id_put_request)

Rename a retargeting pixel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_retargeting_pixels_id_put_request import ApiV1RetargetingPixelsIdPutRequest
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
    api_instance = goadserver.RetargetingApi(api_client)
    id = 56 # int | 
    api_v1_retargeting_pixels_id_put_request = goadserver.ApiV1RetargetingPixelsIdPutRequest() # ApiV1RetargetingPixelsIdPutRequest | 

    try:
        # Rename a retargeting pixel.
        api_instance.api_v1_retargeting_pixels_id_put(id, api_v1_retargeting_pixels_id_put_request)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_retargeting_pixels_id_put_request** | [**ApiV1RetargetingPixelsIdPutRequest**](ApiV1RetargetingPixelsIdPutRequest.md)|  | 

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
**200** | Updated |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_retargeting_pixels_post**
> RetargetingPixel api_v1_retargeting_pixels_post(api_v1_retargeting_pixels_post_request)

Create a retargeting pixel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_retargeting_pixels_post_request import ApiV1RetargetingPixelsPostRequest
from goadserver.models.retargeting_pixel import RetargetingPixel
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
    api_instance = goadserver.RetargetingApi(api_client)
    api_v1_retargeting_pixels_post_request = goadserver.ApiV1RetargetingPixelsPostRequest() # ApiV1RetargetingPixelsPostRequest | 

    try:
        # Create a retargeting pixel.
        api_response = api_instance.api_v1_retargeting_pixels_post(api_v1_retargeting_pixels_post_request)
        print("The response of RetargetingApi->api_v1_retargeting_pixels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetargetingApi->api_v1_retargeting_pixels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_retargeting_pixels_post_request** | [**ApiV1RetargetingPixelsPostRequest**](ApiV1RetargetingPixelsPostRequest.md)|  | 

### Return type

[**RetargetingPixel**](RetargetingPixel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


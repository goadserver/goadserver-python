# goadserver.TrackingApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracking_conversion_types_get**](TrackingApi.md#api_v1_tracking_conversion_types_get) | **GET** /api/v1/tracking/conversion-types | Available conversion types for the caller&#39;s account.
[**api_v1_tracking_pixels_get**](TrackingApi.md#api_v1_tracking_pixels_get) | **GET** /api/v1/tracking/pixels | List the caller&#39;s conversion-tracking pixels.
[**api_v1_tracking_pixels_id_delete**](TrackingApi.md#api_v1_tracking_pixels_id_delete) | **DELETE** /api/v1/tracking/pixels/{id} | Delete a pixel.
[**api_v1_tracking_pixels_id_get**](TrackingApi.md#api_v1_tracking_pixels_id_get) | **GET** /api/v1/tracking/pixels/{id} | Get one pixel.
[**api_v1_tracking_pixels_id_put**](TrackingApi.md#api_v1_tracking_pixels_id_put) | **PUT** /api/v1/tracking/pixels/{id} | Update a pixel&#39;s name or conversion type.
[**api_v1_tracking_pixels_post**](TrackingApi.md#api_v1_tracking_pixels_post) | **POST** /api/v1/tracking/pixels | Create a new tracking pixel.


# **api_v1_tracking_conversion_types_get**
> ApiV1TrackingConversionTypesGet200Response api_v1_tracking_conversion_types_get()

Available conversion types for the caller's account.

Use to discover valid `conversion_type_id` values for new pixels,
plus the network's ad-domain and the configured tracking variable
name (needed to construct the actual tracking URL).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracking_conversion_types_get200_response import ApiV1TrackingConversionTypesGet200Response
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
    api_instance = goadserver.TrackingApi(api_client)

    try:
        # Available conversion types for the caller's account.
        api_response = api_instance.api_v1_tracking_conversion_types_get()
        print("The response of TrackingApi->api_v1_tracking_conversion_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_conversion_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackingConversionTypesGet200Response**](ApiV1TrackingConversionTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion types + tracking config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracking_pixels_get**
> ApiV1TrackingPixelsGet200Response api_v1_tracking_pixels_get(conversion_type_id=conversion_type_id, name=name, page=page, per_page=per_page)

List the caller's conversion-tracking pixels.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracking_pixels_get200_response import ApiV1TrackingPixelsGet200Response
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
    api_instance = goadserver.TrackingApi(api_client)
    conversion_type_id = 56 # int | Filter by conversion type. (optional)
    name = 'name_example' # str | Substring search on name. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List the caller's conversion-tracking pixels.
        api_response = api_instance.api_v1_tracking_pixels_get(conversion_type_id=conversion_type_id, name=name, page=page, per_page=per_page)
        print("The response of TrackingApi->api_v1_tracking_pixels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_pixels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_type_id** | **int**| Filter by conversion type. | [optional] 
 **name** | **str**| Substring search on name. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ApiV1TrackingPixelsGet200Response**](ApiV1TrackingPixelsGet200Response.md)

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

# **api_v1_tracking_pixels_id_delete**
> api_v1_tracking_pixels_id_delete(id)

Delete a pixel.

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
    api_instance = goadserver.TrackingApi(api_client)
    id = 56 # int | 

    try:
        # Delete a pixel.
        api_instance.api_v1_tracking_pixels_id_delete(id)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_pixels_id_delete: %s\n" % e)
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

# **api_v1_tracking_pixels_id_get**
> TrackingPixel api_v1_tracking_pixels_id_get(id)

Get one pixel.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.tracking_pixel import TrackingPixel
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
    api_instance = goadserver.TrackingApi(api_client)
    id = 56 # int | 

    try:
        # Get one pixel.
        api_response = api_instance.api_v1_tracking_pixels_id_get(id)
        print("The response of TrackingApi->api_v1_tracking_pixels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_pixels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TrackingPixel**](TrackingPixel.md)

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

# **api_v1_tracking_pixels_id_put**
> TrackingPixel api_v1_tracking_pixels_id_put(id, api_v1_tracking_pixels_id_put_request)

Update a pixel's name or conversion type.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracking_pixels_id_put_request import ApiV1TrackingPixelsIdPutRequest
from goadserver.models.tracking_pixel import TrackingPixel
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
    api_instance = goadserver.TrackingApi(api_client)
    id = 56 # int | 
    api_v1_tracking_pixels_id_put_request = goadserver.ApiV1TrackingPixelsIdPutRequest() # ApiV1TrackingPixelsIdPutRequest | 

    try:
        # Update a pixel's name or conversion type.
        api_response = api_instance.api_v1_tracking_pixels_id_put(id, api_v1_tracking_pixels_id_put_request)
        print("The response of TrackingApi->api_v1_tracking_pixels_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_pixels_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_tracking_pixels_id_put_request** | [**ApiV1TrackingPixelsIdPutRequest**](ApiV1TrackingPixelsIdPutRequest.md)|  | 

### Return type

[**TrackingPixel**](TrackingPixel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracking_pixels_post**
> TrackingPixel api_v1_tracking_pixels_post(api_v1_tracking_pixels_post_request)

Create a new tracking pixel.

`pixel_code` is generated server-side (32 random hex chars) and
returned in the response. Use it in the conversion URL the
advertiser embeds on the post-conversion page.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracking_pixels_post_request import ApiV1TrackingPixelsPostRequest
from goadserver.models.tracking_pixel import TrackingPixel
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
    api_instance = goadserver.TrackingApi(api_client)
    api_v1_tracking_pixels_post_request = goadserver.ApiV1TrackingPixelsPostRequest() # ApiV1TrackingPixelsPostRequest | 

    try:
        # Create a new tracking pixel.
        api_response = api_instance.api_v1_tracking_pixels_post(api_v1_tracking_pixels_post_request)
        print("The response of TrackingApi->api_v1_tracking_pixels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->api_v1_tracking_pixels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracking_pixels_post_request** | [**ApiV1TrackingPixelsPostRequest**](ApiV1TrackingPixelsPostRequest.md)|  | 

### Return type

[**TrackingPixel**](TrackingPixel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


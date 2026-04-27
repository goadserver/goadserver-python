# goadserver.PublicApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_public_openapi_json_get**](PublicApi.md#api_public_openapi_json_get) | **GET** /api/public/openapi.json | OpenAPI spec as JSON.
[**api_public_openapi_yaml_get**](PublicApi.md#api_public_openapi_yaml_get) | **GET** /api/public/openapi.yaml | Raw OpenAPI spec (this document).
[**api_public_routes_txt_get**](PublicApi.md#api_public_routes_txt_get) | **GET** /api/public/routes.txt | Flat list of public routes — agent-friendly.


# **api_public_openapi_json_get**
> api_public_openapi_json_get()

OpenAPI spec as JSON.

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)

    try:
        # OpenAPI spec as JSON.
        api_instance.api_public_openapi_json_get()
    except Exception as e:
        print("Exception when calling PublicApi->api_public_openapi_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON spec |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_openapi_yaml_get**
> api_public_openapi_yaml_get()

Raw OpenAPI spec (this document).

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)

    try:
        # Raw OpenAPI spec (this document).
        api_instance.api_public_openapi_yaml_get()
    except Exception as e:
        print("Exception when calling PublicApi->api_public_openapi_yaml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | YAML spec |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_routes_txt_get**
> api_public_routes_txt_get()

Flat list of public routes — agent-friendly.

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)

    try:
        # Flat list of public routes — agent-friendly.
        api_instance.api_public_routes_txt_get()
    except Exception as e:
        print("Exception when calling PublicApi->api_public_routes_txt_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | text/plain METHOD path  scope  description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


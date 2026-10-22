# goadserver.PublicApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_public_demo_get**](PublicApi.md#api_public_demo_get) | **GET** /api/public/demo | The network&#39;s ad format demo pages.
[**api_public_demo_slug_get**](PublicApi.md#api_public_demo_slug_get) | **GET** /api/public/demo/{slug} | One ad format demo page (HTML).
[**api_public_offerwall_id_get**](PublicApi.md#api_public_offerwall_id_get) | **GET** /api/public/offerwall/{id} | Offerwall list of an offer zone.
[**api_public_openapi_json_get**](PublicApi.md#api_public_openapi_json_get) | **GET** /api/public/openapi.json | OpenAPI spec as JSON.
[**api_public_openapi_yaml_get**](PublicApi.md#api_public_openapi_yaml_get) | **GET** /api/public/openapi.yaml | Raw OpenAPI spec (this document).
[**api_public_routes_txt_get**](PublicApi.md#api_public_routes_txt_get) | **GET** /api/public/routes.txt | Flat list of public routes — agent-friendly.


# **api_public_demo_get**
> ApiPublicDemoGet200Response api_public_demo_get()

The network's ad format demo pages.

White-label live demos of the ad formats this network offers, shown in
the panel at /demo (optional per tenant; the admin setting
`panel_settings.options.pages.options.show_demo_pages`, off by
default). Lists only pages with at least one demo whose zone types the
network has active. No authentication; 404 while the setting is off.


### Example


```python
import goadserver
from goadserver.models.api_public_demo_get200_response import ApiPublicDemoGet200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)

    try:
        # The network's ad format demo pages.
        api_response = api_instance.api_public_demo_get()
        print("The response of PublicApi->api_public_demo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->api_public_demo_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiPublicDemoGet200Response**](ApiPublicDemoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The demo pages, in hub order. |  -  |
**404** | Demo pages are switched off for this network. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_demo_slug_get**
> str api_public_demo_slug_get(slug)

One ad format demo page (HTML).

The page itself, under the network's name, cut down to the demos whose
zone types the network offers and renumbered. The panel shows it in an
iframe at /demo/{slug}. Served sandboxed (`Content-Security-Policy:
sandbox allow-scripts allow-popups …`, no `allow-same-origin`), so its
ad scripts get an opaque origin and cannot reach the panel's session.
The demo zones run on a demo account; the advertisers are made up.


### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)
    slug = 'native' # str | 

    try:
        # One ad format demo page (HTML).
        api_response = api_instance.api_public_demo_slug_get(slug)
        print("The response of PublicApi->api_public_demo_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->api_public_demo_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The demo page. |  -  |
**404** | Switched off, unknown page, or none of its formats offered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_offerwall_id_get**
> ApiPublicOfferwallIdGet200Response api_public_offerwall_id_get(id)

Offerwall list of an offer zone.

The offers of an offer zone (adzone type 32, its `offerids`) as goCtrl's
`offerwall` plugin shows them: title, description, thumbnail, the
publisher's payout per conversion (in `currency`) and the countries the
offer converts in (empty = all). No authentication; cached 5 minutes,
CORS open. GET /api/v1/adspaces/{id}/code of an offer zone returns the
offerwall snippet pointing here. The visitor's id rides the offer
click as `subid1`; the publisher's conversion postback gets it back
with `{subid1}`, `{payout}` and `{offerid}`.


### Example


```python
import goadserver
from goadserver.models.api_public_offerwall_id_get200_response import ApiPublicOfferwallIdGet200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.PublicApi(api_client)
    id = 56 # int | 

    try:
        # Offerwall list of an offer zone.
        api_response = api_instance.api_public_offerwall_id_get(id)
        print("The response of PublicApi->api_public_offerwall_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->api_public_offerwall_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiPublicOfferwallIdGet200Response**](ApiPublicOfferwallIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The zone&#39;s offers. |  -  |
**400** | Not an offer zone, or no offers selected. |  -  |
**404** | Unknown zone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_openapi_json_get**
> api_public_openapi_json_get()

OpenAPI spec as JSON.

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
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

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
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

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
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


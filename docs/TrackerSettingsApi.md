# goadserver.TrackerSettingsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_countries_get**](TrackerSettingsApi.md#api_v1_tracker_countries_get) | **GET** /api/v1/tracker/countries | List countries seen in the caller&#39;s traffic.
[**api_v1_tracker_custom_params_get**](TrackerSettingsApi.md#api_v1_tracker_custom_params_get) | **GET** /api/v1/tracker/custom-params | Get the custom-parameter slots.
[**api_v1_tracker_custom_params_put**](TrackerSettingsApi.md#api_v1_tracker_custom_params_put) | **PUT** /api/v1/tracker/custom-params | Name the custom-parameter slots.
[**api_v1_tracker_settings_get**](TrackerSettingsApi.md#api_v1_tracker_settings_get) | **GET** /api/v1/tracker/settings | Tracker settings for this account.
[**api_v1_tracker_source_templates_get**](TrackerSettingsApi.md#api_v1_tracker_source_templates_get) | **GET** /api/v1/tracker/source-templates | List traffic-source templates.
[**api_v1_tracker_tokens_get**](TrackerSettingsApi.md#api_v1_tracker_tokens_get) | **GET** /api/v1/tracker/tokens | List the macro tokens.


# **api_v1_tracker_countries_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_countries_get()

List countries seen in the caller's traffic.

Only the countries this account actually has clicks from, so a filter
dropdown built from it has no dead entries.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)

    try:
        # List countries seen in the caller's traffic.
        api_response = api_instance.api_v1_tracker_countries_get()
        print("The response of TrackerSettingsApi->api_v1_tracker_countries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_countries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_custom_params_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_custom_params_get()

Get the custom-parameter slots.

All 11 passthrough slots (subid plus sid1–sid10), named or not. These are
the names that appear as `sid1`–`sid5` dimensions on the stats endpoints.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)

    try:
        # Get the custom-parameter slots.
        api_response = api_instance.api_v1_tracker_custom_params_get()
        print("The response of TrackerSettingsApi->api_v1_tracker_custom_params_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_custom_params_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_custom_params_put**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_custom_params_put(api_v1_tracker_custom_params_put_request)

Name the custom-parameter slots.

Bulk upsert of the whole grid — send every slot you want to keep.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_custom_params_put_request import ApiV1TrackerCustomParamsPutRequest
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)
    api_v1_tracker_custom_params_put_request = goadserver.ApiV1TrackerCustomParamsPutRequest() # ApiV1TrackerCustomParamsPutRequest | 

    try:
        # Name the custom-parameter slots.
        api_response = api_instance.api_v1_tracker_custom_params_put(api_v1_tracker_custom_params_put_request)
        print("The response of TrackerSettingsApi->api_v1_tracker_custom_params_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_custom_params_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_custom_params_put_request** | [**ApiV1TrackerCustomParamsPutRequest**](ApiV1TrackerCustomParamsPutRequest.md)|  | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_settings_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_settings_get()

Tracker settings for this account.

The tracker-relevant slice of tenant configuration — which sub-modules are
live and what the click pipeline expects.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)

    try:
        # Tracker settings for this account.
        api_response = api_instance.api_v1_tracker_settings_get()
        print("The response of TrackerSettingsApi->api_v1_tracker_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_templates_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_source_templates_get()

List traffic-source templates.

The macro presets a source can be built from — the valid `template_slug`
values.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)

    try:
        # List traffic-source templates.
        api_response = api_instance.api_v1_tracker_source_templates_get()
        print("The response of TrackerSettingsApi->api_v1_tracker_source_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_source_templates_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tokens_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_tokens_get()

List the macro tokens.

The placeholder registry a click URL can carry — `{clickid}`, `{country}`,
`{source_id}` and the rest. The valid values for a link's `tokens`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSettingsApi(api_client)

    try:
        # List the macro tokens.
        api_response = api_instance.api_v1_tracker_tokens_get()
        print("The response of TrackerSettingsApi->api_v1_tracker_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSettingsApi->api_v1_tracker_tokens_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


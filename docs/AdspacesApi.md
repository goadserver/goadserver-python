# goadserver.AdspacesApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_adspaces_get**](AdspacesApi.md#api_v1_adspaces_get) | **GET** /api/v1/adspaces | List ad zones owned by the caller.
[**api_v1_adspaces_id_active_patch**](AdspacesApi.md#api_v1_adspaces_id_active_patch) | **PATCH** /api/v1/adspaces/{id}/active | Activate or deactivate an adspace.
[**api_v1_adspaces_id_get**](AdspacesApi.md#api_v1_adspaces_id_get) | **GET** /api/v1/adspaces/{id} | Get a single adspace.


# **api_v1_adspaces_get**
> ApiV1AdspacesGet200Response api_v1_adspaces_get(site_id=site_id, page=page, per_page=per_page)

List ad zones owned by the caller.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_get200_response import ApiV1AdspacesGet200Response
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
    api_instance = goadserver.AdspacesApi(api_client)
    site_id = 56 # int | Filter to one site. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List ad zones owned by the caller.
        api_response = api_instance.api_v1_adspaces_get(site_id=site_id, page=page, per_page=per_page)
        print("The response of AdspacesApi->api_v1_adspaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Filter to one site. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ApiV1AdspacesGet200Response**](ApiV1AdspacesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adspace list (filtered by resource_filter.site_ids/adzone_ids when set). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_active_patch**
> ApiV1CampaignsTypeIdActivePatch200Response api_v1_adspaces_id_active_patch(id, api_v1_campaigns_type_id_active_patch_request)

Activate or deactivate an adspace.

Idempotent. `active=true` activates, `active=false` deactivates.
This is the endpoint behind the **"On / off only"** key preset
for publishers. Honors `resource_filter.adzone_ids` for per-key
scoping to specific zones.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
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
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Activate or deactivate an adspace.
        api_response = api_instance.api_v1_adspaces_id_active_patch(id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of AdspacesApi->api_v1_adspaces_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdActivePatch200Response**](ApiV1CampaignsTypeIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_get**
> api_v1_adspaces_id_get(id)

Get a single adspace.

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
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Get a single adspace.
        api_instance.api_v1_adspaces_id_get(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_get: %s\n" % e)
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
**200** | Adspace |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


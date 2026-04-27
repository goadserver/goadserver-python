# goadserver.SitesApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_sites_get**](SitesApi.md#api_v1_sites_get) | **GET** /api/v1/sites | List the caller&#39;s websites.


# **api_v1_sites_get**
> ApiV1SitesGet200Response api_v1_sites_get()

List the caller's websites.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_sites_get200_response import ApiV1SitesGet200Response
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
    api_instance = goadserver.SitesApi(api_client)

    try:
        # List the caller's websites.
        api_response = api_instance.api_v1_sites_get()
        print("The response of SitesApi->api_v1_sites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1SitesGet200Response**](ApiV1SitesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site list (filtered by &#x60;resource_filter.site_ids&#x60; when set). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


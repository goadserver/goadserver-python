# goadserver.AccountApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_account_get**](AccountApi.md#api_v1_account_get) | **GET** /api/v1/account | Identity check — returns the authenticated user + scopes of the calling key.


# **api_v1_account_get**
> ApiV1AccountGet200Response api_v1_account_get()

Identity check — returns the authenticated user + scopes of the calling key.

Minimal identity payload. Use this to verify a key is alive,
discover which user it belongs to, and inspect what scopes the key
was granted. No PII beyond name/email/company.

Key management (create/list/revoke) is **not** exposed via the
public API — it requires a browser session. Visit MyAccount →
API access in the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_get200_response import ApiV1AccountGet200Response
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
    api_instance = goadserver.AccountApi(api_client)

    try:
        # Identity check — returns the authenticated user + scopes of the calling key.
        api_response = api_instance.api_v1_account_get()
        print("The response of AccountApi->api_v1_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_v1_account_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1AccountGet200Response**](ApiV1AccountGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user identity (and key context if authenticated by API key) |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


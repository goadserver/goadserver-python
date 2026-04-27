# goadserver.FundsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_funds_get**](FundsApi.md#api_v1_funds_get) | **GET** /api/v1/funds | Current advertiser balance + pending deposits.


# **api_v1_funds_get**
> ApiV1FundsGet200Response api_v1_funds_get()

Current advertiser balance + pending deposits.

Use this before deciding to launch or pause a campaign — `low_balance`
is true when current balance is below the user-configured minimum.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_get200_response import ApiV1FundsGet200Response
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
    api_instance = goadserver.FundsApi(api_client)

    try:
        # Current advertiser balance + pending deposits.
        api_response = api_instance.api_v1_funds_get()
        print("The response of FundsApi->api_v1_funds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1FundsGet200Response**](ApiV1FundsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance snapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.OffersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_offers_get**](OffersApi.md#api_v1_offers_get) | **GET** /api/v1/offers | List available offers.


# **api_v1_offers_get**
> ApiV1OffersGet200Response api_v1_offers_get(main_catid=main_catid, catids=catids)

List available offers.

Returns the offer catalog visible to the authenticated publisher —
offer-type campaigns the publisher is whitelisted for (and not
blacklisted from), with the payout computed for this publisher.
Documented in audit_20260723_1117 (was implemented but unspecified).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_offers_get200_response import ApiV1OffersGet200Response
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
    api_instance = goadserver.OffersApi(api_client)
    main_catid = 56 # int | Filter by main category id. (optional)
    catids = 'catids_example' # str | Comma-separated sub-category ids. (optional)

    try:
        # List available offers.
        api_response = api_instance.api_v1_offers_get(main_catid=main_catid, catids=catids)
        print("The response of OffersApi->api_v1_offers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->api_v1_offers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_catid** | **int**| Filter by main category id. | [optional] 
 **catids** | **str**| Comma-separated sub-category ids. | [optional] 

### Return type

[**ApiV1OffersGet200Response**](ApiV1OffersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer list |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


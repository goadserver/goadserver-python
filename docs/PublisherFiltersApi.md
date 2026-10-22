# goadserver.PublisherFiltersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_filters_get**](PublisherFiltersApi.md#api_v1_publisher_filters_get) | **GET** /api/v1/publisher/filters | List the publisher&#39;s URL block list.
[**api_v1_publisher_filters_urls_delete**](PublisherFiltersApi.md#api_v1_publisher_filters_urls_delete) | **DELETE** /api/v1/publisher/filters/urls | Remove one or more URLs from the block list.
[**api_v1_publisher_filters_urls_post**](PublisherFiltersApi.md#api_v1_publisher_filters_urls_post) | **POST** /api/v1/publisher/filters/urls | Add one or more URLs to the block list.


# **api_v1_publisher_filters_get**
> ApiV1PublisherFiltersGet200Response api_v1_publisher_filters_get()

List the publisher's URL block list.

**URLs** — global block list applied to every adspace this
publisher owns. Stored as a CSV in `usersettings.excldomains`.
Returned as a flat array of `{url, type}` entries.

**`categories` is deprecated and always empty.** Category filters
were retired, along with the four `/filters/categories` endpoints
that managed them. The key is still returned so existing callers
keep parsing the response unchanged; do not build against it.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_filters_get200_response import ApiV1PublisherFiltersGet200Response
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
    api_instance = goadserver.PublisherFiltersApi(api_client)

    try:
        # List the publisher's URL block list.
        api_response = api_instance.api_v1_publisher_filters_get()
        print("The response of PublisherFiltersApi->api_v1_publisher_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublisherFiltersApi->api_v1_publisher_filters_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherFiltersGet200Response**](ApiV1PublisherFiltersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Both filter flavors. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_filters_urls_delete**
> ApiV1PublisherFiltersUrlsDelete200Response api_v1_publisher_filters_urls_delete(api_v1_publisher_filters_urls_delete_request)

Remove one or more URLs from the block list.

Body accepts `url` (single) or `urls` (array). Matching is
case-insensitive. Unknown URLs are silently ignored.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_filters_urls_delete200_response import ApiV1PublisherFiltersUrlsDelete200Response
from goadserver.models.api_v1_publisher_filters_urls_delete_request import ApiV1PublisherFiltersUrlsDeleteRequest
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
    api_instance = goadserver.PublisherFiltersApi(api_client)
    api_v1_publisher_filters_urls_delete_request = goadserver.ApiV1PublisherFiltersUrlsDeleteRequest() # ApiV1PublisherFiltersUrlsDeleteRequest | 

    try:
        # Remove one or more URLs from the block list.
        api_response = api_instance.api_v1_publisher_filters_urls_delete(api_v1_publisher_filters_urls_delete_request)
        print("The response of PublisherFiltersApi->api_v1_publisher_filters_urls_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublisherFiltersApi->api_v1_publisher_filters_urls_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_filters_urls_delete_request** | [**ApiV1PublisherFiltersUrlsDeleteRequest**](ApiV1PublisherFiltersUrlsDeleteRequest.md)|  | 

### Return type

[**ApiV1PublisherFiltersUrlsDelete200Response**](ApiV1PublisherFiltersUrlsDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. Body has the slice that was actually removed and the new total. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_filters_urls_post**
> ApiV1PublisherFiltersUrlsPost201Response api_v1_publisher_filters_urls_post(api_v1_publisher_filters_urls_post_request)

Add one or more URLs to the block list.

Adds URLs to `usersettings.excldomains` (deduped). Body accepts
either `url` (single) or `urls` (array). Existing entries stay.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_filters_urls_post201_response import ApiV1PublisherFiltersUrlsPost201Response
from goadserver.models.api_v1_publisher_filters_urls_post_request import ApiV1PublisherFiltersUrlsPostRequest
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
    api_instance = goadserver.PublisherFiltersApi(api_client)
    api_v1_publisher_filters_urls_post_request = goadserver.ApiV1PublisherFiltersUrlsPostRequest() # ApiV1PublisherFiltersUrlsPostRequest | 

    try:
        # Add one or more URLs to the block list.
        api_response = api_instance.api_v1_publisher_filters_urls_post(api_v1_publisher_filters_urls_post_request)
        print("The response of PublisherFiltersApi->api_v1_publisher_filters_urls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublisherFiltersApi->api_v1_publisher_filters_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_filters_urls_post_request** | [**ApiV1PublisherFiltersUrlsPostRequest**](ApiV1PublisherFiltersUrlsPostRequest.md)|  | 

### Return type

[**ApiV1PublisherFiltersUrlsPost201Response**](ApiV1PublisherFiltersUrlsPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated. Body has the slice that was newly added and the new total. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**409** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


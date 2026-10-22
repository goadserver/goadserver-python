# goadserver.TrackerOffersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_offers_bulk_post**](TrackerOffersApi.md#api_v1_tracker_offers_bulk_post) | **POST** /api/v1/tracker/offers/bulk | Pause, activate or delete many offers.
[**api_v1_tracker_offers_get**](TrackerOffersApi.md#api_v1_tracker_offers_get) | **GET** /api/v1/tracker/offers | List tracker offers.
[**api_v1_tracker_offers_id_delete**](TrackerOffersApi.md#api_v1_tracker_offers_id_delete) | **DELETE** /api/v1/tracker/offers/{id} | Delete an offer.
[**api_v1_tracker_offers_id_get**](TrackerOffersApi.md#api_v1_tracker_offers_id_get) | **GET** /api/v1/tracker/offers/{id} | Get one offer.
[**api_v1_tracker_offers_id_put**](TrackerOffersApi.md#api_v1_tracker_offers_id_put) | **PUT** /api/v1/tracker/offers/{id} | Update an offer.
[**api_v1_tracker_offers_id_urls_post**](TrackerOffersApi.md#api_v1_tracker_offers_id_urls_post) | **POST** /api/v1/tracker/offers/{id}/urls | Add a landing URL to an offer.
[**api_v1_tracker_offers_id_urls_url_id_delete**](TrackerOffersApi.md#api_v1_tracker_offers_id_urls_url_id_delete) | **DELETE** /api/v1/tracker/offers/{id}/urls/{urlId} | Delete one landing URL.
[**api_v1_tracker_offers_id_urls_url_id_put**](TrackerOffersApi.md#api_v1_tracker_offers_id_urls_url_id_put) | **PUT** /api/v1/tracker/offers/{id}/urls/{urlId} | Update one landing URL.
[**api_v1_tracker_offers_post**](TrackerOffersApi.md#api_v1_tracker_offers_post) | **POST** /api/v1/tracker/offers | Create an offer.


# **api_v1_tracker_offers_bulk_post**
> ApiV1PublisherPushSubscribersActionPost200Response api_v1_tracker_offers_bulk_post(api_v1_tracker_offers_bulk_post_request)

Pause, activate or delete many offers.

One action across a list of offer ids the caller owns. Ids that are not
the caller's are skipped rather than failing the batch.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_subscribers_action_post200_response import ApiV1PublisherPushSubscribersActionPost200Response
from goadserver.models.api_v1_tracker_offers_bulk_post_request import ApiV1TrackerOffersBulkPostRequest
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    api_v1_tracker_offers_bulk_post_request = goadserver.ApiV1TrackerOffersBulkPostRequest() # ApiV1TrackerOffersBulkPostRequest | 

    try:
        # Pause, activate or delete many offers.
        api_response = api_instance.api_v1_tracker_offers_bulk_post(api_v1_tracker_offers_bulk_post_request)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_offers_bulk_post_request** | [**ApiV1TrackerOffersBulkPostRequest**](ApiV1TrackerOffersBulkPostRequest.md)|  | 

### Return type

[**ApiV1PublisherPushSubscribersActionPost200Response**](ApiV1PublisherPushSubscribersActionPost200Response.md)

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

# **api_v1_tracker_offers_get**
> ApiV1TrackerOffersGet200Response api_v1_tracker_offers_get()

List tracker offers.

Every offer the caller owns. An offer is a `roncampaigns` row with
`adtypeid=21` — the same row the click pipeline, conversion settlement
and stats already key off, so an offer created here is immediately
servable through a tracking link.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_offers_get200_response import ApiV1TrackerOffersGet200Response
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
    api_instance = goadserver.TrackerOffersApi(api_client)

    try:
        # List tracker offers.
        api_response = api_instance.api_v1_tracker_offers_get()
        print("The response of TrackerOffersApi->api_v1_tracker_offers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerOffersGet200Response**](ApiV1TrackerOffersGet200Response.md)

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

# **api_v1_tracker_offers_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_offers_id_delete(id)

Delete an offer.

Soft delete (`isdeleted=1`). Clicks, conversions and stats history stay
intact and keep reporting under the offer's name.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.

    try:
        # Delete an offer.
        api_response = api_instance.api_v1_tracker_offers_id_delete(id)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 

### Return type

[**ApiV1PublisherPushCampaignsIdDelete200Response**](ApiV1PublisherPushCampaignsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Offer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_offers_id_get**
> ApiV1TrackerOffersIdGet200Response api_v1_tracker_offers_id_get(id)

Get one offer.

The full offer including its landing URLs and targeting.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_offers_id_get200_response import ApiV1TrackerOffersIdGet200Response
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.

    try:
        # Get one offer.
        api_response = api_instance.api_v1_tracker_offers_id_get(id)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 

### Return type

[**ApiV1TrackerOffersIdGet200Response**](ApiV1TrackerOffersIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Offer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_offers_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_offers_id_put(id, api_v1_tracker_offers_id_put_request)

Update an offer.

Partial update — only the fields present in the body are written, so a
caller that knows about one field cannot blank the rest.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_offers_id_put_request import ApiV1TrackerOffersIdPutRequest
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.
    api_v1_tracker_offers_id_put_request = goadserver.ApiV1TrackerOffersIdPutRequest() # ApiV1TrackerOffersIdPutRequest | 

    try:
        # Update an offer.
        api_response = api_instance.api_v1_tracker_offers_id_put(id, api_v1_tracker_offers_id_put_request)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 
 **api_v1_tracker_offers_id_put_request** | [**ApiV1TrackerOffersIdPutRequest**](ApiV1TrackerOffersIdPutRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Offer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_offers_id_urls_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_offers_id_urls_post(id, api_v1_tracker_offers_id_urls_post_request)

Add a landing URL to an offer.

Adds one rotator URL without round-tripping the whole offer.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_offers_id_urls_post_request import ApiV1TrackerOffersIdUrlsPostRequest
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.
    api_v1_tracker_offers_id_urls_post_request = goadserver.ApiV1TrackerOffersIdUrlsPostRequest() # ApiV1TrackerOffersIdUrlsPostRequest | 

    try:
        # Add a landing URL to an offer.
        api_response = api_instance.api_v1_tracker_offers_id_urls_post(id, api_v1_tracker_offers_id_urls_post_request)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_urls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 
 **api_v1_tracker_offers_id_urls_post_request** | [**ApiV1TrackerOffersIdUrlsPostRequest**](ApiV1TrackerOffersIdUrlsPostRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

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

# **api_v1_tracker_offers_id_urls_url_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_offers_id_urls_url_id_delete(id, url_id)

Delete one landing URL.

Soft delete, so the URL's click and conversion history survives.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.
    url_id = 56 # int | URL row ID.

    try:
        # Delete one landing URL.
        api_response = api_instance.api_v1_tracker_offers_id_urls_url_id_delete(id, url_id)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_urls_url_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_urls_url_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 
 **url_id** | **int**| URL row ID. | 

### Return type

[**ApiV1PublisherPushCampaignsIdDelete200Response**](ApiV1PublisherPushCampaignsIdDelete200Response.md)

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

# **api_v1_tracker_offers_id_urls_url_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_offers_id_urls_url_id_put(id, url_id, api_v1_tracker_offers_id_urls_url_id_put_request)

Update one landing URL.

Writes only the columns the payload carries, so saving one row cannot
clobber fields another editor changed.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_offers_id_urls_url_id_put_request import ApiV1TrackerOffersIdUrlsUrlIdPutRequest
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    id = 56 # int | Offer ID.
    url_id = 56 # int | URL row ID.
    api_v1_tracker_offers_id_urls_url_id_put_request = goadserver.ApiV1TrackerOffersIdUrlsUrlIdPutRequest() # ApiV1TrackerOffersIdUrlsUrlIdPutRequest | 

    try:
        # Update one landing URL.
        api_response = api_instance.api_v1_tracker_offers_id_urls_url_id_put(id, url_id, api_v1_tracker_offers_id_urls_url_id_put_request)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_id_urls_url_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_id_urls_url_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Offer ID. | 
 **url_id** | **int**| URL row ID. | 
 **api_v1_tracker_offers_id_urls_url_id_put_request** | [**ApiV1TrackerOffersIdUrlsUrlIdPutRequest**](ApiV1TrackerOffersIdUrlsUrlIdPutRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

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

# **api_v1_tracker_offers_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_offers_post(api_v1_tracker_offers_post_request)

Create an offer.

Creates the offer and its first landing URL in one call. Give either
`destination_url` for a single URL or `urls` for a weighted rotator.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_offers_post_request import ApiV1TrackerOffersPostRequest
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
    api_instance = goadserver.TrackerOffersApi(api_client)
    api_v1_tracker_offers_post_request = goadserver.ApiV1TrackerOffersPostRequest() # ApiV1TrackerOffersPostRequest | 

    try:
        # Create an offer.
        api_response = api_instance.api_v1_tracker_offers_post(api_v1_tracker_offers_post_request)
        print("The response of TrackerOffersApi->api_v1_tracker_offers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerOffersApi->api_v1_tracker_offers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_offers_post_request** | [**ApiV1TrackerOffersPostRequest**](ApiV1TrackerOffersPostRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error — a required field is missing or a targeting id is unknown. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


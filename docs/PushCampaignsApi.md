# goadserver.PushCampaignsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_push_campaigns_get**](PushCampaignsApi.md#api_v1_publisher_push_campaigns_get) | **GET** /api/v1/publisher/push-campaigns | List the caller&#39;s push campaigns.
[**api_v1_publisher_push_campaigns_id_delete**](PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_delete) | **DELETE** /api/v1/publisher/push-campaigns/{id} | Delete a push campaign.
[**api_v1_publisher_push_campaigns_id_put**](PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_put) | **PUT** /api/v1/publisher/push-campaigns/{id} | Update a push campaign&#39;s notification content.
[**api_v1_publisher_push_campaigns_id_send_post**](PushCampaignsApi.md#api_v1_publisher_push_campaigns_id_send_post) | **POST** /api/v1/publisher/push-campaigns/{id}/send | Queue a push campaign for delivery.
[**api_v1_publisher_push_campaigns_post**](PushCampaignsApi.md#api_v1_publisher_push_campaigns_post) | **POST** /api/v1/publisher/push-campaigns | Create a push campaign.


# **api_v1_publisher_push_campaigns_get**
> ApiV1PublisherPushCampaignsGet200Response api_v1_publisher_push_campaigns_get()

List the caller's push campaigns.

Returns the most recent 200 push campaigns owned by the caller,
newest first, with their delivery counts.

Web-push is a publisher capability, so all push endpoints live under
`/api/v1/publisher/push-*`. The former `/api/v1/tracker/push-*` paths
remain mounted as **deprecated aliases** (same handlers, same scopes)
for back-compat — prefer the `publisher` prefix in new integrations.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_get200_response import ApiV1PublisherPushCampaignsGet200Response
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
    api_instance = goadserver.PushCampaignsApi(api_client)

    try:
        # List the caller's push campaigns.
        api_response = api_instance.api_v1_publisher_push_campaigns_get()
        print("The response of PushCampaignsApi->api_v1_publisher_push_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushCampaignsApi->api_v1_publisher_push_campaigns_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherPushCampaignsGet200Response**](ApiV1PublisherPushCampaignsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_campaigns_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_publisher_push_campaigns_id_delete(id)

Delete a push campaign.

Deletes the campaign. A campaign currently `sending` cannot be
deleted (it would vanish under the sender) and returns 404.


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
    api_instance = goadserver.PushCampaignsApi(api_client)
    id = 56 # int | Campaign ID.

    try:
        # Delete a push campaign.
        api_response = api_instance.api_v1_publisher_push_campaigns_id_delete(id)
        print("The response of PushCampaignsApi->api_v1_publisher_push_campaigns_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushCampaignsApi->api_v1_publisher_push_campaigns_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Campaign ID. | 

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
**200** | Deleted |  -  |
**404** | Campaign not found, or it is currently sending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_campaigns_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_campaigns_id_put(id, api_v1_publisher_push_campaigns_post_request)

Update a push campaign's notification content.

Replaces the notification fields. Counters, status, audience and
timestamps belong to the sender and are not writable here. Only a
campaign at rest (`draft`, `sent`, `failed`) is editable — one
that is `queued` or `sending` returns 409.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_campaigns_post_request import ApiV1PublisherPushCampaignsPostRequest
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
    api_instance = goadserver.PushCampaignsApi(api_client)
    id = 56 # int | Campaign ID.
    api_v1_publisher_push_campaigns_post_request = goadserver.ApiV1PublisherPushCampaignsPostRequest() # ApiV1PublisherPushCampaignsPostRequest | 

    try:
        # Update a push campaign's notification content.
        api_response = api_instance.api_v1_publisher_push_campaigns_id_put(id, api_v1_publisher_push_campaigns_post_request)
        print("The response of PushCampaignsApi->api_v1_publisher_push_campaigns_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushCampaignsApi->api_v1_publisher_push_campaigns_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Campaign ID. | 
 **api_v1_publisher_push_campaigns_post_request** | [**ApiV1PublisherPushCampaignsPostRequest**](ApiV1PublisherPushCampaignsPostRequest.md)|  | 

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
**200** | Updated |  -  |
**400** | Validation error — invalid_id, title_required. |  -  |
**409** | not_editable — campaign not found, or currently queued / sending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_campaigns_id_send_post**
> ApiV1PublisherPushCampaignsIdSendPost200Response api_v1_publisher_push_campaigns_id_send_post(id)

Queue a push campaign for delivery.

Flips the campaign to `queued`; the push sender picks it up
within ~60s and delivers it to every active web-push subscriber
of the network. Only campaigns at rest (`draft`, `sent`,
`failed`) can be queued — a campaign already `queued` or
`sending` returns 409.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_send_post200_response import ApiV1PublisherPushCampaignsIdSendPost200Response
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
    api_instance = goadserver.PushCampaignsApi(api_client)
    id = 56 # int | Campaign ID.

    try:
        # Queue a push campaign for delivery.
        api_response = api_instance.api_v1_publisher_push_campaigns_id_send_post(id)
        print("The response of PushCampaignsApi->api_v1_publisher_push_campaigns_id_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushCampaignsApi->api_v1_publisher_push_campaigns_id_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Campaign ID. | 

### Return type

[**ApiV1PublisherPushCampaignsIdSendPost200Response**](ApiV1PublisherPushCampaignsIdSendPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Queued |  -  |
**409** | Not sendable — campaign not found, or already queued / sending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_campaigns_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_campaigns_post(api_v1_publisher_push_campaigns_post_request)

Create a push campaign.

Creates the campaign in `draft` status — it is not delivered
until you queue it with `POST /api/v1/publisher/push-campaigns/{id}/send`.
Only `title` is required.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_campaigns_post_request import ApiV1PublisherPushCampaignsPostRequest
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
    api_instance = goadserver.PushCampaignsApi(api_client)
    api_v1_publisher_push_campaigns_post_request = goadserver.ApiV1PublisherPushCampaignsPostRequest() # ApiV1PublisherPushCampaignsPostRequest | 

    try:
        # Create a push campaign.
        api_response = api_instance.api_v1_publisher_push_campaigns_post(api_v1_publisher_push_campaigns_post_request)
        print("The response of PushCampaignsApi->api_v1_publisher_push_campaigns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushCampaignsApi->api_v1_publisher_push_campaigns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_push_campaigns_post_request** | [**ApiV1PublisherPushCampaignsPostRequest**](ApiV1PublisherPushCampaignsPostRequest.md)|  | 

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
**200** | Created — returns the new campaign id. |  -  |
**400** | Validation error — title_required. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.WebhooksEventsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_events_get**](WebhooksEventsApi.md#api_v1_events_get) | **GET** /api/v1/events | Read the account&#39;s event feed.
[**api_v1_webhooks_get**](WebhooksEventsApi.md#api_v1_webhooks_get) | **GET** /api/v1/webhooks | List webhooks.
[**api_v1_webhooks_id_delete**](WebhooksEventsApi.md#api_v1_webhooks_id_delete) | **DELETE** /api/v1/webhooks/{id} | Remove a webhook.
[**api_v1_webhooks_id_deliveries_delivery_redeliver_post**](WebhooksEventsApi.md#api_v1_webhooks_id_deliveries_delivery_redeliver_post) | **POST** /api/v1/webhooks/{id}/deliveries/{delivery}/redeliver | Send a delivery again.
[**api_v1_webhooks_id_deliveries_get**](WebhooksEventsApi.md#api_v1_webhooks_id_deliveries_get) | **GET** /api/v1/webhooks/{id}/deliveries | List a webhook&#39;s deliveries.
[**api_v1_webhooks_id_get**](WebhooksEventsApi.md#api_v1_webhooks_id_get) | **GET** /api/v1/webhooks/{id} | Get one webhook.
[**api_v1_webhooks_id_patch**](WebhooksEventsApi.md#api_v1_webhooks_id_patch) | **PATCH** /api/v1/webhooks/{id} | Edit, pause or resume a webhook.
[**api_v1_webhooks_id_rotate_secret_post**](WebhooksEventsApi.md#api_v1_webhooks_id_rotate_secret_post) | **POST** /api/v1/webhooks/{id}/rotate-secret | Issue a new signing secret.
[**api_v1_webhooks_id_test_post**](WebhooksEventsApi.md#api_v1_webhooks_id_test_post) | **POST** /api/v1/webhooks/{id}/test | Send a test ping.
[**api_v1_webhooks_post**](WebhooksEventsApi.md#api_v1_webhooks_post) | **POST** /api/v1/webhooks | Create a webhook.


# **api_v1_events_get**
> ApiV1EventsGet200Response api_v1_events_get(since=since, types=types, limit=limit)

Read the account's event feed.

The same events the webhooks carry, for agents that cannot receive
webhooks. Oldest first, kept **7 days**. Page with the cursor: pass
`next_cursor` from one answer as `since` in the next; `has_more`
says whether to call again at once. `since=now` returns no events,
only the current cursor — the way to start following from now.

Only the events this credential may see are returned: each event
needs the scope of what it is about (see the tag description), and a
key pinned to campaigns, ad spaces or sites only sees events about
those (and never the account-wide `conversion.summary`). The cursor
moves past events you may not see, so a reader never stalls.

Events are recorded only for accounts that have a live API key, a
connected app or a webhook. `conversion.received` is never in the
feed (webhook opt-in only).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_events_get200_response import ApiV1EventsGet200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    since = 'since_example' # str | Cursor from `next_cursor`, `now`, or omit for the whole 7 days. (optional)
    types = 'types_example' # str | Comma-separated event types to keep, e.g. `campaign.paused,ad.rejected`. (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Read the account's event feed.
        api_response = api_instance.api_v1_events_get(since=since, types=types, limit=limit)
        print("The response of WebhooksEventsApi->api_v1_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Cursor from &#x60;next_cursor&#x60;, &#x60;now&#x60;, or omit for the whole 7 days. | [optional] 
 **types** | **str**| Comma-separated event types to keep, e.g. &#x60;campaign.paused,ad.rejected&#x60;. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ApiV1EventsGet200Response**](ApiV1EventsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | &#x60;since&#x60; is not a cursor, &#x60;types&#x60; names an unknown event, or &#x60;limit&#x60; is out of range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_get**
> ApiV1WebhooksGet200Response api_v1_webhooks_get()

List webhooks.

An API key or app sees the webhooks **it** created (the panel shows
all of the account's). `available_events` lists the events this
credential may subscribe to; `limit` is the per-account cap (20).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_get200_response import ApiV1WebhooksGet200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)

    try:
        # List webhooks.
        api_response = api_instance.api_v1_webhooks_get()
        print("The response of WebhooksEventsApi->api_v1_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1WebhooksGet200Response**](ApiV1WebhooksGet200Response.md)

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

# **api_v1_webhooks_id_delete**
> ApiV1WebhooksIdDelete200Response api_v1_webhooks_id_delete(id)

Remove a webhook.

Deliveries still waiting for it are dropped and never sent.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 

    try:
        # Remove a webhook.
        api_response = api_instance.api_v1_webhooks_id_delete(id)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_deliveries_delivery_redeliver_post**
> ApiV1WebhooksIdDelete200Response api_v1_webhooks_id_deliveries_delivery_redeliver_post(id, delivery)

Send a delivery again.

Delivered, failed or waiting — it is queued again with its original
event id. The content comes from the 7-day event feed when the
delivery itself no longer holds it (410 after that).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_delete200_response import ApiV1WebhooksIdDelete200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 
    delivery = 56 # int | 

    try:
        # Send a delivery again.
        api_response = api_instance.api_v1_webhooks_id_deliveries_delivery_redeliver_post(id, delivery)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_deliveries_delivery_redeliver_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_deliveries_delivery_redeliver_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delivery** | **int**|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Queued. |  -  |
**404** | No such delivery on this webhook. |  -  |
**409** | It is being sent right now. |  -  |
**410** | &#x60;delivery_expired&#x60; — older than 7 days. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_deliveries_get**
> ApiV1WebhooksIdDeliveriesGet200Response api_v1_webhooks_id_deliveries_get(id, status=status, limit=limit)

List a webhook's deliveries.

The last 30 days, newest first.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_deliveries_get200_response import ApiV1WebhooksIdDeliveriesGet200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List a webhook's deliveries.
        api_response = api_instance.api_v1_webhooks_id_deliveries_get(id, status=status, limit=limit)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_deliveries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_deliveries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**ApiV1WebhooksIdDeliveriesGet200Response**](ApiV1WebhooksIdDeliveriesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |
**422** | Unknown status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_get**
> ApiV1WebhooksPost201Response api_v1_webhooks_id_get(id)

Get one webhook.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_post201_response import ApiV1WebhooksPost201Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 

    try:
        # Get one webhook.
        api_response = api_instance.api_v1_webhooks_id_get(id)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1WebhooksPost201Response**](ApiV1WebhooksPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_patch**
> ApiV1WebhooksPost201Response api_v1_webhooks_id_patch(id, api_v1_webhooks_id_patch_request)

Edit, pause or resume a webhook.

Omitted fields keep their value; the result is validated like a
create. `status: paused` stops new events (read them from
`/api/v1/events` meanwhile — kept 7 days) and holds what was already
queued; `active` resumes and sends what was held. An event taken off
the webhook drops its waiting deliveries. The secret stays.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_patch_request import ApiV1WebhooksIdPatchRequest
from goadserver.models.api_v1_webhooks_post201_response import ApiV1WebhooksPost201Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 
    api_v1_webhooks_id_patch_request = goadserver.ApiV1WebhooksIdPatchRequest() # ApiV1WebhooksIdPatchRequest | 

    try:
        # Edit, pause or resume a webhook.
        api_response = api_instance.api_v1_webhooks_id_patch(id, api_v1_webhooks_id_patch_request)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_webhooks_id_patch_request** | [**ApiV1WebhooksIdPatchRequest**](ApiV1WebhooksIdPatchRequest.md)|  | 

### Return type

[**ApiV1WebhooksPost201Response**](ApiV1WebhooksPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |
**422** | Validation error per field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_rotate_secret_post**
> ApiV1WebhooksPost201Response api_v1_webhooks_id_rotate_secret_post(id, api_v1_webhooks_id_rotate_secret_post_request=api_v1_webhooks_id_rotate_secret_post_request)

Issue a new signing secret.

For `overlap_hours` (0..168, default 24) the previous secret keeps
signing too — two `v1=` values — so you can switch whenever you like.
`0` ends the old secret at once. The new `secret` is in the answer
only.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_rotate_secret_post_request import ApiV1WebhooksIdRotateSecretPostRequest
from goadserver.models.api_v1_webhooks_post201_response import ApiV1WebhooksPost201Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 
    api_v1_webhooks_id_rotate_secret_post_request = goadserver.ApiV1WebhooksIdRotateSecretPostRequest() # ApiV1WebhooksIdRotateSecretPostRequest |  (optional)

    try:
        # Issue a new signing secret.
        api_response = api_instance.api_v1_webhooks_id_rotate_secret_post(id, api_v1_webhooks_id_rotate_secret_post_request=api_v1_webhooks_id_rotate_secret_post_request)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_rotate_secret_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_rotate_secret_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_webhooks_id_rotate_secret_post_request** | [**ApiV1WebhooksIdRotateSecretPostRequest**](ApiV1WebhooksIdRotateSecretPostRequest.md)|  | [optional] 

### Return type

[**ApiV1WebhooksPost201Response**](ApiV1WebhooksPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |
**409** | Rotated by someone else at the same moment. |  -  |
**422** | overlap_hours out of range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_id_test_post**
> ApiV1WebhooksIdTestPost200Response api_v1_webhooks_id_test_post(id)

Send a test ping.

Sends a signed `webhook.test` event now and answers what the receiver
said (`status` delivered / pending / dead, `http_status`, `error`). A
paused webhook only queues it.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_id_test_post200_response import ApiV1WebhooksIdTestPost200Response
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    id = 56 # int | 

    try:
        # Send a test ping.
        api_response = api_instance.api_v1_webhooks_id_test_post(id)
        print("The response of WebhooksEventsApi->api_v1_webhooks_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1WebhooksIdTestPost200Response**](ApiV1WebhooksIdTestPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not one of this credential&#39;s webhooks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_webhooks_post**
> ApiV1WebhooksPost201Response api_v1_webhooks_post(api_v1_webhooks_post_request)

Create a webhook.

Returns the signing `secret` (`whsec_…`) **once**. Every delivery is a
POST of the event envelope with `X-Integration-Event`,
`X-Integration-Delivery` (the event id — dedupe on it, delivery is
at-least-once), `X-Integration-Key-Id` and
`X-Integration-Signature: t=<unix>,v1=<hex HMAC-SHA256(secret, "<t>.<body>")>`
(check every `v1`; during a secret rotation there are two). Answer 2xx
within 10 s. Failures retry after 1 m, 5 m, 15 m, 1 h, 3 h, 6 h, 12 h,
24 h; a 4xx other than 408/429 is final; redirects are not followed.
20 failures in a row over a day pause the webhook (`paused_reason:
auto_failing`). Events are queued within about a minute (state
changes detected by the server's checks within about two to five).

The URL must be a public `https://` address — private, loopback,
link-local, metadata and reserved addresses are refused, when saved
and again when sent. Each event must be one this credential may see
(422 names the missing scope). Unknown body fields are refused.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_webhooks_post201_response import ApiV1WebhooksPost201Response
from goadserver.models.api_v1_webhooks_post_request import ApiV1WebhooksPostRequest
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
    api_instance = goadserver.WebhooksEventsApi(api_client)
    api_v1_webhooks_post_request = goadserver.ApiV1WebhooksPostRequest() # ApiV1WebhooksPostRequest | 

    try:
        # Create a webhook.
        api_response = api_instance.api_v1_webhooks_post(api_v1_webhooks_post_request)
        print("The response of WebhooksEventsApi->api_v1_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksEventsApi->api_v1_webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_webhooks_post_request** | [**ApiV1WebhooksPostRequest**](ApiV1WebhooksPostRequest.md)|  | 

### Return type

[**ApiV1WebhooksPost201Response**](ApiV1WebhooksPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created — the only answer that carries &#x60;secret&#x60;. |  -  |
**409** | &#x60;webhook_limit&#x60; — the account has 20 webhooks. |  -  |
**422** | Validation error per field (url, events, description) or an unknown field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.AccountNotificationsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_account_notification_destinations_get**](AccountNotificationsApi.md#api_v1_account_notification_destinations_get) | **GET** /api/v1/account/notification-destinations | The account&#39;s notification destinations.
[**api_v1_account_notification_destinations_id_delete**](AccountNotificationsApi.md#api_v1_account_notification_destinations_id_delete) | **DELETE** /api/v1/account/notification-destinations/{id} | Delete a notification destination.
[**api_v1_account_notification_destinations_id_status_get**](AccountNotificationsApi.md#api_v1_account_notification_destinations_id_status_get) | **GET** /api/v1/account/notification-destinations/{id}/status | Whether a destination is linked.
[**api_v1_account_notification_destinations_id_test_post**](AccountNotificationsApi.md#api_v1_account_notification_destinations_id_test_post) | **POST** /api/v1/account/notification-destinations/{id}/test | Send a test message to a destination.
[**api_v1_account_notification_destinations_post**](AccountNotificationsApi.md#api_v1_account_notification_destinations_post) | **POST** /api/v1/account/notification-destinations | Add a notification destination.
[**api_v1_account_notification_preferences_get**](AccountNotificationsApi.md#api_v1_account_notification_preferences_get) | **GET** /api/v1/account/notification-preferences | Per-event channel preferences.
[**api_v1_account_notification_preferences_put**](AccountNotificationsApi.md#api_v1_account_notification_preferences_put) | **PUT** /api/v1/account/notification-preferences | Save channel preferences.
[**api_v1_account_notifications_get**](AccountNotificationsApi.md#api_v1_account_notifications_get) | **GET** /api/v1/account/notifications | The in-app notification feed.
[**api_v1_account_notifications_read_post**](AccountNotificationsApi.md#api_v1_account_notifications_read_post) | **POST** /api/v1/account/notifications/read | Mark notifications read.
[**api_v1_account_notifications_unread_count_get**](AccountNotificationsApi.md#api_v1_account_notifications_unread_count_get) | **GET** /api/v1/account/notifications/unread-count | Unread notification count.


# **api_v1_account_notification_destinations_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_destinations_get()

The account's notification destinations.

User-created Telegram bots and Slack webhooks notifications can route to.
Secrets are never returned — only the kind, label and whether the channel
is linked.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)

    try:
        # The account's notification destinations.
        api_response = api_instance.api_v1_account_notification_destinations_get()
        print("The response of AccountNotificationsApi->api_v1_account_notification_destinations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_destinations_get: %s\n" % e)
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

# **api_v1_account_notification_destinations_id_delete**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_destinations_id_delete(id)

Delete a notification destination.

Events routed to it fall back to email.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    id = 56 # int | Destination ID.

    try:
        # Delete a notification destination.
        api_response = api_instance.api_v1_account_notification_destinations_id_delete(id)
        print("The response of AccountNotificationsApi->api_v1_account_notification_destinations_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_destinations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Destination ID. | 

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

# **api_v1_account_notification_destinations_id_status_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_destinations_id_status_get(id)

Whether a destination is linked.

A Telegram bot is only usable once the user has started a chat with it;
this reports whether that has happened.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    id = 56 # int | Destination ID.

    try:
        # Whether a destination is linked.
        api_response = api_instance.api_v1_account_notification_destinations_id_status_get(id)
        print("The response of AccountNotificationsApi->api_v1_account_notification_destinations_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_destinations_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Destination ID. | 

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

# **api_v1_account_notification_destinations_id_test_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_destinations_id_test_post(id)

Send a test message to a destination.

**Sends a real message** to the linked chat or channel. Use it to prove a
destination works; it is not a dry run.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    id = 56 # int | Destination ID.

    try:
        # Send a test message to a destination.
        api_response = api_instance.api_v1_account_notification_destinations_id_test_post(id)
        print("The response of AccountNotificationsApi->api_v1_account_notification_destinations_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_destinations_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Destination ID. | 

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

# **api_v1_account_notification_destinations_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_destinations_post(api_v1_account_notification_destinations_post_request)

Add a notification destination.

A Telegram bot (`token`) or a Slack incoming webhook (`url`). The
secret is stored write-only and never read back.

**Creating a destination contacts it.** A Slack webhook is posted a
"destination connected" message and a Telegram token is checked
against Telegram's API, both before the row is written — so a
destination that exists is one that has been proven to work. A URL
that is well-formed but dead answers 400 `unreachable`; one that is
not webhook-shaped answers 400 `invalid_url`; a rejected bot token
answers 400 `invalid_token`.

There is no way to register a destination without that round-trip,
which is deliberate: a silently broken notification channel is worse
than a create that fails loudly.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_notification_destinations_post_request import ApiV1AccountNotificationDestinationsPostRequest
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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    api_v1_account_notification_destinations_post_request = goadserver.ApiV1AccountNotificationDestinationsPostRequest() # ApiV1AccountNotificationDestinationsPostRequest | 

    try:
        # Add a notification destination.
        api_response = api_instance.api_v1_account_notification_destinations_post(api_v1_account_notification_destinations_post_request)
        print("The response of AccountNotificationsApi->api_v1_account_notification_destinations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_destinations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_account_notification_destinations_post_request** | [**ApiV1AccountNotificationDestinationsPostRequest**](ApiV1AccountNotificationDestinationsPostRequest.md)|  | 

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
**400** | invalid_kind, invalid_url, invalid_token, or unreachable — see the description. |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_notification_preferences_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notification_preferences_get()

Per-event channel preferences.

The full catalogue of notifiable events with, for each, whether email and
in-app are on, which destination it routes to, and whether it is mandatory
(mandatory = a security notice: on by default and always sent immediately,
never folded into a digest; it can still be switched off).


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
    api_instance = goadserver.AccountNotificationsApi(api_client)

    try:
        # Per-event channel preferences.
        api_response = api_instance.api_v1_account_notification_preferences_get()
        print("The response of AccountNotificationsApi->api_v1_account_notification_preferences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_preferences_get: %s\n" % e)
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

# **api_v1_account_notification_preferences_put**
> ApiV1WebhooksIdDelete200Response api_v1_account_notification_preferences_put(api_v1_account_notification_preferences_put_request)

Save channel preferences.

Bulk save of the per-event grid. Every visible event, mandatory ones
included, takes the sent value; unknown or hidden keys are ignored, so a
client can send the whole catalogue back unchanged.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_notification_preferences_put_request import ApiV1AccountNotificationPreferencesPutRequest
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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    api_v1_account_notification_preferences_put_request = goadserver.ApiV1AccountNotificationPreferencesPutRequest() # ApiV1AccountNotificationPreferencesPutRequest | 

    try:
        # Save channel preferences.
        api_response = api_instance.api_v1_account_notification_preferences_put(api_v1_account_notification_preferences_put_request)
        print("The response of AccountNotificationsApi->api_v1_account_notification_preferences_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notification_preferences_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_account_notification_preferences_put_request** | [**ApiV1AccountNotificationPreferencesPutRequest**](ApiV1AccountNotificationPreferencesPutRequest.md)|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

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

# **api_v1_account_notifications_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notifications_get(limit=limit, unread=unread)

The in-app notification feed.

Newest first, each item carrying the event key, its rendered title and
body, a deep link into the panel, and whether it has been read.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    limit = 56 # int | Rows to return. (optional)
    unread = 'unread_example' # str | Pass 1 to return only unread items. (optional)

    try:
        # The in-app notification feed.
        api_response = api_instance.api_v1_account_notifications_get(limit=limit, unread=unread)
        print("The response of AccountNotificationsApi->api_v1_account_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Rows to return. | [optional] 
 **unread** | **str**| Pass 1 to return only unread items. | [optional] 

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

# **api_v1_account_notifications_read_post**
> ApiV1WebhooksIdDelete200Response api_v1_account_notifications_read_post(api_v1_account_notifications_read_post_request)

Mark notifications read.

Pass `ids` for specific items, or `all` to clear the feed.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_notifications_read_post_request import ApiV1AccountNotificationsReadPostRequest
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
    api_instance = goadserver.AccountNotificationsApi(api_client)
    api_v1_account_notifications_read_post_request = goadserver.ApiV1AccountNotificationsReadPostRequest() # ApiV1AccountNotificationsReadPostRequest | 

    try:
        # Mark notifications read.
        api_response = api_instance.api_v1_account_notifications_read_post(api_v1_account_notifications_read_post_request)
        print("The response of AccountNotificationsApi->api_v1_account_notifications_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notifications_read_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_account_notifications_read_post_request** | [**ApiV1AccountNotificationsReadPostRequest**](ApiV1AccountNotificationsReadPostRequest.md)|  | 

### Return type

[**ApiV1WebhooksIdDelete200Response**](ApiV1WebhooksIdDelete200Response.md)

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

# **api_v1_account_notifications_unread_count_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_notifications_unread_count_get()

Unread notification count.

Just the number — the cheap poll behind the bell badge.


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
    api_instance = goadserver.AccountNotificationsApi(api_client)

    try:
        # Unread notification count.
        api_response = api_instance.api_v1_account_notifications_unread_count_get()
        print("The response of AccountNotificationsApi->api_v1_account_notifications_unread_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->api_v1_account_notifications_unread_count_get: %s\n" % e)
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


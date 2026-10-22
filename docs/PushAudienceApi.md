# goadserver.PushAudienceApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_push_delivery_rules_get**](PushAudienceApi.md#api_v1_publisher_push_delivery_rules_get) | **GET** /api/v1/publisher/push-delivery-rules | List standing delivery rules.
[**api_v1_publisher_push_delivery_rules_id_delete**](PushAudienceApi.md#api_v1_publisher_push_delivery_rules_id_delete) | **DELETE** /api/v1/publisher/push-delivery-rules/{id} | Delete a delivery rule.
[**api_v1_publisher_push_delivery_rules_id_put**](PushAudienceApi.md#api_v1_publisher_push_delivery_rules_id_put) | **PUT** /api/v1/publisher/push-delivery-rules/{id} | Update a delivery rule.
[**api_v1_publisher_push_delivery_rules_post**](PushAudienceApi.md#api_v1_publisher_push_delivery_rules_post) | **POST** /api/v1/publisher/push-delivery-rules | Create a delivery rule.
[**api_v1_publisher_push_segments_get**](PushAudienceApi.md#api_v1_publisher_push_segments_get) | **GET** /api/v1/publisher/push-segments | List saved audience segments.
[**api_v1_publisher_push_segments_id_delete**](PushAudienceApi.md#api_v1_publisher_push_segments_id_delete) | **DELETE** /api/v1/publisher/push-segments/{id} | Delete an audience segment.
[**api_v1_publisher_push_segments_id_put**](PushAudienceApi.md#api_v1_publisher_push_segments_id_put) | **PUT** /api/v1/publisher/push-segments/{id} | Update an audience segment.
[**api_v1_publisher_push_segments_post**](PushAudienceApi.md#api_v1_publisher_push_segments_post) | **POST** /api/v1/publisher/push-segments | Create an audience segment.
[**api_v1_publisher_push_setup_get**](PushAudienceApi.md#api_v1_publisher_push_setup_get) | **GET** /api/v1/publisher/push-setup | Collector setup facts for the opt-in script.
[**api_v1_publisher_push_stats_get**](PushAudienceApi.md#api_v1_publisher_push_stats_get) | **GET** /api/v1/publisher/push-stats | Push delivery performance.
[**api_v1_publisher_push_subscribers_action_post**](PushAudienceApi.md#api_v1_publisher_push_subscribers_action_post) | **POST** /api/v1/publisher/push-subscribers/action | Activate, deactivate or delete subscribers in bulk.
[**api_v1_publisher_push_subscribers_get**](PushAudienceApi.md#api_v1_publisher_push_subscribers_get) | **GET** /api/v1/publisher/push-subscribers | List captured push subscribers.


# **api_v1_publisher_push_delivery_rules_get**
> ApiV1PublisherPushDeliveryRulesGet200Response api_v1_publisher_push_delivery_rules_get()

List standing delivery rules.

Returns up to 200 rules, newest first, each with the outcome of
its last run (sent / failed / no-ad counts).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_delivery_rules_get200_response import ApiV1PublisherPushDeliveryRulesGet200Response
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
    api_instance = goadserver.PushAudienceApi(api_client)

    try:
        # List standing delivery rules.
        api_response = api_instance.api_v1_publisher_push_delivery_rules_get()
        print("The response of PushAudienceApi->api_v1_publisher_push_delivery_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_delivery_rules_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherPushDeliveryRulesGet200Response**](ApiV1PublisherPushDeliveryRulesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rule list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_delivery_rules_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_publisher_push_delivery_rules_id_delete(id)

Delete a delivery rule.

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
    api_instance = goadserver.PushAudienceApi(api_client)
    id = 56 # int | Rule ID.

    try:
        # Delete a delivery rule.
        api_response = api_instance.api_v1_publisher_push_delivery_rules_id_delete(id)
        print("The response of PushAudienceApi->api_v1_publisher_push_delivery_rules_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_delivery_rules_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 

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
**404** | Delivery rule not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_delivery_rules_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_delivery_rules_id_put(id, api_v1_publisher_push_delivery_rules_id_put_request)

Update a delivery rule.

Full replace, including `is_active` — this is also how a rule is
paused and resumed.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_delivery_rules_id_put_request import ApiV1PublisherPushDeliveryRulesIdPutRequest
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
    api_instance = goadserver.PushAudienceApi(api_client)
    id = 56 # int | Rule ID.
    api_v1_publisher_push_delivery_rules_id_put_request = goadserver.ApiV1PublisherPushDeliveryRulesIdPutRequest() # ApiV1PublisherPushDeliveryRulesIdPutRequest | 

    try:
        # Update a delivery rule.
        api_response = api_instance.api_v1_publisher_push_delivery_rules_id_put(id, api_v1_publisher_push_delivery_rules_id_put_request)
        print("The response of PushAudienceApi->api_v1_publisher_push_delivery_rules_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_delivery_rules_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 
 **api_v1_publisher_push_delivery_rules_id_put_request** | [**ApiV1PublisherPushDeliveryRulesIdPutRequest**](ApiV1PublisherPushDeliveryRulesIdPutRequest.md)|  | 

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
**400** | invalid_id, name_required, or invalid_segment. |  -  |
**404** | Delivery rule not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_delivery_rules_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_delivery_rules_post(api_v1_publisher_push_delivery_rules_post_request)

Create a delivery rule.

`segment_id` must be a segment you own, or 0 for the whole active
audience. `cadence_hours` below 1 is rejected into the 24h
default; the other numeric knobs clamp to >= 0.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_delivery_rules_post_request import ApiV1PublisherPushDeliveryRulesPostRequest
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
    api_instance = goadserver.PushAudienceApi(api_client)
    api_v1_publisher_push_delivery_rules_post_request = goadserver.ApiV1PublisherPushDeliveryRulesPostRequest() # ApiV1PublisherPushDeliveryRulesPostRequest | 

    try:
        # Create a delivery rule.
        api_response = api_instance.api_v1_publisher_push_delivery_rules_post(api_v1_publisher_push_delivery_rules_post_request)
        print("The response of PushAudienceApi->api_v1_publisher_push_delivery_rules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_delivery_rules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_push_delivery_rules_post_request** | [**ApiV1PublisherPushDeliveryRulesPostRequest**](ApiV1PublisherPushDeliveryRulesPostRequest.md)|  | 

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
**200** | Created — returns the new rule id. |  -  |
**400** | name_required, or invalid_segment (segment not yours). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_segments_get**
> ApiV1PublisherPushSegmentsGet200Response api_v1_publisher_push_segments_get()

List saved audience segments.

Returns up to 200 segments, newest first. Each carries
`subscriber_count` — how many of the caller's subscribers match
the segment right now, counted live.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_segments_get200_response import ApiV1PublisherPushSegmentsGet200Response
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
    api_instance = goadserver.PushAudienceApi(api_client)

    try:
        # List saved audience segments.
        api_response = api_instance.api_v1_publisher_push_segments_get()
        print("The response of PushAudienceApi->api_v1_publisher_push_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_segments_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherPushSegmentsGet200Response**](ApiV1PublisherPushSegmentsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_segments_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_publisher_push_segments_id_delete(id)

Delete an audience segment.

Deletes the segment. Delivery rules that referenced it keep
running against the whole active audience.


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
    api_instance = goadserver.PushAudienceApi(api_client)
    id = 56 # int | Segment ID.

    try:
        # Delete an audience segment.
        api_response = api_instance.api_v1_publisher_push_segments_id_delete(id)
        print("The response of PushAudienceApi->api_v1_publisher_push_segments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_segments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment ID. | 

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
**404** | Segment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_segments_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_segments_id_put(id, api_v1_publisher_push_segments_id_put_request)

Update an audience segment.

Full replace — every omitted criterion resets to its zero value.
Saving identical values is a no-op, not a 404.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_segments_id_put_request import ApiV1PublisherPushSegmentsIdPutRequest
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
    api_instance = goadserver.PushAudienceApi(api_client)
    id = 56 # int | Segment ID.
    api_v1_publisher_push_segments_id_put_request = goadserver.ApiV1PublisherPushSegmentsIdPutRequest() # ApiV1PublisherPushSegmentsIdPutRequest | 

    try:
        # Update an audience segment.
        api_response = api_instance.api_v1_publisher_push_segments_id_put(id, api_v1_publisher_push_segments_id_put_request)
        print("The response of PushAudienceApi->api_v1_publisher_push_segments_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_segments_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment ID. | 
 **api_v1_publisher_push_segments_id_put_request** | [**ApiV1PublisherPushSegmentsIdPutRequest**](ApiV1PublisherPushSegmentsIdPutRequest.md)|  | 

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
**400** | invalid_id, or name_required. |  -  |
**404** | Segment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_segments_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_publisher_push_segments_post(api_v1_publisher_push_segments_post_request)

Create an audience segment.

Every criterion is optional and they AND together — a segment with
no criteria set matches the whole audience. Only `name` is
required. Numeric criteria are clamped to >= 0.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_publisher_push_segments_post_request import ApiV1PublisherPushSegmentsPostRequest
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
    api_instance = goadserver.PushAudienceApi(api_client)
    api_v1_publisher_push_segments_post_request = goadserver.ApiV1PublisherPushSegmentsPostRequest() # ApiV1PublisherPushSegmentsPostRequest | 

    try:
        # Create an audience segment.
        api_response = api_instance.api_v1_publisher_push_segments_post(api_v1_publisher_push_segments_post_request)
        print("The response of PushAudienceApi->api_v1_publisher_push_segments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_segments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_push_segments_post_request** | [**ApiV1PublisherPushSegmentsPostRequest**](ApiV1PublisherPushSegmentsPostRequest.md)|  | 

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
**200** | Created — returns the new segment id. |  -  |
**400** | name_required. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_setup_get**
> ApiV1PublisherPushSetupGet200Response api_v1_publisher_push_setup_get()

Collector setup facts for the opt-in script.

Everything needed to wire the web-push opt-in collector onto a
landing page: the ad host the collector and service worker are
served from, the service-worker path this network expects, and
every pushads adzone you own with its ad domain, captured
subscriber count and most recent opt-in. Read-only — nothing is
generated or registered by calling it.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_setup_get200_response import ApiV1PublisherPushSetupGet200Response
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
    api_instance = goadserver.PushAudienceApi(api_client)

    try:
        # Collector setup facts for the opt-in script.
        api_response = api_instance.api_v1_publisher_push_setup_get()
        print("The response of PushAudienceApi->api_v1_publisher_push_setup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_setup_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherPushSetupGet200Response**](ApiV1PublisherPushSetupGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Setup facts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_stats_get**
> ApiV1PublisherPushStatsGet200Response api_v1_publisher_push_stats_get(days=days)

Push delivery performance.

Delivery, clicks and revenue for auctioned pushes served on the
caller's pushads adzones, paired with subscriber growth over the
same window. Revenue is in the account currency.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_stats_get200_response import ApiV1PublisherPushStatsGet200Response
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
    api_instance = goadserver.PushAudienceApi(api_client)
    days = 30 # int | Trailing window in days. Default 30, capped at 365. (optional) (default to 30)

    try:
        # Push delivery performance.
        api_response = api_instance.api_v1_publisher_push_stats_get(days=days)
        print("The response of PushAudienceApi->api_v1_publisher_push_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Trailing window in days. Default 30, capped at 365. | [optional] [default to 30]

### Return type

[**ApiV1PublisherPushStatsGet200Response**](ApiV1PublisherPushStatsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary + daily series |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_subscribers_action_post**
> ApiV1PublisherPushSubscribersActionPost200Response api_v1_publisher_push_subscribers_action_post(api_v1_publisher_push_subscribers_action_post_request)

Activate, deactivate or delete subscribers in bulk.

One action over up to 5000 subscriber ids. Ids that are not the
caller's are silently skipped — `affected` reports how many rows
actually changed.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_subscribers_action_post200_response import ApiV1PublisherPushSubscribersActionPost200Response
from goadserver.models.api_v1_publisher_push_subscribers_action_post_request import ApiV1PublisherPushSubscribersActionPostRequest
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
    api_instance = goadserver.PushAudienceApi(api_client)
    api_v1_publisher_push_subscribers_action_post_request = goadserver.ApiV1PublisherPushSubscribersActionPostRequest() # ApiV1PublisherPushSubscribersActionPostRequest | 

    try:
        # Activate, deactivate or delete subscribers in bulk.
        api_response = api_instance.api_v1_publisher_push_subscribers_action_post(api_v1_publisher_push_subscribers_action_post_request)
        print("The response of PushAudienceApi->api_v1_publisher_push_subscribers_action_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_subscribers_action_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_push_subscribers_action_post_request** | [**ApiV1PublisherPushSubscribersActionPostRequest**](ApiV1PublisherPushSubscribersActionPostRequest.md)|  | 

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
**200** | Applied |  -  |
**400** | no_ids, too_many (&gt;5000), or invalid_action. |  -  |
**403** | The key&#39;s member scope does not reach these subscribers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_push_subscribers_get**
> ApiV1PublisherPushSubscribersGet200Response api_v1_publisher_push_subscribers_get(days=days)

List captured push subscribers.

The caller's opt-ins within the trailing window, newest first,
capped at 1000 rows — alongside lifetime totals so you can size
the audience without paging. Subscriber IPs are masked to a /24
(IPv4) or /48 (IPv6) prefix on the way out.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_subscribers_get200_response import ApiV1PublisherPushSubscribersGet200Response
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
    api_instance = goadserver.PushAudienceApi(api_client)
    days = 30 # int | Trailing window in days. Default 30, capped at 365. (optional) (default to 30)

    try:
        # List captured push subscribers.
        api_response = api_instance.api_v1_publisher_push_subscribers_get(days=days)
        print("The response of PushAudienceApi->api_v1_publisher_push_subscribers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushAudienceApi->api_v1_publisher_push_subscribers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Trailing window in days. Default 30, capped at 365. | [optional] [default to 30]

### Return type

[**ApiV1PublisherPushSubscribersGet200Response**](ApiV1PublisherPushSubscribersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscriber list + audience totals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


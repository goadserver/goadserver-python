# goadserver.TrackerTrackingLinksApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_tracking_links_bulk_post**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_bulk_post) | **POST** /api/v1/tracker/tracking-links/bulk | Delete many tracking links.
[**api_v1_tracker_tracking_links_get**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_get) | **GET** /api/v1/tracker/tracking-links | List tracking links.
[**api_v1_tracker_tracking_links_id_blocklist_get**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_get) | **GET** /api/v1/tracker/tracking-links/{id}/blocklist | List zones blocked on one link.
[**api_v1_tracker_tracking_links_id_blocklist_post**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_post) | **POST** /api/v1/tracker/tracking-links/{id}/blocklist | Block a zone on one link.
[**api_v1_tracker_tracking_links_id_blocklist_zone_id_delete**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_blocklist_zone_id_delete) | **DELETE** /api/v1/tracker/tracking-links/{id}/blocklist/{zoneId} | Unblock a zone on one link.
[**api_v1_tracker_tracking_links_id_delete**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_delete) | **DELETE** /api/v1/tracker/tracking-links/{id} | Delete a tracking link.
[**api_v1_tracker_tracking_links_id_network_binding_delete**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_network_binding_delete) | **DELETE** /api/v1/tracker/tracking-links/{id}/network-binding | Unbind a tracking link from its ad-network campaign.
[**api_v1_tracker_tracking_links_id_network_binding_put**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_network_binding_put) | **PUT** /api/v1/tracker/tracking-links/{id}/network-binding | Bind a tracking link to an ad-network campaign.
[**api_v1_tracker_tracking_links_id_put**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_put) | **PUT** /api/v1/tracker/tracking-links/{id} | Update a tracking link.
[**api_v1_tracker_tracking_links_id_toggle_active_post**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_toggle_active_post) | **POST** /api/v1/tracker/tracking-links/{id}/toggle-active | Pause or resume the bound network campaign.
[**api_v1_tracker_tracking_links_id_zone_costs_get**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_id_zone_costs_get) | **GET** /api/v1/tracker/tracking-links/{id}/zone-costs | Per-zone cost and performance for one link.
[**api_v1_tracker_tracking_links_post**](TrackerTrackingLinksApi.md#api_v1_tracker_tracking_links_post) | **POST** /api/v1/tracker/tracking-links | Create a tracking link.


# **api_v1_tracker_tracking_links_bulk_post**
> ApiV1PublisherPushSubscribersActionPost200Response api_v1_tracker_tracking_links_bulk_post(api_v1_tracker_tracking_links_bulk_post_request)

Delete many tracking links.

The tracking-link twin of `/offers/bulk`, but delete-only. A link's
on/off state is set one at a time through
`POST /tracking-links/{id}/toggle-active` — pausing a link a live
traffic source is still sending to is a decision worth making per
link, not per batch.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_subscribers_action_post200_response import ApiV1PublisherPushSubscribersActionPost200Response
from goadserver.models.api_v1_tracker_tracking_links_bulk_post_request import ApiV1TrackerTrackingLinksBulkPostRequest
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    api_v1_tracker_tracking_links_bulk_post_request = goadserver.ApiV1TrackerTrackingLinksBulkPostRequest() # ApiV1TrackerTrackingLinksBulkPostRequest | 

    try:
        # Delete many tracking links.
        api_response = api_instance.api_v1_tracker_tracking_links_bulk_post(api_v1_tracker_tracking_links_bulk_post_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_tracking_links_bulk_post_request** | [**ApiV1TrackerTrackingLinksBulkPostRequest**](ApiV1TrackerTrackingLinksBulkPostRequest.md)|  | 

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

# **api_v1_tracker_tracking_links_get**
> ApiV1TrackerTrackingLinksGet200Response api_v1_tracker_tracking_links_get()

List tracking links.

Each link is a `publisher_adzones` row under a hidden source site. A link
bound to one offer redirects straight to it; a smartlink carries several
`offer_ids` and lets targeting and eCPM pick the winner per click.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_get200_response import ApiV1TrackerTrackingLinksGet200Response
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)

    try:
        # List tracking links.
        api_response = api_instance.api_v1_tracker_tracking_links_get()
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksGet200Response**](ApiV1TrackerTrackingLinksGet200Response.md)

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

# **api_v1_tracker_tracking_links_id_blocklist_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_tracking_links_id_blocklist_get(id)

List zones blocked on one link.

The placements this link refuses to buy. 404 while the link is not
bound to an ad network — there are no placements to block until it is.


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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.

    try:
        # List zones blocked on one link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_blocklist_get(id)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 

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

# **api_v1_tracker_tracking_links_id_blocklist_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_tracking_links_id_blocklist_post(id, api_v1_tracker_tracking_links_id_blocklist_post_request)

Block a zone on one link.

Adds a placement to the link's block list; the traffic source stops being
bought on that zone. 404 while the link is not bound to an ad network.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_blocklist_post_request import ApiV1TrackerTrackingLinksIdBlocklistPostRequest
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.
    api_v1_tracker_tracking_links_id_blocklist_post_request = goadserver.ApiV1TrackerTrackingLinksIdBlocklistPostRequest() # ApiV1TrackerTrackingLinksIdBlocklistPostRequest | 

    try:
        # Block a zone on one link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_blocklist_post(id, api_v1_tracker_tracking_links_id_blocklist_post_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 
 **api_v1_tracker_tracking_links_id_blocklist_post_request** | [**ApiV1TrackerTrackingLinksIdBlocklistPostRequest**](ApiV1TrackerTrackingLinksIdBlocklistPostRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_blocklist_zone_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_tracking_links_id_blocklist_zone_id_delete(id, zone_id)

Unblock a zone on one link.

Removes the placement from the block list. 404 while the link is not
bound to an ad network.


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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.
    zone_id = 'zone_id_example' # str | Zone / placement id.

    try:
        # Unblock a zone on one link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_blocklist_zone_id_delete(id, zone_id)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_zone_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_blocklist_zone_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 
 **zone_id** | **str**| Zone / placement id. | 

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

# **api_v1_tracker_tracking_links_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_tracking_links_id_delete(id)

Delete a tracking link.

Soft delete — the link stops serving, its click history stays.


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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.

    try:
        # Delete a tracking link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_delete(id)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 

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

# **api_v1_tracker_tracking_links_id_network_binding_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_tracking_links_id_network_binding_delete(id)

Unbind a tracking link from its ad-network campaign.

Cost stops being attributed to the link.


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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.

    try:
        # Unbind a tracking link from its ad-network campaign.
        api_response = api_instance.api_v1_tracker_tracking_links_id_network_binding_delete(id)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_network_binding_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_network_binding_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 

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

# **api_v1_tracker_tracking_links_id_network_binding_put**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_tracking_links_id_network_binding_put(id, api_v1_tracker_tracking_links_id_network_binding_put_request)

Bind a tracking link to an ad-network campaign.

Ties the link to a campaign on the buying side, so spend pulled from that
network lands against this link's revenue. `auto_api` lets rules push
pause / bid changes back to the network.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_network_binding_put_request import ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.
    api_v1_tracker_tracking_links_id_network_binding_put_request = goadserver.ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest() # ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest | 

    try:
        # Bind a tracking link to an ad-network campaign.
        api_response = api_instance.api_v1_tracker_tracking_links_id_network_binding_put(id, api_v1_tracker_tracking_links_id_network_binding_put_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_network_binding_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_network_binding_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 
 **api_v1_tracker_tracking_links_id_network_binding_put_request** | [**ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest**](ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_tracking_links_id_put(id, api_v1_tracker_tracking_links_id_put_request)

Update a tracking link.

Partial update — omitted fields keep their current value.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_tracking_links_id_put_request import ApiV1TrackerTrackingLinksIdPutRequest
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link (adzone) ID.
    api_v1_tracker_tracking_links_id_put_request = goadserver.ApiV1TrackerTrackingLinksIdPutRequest() # ApiV1TrackerTrackingLinksIdPutRequest | 

    try:
        # Update a tracking link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_put(id, api_v1_tracker_tracking_links_id_put_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link (adzone) ID. | 
 **api_v1_tracker_tracking_links_id_put_request** | [**ApiV1TrackerTrackingLinksIdPutRequest**](ApiV1TrackerTrackingLinksIdPutRequest.md)|  | 

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

# **api_v1_tracker_tracking_links_id_toggle_active_post**
> ApiV1TrackerTrackingLinksIdToggleActivePost200Response api_v1_tracker_tracking_links_id_toggle_active_post(id, api_v1_campaigns_type_id_active_patch_request)

Pause or resume the bound network campaign.

**This reaches out to the traffic source.** It does not flip a local
flag: it calls the bound ad network's API to pause or resume the
campaign this link is bound to, and writes the outcome back to
`adnetwork_state`.

The binding is required — an unbound link answers 400 `no_binding`.

Day to day you do not need this: goadserver's `UpdateFromAdzones`
cron already mirrors local offer state to the remote campaign every
tick. It exists for "pause the source right now" without waiting for
the next tick, and for reporting-only bindings (`auto_api` false)
where the cron never acts.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_tracker_tracking_links_id_toggle_active_post200_response import ApiV1TrackerTrackingLinksIdToggleActivePost200Response
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Pause or resume the bound network campaign.
        api_response = api_instance.api_v1_tracker_tracking_links_id_toggle_active_post(id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_toggle_active_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_toggle_active_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1TrackerTrackingLinksIdToggleActivePost200Response**](ApiV1TrackerTrackingLinksIdToggleActivePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | no_binding — the link is not bound to an ad network; or invalid_body. |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_zone_costs_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_tracking_links_id_zone_costs_get(id, days=days)

Per-zone cost and performance for one link.

Placement-level spend and result for the link's bound traffic source, the
input a placement rule blocks on. See docs/TRACKER_ZONE_BLOCKING.md.

Placement data comes from the bound ad network, so a link with no
binding answers 404 — bind it with `PUT /tracking-links/{id}/network-binding`
first.


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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    id = 56 # int | Tracking link ID.
    days = 7 # int | Trailing window in days. (optional) (default to 7)

    try:
        # Per-zone cost and performance for one link.
        api_response = api_instance.api_v1_tracker_tracking_links_id_zone_costs_get(id, days=days)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_zone_costs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_id_zone_costs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking link ID. | 
 **days** | **int**| Trailing window in days. | [optional] [default to 7]

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

# **api_v1_tracker_tracking_links_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_tracking_links_post(api_v1_tracker_tracking_links_post_request)

Create a tracking link.

Pass `offer_id` for a single-offer link, or `offer_ids` (optionally with
matching `weights`) for a smartlink. `tokens` names the macro slots the
click URL should carry.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_tracking_links_post_request import ApiV1TrackerTrackingLinksPostRequest
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
    api_instance = goadserver.TrackerTrackingLinksApi(api_client)
    api_v1_tracker_tracking_links_post_request = goadserver.ApiV1TrackerTrackingLinksPostRequest() # ApiV1TrackerTrackingLinksPostRequest | 

    try:
        # Create a tracking link.
        api_response = api_instance.api_v1_tracker_tracking_links_post(api_v1_tracker_tracking_links_post_request)
        print("The response of TrackerTrackingLinksApi->api_v1_tracker_tracking_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerTrackingLinksApi->api_v1_tracker_tracking_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_tracking_links_post_request** | [**ApiV1TrackerTrackingLinksPostRequest**](ApiV1TrackerTrackingLinksPostRequest.md)|  | 

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


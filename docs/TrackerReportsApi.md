# goadserver.TrackerReportsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_cost_summary_get**](TrackerReportsApi.md#api_v1_tracker_cost_summary_get) | **GET** /api/v1/tracker/cost-summary | Spend against revenue.
[**api_v1_tracker_daily_stats_get**](TrackerReportsApi.md#api_v1_tracker_daily_stats_get) | **GET** /api/v1/tracker/daily-stats | Daily performance, filtered.
[**api_v1_tracker_inline_stats_get**](TrackerReportsApi.md#api_v1_tracker_inline_stats_get) | **GET** /api/v1/tracker/inline-stats | Per-row performance for a listing.
[**api_v1_tracker_player_ltv_get**](TrackerReportsApi.md#api_v1_tracker_player_ltv_get) | **GET** /api/v1/tracker/player-ltv | Lifetime value by cohort.
[**api_v1_tracker_postbacks_stats_get**](TrackerReportsApi.md#api_v1_tracker_postbacks_stats_get) | **GET** /api/v1/tracker/postbacks/stats | Outbound postback firing log.
[**api_v1_tracker_recent_clicks_get**](TrackerReportsApi.md#api_v1_tracker_recent_clicks_get) | **GET** /api/v1/tracker/recent-clicks | The most recent clicks.


# **api_v1_tracker_cost_summary_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_cost_summary_get(var_from=var_from, to=to)

Spend against revenue.

Imported ad-account spend joined to tracker revenue — the ROI view. Only
as complete as the last cost pull; see /source-accounts for sync state.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    var_from = 'var_from_example' # str | Start date, YYYY-MM-DD. (optional)
    to = 'to_example' # str | End date, YYYY-MM-DD. (optional)

    try:
        # Spend against revenue.
        api_response = api_instance.api_v1_tracker_cost_summary_get(var_from=var_from, to=to)
        print("The response of TrackerReportsApi->api_v1_tracker_cost_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_cost_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| Start date, YYYY-MM-DD. | [optional] 
 **to** | **str**| End date, YYYY-MM-DD. | [optional] 

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

# **api_v1_tracker_daily_stats_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_daily_stats_get(var_from=var_from, to=to, offer_ids=offer_ids, link_ids=link_ids, source_ids=source_ids, countries=countries, device_ids=device_ids)

Daily performance, filtered.

Clicks, conversions, revenue and cost per day for the caller's tracker
traffic. Every filter is repeatable and ANDs with the rest.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    var_from = 'var_from_example' # str | Start date, YYYY-MM-DD. (optional)
    to = 'to_example' # str | End date, YYYY-MM-DD. (optional)
    offer_ids = 'offer_ids_example' # str | Comma-separated offer ids. (optional)
    link_ids = 'link_ids_example' # str | Comma-separated tracking-link ids. (optional)
    source_ids = 'source_ids_example' # str | Comma-separated source ids. (optional)
    countries = 'countries_example' # str | Comma-separated country codes. (optional)
    device_ids = 'device_ids_example' # str | Comma-separated device-type ids. (optional)

    try:
        # Daily performance, filtered.
        api_response = api_instance.api_v1_tracker_daily_stats_get(var_from=var_from, to=to, offer_ids=offer_ids, link_ids=link_ids, source_ids=source_ids, countries=countries, device_ids=device_ids)
        print("The response of TrackerReportsApi->api_v1_tracker_daily_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_daily_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| Start date, YYYY-MM-DD. | [optional] 
 **to** | **str**| End date, YYYY-MM-DD. | [optional] 
 **offer_ids** | **str**| Comma-separated offer ids. | [optional] 
 **link_ids** | **str**| Comma-separated tracking-link ids. | [optional] 
 **source_ids** | **str**| Comma-separated source ids. | [optional] 
 **countries** | **str**| Comma-separated country codes. | [optional] 
 **device_ids** | **str**| Comma-separated device-type ids. | [optional] 

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

# **api_v1_tracker_inline_stats_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_inline_stats_get(var_from=var_from, to=to, type=type)

Per-row performance for a listing.

The numbers the offer and tracking-link listings show inline, so an
integration can render the same table without a stats query per row.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    var_from = 'var_from_example' # str | Start date, YYYY-MM-DD. (optional)
    to = 'to_example' # str | End date, YYYY-MM-DD. (optional)
    type = 'type_example' # str | Which listing to size. (optional)

    try:
        # Per-row performance for a listing.
        api_response = api_instance.api_v1_tracker_inline_stats_get(var_from=var_from, to=to, type=type)
        print("The response of TrackerReportsApi->api_v1_tracker_inline_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_inline_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| Start date, YYYY-MM-DD. | [optional] 
 **to** | **str**| End date, YYYY-MM-DD. | [optional] 
 **type** | **str**| Which listing to size. | [optional] 

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

# **api_v1_tracker_player_ltv_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_player_ltv_get(days=days)

Lifetime value by cohort.

Revenue per acquired user over time, for offers that keep paying after the
first conversion.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    days = 30 # int | Cohort window in days. (optional) (default to 30)

    try:
        # Lifetime value by cohort.
        api_response = api_instance.api_v1_tracker_player_ltv_get(days=days)
        print("The response of TrackerReportsApi->api_v1_tracker_player_ltv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_player_ltv_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Cohort window in days. | [optional] [default to 30]

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

# **api_v1_tracker_postbacks_stats_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_postbacks_stats_get(datestart=datestart, dateend=dateend, siteid=siteid, conv_type=conv_type)

Outbound postback firing log.

Every postback the tracker sent upstream and how the receiver answered —
the evidence when a network says it never heard from you.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    datestart = 'datestart_example' # str | Start date, YYYY-MM-DD. (optional)
    dateend = 'dateend_example' # str | End date, YYYY-MM-DD. (optional)
    siteid = 56 # int | Narrow to one traffic source. (optional)
    conv_type = 'conv_type_example' # str | Narrow to one conversion-type letter. (optional)

    try:
        # Outbound postback firing log.
        api_response = api_instance.api_v1_tracker_postbacks_stats_get(datestart=datestart, dateend=dateend, siteid=siteid, conv_type=conv_type)
        print("The response of TrackerReportsApi->api_v1_tracker_postbacks_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_postbacks_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datestart** | **str**| Start date, YYYY-MM-DD. | [optional] 
 **dateend** | **str**| End date, YYYY-MM-DD. | [optional] 
 **siteid** | **int**| Narrow to one traffic source. | [optional] 
 **conv_type** | **str**| Narrow to one conversion-type letter. | [optional] 

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

# **api_v1_tracker_recent_clicks_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_recent_clicks_get(limit=limit)

The most recent clicks.

A live tail of the click stream with the macro values each click carried —
what you read while checking that a new link fires correctly.


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
    api_instance = goadserver.TrackerReportsApi(api_client)
    limit = 100 # int | Rows to return. (optional) (default to 100)

    try:
        # The most recent clicks.
        api_response = api_instance.api_v1_tracker_recent_clicks_get(limit=limit)
        print("The response of TrackerReportsApi->api_v1_tracker_recent_clicks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportsApi->api_v1_tracker_recent_clicks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Rows to return. | [optional] [default to 100]

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


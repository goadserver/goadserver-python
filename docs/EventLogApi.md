# goadserver.EventLogApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_event_log_exports_get**](EventLogApi.md#api_v1_event_log_exports_get) | **GET** /api/v1/event-log/exports | Your event log exports, newest first.
[**api_v1_event_log_exports_id_download_get**](EventLogApi.md#api_v1_event_log_exports_id_download_get) | **GET** /api/v1/event-log/exports/{id}/download | Download a finished export (.csv.gz).
[**api_v1_event_log_exports_post**](EventLogApi.md#api_v1_event_log_exports_post) | **POST** /api/v1/event-log/exports | Queue a CSV export of your events.
[**api_v1_event_log_get**](EventLogApi.md#api_v1_event_log_get) | **GET** /api/v1/event-log | Your raw events — impressions and clicks with IP and user agent (90 days).


# **api_v1_event_log_exports_get**
> api_v1_event_log_exports_get()

Your event log exports, newest first.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.EventLogApi(api_client)

    try:
        # Your event log exports, newest first.
        api_instance.api_v1_event_log_exports_get()
    except Exception as e:
        print("Exception when calling EventLogApi->api_v1_event_log_exports_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | The event log is not enabled for this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_event_log_exports_id_download_get**
> api_v1_event_log_exports_id_download_get(id)

Download a finished export (.csv.gz).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.EventLogApi(api_client)
    id = 56 # int | 

    try:
        # Download a finished export (.csv.gz).
        api_instance.api_v1_event_log_exports_id_download_get(id)
    except Exception as e:
        print("Exception when calling EventLogApi->api_v1_event_log_exports_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gzip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gzip-compressed CSV. |  -  |
**404** | Not your export. |  -  |
**409** | Not finished yet (queued, running, failed). |  -  |
**410** | Expired — files are kept 7 days. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_event_log_exports_post**
> api_v1_event_log_exports_post(api_v1_event_log_exports_post_request)

Queue a CSV export of your events.

Queues a CSV export; it is built in the background, one export at a time,
and the 202 answer is the export row (`status: queued`). Follow it on the
exports list; the file is a gzip-compressed CSV with the same columns as
the preview, at most 31 days and 20,000,000 rows (`truncated: true` when
the cap was hit), kept 7 days. At most 3 exports may wait per requester
(429 `too_many_exports`).
You are notified (in-app / email, per your notification settings) when it is ready.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_event_log_exports_post_request import ApiV1EventLogExportsPostRequest
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
    api_instance = goadserver.EventLogApi(api_client)
    api_v1_event_log_exports_post_request = {"date_from":"2026-10-22","date_to":"2026-10-28","ad_id":3891355,"event":"click"} # ApiV1EventLogExportsPostRequest | 

    try:
        # Queue a CSV export of your events.
        api_instance.api_v1_event_log_exports_post(api_v1_event_log_exports_post_request)
    except Exception as e:
        print("Exception when calling EventLogApi->api_v1_event_log_exports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_event_log_exports_post_request** | [**ApiV1EventLogExportsPostRequest**](ApiV1EventLogExportsPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Queued |  -  |
**403** | The event log is not enabled for this account. |  -  |
**422** | Invalid filter. |  -  |
**429** | Three exports already waiting. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_event_log_get**
> api_v1_event_log_get(date_from=date_from, date_to=date_to, side=side, campaign_id=campaign_id, ad_id=ad_id, site_id=site_id, zone_id=zone_id, event=event, country=country, ip=ip, page=page, per_page=per_page)

Your raw events — impressions and clicks with IP and user agent (90 days).

Only for accounts the network enabled the event log for (user right
`raw_event_log`, off by default; 403 otherwise). Not available on ad
networks, where the event log is for the network's administrators
only (403). Every event where you
are the advertiser or the publisher, kept 90 days from the day the
right was switched on: `time` (network timezone), `time_utc`, `event`,
the campaign / ad / publisher / site / zone ids, `ip`, `user_agent`,
`country` and device / os / browser / isp ids. No money columns. Newest
first, 100 rows a page at most; `total` is the full match count. For
more than a screenful, queue an export. Same handler as the panel's
Event Log page.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.EventLogApi(api_client)
    date_from = '2013-10-20' # date | First day (YYYY-MM-DD, network timezone). Default date_to. Events are kept 90 days; older dates are a 422. (optional)
    date_to = '2013-10-20' # date | Last day. Default today. (optional)
    side = 'side_example' # str | Only events where the account is the advertiser, or the publisher. Omit for both. (optional)
    campaign_id = 56 # int |  (optional)
    ad_id = 56 # int |  (optional)
    site_id = 56 # int |  (optional)
    zone_id = 56 # int |  (optional)
    event = 'event_example' # str |  (optional)
    country = 'NL' # str | Two-letter country code. (optional)
    ip = 'ip_example' # str | Exact visitor IP. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # Your raw events — impressions and clicks with IP and user agent (90 days).
        api_instance.api_v1_event_log_get(date_from=date_from, date_to=date_to, side=side, campaign_id=campaign_id, ad_id=ad_id, site_id=site_id, zone_id=zone_id, event=event, country=country, ip=ip, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling EventLogApi->api_v1_event_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **date**| First day (YYYY-MM-DD, network timezone). Default date_to. Events are kept 90 days; older dates are a 422. | [optional] 
 **date_to** | **date**| Last day. Default today. | [optional] 
 **side** | **str**| Only events where the account is the advertiser, or the publisher. Omit for both. | [optional] 
 **campaign_id** | **int**|  | [optional] 
 **ad_id** | **int**|  | [optional] 
 **site_id** | **int**|  | [optional] 
 **zone_id** | **int**|  | [optional] 
 **event** | **str**|  | [optional] 
 **country** | **str**| Two-letter country code. | [optional] 
 **ip** | **str**| Exact visitor IP. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | The event log is not enabled for this account. |  -  |
**422** | Invalid filter (e.g. a date older than 90 days). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


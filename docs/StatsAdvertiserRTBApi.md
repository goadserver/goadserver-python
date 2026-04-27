# goadserver.StatsAdvertiserRTBApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_advertiser_rtb_stats_get**](StatsAdvertiserRTBApi.md#api_v1_advertiser_rtb_stats_get) | **GET** /api/v1/advertiser/rtb/stats | DSP / RTB-side stats.


# **api_v1_advertiser_rtb_stats_get**
> StatsResponse api_v1_advertiser_rtb_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, format=format, page=page, per_page=per_page, sort=sort)

DSP / RTB-side stats.

**group_by:** `campaign`, `country`, `isp`, `domain`, `spaceid`.

**Metrics:** `requests`, `bids`, `wins`, `noresult`, `errors`,
`views`, `clicks`, `ctr`, `wpr`, `conversions`, `paid`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.stats_response import StatsResponse
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.goadserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.goadserver.com"
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
    api_instance = goadserver.StatsAdvertiserRTBApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = 'group_by_example' # str | Comma-separated dimensions to aggregate by, in priority order. Max 4 dimensions. Available dimensions vary per endpoint — see the per-endpoint description.  (optional)
    metrics = 'metrics_example' # str | Optional comma-separated metric whitelist. When omitted, all metrics for the endpoint are returned.  (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Field name. Prefix with `-` for descending (e.g. `-views`). (optional)

    try:
        # DSP / RTB-side stats.
        api_response = api_instance.api_v1_advertiser_rtb_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, format=format, page=page, per_page=per_page, sort=sort)
        print("The response of StatsAdvertiserRTBApi->api_v1_advertiser_rtb_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsAdvertiserRTBApi->api_v1_advertiser_rtb_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **interval** | **str**|  | [optional] [default to sum]
 **group_by** | **str**| Comma-separated dimensions to aggregate by, in priority order. Max 4 dimensions. Available dimensions vary per endpoint — see the per-endpoint description.  | [optional] 
 **metrics** | **str**| Optional comma-separated metric whitelist. When omitted, all metrics for the endpoint are returned.  | [optional] 
 **format** | **str**|  | [optional] [default to json]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Field name. Prefix with &#x60;-&#x60; for descending (e.g. &#x60;-views&#x60;). | [optional] 

### Return type

[**StatsResponse**](StatsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


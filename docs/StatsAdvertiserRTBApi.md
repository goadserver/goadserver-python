# goadserver.StatsAdvertiserRTBApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_advertiser_rtb_stats_get**](StatsAdvertiserRTBApi.md#api_v1_advertiser_rtb_stats_get) | **GET** /api/v1/advertiser/rtb/stats | DSP / RTB-side stats.


# **api_v1_advertiser_rtb_stats_get**
> StatsResponse api_v1_advertiser_rtb_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_campaign_id=filter_campaign_id, filter_network_id=filter_network_id, filter_ad_type=filter_ad_type, filter_device=filter_device, filter_country=filter_country, filter_spaceid=filter_spaceid, filter_isp_id=filter_isp_id, filter_domain_id=filter_domain_id, filter_site_id=filter_site_id, filter_ad_id=filter_ad_id, filter_os=filter_os, filter_browser=filter_browser, filter_conn_type=filter_conn_type, format=format, page=page, per_page=per_page, sort=sort, strict=strict)

DSP / RTB-side stats.

Bid-stream stats for the advertiser's RTB campaigns — the panel's
RTB Stats report (`dspstats_stats` / `dspstats_stats_sum`), same
sums and formulas.

**Money unit:** `paid` is in the account currency's main unit
(cents ÷ 100), rounded to 4 decimals. `avg_bidfloor` is the
average floor per request in main units — a CPM for
impression-billed ad types, a per-click price for click-billed
ones. `ctr`, `wpr`, `win_pct` and `bid_rate` are percentages.

**Dates:** `from` and `to` are used only when both are given;
otherwise the last 7 days. Max range 92 days. `interval=hour`
buckets on the bid timestamp (`YYYY-MM-DD HH:00`).

Not on this endpoint (panel-only): the per-error-code breakdown
and the merge of externally pulled network counters
(`nw_views`/`nw_clicks`/`nw_earned`).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.stats_response import StatsResponse
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
    api_instance = goadserver.StatsAdvertiserRTBApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = ['[\"campaign\",\"country\"]'] # List[str] | Dimensions to aggregate by. Multi-pick up to 8; unknown → 422. Each comes back as `{id, name}` (`country`: `{id: \"US\", name}`); `ad` and `site` carry the id as name. Without the `stats_source_names` right `name` equals the id.  | Dim | Meaning | |---|---| | `campaign` | RTB campaign | | `network` | RTB network (SSP) the request came from | | `ad_type` | ad type | | `device` | device type | | `country` | country | | `isp` | ISP / ASN | | `domain` | domain | | `spaceid` | publisher adzone id | | `site` | publisher site id | | `os` | operating system | | `browser` | browser | | `conn_type` | connection type | | `ad` | ad id |  (optional)
    metrics = ['metrics_example'] # List[str] | Metrics to return (comma-separated). Empty → the default set `requests, bids, wins, noresult, errors, views, clicks, ctr, wpr, paid`; `all` → every metric. Opt-in: `timeouts`, `skipnobids`, `skiptimeouts`, `win_pct` (wins / bids × 100), `bid_rate` (bids / requests × 100), `avg_bidfloor`, `avg_time` (average response time per request). `wpr` is wins / requests × 100. An unknown name is ignored and echoed in `ignored_metrics`; with `strict=1` it is a 422.  (optional)
    filter_campaign_id = 'filter_campaign_id_example' # str | RTB campaign ID, or a comma-separated list. (optional)
    filter_network_id = 56 # int | RTB network ID. (optional)
    filter_ad_type = 56 # int | Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  (optional)
    filter_device = 56 # int | Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  (optional)
    filter_country = 'US' # str | ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`). (optional)
    filter_spaceid = 56 # int | Adspace ID. (optional)
    filter_isp_id = 'filter_isp_id_example' # str | ISP / ASN id, or a comma-separated list. (optional)
    filter_domain_id = 'filter_domain_id_example' # str | Domain id, or a comma-separated list. (optional)
    filter_site_id = 'filter_site_id_example' # str | Publisher site id, or a comma-separated list. (optional)
    filter_ad_id = 'filter_ad_id_example' # str | Ad id, or a comma-separated list. (optional)
    filter_os = 'filter_os_example' # str | Operating-system id (`GET /api/v1/lookups/operating-systems`), or a comma-separated list. (optional)
    filter_browser = 'filter_browser_example' # str | Browser id (`GET /api/v1/lookups/browsers`), or a comma-separated list. (optional)
    filter_conn_type = 'filter_conn_type_example' # str | Connection-type id, or a comma-separated list. (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = '-paid' # str | Sort key, `-` prefix for descending: `requests`, `bids`, `wins`, `noresult`, `errors`, `views`, `clicks`, `paid`, `timeouts`, `skipnobids`, `skiptimeouts`, `ctr`, `wpr`, `win_pct`, `bid_rate`, `date` (non-`sum` interval only). Any other value falls back to `-paid`.  (optional) (default to '-paid')
    strict = 'strict_example' # str | `1` turns an unknown metric name into a 422 instead of ignoring it. (optional)

    try:
        # DSP / RTB-side stats.
        api_response = api_instance.api_v1_advertiser_rtb_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_campaign_id=filter_campaign_id, filter_network_id=filter_network_id, filter_ad_type=filter_ad_type, filter_device=filter_device, filter_country=filter_country, filter_spaceid=filter_spaceid, filter_isp_id=filter_isp_id, filter_domain_id=filter_domain_id, filter_site_id=filter_site_id, filter_ad_id=filter_ad_id, filter_os=filter_os, filter_browser=filter_browser, filter_conn_type=filter_conn_type, format=format, page=page, per_page=per_page, sort=sort, strict=strict)
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
 **group_by** | [**List[str]**](str.md)| Dimensions to aggregate by. Multi-pick up to 8; unknown → 422. Each comes back as &#x60;{id, name}&#x60; (&#x60;country&#x60;: &#x60;{id: \&quot;US\&quot;, name}&#x60;); &#x60;ad&#x60; and &#x60;site&#x60; carry the id as name. Without the &#x60;stats_source_names&#x60; right &#x60;name&#x60; equals the id.  | Dim | Meaning | |---|---| | &#x60;campaign&#x60; | RTB campaign | | &#x60;network&#x60; | RTB network (SSP) the request came from | | &#x60;ad_type&#x60; | ad type | | &#x60;device&#x60; | device type | | &#x60;country&#x60; | country | | &#x60;isp&#x60; | ISP / ASN | | &#x60;domain&#x60; | domain | | &#x60;spaceid&#x60; | publisher adzone id | | &#x60;site&#x60; | publisher site id | | &#x60;os&#x60; | operating system | | &#x60;browser&#x60; | browser | | &#x60;conn_type&#x60; | connection type | | &#x60;ad&#x60; | ad id |  | [optional] 
 **metrics** | [**List[str]**](str.md)| Metrics to return (comma-separated). Empty → the default set &#x60;requests, bids, wins, noresult, errors, views, clicks, ctr, wpr, paid&#x60;; &#x60;all&#x60; → every metric. Opt-in: &#x60;timeouts&#x60;, &#x60;skipnobids&#x60;, &#x60;skiptimeouts&#x60;, &#x60;win_pct&#x60; (wins / bids × 100), &#x60;bid_rate&#x60; (bids / requests × 100), &#x60;avg_bidfloor&#x60;, &#x60;avg_time&#x60; (average response time per request). &#x60;wpr&#x60; is wins / requests × 100. An unknown name is ignored and echoed in &#x60;ignored_metrics&#x60;; with &#x60;strict&#x3D;1&#x60; it is a 422.  | [optional] 
 **filter_campaign_id** | **str**| RTB campaign ID, or a comma-separated list. | [optional] 
 **filter_network_id** | **int**| RTB network ID. | [optional] 
 **filter_ad_type** | **int**| Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  | [optional] 
 **filter_device** | **int**| Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  | [optional] 
 **filter_country** | **str**| ISO-3166 alpha-2 country code (e.g. &#x60;US&#x60;, &#x60;DE&#x60;, &#x60;BR&#x60;). | [optional] 
 **filter_spaceid** | **int**| Adspace ID. | [optional] 
 **filter_isp_id** | **str**| ISP / ASN id, or a comma-separated list. | [optional] 
 **filter_domain_id** | **str**| Domain id, or a comma-separated list. | [optional] 
 **filter_site_id** | **str**| Publisher site id, or a comma-separated list. | [optional] 
 **filter_ad_id** | **str**| Ad id, or a comma-separated list. | [optional] 
 **filter_os** | **str**| Operating-system id (&#x60;GET /api/v1/lookups/operating-systems&#x60;), or a comma-separated list. | [optional] 
 **filter_browser** | **str**| Browser id (&#x60;GET /api/v1/lookups/browsers&#x60;), or a comma-separated list. | [optional] 
 **filter_conn_type** | **str**| Connection-type id, or a comma-separated list. | [optional] 
 **format** | **str**|  | [optional] [default to json]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sort key, &#x60;-&#x60; prefix for descending: &#x60;requests&#x60;, &#x60;bids&#x60;, &#x60;wins&#x60;, &#x60;noresult&#x60;, &#x60;errors&#x60;, &#x60;views&#x60;, &#x60;clicks&#x60;, &#x60;paid&#x60;, &#x60;timeouts&#x60;, &#x60;skipnobids&#x60;, &#x60;skiptimeouts&#x60;, &#x60;ctr&#x60;, &#x60;wpr&#x60;, &#x60;win_pct&#x60;, &#x60;bid_rate&#x60;, &#x60;date&#x60; (non-&#x60;sum&#x60; interval only). Any other value falls back to &#x60;-paid&#x60;.  | [optional] [default to &#39;-paid&#39;]
 **strict** | **str**| &#x60;1&#x60; turns an unknown metric name into a 422 instead of ignoring it. | [optional] 

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
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Bad date range, unknown &#x60;group_by&#x60; / &#x60;interval&#x60;, or (with &#x60;strict&#x3D;1&#x60;) an unknown metric. |  -  |
**429** | Per-key rate limit exceeded (default 60 rpm). Retry after &#x60;Retry-After&#x60; seconds. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


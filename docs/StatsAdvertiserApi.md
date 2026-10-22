# goadserver.StatsAdvertiserApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_advertiser_stats_get**](StatsAdvertiserApi.md#api_v1_advertiser_stats_get) | **GET** /api/v1/advertiser/stats | Display, native and CPM/RON campaign stats.


# **api_v1_advertiser_stats_get**
> StatsResponse api_v1_advertiser_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_campaign_id=filter_campaign_id, filter_ad_id=filter_ad_id, filter_tag_id=filter_tag_id, filter_ad_type=filter_ad_type, filter_selling_type=filter_selling_type, filter_adzone_type=filter_adzone_type, filter_device=filter_device, filter_country=filter_country, filter_adzone_id=filter_adzone_id, filter_site_id=filter_site_id, filter_network_id=filter_network_id, filter_bidruleset_id=filter_bidruleset_id, filter_bidrule_id=filter_bidrule_id, filter_creative_pool_id=filter_creative_pool_id, filter_creative_pool_ad_id=filter_creative_pool_ad_id, format=format, page=page, per_page=per_page, sort=sort, min=min, max=max, strict=strict)

Display, native and CPM/RON campaign stats.

Aggregated performance for the advertiser's campaigns. Pick the
dimensions to group by, the metrics you want returned, and any
filters — the form below auto-builds the query.

The numbers are the panel's Stats screen numbers: the same
aggregate and the same formulas (revenue, profit, ROI, CPA, CR,
eCPC, traffic cost and the bot breakdown included), over
`userstats_daily` (or `userstats_daily_details` when a grouped
dimension or filter needs it).

**Money unit:** every money metric (`paid`, `cpm_paid`, `cpc_paid`,
`ecpm`, `ecpc`, `conv_*_earned`, `revenue`, `profit`, `cpa`,
`traffic_cost`) is in the account currency's **main unit**
(dollars/euros, not cents), rounded to 4 decimals. `ctr`, `cr`,
`roi` and the `bot_*_pct` metrics are percentages.

**Dates:** `from` and `to` are used only when *both* are given and
valid; otherwise the range is the last 7 days ending today
(a lone `from` is ignored). Max range 92 days.

A key made by a team member whose role is limited to their own
campaigns sees only those campaigns, as in the panel. A key
pinned to campaigns sees only those campaigns.

**Several values:** `filter[ad_type]`, `filter[device]` and
`filter[country]` also take a comma-separated list
(`filter[country]=NL,DE`), matching any of them — the panel's
multi-select filters send the same.


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
    api_instance = goadserver.StatsAdvertiserApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = ['[\"campaign\",\"country\"]'] # List[str] | Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (`subid`, `sid1`–`sid5`, `domain`) explode row count — pair with `from`/`to`/pagination. An unknown dimension is a 422.  `sid1`–`sid5` are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone `sid1` holds the visitor's search; a network can keep those terms admin-only, and then Search Ads rows report an empty `sid1`. `creative_pool` / `url_pool` group by the pool an ad drew from, `creative_pool_ad` / `url_pool_ad` by the individual pool item. `adzone_type` is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). `selling_type` groups by pay type (see `filter[selling_type]` for the ids).  Each grouped dimension comes back as an `{id, name}` object, except `country`, `domain` and `subid`, which are plain strings. Without the `stats_source_names` right `name` equals the id.  (optional)
    metrics = ['[\"views\",\"clicks\",\"paid\",\"revenue\",\"profit\",\"roi\"]'] # List[str] | Metrics to return (comma-separated). **Empty** returns the default set `views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c` (unchanged since launch). `all` returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | `ecpm` | blended: `paid` / `views` × 1000 | | `ecpc` | CPC spend / CPC clicks (click-billed ad types only) | | `cpm_views`, `cpm_paid` | views / spend on impression-billed ad types | | `cpc_clicks`, `cpc_paid` | clicks / spend on click-billed ad types | | `conv_a_earned` … `conv_c_earned` | conversion revenue per conversion type (the postback value) | | `revenue` | conversion revenue over the selected conversion types | | `profit` | `revenue` − cost (cost = `traffic_cost` when the row carries one, else `paid`) | | `roi` | `profit` / cost × 100; `null` when cost < 1.00 | | `cpa` | `paid` / conversions of the selected types | | `cr` | conversions of the selected types / `clicks` × 100 | | `traffic_cost` | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network's own buying cost: network admins only, an advertiser key gets a 422 and `all` leaves it out) | | `nw_views`, `nw_clicks` | the ad network's own counters for that traffic — same rule as `traffic_cost` | | `bot_views`, `bot_clicks`, `bot_views_pct`, `bot_clicks_pct`, `bot_unknown`, `bot_click`, `bot_impression`, `bot_conversion`, `bot_web`, `bot_high_frequency`, `bot_artificial_ip`, `bot_adspace_abuse`, `bot_suspicious`, `bot_datacenter`, `bot_vpn` | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \"Selected conversion types\" are the `conv_a`/`conv_b`/`conv_c` metrics in this request; with none of them requested, `revenue`/`cpa`/`cr` cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response's `ignored_metrics`; with `strict=1` it is a 422.  (optional)
    filter_campaign_id = '123,124' # str | Campaign ID, or a comma-separated list. Look up via `GET /api/v1/campaigns`. (optional)
    filter_ad_id = 'filter_ad_id_example' # str | Ad ID, or a comma-separated list. (optional)
    filter_tag_id = 'filter_tag_id_example' # str | Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing.  (optional)
    filter_ad_type = 56 # int | Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  (optional)
    filter_selling_type = '2' # str | Pay type (the campaign's pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id = the tenant's `bid_types` id + 1; the ids above are the standard set.)  (optional)
    filter_adzone_type = 'filter_adzone_type_example' # str | Adzone (placement) type id, or a comma-separated list. (optional)
    filter_device = 56 # int | Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  (optional)
    filter_country = 'US' # str | ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`). (optional)
    filter_adzone_id = '12345,12346' # str | Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`. (optional)
    filter_site_id = 'filter_site_id_example' # str | Comma-separated site IDs. Look up via `GET /api/v1/sites`. (optional)
    filter_network_id = 56 # int | RTB network ID. (optional)
    filter_bidruleset_id = 56 # int | Bid ruleset ID — only traffic bid through that ruleset (`GET /api/v1/bid-rulesets`). (optional)
    filter_bidrule_id = 56 # int | Bid rule ID inside a ruleset — only traffic that rule priced. (optional)
    filter_creative_pool_id = 56 # int | Creative pool ID. (optional)
    filter_creative_pool_ad_id = 56 # int | Creative pool item ID. (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = '-paid' # str | Sort key, `-` prefix for descending. One of `views`, `clicks`, `ctr`, `paid`, `ecpm`, `ecpc`, `conv_a`, `conv_b`, `conv_c`, `conv_a_earned`, `conv_b_earned`, `conv_c_earned`, `revenue`, `traffic_cost`, `nw_views`, `nw_clicks` (where those metrics are available, see `metrics`), `date` (only with a non-`sum` interval); admins also `bot_views`, `bot_clicks`. Any other value falls back to the default, `-paid`.  (optional) (default to '-paid')
    min = {'key': {"cpa":10}} # Dict[str, float] | Keep only rows whose metric is at least this value, as `min[<metric>]=<number>` — e.g. `min[cpa]=10`. Pair with `max[<metric>]` for a range (both ends inclusive). Any metric `metrics` accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (`roi` below 1.00 of spend) is dropped. Money in main currency units, `ctr` in percent. Same as the comparisons (`>10`, `<200`, `10-200`) in the panel's statistics details column search.  With a bound set, up to 10,000 grouped rows (in `sort` order) are tested and the survivors paginated; `total_rows` counts the survivors, `totals` stay over the whole selection, and `range_scan_truncated: true` says more rows existed than were tested. Unknown metric, non-number or min > max → 422.  (optional)
    max = {'key': {"cpa":200}} # Dict[str, float] | Keep only rows whose metric is at most this value, as `max[<metric>]=<number>`. See `min`. (optional)
    strict = 'strict_example' # str | `1` turns an unknown metric name into a 422 instead of ignoring it. (optional)

    try:
        # Display, native and CPM/RON campaign stats.
        api_response = api_instance.api_v1_advertiser_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_campaign_id=filter_campaign_id, filter_ad_id=filter_ad_id, filter_tag_id=filter_tag_id, filter_ad_type=filter_ad_type, filter_selling_type=filter_selling_type, filter_adzone_type=filter_adzone_type, filter_device=filter_device, filter_country=filter_country, filter_adzone_id=filter_adzone_id, filter_site_id=filter_site_id, filter_network_id=filter_network_id, filter_bidruleset_id=filter_bidruleset_id, filter_bidrule_id=filter_bidrule_id, filter_creative_pool_id=filter_creative_pool_id, filter_creative_pool_ad_id=filter_creative_pool_ad_id, format=format, page=page, per_page=per_page, sort=sort, min=min, max=max, strict=strict)
        print("The response of StatsAdvertiserApi->api_v1_advertiser_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsAdvertiserApi->api_v1_advertiser_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **interval** | **str**|  | [optional] [default to sum]
 **group_by** | [**List[str]**](str.md)| Dimensions to aggregate by, in priority order. Multi-pick up to 8. High-cardinality dims (&#x60;subid&#x60;, &#x60;sid1&#x60;–&#x60;sid5&#x60;, &#x60;domain&#x60;) explode row count — pair with &#x60;from&#x60;/&#x60;to&#x60;/pagination. An unknown dimension is a 422.  &#x60;sid1&#x60;–&#x60;sid5&#x60; are the named custom-parameter slots the tracker records per click; their labels are whatever this account configured. On a Search Ads zone &#x60;sid1&#x60; holds the visitor&#39;s search; a network can keep those terms admin-only, and then Search Ads rows report an empty &#x60;sid1&#x60;. &#x60;creative_pool&#x60; / &#x60;url_pool&#x60; group by the pool an ad drew from, &#x60;creative_pool_ad&#x60; / &#x60;url_pool_ad&#x60; by the individual pool item. &#x60;adzone_type&#x60; is the ad placement (e.g. in-page video vs VAST pre-roll on the same video ad type). &#x60;selling_type&#x60; groups by pay type (see &#x60;filter[selling_type]&#x60; for the ids).  Each grouped dimension comes back as an &#x60;{id, name}&#x60; object, except &#x60;country&#x60;, &#x60;domain&#x60; and &#x60;subid&#x60;, which are plain strings. Without the &#x60;stats_source_names&#x60; right &#x60;name&#x60; equals the id.  | [optional] 
 **metrics** | [**List[str]**](str.md)| Metrics to return (comma-separated). **Empty** returns the default set &#x60;views, clicks, ctr, ecpm, paid, conv_a, conv_b, conv_c&#x60; (unchanged since launch). &#x60;all&#x60; returns every metric this caller may read. Everything else is opt-in by name:  | Metric | Meaning | |---|---| | &#x60;ecpm&#x60; | blended: &#x60;paid&#x60; / &#x60;views&#x60; × 1000 | | &#x60;ecpc&#x60; | CPC spend / CPC clicks (click-billed ad types only) | | &#x60;cpm_views&#x60;, &#x60;cpm_paid&#x60; | views / spend on impression-billed ad types | | &#x60;cpc_clicks&#x60;, &#x60;cpc_paid&#x60; | clicks / spend on click-billed ad types | | &#x60;conv_a_earned&#x60; … &#x60;conv_c_earned&#x60; | conversion revenue per conversion type (the postback value) | | &#x60;revenue&#x60; | conversion revenue over the selected conversion types | | &#x60;profit&#x60; | &#x60;revenue&#x60; − cost (cost &#x3D; &#x60;traffic_cost&#x60; when the row carries one, else &#x60;paid&#x60;) | | &#x60;roi&#x60; | &#x60;profit&#x60; / cost × 100; &#x60;null&#x60; when cost &lt; 1.00 | | &#x60;cpa&#x60; | &#x60;paid&#x60; / conversions of the selected types | | &#x60;cr&#x60; | conversions of the selected types / &#x60;clicks&#x60; × 100 | | &#x60;traffic_cost&#x60; | traffic-acquisition cost pulled from a bound ad network — **ad manager accounts only** (on an ad network it is the network&#39;s own buying cost: network admins only, an advertiser key gets a 422 and &#x60;all&#x60; leaves it out) | | &#x60;nw_views&#x60;, &#x60;nw_clicks&#x60; | the ad network&#39;s own counters for that traffic — same rule as &#x60;traffic_cost&#x60; | | &#x60;bot_views&#x60;, &#x60;bot_clicks&#x60;, &#x60;bot_views_pct&#x60;, &#x60;bot_clicks_pct&#x60;, &#x60;bot_unknown&#x60;, &#x60;bot_click&#x60;, &#x60;bot_impression&#x60;, &#x60;bot_conversion&#x60;, &#x60;bot_web&#x60;, &#x60;bot_high_frequency&#x60;, &#x60;bot_artificial_ip&#x60;, &#x60;bot_adspace_abuse&#x60;, &#x60;bot_suspicious&#x60;, &#x60;bot_datacenter&#x60;, &#x60;bot_vpn&#x60; | bot breakdown — **network admins only** (as in the panel); an advertiser key asking for one gets a 422 |  \&quot;Selected conversion types\&quot; are the &#x60;conv_a&#x60;/&#x60;conv_b&#x60;/&#x60;conv_c&#x60; metrics in this request; with none of them requested, &#x60;revenue&#x60;/&#x60;cpa&#x60;/&#x60;cr&#x60; cover all three (same rule as the panel).  An unknown metric name is ignored and listed in the response&#39;s &#x60;ignored_metrics&#x60;; with &#x60;strict&#x3D;1&#x60; it is a 422.  | [optional] 
 **filter_campaign_id** | **str**| Campaign ID, or a comma-separated list. Look up via &#x60;GET /api/v1/campaigns&#x60;. | [optional] 
 **filter_ad_id** | **str**| Ad ID, or a comma-separated list. | [optional] 
 **filter_tag_id** | **str**| Campaign group (tag) ID, or a comma-separated list — resolves to the campaigns in those groups, sub-groups included. A group with no campaigns returns nothing.  | [optional] 
 **filter_ad_type** | **int**| Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  | [optional] 
 **filter_selling_type** | **str**| Pay type (the campaign&#39;s pricing model), one id or a comma-separated list:  | ID | Pay type | |----|----------| | 1  | CPC | | 2  | CPM | | 3  | CPA | | 5  | SmartAds | | 6  | Flat rate |  (Pay-type id &#x3D; the tenant&#39;s &#x60;bid_types&#x60; id + 1; the ids above are the standard set.)  | [optional] 
 **filter_adzone_type** | **str**| Adzone (placement) type id, or a comma-separated list. | [optional] 
 **filter_device** | **int**| Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  | [optional] 
 **filter_country** | **str**| ISO-3166 alpha-2 country code (e.g. &#x60;US&#x60;, &#x60;DE&#x60;, &#x60;BR&#x60;). | [optional] 
 **filter_adzone_id** | **str**| Adspace ID, or comma-separated list. Look up via &#x60;GET /api/v1/adspaces&#x60;. | [optional] 
 **filter_site_id** | **str**| Comma-separated site IDs. Look up via &#x60;GET /api/v1/sites&#x60;. | [optional] 
 **filter_network_id** | **int**| RTB network ID. | [optional] 
 **filter_bidruleset_id** | **int**| Bid ruleset ID — only traffic bid through that ruleset (&#x60;GET /api/v1/bid-rulesets&#x60;). | [optional] 
 **filter_bidrule_id** | **int**| Bid rule ID inside a ruleset — only traffic that rule priced. | [optional] 
 **filter_creative_pool_id** | **int**| Creative pool ID. | [optional] 
 **filter_creative_pool_ad_id** | **int**| Creative pool item ID. | [optional] 
 **format** | **str**|  | [optional] [default to json]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sort key, &#x60;-&#x60; prefix for descending. One of &#x60;views&#x60;, &#x60;clicks&#x60;, &#x60;ctr&#x60;, &#x60;paid&#x60;, &#x60;ecpm&#x60;, &#x60;ecpc&#x60;, &#x60;conv_a&#x60;, &#x60;conv_b&#x60;, &#x60;conv_c&#x60;, &#x60;conv_a_earned&#x60;, &#x60;conv_b_earned&#x60;, &#x60;conv_c_earned&#x60;, &#x60;revenue&#x60;, &#x60;traffic_cost&#x60;, &#x60;nw_views&#x60;, &#x60;nw_clicks&#x60; (where those metrics are available, see &#x60;metrics&#x60;), &#x60;date&#x60; (only with a non-&#x60;sum&#x60; interval); admins also &#x60;bot_views&#x60;, &#x60;bot_clicks&#x60;. Any other value falls back to the default, &#x60;-paid&#x60;.  | [optional] [default to &#39;-paid&#39;]
 **min** | [**Dict[str, float]**](float.md)| Keep only rows whose metric is at least this value, as &#x60;min[&lt;metric&gt;]&#x3D;&lt;number&gt;&#x60; — e.g. &#x60;min[cpa]&#x3D;10&#x60;. Pair with &#x60;max[&lt;metric&gt;]&#x60; for a range (both ends inclusive). Any metric &#x60;metrics&#x60; accepts for this caller can be bounded, whether or not it is returned; several metrics combine with AND. A row with no value for the metric (&#x60;roi&#x60; below 1.00 of spend) is dropped. Money in main currency units, &#x60;ctr&#x60; in percent. Same as the comparisons (&#x60;&gt;10&#x60;, &#x60;&lt;200&#x60;, &#x60;10-200&#x60;) in the panel&#39;s statistics details column search.  With a bound set, up to 10,000 grouped rows (in &#x60;sort&#x60; order) are tested and the survivors paginated; &#x60;total_rows&#x60; counts the survivors, &#x60;totals&#x60; stay over the whole selection, and &#x60;range_scan_truncated: true&#x60; says more rows existed than were tested. Unknown metric, non-number or min &gt; max → 422.  | [optional] 
 **max** | [**Dict[str, float]**](float.md)| Keep only rows whose metric is at most this value, as &#x60;max[&lt;metric&gt;]&#x3D;&lt;number&gt;&#x60;. See &#x60;min&#x60;. | [optional] 
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
**200** | Stats response. Money in main currency units (see the endpoint description). &#x60;ignored_metrics&#x60; appears only when the request named metrics this endpoint does not know (lenient mode).  |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Bad date range, unknown &#x60;group_by&#x60; dimension or &#x60;interval&#x60;, a bot metric requested by a non-admin, or (with &#x60;strict&#x3D;1&#x60;) an unknown metric.  |  -  |
**429** | Per-key rate limit exceeded (default 60 rpm). Retry after &#x60;Retry-After&#x60; seconds. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


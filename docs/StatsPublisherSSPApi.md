# goadserver.StatsPublisherSSPApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_ssp_stats_details_get**](StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_details_get) | **GET** /api/v1/publisher/ssp/stats/details | SSP report broken down by one dimension.
[**api_v1_publisher_ssp_stats_filters_get**](StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_filters_get) | **GET** /api/v1/publisher/ssp/stats/filters | Filter values for the SSP reports.
[**api_v1_publisher_ssp_stats_flat_get**](StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_flat_get) | **GET** /api/v1/publisher/ssp/stats/flat | SSP report grouped by several dimensions.
[**api_v1_publisher_ssp_stats_get**](StatsPublisherSSPApi.md#api_v1_publisher_ssp_stats_get) | **GET** /api/v1/publisher/ssp/stats | SSP / smart-campaign earnings.


# **api_v1_publisher_ssp_stats_details_get**
> api_v1_publisher_ssp_stats_details_get(var_from=var_from, to=to, type=type, ssptype=ssptype, campaignid=campaignid, networkid=networkid, siteid=siteid, country=country, device_type=device_type, ad_type=ad_type, subid=subid, filter_bid_type=filter_bid_type)

SSP report broken down by one dimension.

The panel's SSP "details" console: one row per value of `type`
(`campaign`, `country`, `website`, `adzone`, `network`, `bid_type`,
`keyword`), with request/bid/win funnel, errors and timings.
Defaults to every SSP campaign of yours (narrow with `ssptype` or
`campaignid`). Capped rows report `truncated: true` + `row_cap`.
**Money is in currency units (not cents)**: `paid`, `ecpm`,
`avg_bidfloor`, `avg_cpm` (CPM) and `nw_earned`. `avg_resp_time` is
seconds. For campaign/country rows, `nw_views` / `nw_clicks` /
`nw_earned` carry what the partner's own API reported.


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
    api_instance = goadserver.StatsPublisherSSPApi(api_client)
    var_from = '2013-10-20' # date | Inclusive start. Defaults to 6 days ago (send both from and to). (optional)
    to = '2013-10-20' # date |  (optional)
    type = campaign # str |  (optional) (default to campaign)
    ssptype = 'ssptype_example' # str |  (optional)
    campaignid = [56] # List[int] | One or more SSP campaign ids (`campaignid=1&campaignid=2` or `campaignid[]=…`). (optional)
    networkid = [56] # List[int] |  (optional)
    siteid = [56] # List[int] |  (optional)
    country = ['country_example'] # List[str] | ISO-3166 alpha-2 codes. (optional)
    device_type = [56] # List[int] |  (optional)
    ad_type = [56] # List[int] |  (optional)
    subid = 'subid_example' # str |  (optional)
    filter_bid_type = 56 # int | Only this bid type. (optional)

    try:
        # SSP report broken down by one dimension.
        api_instance.api_v1_publisher_ssp_stats_details_get(var_from=var_from, to=to, type=type, ssptype=ssptype, campaignid=campaignid, networkid=networkid, siteid=siteid, country=country, device_type=device_type, ad_type=ad_type, subid=subid, filter_bid_type=filter_bid_type)
    except Exception as e:
        print("Exception when calling StatsPublisherSSPApi->api_v1_publisher_ssp_stats_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Inclusive start. Defaults to 6 days ago (send both from and to). | [optional] 
 **to** | **date**|  | [optional] 
 **type** | **str**|  | [optional] [default to campaign]
 **ssptype** | **str**|  | [optional] 
 **campaignid** | [**List[int]**](int.md)| One or more SSP campaign ids (&#x60;campaignid&#x3D;1&amp;campaignid&#x3D;2&#x60; or &#x60;campaignid[]&#x3D;…&#x60;). | [optional] 
 **networkid** | [**List[int]**](int.md)|  | [optional] 
 **siteid** | [**List[int]**](int.md)|  | [optional] 
 **country** | [**List[str]**](str.md)| ISO-3166 alpha-2 codes. | [optional] 
 **device_type** | [**List[int]**](int.md)|  | [optional] 
 **ad_type** | [**List[int]**](int.md)|  | [optional] 
 **subid** | **str**|  | [optional] 
 **filter_bid_type** | **int**| Only this bid type. | [optional] 

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
**200** | Rows. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_stats_filters_get**
> api_v1_publisher_ssp_stats_filters_get()

Filter values for the SSP reports.

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
    api_instance = goadserver.StatsPublisherSSPApi(api_client)

    try:
        # Filter values for the SSP reports.
        api_instance.api_v1_publisher_ssp_stats_filters_get()
    except Exception as e:
        print("Exception when calling StatsPublisherSSPApi->api_v1_publisher_ssp_stats_filters_get: %s\n" % e)
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
**200** | &#x60;{id, name}&#x60; lists for the filter parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_stats_flat_get**
> api_v1_publisher_ssp_stats_flat_get(var_from=var_from, to=to, group=group, viewtype=viewtype, ssptype=ssptype, campaignid=campaignid, networkid=networkid, siteid=siteid, country=country, device_type=device_type, ad_type=ad_type, subid=subid, filter_bid_type=filter_bid_type)

SSP report grouped by several dimensions.

The panel's flat SSP table. `group` is a comma-separated list of
`date`, `campaign`, `country`, `website`, `adzone`, `subid`,
`domainid`, `bid_type`, `bid_advid`, `bid_cid`, `bid_adid`,
`mxispid` (default `date`); each row carries the grouped values
plus `<dim>_name` where a name exists, and `startdate`/`enddate`
for the row's period. `viewtype` sets the date bucket. At most
10,000 rows. Same filters and money units as `stats/details`
(**currency units, not cents**). `totals` sums the whole result.


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
    api_instance = goadserver.StatsPublisherSSPApi(api_client)
    var_from = '2013-10-20' # date |  (optional)
    to = '2013-10-20' # date |  (optional)
    group = 'date' # str |  (optional) (default to 'date')
    viewtype = day # str |  (optional) (default to day)
    ssptype = 'ssptype_example' # str |  (optional)
    campaignid = [56] # List[int] |  (optional)
    networkid = [56] # List[int] |  (optional)
    siteid = [56] # List[int] |  (optional)
    country = ['country_example'] # List[str] |  (optional)
    device_type = [56] # List[int] |  (optional)
    ad_type = [56] # List[int] |  (optional)
    subid = 'subid_example' # str |  (optional)
    filter_bid_type = 56 # int |  (optional)

    try:
        # SSP report grouped by several dimensions.
        api_instance.api_v1_publisher_ssp_stats_flat_get(var_from=var_from, to=to, group=group, viewtype=viewtype, ssptype=ssptype, campaignid=campaignid, networkid=networkid, siteid=siteid, country=country, device_type=device_type, ad_type=ad_type, subid=subid, filter_bid_type=filter_bid_type)
    except Exception as e:
        print("Exception when calling StatsPublisherSSPApi->api_v1_publisher_ssp_stats_flat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **group** | **str**|  | [optional] [default to &#39;date&#39;]
 **viewtype** | **str**|  | [optional] [default to day]
 **ssptype** | **str**|  | [optional] 
 **campaignid** | [**List[int]**](int.md)|  | [optional] 
 **networkid** | [**List[int]**](int.md)|  | [optional] 
 **siteid** | [**List[int]**](int.md)|  | [optional] 
 **country** | [**List[str]**](str.md)|  | [optional] 
 **device_type** | [**List[int]**](int.md)|  | [optional] 
 **ad_type** | [**List[int]**](int.md)|  | [optional] 
 **subid** | **str**|  | [optional] 
 **filter_bid_type** | **int**|  | [optional] 

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
**200** | Rows + totals. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_stats_get**
> StatsResponse api_v1_publisher_ssp_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_feed_id=filter_feed_id, filter_campaign_id=filter_campaign_id, filter_ssptype=filter_ssptype, filter_country=filter_country, filter_device=filter_device, filter_ad_type=filter_ad_type, filter_network_id=filter_network_id, filter_adzone_id=filter_adzone_id, filter_website=filter_website, format=format, page=page, per_page=per_page, sort=sort)

SSP / smart-campaign earnings.

SSP / smart-campaign earnings.

**Scoping (priority order):**
1. `filter[feed_id]` — the SSP feed hash from the campaign row
   (the public identifier you give to ad networks). Limits results
   to one campaign without exposing the internal numeric ID.
2. `filter[campaign_id]` — internal numeric ID.
3. (default) every SSP campaign owned by the caller, optionally
   narrowed with `filter[ssptype]`.

**Authentication — this endpoint accepts two credentials.** Either an
account API key with the `stats.read` scope in the `Authorization`
header, as everywhere else on this API, or the feed hash itself in
`filter[feed_id]` (`token` is accepted as an alias, matching the legacy
`/apitool/ssp_stats/` URL). The feed hash authenticates nothing but this
report for that one feed, which is what makes the URL safe to hand to an
ad network; an account key covers every feed on the account. When an
`Authorization` header is present it is always used, so an invalid key
is reported as such rather than falling back to the feed hash.


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
    api_instance = goadserver.StatsPublisherSSPApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = ['[\"campaign\",\"country\"]'] # List[str] | Dimensions to aggregate by. Multi-pick up to 8. (optional)
    metrics = ['metrics_example'] # List[str] | Metrics to return. Multi-pick — leave empty for all. (optional)
    filter_feed_id = 'filter_feed_id_example' # str | SSP campaign feed hash (the public identifier given to ad networks). Pins results to one SSP campaign without exposing the internal numeric ID.  (optional)
    filter_campaign_id = 56 # int | Campaign ID. Look up via `GET /api/v1/campaigns`. (optional)
    filter_ssptype = 'filter_ssptype_example' # str | SSP feed type filter. (optional)
    filter_country = 'US' # str | ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`). (optional)
    filter_device = 56 # int | Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  (optional)
    filter_ad_type = 56 # int | Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  (optional)
    filter_network_id = 56 # int | RTB network ID. (optional)
    filter_adzone_id = 56 # int | One adspace id — look up via `GET /api/v1/adspaces`. (optional)
    filter_website = 56 # int | Site ID — look up via `GET /api/v1/sites`. (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Field name. Prefix with `-` for descending (e.g. `-views`). (optional)

    try:
        # SSP / smart-campaign earnings.
        api_response = api_instance.api_v1_publisher_ssp_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_feed_id=filter_feed_id, filter_campaign_id=filter_campaign_id, filter_ssptype=filter_ssptype, filter_country=filter_country, filter_device=filter_device, filter_ad_type=filter_ad_type, filter_network_id=filter_network_id, filter_adzone_id=filter_adzone_id, filter_website=filter_website, format=format, page=page, per_page=per_page, sort=sort)
        print("The response of StatsPublisherSSPApi->api_v1_publisher_ssp_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsPublisherSSPApi->api_v1_publisher_ssp_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **interval** | **str**|  | [optional] [default to sum]
 **group_by** | [**List[str]**](str.md)| Dimensions to aggregate by. Multi-pick up to 8. | [optional] 
 **metrics** | [**List[str]**](str.md)| Metrics to return. Multi-pick — leave empty for all. | [optional] 
 **filter_feed_id** | **str**| SSP campaign feed hash (the public identifier given to ad networks). Pins results to one SSP campaign without exposing the internal numeric ID.  | [optional] 
 **filter_campaign_id** | **int**| Campaign ID. Look up via &#x60;GET /api/v1/campaigns&#x60;. | [optional] 
 **filter_ssptype** | **str**| SSP feed type filter. | [optional] 
 **filter_country** | **str**| ISO-3166 alpha-2 country code (e.g. &#x60;US&#x60;, &#x60;DE&#x60;, &#x60;BR&#x60;). | [optional] 
 **filter_device** | **int**| Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  | [optional] 
 **filter_ad_type** | **int**| Ad-type ID. Available types are tenant-specific (banner, popunder, native, video, push, …); the dropdown shows the types active on your system.  | [optional] 
 **filter_network_id** | **int**| RTB network ID. | [optional] 
 **filter_adzone_id** | **int**| One adspace id — look up via &#x60;GET /api/v1/adspaces&#x60;. | [optional] 
 **filter_website** | **int**| Site ID — look up via &#x60;GET /api/v1/sites&#x60;. | [optional] 
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


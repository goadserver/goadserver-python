# goadserver.StatsAffiliateApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_offers_postback_log_get**](StatsAffiliateApi.md#api_v1_publisher_offers_postback_log_get) | **GET** /api/v1/publisher/offers/postback-log | Postback log — the conversion postbacks fired to your URLs.
[**api_v1_publisher_offers_stats_get**](StatsAffiliateApi.md#api_v1_publisher_offers_stats_get) | **GET** /api/v1/publisher/offers/stats | Affiliate / smartlink offer performance — publisher side.


# **api_v1_publisher_offers_postback_log_get**
> ApiV1PublisherOffersPostbackLogGet200Response api_v1_publisher_offers_postback_log_get(var_from=var_from, to=to, site_id=site_id)

Postback log — the conversion postbacks fired to your URLs.

The panel's Offer Reports → Postback Log. One row per postback the
platform fired to the publisher's postback URL, newest first,
capped at 1000 rows (no paging). `status` is `Success` for HTTP
200 (or an unrecorded state) and `Failed (<state>)` otherwise.
Date params that are missing or not `YYYY-MM-DD` fall back to the
last 7 days.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response import ApiV1PublisherOffersPostbackLogGet200Response
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
    api_instance = goadserver.StatsAffiliateApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    site_id = 56 # int | Only postbacks for this site. (optional)

    try:
        # Postback log — the conversion postbacks fired to your URLs.
        api_response = api_instance.api_v1_publisher_offers_postback_log_get(var_from=var_from, to=to, site_id=site_id)
        print("The response of StatsAffiliateApi->api_v1_publisher_offers_postback_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsAffiliateApi->api_v1_publisher_offers_postback_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **site_id** | **int**| Only postbacks for this site. | [optional] 

### Return type

[**ApiV1PublisherOffersPostbackLogGet200Response**](ApiV1PublisherOffersPostbackLogGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Postback log rows (empty &#x60;data&#x60; on a query failure too). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_offers_stats_get**
> StatsResponse api_v1_publisher_offers_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_offer_id=filter_offer_id, filter_offer_type_id=filter_offer_type_id, filter_website=filter_website, filter_adzone_id=filter_adzone_id, filter_device=filter_device, filter_country=filter_country, filter_subid=filter_subid, format=format, page=page, per_page=per_page, sort=sort)

Affiliate / smartlink offer performance — publisher side.

Affiliate / smartlink offer performance for the publisher.
`earned` and `epc` are in the account currency (currency units,
not cents).


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
    api_instance = goadserver.StatsAffiliateApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = ['[\"offer\",\"country\"]'] # List[str] | Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text.  (optional)
    metrics = ['metrics_example'] # List[str] | Metrics to return. Multi-pick — leave empty for all. (optional)
    filter_offer_id = 56 # int | Offer ID. Look up via `GET /api/v1/offers`. (optional)
    filter_offer_type_id = 56 # int | Offer-type ID. (optional)
    filter_website = 56 # int | Site ID — look up via `GET /api/v1/sites`. (optional)
    filter_adzone_id = '12345,12346' # str | Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`. (optional)
    filter_device = 56 # int | Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  (optional)
    filter_country = 'US' # str | ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`). (optional)
    filter_subid = 'filter_subid_example' # str | SubID (free-form publisher identifier). (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Field name. Prefix with `-` for descending (e.g. `-views`). (optional)

    try:
        # Affiliate / smartlink offer performance — publisher side.
        api_response = api_instance.api_v1_publisher_offers_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_offer_id=filter_offer_id, filter_offer_type_id=filter_offer_type_id, filter_website=filter_website, filter_adzone_id=filter_adzone_id, filter_device=filter_device, filter_country=filter_country, filter_subid=filter_subid, format=format, page=page, per_page=per_page, sort=sort)
        print("The response of StatsAffiliateApi->api_v1_publisher_offers_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsAffiliateApi->api_v1_publisher_offers_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **interval** | **str**|  | [optional] [default to sum]
 **group_by** | [**List[str]**](str.md)| Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (&#x60;subid&#x60;, &#x60;clickid&#x60;, &#x60;sid*&#x60;, &#x60;domain&#x60;) explode row count. &#x60;clickid&#x60; is the advertiser-side click id passed back on the conversion (the panel&#39;s ClickID tab) and comes back as plain text.  | [optional] 
 **metrics** | [**List[str]**](str.md)| Metrics to return. Multi-pick — leave empty for all. | [optional] 
 **filter_offer_id** | **int**| Offer ID. Look up via &#x60;GET /api/v1/offers&#x60;. | [optional] 
 **filter_offer_type_id** | **int**| Offer-type ID. | [optional] 
 **filter_website** | **int**| Site ID — look up via &#x60;GET /api/v1/sites&#x60;. | [optional] 
 **filter_adzone_id** | **str**| Adspace ID, or comma-separated list. Look up via &#x60;GET /api/v1/adspaces&#x60;. | [optional] 
 **filter_device** | **int**| Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  | [optional] 
 **filter_country** | **str**| ISO-3166 alpha-2 country code (e.g. &#x60;US&#x60;, &#x60;DE&#x60;, &#x60;BR&#x60;). | [optional] 
 **filter_subid** | **str**| SubID (free-form publisher identifier). | [optional] 
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


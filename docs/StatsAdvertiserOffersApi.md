# goadserver.StatsAdvertiserOffersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_advertiser_offers_stats_get**](StatsAdvertiserOffersApi.md#api_v1_advertiser_offers_stats_get) | **GET** /api/v1/advertiser/offers/stats | CPA / affiliate offer performance — advertiser side.


# **api_v1_advertiser_offers_stats_get**
> StatsResponse api_v1_advertiser_offers_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_offer_id=filter_offer_id, filter_offer_type_id=filter_offer_type_id, filter_device=filter_device, filter_country=filter_country, format=format, page=page, per_page=per_page, sort=sort)

CPA / affiliate offer performance — advertiser side.

Performance for the advertiser's CPA / affiliate offers.


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
    api_instance = goadserver.StatsAdvertiserOffersApi(api_client)
    var_from = '2013-10-20' # date | ISO date — inclusive start. Defaults to 7 days ago. (optional)
    to = '2013-10-20' # date | ISO date — inclusive end. Defaults to today. Max range 92 days. (optional)
    interval = sum # str |  (optional) (default to sum)
    group_by = ['[\"offer\",\"country\"]'] # List[str] | Dimensions to aggregate by. Multi-pick up to 8. (optional)
    metrics = ['metrics_example'] # List[str] | Metrics to return. Multi-pick — leave empty for all. (optional)
    filter_offer_id = 56 # int | Offer ID. Look up via `GET /api/v1/offers`. (optional)
    filter_offer_type_id = 56 # int | Offer-type ID. (optional)
    filter_device = 56 # int | Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  (optional)
    filter_country = 'US' # str | ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`). (optional)
    format = json # str |  (optional) (default to json)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Field name. Prefix with `-` for descending (e.g. `-views`). (optional)

    try:
        # CPA / affiliate offer performance — advertiser side.
        api_response = api_instance.api_v1_advertiser_offers_stats_get(var_from=var_from, to=to, interval=interval, group_by=group_by, metrics=metrics, filter_offer_id=filter_offer_id, filter_offer_type_id=filter_offer_type_id, filter_device=filter_device, filter_country=filter_country, format=format, page=page, per_page=per_page, sort=sort)
        print("The response of StatsAdvertiserOffersApi->api_v1_advertiser_offers_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsAdvertiserOffersApi->api_v1_advertiser_offers_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| ISO date — inclusive start. Defaults to 7 days ago. | [optional] 
 **to** | **date**| ISO date — inclusive end. Defaults to today. Max range 92 days. | [optional] 
 **interval** | **str**|  | [optional] [default to sum]
 **group_by** | [**List[str]**](str.md)| Dimensions to aggregate by. Multi-pick up to 8. | [optional] 
 **metrics** | [**List[str]**](str.md)| Metrics to return. Multi-pick — leave empty for all. | [optional] 
 **filter_offer_id** | **int**| Offer ID. Look up via &#x60;GET /api/v1/offers&#x60;. | [optional] 
 **filter_offer_type_id** | **int**| Offer-type ID. | [optional] 
 **filter_device** | **int**| Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV |  | [optional] 
 **filter_country** | **str**| ISO-3166 alpha-2 country code (e.g. &#x60;US&#x60;, &#x60;DE&#x60;, &#x60;BR&#x60;). | [optional] 
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


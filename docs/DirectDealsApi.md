# goadserver.DirectDealsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_campaigns_directdeal_id_cancel_put**](DirectDealsApi.md#api_v1_campaigns_directdeal_id_cancel_put) | **PUT** /api/v1/campaigns/directdeal/{id}/cancel | Cancel a direct deal.
[**api_v1_direct_deals_adzones_get**](DirectDealsApi.md#api_v1_direct_deals_adzones_get) | **GET** /api/v1/direct-deals/adzones | Ad zones a direct deal can be booked on.
[**api_v1_direct_deals_get**](DirectDealsApi.md#api_v1_direct_deals_get) | **GET** /api/v1/direct-deals | List direct deals with their derived status.


# **api_v1_campaigns_directdeal_id_cancel_put**
> api_v1_campaigns_directdeal_id_cancel_put(id)

Cancel a direct deal.

The panel's Cancel button: sets `iscancelled = 1`, which stops the
deal for good — unlike `PATCH …/active` (pause), it cannot be
resumed; book a new deal (or clone this one) instead. The row stays
listed with `status: cancelled`. Pinned keys may only cancel a
pinned campaign; an own-scoped member only a deal they manage.
No body.


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
    api_instance = goadserver.DirectDealsApi(api_client)
    id = 56 # int | The direct deal (campaign) id.

    try:
        # Cancel a direct deal.
        api_instance.api_v1_campaigns_directdeal_id_cancel_put(id)
    except Exception as e:
        print("Exception when calling DirectDealsApi->api_v1_campaigns_directdeal_id_cancel_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The direct deal (campaign) id. | 

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
**200** | Cancelled. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;deal_not_found&#x60; — no direct deal with this id on the account, or (own-scoped team member) not one they manage. A team member with read-only campaign access gets 403 &#x60;forbidden&#x60;. |  -  |
**422** | &#x60;already_cancelled&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_direct_deals_adzones_get**
> api_v1_direct_deals_adzones_get(website_id=website_id)

Ad zones a direct deal can be booked on.

The account's own, non-deleted publisher ad zones (offer sites
excluded) — the picker behind `ad_space_id` on
`POST /api/v1/campaigns/directdeal`. A deal takes its ad type from
the zone, so there is no ad-type filter. A team member limited to
their own ad zones sees only those (directly or via the website),
and can only book a deal on them. Same handler as the panel.


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
    api_instance = goadserver.DirectDealsApi(api_client)
    website_id = 56 # int | Only zones on this site. (optional)

    try:
        # Ad zones a direct deal can be booked on.
        api_instance.api_v1_direct_deals_adzones_get(website_id=website_id)
    except Exception as e:
        print("Exception when calling DirectDealsApi->api_v1_direct_deals_adzones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **int**| Only zones on this site. | [optional] 

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
**200** | Zones, by name. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_direct_deals_get**
> api_v1_direct_deals_get(page=page, per_page=per_page, status=status, website_ids=website_ids, ad_type=ad_type, tag_ids=tag_ids, filter_name=filter_name, sort_by=sort_by, sort_dir=sort_dir)

List direct deals with their derived status.

The panel's Direct Deals listing (`flatratecampaigns` rows with
`isdirectdeal = 1`, deleted rows excluded), newest first. Unlike
`GET /api/v1/campaigns?type=directdeal` each row carries the
derived `status` and the booked zone / site names. Same handler as
the panel.

`status` is derived in this order: `cancelled` (cancel button) →
`completed` → `paused` → `active` (state 1) → `pending` (state 0)
→ `rejected` (state -1) → `ended` (state 2).

`totalbudget` is in the account's currency units. Account-wide, so
a key pinned to campaigns gets 403 `forbidden_resource` — use
`GET /api/v1/campaigns?type=directdeal` (pin-filtered) instead.
For a team member whose campaign access is limited to their own
campaigns, only the deals they manage (created, assigned, or filed
under a campaign group they manage) are listed and counted.


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
    api_instance = goadserver.DirectDealsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    status = 'status_example' # str | CSV of active, paused, pending, completed, ended, cancelled, rejected. (optional)
    website_ids = 'website_ids_example' # str | CSV of site ids (the booked zone's site). (optional)
    ad_type = 'ad_type_example' # str | CSV of ad type ids. (optional)
    tag_ids = 'tag_ids_example' # str | CSV of tag ids; a folder tag also matches its sub-tags. (optional)
    filter_name = 'filter_name_example' # str | Name substring. (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)

    try:
        # List direct deals with their derived status.
        api_instance.api_v1_direct_deals_get(page=page, per_page=per_page, status=status, website_ids=website_ids, ad_type=ad_type, tag_ids=tag_ids, filter_name=filter_name, sort_by=sort_by, sort_dir=sort_dir)
    except Exception as e:
        print("Exception when calling DirectDealsApi->api_v1_direct_deals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **status** | **str**| CSV of active, paused, pending, completed, ended, cancelled, rejected. | [optional] 
 **website_ids** | **str**| CSV of site ids (the booked zone&#39;s site). | [optional] 
 **ad_type** | **str**| CSV of ad type ids. | [optional] 
 **tag_ids** | **str**| CSV of tag ids; a folder tag also matches its sub-tags. | [optional] 
 **filter_name** | **str**| Name substring. | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]

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
**200** | One page of deals. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.SSPCampaignsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_ssp_campaigns_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_get) | **GET** /api/v1/publisher/ssp/campaigns | List SSP campaigns (feeds).
[**api_v1_publisher_ssp_campaigns_id_clone_post**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_clone_post) | **POST** /api/v1/publisher/ssp/campaigns/{id}/clone | Clone an SSP campaign.
[**api_v1_publisher_ssp_campaigns_id_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_get) | **GET** /api/v1/publisher/ssp/campaigns/{id} | Get one SSP campaign.
[**api_v1_publisher_ssp_campaigns_id_put**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id} | Update an SSP campaign.
[**api_v1_publisher_ssp_campaigns_id_test_rtb_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_test_rtb_get) | **GET** /api/v1/publisher/ssp/campaigns/{id}/test-rtb | Context for an RTB test request.
[**api_v1_publisher_ssp_campaigns_id_test_rtb_post**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_test_rtb_post) | **POST** /api/v1/publisher/ssp/campaigns/{id}/test-rtb | Send one test bid request to the feed&#39;s endpoint.
[**api_v1_publisher_ssp_campaigns_id_toggle_delete_put**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_toggle_delete_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id}/toggle-delete | Delete or restore an SSP campaign.
[**api_v1_publisher_ssp_campaigns_id_toggle_pause_put**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_toggle_pause_put) | **PUT** /api/v1/publisher/ssp/campaigns/{id}/toggle-pause | Pause or resume an SSP campaign.
[**api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get) | **GET** /api/v1/publisher/ssp/campaigns/{id}/wl-ron-campaigns | RON campaigns that can be whitelisted on a feed.
[**api_v1_publisher_ssp_campaigns_post**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_post) | **POST** /api/v1/publisher/ssp/campaigns | Create an SSP campaign.
[**api_v1_publisher_ssp_campaigns_setup_data_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_campaigns_setup_data_get) | **GET** /api/v1/publisher/ssp/campaigns/setup-data | Lookups for the SSP campaign form.
[**api_v1_publisher_ssp_filters_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_filters_get) | **GET** /api/v1/publisher/ssp/filters | Filter values for the SSP campaign list.
[**api_v1_publisher_ssp_networks_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_networks_get) | **GET** /api/v1/publisher/ssp/networks | RTB networks your SSP campaigns use.
[**api_v1_publisher_ssp_seller_disclosure_put**](SSPCampaignsApi.md#api_v1_publisher_ssp_seller_disclosure_put) | **PUT** /api/v1/publisher/ssp/seller-disclosure | Publish or hide your name in sellers.json.
[**api_v1_publisher_ssp_sites_id_ads_txt_check_post**](SSPCampaignsApi.md#api_v1_publisher_ssp_sites_id_ads_txt_check_post) | **POST** /api/v1/publisher/ssp/sites/{id}/ads-txt-check | Re-check a site&#39;s ads.txt now.
[**api_v1_publisher_ssp_sites_id_ads_txt_status_get**](SSPCampaignsApi.md#api_v1_publisher_ssp_sites_id_ads_txt_status_get) | **GET** /api/v1/publisher/ssp/sites/{id}/ads-txt-status | Last stored ads.txt check for a site.


# **api_v1_publisher_ssp_campaigns_get**
> api_v1_publisher_ssp_campaigns_get()

List SSP campaigns (feeds).

Every SSP campaign of the account, newest first, including paused
and deleted ones (`campaignstate`: 0 active, 1 paused, 2 deleted).
An SSP campaign is a feed that sells your inventory to — or buys
RTB traffic from — another platform. The response is a bare JSON
array, not paginated.

All SSP routes need one of the SSP rights (`mod_ssp`,
`ssp_external`, `ssp_networks`, `ssp_exchange`,
`ssp_headerbidding`) and answer for publisher and advertiser
(ad-manager) accounts alike. Keys pinned to `adzone_ids` or
`site_ids` are refused with `403 forbidden_resource`: a feed spans
sites and zones the pin cannot follow.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)

    try:
        # List SSP campaigns (feeds).
        api_instance.api_v1_publisher_ssp_campaigns_get()
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_get: %s\n" % e)
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
**200** | Campaigns. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_clone_post**
> api_v1_publisher_ssp_campaigns_id_clone_post(id)

Clone an SSP campaign.

Copies every column into a new campaign named `<name>('Copy')`. A
clone of an external/exchange feed gets its own fresh `hash`. No
request body.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 

    try:
        # Clone an SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_id_clone_post(id)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_clone_post: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloned. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_get**
> api_v1_publisher_ssp_campaigns_id_get(id)

Get one SSP campaign.

The full campaign as the edit form loads it. Targeting lists come
back as string arrays (`"0"`/empty = all). `json_zone_urls` is the
stored `{zoneId: {url, active}}` map, `zone_urls` the same as an
array with zone names. Note: the browser-language targeting is read
back as `language` (comma-separated) but written as
`browserlanguages`.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 

    try:
        # Get one SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_id_get(id)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_get: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The campaign, wrapped in a one-element &#x60;campaigns&#x60; array. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_put**
> api_v1_publisher_ssp_campaigns_id_put(id, ssp_campaign_write)

Update an SSP campaign.

**Full replace, not a patch**: every column is rewritten from the
body, so a missing targeting list resets to "all" and a missing
scalar to its default. Read the campaign first and send it back
whole. Exceptions: `header_bidding` is locked to its create-time
value, `dsp_ids` is kept unless an admin sets it, and an absent
`bill_on_burl` keeps the stored value. Same validation (409) and
`unknown_fields` (422) as create.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.ssp_campaign_write import SspCampaignWrite
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 
    ssp_campaign_write = goadserver.SspCampaignWrite() # SspCampaignWrite | 

    try:
        # Update an SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_id_put(id, ssp_campaign_write)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ssp_campaign_write** | [**SspCampaignWrite**](SspCampaignWrite.md)|  | 

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
**200** | Saved. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**409** | Validation failed. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |
**500** | &#x60;save_failed&#x60; — also returned when the campaign is not yours. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_test_rtb_get**
> api_v1_publisher_ssp_campaigns_id_test_rtb_get(id)

Context for an RTB test request.

The resolved ad type, request URL and RTB type of the campaign, the tenant's common banner sizes and the caller's IP/UA, as defaults for the POST.

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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 

    try:
        # Context for an RTB test request.
        api_instance.api_v1_publisher_ssp_campaigns_id_test_rtb_get(id)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_test_rtb_get: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found (or deleted). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_test_rtb_post**
> api_v1_publisher_ssp_campaigns_id_test_rtb_post(id, api_v1_publisher_ssp_campaigns_id_test_rtb_post_request=api_v1_publisher_ssp_campaigns_id_test_rtb_post_request)

Send one test bid request to the feed's endpoint.

Builds a request the way the ad server would for this campaign,
sends it (outbound to public addresses only) and classifies the
answer. Every field is optional. **`bidfloor` and `best_price` are
CPM in currency units.**


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_ssp_campaigns_id_test_rtb_post_request import ApiV1PublisherSspCampaignsIdTestRtbPostRequest
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 
    api_v1_publisher_ssp_campaigns_id_test_rtb_post_request = {"ad_type":"banner","width":728,"height":90,"country":"DE","bidfloor":0.5} # ApiV1PublisherSspCampaignsIdTestRtbPostRequest |  (optional)

    try:
        # Send one test bid request to the feed's endpoint.
        api_instance.api_v1_publisher_ssp_campaigns_id_test_rtb_post(id, api_v1_publisher_ssp_campaigns_id_test_rtb_post_request=api_v1_publisher_ssp_campaigns_id_test_rtb_post_request)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_test_rtb_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_publisher_ssp_campaigns_id_test_rtb_post_request** | [**ApiV1PublisherSspCampaignsIdTestRtbPostRequest**](ApiV1PublisherSspCampaignsIdTestRtbPostRequest.md)|  | [optional] 

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
**200** | Test result (also for a failed partner call — read &#x60;verdict&#x60;). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found (or deleted). |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_toggle_delete_put**
> api_v1_publisher_ssp_campaigns_id_toggle_delete_put(id, api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request)

Delete or restore an SSP campaign.

Soft delete (`isdeleted`). `{status: 0}` restores it.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request import ApiV1PublisherSspCampaignsIdToggleDeletePutRequest
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 
    api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request = {"status":1} # ApiV1PublisherSspCampaignsIdToggleDeletePutRequest | 

    try:
        # Delete or restore an SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_id_toggle_delete_put(id, api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_toggle_delete_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_publisher_ssp_campaigns_id_toggle_delete_put_request** | [**ApiV1PublisherSspCampaignsIdToggleDeletePutRequest**](ApiV1PublisherSspCampaignsIdToggleDeletePutRequest.md)|  | 

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
**200** | Done. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;not_found&#x60; (also when the value was already set). |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_toggle_pause_put**
> api_v1_publisher_ssp_campaigns_id_toggle_pause_put(id, api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request)

Pause or resume an SSP campaign.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request import ApiV1PublisherSspCampaignsIdTogglePausePutRequest
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 
    api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request = {"status":0} # ApiV1PublisherSspCampaignsIdTogglePausePutRequest | 

    try:
        # Pause or resume an SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_id_toggle_pause_put(id, api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_toggle_pause_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_publisher_ssp_campaigns_id_toggle_pause_put_request** | [**ApiV1PublisherSspCampaignsIdTogglePausePutRequest**](ApiV1PublisherSspCampaignsIdTogglePausePutRequest.md)|  | 

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
**200** | Done. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;not_found&#x60; (also when the value was already set). |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get**
> api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get(id, adtype=adtype, siteid=siteid, search=search, ids=ids)

RON campaigns that can be whitelisted on a feed.

Candidates for `wl_ron_campaign_ids`: RON campaigns of the feed's ad
type (matching the site's main category when that module is on).
`available: false` means the picker is off for this tenant (the
`modules.publisher.connect_campaigns` module, ad-manager tenants
only) — not an error. Use `id = 0` with `?adtype=` for a campaign
that is not saved yet. `ids` echoes the current selection.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | SSP campaign id, or 0.
    adtype = 56 # int | Ad type when `id` is 0. (optional)
    siteid = 56 # int | Override the site used for the category match (must be yours). (optional)
    search = 'search_example' # str |  (optional)
    ids = 'ids_example' # str | Comma-separated currently-selected ids. (optional)

    try:
        # RON campaigns that can be whitelisted on a feed.
        api_instance.api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get(id, adtype=adtype, siteid=siteid, search=search, ids=ids)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_id_wl_ron_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SSP campaign id, or 0. | 
 **adtype** | **int**| Ad type when &#x60;id&#x60; is 0. | [optional] 
 **siteid** | **int**| Override the site used for the category match (must be yours). | [optional] 
 **search** | **str**|  | [optional] 
 **ids** | **str**| Comma-separated currently-selected ids. | [optional] 

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
**200** | Candidates. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_post**
> api_v1_publisher_ssp_campaigns_post(ssp_campaign_write)

Create an SSP campaign.

Same save path as the panel's SSP campaign form. New campaigns start
**paused** (`ispaused = 1`); resume with
`PUT /api/v1/publisher/ssp/campaigns/{id}/toggle-pause` `{status: 0}`.
External and exchange campaigns get a fresh feed `hash` (their
endpoint identity and the token for the SSP stats feed).

`ssptype`:
- `ssp` — outgoing RTB to a network (`rtb_network` required).
  `use_type`: 0 = one request URL, 1 = per-ad-zone URLs
  (`zoneurls`), 2 = smart-zone RTB feed.
- `external` — an incoming feed a partner calls (`siteid` required).
- `exchange` — incoming exchange feed (`ssp_pct` 1–100 required).
- `header_bidding: true` (external/exchange only) collapses the
  campaign to Prebid slots (`slots` required).

Validation failures answer **409** with
`{"errors": {"<field>": "<CODE>"}}` (codes such as `EMPTY_NAME`,
`NO_NETWORK_ID_GIVEN`, `NO_WEBSITE_SELECTED`, `WEBSITE_NOT_FOUND`,
`SSP_EXCHANGE_PCT_ERROR`, `HB_SLOTS_REQUIRED`) — the panel's shape,
kept as is. Unknown body fields are refused with
`422 unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.ssp_campaign_write import SspCampaignWrite
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    ssp_campaign_write = {"name":"Exo RTB feed","adtype":2,"ssptype":"ssp","rtbtype":"openrtb","rtb_network":5,"use_type":0,"request_url":"https://rtb.network.example/bid?feed=abc","device_type_ids":[1,3],"regionids":[],"ssp_pct":80} # SspCampaignWrite | 

    try:
        # Create an SSP campaign.
        api_instance.api_v1_publisher_ssp_campaigns_post(ssp_campaign_write)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssp_campaign_write** | [**SspCampaignWrite**](SspCampaignWrite.md)|  | 

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
**200** | Created (paused). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**409** | Validation failed. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_campaigns_setup_data_get**
> api_v1_publisher_ssp_campaigns_setup_data_get()

Lookups for the SSP campaign form.

Ad types, RTB networks, your websites, targeting lists (device
types, OS, browsers, connection types, languages, carriers, IP
pools, RTB categories, tier country lists), your other SSP
campaigns, enabled modules, display-option config, and the values a
partner needs to integrate (`ad_domain`, `rtb_domain`,
`hb_endpoint`, `openrtb2_endpoint`, `sellers_json_url`,
`ads_txt_line`, `seller_id`, `public_seller_disclosure`).
In-app (Prebid Mobile, docs/IN_APP.md): the SDK's Prebid Server
host is `openrtb2_endpoint`, its account id the campaign's token
(`hash`), and each ad unit's config id names its adzone; apps send
`app.bundle` instead of `site.page`, interstitial units `imp.instl`,
rewarded ones `imp.rwdd` / `imp.ext.prebid.is_rewarded_inventory`.
`ads_txt_line` goes in app-ads.txt on the app's developer website.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)

    try:
        # Lookups for the SSP campaign form.
        api_instance.api_v1_publisher_ssp_campaigns_setup_data_get()
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_campaigns_setup_data_get: %s\n" % e)
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
**200** | Lookups. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_filters_get**
> api_v1_publisher_ssp_filters_get()

Filter values for the SSP campaign list.

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
    api_instance = goadserver.SSPCampaignsApi(api_client)

    try:
        # Filter values for the SSP campaign list.
        api_instance.api_v1_publisher_ssp_filters_get()
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_filters_get: %s\n" % e)
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
**200** | Ad types, active RTB networks and statuses. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_networks_get**
> api_v1_publisher_ssp_networks_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_name=filter_name)

RTB networks your SSP campaigns use.

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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    filter_id = 56 # int |  (optional)
    filter_name = 'filter_name_example' # str |  (optional)

    try:
        # RTB networks your SSP campaigns use.
        api_instance.api_v1_publisher_ssp_networks_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_name=filter_name)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **filter_id** | **int**|  | [optional] 
 **filter_name** | **str**|  | [optional] 

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
**200** | Networks. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_seller_disclosure_put**
> api_v1_publisher_ssp_seller_disclosure_put(api_v1_publisher_ssp_seller_disclosure_put_request)

Publish or hide your name in sellers.json.

`true`: `/sellers.json` lists your company name and primary site domain. `false`: confidential, `seller_id` only (the default).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_ssp_seller_disclosure_put_request import ApiV1PublisherSspSellerDisclosurePutRequest
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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    api_v1_publisher_ssp_seller_disclosure_put_request = {"enabled":true} # ApiV1PublisherSspSellerDisclosurePutRequest | 

    try:
        # Publish or hide your name in sellers.json.
        api_instance.api_v1_publisher_ssp_seller_disclosure_put(api_v1_publisher_ssp_seller_disclosure_put_request)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_seller_disclosure_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_ssp_seller_disclosure_put_request** | [**ApiV1PublisherSspSellerDisclosurePutRequest**](ApiV1PublisherSspSellerDisclosurePutRequest.md)|  | 

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
**200** | Saved. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_sites_id_ads_txt_check_post**
> api_v1_publisher_ssp_sites_id_ads_txt_check_post(id)

Re-check a site's ads.txt now.

Fetches `https://<site>/ads.txt`, looks for the network's line
(`ad_domain`, your `seller_id`, `DIRECT`), stores and returns the
result. Within the fetch cooldown the stored result is returned
without a new fetch. No request body.


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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | Your site id.

    try:
        # Re-check a site's ads.txt now.
        api_instance.api_v1_publisher_ssp_sites_id_ads_txt_check_post(id)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_sites_id_ads_txt_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Your site id. | 

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
**200** | Check result. |  -  |
**400** | &#x60;invalid_site&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;not_found&#x60; — not one of your live sites. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_ssp_sites_id_ads_txt_status_get**
> api_v1_publisher_ssp_sites_id_ads_txt_status_get(id)

Last stored ads.txt check for a site.

No fetch. `checked:false` when the site was never checked.

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
    api_instance = goadserver.SSPCampaignsApi(api_client)
    id = 56 # int | 

    try:
        # Last stored ads.txt check for a site.
        api_instance.api_v1_publisher_ssp_sites_id_ads_txt_status_get(id)
    except Exception as e:
        print("Exception when calling SSPCampaignsApi->api_v1_publisher_ssp_sites_id_ads_txt_status_get: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status. |  -  |
**400** | &#x60;invalid_site&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


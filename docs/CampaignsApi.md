# goadserver.CampaignsApi

All URIs are relative to *https://up.goadserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_campaigns_get**](CampaignsApi.md#api_v1_campaigns_get) | **GET** /api/v1/campaigns | List the caller&#39;s campaigns across all types (or one type).
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get) | **GET** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | List per-zone bid overrides for a RON ad.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put) | **PUT** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | Replace the per-zone bid overrides on a RON ad.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete) | **DELETE** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/{zoneId} | Clear a single per-zone bid override.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/active | Pause or unpause a single ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bid | Set a single ad&#39;s bid.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/clone | Clone a single ad within a campaign.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_delete**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_delete) | **DELETE** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Soft-delete an ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Show one ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Update an ad.
[**api_v1_campaigns_type_campaign_id_ads_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads | List ads on a campaign.
[**api_v1_campaigns_type_campaign_id_ads_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads | Create an ad on a campaign (smart-default, JSON-only).
[**api_v1_campaigns_type_campaign_id_schema_ads_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_schema_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/_schema/ads | Field metadata for ad creation, scoped to a campaign.
[**api_v1_campaigns_type_id_active_patch**](CampaignsApi.md#api_v1_campaigns_type_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/active | Pause or unpause a campaign.
[**api_v1_campaigns_type_id_bids_patch**](CampaignsApi.md#api_v1_campaigns_type_id_bids_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/bids | Mass update bids on every ad in a campaign.
[**api_v1_campaigns_type_id_clone_post**](CampaignsApi.md#api_v1_campaigns_type_id_clone_post) | **POST** /api/v1/campaigns/{type}/{id}/clone | Clone a campaign and all its ads.
[**api_v1_campaigns_type_id_delete**](CampaignsApi.md#api_v1_campaigns_type_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id} | Soft-delete a campaign.
[**api_v1_campaigns_type_id_filters_filter_type_filter_id_delete**](CampaignsApi.md#api_v1_campaigns_type_id_filters_filter_type_filter_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id}/filters/{filter_type}/{filter_id} | Detach a filter from this campaign.
[**api_v1_campaigns_type_id_filters_get**](CampaignsApi.md#api_v1_campaigns_type_id_filters_get) | **GET** /api/v1/campaigns/{type}/{id}/filters | List filters attached to this campaign.
[**api_v1_campaigns_type_id_filters_post**](CampaignsApi.md#api_v1_campaigns_type_id_filters_post) | **POST** /api/v1/campaigns/{type}/{id}/filters | Attach a filter to this campaign.
[**api_v1_campaigns_type_id_get**](CampaignsApi.md#api_v1_campaigns_type_id_get) | **GET** /api/v1/campaigns/{type}/{id} | Get a single campaign.
[**api_v1_campaigns_type_id_min_bid_get**](CampaignsApi.md#api_v1_campaigns_type_id_min_bid_get) | **GET** /api/v1/campaigns/{type}/{id}/min-bid | Get the campaign&#39;s minimum acceptable CPC bid.
[**api_v1_campaigns_type_post**](CampaignsApi.md#api_v1_campaigns_type_post) | **POST** /api/v1/campaigns/{type} | Create a new campaign (smart-default).
[**api_v1_campaigns_type_schema_ads_get**](CampaignsApi.md#api_v1_campaigns_type_schema_ads_get) | **GET** /api/v1/campaigns/{type}/_schema/ads | Field metadata for ad creation.
[**api_v1_campaigns_type_schema_get**](CampaignsApi.md#api_v1_campaigns_type_schema_get) | **GET** /api/v1/campaigns/{type}/_schema | Field metadata for create/update.


# **api_v1_campaigns_get**
> ApiV1CampaignsGet200Response api_v1_campaigns_get(type=type, page=page, per_page=per_page, fields=fields)

List the caller's campaigns across all types (or one type).

Returns the caller's campaigns. By default each row carries a
rich-but-bounded projection: identity (`id`, `name`, `campaign_type`,
`ad_type` + `ad_type_label`, `selling_type`), lifecycle
(`is_paused`, `is_active`, `is_deleted`, `is_complete`,
`pending_state`), budget (`daily_budget`, `daily_spent`,
`total_budget`, `total_spent`, `use_campaign_budget`), bidding
(`bid_default`, `min_bid`), targeting summary (`countries`,
`languages`, `categories`, `device_type_ids`, …), capping,
schedule, linked filter/pool ids, and timestamps.

Use `?fields=` to opt in or out of fields:

  - `?fields=*` — return **every** column on the underlying
    campaign row (70+ fields, type-dependent). Convenient for
    AI agents that want the full picture in one call.
  - `?fields=name,daily_budget,countries` — narrow to just
    those fields. `id` is always included.
  - (omitted) — default rich projection above.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_get200_response import ApiV1CampaignsGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = all # str |  (optional) (default to all)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)
    fields = 'fields_example' # str | CSV of fields to return; `*` returns everything available. (optional)

    try:
        # List the caller's campaigns across all types (or one type).
        api_response = api_instance.api_v1_campaigns_get(type=type, page=page, per_page=per_page, fields=fields)
        print("The response of CampaignsApi->api_v1_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to all]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]
 **fields** | **str**| CSV of fields to return; &#x60;*&#x60; returns everything available. | [optional] 

### Return type

[**ApiV1CampaignsGet200Response**](ApiV1CampaignsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated campaign list (projected to a stable subset of fields). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get**
> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get(campaign_id, ad_id)

List per-zone bid overrides for a RON ad.

RON ads carry a per-adzone bid map (`bids_per_zone` JSON), letting
an advertiser bid different amounts on different publisher zones.
This endpoint returns each override enriched with the zone + site
names, so an auto-optimiser can correlate ids ↔ human labels in
one call.

Empty list if the ad has no overrides — the global ad bid applies
to every zone.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # List per-zone bid overrides for a RON ad.
        api_response = api_instance.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get(campaign_id, ad_id)
        print("The response of CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

[**ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response**](ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zone bid map. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put**
> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put(campaign_id, ad_id, api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request)

Replace the per-zone bid overrides on a RON ad.

Full-replace semantics — any zone NOT in the request body has its
override cleared. If you only want to update a few zones, pass the
complete current set merged with your changes. Auto-optimisers
usually recompute the full bid sheet per cycle so this fits the
common loop.

Negative or zero `zone_id` and negative `bid` entries are silently
dropped.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request = {"zone_bids":[{"zone_id":12,"bid":0.002},{"zone_id":19,"bid":8.0E-4}]} # ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest | 

    try:
        # Replace the per-zone bid overrides on a RON ad.
        api_response = api_instance.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put(campaign_id, ad_id, api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request)
        print("The response of CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request** | [**ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest**](ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest.md)|  | 

### Return type

[**ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response**](ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replaced. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete**
> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete(campaign_id, ad_id, zone_id)

Clear a single per-zone bid override.

Removes the override for one zone. The global ad bid takes over
again for that zone. Returns 404 if no override exists for the
given zone.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    zone_id = 56 # int | 

    try:
        # Clear a single per-zone bid override.
        api_response = api_instance.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete(campaign_id, ad_id, zone_id)
        print("The response of CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **zone_id** | **int**|  | 

### Return type

[**ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response**](ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Override cleared. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found, or no override for that zone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch**
> ApiV1CampaignsTypeIdActivePatch200Response api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch(type, campaign_id, ad_id, api_v1_campaigns_type_id_active_patch_request)

Pause or unpause a single ad.

Idempotent set. `active=true` activates the ad, `active=false`
pauses it. Useful for granular pause/resume from an optimiser
without touching the campaign-level pause state.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Pause or unpause a single ad.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch(type, campaign_id, ad_id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdActivePatch200Response**](ApiV1CampaignsTypeIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch**
> ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request)

Set a single ad's bid.

Updates one ad's bid. Value is in main-currency units (the same
scale `bid` is stored in). For the legal floor on the parent
campaign, query `GET /campaigns/{type}/{id}/min-bid` first.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request = goadserver.ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest() # ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest | 

    try:
        # Set a single ad's bid.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request** | [**ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest**](ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bid updated. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found. |  -  |
**422** | Validation error (negative bid, missing field). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post(type, campaign_id, ad_id)

Clone a single ad within a campaign.

Duplicates one ad. The clone is attached to the same campaign as
the source. Useful for A/B-testing creative variants without
rebuilding the whole record from scratch.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Clone a single ad within a campaign.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post(type, campaign_id, ad_id)
        print("The response of CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ad cloned. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Source ad not found or not owned by caller. |  -  |
**422** | Clone failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_delete**
> api_v1_campaigns_type_campaign_id_ads_ad_id_delete(type, campaign_id, ad_id)

Soft-delete an ad.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Soft-delete an ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_delete(type, campaign_id, ad_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**404** | Ad not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_get**
> api_v1_campaigns_type_campaign_id_ads_ad_id_get(type, campaign_id, ad_id)

Show one ad.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Show one ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_get(type, campaign_id, ad_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ad detail. |  -  |
**404** | Ad not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_put**
> api_v1_campaigns_type_campaign_id_ads_ad_id_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_put_request)

Update an ad.

Editable fields depend on ad type. Common fields:
`bid`, `isactive`, `creatives` (banner/video/native blob).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_ad_id_put_request = goadserver.ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest() # ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest | 

    try:
        # Update an ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_ad_id_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest**](ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**404** | Ad not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_get**
> ApiV1CampaignsTypeCampaignIdAdsGet200Response api_v1_campaigns_type_campaign_id_ads_get(type, campaign_id, page=page, per_page=per_page)

List ads on a campaign.

Returns every ad attached to the campaign (paginated). Each row
carries `id`, `bid`, `isactive`, `bansizeid`, the underlying
`creatives` JSON (banner/video/native, with file paths and
creative_id refs), and lifetime stats from the campaign-side
rollup.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response import ApiV1CampaignsTypeCampaignIdAdsGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)

    try:
        # List ads on a campaign.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_get(type, campaign_id, page=page, per_page=per_page)
        print("The response of CampaignsApi->api_v1_campaigns_type_campaign_id_ads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsGet200Response**](ApiV1CampaignsTypeCampaignIdAdsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ads. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_post**
> api_v1_campaigns_type_campaign_id_ads_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_post_request, dry_run=dry_run, strict=strict)

Create an ad on a campaign (smart-default, JSON-only).

Creates a new ad attached to the campaign. JSON-only — agents
reference an existing creative (banner pool, single creative,
URL or HTML) instead of uploading files. The panel handler at
the same path still accepts `multipart/form-data` for file
uploads — this docs entry covers the JSON path only.

Required: `title` + `bid` + exactly **one** creative reference
(`banner_pool_id` / `creative_id` / `banner_url` / `banner_html`
/ `video_pool_id`). `destination_url` is required unless the
creative carries its own URL (popunder/JS) or you set
`url_pool_id`.

**Modes:**
  - `?dry_run=1` — return the resolved field map + computed
    `creatives` JSON without inserting.
  - `?strict=1` — reject unknown field names with a 422.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request import ApiV1CampaignsTypeCampaignIdAdsPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_post_request = {"title":"My banner ad","bid":0.0042,"banner_pool_id":129481,"destination_url":"https://example.com/lander"} # ApiV1CampaignsTypeCampaignIdAdsPostRequest | 
    dry_run = 'dry_run_example' # str |  (optional)
    strict = 'strict_example' # str |  (optional)

    try:
        # Create an ad on a campaign (smart-default, JSON-only).
        api_instance.api_v1_campaigns_type_campaign_id_ads_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_post_request, dry_run=dry_run, strict=strict)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_post_request** | [**ApiV1CampaignsTypeCampaignIdAdsPostRequest**](ApiV1CampaignsTypeCampaignIdAdsPostRequest.md)|  | 
 **dry_run** | **str**|  | [optional] 
 **strict** | **str**|  | [optional] 

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
**201** | Created. Body is the freshly-created ad in the same shape as &#x60;GET /campaigns/{type}/{campaignId}/ads/{adId}&#x60;. |  -  |
**200** | When &#x60;?dry_run&#x3D;1&#x60; — body is &#x60;{ dry_run: true, resolved: ..., creatives: ..., would_insert: ... }&#x60;. |  -  |
**422** | Validation error. |  -  |
**404** | Campaign not found. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_schema_ads_get**
> api_v1_campaigns_type_campaign_id_schema_ads_get(type, campaign_id)

Field metadata for ad creation, scoped to a campaign.

Same as `/_schema/ads` above, but uses the campaign's ad type to
return only the fields that apply (e.g. video pools omitted for
a banner-only campaign). Sets `campaign_ad_type` in the response.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 

    try:
        # Field metadata for ad creation, scoped to a campaign.
        api_instance.api_v1_campaigns_type_campaign_id_schema_ads_get(type, campaign_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_schema_ads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ad-create field metadata, narrowed to the campaign&#39;s ad type. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_active_patch**
> ApiV1CampaignsTypeIdActivePatch200Response api_v1_campaigns_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)

Pause or unpause a campaign.

Idempotent. `active=true` unpauses, `active=false` pauses. Reuses
the same panel-side guards: flat-rate campaigns with running deals
cannot be paused; offer campaigns require >= 5 ads to be unpaused.

This is the endpoint behind the **"On / off only"** key preset.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Pause or unpause a campaign.
        api_response = api_instance.api_v1_campaigns_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdActivePatch200Response**](ApiV1CampaignsTypeIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |
**422** | Toggle blocked by a business rule (e.g. flat-rate running deals, offer min-ads). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_bids_patch**
> ApiV1CampaignsTypeIdBidsPatch200Response api_v1_campaigns_type_id_bids_patch(type, id, api_v1_campaigns_type_id_bids_patch_request)

Mass update bids on every ad in a campaign.

Update every (or a subset of) ad's bid in one call. Three modes:

  - `set`     — overwrite each target ad's bid with `value`.
  - `pct_inc` — raise each target ad's bid by `pct` percent.
  - `pct_dec` — lower each target ad's bid by `pct` percent.

Optional `ad_ids` narrows the update to a subset (omit or empty
list = every non-deleted ad on the campaign). Bids are clamped at
0 — anything that would resolve below 0 is set to 0.

Bid values are in main-currency units (the same scale `bid` is
stored in). For minimum-acceptable-bid floors call
`GET /api/v1/campaigns/{type}/{id}/min-bid` first.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_bids_patch200_response import ApiV1CampaignsTypeIdBidsPatch200Response
from goadserver.models.api_v1_campaigns_type_id_bids_patch_request import ApiV1CampaignsTypeIdBidsPatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_bids_patch_request = {"mode":"set","value":0.0042} # ApiV1CampaignsTypeIdBidsPatchRequest | 

    try:
        # Mass update bids on every ad in a campaign.
        api_response = api_instance.api_v1_campaigns_type_id_bids_patch(type, id, api_v1_campaigns_type_id_bids_patch_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_bids_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_bids_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_bids_patch_request** | [**ApiV1CampaignsTypeIdBidsPatchRequest**](ApiV1CampaignsTypeIdBidsPatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdBidsPatch200Response**](ApiV1CampaignsTypeIdBidsPatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | Validation error (invalid mode / value / pct). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_clone_post**
> ApiV1CampaignsTypeIdClonePost201Response api_v1_campaigns_type_id_clone_post(type, id, api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request)

Clone a campaign and all its ads.

Duplicates the campaign row and every ad attached to it. The clone
lands paused (`is_active=false`) so you can review and tweak it
before activating. Targeting filters, bids, daily caps and budget
settings are all carried over verbatim — only `name` (suffix
" Copy" by default, overridable via the body) and reset
bookkeeping fields (`num_ads`, `pending_state`, `dateadded`,
`wl_zoneids`) differ from the original.

For `ron` campaigns the clone also strips any flat-rate deals
(the new campaign starts with no running placements) and
copies offer screenshot files from the original so the cloned
offer-mode campaign retains its preview imagery.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response import ApiV1CampaignsTypeIdClonePost201Response
from goadserver.models.api_v1_campaigns_type_id_clone_post_request import ApiV1CampaignsTypeIdClonePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_clone_post_request = goadserver.ApiV1CampaignsTypeIdClonePostRequest() # ApiV1CampaignsTypeIdClonePostRequest |  (optional)

    try:
        # Clone a campaign and all its ads.
        api_response = api_instance.api_v1_campaigns_type_id_clone_post(type, id, api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_clone_post_request** | [**ApiV1CampaignsTypeIdClonePostRequest**](ApiV1CampaignsTypeIdClonePostRequest.md)|  | [optional] 

### Return type

[**ApiV1CampaignsTypeIdClonePost201Response**](ApiV1CampaignsTypeIdClonePost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Clone created. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Source campaign not found or not owned by caller. |  -  |
**422** | Clone failed (invalid type, schema mismatch, etc.). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_delete**
> ApiV1CampaignsTypeIdDelete200Response api_v1_campaigns_type_id_delete(type, id)

Soft-delete a campaign.

Sets `isdeleted=1`, `ispaused=1`, `dayactive=0`. The campaign and
its history remain in the database for billing/stats reconciliation
but stop serving immediately. Idempotent — deleting an already-
deleted campaign returns 404.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_delete200_response import ApiV1CampaignsTypeIdDelete200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Soft-delete a campaign.
        api_response = api_instance.api_v1_campaigns_type_id_delete(type, id)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeIdDelete200Response**](ApiV1CampaignsTypeIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found or already deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_filters_filter_type_filter_id_delete**
> api_v1_campaigns_type_id_filters_filter_type_filter_id_delete(type, id, filter_type, filter_id)

Detach a filter from this campaign.

Exclusion filter: removes the campaign id from the filter's
`campaignids` CSV (if the CSV becomes empty, falls back to "0"
meaning "applies to all campaigns" — same legacy sentinel).
Inclusion filter: clears the campaign's FK column only if it
currently points to this filter; otherwise returns 404.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    filter_type = 'filter_type_example' # str | 
    filter_id = 56 # int | 

    try:
        # Detach a filter from this campaign.
        api_instance.api_v1_campaigns_type_id_filters_filter_type_filter_id_delete(type, id, filter_type, filter_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_filters_filter_type_filter_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **filter_type** | **str**|  | 
 **filter_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detached |  -  |
**404** | Not attached / campaign not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_filters_get**
> ApiV1CampaignsTypeIdFiltersGet200Response api_v1_campaigns_type_id_filters_get(type, id)

List filters attached to this campaign.

Returns every filter (exclusion via `campaignids` membership,
inclusion via FK columns) currently linked to this campaign.
Only `ron` and `rtb` campaign types support filter linkage.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response import ApiV1CampaignsTypeIdFiltersGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # List filters attached to this campaign.
        api_response = api_instance.api_v1_campaigns_type_id_filters_get(type, id)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeIdFiltersGet200Response**](ApiV1CampaignsTypeIdFiltersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Linked filters |  -  |
**404** | Campaign not found |  -  |
**422** | Unsupported campaign type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_filters_post**
> ApiV1CampaignsTypeIdFiltersPost200Response api_v1_campaigns_type_id_filters_post(type, id, api_v1_campaigns_type_id_filters_post_request)

Attach a filter to this campaign.

For exclusion filters, appends the campaign id to the filter's
`campaignids` CSV. For inclusion filters, sets the campaign's
FK column to this filter (replacing any previous inclusion
filter of the same kind).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_filters_post200_response import ApiV1CampaignsTypeIdFiltersPost200Response
from goadserver.models.api_v1_campaigns_type_id_filters_post_request import ApiV1CampaignsTypeIdFiltersPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_filters_post_request = goadserver.ApiV1CampaignsTypeIdFiltersPostRequest() # ApiV1CampaignsTypeIdFiltersPostRequest | 

    try:
        # Attach a filter to this campaign.
        api_response = api_instance.api_v1_campaigns_type_id_filters_post(type, id, api_v1_campaigns_type_id_filters_post_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_filters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_filters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_filters_post_request** | [**ApiV1CampaignsTypeIdFiltersPostRequest**](ApiV1CampaignsTypeIdFiltersPostRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdFiltersPost200Response**](ApiV1CampaignsTypeIdFiltersPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attached |  -  |
**404** | Campaign or filter not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_get**
> object api_v1_campaigns_type_id_get(type, id)

Get a single campaign.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Get a single campaign.
        api_response = api_instance.api_v1_campaigns_type_id_get(type, id)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_min_bid_get**
> ApiV1CampaignsTypeIdMinBidGet200Response api_v1_campaigns_type_id_min_bid_get(type, id)

Get the campaign's minimum acceptable CPC bid.

Returns the floor the platform will accept for this campaign,
derived from the same logic the panel uses (admanager → effectively
zero, custom `fx_minprice`, or the `min_prices_ron` table matched
against the campaign's targeting). Use this before bulk-updating
bids so the optimiser doesn't push values below the floor and have
them clamped or rejected.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_min_bid_get200_response import ApiV1CampaignsTypeIdMinBidGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Get the campaign's minimum acceptable CPC bid.
        api_response = api_instance.api_v1_campaigns_type_id_min_bid_get(type, id)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_min_bid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_min_bid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ApiV1CampaignsTypeIdMinBidGet200Response**](ApiV1CampaignsTypeIdMinBidGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Minimum bid. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_post**
> api_v1_campaigns_type_post(type, api_v1_campaigns_type_post_request, dry_run=dry_run, strict=strict)

Create a new campaign (smart-default).

Creates a new campaign with sensible defaults applied for any
field you don't send. Required: `name` + `ad_type`. Everything
else (targeting, capping, schedule, …) defaults to "all/none"
unless explicitly supplied — see
`GET /api/v1/campaigns/{type}/_schema` for the full field list.

The campaign always starts paused (`is_paused=true`) so you can
attach ads via `POST /api/v1/campaigns/{type}/{id}/ads` and verify
before activating. Flip the active flag when ready via
`PATCH /api/v1/campaigns/{type}/{id}/active`.

**Modes:**
  - `?dry_run=1` — validate and return the resolved field map
    without inserting. Useful for previewing what an LLM would
    create before charging it.
  - `?strict=1` — reject unknown field names with a 422 listing
    them. Without this, unknown keys are silently ignored.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_post_request import ApiV1CampaignsTypePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    api_v1_campaigns_type_post_request = {"name":"My first API campaign","ad_type":2} # ApiV1CampaignsTypePostRequest | 
    dry_run = 'dry_run_example' # str |  (optional)
    strict = 'strict_example' # str |  (optional)

    try:
        # Create a new campaign (smart-default).
        api_instance.api_v1_campaigns_type_post(type, api_v1_campaigns_type_post_request, dry_run=dry_run, strict=strict)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **api_v1_campaigns_type_post_request** | [**ApiV1CampaignsTypePostRequest**](ApiV1CampaignsTypePostRequest.md)|  | 
 **dry_run** | **str**|  | [optional] 
 **strict** | **str**|  | [optional] 

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
**201** | Created. Body is the freshly-created campaign in the public projection (same shape as &#x60;GET /api/v1/campaigns/{type}/{id}&#x60;). |  -  |
**200** | When &#x60;?dry_run&#x3D;1&#x60; — body is &#x60;{ dry_run: true, resolved: ..., would_insert: ... }&#x60;. |  -  |
**422** | Validation error (missing required, unknown field with &#x60;?strict&#x3D;1&#x60;, …). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_schema_ads_get**
> ApiV1CampaignsTypeSchemaAdsGet200Response api_v1_campaigns_type_schema_ads_get(type)

Field metadata for ad creation.

Discovery endpoint mirroring `/_schema` for campaigns, scoped to
ads. Lists every public field a `POST /campaigns/{type}/{campaignId}/ads`
accepts, with type, required-flag, default, example, and
description. Also returns a `creative_choice` block reminding the
caller that exactly one of `banner_pool_id` / `creative_id` /
`banner_url` / `banner_html` / `video_pool_id` must be set.

Use the campaign-scoped variant
`/api/v1/campaigns/{type}/{campaignId}/_schema/ads` to get the
same payload narrowed to fields that apply to that specific
campaign's ad type (returns `campaign_ad_type` so AI agents know
which creative shape is appropriate).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_schema_ads_get200_response import ApiV1CampaignsTypeSchemaAdsGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 

    try:
        # Field metadata for ad creation.
        api_response = api_instance.api_v1_campaigns_type_schema_ads_get(type)
        print("The response of CampaignsApi->api_v1_campaigns_type_schema_ads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_schema_ads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**ApiV1CampaignsTypeSchemaAdsGet200Response**](ApiV1CampaignsTypeSchemaAdsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ad-create field metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_schema_get**
> ApiV1CampaignsTypeSchemaGet200Response api_v1_campaigns_type_schema_get(type)

Field metadata for create/update.

Discovery endpoint for AI agents and integrators. Returns the
canonical list of public field names a `POST /api/v1/campaigns/{type}`
accepts, with type, required-flag, default value, an example, and
a one-line description. `ad_type` enumerates the active ad-type
ids on the caller's tenant.

Use this to drive form UIs, validate agent-generated payloads
client-side, or feed into a function-calling LLM.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_schema_get200_response import ApiV1CampaignsTypeSchemaGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 

    try:
        # Field metadata for create/update.
        api_response = api_instance.api_v1_campaigns_type_schema_get(type)
        print("The response of CampaignsApi->api_v1_campaigns_type_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_schema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**ApiV1CampaignsTypeSchemaGet200Response**](ApiV1CampaignsTypeSchemaGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


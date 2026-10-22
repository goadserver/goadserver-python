# goadserver.CampaignsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_campaigns_cpm_campaign_id_spots_space_id_delete**](CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_delete) | **DELETE** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Remove an ad zone from a CPM campaign.
[**api_v1_campaigns_cpm_campaign_id_spots_space_id_post**](CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_post) | **POST** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Add an ad zone to a CPM campaign (or re-price it).
[**api_v1_campaigns_cpm_campaign_id_spots_space_id_put**](CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_put) | **PUT** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId} | Switch a CPM campaign&#39;s zone spot on or off.
[**api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put**](CampaignsApi.md#api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put) | **PUT** /api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}/{type} | Set a CPM zone spot&#39;s bid or state.
[**api_v1_campaigns_get**](CampaignsApi.md#api_v1_campaigns_get) | **GET** /api/v1/campaigns | List the caller&#39;s campaigns across all types (or one type).
[**api_v1_campaigns_mass_delete_post**](CampaignsApi.md#api_v1_campaigns_mass_delete_post) | **POST** /api/v1/campaigns/mass-delete | Soft-delete many campaigns.
[**api_v1_campaigns_mass_toggle_put**](CampaignsApi.md#api_v1_campaigns_mass_toggle_put) | **PUT** /api/v1/campaigns/mass-toggle | Pause or resume many campaigns at once.
[**api_v1_campaigns_mass_undelete_post**](CampaignsApi.md#api_v1_campaigns_mass_undelete_post) | **POST** /api/v1/campaigns/mass-undelete | Restore soft-deleted campaigns.
[**api_v1_campaigns_purge_post**](CampaignsApi.md#api_v1_campaigns_purge_post) | **POST** /api/v1/campaigns/purge | Permanently delete soft-deleted campaigns and their ads.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get) | **GET** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | List per-zone bid overrides for a RON ad.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put) | **PUT** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids | Replace the per-zone bid overrides on a RON ad.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete) | **DELETE** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/{zoneId} | Clear a single per-zone bid override.
[**api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put**](CampaignsApi.md#api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put) | **PUT** /api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/zones-only | Switch \&quot;only these zones\&quot; mode for a RON ad&#39;s per-zone bids.
[**api_v1_campaigns_ron_id_site_list_get**](CampaignsApi.md#api_v1_campaigns_ron_id_site_list_get) | **GET** /api/v1/campaigns/ron/{id}/site-list | The Premium-sites box of a RON campaign.
[**api_v1_campaigns_ron_id_site_list_site_id_put**](CampaignsApi.md#api_v1_campaigns_ron_id_site_list_site_id_put) | **PUT** /api/v1/campaigns/ron/{id}/site-list/{siteId} | Set one site of the Premium-sites box active or blocked.
[**api_v1_campaigns_ron_id_zones_get**](CampaignsApi.md#api_v1_campaigns_ron_id_zones_get) | **GET** /api/v1/campaigns/ron/{id}/zones | List the zones a RON campaign is linked to.
[**api_v1_campaigns_rtb_id_test_rtb_get**](CampaignsApi.md#api_v1_campaigns_rtb_id_test_rtb_get) | **GET** /api/v1/campaigns/rtb/{id}/test-rtb | Context for testing an RTB campaign&#39;s endpoint.
[**api_v1_campaigns_rtb_id_test_rtb_post**](CampaignsApi.md#api_v1_campaigns_rtb_id_test_rtb_post) | **POST** /api/v1/campaigns/rtb/{id}/test-rtb | Fire a test bid request at an RTB campaign&#39;s endpoint.
[**api_v1_campaigns_save_categories_put**](CampaignsApi.md#api_v1_campaigns_save_categories_put) | **PUT** /api/v1/campaigns/save-categories | Assign categories to many campaigns.
[**api_v1_campaigns_save_tags_put**](CampaignsApi.md#api_v1_campaigns_save_tags_put) | **PUT** /api/v1/campaigns/save-tags | Assign tags (campaign groups) to many campaigns.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/active | Pause or unpause a single ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch) | **PATCH** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bid | Set a single ad&#39;s bid.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bids-per-geo | Set per-country bids for a RON ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/clone | Clone a single ad within a campaign.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/countries | Set per-ad country targeting for a RON ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_delete**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_delete) | **DELETE** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Soft-delete an ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Show one ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/overlay-stats | Shoppable video — shown and clicks per overlay.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId} | Update an ad.
[**api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/{adId}/restore | Restore a deleted RON ad.
[**api_v1_campaigns_type_campaign_id_ads_copy_targets_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_copy_targets_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads/copy-targets | Campaigns this campaign&#39;s ads can be copied into.
[**api_v1_campaigns_type_campaign_id_ads_csv_import_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_csv_import_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/csv-import | Import native ads from a CSV — one ad per row, or one ad per group.
[**api_v1_campaigns_type_campaign_id_ads_from_pool_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_from_pool_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/from-pool | Create ads from a creative pool.
[**api_v1_campaigns_type_campaign_id_ads_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/ads | List ads on a campaign.
[**api_v1_campaigns_type_campaign_id_ads_mass_clone_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_clone_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-clone | Copy many ads of a campaign.
[**api_v1_campaigns_type_campaign_id_ads_mass_delete_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_delete_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-delete | Soft-delete many ads of a campaign.
[**api_v1_campaigns_type_campaign_id_ads_mass_toggle_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_toggle_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/mass-toggle | Activate or pause many ads of a campaign at once.
[**api_v1_campaigns_type_campaign_id_ads_multi_upload_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_multi_upload_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/multi-upload | Bulk-upload ads — one ad per creative file.
[**api_v1_campaigns_type_campaign_id_ads_post**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads | Create an ad on a campaign (smart-default).
[**api_v1_campaigns_type_campaign_id_ads_update_pool_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_pool_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-pool | Point many ads at a different creative pool.
[**api_v1_campaigns_type_campaign_id_ads_update_url_pool_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_url_pool_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-url-pool | Point many ads at a URL pool, or detach it.
[**api_v1_campaigns_type_campaign_id_ads_update_url_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_url_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-url | Rewrite the destination URL of many ads at once.
[**api_v1_campaigns_type_campaign_id_ads_update_weight_put**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_ads_update_weight_put) | **PUT** /api/v1/campaigns/{type}/{campaignId}/ads/update-weight | Set the rotation weight of one or more RON ads.
[**api_v1_campaigns_type_campaign_id_schema_ads_get**](CampaignsApi.md#api_v1_campaigns_type_campaign_id_schema_ads_get) | **GET** /api/v1/campaigns/{type}/{campaignId}/_schema/ads | Field metadata for ad creation, scoped to a campaign.
[**api_v1_campaigns_type_id_active_patch**](CampaignsApi.md#api_v1_campaigns_type_id_active_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/active | Pause or unpause a campaign.
[**api_v1_campaigns_type_id_available_zones_get**](CampaignsApi.md#api_v1_campaigns_type_id_available_zones_get) | **GET** /api/v1/campaigns/{type}/{id}/available-zones | List your ad zones that can be attached to a campaign.
[**api_v1_campaigns_type_id_bids_patch**](CampaignsApi.md#api_v1_campaigns_type_id_bids_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/bids | Mass update bids on every ad in a campaign.
[**api_v1_campaigns_type_id_budget_patch**](CampaignsApi.md#api_v1_campaigns_type_id_budget_patch) | **PATCH** /api/v1/campaigns/{type}/{id}/budget | Update a campaign&#39;s total and/or daily budget.
[**api_v1_campaigns_type_id_clone_post**](CampaignsApi.md#api_v1_campaigns_type_id_clone_post) | **POST** /api/v1/campaigns/{type}/{id}/clone | Clone a campaign — everything, or the parts you pick.
[**api_v1_campaigns_type_id_delete**](CampaignsApi.md#api_v1_campaigns_type_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id} | Soft-delete a campaign.
[**api_v1_campaigns_type_id_filters_filter_type_filter_id_delete**](CampaignsApi.md#api_v1_campaigns_type_id_filters_filter_type_filter_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id}/filters/{filter_type}/{filter_id} | Detach a filter from this campaign.
[**api_v1_campaigns_type_id_filters_get**](CampaignsApi.md#api_v1_campaigns_type_id_filters_get) | **GET** /api/v1/campaigns/{type}/{id}/filters | List filters attached to this campaign.
[**api_v1_campaigns_type_id_filters_post**](CampaignsApi.md#api_v1_campaigns_type_id_filters_post) | **POST** /api/v1/campaigns/{type}/{id}/filters | Attach a filter to this campaign.
[**api_v1_campaigns_type_id_get**](CampaignsApi.md#api_v1_campaigns_type_id_get) | **GET** /api/v1/campaigns/{type}/{id} | Get a single campaign.
[**api_v1_campaigns_type_id_min_bid_get**](CampaignsApi.md#api_v1_campaigns_type_id_min_bid_get) | **GET** /api/v1/campaigns/{type}/{id}/min-bid | Get the campaign&#39;s minimum acceptable CPC bid.
[**api_v1_campaigns_type_id_patch**](CampaignsApi.md#api_v1_campaigns_type_id_patch) | **PATCH** /api/v1/campaigns/{type}/{id} | Partially update a campaign.
[**api_v1_campaigns_type_id_reset_max_budget_put**](CampaignsApi.md#api_v1_campaigns_type_id_reset_max_budget_put) | **PUT** /api/v1/campaigns/{type}/{id}/reset-max-budget | Reset a campaign&#39;s lifetime-budget spend.
[**api_v1_campaigns_type_id_sites_get**](CampaignsApi.md#api_v1_campaigns_type_id_sites_get) | **GET** /api/v1/campaigns/{type}/{id}/sites | Your sites that have zones attachable to a campaign.
[**api_v1_campaigns_type_id_whitelist_zones_get**](CampaignsApi.md#api_v1_campaigns_type_id_whitelist_zones_get) | **GET** /api/v1/campaigns/{type}/{id}/whitelist-zones | List the ad zones attached to a campaign.
[**api_v1_campaigns_type_id_zones_post**](CampaignsApi.md#api_v1_campaigns_type_id_zones_post) | **POST** /api/v1/campaigns/{type}/{id}/zones | Attach ad zones to a campaign.
[**api_v1_campaigns_type_id_zones_zone_id_delete**](CampaignsApi.md#api_v1_campaigns_type_id_zones_zone_id_delete) | **DELETE** /api/v1/campaigns/{type}/{id}/zones/{zoneId} | Detach an ad zone from a campaign.
[**api_v1_campaigns_type_id_zones_zone_id_weight_put**](CampaignsApi.md#api_v1_campaigns_type_id_zones_zone_id_weight_put) | **PUT** /api/v1/campaigns/{type}/{id}/zones/{zoneId}/weight | Set an attached zone&#39;s weight for this campaign.
[**api_v1_campaigns_type_post**](CampaignsApi.md#api_v1_campaigns_type_post) | **POST** /api/v1/campaigns/{type} | Create a new campaign (smart-default).
[**api_v1_campaigns_type_schema_ads_get**](CampaignsApi.md#api_v1_campaigns_type_schema_ads_get) | **GET** /api/v1/campaigns/{type}/_schema/ads | Field metadata for ad creation.
[**api_v1_campaigns_type_schema_get**](CampaignsApi.md#api_v1_campaigns_type_schema_get) | **GET** /api/v1/campaigns/{type}/_schema | Field metadata for create/update.
[**api_v1_rtb_test_rtb_context_get**](CampaignsApi.md#api_v1_rtb_test_rtb_context_get) | **GET** /api/v1/rtb/test-rtb/context | Context for testing an endpoint before the campaign exists.
[**api_v1_rtb_test_rtb_post**](CampaignsApi.md#api_v1_rtb_test_rtb_post) | **POST** /api/v1/rtb/test-rtb | Fire a test bid request at any endpoint URL.
[**api_v1_tools_replace_domain_put**](CampaignsApi.md#api_v1_tools_replace_domain_put) | **PUT** /api/v1/tools/replace-domain | Replace the landing domain across your RON ads.


# **api_v1_campaigns_cpm_campaign_id_spots_space_id_delete**
> api_v1_campaigns_cpm_campaign_id_spots_space_id_delete(campaign_id, space_id)

Remove an ad zone from a CPM campaign.

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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    space_id = 56 # int | 

    try:
        # Remove an ad zone from a CPM campaign.
        api_instance.api_v1_campaigns_cpm_campaign_id_spots_space_id_delete(campaign_id, space_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_cpm_campaign_id_spots_space_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **space_id** | **int**|  | 

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
**200** | Removed. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found, or &#x60;spot_not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_cpm_campaign_id_spots_space_id_post**
> api_v1_campaigns_cpm_campaign_id_spots_space_id_post(campaign_id, space_id, api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request)

Add an ad zone to a CPM campaign (or re-price it).

Adds the zone as a spot of the campaign, or updates the bid when
it is already one. `cpm` 0 / omitted takes the zone's minimum CPM;
a `cpm` under the minimum is raised to it; a Mini Network peer
zone is also raised to the floor its publisher set for you. The
zone must be yours or shared with you through an accepted Mini
Network pair. Spot activity is recalculated from the campaign's
ads. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    space_id = 56 # int | Ad zone id.
    api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request = {"cpm":250,"bid_type":0} # ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest |  (optional)

    try:
        # Add an ad zone to a CPM campaign (or re-price it).
        api_instance.api_v1_campaigns_cpm_campaign_id_spots_space_id_post(campaign_id, space_id, api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_cpm_campaign_id_spots_space_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **space_id** | **int**| Ad zone id. | 
 **api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request** | [**ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest**](ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest.md)|  | [optional] 

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
**201** | Spot saved (&#x60;cpm&#x60; is the stored, possibly raised, value). |  -  |
**400** | &#x60;invalid_campaign_id&#x60; / &#x60;invalid_space_id&#x60;. |  -  |
**403** | &#x60;forbidden&#x60; — the zone is not shared with you; or a pinned key. |  -  |
**404** | Campaign (not a CPM / flat-request campaign of yours) or zone not found. |  -  |
**500** | The Mini Network floor could not be read — retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_cpm_campaign_id_spots_space_id_put**
> api_v1_campaigns_cpm_campaign_id_spots_space_id_put(campaign_id, space_id)

Switch a CPM campaign's zone spot on or off.

Without a sub-path this toggles the spot's `isinuse`. Use
`PUT …/spots/{spaceId}/bidding` to set the bid and
`…/state` to set state explicitly. Same handler as the panel.


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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    space_id = 56 # int | 

    try:
        # Switch a CPM campaign's zone spot on or off.
        api_instance.api_v1_campaigns_cpm_campaign_id_spots_space_id_put(campaign_id, space_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_cpm_campaign_id_spots_space_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **space_id** | **int**|  | 

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
**200** | Toggled. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found, or &#x60;zone_not_found&#x60; — not a spot of this campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put**
> api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put(campaign_id, space_id, type, api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request)

Set a CPM zone spot's bid or state.

`type=bidding`: `cpm` (cents CPM) > 0 sets the bid, raised to the
zone's minimum and any Mini Network floor; `user_bid` defaults to
`cpm`. `bid_type` (1 = smart bidding) and `isinuse` (1 on, 0 off)
change only when sent.

`type=state`: `state` (-1, 0 or 1) and/or `isinuse`, each only when
sent. The state is recalculated from the campaign's ads right
after, so it mostly reflects ad availability.

Any other `type` toggles `isinuse` like the plain PUT. Same
handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    space_id = 56 # int | 
    type = 'type_example' # str | 
    api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request = {"cpm":320} # ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest | 

    try:
        # Set a CPM zone spot's bid or state.
        api_instance.api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put(campaign_id, space_id, type, api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **space_id** | **int**|  | 
 **type** | **str**|  | 
 **api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request** | [**ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest**](ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest.md)|  | 

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found, or &#x60;zone_not_found&#x60; — not a spot of this campaign. |  -  |
**500** | The Mini Network floor could not be read — retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_get**
> ApiV1CampaignsGet200Response api_v1_campaigns_get(type=type, deleted=deleted, page=page, per_page=per_page, fields=fields)

List the caller's campaigns across all types (or one type).

Returns the caller's campaigns. By default each row carries a
rich-but-bounded projection: identity (`id`, `name`, `campaign_type`,
`ad_type` + `ad_type_label`, `selling_type`), lifecycle
(`is_paused`, `is_active`, `is_deleted`, `is_complete`,
`pending_state`), budget in main currency units (`daily_budget`,
`total_budget`, `total_spent`, `use_campaign_budget`), impression limits
(`use_maxday_impressions` / `maxday_impressions` per day and
`use_maxtotal_impressions` / `maxtotal_impressions` for the
campaign's lifetime), targeting summary (`countries`,
`languages`, `categories`, `device_type_ids`, …), capping,
schedule (`use_start_date` / `start_date`, `use_end_date` /
`end_date`), linked filter/pool ids, the campaign-form fields of
`CampaignPanelFields` the row carries, and timestamps. The list
does not read the options column, so option fields other than
`priority` (`day_parting`, `av_check`, …) are returned by
`GET /api/v1/campaigns/{type}/{id}` only. Spend per day and ad bids
are not part of the campaign row — use `/api/v1/stats` and the ad
endpoints.

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
    api_instance = goadserver.CampaignsApi(api_client)
    type = all # str |  (optional) (default to all)
    deleted = True # bool | true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)
    fields = 'fields_example' # str | CSV of fields to return; `*` returns everything available. (optional)

    try:
        # List the caller's campaigns across all types (or one type).
        api_response = api_instance.api_v1_campaigns_get(type=type, deleted=deleted, page=page, per_page=per_page, fields=fields)
        print("The response of CampaignsApi->api_v1_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to all]
 **deleted** | **bool**| true / 1 &#x3D; list the soft-deleted campaigns instead (the panel&#39;s Deleted view); restore them with POST /api/v1/campaigns/mass-undelete. | [optional] 
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

# **api_v1_campaigns_mass_delete_post**
> api_v1_campaigns_mass_delete_post(api_v1_campaigns_mass_delete_post_request)

Soft-delete many campaigns.

Marks every listed campaign you own deleted (`isdeleted = 1`; flat
deals and direct deals: `iscancelled = 1`). Their live ads are
soft-deleted with them (marked as deleted-with-the-campaign), and
`POST /api/v1/campaigns/mass-undelete` brings the campaigns and
those ads back exactly as they were. A ron flat campaign's pending
marketplace flat-deal request is cancelled. Unlike the single
`DELETE /api/v1/campaigns/{type}/{id}` this does not refuse a flat
campaign with a live deal. Same handler as the panel. On a network
that reviews campaign deletes, live ron campaigns go to Pending
Delete instead and keep running until approved: `affected` counts
what was deleted, `pending_review` what was sent for approval.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_mass_delete_post_request = {"ids":[445071,445072],"type":"ron"} # ApiV1CampaignsMassDeletePostRequest | 

    try:
        # Soft-delete many campaigns.
        api_instance.api_v1_campaigns_mass_delete_post(api_v1_campaigns_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_mass_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_mass_delete_post_request** | [**ApiV1CampaignsMassDeletePostRequest**](ApiV1CampaignsMassDeletePostRequest.md)|  | 

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
**400** | &#x60;no_ids&#x60; / &#x60;invalid_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_mass_toggle_put**
> api_v1_campaigns_mass_toggle_put(api_v1_campaigns_mass_toggle_put_request)

Pause or resume many campaigns at once.

Writes `ispaused` for every listed campaign you own. Same handler
as the panel's bulk Pause / Resume buttons, and like them it skips
the per-campaign checks `PATCH …/{id}/active` makes (flat-deal
rules, lifetime-budget cap): a campaign resumed here that is at
its budget cap pauses itself again within about a minute. Use
`PATCH /api/v1/campaigns/{type}/{id}/active` when you want those
checks.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_mass_toggle_put_request import ApiV1CampaignsMassTogglePutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_mass_toggle_put_request = {"ids":[445071,445072],"type":"ron","pause":true} # ApiV1CampaignsMassTogglePutRequest | 

    try:
        # Pause or resume many campaigns at once.
        api_instance.api_v1_campaigns_mass_toggle_put(api_v1_campaigns_mass_toggle_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_mass_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_mass_toggle_put_request** | [**ApiV1CampaignsMassTogglePutRequest**](ApiV1CampaignsMassTogglePutRequest.md)|  | 

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
**200** | Done. &#x60;affected&#x60; counts rows whose state changed; &#x60;pending&#x60; how many of those went to an admin for approval (Pending Pause / Pending Active) because the network validates campaign changes. |  -  |
**400** | &#x60;no_ids&#x60; — empty &#x60;ids&#x60;; &#x60;invalid_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_mass_undelete_post**
> api_v1_campaigns_mass_undelete_post(api_v1_campaigns_mass_delete_post_request)

Restore soft-deleted campaigns.

Undoes a delete: `isdeleted = 0` (flat / direct deals:
`iscancelled = 0`) for every listed campaign you own that is
currently deleted. This is how a `DELETE /api/v1/campaigns/{type}/{id}`
or a `mass-delete` is reversed. Find deleted campaigns with
`GET /api/v1/campaigns?deleted=1`.

The ads the delete took down with the campaign come back too; ads
you had deleted one by one before stay deleted. A ron / cpm / rtb
campaign returns paused or running as it was before the delete; a
flat / direct deal deleted with the single `DELETE` comes back
paused (resume it with `PATCH …/{id}/active`). Ads deleted together
with a campaign before 2026-10-13 cannot be told apart from ones
deleted individually and stay deleted — bring RON ads back with
`PUT /api/v1/campaigns/ron/{campaignId}/ads/{adId}/restore` (list
them with `GET …/ads?ad_state=3`). A purged campaign cannot be
restored. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_mass_delete_post_request = {"ids":[445071],"type":"ron"} # ApiV1CampaignsMassDeletePostRequest | 

    try:
        # Restore soft-deleted campaigns.
        api_instance.api_v1_campaigns_mass_undelete_post(api_v1_campaigns_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_mass_undelete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_mass_delete_post_request** | [**ApiV1CampaignsMassDeletePostRequest**](ApiV1CampaignsMassDeletePostRequest.md)|  | 

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
**200** | Done. Ids that were not deleted are not counted. |  -  |
**400** | &#x60;no_ids&#x60; / &#x60;invalid_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_purge_post**
> api_v1_campaigns_purge_post(api_v1_campaigns_mass_delete_post_request)

Permanently delete soft-deleted campaigns and their ads.

Hard-deletes listed campaigns that are already soft-deleted, with
their ads. Irreversible — the rows are snapshotted into the action
log first, but nothing can restore them. Ids that are not deleted
(or not yours) are skipped. Same handler as the panel's Purge.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_mass_delete_post_request = {ids=[445071], type=ron} # ApiV1CampaignsMassDeletePostRequest | 

    try:
        # Permanently delete soft-deleted campaigns and their ads.
        api_instance.api_v1_campaigns_purge_post(api_v1_campaigns_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_purge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_mass_delete_post_request** | [**ApiV1CampaignsMassDeletePostRequest**](ApiV1CampaignsMassDeletePostRequest.md)|  | 

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
**200** | Done. &#x60;affected&#x60; &#x3D; rows removed (0 when no listed id was deleted). |  -  |
**400** | &#x60;no_ids&#x60; / &#x60;invalid_type&#x60;. |  -  |
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

# **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put**
> api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put(campaign_id, ad_id, api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request)

Switch \"only these zones\" mode for a RON ad's per-zone bids.

When on, the ad serves **only** on the zones listed in its
per-zone bid map (`GET/PUT …/zone-bids`) — the panel's "only
these zones" switch on the Bids per zone tab. When off (default)
the zone bids are overrides and every other zone uses the ad bid.
Same write as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request = {"bids_per_zone_only":true} # ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest | 

    try:
        # Switch \"only these zones\" mode for a RON ad's per-zone bids.
        api_instance.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put(campaign_id, ad_id, api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request** | [**ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest**](ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest.md)|  | 

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found on this campaign. |  -  |
**422** | &#x60;bids_per_zone_only&#x60; missing, or an unknown field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_id_site_list_get**
> api_v1_campaigns_ron_id_site_list_get(id, main_catid=main_catid, catids=catids)

The Premium-sites box of a RON campaign.

The tenant's site list filtered to the campaign's categories, each
with this campaign's status (1 active, 0 blocked). Shown only when
the tenant switched the Sites box on for your account or for all
users; otherwise `visible: false` and an empty `data`. `editable`
is false when an admin made this campaign's list read only.
Optional `main_catid` + `catids` filter on categories other than
the saved ones. Display only — the ad server does not read it.
Same handler as the panel.


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
    api_instance = goadserver.CampaignsApi(api_client)
    id = 56 # int | 
    main_catid = 56 # int |  (optional)
    catids = 'catids_example' # str | Comma-separated category ids, with main_catid. (optional)

    try:
        # The Premium-sites box of a RON campaign.
        api_instance.api_v1_campaigns_ron_id_site_list_get(id, main_catid=main_catid, catids=catids)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_id_site_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **main_catid** | **int**|  | [optional] 
 **catids** | **str**| Comma-separated category ids, with main_catid. | [optional] 

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
**200** | Sites box. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_id_site_list_site_id_put**
> api_v1_campaigns_ron_id_site_list_site_id_put(id, site_id, api_v1_campaigns_ron_id_site_list_site_id_put_request)

Set one site of the Premium-sites box active or blocked.

`status` 1 = active, 0 = blocked. Refused (403) when the Sites box
is not on for you or the campaign's list is read only. Setting a
site active needs the tenant's minimum balance for Premium sites
(422 with code `premium_sites_min_balance` and `amount`); blocking
is always allowed. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_id_site_list_site_id_put_request import ApiV1CampaignsRonIdSiteListSiteIdPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    id = 56 # int | 
    site_id = 56 # int | 
    api_v1_campaigns_ron_id_site_list_site_id_put_request = {"status":0} # ApiV1CampaignsRonIdSiteListSiteIdPutRequest | 

    try:
        # Set one site of the Premium-sites box active or blocked.
        api_instance.api_v1_campaigns_ron_id_site_list_site_id_put(id, site_id, api_v1_campaigns_ron_id_site_list_site_id_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_id_site_list_site_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **site_id** | **int**|  | 
 **api_v1_campaigns_ron_id_site_list_site_id_put_request** | [**ApiV1CampaignsRonIdSiteListSiteIdPutRequest**](ApiV1CampaignsRonIdSiteListSiteIdPutRequest.md)|  | 

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
**403** | &#x60;forbidden&#x60; — the box is not on for you or is read only; or a pinned key. |  -  |
**404** | Campaign or site not found. |  -  |
**422** | &#x60;validation_error&#x60; — status not 0/1; or the Premium-sites minimum balance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_ron_id_zones_get**
> ApiV1CampaignsRonIdZonesGet200Response api_v1_campaigns_ron_id_zones_get(id)

List the zones a RON campaign is linked to.

The campaign's whitelist zones, the same list the panel shows on the
campaign's Ad Zones step: zone id, zone name, site and the campaign's
weight on that zone. The raw id list is also available as
`wl_zoneids` on `GET /api/v1/campaigns/ron/{id}?fields=*`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_ron_id_zones_get200_response import ApiV1CampaignsRonIdZonesGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    id = 56 # int | 

    try:
        # List the zones a RON campaign is linked to.
        api_response = api_instance.api_v1_campaigns_ron_id_zones_get(id)
        print("The response of CampaignsApi->api_v1_campaigns_ron_id_zones_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_ron_id_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CampaignsRonIdZonesGet200Response**](ApiV1CampaignsRonIdZonesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Linked zones (empty &#x60;data&#x60; when the campaign has none). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_rtb_id_test_rtb_get**
> api_v1_campaigns_rtb_id_test_rtb_get(id)

Context for testing an RTB campaign's endpoint.

The campaign's `request_url`, `rtbtype` and ad type, the network's common banner sizes, and the caller's IP / user agent (the defaults the test sends). Same handler as the panel.

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
    api_instance = goadserver.CampaignsApi(api_client)
    id = 56 # int | 

    try:
        # Context for testing an RTB campaign's endpoint.
        api_instance.api_v1_campaigns_rtb_id_test_rtb_get(id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_rtb_id_test_rtb_get: %s\n" % e)
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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found (or the RTB module is off). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_rtb_id_test_rtb_post**
> RtbTestResult api_v1_campaigns_rtb_id_test_rtb_post(id, rtb_test_request=rtb_test_request)

Fire a test bid request at an RTB campaign's endpoint.

Sends one bid-style request to the campaign's `request_url` (or
`override_url`) the way the ad server would — OpenRTB 2.6 POST for
`openrtb`, GET with macros for `json` / `json_bidder` / `xml` — and
returns what was sent, what came back and a `verdict`: `ok` (a
bid), `no_bid`, `http_error`, `network_error`. Only public hosts
are reached (private / loopback / metadata addresses are refused
with `error_category: blocked_url`). `bidfloor` and `best_price`
are in the request's currency units (`currency`, default USD).
Nothing is stored. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.rtb_test_request import RtbTestRequest
from goadserver.models.rtb_test_result import RtbTestResult
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
    api_instance = goadserver.CampaignsApi(api_client)
    id = 56 # int | 
    rtb_test_request = {"width":300,"height":250,"country":"US","domain":"example.com","bidfloor":0.5} # RtbTestRequest |  (optional)

    try:
        # Fire a test bid request at an RTB campaign's endpoint.
        api_response = api_instance.api_v1_campaigns_rtb_id_test_rtb_post(id, rtb_test_request=rtb_test_request)
        print("The response of CampaignsApi->api_v1_campaigns_rtb_id_test_rtb_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_rtb_id_test_rtb_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **rtb_test_request** | [**RtbTestRequest**](RtbTestRequest.md)|  | [optional] 

### Return type

[**RtbTestResult**](RtbTestResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test result (also for a failed endpoint — see verdict). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found (or the RTB module is off). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_save_categories_put**
> api_v1_campaigns_save_categories_put(api_v1_campaigns_save_categories_put_request)

Assign categories to many campaigns.

Adds the category ids in `categories` (GET /api/v1/lookups/categories)
to every listed campaign; `overwrite: true` replaces the campaigns'
categories instead. Unknown category ids are dropped; none left →
400 `no_categories`. Same handler as the panel's bulk Categories.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_save_categories_put_request import ApiV1CampaignsSaveCategoriesPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_save_categories_put_request = {"ids":[445071],"type":"ron","categories":[3,7],"overwrite":true} # ApiV1CampaignsSaveCategoriesPutRequest | 

    try:
        # Assign categories to many campaigns.
        api_instance.api_v1_campaigns_save_categories_put(api_v1_campaigns_save_categories_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_save_categories_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_save_categories_put_request** | [**ApiV1CampaignsSaveCategoriesPutRequest**](ApiV1CampaignsSaveCategoriesPutRequest.md)|  | 

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
**400** | &#x60;no_ids&#x60;, &#x60;invalid_type&#x60;, or &#x60;no_categories&#x60; (no valid category id). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_save_tags_put**
> api_v1_campaigns_save_tags_put(api_v1_campaigns_save_tags_put_request)

Assign tags (campaign groups) to many campaigns.

Adds the tag ids in `tags` to every listed campaign (`groupid`);
with `clear: true` the campaigns' tags are replaced by `tags`
(an empty `tags` + `clear: true` removes all). Tag ids come from
the campaign tags list. Same handler as the panel's bulk Tags.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_save_tags_put_request import ApiV1CampaignsSaveTagsPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_campaigns_save_tags_put_request = {"ids":[445071,445072],"type":"ron","tags":[12],"clear":false} # ApiV1CampaignsSaveTagsPutRequest | 

    try:
        # Assign tags (campaign groups) to many campaigns.
        api_instance.api_v1_campaigns_save_tags_put(api_v1_campaigns_save_tags_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_save_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_campaigns_save_tags_put_request** | [**ApiV1CampaignsSaveTagsPutRequest**](ApiV1CampaignsSaveTagsPutRequest.md)|  | 

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
**400** | &#x60;no_ids&#x60; / &#x60;invalid_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch**
> ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch(type, campaign_id, ad_id, api_v1_campaigns_type_id_active_patch_request)

Pause or unpause a single ad.

Idempotent set. `active=true` activates the ad, `active=false`
pauses it. Useful for granular pause/resume from an optimiser
without touching the campaign-level pause state.

Same effect as the panel's ad toggle: the pause/activate
notification is sent, CPM zone states are recomputed, and on
networks that validate changes to whitelist-zone RON campaigns
the change is queued for approval — `pending_validation: true`
in the response.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
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

[**ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response.md)

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

Updates one ad's bid.

Bids are in **currency units of your account's currency** (`0.05` =
0.05), the same as the panel, and must be at least
`GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is
allowed and stops the ad bidding). Reads return the bid as
`bid_amount` in the same unit; `user_bid` / `bid` are the stored
values in cents (your currency / the network's main currency). Keys
that wrote bids before 2026-10-12 keep the old raw-cents contract;
every bid write echoes `bid_unit` (`currency` or `raw_cents`).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
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

# **api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put**
> api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request)

Set per-country bids for a RON ad.

Replaces the ad's whole per-country bid map (`ronads.bids_per_geo`)
— send every country you want to keep; `[]` clears it. A bid of 0
removes that country. On CPC / CPM campaigns the ad server uses the
visitor country's bid in place of the ad bid (and skips smart
bidding for that impression).

**Unit** — the same contract as the ad `bid` writes, echoed as
`bid_unit`:

- `currency` (every key minted normally): the bid is in the
  advertiser's own currency, e.g. `0.08`. Stored as sent — this
  column is kept in currency units (the ad server multiplies by 100
  and converts to the network currency when it loads the ad), the
  same as the panel's Bids per country tab.
- `raw_cents` (keys on the grandfathered raw-bid contract): send
  cents, as for that key's ad bids (`8` = 0.08); divided by 100
  before storage.

Per-country bids are not held to the ad format's minimum bid (the
panel does not check it either). Codes are two-letter country codes
(case-insensitive, stored lowercase). Unknown fields → 422. RON
campaigns only (`type` must be `ron`, else 400 `invalid_type`).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request = {"geo_bids":[{"code":"US","bid":0.08},{"code":"DE","bid":0.05}]} # ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest | 

    try:
        # Set per-country bids for a RON ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest**](ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest.md)|  | 

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
**200** | Saved. &#x60;bids_per_geo&#x60; is the stored map in the caller&#39;s unit. |  -  |
**400** | &#x60;invalid_type&#x60; — not a RON campaign; &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found on this campaign. |  -  |
**422** | Malformed body / unknown field, &#x60;geo_bids&#x60; missing, bad country code or negative bid. |  -  |

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

# **api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put**
> api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request)

Set per-ad country targeting for a RON ad.

Narrows one ad to a subset of countries (`ronads.countries`). An
empty list means the ad runs wherever the campaign runs (the
default). Codes are lowercased, de-duplicated and checked against
the country table; unknown codes are dropped. The stored list is
capped at 255 characters (~85 countries) → 422. Applies to every
paytype. Same handler as the panel. RON campaigns only.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request = {"countries":["us","ca"]} # ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest | 

    try:
        # Set per-ad country targeting for a RON ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest**](ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest.md)|  | 

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
**400** | &#x60;invalid_type&#x60; — not a RON campaign. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found on this campaign. |  -  |
**422** | Too many countries. |  -  |

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

# **api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get**
> api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get(type, campaign_id, ad_id, var_from=var_from, to=to)

Shoppable video — shown and clicks per overlay.

Per overlay of the ad's video_overlays (index = position in the list):
how often it came on screen and how often it was clicked, with the
click-through rate in percent. `from` / `to` (YYYY-MM-DD, UTC days,
default the last 30 days, at most a year). Overlays removed from the
ad since keep their numbers as type `removed`. The clicks are also
the ad's own clicks in the normal stats.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    var_from = '2013-10-20' # date |  (optional)
    to = '2013-10-20' # date |  (optional)

    try:
        # Shoppable video — shown and clicks per overlay.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get(type, campaign_id, ad_id, var_from=var_from, to=to)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **ad_id** | **int**|  | 
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

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
**200** | &#x60;data&#x60; &#x3D; rows &#x60;{overlay, type, name, shown, clicks, ctr}&#x60;, plus &#x60;from&#x60; / &#x60;to&#x60;. |  -  |
**404** | Ad not found (or not a ron ad). |  -  |
**422** | &#x60;validation_error&#x60;: from / to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_put**
> api_v1_campaigns_type_campaign_id_ads_ad_id_put(type, campaign_id, ad_id, api_v1_campaigns_type_campaign_id_ads_ad_id_put_request)

Update an ad.

Partial update — the same handler the panel's ad form saves
through, with the same validation (per-format minimum bid,
destination-URL rules, SmartAds `{spaceid}`, html video zones,
native SmartAd html-only, creator pool orientation). Send only
the fields to change. Accepts JSON or `multipart/form-data`
(multipart adds the file inputs `banner_file`, `icon_file`,
`image_file`, `video_file`, which replace that creative slot).

Field names are the ad's column names. The create-style names
`destination_url`, `display_url`, `preview_url`, `is_active`,
`url_pool_id` are accepted as aliases (the column name wins if
both are sent), so a create payload can be reused here.

Which columns exist depends on the campaign type: ron / cpm ads
take every field below; flatrate / directdeal ads have no
bid / sort / keyword / imptracking / icon / SmartAds columns,
and those keys are dropped there. Unknown keys are ignored
(not an error). `bansizeid` is locked after create and ignored.

Changing the destination URL (or rebuilding the creative) sends
the ad back to review unless your account is auto-validated.

**Creative inputs** (rebuild the `creatives` blob, panel
vocabulary): `banner_type` (`creative` / `pool` /
`hotlink_image` / `hotlink_video` / `iframe` / `html`) with
`creative_id` / `banner_pool_id` / `banner_url` /
`banner_iframe_url` / `banner_html`; `image_type` (`creative` /
`pool` / `html` / `none`) with `creative_id` / `image_pool_id` /
`image_url` / `html_code` + `html_total_items` (`none` = native
text-only ad); `video_type` (`url` / `xml` / `html` / `creative` /
`pool`) with `video_url` / `html_code` / `creative_id` /
`video_pool_id`; `icon_type: creative` + `icon_id` (push icon).
Or send `creatives` itself (object, as GET returns it, or a JSON
string) to write the blob verbatim.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_ad_id_put_request = {"bid":0.06,"destination_url":"https://example.com/new-lander?cid={clickid}"} # ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest | 

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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**400** | &#x60;no_fields&#x60; — nothing to update. |  -  |
**404** | Ad not found. |  -  |
**413** | &#x60;payload_too_large&#x60;. |  -  |
**422** | Validation error (bid floor, URL, SmartAds macro, creative mode). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put**
> api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put(type, campaign_id, ad_id)

Restore a deleted RON ad.

Undoes a soft delete (`is_deleted = 0`, `pending_state = 0`). The
ad comes back in the state it was deleted in. List deleted ads
with `GET …/ads?ad_state=3`. Same handler as the panel. RON
campaigns only.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Restore a deleted RON ad.
        api_instance.api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put(type, campaign_id, ad_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Restored. |  -  |
**400** | &#x60;invalid_type&#x60; — not a RON campaign. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad not found on this campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_copy_targets_get**
> api_v1_campaigns_type_campaign_id_ads_copy_targets_get(type, campaign_id)

Campaigns this campaign's ads can be copied into.

Your live campaigns (other than this one) whose ads share this
campaign's ad format: RON and CPM, flat deals and direct deals,
RTB alone. Use an `id` as `target_campaign_id` on `…/ads/mass-clone`.
Narrowed to a key's campaign pin. Same handler as the panel's
Copy to campaign… picker.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 

    try:
        # Campaigns this campaign's ads can be copied into.
        api_instance.api_v1_campaigns_type_campaign_id_ads_copy_targets_get(type, campaign_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_copy_targets_get: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Candidate campaigns, newest first per type. |  -  |
**400** | &#x60;invalid_campaign_type&#x60;, &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_csv_import_post**
> ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response api_v1_campaigns_type_campaign_id_ads_csv_import_post(type, campaign_id, file, image_column=image_column, url_column=url_column, name_column=name_column, group_column=group_column, groups=groups, folder_id=folder_id, folder_name=folder_name, folder_per_group=folder_per_group, name_prefix=name_prefix, square_mode=square_mode, pad_color=pad_color, crop_square=crop_square, set_active=set_active, bid=bid)

Import native ads from a CSV — one ad per row, or one ad per group.

`multipart/form-data`. Field `file` is a CSV (comma, semicolon or
tab separated) with a header row. Each row names an image URL,
a destination URL and optionally an ad name; the server fetches
the image (public http/https only, max 20 MB), centre-crops it to
1:1 — by default PADDING the whole image onto a square canvas rather
than cropping it, since a centre crop on a wide video still routinely
removes the subject (`square_mode`) — and creates one native ad. Columns are
chosen by header name via `image_column` / `url_column` /
`name_column`, or guessed from common names (`image_url`,
`thumbnail_url`, `destination_url`, `url`, `name`, ...).
At most 100 rows per request; rows not started within 180s are
reported as not attempted. Native campaigns only.

With `group_column` set the import switches to GROUPED mode: rows
sharing that column's value become ONE ad whose creatives live in a
creative pool of their own, each pool item carrying its row's
destination URL tail in `url_prefix` so the image and its page stay
paired. The ad's destination URL is the group's common base, cut back
to the last `/`; rows of a group whose URL shares no base with the
rest get their own pool + ad, named `<group> (2)`. Answer `groups`
must be echoed back in the next request's `groups` field when a group
spans several requests, or it gets a second ad instead of reusing the
first.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_csv_import_post200_response import ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    file = None # bytes | 
    image_column = 'image_column_example' # str |  (optional)
    url_column = 'url_column_example' # str |  (optional)
    name_column = 'name_column_example' # str |  (optional)
    group_column = 'group_column_example' # str | Header to group rows by. Omit for one ad per row. Never guessed. (optional)
    groups = 'groups_example' # str | The previous request's `groups` answer, verbatim, when a group spans requests. (optional)
    folder_id = 56 # int | Existing media-bank folder to file the creatives into. 0/absent = unfiled. (optional)
    folder_name = 'folder_name_example' # str | Create-or-reuse a folder of this name under folder_id and file into it. (optional)
    folder_per_group = 'folder_per_group_example' # str | Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent. (optional)
    name_prefix = 'name_prefix_example' # str | Prepended to every ad name, separated by a space. (optional)
    square_mode = pad # str | How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone. (optional) (default to pad)
    pad_color = '#FFFFFF' # str | Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead. (optional) (default to '#FFFFFF')
    crop_square = 'crop_square_example' # str | Legacy: 0 = none, anything else = crop. square_mode takes precedence. (optional)
    set_active = 1 # str |  (optional) (default to 1)
    bid = 3.4 # float |  (optional)

    try:
        # Import native ads from a CSV — one ad per row, or one ad per group.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_csv_import_post(type, campaign_id, file, image_column=image_column, url_column=url_column, name_column=name_column, group_column=group_column, groups=groups, folder_id=folder_id, folder_name=folder_name, folder_per_group=folder_per_group, name_prefix=name_prefix, square_mode=square_mode, pad_color=pad_color, crop_square=crop_square, set_active=set_active, bid=bid)
        print("The response of CampaignsApi->api_v1_campaigns_type_campaign_id_ads_csv_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_csv_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **file** | **bytes**|  | 
 **image_column** | **str**|  | [optional] 
 **url_column** | **str**|  | [optional] 
 **name_column** | **str**|  | [optional] 
 **group_column** | **str**| Header to group rows by. Omit for one ad per row. Never guessed. | [optional] 
 **groups** | **str**| The previous request&#39;s &#x60;groups&#x60; answer, verbatim, when a group spans requests. | [optional] 
 **folder_id** | **int**| Existing media-bank folder to file the creatives into. 0/absent &#x3D; unfiled. | [optional] 
 **folder_name** | **str**| Create-or-reuse a folder of this name under folder_id and file into it. | [optional] 
 **folder_per_group** | **str**| Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent. | [optional] 
 **name_prefix** | **str**| Prepended to every ad name, separated by a space. | [optional] 
 **square_mode** | **str**| How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone. | [optional] [default to pad]
 **pad_color** | **str**| Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead. | [optional] [default to &#39;#FFFFFF&#39;]
 **crop_square** | **str**| Legacy: 0 &#x3D; none, anything else &#x3D; crop. square_mode takes precedence. | [optional] 
 **set_active** | **str**|  | [optional] [default to 1]
 **bid** | **float**|  | [optional] 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response**](ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-row report. &#x60;rows[]&#x60; carries &#x60;row&#x60; (line in the file, header &#x3D; 1), &#x60;name&#x60;, &#x60;image_url&#x60;, &#x60;destination_url&#x60;, &#x60;status&#x60; (&#x60;created&#x60; / &#x60;failed&#x60;), &#x60;ad_id&#x60; + &#x60;creative_id&#x60; when created, &#x60;error&#x60; when failed. In grouped mode each row also carries &#x60;group&#x60;, &#x60;pool_id&#x60; and &#x60;pool_item_id&#x60;, the body carries &#x60;ad_count&#x60;, and &#x60;groups&#x60; maps each group to the &#x60;pool_id&#x60; / &#x60;ad_id&#x60; / &#x60;base&#x60; / &#x60;folder_id&#x60; to echo into the next request. The body&#39;s &#x60;folder_id&#x60; is the parent the import filed into.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_from_pool_post**
> api_v1_campaigns_type_campaign_id_ads_from_pool_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_from_pool_post_request)

Create ads from a creative pool.

A banner pool yields one ad per banner size it holds; a native /
creator / video pool yields one ad referencing the whole pool. The
pool must be yours and of a flavour the campaign's ad type renders
(422 otherwise), and for creator campaigns it must hold creatives of
the campaign's orientation.

`bid` uses the same unit contract as the other ad bid writes:
**currency units** (the advertiser's currency, e.g. `0.05`), checked
against the ad format's minimum bid and converted to the stored
cents; keys on the grandfathered raw-bid contract write raw cents.
Omit it (or 0) to leave the bid empty. `destinationurl` passes the
single-ad checks (format, blocked domains). New ads start
unvalidated unless the account is auto-validated.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_from_pool_post_request import ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_from_pool_post_request = {"pool_id":812,"destinationurl":"https://example.com/lp?cid={clickid}","bid":0.05,"set_active":true} # ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest | 

    try:
        # Create ads from a creative pool.
        api_instance.api_v1_campaigns_type_campaign_id_ads_from_pool_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_from_pool_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_from_pool_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_from_pool_post_request** | [**ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest**](ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest.md)|  | 

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
**201** | Ads created. |  -  |
**400** | &#x60;empty_pool&#x60;, &#x60;invalid_campaign_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Creative pool or campaign not found. |  -  |
**422** | &#x60;pool_id&#x60; missing / wrong flavour / orientation misfit, invalid or blocked &#x60;destinationurl&#x60;, &#x60;bid&#x60; under the minimum, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_get**
> ApiV1CampaignsTypeCampaignIdAdsGet200Response api_v1_campaigns_type_campaign_id_ads_get(type, campaign_id, ad_state=ad_state, search=search, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)

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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    ad_state = 'ad_state_example' # str | 1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted. (optional)
    search = 'search_example' # str | Matches the ad id (exact, when numeric), title, destination URL and display URL. (optional)
    sort_by = 'sort_by_example' # str | Omit for the panel's order: active first, then by position. (optional)
    sort_dir = desc # str |  (optional) (default to desc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List ads on a campaign.
        api_response = api_instance.api_v1_campaigns_type_campaign_id_ads_get(type, campaign_id, ad_state=ad_state, search=search, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)
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
 **ad_state** | **str**| 1 &#x3D; active only, 2 &#x3D; inactive only, 3 &#x3D; deleted only. Omit for every ad that isn&#39;t deleted. | [optional] 
 **search** | **str**| Matches the ad id (exact, when numeric), title, destination URL and display URL. | [optional] 
 **sort_by** | **str**| Omit for the panel&#39;s order: active first, then by position. | [optional] 
 **sort_dir** | **str**|  | [optional] [default to desc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

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

# **api_v1_campaigns_type_campaign_id_ads_mass_clone_post**
> api_v1_campaigns_type_campaign_id_ads_mass_clone_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request)

Copy many ads of a campaign.

Bulk form of `POST …/ads/{adId}/clone`: each copy keeps every column
of its source (including the active state) and starts unvalidated.
At most 50 ids per call. An id that fails to copy (not in this
campaign, deleted meanwhile) is listed in `failed`; the call fails
only when nothing was copied. Same handler as the panel.

`target_campaign_id` copies into another of your campaigns instead
(the panel's Mass Actions → Copy to campaign…). The target must be
live and take the same ads: RON ↔ CPM, flat deal ↔ direct deal,
RTB → RTB — list them with `GET …/ads/copy-targets`. Copies into
another campaign keep their title; all copies start unvalidated.
A key pinned to campaigns needs the target on its pin too.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request import ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request = {"ids":[3692752,3692753],"target_campaign_id":455210} # ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest | 

    try:
        # Copy many ads of a campaign.
        api_instance.api_v1_campaigns_type_campaign_id_ads_mass_clone_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_mass_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request** | [**ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest**](ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest.md)|  | 

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
**200** | Copied. &#x60;target_campaign_id&#x60; / &#x60;target_type&#x60; name where the copies landed. |  -  |
**400** | &#x60;no_ids&#x60;, &#x60;too_many_ids&#x60; (&gt; 50), &#x60;invalid_campaign_type&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;target_not_found&#x60; — not your live campaign, or its ads cannot take this campaign&#39;s ads. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |
**500** | &#x60;mass_clone_failed&#x60; — none of the ids could be copied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_mass_delete_post**
> api_v1_campaigns_type_campaign_id_ads_mass_delete_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request)

Soft-delete many ads of a campaign.

Soft delete (`is_deleted = 1`); restore one with
`PUT …/ads/{adId}/restore`. Ids outside the campaign are ignored.
On tenants that validate connect-campaign changes the deletion is
queued for publisher approval; a CPM campaign's zone states are
recomputed. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request import ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request = {"ids":[3692752,3692753]} # ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest | 

    try:
        # Soft-delete many ads of a campaign.
        api_instance.api_v1_campaigns_type_campaign_id_ads_mass_delete_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_mass_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request** | [**ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest**](ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest.md)|  | 

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
**200** | Deleted. |  -  |
**400** | &#x60;no_ids&#x60;, &#x60;invalid_campaign_type&#x60;, &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_mass_toggle_put**
> api_v1_campaigns_type_campaign_id_ads_mass_toggle_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request)

Activate or pause many ads of a campaign at once.

The panel's Mass Actions → Activate / Deactivate. `ids` selects ads
of this campaign; an empty or missing list means **every** live ad of
the campaign. Runs the same steps as the single toggle
(`PATCH …/ads/{adId}/active`): on tenants that validate
connect-campaign changes the ads are queued for publisher approval,
one pause/activate notification is sent for the whole action, and a
CPM campaign's zone states are recomputed. Ids outside the campaign
are ignored (not counted in `affected`). Same handler as the panel.
Unknown body fields → 422 `unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request import ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request = {"activate":false,"ids":[3692752,3692753]} # ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest | 

    try:
        # Activate or pause many ads of a campaign at once.
        api_instance.api_v1_campaigns_type_campaign_id_ads_mass_toggle_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_mass_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest**](ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest.md)|  | 

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
**400** | &#x60;invalid_campaign_type&#x60; / &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_multi_upload_post**
> api_v1_campaigns_type_campaign_id_ads_multi_upload_post(type, campaign_id, files, title=title, description=description, use_overlays=use_overlays, clone_per_overlay=clone_per_overlay, overlay=overlay, overlays_zip=overlays_zip)

Bulk-upload ads — one ad per creative file.

`multipart/form-data` upload of multiple creative files; the
server creates one ad per file on the campaign. Field `files`
(repeatable) carries the uploads.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    files = None # List[bytes] | One creative file per ad (also accepted as files[]).
    title = 'title_example' # str | Native campaigns only: headline for every ad in the batch. Empty = each file name. (optional)
    description = 'description_example' # str | Native campaigns only: description for every ad in the batch. (optional)
    use_overlays = 'use_overlays_example' # str | 1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images. (optional)
    clone_per_overlay = 'clone_per_overlay_example' # str | With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files. (optional)
    overlay = None # List[bytes] | Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation. (optional)
    overlays_zip = None # List[bytes] | ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays. (optional)

    try:
        # Bulk-upload ads — one ad per creative file.
        api_instance.api_v1_campaigns_type_campaign_id_ads_multi_upload_post(type, campaign_id, files, title=title, description=description, use_overlays=use_overlays, clone_per_overlay=clone_per_overlay, overlay=overlay, overlays_zip=overlays_zip)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_multi_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **files** | **List[bytes]**| One creative file per ad (also accepted as files[]). | 
 **title** | **str**| Native campaigns only: headline for every ad in the batch. Empty &#x3D; each file name. | [optional] 
 **description** | **str**| Native campaigns only: description for every ad in the batch. | [optional] 
 **use_overlays** | **str**| 1 &#x3D; composite the PNG overlays sent on &#x60;overlay&#x60; / &#x60;overlays_zip&#x60; onto the uploaded images. | [optional] 
 **clone_per_overlay** | **str**| With use_overlays&#x3D;1: create one variant per overlay instead of rotating the overlays across the files. | [optional] 
 **overlay** | **List[bytes]**| Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation. | [optional] 
 **overlays_zip** | **List[bytes]**| ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-file create results. |  -  |
**201** | Ads created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_post**
> api_v1_campaigns_type_campaign_id_ads_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_post_request, dry_run=dry_run, strict=strict)

Create an ad on a campaign (smart-default).

Creates a new ad attached to the campaign. Two request modes,
selected by `Content-Type`:

- **`application/json`** — reference an existing creative
  (banner pool, single creative, URL, HTML or a native image);
  no file upload.
- **`multipart/form-data`** — upload a real creative file
  directly: `banner_file` (banner image / HTML5 zip),
  `icon_file`, `image_file` (native), or `video_file`,
  alongside the text fields (`title`, `bid`,
  `destination_url`, …). The server stores the file, creates
  the creative row and attaches it — no pre-uploaded
  `creative_id` needed.

Required (JSON mode): `title` + `bid` + exactly **one** creative
reference (`banner_pool_id` / `creative_id` / `banner_url` /
`banner_html` / `banner_iframe_url` / `video_url` /
`video_pool_id` / `native_image_url` / `image_pool_id` /
`html_code`). Push ads add their icon with `icon_id` on top of
the image reference. `destination_url` is required unless the
creative carries its own URL (popunder/JS, VAST, html video) or
you set `url_pool_id`. In multipart mode the uploaded file *is*
the creative reference.

**Same validation as the panel.** Both modes run the panel's
create checks: the per-format minimum bid, the destination-URL
rules (format, blocked domains), the SmartAds `{spaceid}` macro
requirement (paytype 4 campaigns), the html-video zone rule
(an `html_code` video ad needs a Video Slider / In-page Video
zone in the campaign whitelist), native SmartAds html-only, and
the creator-pool orientation fit (`image_pool_id` on adtype 22).
CPM campaigns get their zone states recomputed after the insert.
`creative_id` / `icon_id` must be creatives from your own library.

**Field names.** The create names (`destination_url`,
`display_url`, `preview_url`, `is_active`, `url_pool_id`) and
the panel / PUT column names (`destinationurl`, `displayurl`,
`previewurl`, `isactive`, `url_poolid`) are both accepted on
create and on PUT, so one payload works for both. When both
spellings are sent the create name wins here and the column
name wins on PUT.

**Native ads (uploading a native creative by URL):**

The canonical field is `native_image_url` — a direct image URL.
The native headline/body are taken from `title` + `description`,
and `destination_url` is the click target; no creative pool
needed. The server saves `creatives = {"image": {"type": "url",
"url": "…"}}`, which is the only shape the panel preview and
the goadserver native-ad poll render.

Convenience for callers that don't know the campaign's ad type:
on a native campaign (adtypeid 3 / 21 / 22 / 42) a `banner_url`,
`banner_pool_id` or `creative_id` is **auto-routed** into
`creatives.image.*` using the matching shape — i.e. `banner_url`
becomes `{image:{type:url,url:…}}`, `banner_pool_id` becomes
`{image:{type:pool,poolid:…}}`, `creative_id` becomes
`{image:{type:creative,creative_id:…}}`. Banner-only shapes that
have no native equivalent (`banner_html`, `banner_iframe_url`,
`video_url`, `video_pool_id`) are rejected with a 422 on native
campaigns rather than persisted as an unrenderable row.

New integrations should still send `native_image_url` explicitly
— it's the unambiguous, type-correct path.

**Modes:**
  - `?dry_run=1` — return the resolved field map + computed
    `creatives` JSON without inserting.
  - `?strict=1` / `?strict=0` — reject / ignore unknown field names
    (default: the key's setting, strict for keys created from 2026-10-12).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request import ApiV1CampaignsTypeCampaignIdAdsPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_post_request = {"title":"Flash sale","bid":0.03,"native_image_url":"https://cdn.example.com/push/sale.png","icon_id":1080977,"display_url":"example.com","description":"Ends tonight.","destination_url":"https://example.com/sale?cid={clickid}"} # ApiV1CampaignsTypeCampaignIdAdsPostRequest | 
    dry_run = 'dry_run_example' # str |  (optional)
    strict = 'strict_example' # str | `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12).  (optional)

    try:
        # Create an ad on a campaign (smart-default).
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
 **strict** | **str**| &#x60;1&#x60; rejects unknown body fields (422 &#x60;unknown_fields&#x60;), &#x60;0&#x60; ignores them, for this request only. Omitted: the key&#39;s &#x60;strict_fields&#x60; setting (strict for keys created from 2026-10-12).  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
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

# **api_v1_campaigns_type_campaign_id_ads_update_pool_put**
> api_v1_campaigns_type_campaign_id_ads_update_pool_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_pool_put_request)

Point many ads at a different creative pool.

The panel's bulk "Change creative pool". `ids` selects ads (max 200;
empty = every ad of the campaign). Give either one `pool_id` for the
whole selection or `pool_by_size` (`{bansizeid: poolid}`) for a banner
selection running several sizes (it wins when both are sent). Only
ads with a pool-shaped slot are touched; `include_unpooled: true` also
converts ads that carry their own uploaded / hotlinked creative
(that creative reference is replaced). Every target pool must be
yours; native / creator pools must fit the campaign's orientation
(422 names the mismatch). List the pools a selection can take with
the panel picker rules described on the ad schema.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_update_pool_put_request = {"ids":[3692752,3692753],"pool_id":812} # ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest | 

    try:
        # Point many ads at a different creative pool.
        api_instance.api_v1_campaigns_type_campaign_id_ads_update_pool_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_pool_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_update_pool_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_update_pool_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest**](ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest.md)|  | 

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
**200** | Result counts. |  -  |
**400** | &#x60;too_many_ads&#x60;, &#x60;no_pool_ads&#x60; (none of the selection takes a pool). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Creative pool not found. |  -  |
**422** | &#x60;pool_id&#x60; missing, pool does not fit the ads / the campaign orientation, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_update_url_pool_put**
> api_v1_campaigns_type_campaign_id_ads_update_url_pool_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request)

Point many ads at a URL pool, or detach it.

The panel's bulk "Change URL pool". `pool_id` > 0 attaches that URL
pool (it must be yours and hold at least one active URL); `pool_id: 0`
detaches, so each ad falls back to its own destination URL — an ad
with none stays on its pool and is counted in `no_fallback`. Ads
whose creative links itself (html / iframe / VAST / phone) are
`skipped`. `ids` max 200, empty = every ad. Changed ads go back to
review unless the account is auto-validated.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request = {"ids":[3692752],"pool_id":44} # ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest | 

    try:
        # Point many ads at a URL pool, or detach it.
        api_instance.api_v1_campaigns_type_campaign_id_ads_update_url_pool_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_update_url_pool_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest**](ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest.md)|  | 

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
**200** | Result counts. |  -  |
**400** | &#x60;too_many_ads&#x60;, &#x60;no_url_pool_ads&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | URL pool not found, or &#x60;ads_not_found&#x60; — the selected ads no longer exist. |  -  |
**422** | &#x60;pool_id&#x60; missing / negative, pool has no active URLs, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_update_url_put**
> api_v1_campaigns_type_campaign_id_ads_update_url_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_url_put_request)

Rewrite the destination URL of many ads at once.

The panel's bulk "Change URL" action. Two modes:

- `set` (default) — write `url` onto every selected ad.
- `replace` — substring find/replace (`find` → `replace`) inside
  each ad's own URL, e.g. to move a campaign to a new domain or
  tracker id while per-ad paths and macros differ.

`ids` selects ads (max 200); empty = every ad of the campaign.
Only ads whose click target is their own destination URL are
touched — ads on a URL pool, with a self-linking creative (html /
iframe / VAST) or a phone number are reported as `skipped`. Every
new URL passes the single-ad checks first (format, blocked
domains); one bad URL fails the whole call before anything is
written. Changed ads go back to review unless the account is
auto-validated. Legacy shape `{adids, destinationurl}` is also
accepted.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_update_url_put_request = {"mode":"replace","find":"old-lander.com","replace":"new-lander.com"} # ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest | 

    try:
        # Rewrite the destination URL of many ads at once.
        api_instance.api_v1_campaigns_type_campaign_id_ads_update_url_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_url_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_update_url_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_update_url_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest**](ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest.md)|  | 

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
**200** | Result counts. |  -  |
**400** | &#x60;too_many_ads&#x60;, &#x60;invalid_mode&#x60;, or &#x60;no_ads_with_url&#x60; (every selected ad is on a URL pool / self-linking). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Missing &#x60;url&#x60; / &#x60;find&#x60;, or a resulting URL failed validation (message names the ad). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_campaign_id_ads_update_weight_put**
> api_v1_campaigns_type_campaign_id_ads_update_weight_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_weight_put_request)

Set the rotation weight of one or more RON ads.

Writes `sort_weight` on every listed ad of this campaign (the
relative share an ad gets when the campaign rotates its ads by
weight). Same handler as the panel. RON only.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_weight_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_update_weight_put_request = {"adid":[3692752,3692753],"sort_weight":5} # ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest | 

    try:
        # Set the rotation weight of one or more RON ads.
        api_instance.api_v1_campaigns_type_campaign_id_ads_update_weight_put(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_update_weight_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_campaign_id_ads_update_weight_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_update_weight_put_request** | [**ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest**](ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest.md)|  | 

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
**400** | &#x60;invalid_type&#x60; — not a RON campaign. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | No &#x60;adid&#x60;, or &#x60;unknown_fields&#x60;. |  -  |

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

# **api_v1_campaigns_type_id_available_zones_get**
> api_v1_campaigns_type_id_available_zones_get(type, id, page=page, per_page=per_page, search=search, site_id=site_id, exclude_ids=exclude_ids, only_used_sizes=only_used_sizes)

List your ad zones that can be attached to a campaign.

Your own, non-deleted ad zones matching the campaign's ad type
(and main category / native orientation where they apply), newest
first, with `is_whitelisted` for the ones already attached.
Paginated (`per_page` default 50, max 200). Same handler as the
panel's zone picker.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 50 # int |  (optional) (default to 50)
    search = 'search_example' # str | Matches zone name, site name or zone id. (optional)
    site_id = 56 # int | Only zones of this site (GET …/sites). (optional)
    exclude_ids = 'exclude_ids_example' # str | Comma-separated zone ids to leave out. (optional)
    only_used_sizes = True # bool | Banner campaigns: only zones whose size one of the campaign's live ads has. (optional)

    try:
        # List your ad zones that can be attached to a campaign.
        api_instance.api_v1_campaigns_type_id_available_zones_get(type, id, page=page, per_page=per_page, search=search, site_id=site_id, exclude_ids=exclude_ids, only_used_sizes=only_used_sizes)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_available_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 50]
 **search** | **str**| Matches zone name, site name or zone id. | [optional] 
 **site_id** | **int**| Only zones of this site (GET …/sites). | [optional] 
 **exclude_ids** | **str**| Comma-separated zone ids to leave out. | [optional] 
 **only_used_sizes** | **bool**| Banner campaigns: only zones whose size one of the campaign&#39;s live ads has. | [optional] 

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
**200** | Zones. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

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

Bids are in **currency units of your account's currency** (`0.05` =
0.05), the same as the panel, and must be at least
`GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is
allowed and stops the ad bidding). Reads return the bid as
`bid_amount` in the same unit; `user_bid` / `bid` are the stored
values in cents (your currency / the network's main currency). Keys
that wrote bids before 2026-10-12 keep the old raw-cents contract;
every bid write echoes `bid_unit` (`currency` or `raw_cents`).

`pct_inc` / `pct_dec` scale the stored bid and user_bid alike.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_bids_patch200_response import ApiV1CampaignsTypeIdBidsPatch200Response
from goadserver.models.api_v1_campaigns_type_id_bids_patch_request import ApiV1CampaignsTypeIdBidsPatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_bids_patch_request = {"mode":"set","value":0.05} # ApiV1CampaignsTypeIdBidsPatchRequest | 

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

# **api_v1_campaigns_type_id_budget_patch**
> ApiV1CampaignsTypeIdBudgetPatch200Response api_v1_campaigns_type_id_budget_patch(type, id, api_v1_campaigns_type_id_budget_patch_request)

Update a campaign's total and/or daily budget.

Sets the campaign (total) budget and/or the max daily budget, plus the
flags that enable each cap. All four fields are optional — send only the
ones you want to change. Amounts are in the account currency.
Documented in audit_20260723_1117 (was implemented but unspecified).

`max_day_budget` is corrected upward to the ad type's configured
minimum daily budget rather than rejected, matching every other write
path. The stored amount is returned as `max_day_budget` in the
response — read it back instead of assuming the value you sent.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_budget_patch200_response import ApiV1CampaignsTypeIdBudgetPatch200Response
from goadserver.models.api_v1_campaigns_type_id_budget_patch_request import ApiV1CampaignsTypeIdBudgetPatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_budget_patch_request = goadserver.ApiV1CampaignsTypeIdBudgetPatchRequest() # ApiV1CampaignsTypeIdBudgetPatchRequest | 

    try:
        # Update a campaign's total and/or daily budget.
        api_response = api_instance.api_v1_campaigns_type_id_budget_patch(type, id, api_v1_campaigns_type_id_budget_patch_request)
        print("The response of CampaignsApi->api_v1_campaigns_type_id_budget_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_budget_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_budget_patch_request** | [**ApiV1CampaignsTypeIdBudgetPatchRequest**](ApiV1CampaignsTypeIdBudgetPatchRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeIdBudgetPatch200Response**](ApiV1CampaignsTypeIdBudgetPatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated budget state |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |
**422** | Invalid campaign id/type or body, or &#x60;budget_not_supported&#x60; — a flat deal or direct deal carries no budget columns. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_clone_post**
> ApiV1CampaignsTypeIdClonePost201Response api_v1_campaigns_type_id_clone_post(type, id, strict=strict, api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request)

Clone a campaign — everything, or the parts you pick.

Same core as the panel's Duplicate button. The clone lands paused
(`is_active=false`; a network can make ron clones start active, and
one that reviews new campaigns puts them in Pending Created) and named "<original> Copy" unless `name` is
sent. By default every part is copied; the four `copy_*` switches
(the Duplicate dialog's choices, each default `true`) leave a part
out, in which case the clone gets the table defaults for it:

- `copy_ads` — the campaign's ads and creatives.
- `copy_targeting` — countries/regions, categories, devices,
  browsers, OS, languages, location, connection / carrier / ISP,
  keywords, webview / adblock, orientation and the linked domain /
  IP / retargeting filters.
- `copy_budget` — total and daily budget, impression limits,
  frequency capping, conversion capping.
- `copy_schedule` — day/time parting and the start / end dates.

Bookkeeping (`num_ads`, `pending_state`, `dateadded`, `wl_zoneids`)
is always reset. A RON clone also drops any flat-deal records,
copies offer screenshots, and goes to review when the network
validates campaigns. A flat campaign (paytype 5) can only be cloned
by an administrator → 403 for API keys.

`copied` in the response echoes which parts were copied. Unknown
body keys are ignored, or a 422 with `?strict=1`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response import ApiV1CampaignsTypeIdClonePost201Response
from goadserver.models.api_v1_campaigns_type_id_clone_post_request import ApiV1CampaignsTypeIdClonePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    strict = 56 # int | 1 = reject unknown body keys (422). (optional)
    api_v1_campaigns_type_id_clone_post_request = {"name":"Spring test B","copy_ads":false} # ApiV1CampaignsTypeIdClonePostRequest |  (optional)

    try:
        # Clone a campaign — everything, or the parts you pick.
        api_response = api_instance.api_v1_campaigns_type_id_clone_post(type, id, strict=strict, api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request)
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
 **strict** | **int**| 1 &#x3D; reject unknown body keys (422). | [optional] 
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
**403** | &#x60;forbidden&#x60; — a flat (paytype 5) campaign; or &#x60;forbidden_resource&#x60; (pinned key). |  -  |
**404** | Source campaign not found or not owned by caller. |  -  |
**422** | Invalid body (malformed JSON, or an unknown key with ?strict&#x3D;1), or the clone failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_delete**
> ApiV1CampaignsTypeIdDelete200Response api_v1_campaigns_type_id_delete(type, id)

Soft-delete a campaign.

Sets `isdeleted=1`, `dayactive=0` (flatrate / directdeal:
`iscancelled=1`, `ispaused=1`, `dayactive=0`). The campaign and its
history remain in the database for billing/stats reconciliation but
stop serving immediately. Idempotent — deleting an already-deleted
campaign returns 404. The campaign's live ads are soft-deleted with
it (marked as deleted-with-the-campaign; ads you had deleted
yourself before stay as they were).

Undo with `POST /api/v1/campaigns/mass-undelete` `{ids:[id], type}`:
the ads the delete took down come back, and a ron / cpm / rtb
campaign returns paused or running as it was before the delete (a
flat / direct deal comes back paused). Find deleted campaigns with
`GET /api/v1/campaigns?deleted=1`.

On a network that reviews campaign deletes, a live ron campaign
(not a flat one) is not deleted: the answer is `deleted: false,
pending_review: true`, the campaign keeps running with
`pending_state: 2` (Pending Delete), and an admin's approval deletes
it.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_delete200_response import ApiV1CampaignsTypeIdDelete200Response
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

Block list: removes the campaign from the filter's campaign list.
Refused with 409 when that would widen the filter instead —
`last_campaign` (it is the only listed campaign; an empty list
means every campaign of the ad type) or
`filter_not_campaign_scoped` (the filter covers every campaign
anyway). Deactivate, delete or re-scope the filter
(PUT /api/v1/filters/{type}/{id}) instead.
Allow-list / `ip`: clears the campaign's FK column only if it
currently points to this filter; otherwise returns 404.


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
**409** | &#x60;last_campaign&#x60; or &#x60;filter_not_campaign_scoped&#x60; — detaching would widen the filter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_filters_get**
> ApiV1CampaignsTypeIdFiltersGet200Response api_v1_campaigns_type_id_filters_get(type, id)

List filters attached to this campaign.

Returns every filter that reaches this campaign: allow-lists and
the IP pool via the campaign's FK columns, and block lists that
either list it (`applies_to: listed_campaigns`, matching
campaign_type) or cover it without a list (`all_campaigns` =
ad_type 0; `all_campaigns_of_ad_type` = same ad type, empty list).
`ron`, `cpm` and `rtb` campaigns support filter linkage. A cpm
campaign takes `subid_incl`, `subid_excl`, `ip` and the domain /
adzone / ISP block lists (block lists hold it as a `ron` campaign);
`domain_incl` / `adzone_incl` are ron / rtb only → 422
`validation_error`. Any other type → 422 "Filter linking is only
supported for campaign types: ron, cpm, rtb."


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response import ApiV1CampaignsTypeIdFiltersGet200Response
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

Block lists (`*_excl`): adds the campaign to the filter's campaign
list. A filter that already covers the campaign (ad_type 0, or an
empty list of the campaign's ad type) is left alone — `changed:
false` + `applies_to` — instead of being narrowed to this one
campaign. Refused with 422 when the filter's ad type differs from
the campaign's (the block would never apply) or when its list holds
the other campaign kind (ron vs rtb).
Allow-lists (`*_incl`) and `ip`: sets the campaign's FK column to
this filter (replacing any previous one of the same kind).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_filters_post200_response import ApiV1CampaignsTypeIdFiltersPost200Response
from goadserver.models.api_v1_campaigns_type_id_filters_post_request import ApiV1CampaignsTypeIdFiltersPostRequest
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
**422** | Unsupported filter_type / campaign type, or an ad_type / campaign-kind mismatch. |  -  |

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
**422** | &#x60;min_bid_not_supported&#x60; — flat deals are priced by the deal and RTB bids are set by the bidder, so neither has a per-click floor. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_patch**
> api_v1_campaigns_type_id_patch(type, id, api_v1_campaigns_type_id_patch_request, dry_run=dry_run, strict=strict)

Partially update a campaign.

Updates one or more writable fields on an existing campaign. Send
only the fields you want to change — anything you omit is left
alone. Field names are the public ones from
`GET /api/v1/campaigns/{type}/_schema` (`daily_budget`,
`regions`, `device_type_ids`, …).

**Region targeting (`regions`):** the server defensively trims
any ancestor id whose descendant is also in the list, at any
depth (continent → country → state → sub-region → city). If you
send a higher-level id alongside one of its descendants, the
higher-level id is dropped — sending both would otherwise
broaden targeting back up to the whole subtree and undo the
leaf pick. Use `GET /api/v1/lookups/regions` to walk the geo
tree and pick the leaf id you actually want.

**`directdeal` / `flatrate`** take their own field set:
`name`, `is_paused`, `start_date`, `total_days` (either alone —
the other keeps its stored value; the end date is recomputed),
`deal_type`, `total_budget`, `regions` (or legacy `countries`),
`languages`, `device_type_ids`, `os_ids`, `browser_ids`,
`max_impressions`, `percentage` (0-100), `use_keywords`,
`keywords`, `keywords_exclude`. Any other field — including
`ad_space_id`, which is fixed at create — answers
`422 unsupported_fields` with the list, rather than being ignored.

Some fields cannot be changed via this endpoint:
  - `ad_type` — the ads table layout differs per type, change
    requires recreating the campaign.
  - `id`, `userid`, `systemid`, `isdeleted`, `dateadded`, audit
    stamps — system-managed.
  - Read-only projection fields — `total_spent`, `sites_locked`,
    `pending_state`, `num_ads`, `is_deleted`, `is_complete`,
    `created_at`, `started_at`, `ended_at`, `last_paid_at` — are
    ignored (rejected in strict mode).
  - `selling_type` — a change is refused with 409; change it in
    the panel.

The same save rules as the panel apply: `daily_budget` is raised
to the system minimum, `total_budget` must be > 0 while
`use_campaign_budget` is true, an impression limit that is
switched on needs a value > 0, and `start_date` / `end_date`
must be YYYY-MM-DD. Every campaign-form field of
`CampaignPanelFields` is writable here too, with the same gates
as on create (a field that does not apply is a `422`); object
fields (`day_parting`, `conversion_capping`, …) merge with the
stored value, and the other option keys are kept. `banner_size_ids`
(rtb banner) replaces the size set. The change is recorded in the
campaign history and mailed like a panel save.

**Modes:**
  - `?dry_run=1` — return the resolved field map without writing.
  - `?strict=1` / `?strict=0` — reject / ignore unknown field names
    (default: the key's setting, strict for keys created from 2026-10-12).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_patch_request import ApiV1CampaignsTypeIdPatchRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_patch_request = {"name":"Holiday banners — v2"} # ApiV1CampaignsTypeIdPatchRequest | 
    dry_run = 'dry_run_example' # str |  (optional)
    strict = 'strict_example' # str | `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12).  (optional)

    try:
        # Partially update a campaign.
        api_instance.api_v1_campaigns_type_id_patch(type, id, api_v1_campaigns_type_id_patch_request, dry_run=dry_run, strict=strict)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_patch_request** | [**ApiV1CampaignsTypeIdPatchRequest**](ApiV1CampaignsTypeIdPatchRequest.md)|  | 
 **dry_run** | **str**|  | [optional] 
 **strict** | **str**| &#x60;1&#x60; rejects unknown body fields (422 &#x60;unknown_fields&#x60;), &#x60;0&#x60; ignores them, for this request only. Omitted: the key&#39;s &#x60;strict_fields&#x60; setting (strict for keys created from 2026-10-12).  | [optional] 

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
**200** | Updated. Body is the freshly-updated campaign in the public projection (same shape as &#x60;GET /api/v1/campaigns/{type}/{id}&#x60;). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | Validation error (empty body, no updatable fields, or unknown field in strict mode). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_reset_max_budget_put**
> api_v1_campaigns_type_id_reset_max_budget_put(type, id)

Reset a campaign's lifetime-budget spend.

Zeroes the spend counted against the campaign's total budget
(`campaignbudget`) and re-arms the "budget reached" email, so a
campaign stopped by its lifetime budget can spend it again. The
budget value itself is unchanged. Not for flatrate / directdeal
(422 `budget_reset_not_supported`). Same handler as the panel's
Reset button.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # Reset a campaign's lifetime-budget spend.
        api_instance.api_v1_campaigns_type_id_reset_max_budget_put(type, id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_reset_max_budget_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
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
**200** | Reset. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; (unknown type) or &#x60;budget_reset_not_supported&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_sites_get**
> api_v1_campaigns_type_id_sites_get(type, id, exclude_ids=exclude_ids)

Your sites that have zones attachable to a campaign.

Your own sites with the number of their zones that match the
campaign (same rules as available-zones); sites with none are
left out. Use a site's `id` as `site_id` on available-zones.
Same handler as the panel.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    exclude_ids = 'exclude_ids_example' # str | Comma-separated zone ids to leave out of the counts. (optional)

    try:
        # Your sites that have zones attachable to a campaign.
        api_instance.api_v1_campaigns_type_id_sites_get(type, id, exclude_ids=exclude_ids)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_sites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **exclude_ids** | **str**| Comma-separated zone ids to leave out of the counts. | [optional] 

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
**200** | Sites. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_whitelist_zones_get**
> api_v1_campaigns_type_id_whitelist_zones_get(type, id)

List the ad zones attached to a campaign.

The campaign's zone allow-list with each zone's weight for this
campaign (0–100, default 100). Only zones you own are returned.
`owned` is false for a zone that is deleted. On an Ad Shop
campaign the zone name is masked ("Space #N") and `site` /
`siteid` are left out unless you hold the source-names right.
Same handler as the panel.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 

    try:
        # List the ad zones attached to a campaign.
        api_instance.api_v1_campaigns_type_id_whitelist_zones_get(type, id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_whitelist_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
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
**200** | Attached zones. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_zones_post**
> api_v1_campaigns_type_id_zones_post(type, id, api_v1_campaigns_type_id_zones_post_request)

Attach ad zones to a campaign.

Adds zones to the campaign's allow-list (kept ones stay) and
connects each zone to the campaign at weight 100. Ids that are not
yours, deleted, or don't match the campaign's ad type / main
category / orientation are dropped; when none is left → 403
`not_allowed`. An empty list is a no-op 200. Same handler as the
panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_zones_post_request import ApiV1CampaignsTypeIdZonesPostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    api_v1_campaigns_type_id_zones_post_request = {"spaceids":[81234,81235]} # ApiV1CampaignsTypeIdZonesPostRequest | 

    try:
        # Attach ad zones to a campaign.
        api_instance.api_v1_campaigns_type_id_zones_post(type, id, api_v1_campaigns_type_id_zones_post_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_zones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_zones_post_request** | [**ApiV1CampaignsTypeIdZonesPostRequest**](ApiV1CampaignsTypeIdZonesPostRequest.md)|  | 

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
**200** | Attached. &#x60;added&#x60; &#x3D; zones that passed the checks. |  -  |
**403** | &#x60;not_allowed&#x60; — no listed zone may be attached; or &#x60;forbidden_resource&#x60; (pinned key). |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_zones_zone_id_delete**
> api_v1_campaigns_type_id_zones_zone_id_delete(type, id, zone_id)

Detach an ad zone from a campaign.

Removes the zone from the allow-list and the campaign from the
zone's connected campaigns. Removing the last zone stores `0`
(no allow-list). Detaching a zone that isn't attached is a 200
no-op. Same handler as the panel.


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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    zone_id = 56 # int | 

    try:
        # Detach an ad zone from a campaign.
        api_instance.api_v1_campaigns_type_id_zones_zone_id_delete(type, id, zone_id)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_zones_zone_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **zone_id** | **int**|  | 

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
**200** | Detached. |  -  |
**400** | &#x60;invalid_id&#x60; — bad zone id. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_id_zones_zone_id_weight_put**
> api_v1_campaigns_type_id_zones_zone_id_weight_put(type, id, zone_id, api_v1_campaigns_type_id_zones_zone_id_weight_put_request)

Set an attached zone's weight for this campaign.

The share of the zone's traffic this campaign gets relative to the
zone's other connected campaigns, 0–100 (values outside are
clamped). The zone must be yours and connected to the campaign.
Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_zones_zone_id_weight_put_request import ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int | 
    zone_id = 56 # int | 
    api_v1_campaigns_type_id_zones_zone_id_weight_put_request = {"weight":60} # ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest | 

    try:
        # Set an attached zone's weight for this campaign.
        api_instance.api_v1_campaigns_type_id_zones_zone_id_weight_put(type, id, zone_id, api_v1_campaigns_type_id_zones_zone_id_weight_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_id_zones_zone_id_weight_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | 
 **zone_id** | **int**|  | 
 **api_v1_campaigns_type_id_zones_zone_id_weight_put_request** | [**ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest**](ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest.md)|  | 

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
**200** | Saved (the clamped weight is echoed). |  -  |
**400** | &#x60;invalid_id&#x60;, or &#x60;not_connected&#x60; — the zone is not attached to this campaign. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Campaign or zone not found. |  -  |
**422** | &#x60;validation_error&#x60; — type other than ron / cpm. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_campaigns_type_post**
> api_v1_campaigns_type_post(type, api_v1_campaigns_type_post_request, dry_run=dry_run, strict=strict)

Create a new campaign (smart-default).

Creates a new campaign with sensible defaults applied for any
field you don't send. Everything not supplied defaults to
"all/none" — see `GET /api/v1/campaigns/{type}/_schema` for the
exact field list, which **differs by `type`**.

**Per campaign type:**
  - `ron` / `cpm` / `rtb` — required `name` + `ad_type`; the
    request body documented below applies.
  - `directdeal` — books one of your own ad zones for a date
    range. Required `name` + `ad_space_id` + `start_date` +
    `total_days`; `ad_type` is taken from the zone and is not
    accepted. Geo targeting takes `regions` (region ids from
    `/api/v1/lookups/regions`, states and cities included), the
    same as the other types; the legacy `countries` codes are
    still accepted when `regions` is not sent. See
    `GET /api/v1/campaigns/directdeal/_schema`.
  - `rtb` — also requires `request_url` (unless `use_type: 1`, a
    URL per zone in `zone_urls`), and for banner campaigns
    (`ad_type: 2`) `banner_size_ids`. The daily cap applies only
    with `use_daily_budget: true`; there is no total budget
    (exchange-paced). A user locked to one RTB network always
    lands on it.

Every campaign-form field is accepted (`CampaignPanelFields`:
day parting and the other options, language / connection /
carrier / IP / SubID targeting, pricing extras, RTB config,
offers) with the panel's own rules: the minimum daily budget,
IP list syntax, source-optimizer ownership, and — on create — a
real ad zone location for ron banner (2), ron/rtb link (6) and
ron reel (20) campaigns where the network defines locations,
link types or reel types (`location_ids` empty or `"0"` is a `422`
there, as in the panel).
  - `flatrate` — **not creatable through the public API** (the
    legacy self-service ad-space buy is heading EOL). A POST
    returns `422 unsupported_type`.

The campaign starts paused (`is_paused=true`) so you can
attach ads via `POST /api/v1/campaigns/{type}/{id}/ads` and verify
before activating — unless you send `is_paused`, or the network has
new ron campaigns start active. On a network that reviews new
campaigns, a new ron campaign also shows `pending_state: 5` (Pending
Created) until an admin approves it. Flip the active flag when ready via
`PATCH /api/v1/campaigns/{type}/{id}/active`.

**Modes:**
  - `?dry_run=1` — validate and return the resolved field map
    without inserting. Useful for previewing what an LLM would
    create before charging it.
  - `?strict=1` / `?strict=0` — reject / ignore unknown field names
    for this request (422 `unknown_fields` listing them). Without
    it the key's default applies: keys created from 2026-10-12 are
    strict, older keys ignore unknown fields.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_post_request import ApiV1CampaignsTypePostRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    api_v1_campaigns_type_post_request = {"name":"My first API campaign","ad_type":11} # ApiV1CampaignsTypePostRequest | 
    dry_run = 'dry_run_example' # str |  (optional)
    strict = 'strict_example' # str | `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12).  (optional)

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
 **strict** | **str**| &#x60;1&#x60; rejects unknown body fields (422 &#x60;unknown_fields&#x60;), &#x60;0&#x60; ignores them, for this request only. Omitted: the key&#39;s &#x60;strict_fields&#x60; setting (strict for keys created from 2026-10-12).  | [optional] 

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
**422** | Validation error (missing required, unknown field in strict mode (key default or &#x60;?strict&#x3D;1&#x60;), a field that does not apply to this campaign, …). |  -  |
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
which creative shape is appropriate). For native ad types
(`campaign_ad_type` 3 / 21 / 22) the canonical URL field is
`native_image_url`; `banner_url` works too because the server
auto-routes it to `creatives.image` on a native campaign.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_schema_ads_get200_response import ApiV1CampaignsTypeSchemaAdsGet200Response
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
> ApiV1CampaignsTypeSchemaGet200Response api_v1_campaigns_type_schema_get(type, ad_type=ad_type)

Field metadata for create/update.

Discovery endpoint for AI agents and integrators. Returns the
canonical list of public field names a `POST /api/v1/campaigns/{type}`
accepts, with type, required-flag, default value, an example, and
a one-line description. `ad_type` enumerates the active ad-type
ids on the caller's tenant.

The field set differs by `type` — `directdeal` returns its own
ad-zone-booking fields (`ad_space_id`, `start_date`, `total_days`,
…), not the RON-shaped targeting fields. `flatrate` is not
creatable through the public API: its `_schema` returns
`{creatable: false}` instead of a field list.

For `ron` / `cpm` / `rtb` the list is built from the campaign
table's real columns and the network's modules: a field the type
cannot store (keywords or schedule dates on rtb, total budget on
rtb) or the network does not offer is not listed. It is exactly
the set `?strict=1` accepts on **both** `POST` and `PATCH`.
`ad_types` / `selling_types` / `not_selling_types` on a field mean
it only applies to those ad types / pay types; sending it to any
other campaign is a `422`. `?ad_type=<id>` narrows the list to one
ad type.

Use this to drive form UIs, validate agent-generated payloads
client-side, or feed into a function-calling LLM.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_schema_get200_response import ApiV1CampaignsTypeSchemaGet200Response
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
    api_instance = goadserver.CampaignsApi(api_client)
    type = 'type_example' # str | 
    ad_type = 56 # int | Only list the fields that apply to this ad type. (optional)

    try:
        # Field metadata for create/update.
        api_response = api_instance.api_v1_campaigns_type_schema_get(type, ad_type=ad_type)
        print("The response of CampaignsApi->api_v1_campaigns_type_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_campaigns_type_schema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **ad_type** | **int**| Only list the fields that apply to this ad type. | [optional] 

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

# **api_v1_rtb_test_rtb_context_get**
> api_v1_rtb_test_rtb_context_get(adtypeid=adtypeid, rtbtype=rtbtype)

Context for testing an endpoint before the campaign exists.

Same as the per-campaign context, for an unsaved endpoint — resolves `adtypeid` to the bid-request ad type. Same handler as the panel.

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
    api_instance = goadserver.CampaignsApi(api_client)
    adtypeid = 1 # int |  (optional) (default to 1)
    rtbtype = openrtb # str |  (optional) (default to openrtb)

    try:
        # Context for testing an endpoint before the campaign exists.
        api_instance.api_v1_rtb_test_rtb_context_get(adtypeid=adtypeid, rtbtype=rtbtype)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_rtb_test_rtb_context_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adtypeid** | **int**|  | [optional] [default to 1]
 **rtbtype** | **str**|  | [optional] [default to openrtb]

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_rtb_test_rtb_post**
> RtbTestResult api_v1_rtb_test_rtb_post(api_v1_rtb_test_rtb_post_request)

Fire a test bid request at any endpoint URL.

The tester for an endpoint you are about to save on an RTB campaign:
`url` (or `override_url`) + `rtbtype` + `adtypeid` come from the
body instead of a campaign. Same safety rules and result as
`POST /api/v1/campaigns/rtb/{id}/test-rtb`. Same handler as the
panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_rtb_test_rtb_post_request import ApiV1RtbTestRtbPostRequest
from goadserver.models.rtb_test_result import RtbTestResult
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_rtb_test_rtb_post_request = {"url":"https://dsp.example.com/bid","rtbtype":"openrtb","adtypeid":1,"width":300,"height":250,"country":"US"} # ApiV1RtbTestRtbPostRequest | 

    try:
        # Fire a test bid request at any endpoint URL.
        api_response = api_instance.api_v1_rtb_test_rtb_post(api_v1_rtb_test_rtb_post_request)
        print("The response of CampaignsApi->api_v1_rtb_test_rtb_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_rtb_test_rtb_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_rtb_test_rtb_post_request** | [**ApiV1RtbTestRtbPostRequest**](ApiV1RtbTestRtbPostRequest.md)|  | 

### Return type

[**RtbTestResult**](RtbTestResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test result. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | &#x60;url&#x60; missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tools_replace_domain_put**
> api_v1_tools_replace_domain_put(api_v1_tools_replace_domain_put_request)

Replace the landing domain across your RON ads.

The panel's Tools → Replace domain: in every live RON ad whose
destination URL contains `search`, the first occurrence is replaced
with `replace` (a domain). `campaignids` narrows it to those
campaigns; empty = every RON ad of the account. A key pinned to
campaigns must list `campaignids`, all within its pin (403
`forbidden_resource` otherwise).

Same safeguards as a single-ad save: a resulting URL on a blocked
domain fails the whole call before anything is written, and the
changed ads go back to review unless the account is auto-validated.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tools_replace_domain_put_request import ApiV1ToolsReplaceDomainPutRequest
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
    api_instance = goadserver.CampaignsApi(api_client)
    api_v1_tools_replace_domain_put_request = {"search":"old-lander.com","replace":"new-lander.com","campaignids":[451360]} # ApiV1ToolsReplaceDomainPutRequest | 

    try:
        # Replace the landing domain across your RON ads.
        api_instance.api_v1_tools_replace_domain_put(api_v1_tools_replace_domain_put_request)
    except Exception as e:
        print("Exception when calling CampaignsApi->api_v1_tools_replace_domain_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tools_replace_domain_put_request** | [**ApiV1ToolsReplaceDomainPutRequest**](ApiV1ToolsReplaceDomainPutRequest.md)|  | 

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
**400** | &#x60;invalid_domain&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;search&#x60; / &#x60;replace&#x60; missing, blocked replacement domain, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


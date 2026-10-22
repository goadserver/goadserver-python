# goadserver.AdsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_campaigns_type_campaign_id_ads_mass_undelete_post**](AdsApi.md#api_v1_campaigns_type_campaign_id_ads_mass_undelete_post) | **POST** /api/v1/campaigns/{type}/{campaignId}/ads/mass-undelete | Restore archived ads of a campaign.


# **api_v1_campaigns_type_campaign_id_ads_mass_undelete_post**
> api_v1_campaigns_type_campaign_id_ads_mass_undelete_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request)

Restore archived ads of a campaign.

The undo of POST …/ads/mass-delete, for every campaign type except
rtb (the single PUT …/ads/{adId}/restore is RON-only). Only ads at
is_deleted = 1 move; on a tenant that validates RON ads they go
back through validation. At most 200 ids.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request import ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest
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
    api_instance = goadserver.AdsApi(api_client)
    type = 'type_example' # str | 
    campaign_id = 56 # int | 
    api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request = goadserver.ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest() # ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest | 

    try:
        # Restore archived ads of a campaign.
        api_instance.api_v1_campaigns_type_campaign_id_ads_mass_undelete_post(type, campaign_id, api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request)
    except Exception as e:
        print("Exception when calling AdsApi->api_v1_campaigns_type_campaign_id_ads_mass_undelete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **campaign_id** | **int**|  | 
 **api_v1_campaigns_type_campaign_id_ads_mass_undelete_post_request** | [**ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest**](ApiV1CampaignsTypeCampaignIdAdsMassUndeletePostRequest.md)|  | 

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
**200** | &#x60;affected&#x60; &#x3D; ads restored. |  -  |
**400** | No ids, or more than 200. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**pending_validation** | **bool** | The change waits for network approval (only present when &#x60;changed&#x60; is true). | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response from a JSON string
api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response_instance = ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response_dict = api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response from a dict
api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response_from_dict = ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response.from_dict(api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



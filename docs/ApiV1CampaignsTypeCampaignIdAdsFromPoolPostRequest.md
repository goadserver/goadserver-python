# ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **int** |  | 
**destinationurl** | **str** |  | [optional] 
**bid** | **float** | Currency units (raw cents for legacy raw-bid keys). | [optional] 
**set_active** | **bool** |  | [optional] [default to False]
**use_imptracking** | **bool** |  | [optional] [default to False]
**imptrackingurl** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_from_pool_post_request import ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_from_pool_post_request_instance = ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_from_pool_post_request_dict = api_v1_campaigns_type_campaign_id_ads_from_pool_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest from a dict
api_v1_campaigns_type_campaign_id_ads_from_pool_post_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_from_pool_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



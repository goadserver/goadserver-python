# ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adid** | **List[int]** | Ad ids (the panel&#39;s field name). | 
**sort_weight** | **int** |  | 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_weight_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_update_weight_put_request_instance = ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_update_weight_put_request_dict = api_v1_campaigns_type_campaign_id_ads_update_weight_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest from a dict
api_v1_campaigns_type_campaign_id_ads_update_weight_put_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_update_weight_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



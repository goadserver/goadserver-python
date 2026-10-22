# ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**target_campaign_id** | **int** | Optional. Copy into this campaign (see copy-targets) instead of the same one. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request import ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request_instance = ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request_dict = api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest from a dict
api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **bool** | true &#x3D; activate, false (default) &#x3D; pause. | [optional] 
**ids** | **List[int]** | Ad ids; empty &#x3D; every ad of the campaign. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request import ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request_instance = ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request_dict = api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest from a dict
api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



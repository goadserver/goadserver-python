# ApiV1CampaignsMassDeletePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**type** | **str** |  | [optional] [default to 'ron']

## Example

```python
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsMassDeletePostRequest from a JSON string
api_v1_campaigns_mass_delete_post_request_instance = ApiV1CampaignsMassDeletePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsMassDeletePostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_mass_delete_post_request_dict = api_v1_campaigns_mass_delete_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsMassDeletePostRequest from a dict
api_v1_campaigns_mass_delete_post_request_from_dict = ApiV1CampaignsMassDeletePostRequest.from_dict(api_v1_campaigns_mass_delete_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



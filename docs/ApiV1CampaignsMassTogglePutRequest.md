# ApiV1CampaignsMassTogglePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | Campaign ids (body capped at 64 KB). | 
**type** | **str** |  | [optional] [default to 'ron']
**pause** | **bool** | true &#x3D; pause, false &#x3D; resume. | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_campaigns_mass_toggle_put_request import ApiV1CampaignsMassTogglePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsMassTogglePutRequest from a JSON string
api_v1_campaigns_mass_toggle_put_request_instance = ApiV1CampaignsMassTogglePutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsMassTogglePutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_mass_toggle_put_request_dict = api_v1_campaigns_mass_toggle_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsMassTogglePutRequest from a dict
api_v1_campaigns_mass_toggle_put_request_from_dict = ApiV1CampaignsMassTogglePutRequest.from_dict(api_v1_campaigns_mass_toggle_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



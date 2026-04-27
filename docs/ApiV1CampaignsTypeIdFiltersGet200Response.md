# ApiV1CampaignsTypeIdFiltersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_type** | **str** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**filters** | [**List[ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner]**](ApiV1CampaignsTypeIdFiltersGet200ResponseFiltersInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response import ApiV1CampaignsTypeIdFiltersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdFiltersGet200Response from a JSON string
api_v1_campaigns_type_id_filters_get200_response_instance = ApiV1CampaignsTypeIdFiltersGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdFiltersGet200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_filters_get200_response_dict = api_v1_campaigns_type_id_filters_get200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdFiltersGet200Response from a dict
api_v1_campaigns_type_id_filters_get200_response_from_dict = ApiV1CampaignsTypeIdFiltersGet200Response.from_dict(api_v1_campaigns_type_id_filters_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



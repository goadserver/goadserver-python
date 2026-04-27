# ApiV1CampaignsTypeIdFiltersPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_type** | **str** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**filter_type** | **str** |  | [optional] 
**filter_id** | **int** |  | [optional] 
**attached** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_filters_post200_response import ApiV1CampaignsTypeIdFiltersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdFiltersPost200Response from a JSON string
api_v1_campaigns_type_id_filters_post200_response_instance = ApiV1CampaignsTypeIdFiltersPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdFiltersPost200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_filters_post200_response_dict = api_v1_campaigns_type_id_filters_post200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdFiltersPost200Response from a dict
api_v1_campaigns_type_id_filters_post200_response_from_dict = ApiV1CampaignsTypeIdFiltersPost200Response.from_dict(api_v1_campaigns_type_id_filters_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



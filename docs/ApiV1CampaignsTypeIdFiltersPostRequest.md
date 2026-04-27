# ApiV1CampaignsTypeIdFiltersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | 
**filter_id** | **int** |  | 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_filters_post_request import ApiV1CampaignsTypeIdFiltersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdFiltersPostRequest from a JSON string
api_v1_campaigns_type_id_filters_post_request_instance = ApiV1CampaignsTypeIdFiltersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdFiltersPostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_filters_post_request_dict = api_v1_campaigns_type_id_filters_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdFiltersPostRequest from a dict
api_v1_campaigns_type_id_filters_post_request_from_dict = ApiV1CampaignsTypeIdFiltersPostRequest.from_dict(api_v1_campaigns_type_id_filters_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1FiltersMassActionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**filters** | [**List[ApiV1FiltersMassActionPostRequestFiltersInner]**](ApiV1FiltersMassActionPostRequestFiltersInner.md) |  | 

## Example

```python
from goadserver.models.api_v1_filters_mass_action_post_request import ApiV1FiltersMassActionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersMassActionPostRequest from a JSON string
api_v1_filters_mass_action_post_request_instance = ApiV1FiltersMassActionPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersMassActionPostRequest.to_json())

# convert the object into a dict
api_v1_filters_mass_action_post_request_dict = api_v1_filters_mass_action_post_request_instance.to_dict()
# create an instance of ApiV1FiltersMassActionPostRequest from a dict
api_v1_filters_mass_action_post_request_from_dict = ApiV1FiltersMassActionPostRequest.from_dict(api_v1_filters_mass_action_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



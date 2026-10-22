# ApiV1FiltersMassActionPostRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** | Filter type, e.g. domain_excl, subid_incl, ip. | [optional] 

## Example

```python
from goadserver.models.api_v1_filters_mass_action_post_request_filters_inner import ApiV1FiltersMassActionPostRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersMassActionPostRequestFiltersInner from a JSON string
api_v1_filters_mass_action_post_request_filters_inner_instance = ApiV1FiltersMassActionPostRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersMassActionPostRequestFiltersInner.to_json())

# convert the object into a dict
api_v1_filters_mass_action_post_request_filters_inner_dict = api_v1_filters_mass_action_post_request_filters_inner_instance.to_dict()
# create an instance of ApiV1FiltersMassActionPostRequestFiltersInner from a dict
api_v1_filters_mass_action_post_request_filters_inner_from_dict = ApiV1FiltersMassActionPostRequestFiltersInner.from_dict(api_v1_filters_mass_action_post_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



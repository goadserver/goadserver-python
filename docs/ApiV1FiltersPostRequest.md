# ApiV1FiltersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**items** | **List[str]** |  | 
**campaign_ids** | **List[int]** | Exclusion filters: limits this filter to these campaigns. Empty/omitted &#x3D; applies to all. | [optional] 
**ad_type** | **int** | 0 &#x3D; all ad types, otherwise the adtypeid this filter applies to. | [optional] [default to 0]

## Example

```python
from goadserver.models.api_v1_filters_post_request import ApiV1FiltersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersPostRequest from a JSON string
api_v1_filters_post_request_instance = ApiV1FiltersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersPostRequest.to_json())

# convert the object into a dict
api_v1_filters_post_request_dict = api_v1_filters_post_request_instance.to_dict()
# create an instance of ApiV1FiltersPostRequest from a dict
api_v1_filters_post_request_from_dict = ApiV1FiltersPostRequest.from_dict(api_v1_filters_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



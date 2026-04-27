# ApiV1CreativePoolsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sort_type** | **str** |  | [optional] 
**conv_type** | **int** |  | [optional] 
**tags** | **str** | CSV of tag ids. | [optional] 
**tagids** | **List[str]** |  | [optional] 
**items_count** | **int** |  | [optional] 
**total_sizes** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_get200_response_data_inner import ApiV1CreativePoolsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsGet200ResponseDataInner from a JSON string
api_v1_creative_pools_get200_response_data_inner_instance = ApiV1CreativePoolsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_creative_pools_get200_response_data_inner_dict = api_v1_creative_pools_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1CreativePoolsGet200ResponseDataInner from a dict
api_v1_creative_pools_get200_response_data_inner_from_dict = ApiV1CreativePoolsGet200ResponseDataInner.from_dict(api_v1_creative_pools_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



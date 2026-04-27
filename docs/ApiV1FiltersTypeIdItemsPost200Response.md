# ApiV1FiltersTypeIdItemsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**items** | **List[str]** |  | [optional] 
**item_count** | **int** |  | [optional] 
**added** | **List[str]** | The IDs/strings actually added (post resolution + dedupe). | [optional] 

## Example

```python
from goadserver.models.api_v1_filters_type_id_items_post200_response import ApiV1FiltersTypeIdItemsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersTypeIdItemsPost200Response from a JSON string
api_v1_filters_type_id_items_post200_response_instance = ApiV1FiltersTypeIdItemsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersTypeIdItemsPost200Response.to_json())

# convert the object into a dict
api_v1_filters_type_id_items_post200_response_dict = api_v1_filters_type_id_items_post200_response_instance.to_dict()
# create an instance of ApiV1FiltersTypeIdItemsPost200Response from a dict
api_v1_filters_type_id_items_post200_response_from_dict = ApiV1FiltersTypeIdItemsPost200Response.from_dict(api_v1_filters_type_id_items_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



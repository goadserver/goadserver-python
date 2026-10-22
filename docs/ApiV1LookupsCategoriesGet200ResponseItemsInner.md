# ApiV1LookupsCategoriesGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pid** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**main_categories** | **str** | CSV of main-category ids this category is a member of. | [optional] 

## Example

```python
from goadserver.models.api_v1_lookups_categories_get200_response_items_inner import ApiV1LookupsCategoriesGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LookupsCategoriesGet200ResponseItemsInner from a JSON string
api_v1_lookups_categories_get200_response_items_inner_instance = ApiV1LookupsCategoriesGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1LookupsCategoriesGet200ResponseItemsInner.to_json())

# convert the object into a dict
api_v1_lookups_categories_get200_response_items_inner_dict = api_v1_lookups_categories_get200_response_items_inner_instance.to_dict()
# create an instance of ApiV1LookupsCategoriesGet200ResponseItemsInner from a dict
api_v1_lookups_categories_get200_response_items_inner_from_dict = ApiV1LookupsCategoriesGet200ResponseItemsInner.from_dict(api_v1_lookups_categories_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



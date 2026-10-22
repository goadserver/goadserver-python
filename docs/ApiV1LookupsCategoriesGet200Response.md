# ApiV1LookupsCategoriesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**main_catid** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**items** | [**List[ApiV1LookupsCategoriesGet200ResponseItemsInner]**](ApiV1LookupsCategoriesGet200ResponseItemsInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_lookups_categories_get200_response import ApiV1LookupsCategoriesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LookupsCategoriesGet200Response from a JSON string
api_v1_lookups_categories_get200_response_instance = ApiV1LookupsCategoriesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1LookupsCategoriesGet200Response.to_json())

# convert the object into a dict
api_v1_lookups_categories_get200_response_dict = api_v1_lookups_categories_get200_response_instance.to_dict()
# create an instance of ApiV1LookupsCategoriesGet200Response from a dict
api_v1_lookups_categories_get200_response_from_dict = ApiV1LookupsCategoriesGet200Response.from_dict(api_v1_lookups_categories_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListMeta

Pagination block of the `{data, meta}` list envelope. Lists take `page` + `per_page` (capped per endpoint) or `offset` + `limit`; `per_page=all` returns the whole set in one page. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 
**limit** | **int** | Same as per_page. | [optional] 
**offset** | **int** | (current_page - 1) * per_page. | [optional] 

## Example

```python
from goadserver.models.list_meta import ListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ListMeta from a JSON string
list_meta_instance = ListMeta.from_json(json)
# print the JSON string representation of the object
print(ListMeta.to_json())

# convert the object into a dict
list_meta_dict = list_meta_instance.to_dict()
# create an instance of ListMeta from a dict
list_meta_from_dict = ListMeta.from_dict(list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



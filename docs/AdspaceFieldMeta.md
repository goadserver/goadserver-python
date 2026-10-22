# AdspaceFieldMeta

One field entry on the adspace schema response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**default** | **object** |  | [optional] 
**example** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**enum** | **List[object]** | Allowed values when present. | [optional] 
**fields** | [**List[AdspaceFieldMeta]**](AdspaceFieldMeta.md) | Nested fields when type&#x3D;object/array. | [optional] 

## Example

```python
from goadserver.models.adspace_field_meta import AdspaceFieldMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceFieldMeta from a JSON string
adspace_field_meta_instance = AdspaceFieldMeta.from_json(json)
# print the JSON string representation of the object
print(AdspaceFieldMeta.to_json())

# convert the object into a dict
adspace_field_meta_dict = adspace_field_meta_instance.to_dict()
# create an instance of AdspaceFieldMeta from a dict
adspace_field_meta_from_dict = AdspaceFieldMeta.from_dict(adspace_field_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



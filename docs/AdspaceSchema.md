# AdspaceSchema

Full per-type schema for adspace create/update. `fields` are the common top-level body fields; `settings_block` is the type-specific nested object; `options` are the config flag bag (booleans, selects, numbers) the type exposes — pass them at body top level. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adspace_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**adtype_id** | **int** |  | [optional] 
**selling_types** | **List[str]** |  | [optional] 
**fields** | [**List[AdspaceFieldMeta]**](AdspaceFieldMeta.md) |  | [optional] 
**settings_block** | [**AdspaceSettingsBlock**](AdspaceSettingsBlock.md) |  | [optional] 
**options** | [**List[AdspaceTypeOption]**](AdspaceTypeOption.md) |  | [optional] 
**notes** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.adspace_schema import AdspaceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceSchema from a JSON string
adspace_schema_instance = AdspaceSchema.from_json(json)
# print the JSON string representation of the object
print(AdspaceSchema.to_json())

# convert the object into a dict
adspace_schema_dict = adspace_schema_instance.to_dict()
# create an instance of AdspaceSchema from a dict
adspace_schema_from_dict = AdspaceSchema.from_dict(adspace_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



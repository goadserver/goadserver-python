# AdspaceSettingsBlock

Per-type settings block descriptor — the key on the request body the type-specific config goes under (e.g. `banner_settings`, `pop_settings`, `native_settings`). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**fields** | [**List[AdspaceFieldMeta]**](AdspaceFieldMeta.md) |  | [optional] 

## Example

```python
from goadserver.models.adspace_settings_block import AdspaceSettingsBlock

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceSettingsBlock from a JSON string
adspace_settings_block_instance = AdspaceSettingsBlock.from_json(json)
# print the JSON string representation of the object
print(AdspaceSettingsBlock.to_json())

# convert the object into a dict
adspace_settings_block_dict = adspace_settings_block_instance.to_dict()
# create an instance of AdspaceSettingsBlock from a dict
adspace_settings_block_from_dict = AdspaceSettingsBlock.from_dict(adspace_settings_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



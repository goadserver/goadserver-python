# AdspaceTypeItem

One entry returned by GET /api/v1/lookups/adspace-types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** | Use as the {type} path parameter on /api/v1/adspaces/{type}/_schema and POST /api/v1/adspaces/{type}. | [optional] 
**name** | **str** |  | [optional] 
**adtype_id** | **int** |  | [optional] 
**settings_key** | **str** | Body key for the type-specific settings block; \&quot;\&quot; if the type takes no nested settings. | [optional] 
**selling_types** | **List[str]** |  | [optional] 
**use_min_price** | **bool** |  | [optional] 
**use_smartzone** | **bool** |  | [optional] 
**has_own_ads** | **bool** |  | [optional] 
**has_preview** | **bool** |  | [optional] 
**right** | **str** |  | [optional] 
**options** | [**List[AdspaceTypeOption]**](AdspaceTypeOption.md) |  | [optional] 

## Example

```python
from goadserver.models.adspace_type_item import AdspaceTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceTypeItem from a JSON string
adspace_type_item_instance = AdspaceTypeItem.from_json(json)
# print the JSON string representation of the object
print(AdspaceTypeItem.to_json())

# convert the object into a dict
adspace_type_item_dict = adspace_type_item_instance.to_dict()
# create an instance of AdspaceTypeItem from a dict
adspace_type_item_from_dict = AdspaceTypeItem.from_dict(adspace_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



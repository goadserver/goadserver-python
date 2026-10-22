# AdspaceTypeOption

One entry from a config adspacetype's options bag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**default** | **object** |  | [optional] 
**multiple** | **bool** | Allow multiple values (selects only). | [optional] 
**list_items** | **str** | Where this option&#39;s options come from (e.g. \&quot;banner_sizes\&quot;, \&quot;countries\&quot;). | [optional] 
**label** | **str** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**mod_enabled** | **str** | Module gate path; only present when the option is conditional. | [optional] 
**items** | **Dict[str, object]** | Inline enum options (e.g. popads.displaytypes → {popup: {id:1}, popunder: {id:2}}). | [optional] 
**sub_options** | [**List[AdspaceTypeOption]**](AdspaceTypeOption.md) | Nested options revealed by a bool toggle (e.g. use_fixed_capping → capping_minutes). | [optional] 

## Example

```python
from goadserver.models.adspace_type_option import AdspaceTypeOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceTypeOption from a JSON string
adspace_type_option_instance = AdspaceTypeOption.from_json(json)
# print the JSON string representation of the object
print(AdspaceTypeOption.to_json())

# convert the object into a dict
adspace_type_option_dict = adspace_type_option_instance.to_dict()
# create an instance of AdspaceTypeOption from a dict
adspace_type_option_from_dict = AdspaceTypeOption.from_dict(adspace_type_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



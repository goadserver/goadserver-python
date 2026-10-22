# ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner

An id plus at least one operation. An unknown operation is rejected by name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The menu node this patch targets. | 
**hidden** | **bool** | true hides the node; false un-hides one a lower tier hid. | [optional] 
**move** | **object** |  | [optional] 
**label** | **str** | Tenant-specific wording for the node. | [optional] 
**order** | **object** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_account_ui_layouts_scope_put_request_data_patches_inner import ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner from a JSON string
api_v1_account_ui_layouts_scope_put_request_data_patches_inner_instance = ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner.to_json())

# convert the object into a dict
api_v1_account_ui_layouts_scope_put_request_data_patches_inner_dict = api_v1_account_ui_layouts_scope_put_request_data_patches_inner_instance.to_dict()
# create an instance of ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner from a dict
api_v1_account_ui_layouts_scope_put_request_data_patches_inner_from_dict = ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner.from_dict(api_v1_account_ui_layouts_scope_put_request_data_patches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



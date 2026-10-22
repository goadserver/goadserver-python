# ApiV1AccountUiLayoutsScopePutRequestData

A PATCH LIST, not a full menu definition — the panel applies these on top of the menu it builds from the caller's rights and modules, so a patch cannot conjure a node the account may not see. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patches** | [**List[ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner]**](ApiV1AccountUiLayoutsScopePutRequestDataPatchesInner.md) | Empty array &#x3D; no overrides, which is also how you flatten a layout without deleting it. | 

## Example

```python
from goadserver.models.api_v1_account_ui_layouts_scope_put_request_data import ApiV1AccountUiLayoutsScopePutRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountUiLayoutsScopePutRequestData from a JSON string
api_v1_account_ui_layouts_scope_put_request_data_instance = ApiV1AccountUiLayoutsScopePutRequestData.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountUiLayoutsScopePutRequestData.to_json())

# convert the object into a dict
api_v1_account_ui_layouts_scope_put_request_data_dict = api_v1_account_ui_layouts_scope_put_request_data_instance.to_dict()
# create an instance of ApiV1AccountUiLayoutsScopePutRequestData from a dict
api_v1_account_ui_layouts_scope_put_request_data_from_dict = ApiV1AccountUiLayoutsScopePutRequestData.from_dict(api_v1_account_ui_layouts_scope_put_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



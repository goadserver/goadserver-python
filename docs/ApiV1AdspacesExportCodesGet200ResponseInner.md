# ApiV1AdspacesExportCodesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siteid** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**ctrl_js** | **str** | Controller &lt;script&gt; tag — once per page, before the zone snippets. | [optional] 
**ctrl_js_failover** | **str** | Alternative to ctrl_js, pasted instead of it: the inline ad-blocker failover loader. Empty when fewer than two usable ad domains are available. | [optional] 
**ctrl_name** | **str** |  | [optional] 
**codes** | [**List[ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner]**](ApiV1AdspacesExportCodesGet200ResponseInnerCodesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_export_codes_get200_response_inner import ApiV1AdspacesExportCodesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesExportCodesGet200ResponseInner from a JSON string
api_v1_adspaces_export_codes_get200_response_inner_instance = ApiV1AdspacesExportCodesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesExportCodesGet200ResponseInner.to_json())

# convert the object into a dict
api_v1_adspaces_export_codes_get200_response_inner_dict = api_v1_adspaces_export_codes_get200_response_inner_instance.to_dict()
# create an instance of ApiV1AdspacesExportCodesGet200ResponseInner from a dict
api_v1_adspaces_export_codes_get200_response_inner_from_dict = ApiV1AdspacesExportCodesGet200ResponseInner.from_dict(api_v1_adspaces_export_codes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



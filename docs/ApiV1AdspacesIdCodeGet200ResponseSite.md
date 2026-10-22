# ApiV1AdspacesIdCodeGet200ResponseSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ctrl_js** | **str** | Controller &lt;script&gt; tag — paste once per page. | [optional] 
**ctrl_js_failover** | **str** | Alternative to ctrl_js, pasted instead of it: the inline ad-blocker failover loader. Empty when fewer than two usable ad domains are available. | [optional] 
**ctrl_name** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_code_get200_response_site import ApiV1AdspacesIdCodeGet200ResponseSite

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdCodeGet200ResponseSite from a JSON string
api_v1_adspaces_id_code_get200_response_site_instance = ApiV1AdspacesIdCodeGet200ResponseSite.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdCodeGet200ResponseSite.to_json())

# convert the object into a dict
api_v1_adspaces_id_code_get200_response_site_dict = api_v1_adspaces_id_code_get200_response_site_instance.to_dict()
# create an instance of ApiV1AdspacesIdCodeGet200ResponseSite from a dict
api_v1_adspaces_id_code_get200_response_site_from_dict = ApiV1AdspacesIdCodeGet200ResponseSite.from_dict(api_v1_adspaces_id_code_get200_response_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



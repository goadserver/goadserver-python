# ApiV1AdspacesIdCodeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adspace_id** | **int** |  | [optional] 
**site** | [**ApiV1AdspacesIdCodeGet200ResponseSite**](ApiV1AdspacesIdCodeGet200ResponseSite.md) |  | [optional] 
**space_name** | **str** |  | [optional] 
**js_code** | **str** | Per-zone JS call — wrap in &lt;script&gt;. | [optional] 
**ad_tag** | **str** | Iframe alternative. | [optional] 
**alternative** | **str** | No-JS fallback. | [optional] 
**note** | **str** |  | [optional] 
**amp** | [**ApiV1AdspacesIdCodeGet200ResponseAmp**](ApiV1AdspacesIdCodeGet200ResponseAmp.md) |  | [optional] 
**screen** | [**ApiV1AdspacesIdCodeGet200ResponseScreen**](ApiV1AdspacesIdCodeGet200ResponseScreen.md) |  | [optional] 
**ctv** | [**ApiV1AdspacesIdCodeGet200ResponseCtv**](ApiV1AdspacesIdCodeGet200ResponseCtv.md) |  | [optional] 
**layout** | **str** | Native and creator widget zones only: the ?layout the code was rendered with (empty &#x3D; default). | [optional] 
**layouts** | [**List[ApiV1AdspacesIdCodeGet200ResponseLayoutsInner]**](ApiV1AdspacesIdCodeGet200ResponseLayoutsInner.md) | Native and creator widget zones only: the ready-made layouts ?layout accepts for this zone. | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_code_get200_response import ApiV1AdspacesIdCodeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdCodeGet200Response from a JSON string
api_v1_adspaces_id_code_get200_response_instance = ApiV1AdspacesIdCodeGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdCodeGet200Response.to_json())

# convert the object into a dict
api_v1_adspaces_id_code_get200_response_dict = api_v1_adspaces_id_code_get200_response_instance.to_dict()
# create an instance of ApiV1AdspacesIdCodeGet200Response from a dict
api_v1_adspaces_id_code_get200_response_from_dict = ApiV1AdspacesIdCodeGet200Response.from_dict(api_v1_adspaces_id_code_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



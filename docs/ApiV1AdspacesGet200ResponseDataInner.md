# ApiV1AdspacesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site** | [**ApiV1AdspacesGet200ResponseDataInnerSite**](ApiV1AdspacesGet200ResponseDataInnerSite.md) |  | [optional] 
**ad_type** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_get200_response_data_inner import ApiV1AdspacesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesGet200ResponseDataInner from a JSON string
api_v1_adspaces_get200_response_data_inner_instance = ApiV1AdspacesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_adspaces_get200_response_data_inner_dict = api_v1_adspaces_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1AdspacesGet200ResponseDataInner from a dict
api_v1_adspaces_get200_response_data_inner_from_dict = ApiV1AdspacesGet200ResponseDataInner.from_dict(api_v1_adspaces_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



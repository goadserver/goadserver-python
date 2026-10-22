# ApiV1AdspacesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site** | [**ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner**](ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner.md) |  | [optional] 
**siteid** | **int** |  | [optional] 
**adspace_type** | **str** | Type config key (e.g. bannerads). Empty when the underlying type is no longer in the tenant config. | [optional] 
**adzone_typeid** | **int** |  | [optional] 
**adtype_id** | **int** |  | [optional] 
**ad_type** | **int** | Backward-compat alias for adtype_id. | [optional] 
**adsizeid** | **int** |  | [optional] 
**is_active** | **bool** | Derived from publisher_adzones.isinuse. | [optional] 
**date_added** | **datetime** |  | [optional] 
**time_changed** | **int** | Unix seconds of last update. | [optional] 
**is_deleted** | **bool** |  | [optional] 
**parentid** | **int** |  | [optional] 

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



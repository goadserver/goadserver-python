# ApiV1FiltersTypeIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**items** | **List[str]** |  | [optional] 
**ad_type** | **int** | Block lists and domain_incl only. | [optional] 
**campaign_ids** | **List[int]** |  | [optional] 
**campaign_type** | **str** | Block lists only; allow-lists always link RON campaigns. | [optional] 
**ip_list** | **str** | type&#x3D;ip only. | [optional] 
**replace_ip_ranges** | **bool** | type&#x3D;ip only; needs ip_list. | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_filters_type_id_put_request import ApiV1FiltersTypeIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersTypeIdPutRequest from a JSON string
api_v1_filters_type_id_put_request_instance = ApiV1FiltersTypeIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersTypeIdPutRequest.to_json())

# convert the object into a dict
api_v1_filters_type_id_put_request_dict = api_v1_filters_type_id_put_request_instance.to_dict()
# create an instance of ApiV1FiltersTypeIdPutRequest from a dict
api_v1_filters_type_id_put_request_from_dict = ApiV1FiltersTypeIdPutRequest.from_dict(api_v1_filters_type_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



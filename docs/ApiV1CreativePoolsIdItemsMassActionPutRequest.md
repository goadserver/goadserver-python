# ApiV1CreativePoolsIdItemsMassActionPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**ids** | **List[int]** | Pool item ids (GET /creative-pools/{id}/items). | 
**url_prefix** | **str** | action&#x3D;url_prefix. | [optional] 
**lang** | **str** | action&#x3D;language — language code. | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_id_items_mass_action_put_request import ApiV1CreativePoolsIdItemsMassActionPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsIdItemsMassActionPutRequest from a JSON string
api_v1_creative_pools_id_items_mass_action_put_request_instance = ApiV1CreativePoolsIdItemsMassActionPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsIdItemsMassActionPutRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_id_items_mass_action_put_request_dict = api_v1_creative_pools_id_items_mass_action_put_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsIdItemsMassActionPutRequest from a dict
api_v1_creative_pools_id_items_mass_action_put_request_from_dict = ApiV1CreativePoolsIdItemsMassActionPutRequest.from_dict(api_v1_creative_pools_id_items_mass_action_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



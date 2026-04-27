# ApiV1CreativePoolsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**sort_type** | **str** |  | [optional] 
**conv_type** | **int** |  | [optional] 
**tags** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_id_put_request import ApiV1CreativePoolsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsIdPutRequest from a JSON string
api_v1_creative_pools_id_put_request_instance = ApiV1CreativePoolsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsIdPutRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_id_put_request_dict = api_v1_creative_pools_id_put_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsIdPutRequest from a dict
api_v1_creative_pools_id_put_request_from_dict = ApiV1CreativePoolsIdPutRequest.from_dict(api_v1_creative_pools_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



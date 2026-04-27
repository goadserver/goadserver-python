# ApiV1CreativePoolsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1CreativePoolsGet200ResponseDataInner]**](ApiV1CreativePoolsGet200ResponseDataInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_get200_response import ApiV1CreativePoolsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsGet200Response from a JSON string
api_v1_creative_pools_get200_response_instance = ApiV1CreativePoolsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsGet200Response.to_json())

# convert the object into a dict
api_v1_creative_pools_get200_response_dict = api_v1_creative_pools_get200_response_instance.to_dict()
# create an instance of ApiV1CreativePoolsGet200Response from a dict
api_v1_creative_pools_get200_response_from_dict = ApiV1CreativePoolsGet200Response.from_dict(api_v1_creative_pools_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



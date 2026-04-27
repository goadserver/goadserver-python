# ApiV1CreativePoolsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**type** | **str** |  | [optional] [default to 'banner']
**tags** | **str** | CSV of tag ids. | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_post_request import ApiV1CreativePoolsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsPostRequest from a JSON string
api_v1_creative_pools_post_request_instance = ApiV1CreativePoolsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsPostRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_post_request_dict = api_v1_creative_pools_post_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsPostRequest from a dict
api_v1_creative_pools_post_request_from_dict = ApiV1CreativePoolsPostRequest.from_dict(api_v1_creative_pools_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



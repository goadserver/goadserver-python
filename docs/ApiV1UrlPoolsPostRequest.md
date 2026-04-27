# ApiV1UrlPoolsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**sort_type** | **str** |  | [optional] [default to 'rnd']
**conv_type** | **int** |  | [optional] 
**tags** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_url_pools_post_request import ApiV1UrlPoolsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UrlPoolsPostRequest from a JSON string
api_v1_url_pools_post_request_instance = ApiV1UrlPoolsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1UrlPoolsPostRequest.to_json())

# convert the object into a dict
api_v1_url_pools_post_request_dict = api_v1_url_pools_post_request_instance.to_dict()
# create an instance of ApiV1UrlPoolsPostRequest from a dict
api_v1_url_pools_post_request_from_dict = ApiV1UrlPoolsPostRequest.from_dict(api_v1_url_pools_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



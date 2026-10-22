# ApiV1TagsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**pid** | **int** | Parent tag id; 0 or omitted &#x3D; top level. | [optional] 

## Example

```python
from goadserver.models.api_v1_tags_post_request import ApiV1TagsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TagsPostRequest from a JSON string
api_v1_tags_post_request_instance = ApiV1TagsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TagsPostRequest.to_json())

# convert the object into a dict
api_v1_tags_post_request_dict = api_v1_tags_post_request_instance.to_dict()
# create an instance of ApiV1TagsPostRequest from a dict
api_v1_tags_post_request_from_dict = ApiV1TagsPostRequest.from_dict(api_v1_tags_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



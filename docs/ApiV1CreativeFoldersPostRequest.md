# ApiV1CreativeFoldersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**pid** | **int** | Parent folder; 0 or omitted for a root. | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_folders_post_request import ApiV1CreativeFoldersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativeFoldersPostRequest from a JSON string
api_v1_creative_folders_post_request_instance = ApiV1CreativeFoldersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativeFoldersPostRequest.to_json())

# convert the object into a dict
api_v1_creative_folders_post_request_dict = api_v1_creative_folders_post_request_instance.to_dict()
# create an instance of ApiV1CreativeFoldersPostRequest from a dict
api_v1_creative_folders_post_request_from_dict = ApiV1CreativeFoldersPostRequest.from_dict(api_v1_creative_folders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



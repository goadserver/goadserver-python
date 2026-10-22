# ApiV1TagsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**pid** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tags_id_put_request import ApiV1TagsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TagsIdPutRequest from a JSON string
api_v1_tags_id_put_request_instance = ApiV1TagsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TagsIdPutRequest.to_json())

# convert the object into a dict
api_v1_tags_id_put_request_dict = api_v1_tags_id_put_request_instance.to_dict()
# create an instance of ApiV1TagsIdPutRequest from a dict
api_v1_tags_id_put_request_from_dict = ApiV1TagsIdPutRequest.from_dict(api_v1_tags_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



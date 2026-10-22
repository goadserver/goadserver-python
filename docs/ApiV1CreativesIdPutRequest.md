# ApiV1CreativesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name; HTML tags are stripped. Must not be empty. | [optional] 
**tags** | [**ApiV1CreativesIdPutRequestTags**](ApiV1CreativesIdPutRequestTags.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creatives_id_put_request import ApiV1CreativesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativesIdPutRequest from a JSON string
api_v1_creatives_id_put_request_instance = ApiV1CreativesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativesIdPutRequest.to_json())

# convert the object into a dict
api_v1_creatives_id_put_request_dict = api_v1_creatives_id_put_request_instance.to_dict()
# create an instance of ApiV1CreativesIdPutRequest from a dict
api_v1_creatives_id_put_request_from_dict = ApiV1CreativesIdPutRequest.from_dict(api_v1_creatives_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



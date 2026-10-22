# ApiV1UrlPoolsReplaceUrlPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** |  | 
**replace** | **str** |  | [optional] 
**poolids** | **List[int]** |  | [optional] 
**urlids** | **List[int]** |  | [optional] 
**dry_run** | **bool** |  | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_url_pools_replace_url_put_request import ApiV1UrlPoolsReplaceUrlPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UrlPoolsReplaceUrlPutRequest from a JSON string
api_v1_url_pools_replace_url_put_request_instance = ApiV1UrlPoolsReplaceUrlPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1UrlPoolsReplaceUrlPutRequest.to_json())

# convert the object into a dict
api_v1_url_pools_replace_url_put_request_dict = api_v1_url_pools_replace_url_put_request_instance.to_dict()
# create an instance of ApiV1UrlPoolsReplaceUrlPutRequest from a dict
api_v1_url_pools_replace_url_put_request_from_dict = ApiV1UrlPoolsReplaceUrlPutRequest.from_dict(api_v1_url_pools_replace_url_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



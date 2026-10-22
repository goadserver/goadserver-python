# ApiV1McpPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonrpc** | **str** |  | 
**id** | [**ApiV1McpPostRequestId**](ApiV1McpPostRequestId.md) |  | [optional] 
**method** | **str** |  | 
**params** | **object** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_mcp_post_request import ApiV1McpPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1McpPostRequest from a JSON string
api_v1_mcp_post_request_instance = ApiV1McpPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1McpPostRequest.to_json())

# convert the object into a dict
api_v1_mcp_post_request_dict = api_v1_mcp_post_request_instance.to_dict()
# create an instance of ApiV1McpPostRequest from a dict
api_v1_mcp_post_request_from_dict = ApiV1McpPostRequest.from_dict(api_v1_mcp_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



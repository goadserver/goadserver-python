# ApiV1ToolsReplaceDomainPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Text to find in the destination URL (usually the old domain). | 
**replace** | **str** | New domain (must contain a dot). | 
**campaignids** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tools_replace_domain_put_request import ApiV1ToolsReplaceDomainPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ToolsReplaceDomainPutRequest from a JSON string
api_v1_tools_replace_domain_put_request_instance = ApiV1ToolsReplaceDomainPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1ToolsReplaceDomainPutRequest.to_json())

# convert the object into a dict
api_v1_tools_replace_domain_put_request_dict = api_v1_tools_replace_domain_put_request_instance.to_dict()
# create an instance of ApiV1ToolsReplaceDomainPutRequest from a dict
api_v1_tools_replace_domain_put_request_from_dict = ApiV1ToolsReplaceDomainPutRequest.from_dict(api_v1_tools_replace_domain_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



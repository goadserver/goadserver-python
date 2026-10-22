# ApiV1WebhooksIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_webhooks_id_patch_request import ApiV1WebhooksIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksIdPatchRequest from a JSON string
api_v1_webhooks_id_patch_request_instance = ApiV1WebhooksIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1WebhooksIdPatchRequest.to_json())

# convert the object into a dict
api_v1_webhooks_id_patch_request_dict = api_v1_webhooks_id_patch_request_instance.to_dict()
# create an instance of ApiV1WebhooksIdPatchRequest from a dict
api_v1_webhooks_id_patch_request_from_dict = ApiV1WebhooksIdPatchRequest.from_dict(api_v1_webhooks_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



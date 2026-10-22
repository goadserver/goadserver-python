# ApiV1WebhooksIdRotateSecretPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overlap_hours** | **int** |  | [optional] [default to 24]

## Example

```python
from goadserver.models.api_v1_webhooks_id_rotate_secret_post_request import ApiV1WebhooksIdRotateSecretPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksIdRotateSecretPostRequest from a JSON string
api_v1_webhooks_id_rotate_secret_post_request_instance = ApiV1WebhooksIdRotateSecretPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1WebhooksIdRotateSecretPostRequest.to_json())

# convert the object into a dict
api_v1_webhooks_id_rotate_secret_post_request_dict = api_v1_webhooks_id_rotate_secret_post_request_instance.to_dict()
# create an instance of ApiV1WebhooksIdRotateSecretPostRequest from a dict
api_v1_webhooks_id_rotate_secret_post_request_from_dict = ApiV1WebhooksIdRotateSecretPostRequest.from_dict(api_v1_webhooks_id_rotate_secret_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



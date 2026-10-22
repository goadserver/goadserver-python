# UserWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**paused_reason** | **str** | &#x60;auto_failing&#x60; when paused after 20 failures in a row; empty when paused by hand. | [optional] 
**fail_count** | **int** |  | [optional] 
**credential** | **str** | What created it — its events follow that credential&#39;s access. | [optional] 
**api_key_id** | **int** |  | [optional] 
**api_key_name** | **str** |  | [optional] 
**app_id** | **int** |  | [optional] 
**app_name** | **str** |  | [optional] 
**credential_active** | **bool** | false once the key is revoked or the app disconnected — nothing is sent then. | [optional] 
**key_id** | **str** | Current signing secret generation (X-Integration-Key-Id). | [optional] 
**previous_key_id** | **str** |  | [optional] 
**previous_valid_until** | **datetime** |  | [optional] 
**waiting** | **int** | Deliveries queued (held while paused). | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**secret** | **str** | Only on create and rotate-secret. | [optional] 

## Example

```python
from goadserver.models.user_webhook import UserWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of UserWebhook from a JSON string
user_webhook_instance = UserWebhook.from_json(json)
# print the JSON string representation of the object
print(UserWebhook.to_json())

# convert the object into a dict
user_webhook_dict = user_webhook_instance.to_dict()
# create an instance of UserWebhook from a dict
user_webhook_from_dict = UserWebhook.from_dict(user_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



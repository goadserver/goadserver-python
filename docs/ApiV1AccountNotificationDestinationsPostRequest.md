# ApiV1AccountNotificationDestinationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**label** | **str** |  | [optional] 
**token** | **str** | Telegram bot token. Write-only. | [optional] 
**url** | **str** | Slack incoming-webhook URL. Write-only. | [optional] 
**channel** | **str** | Slack channel, when the webhook does not pin one. | [optional] 

## Example

```python
from goadserver.models.api_v1_account_notification_destinations_post_request import ApiV1AccountNotificationDestinationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountNotificationDestinationsPostRequest from a JSON string
api_v1_account_notification_destinations_post_request_instance = ApiV1AccountNotificationDestinationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountNotificationDestinationsPostRequest.to_json())

# convert the object into a dict
api_v1_account_notification_destinations_post_request_dict = api_v1_account_notification_destinations_post_request_instance.to_dict()
# create an instance of ApiV1AccountNotificationDestinationsPostRequest from a dict
api_v1_account_notification_destinations_post_request_from_dict = ApiV1AccountNotificationDestinationsPostRequest.from_dict(api_v1_account_notification_destinations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



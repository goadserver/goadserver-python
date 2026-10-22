# ApiV1AccountNotificationPreferencesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefs** | **Dict[str, object]** | Event key → {email, inapp, dest} in the shape the read returns. | [optional] 
**digest** | **str** | Digest cadence for batched email. | [optional] 

## Example

```python
from goadserver.models.api_v1_account_notification_preferences_put_request import ApiV1AccountNotificationPreferencesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountNotificationPreferencesPutRequest from a JSON string
api_v1_account_notification_preferences_put_request_instance = ApiV1AccountNotificationPreferencesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountNotificationPreferencesPutRequest.to_json())

# convert the object into a dict
api_v1_account_notification_preferences_put_request_dict = api_v1_account_notification_preferences_put_request_instance.to_dict()
# create an instance of ApiV1AccountNotificationPreferencesPutRequest from a dict
api_v1_account_notification_preferences_put_request_from_dict = ApiV1AccountNotificationPreferencesPutRequest.from_dict(api_v1_account_notification_preferences_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



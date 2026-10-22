# ApiV1AccountNotificationsReadPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**all** | **bool** | Mark every unread item read. | [optional] 

## Example

```python
from goadserver.models.api_v1_account_notifications_read_post_request import ApiV1AccountNotificationsReadPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountNotificationsReadPostRequest from a JSON string
api_v1_account_notifications_read_post_request_instance = ApiV1AccountNotificationsReadPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountNotificationsReadPostRequest.to_json())

# convert the object into a dict
api_v1_account_notifications_read_post_request_dict = api_v1_account_notifications_read_post_request_instance.to_dict()
# create an instance of ApiV1AccountNotificationsReadPostRequest from a dict
api_v1_account_notifications_read_post_request_from_dict = ApiV1AccountNotificationsReadPostRequest.from_dict(api_v1_account_notifications_read_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AccountPreferencesKeyPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Opaque value. Send the empty string to clear. | 

## Example

```python
from goadserver.models.api_v1_account_preferences_key_put_request import ApiV1AccountPreferencesKeyPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountPreferencesKeyPutRequest from a JSON string
api_v1_account_preferences_key_put_request_instance = ApiV1AccountPreferencesKeyPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountPreferencesKeyPutRequest.to_json())

# convert the object into a dict
api_v1_account_preferences_key_put_request_dict = api_v1_account_preferences_key_put_request_instance.to_dict()
# create an instance of ApiV1AccountPreferencesKeyPutRequest from a dict
api_v1_account_preferences_key_put_request_from_dict = ApiV1AccountPreferencesKeyPutRequest.from_dict(api_v1_account_preferences_key_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



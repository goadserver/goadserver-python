# ApiV1TrackerSourceAccountsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrackerSourceAccount]**](TrackerSourceAccount.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_source_accounts_get200_response import ApiV1TrackerSourceAccountsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerSourceAccountsGet200Response from a JSON string
api_v1_tracker_source_accounts_get200_response_instance = ApiV1TrackerSourceAccountsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerSourceAccountsGet200Response.to_json())

# convert the object into a dict
api_v1_tracker_source_accounts_get200_response_dict = api_v1_tracker_source_accounts_get200_response_instance.to_dict()
# create an instance of ApiV1TrackerSourceAccountsGet200Response from a dict
api_v1_tracker_source_accounts_get200_response_from_dict = ApiV1TrackerSourceAccountsGet200Response.from_dict(api_v1_tracker_source_accounts_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



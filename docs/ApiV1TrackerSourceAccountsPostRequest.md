# ApiV1TrackerSourceAccountsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** |  | 
**label** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**source_id** | **int** | Traffic source the spend belongs to. | [optional] 
**is_active** | **bool** |  | [optional] 
**credentials** | **Dict[str, str]** | Driver-specific secrets. Write-only. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_source_accounts_post_request import ApiV1TrackerSourceAccountsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerSourceAccountsPostRequest from a JSON string
api_v1_tracker_source_accounts_post_request_instance = ApiV1TrackerSourceAccountsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerSourceAccountsPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_source_accounts_post_request_dict = api_v1_tracker_source_accounts_post_request_instance.to_dict()
# create an instance of ApiV1TrackerSourceAccountsPostRequest from a dict
api_v1_tracker_source_accounts_post_request_from_dict = ApiV1TrackerSourceAccountsPostRequest.from_dict(api_v1_tracker_source_accounts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



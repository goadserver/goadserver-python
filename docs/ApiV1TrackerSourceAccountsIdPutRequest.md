# ApiV1TrackerSourceAccountsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**credentials** | **Dict[str, str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_source_accounts_id_put_request import ApiV1TrackerSourceAccountsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerSourceAccountsIdPutRequest from a JSON string
api_v1_tracker_source_accounts_id_put_request_instance = ApiV1TrackerSourceAccountsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerSourceAccountsIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_source_accounts_id_put_request_dict = api_v1_tracker_source_accounts_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerSourceAccountsIdPutRequest from a dict
api_v1_tracker_source_accounts_id_put_request_from_dict = ApiV1TrackerSourceAccountsIdPutRequest.from_dict(api_v1_tracker_source_accounts_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



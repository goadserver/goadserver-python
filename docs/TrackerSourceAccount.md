# TrackerSourceAccount

A credentialed ad account spend is pulled from. Credentials are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**driver** | **str** | Traffic-source API slug — see /cost-drivers. | [optional] 
**driver_name** | **str** |  | [optional] 
**driver_implemented** | **bool** | false when this build ships no puller for the driver. | [optional] 
**label** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**source_id** | **int** | Traffic source the spend is attributed to. | [optional] 
**is_active** | **bool** |  | [optional] 
**last_sync_at** | **str** |  | [optional] 
**last_sync_status** | **str** |  | [optional] 
**last_sync_error** | **str** | Empty on a clean sync. | [optional] 

## Example

```python
from goadserver.models.tracker_source_account import TrackerSourceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerSourceAccount from a JSON string
tracker_source_account_instance = TrackerSourceAccount.from_json(json)
# print the JSON string representation of the object
print(TrackerSourceAccount.to_json())

# convert the object into a dict
tracker_source_account_dict = tracker_source_account_instance.to_dict()
# create an instance of TrackerSourceAccount from a dict
tracker_source_account_from_dict = TrackerSourceAccount.from_dict(tracker_source_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



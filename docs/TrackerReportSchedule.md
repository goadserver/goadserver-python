# TrackerReportSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**cadence** | **str** |  | [optional] 
**day_of_week** | **int** | Weekly cadence only. | [optional] 
**day_of_month** | **int** | Monthly cadence only. | [optional] 
**hour_of_day** | **int** |  | [optional] 
**recipients** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_sent_at** | **str** | Empty until the first delivery. | [optional] 

## Example

```python
from goadserver.models.tracker_report_schedule import TrackerReportSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerReportSchedule from a JSON string
tracker_report_schedule_instance = TrackerReportSchedule.from_json(json)
# print the JSON string representation of the object
print(TrackerReportSchedule.to_json())

# convert the object into a dict
tracker_report_schedule_dict = tracker_report_schedule_instance.to_dict()
# create an instance of TrackerReportSchedule from a dict
tracker_report_schedule_from_dict = TrackerReportSchedule.from_dict(tracker_report_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1TrackerReportSchedulesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**report_type** | **str** |  | 
**cadence** | **str** |  | 
**day_of_week** | **int** | For weekly cadence. | [optional] 
**day_of_month** | **int** | For monthly cadence. | [optional] 
**hour_of_day** | **int** |  | [optional] 
**recipients** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_report_schedules_post_request import ApiV1TrackerReportSchedulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerReportSchedulesPostRequest from a JSON string
api_v1_tracker_report_schedules_post_request_instance = ApiV1TrackerReportSchedulesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerReportSchedulesPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_report_schedules_post_request_dict = api_v1_tracker_report_schedules_post_request_instance.to_dict()
# create an instance of ApiV1TrackerReportSchedulesPostRequest from a dict
api_v1_tracker_report_schedules_post_request_from_dict = ApiV1TrackerReportSchedulesPostRequest.from_dict(api_v1_tracker_report_schedules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1TrackerReportSchedulesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**cadence** | **str** |  | [optional] 
**day_of_week** | **int** |  | [optional] 
**day_of_month** | **int** |  | [optional] 
**hour_of_day** | **int** |  | [optional] 
**recipients** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_report_schedules_id_put_request import ApiV1TrackerReportSchedulesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerReportSchedulesIdPutRequest from a JSON string
api_v1_tracker_report_schedules_id_put_request_instance = ApiV1TrackerReportSchedulesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerReportSchedulesIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_report_schedules_id_put_request_dict = api_v1_tracker_report_schedules_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerReportSchedulesIdPutRequest from a dict
api_v1_tracker_report_schedules_id_put_request_from_dict = ApiV1TrackerReportSchedulesIdPutRequest.from_dict(api_v1_tracker_report_schedules_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



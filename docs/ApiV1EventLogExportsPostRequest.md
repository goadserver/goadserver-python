# ApiV1EventLogExportsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **date** |  | [optional] 
**date_to** | **date** | At most 31 days after date_from. | [optional] 
**side** | **str** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**ad_id** | **int** |  | [optional] 
**site_id** | **int** |  | [optional] 
**zone_id** | **int** |  | [optional] 
**event** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_event_log_exports_post_request import ApiV1EventLogExportsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1EventLogExportsPostRequest from a JSON string
api_v1_event_log_exports_post_request_instance = ApiV1EventLogExportsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1EventLogExportsPostRequest.to_json())

# convert the object into a dict
api_v1_event_log_exports_post_request_dict = api_v1_event_log_exports_post_request_instance.to_dict()
# create an instance of ApiV1EventLogExportsPostRequest from a dict
api_v1_event_log_exports_post_request_from_dict = ApiV1EventLogExportsPostRequest.from_dict(api_v1_event_log_exports_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



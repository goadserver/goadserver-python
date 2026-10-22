# ApiV1TrackerTrackingLinksIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 
**weights** | **List[int]** |  | [optional] 
**tags** | **str** |  | [optional] 
**tokens** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_id_put_request import ApiV1TrackerTrackingLinksIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksIdPutRequest from a JSON string
api_v1_tracker_tracking_links_id_put_request_instance = ApiV1TrackerTrackingLinksIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_id_put_request_dict = api_v1_tracker_tracking_links_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksIdPutRequest from a dict
api_v1_tracker_tracking_links_id_put_request_from_dict = ApiV1TrackerTrackingLinksIdPutRequest.from_dict(api_v1_tracker_tracking_links_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



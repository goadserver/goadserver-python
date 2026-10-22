# ApiV1TrackerTrackingLinksBulkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**ids** | **List[int]** |  | 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_bulk_post_request import ApiV1TrackerTrackingLinksBulkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksBulkPostRequest from a JSON string
api_v1_tracker_tracking_links_bulk_post_request_instance = ApiV1TrackerTrackingLinksBulkPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksBulkPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_bulk_post_request_dict = api_v1_tracker_tracking_links_bulk_post_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksBulkPostRequest from a dict
api_v1_tracker_tracking_links_bulk_post_request_from_dict = ApiV1TrackerTrackingLinksBulkPostRequest.from_dict(api_v1_tracker_tracking_links_bulk_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



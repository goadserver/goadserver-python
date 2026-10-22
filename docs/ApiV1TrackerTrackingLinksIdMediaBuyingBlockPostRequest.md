# ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** | The network&#39;s placement id. | [optional] 
**blocked** | **bool** | false unblocks. | [optional] [default to True]

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_block_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest from a JSON string
api_v1_tracker_tracking_links_id_media_buying_block_post_request_instance = ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_id_media_buying_block_post_request_dict = api_v1_tracker_tracking_links_id_media_buying_block_post_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest from a dict
api_v1_tracker_tracking_links_id_media_buying_block_post_request_from_dict = ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest.from_dict(api_v1_tracker_tracking_links_id_media_buying_block_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



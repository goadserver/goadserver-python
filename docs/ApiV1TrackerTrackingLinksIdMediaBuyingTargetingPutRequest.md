# ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**zones** | [**List[ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner]**](ApiV1AdspacesIdMediaBuyingTargetingPutRequestZonesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_targeting_put_request import ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest from a JSON string
api_v1_tracker_tracking_links_id_media_buying_targeting_put_request_instance = ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_id_media_buying_targeting_put_request_dict = api_v1_tracker_tracking_links_id_media_buying_targeting_put_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest from a dict
api_v1_tracker_tracking_links_id_media_buying_targeting_put_request_from_dict = ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest.from_dict(api_v1_tracker_tracking_links_id_media_buying_targeting_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



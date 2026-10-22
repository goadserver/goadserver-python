# ApiV1TrackerTrackingLinksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_id** | **int** | Traffic source this link belongs to (see /sources). | 
**offer_id** | **int** | Single-offer link. | [optional] 
**offer_ids** | **List[int]** | Smartlink — several offers, narrowed per click by targeting and eCPM. | [optional] 
**weights** | **List[int]** | Rotation weights, positionally matching offer_ids. | [optional] 
**tags** | **str** |  | [optional] 
**tokens** | **List[str]** | Macro slots to carry on the click URL — see /tokens. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_post_request import ApiV1TrackerTrackingLinksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksPostRequest from a JSON string
api_v1_tracker_tracking_links_post_request_instance = ApiV1TrackerTrackingLinksPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_post_request_dict = api_v1_tracker_tracking_links_post_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksPostRequest from a dict
api_v1_tracker_tracking_links_post_request_from_dict = ApiV1TrackerTrackingLinksPostRequest.from_dict(api_v1_tracker_tracking_links_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



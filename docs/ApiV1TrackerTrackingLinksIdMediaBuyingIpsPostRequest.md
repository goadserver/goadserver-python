# ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**cidrs** | **List[str]** | IPv4 / IPv6 addresses or CIDR ranges. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_ips_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest from a JSON string
api_v1_tracker_tracking_links_id_media_buying_ips_post_request_instance = ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_id_media_buying_ips_post_request_dict = api_v1_tracker_tracking_links_id_media_buying_ips_post_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest from a dict
api_v1_tracker_tracking_links_id_media_buying_ips_post_request_from_dict = ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest.from_dict(api_v1_tracker_tracking_links_id_media_buying_ips_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



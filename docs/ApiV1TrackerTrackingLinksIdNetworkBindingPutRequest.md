# ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adnetwork_id** | **int** |  | 
**adnetwork_campaignid** | **int** |  | [optional] 
**adnetwork_campaign_kind** | **str** |  | [optional] 
**auto_api** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_tracking_links_id_network_binding_put_request import ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest from a JSON string
api_v1_tracker_tracking_links_id_network_binding_put_request_instance = ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_tracking_links_id_network_binding_put_request_dict = api_v1_tracker_tracking_links_id_network_binding_put_request_instance.to_dict()
# create an instance of ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest from a dict
api_v1_tracker_tracking_links_id_network_binding_put_request_from_dict = ApiV1TrackerTrackingLinksIdNetworkBindingPutRequest.from_dict(api_v1_tracker_tracking_links_id_network_binding_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



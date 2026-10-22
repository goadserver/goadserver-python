# ApiV1TrackerAffiliateNetworksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**template_slug** | **str** |  | [optional] 
**payout_currency** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_affiliate_networks_post_request import ApiV1TrackerAffiliateNetworksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerAffiliateNetworksPostRequest from a JSON string
api_v1_tracker_affiliate_networks_post_request_instance = ApiV1TrackerAffiliateNetworksPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerAffiliateNetworksPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_affiliate_networks_post_request_dict = api_v1_tracker_affiliate_networks_post_request_instance.to_dict()
# create an instance of ApiV1TrackerAffiliateNetworksPostRequest from a dict
api_v1_tracker_affiliate_networks_post_request_from_dict = ApiV1TrackerAffiliateNetworksPostRequest.from_dict(api_v1_tracker_affiliate_networks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



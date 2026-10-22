# ApiV1TrackerAffiliateNetworksIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_slug** | **str** |  | [optional] 
**payout_currency** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_affiliate_networks_id_put_request import ApiV1TrackerAffiliateNetworksIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerAffiliateNetworksIdPutRequest from a JSON string
api_v1_tracker_affiliate_networks_id_put_request_instance = ApiV1TrackerAffiliateNetworksIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerAffiliateNetworksIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_affiliate_networks_id_put_request_dict = api_v1_tracker_affiliate_networks_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerAffiliateNetworksIdPutRequest from a dict
api_v1_tracker_affiliate_networks_id_put_request_from_dict = ApiV1TrackerAffiliateNetworksIdPutRequest.from_dict(api_v1_tracker_affiliate_networks_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



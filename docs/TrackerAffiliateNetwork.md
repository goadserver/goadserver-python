# TrackerAffiliateNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**payout_currency** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**track_params** | **Dict[str, object]** | Postback token mapping — what the network calls each field. | [optional] 
**options** | **Dict[str, object]** |  | [optional] 

## Example

```python
from goadserver.models.tracker_affiliate_network import TrackerAffiliateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerAffiliateNetwork from a JSON string
tracker_affiliate_network_instance = TrackerAffiliateNetwork.from_json(json)
# print the JSON string representation of the object
print(TrackerAffiliateNetwork.to_json())

# convert the object into a dict
tracker_affiliate_network_dict = tracker_affiliate_network_instance.to_dict()
# create an instance of TrackerAffiliateNetwork from a dict
tracker_affiliate_network_from_dict = TrackerAffiliateNetwork.from_dict(tracker_affiliate_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



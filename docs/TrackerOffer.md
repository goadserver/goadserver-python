# TrackerOffer

An offer, stored as the `roncampaigns` row the click pipeline already uses (`adtypeid=21`). Field names are the storage names, unchanged — the same values the panel reads. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**paytype** | **str** | Payout model — fixed CPA or revenue share. | [optional] 
**fix_cpa** | **float** | Fixed payout per conversion when paytype is CPA. | [optional] 
**countrys** | **str** | Comma-separated country codes the offer targets. Empty &#x3D; worldwide. | [optional] 
**affiliate_network_id** | **int** | 0 when the offer belongs to no network. | [optional] 
**network_name** | **str** | Resolved name for affiliate_network_id, empty when unset. | [optional] 
**failover_offer_id** | **int** | Offer redirected to once this one caps out. 0 &#x3D; none. | [optional] 
**failover_offer_name** | **str** |  | [optional] 
**as_failover** | **bool** | Failover-only — never picked directly. | [optional] 
**ispaused** | **bool** |  | [optional] 
**dayactive** | **int** | Conversions counted against the daily cap today. | [optional] 
**offertypeid** | **int** |  | [optional] 
**tracker_tags** | **str** | Comma-separated tags. | [optional] 
**groupid** | **str** |  | [optional] 

## Example

```python
from goadserver.models.tracker_offer import TrackerOffer

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerOffer from a JSON string
tracker_offer_instance = TrackerOffer.from_json(json)
# print the JSON string representation of the object
print(TrackerOffer.to_json())

# convert the object into a dict
tracker_offer_dict = tracker_offer_instance.to_dict()
# create an instance of TrackerOffer from a dict
tracker_offer_from_dict = TrackerOffer.from_dict(tracker_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



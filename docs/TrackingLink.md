# TrackingLink

A tracking link — a `publisher_adzones` row under a hidden source site. `is_smartlink` distinguishes the two shapes: a single-offer link redirects straight through, a smartlink carries several `offer_ids` and lets each offer's own targeting and eCPM pick the winner per click. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adzone_id** | **int** | The link&#39;s id — pass this as {id} on the link routes. | [optional] 
**name** | **str** |  | [optional] 
**siteid** | **int** | Traffic source the link belongs to. | [optional] 
**source_name** | **str** |  | [optional] 
**source_description** | **str** |  | [optional] 
**source_template** | **str** | Macro template slug inherited from the source. | [optional] 
**url_path** | **str** | The click URL path to hand the traffic source. | [optional] 
**is_smartlink** | **bool** |  | [optional] 
**offer_id** | **int** | Bound offer on a single-offer link. 0 on a smartlink. | [optional] 
**offer_name** | **str** |  | [optional] 
**offer_ids** | **List[int]** | Offer pool on a smartlink. | [optional] 
**weights** | **List[int]** | Rotation weights, positionally matching offer_ids. | [optional] 
**tokens** | **List[str]** | Macro slots the click URL carries. | [optional] 
**tags** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**adnetwork_id** | **int** | Bound ad network, 0 when unbound. | [optional] 
**adnetwork_name** | **str** |  | [optional] 
**adnetwork_campaignid** | **int** |  | [optional] 
**adnetwork_campaign_kind** | **str** |  | [optional] 
**adnetwork_state** | **str** |  | [optional] 
**adnetwork_auto_api** | **bool** | Whether rules may push changes back to the network. | [optional] 

## Example

```python
from goadserver.models.tracking_link import TrackingLink

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLink from a JSON string
tracking_link_instance = TrackingLink.from_json(json)
# print the JSON string representation of the object
print(TrackingLink.to_json())

# convert the object into a dict
tracking_link_dict = tracking_link_instance.to_dict()
# create an instance of TrackingLink from a dict
tracking_link_from_dict = TrackingLink.from_dict(tracking_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



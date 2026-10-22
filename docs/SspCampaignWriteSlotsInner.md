# SspCampaignWriteSlotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot_id** | **str** |  | 
**ad_type** | **str** |  | 
**w** | **int** |  | [optional] 
**h** | **int** |  | [optional] 
**floor_price** | **float** | CPM floor in currency units. | [optional] 

## Example

```python
from goadserver.models.ssp_campaign_write_slots_inner import SspCampaignWriteSlotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SspCampaignWriteSlotsInner from a JSON string
ssp_campaign_write_slots_inner_instance = SspCampaignWriteSlotsInner.from_json(json)
# print the JSON string representation of the object
print(SspCampaignWriteSlotsInner.to_json())

# convert the object into a dict
ssp_campaign_write_slots_inner_dict = ssp_campaign_write_slots_inner_instance.to_dict()
# create an instance of SspCampaignWriteSlotsInner from a dict
ssp_campaign_write_slots_inner_from_dict = SspCampaignWriteSlotsInner.from_dict(ssp_campaign_write_slots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



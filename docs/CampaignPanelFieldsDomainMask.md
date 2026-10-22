# CampaignPanelFieldsDomainMask

rtb on AdManager networks (options): mask publisher domains in the bid request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_domain_mask import CampaignPanelFieldsDomainMask

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsDomainMask from a JSON string
campaign_panel_fields_domain_mask_instance = CampaignPanelFieldsDomainMask.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsDomainMask.to_json())

# convert the object into a dict
campaign_panel_fields_domain_mask_dict = campaign_panel_fields_domain_mask_instance.to_dict()
# create an instance of CampaignPanelFieldsDomainMask from a dict
campaign_panel_fields_domain_mask_from_dict = CampaignPanelFieldsDomainMask.from_dict(campaign_panel_fields_domain_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignPanelFieldsPriority

ron Priority Mode, see the create body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_priority import CampaignPanelFieldsPriority

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsPriority from a JSON string
campaign_panel_fields_priority_instance = CampaignPanelFieldsPriority.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsPriority.to_json())

# convert the object into a dict
campaign_panel_fields_priority_dict = campaign_panel_fields_priority_instance.to_dict()
# create an instance of CampaignPanelFieldsPriority from a dict
campaign_panel_fields_priority_from_dict = CampaignPanelFieldsPriority.from_dict(campaign_panel_fields_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



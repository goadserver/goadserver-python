# CampaignPanelFieldsDayParting

ron/cpm (not flat), stored in the campaign options. `ranges` maps `\"<weekday 0-6>-<HH:MM>\"` to 1 and is replaced as a whole.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**half_hours** | **bool** |  | [optional] 
**ranges** | **Dict[str, int]** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_day_parting import CampaignPanelFieldsDayParting

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsDayParting from a JSON string
campaign_panel_fields_day_parting_instance = CampaignPanelFieldsDayParting.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsDayParting.to_json())

# convert the object into a dict
campaign_panel_fields_day_parting_dict = campaign_panel_fields_day_parting_instance.to_dict()
# create an instance of CampaignPanelFieldsDayParting from a dict
campaign_panel_fields_day_parting_from_dict = CampaignPanelFieldsDayParting.from_dict(campaign_panel_fields_day_parting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



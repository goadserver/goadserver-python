# CampaignPanelFieldsBoosterSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startdate** | **date** |  | [optional] 
**enddate** | **date** |  | [optional] 
**pct** | **float** |  | [optional] 
**ecpm** | **float** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_booster_settings import CampaignPanelFieldsBoosterSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsBoosterSettings from a JSON string
campaign_panel_fields_booster_settings_instance = CampaignPanelFieldsBoosterSettings.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsBoosterSettings.to_json())

# convert the object into a dict
campaign_panel_fields_booster_settings_dict = campaign_panel_fields_booster_settings_instance.to_dict()
# create an instance of CampaignPanelFieldsBoosterSettings from a dict
campaign_panel_fields_booster_settings_from_dict = CampaignPanelFieldsBoosterSettings.from_dict(campaign_panel_fields_booster_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



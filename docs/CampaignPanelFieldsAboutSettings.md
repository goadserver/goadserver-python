# CampaignPanelFieldsAboutSettings

ron banner (ad type 2) on AdManager networks: alternative company info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inuse** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_about_settings import CampaignPanelFieldsAboutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsAboutSettings from a JSON string
campaign_panel_fields_about_settings_instance = CampaignPanelFieldsAboutSettings.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsAboutSettings.to_json())

# convert the object into a dict
campaign_panel_fields_about_settings_dict = campaign_panel_fields_about_settings_instance.to_dict()
# create an instance of CampaignPanelFieldsAboutSettings from a dict
campaign_panel_fields_about_settings_from_dict = CampaignPanelFieldsAboutSettings.from_dict(campaign_panel_fields_about_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



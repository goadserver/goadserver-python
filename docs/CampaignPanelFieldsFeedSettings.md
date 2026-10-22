# CampaignPanelFieldsFeedSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivate_items** | **int** |  | [optional] 
**mincpm** | **float** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_feed_settings import CampaignPanelFieldsFeedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsFeedSettings from a JSON string
campaign_panel_fields_feed_settings_instance = CampaignPanelFieldsFeedSettings.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsFeedSettings.to_json())

# convert the object into a dict
campaign_panel_fields_feed_settings_dict = campaign_panel_fields_feed_settings_instance.to_dict()
# create an instance of CampaignPanelFieldsFeedSettings from a dict
campaign_panel_fields_feed_settings_from_dict = CampaignPanelFieldsFeedSettings.from_dict(campaign_panel_fields_feed_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



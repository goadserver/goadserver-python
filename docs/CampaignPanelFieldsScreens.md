# CampaignPanelFieldsScreens

Banner (ad type 2) ron campaigns on networks with DOOH screens, stored in the campaign options: run on digital screens (adzone type 45). Screens play only campaigns with `on`; `only` keeps the campaign off every other zone; `venues` (empty = any) and a geo-fence (`radius_km` around `lat`/`lon`, 0 = anywhere) narrow the screens. A play is billed as the CPM bid × the screen's audience_per_play, so use CPM and a creative in the screen's size. Keys you omit on PATCH keep their stored value. Not offered elsewhere (422).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**only** | **bool** |  | [optional] 
**venues** | **List[str]** |  | [optional] 
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 
**radius_km** | **float** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_screens import CampaignPanelFieldsScreens

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsScreens from a JSON string
campaign_panel_fields_screens_instance = CampaignPanelFieldsScreens.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsScreens.to_json())

# convert the object into a dict
campaign_panel_fields_screens_dict = campaign_panel_fields_screens_instance.to_dict()
# create an instance of CampaignPanelFieldsScreens from a dict
campaign_panel_fields_screens_from_dict = CampaignPanelFieldsScreens.from_dict(campaign_panel_fields_screens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



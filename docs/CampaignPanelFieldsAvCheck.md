# CampaignPanelFieldsAvCheck

ron/cpm on AdManager networks, stored in the campaign options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**target** | **int** |  | [optional] 
**auto** | **bool** |  | [optional] 
**allow_verified** | **bool** |  | [optional] 
**countries** | **List[object]** |  | [optional] 
**us_regions** | **List[object]** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_av_check import CampaignPanelFieldsAvCheck

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsAvCheck from a JSON string
campaign_panel_fields_av_check_instance = CampaignPanelFieldsAvCheck.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsAvCheck.to_json())

# convert the object into a dict
campaign_panel_fields_av_check_dict = campaign_panel_fields_av_check_instance.to_dict()
# create an instance of CampaignPanelFieldsAvCheck from a dict
campaign_panel_fields_av_check_from_dict = CampaignPanelFieldsAvCheck.from_dict(campaign_panel_fields_av_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



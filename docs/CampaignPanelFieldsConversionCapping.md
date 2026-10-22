# CampaignPanelFieldsConversionCapping

ron/cpm: stop after `max` conversions of `conv_type` per day or in total.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inuse** | **bool** |  | [optional] 
**conv_type** | **int** |  | [optional] 
**cap_type** | **str** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_conversion_capping import CampaignPanelFieldsConversionCapping

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsConversionCapping from a JSON string
campaign_panel_fields_conversion_capping_instance = CampaignPanelFieldsConversionCapping.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsConversionCapping.to_json())

# convert the object into a dict
campaign_panel_fields_conversion_capping_dict = campaign_panel_fields_conversion_capping_instance.to_dict()
# create an instance of CampaignPanelFieldsConversionCapping from a dict
campaign_panel_fields_conversion_capping_from_dict = CampaignPanelFieldsConversionCapping.from_dict(campaign_panel_fields_conversion_capping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



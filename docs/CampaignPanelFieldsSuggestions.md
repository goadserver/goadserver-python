# CampaignPanelFieldsSuggestions

ron video (ad type 4), stored in the options: native suggestions from one of your native (ad type 3) ron campaigns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] 
**campaign_id** | **int** |  | [optional] 

## Example

```python
from goadserver.models.campaign_panel_fields_suggestions import CampaignPanelFieldsSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPanelFieldsSuggestions from a JSON string
campaign_panel_fields_suggestions_instance = CampaignPanelFieldsSuggestions.from_json(json)
# print the JSON string representation of the object
print(CampaignPanelFieldsSuggestions.to_json())

# convert the object into a dict
campaign_panel_fields_suggestions_dict = campaign_panel_fields_suggestions_instance.to_dict()
# create an instance of CampaignPanelFieldsSuggestions from a dict
campaign_panel_fields_suggestions_from_dict = CampaignPanelFieldsSuggestions.from_dict(campaign_panel_fields_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



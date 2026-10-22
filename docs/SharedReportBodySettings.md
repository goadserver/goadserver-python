# SharedReportBodySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_types** | **List[int]** |  | [optional] 
**selling_types** | **List[int]** |  | [optional] 
**device_types** | **List[int]** |  | [optional] 
**countries** | **List[str]** |  | [optional] 
**visible_metrics** | **List[str]** |  | [optional] 
**visible_conv_types** | **List[int]** |  | [optional] 
**allowed_groupby** | **List[str]** |  | [optional] 
**default_groupby** | **str** |  | [optional] [default to 'period']
**allowed_viewtypes** | **List[str]** |  | [optional] 
**viewer_filters** | **List[str]** |  | [optional] 
**follow_groups** | **bool** | Advertiser reports: also cover every campaign filed under &#x60;tagids&#x60;, now and later. | [optional] 
**show_names** | **bool** |  | [optional] [default to True]

## Example

```python
from goadserver.models.shared_report_body_settings import SharedReportBodySettings

# TODO update the JSON string below
json = "{}"
# create an instance of SharedReportBodySettings from a JSON string
shared_report_body_settings_instance = SharedReportBodySettings.from_json(json)
# print the JSON string representation of the object
print(SharedReportBodySettings.to_json())

# convert the object into a dict
shared_report_body_settings_dict = shared_report_body_settings_instance.to_dict()
# create an instance of SharedReportBodySettings from a dict
shared_report_body_settings_from_dict = SharedReportBodySettings.from_dict(shared_report_body_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



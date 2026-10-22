# SharedReportBodyOptions

Stats adjustment shown to viewers; dropped unless the account holds adjust_stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **bool** |  | [optional] 
**impressions** | [**SharedReportAdjust**](SharedReportAdjust.md) |  | [optional] 
**clicks** | [**SharedReportAdjust**](SharedReportAdjust.md) |  | [optional] 
**paid** | [**SharedReportAdjust**](SharedReportAdjust.md) |  | [optional] 

## Example

```python
from goadserver.models.shared_report_body_options import SharedReportBodyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SharedReportBodyOptions from a JSON string
shared_report_body_options_instance = SharedReportBodyOptions.from_json(json)
# print the JSON string representation of the object
print(SharedReportBodyOptions.to_json())

# convert the object into a dict
shared_report_body_options_dict = shared_report_body_options_instance.to_dict()
# create an instance of SharedReportBodyOptions from a dict
shared_report_body_options_from_dict = SharedReportBodyOptions.from_dict(shared_report_body_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



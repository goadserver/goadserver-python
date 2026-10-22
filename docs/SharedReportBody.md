# SharedReportBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**statstype** | **str** | Anything else is stored as advertiser. | [optional] [default to 'advertiser']
**campaigns** | [**List[SharedReportBodyCampaignsInner]**](SharedReportBodyCampaignsInner.md) |  | [optional] 
**sites** | [**List[ApiV1SharedReportsIdPutRequestSitesInner]**](ApiV1SharedReportsIdPutRequestSitesInner.md) |  | [optional] 
**settings** | [**SharedReportBodySettings**](SharedReportBodySettings.md) |  | [optional] 
**options** | [**SharedReportBodyOptions**](SharedReportBodyOptions.md) |  | [optional] 
**tagids** | **str** | CSV of tag ids (GET /api/v1/tags). | [optional] 

## Example

```python
from goadserver.models.shared_report_body import SharedReportBody

# TODO update the JSON string below
json = "{}"
# create an instance of SharedReportBody from a JSON string
shared_report_body_instance = SharedReportBody.from_json(json)
# print the JSON string representation of the object
print(SharedReportBody.to_json())

# convert the object into a dict
shared_report_body_dict = shared_report_body_instance.to_dict()
# create an instance of SharedReportBody from a dict
shared_report_body_from_dict = SharedReportBody.from_dict(shared_report_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1SharedReportsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tagids** | **str** |  | [optional] 
**campaigns** | [**List[ApiV1SharedReportsIdPutRequestCampaignsInner]**](ApiV1SharedReportsIdPutRequestCampaignsInner.md) |  | [optional] 
**sites** | [**List[ApiV1SharedReportsIdPutRequestSitesInner]**](ApiV1SharedReportsIdPutRequestSitesInner.md) |  | [optional] 
**settings** | **object** |  | [optional] 
**options** | **object** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_shared_reports_id_put_request import ApiV1SharedReportsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SharedReportsIdPutRequest from a JSON string
api_v1_shared_reports_id_put_request_instance = ApiV1SharedReportsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1SharedReportsIdPutRequest.to_json())

# convert the object into a dict
api_v1_shared_reports_id_put_request_dict = api_v1_shared_reports_id_put_request_instance.to_dict()
# create an instance of ApiV1SharedReportsIdPutRequest from a dict
api_v1_shared_reports_id_put_request_from_dict = ApiV1SharedReportsIdPutRequest.from_dict(api_v1_shared_reports_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



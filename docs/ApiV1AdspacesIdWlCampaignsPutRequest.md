# ApiV1AdspacesIdWlCampaignsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns** | [**List[ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner]**](ApiV1AdspacesIdWlCampaignsPutRequestCampaignsInner.md) |  | [optional] 
**force_wl_targeting** | **bool** |  | [optional] [default to False]
**skip_rtb_when_wl** | **bool** | Omitted &#x3D; false (the PUT always writes it). | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_adspaces_id_wl_campaigns_put_request import ApiV1AdspacesIdWlCampaignsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdWlCampaignsPutRequest from a JSON string
api_v1_adspaces_id_wl_campaigns_put_request_instance = ApiV1AdspacesIdWlCampaignsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdWlCampaignsPutRequest.to_json())

# convert the object into a dict
api_v1_adspaces_id_wl_campaigns_put_request_dict = api_v1_adspaces_id_wl_campaigns_put_request_instance.to_dict()
# create an instance of ApiV1AdspacesIdWlCampaignsPutRequest from a dict
api_v1_adspaces_id_wl_campaigns_put_request_from_dict = ApiV1AdspacesIdWlCampaignsPutRequest.from_dict(api_v1_adspaces_id_wl_campaigns_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CampaignsTypeIdBidsPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**value** | **float** | Required when mode&#x3D;set. New absolute bid (&gt;&#x3D; 0). | [optional] 
**pct** | **float** | Required when mode&#x3D;pct_inc / pct_dec. Percent change (&gt; 0). | [optional] 
**ad_ids** | **List[int]** | Optional. Subset of ad ids to update. Omit/empty for \&quot;all ads\&quot;. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_bids_patch_request import ApiV1CampaignsTypeIdBidsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdBidsPatchRequest from a JSON string
api_v1_campaigns_type_id_bids_patch_request_instance = ApiV1CampaignsTypeIdBidsPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdBidsPatchRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_bids_patch_request_dict = api_v1_campaigns_type_id_bids_patch_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdBidsPatchRequest from a dict
api_v1_campaigns_type_id_bids_patch_request_from_dict = ApiV1CampaignsTypeIdBidsPatchRequest.from_dict(api_v1_campaigns_type_id_bids_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



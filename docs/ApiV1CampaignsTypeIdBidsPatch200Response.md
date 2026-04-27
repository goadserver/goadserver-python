# ApiV1CampaignsTypeIdBidsPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | **int** | How many ads were actually updated. | [optional] 
**ad_ids** | **List[int]** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_bids_patch200_response import ApiV1CampaignsTypeIdBidsPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdBidsPatch200Response from a JSON string
api_v1_campaigns_type_id_bids_patch200_response_instance = ApiV1CampaignsTypeIdBidsPatch200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdBidsPatch200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_bids_patch200_response_dict = api_v1_campaigns_type_id_bids_patch200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdBidsPatch200Response from a dict
api_v1_campaigns_type_id_bids_patch200_response_from_dict = ApiV1CampaignsTypeIdBidsPatch200Response.from_dict(api_v1_campaigns_type_id_bids_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



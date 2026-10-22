# ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpm** | **float** | bidding: cents CPM. | [optional] 
**user_bid** | **float** | bidding: cents CPM in your currency; defaults to cpm. | [optional] 
**bid_type** | **int** |  | [optional] 
**isinuse** | **int** |  | [optional] 
**state** | **int** | state only. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest from a JSON string
api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request_instance = ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request_dict = api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest from a dict
api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request_from_dict = ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest.from_dict(api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpm** | **float** | Cents CPM. 0 &#x3D; the zone minimum. | [optional] 
**bid_type** | **int** | 1 &#x3D; smart bidding. | [optional] [default to 0]

## Example

```python
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest from a JSON string
api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request_instance = ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request_dict = api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest from a dict
api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request_from_dict = ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest.from_dict(api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



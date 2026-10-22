# ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**pool_id** | **int** | URL pool id (GET /url-pools); 0 &#x3D; detach. | 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request_instance = ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request_dict = api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest from a dict
api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



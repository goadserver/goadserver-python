# ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**pool_id** | **int** | Creative pool id (GET /creative-pools). | [optional] 
**pool_by_size** | **Dict[str, int]** | Banner size id → pool id. | [optional] 
**include_unpooled** | **bool** |  | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_update_pool_put_request_instance = ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_update_pool_put_request_dict = api_v1_campaigns_type_campaign_id_ads_update_pool_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest from a dict
api_v1_campaigns_type_campaign_id_ads_update_pool_put_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_update_pool_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



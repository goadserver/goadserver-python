# ApiV1CampaignsTypeCampaignIdAdsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**bid** | **float** |  | 
**destination_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_url** | **str** |  | [optional] 
**preview_url** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**sort_weight** | **int** |  | [optional] [default to 0]
**banner_pool_id** | **int** | Reference an existing banner pool (most common). | [optional] 
**video_pool_id** | **int** |  | [optional] 
**url_pool_id** | **int** | Independent click-URL rotation pool — combinable with any banner ref. | [optional] 
**creative_id** | **int** | Reference a single creative directly. | [optional] 
**banner_url** | **str** | Direct image URL (hosted-elsewhere creatives). | [optional] 
**banner_html** | **str** | Raw HTML/JS payload (tag-based ad units). | [optional] 
**bansizeid** | **int** | Auto-derived for pool/creative refs; required for url/html on size-aware adtypes. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request import ApiV1CampaignsTypeCampaignIdAdsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsPostRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_post_request_instance = ApiV1CampaignsTypeCampaignIdAdsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsPostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_post_request_dict = api_v1_campaigns_type_campaign_id_ads_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsPostRequest from a dict
api_v1_campaigns_type_campaign_id_ads_post_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsPostRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



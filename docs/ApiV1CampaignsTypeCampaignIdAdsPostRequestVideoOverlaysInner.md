# ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**start** | **float** | Seconds into the video. | 
**end** | **float** | Seconds; after start. | 
**pos** | **str** |  | [optional] [default to 'br']
**label** | **str** | A hotspot&#39;s text (required); a product card&#39;s button text (default Shop). | [optional] 
**title** | **str** | Product card (required). | [optional] 
**price** | **str** |  | [optional] 
**image** | **str** | Product card image, http(s) (required for a product card). | [optional] 
**url** | **str** | Landing page, http(s); empty &#x3D; the ad&#39;s destination. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner import ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner from a JSON string
api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner_instance = ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner_dict = api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner from a dict
api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner_from_dict = ApiV1CampaignsTypeCampaignIdAdsPostRequestVideoOverlaysInner.from_dict(api_v1_campaigns_type_campaign_id_ads_post_request_video_overlays_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



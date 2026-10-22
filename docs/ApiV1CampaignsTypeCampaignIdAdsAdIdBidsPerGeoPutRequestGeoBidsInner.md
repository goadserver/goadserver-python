# ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Country code as in GET /lookups/regions (e.g. US, DE). | 
**bid** | **float** | Currency units (raw cents for raw-bid keys). 0 removes the country. | 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner import ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner from a JSON string
api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner_instance = ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner_dict = api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner from a dict
api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner_from_dict = ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequestGeoBidsInner.from_dict(api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request_geo_bids_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



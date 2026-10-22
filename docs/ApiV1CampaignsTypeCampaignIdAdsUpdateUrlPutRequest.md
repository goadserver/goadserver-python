# ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**mode** | **str** |  | [optional] [default to 'set']
**url** | **str** | mode&#x3D;set: the new URL. | [optional] 
**find** | **str** | mode&#x3D;replace: text to find. | [optional] 
**replace** | **str** | mode&#x3D;replace: replacement text. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest from a JSON string
api_v1_campaigns_type_campaign_id_ads_update_url_put_request_instance = ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_campaign_id_ads_update_url_put_request_dict = api_v1_campaigns_type_campaign_id_ads_update_url_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest from a dict
api_v1_campaigns_type_campaign_id_ads_update_url_put_request_from_dict = ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest.from_dict(api_v1_campaigns_type_campaign_id_ads_update_url_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



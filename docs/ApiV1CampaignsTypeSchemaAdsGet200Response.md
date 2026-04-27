# ApiV1CampaignsTypeSchemaAdsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_type** | **str** |  | [optional] 
**campaign_ad_type** | **int** | 0 if not scoped to a campaign. | [optional] 
**fields** | **List[object]** |  | [optional] 
**creative_choice** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_schema_ads_get200_response import ApiV1CampaignsTypeSchemaAdsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeSchemaAdsGet200Response from a JSON string
api_v1_campaigns_type_schema_ads_get200_response_instance = ApiV1CampaignsTypeSchemaAdsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeSchemaAdsGet200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_schema_ads_get200_response_dict = api_v1_campaigns_type_schema_ads_get200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeSchemaAdsGet200Response from a dict
api_v1_campaigns_type_schema_ads_get200_response_from_dict = ApiV1CampaignsTypeSchemaAdsGet200Response.from_dict(api_v1_campaigns_type_schema_ads_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



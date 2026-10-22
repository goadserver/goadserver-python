# ApiV1CampaignsRonIdZonesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spaceid** | **int** | Zone id. | [optional] 
**zone** | **str** | Zone name (prefixed &#x60;[Deleted]&#x60; for a deleted zone). | [optional] 
**siteid** | **int** |  | [optional] 
**site** | **str** |  | [optional] 
**is_deleted** | **int** |  | [optional] 
**weight** | **int** | This campaign&#39;s weight on the zone (100 when none is set). | [optional] 
**owned** | **bool** | True when the zone is yours and not deleted. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_ron_id_zones_get200_response_data_inner import ApiV1CampaignsRonIdZonesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsRonIdZonesGet200ResponseDataInner from a JSON string
api_v1_campaigns_ron_id_zones_get200_response_data_inner_instance = ApiV1CampaignsRonIdZonesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsRonIdZonesGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_campaigns_ron_id_zones_get200_response_data_inner_dict = api_v1_campaigns_ron_id_zones_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1CampaignsRonIdZonesGet200ResponseDataInner from a dict
api_v1_campaigns_ron_id_zones_get200_response_data_inner_from_dict = ApiV1CampaignsRonIdZonesGet200ResponseDataInner.from_dict(api_v1_campaigns_ron_id_zones_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



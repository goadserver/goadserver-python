# ApiV1CampaignsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**campaign_type** | **str** |  | [optional] 
**ad_type** | **int** |  | [optional] 
**selling_type** | **int** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_get200_response_data_inner import ApiV1CampaignsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsGet200ResponseDataInner from a JSON string
api_v1_campaigns_get200_response_data_inner_instance = ApiV1CampaignsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_campaigns_get200_response_data_inner_dict = api_v1_campaigns_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1CampaignsGet200ResponseDataInner from a dict
api_v1_campaigns_get200_response_data_inner_from_dict = ApiV1CampaignsGet200ResponseDataInner.from_dict(api_v1_campaigns_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



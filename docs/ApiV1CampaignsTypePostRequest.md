# ApiV1CampaignsTypePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**ad_type** | **int** | See /campaigns/&lt;type&gt;/_schema for valid ids on this tenant. | 
**daily_budget** | **float** |  | [optional] 
**total_budget** | **float** |  | [optional] 
**use_campaign_budget** | **bool** |  | [optional] [default to False]
**countries** | **str** |  | [optional] 
**languages** | **str** | CSV of language ids; \&quot;0\&quot; &#x3D; all. | [optional] 
**categories** | **str** |  | [optional] 
**main_catid** | **int** |  | [optional] 
**device_type_ids** | **str** |  | [optional] 
**browser_ids** | **str** |  | [optional] 
**os_ids** | **str** |  | [optional] 
**isp_ids** | **str** |  | [optional] 
**site_types** | **str** |  | [optional] 
**regions** | **str** |  | [optional] 
**display_times** | **str** |  | [optional] 
**display_days** | **str** |  | [optional] 
**use_capping** | **bool** |  | [optional] 
**capping_hours** | **int** |  | [optional] 
**capping_minutes** | **int** |  | [optional] 
**domain_filter_id** | **int** |  | [optional] 
**whitelist_id** | **int** |  | [optional] 
**rt_include_id** | **int** |  | [optional] 
**rt_exclude_id** | **int** |  | [optional] 
**ip_pool_id** | **int** |  | [optional] 
**fx_minprice** | **float** |  | [optional] [default to 0]
**is_paused** | **bool** | Start paused (default) so you can attach ads first. | [optional] [default to True]

## Example

```python
from goadserver.models.api_v1_campaigns_type_post_request import ApiV1CampaignsTypePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypePostRequest from a JSON string
api_v1_campaigns_type_post_request_instance = ApiV1CampaignsTypePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypePostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_post_request_dict = api_v1_campaigns_type_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypePostRequest from a dict
api_v1_campaigns_type_post_request_from_dict = ApiV1CampaignsTypePostRequest.from_dict(api_v1_campaigns_type_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CampaignsTypeIdBudgetPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_budget** | **float** | Total campaign budget. | [optional] 
**use_campaign_budget** | **bool** | Enable/disable the total budget cap. | [optional] 
**max_day_budget** | **float** | Maximum spend per day. | [optional] 
**use_day_budget** | **bool** | Enable/disable the daily budget cap. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_budget_patch_request import ApiV1CampaignsTypeIdBudgetPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdBudgetPatchRequest from a JSON string
api_v1_campaigns_type_id_budget_patch_request_instance = ApiV1CampaignsTypeIdBudgetPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdBudgetPatchRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_budget_patch_request_dict = api_v1_campaigns_type_id_budget_patch_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdBudgetPatchRequest from a dict
api_v1_campaigns_type_id_budget_patch_request_from_dict = ApiV1CampaignsTypeIdBudgetPatchRequest.from_dict(api_v1_campaigns_type_id_budget_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



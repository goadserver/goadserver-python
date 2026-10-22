# ApiV1CampaignsTypeIdBudgetPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**campaign_type** | **str** |  | [optional] 
**updated** | **List[str]** | Names of the fields that were changed. | [optional] 
**max_day_budget** | **float** | The daily budget actually stored | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_budget_patch200_response import ApiV1CampaignsTypeIdBudgetPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdBudgetPatch200Response from a JSON string
api_v1_campaigns_type_id_budget_patch200_response_instance = ApiV1CampaignsTypeIdBudgetPatch200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdBudgetPatch200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_budget_patch200_response_dict = api_v1_campaigns_type_id_budget_patch200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdBudgetPatch200Response from a dict
api_v1_campaigns_type_id_budget_patch200_response_from_dict = ApiV1CampaignsTypeIdBudgetPatch200Response.from_dict(api_v1_campaigns_type_id_budget_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



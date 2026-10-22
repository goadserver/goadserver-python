# CpaOptimizerBody

CPA optimizer (target_cpa). Money in the account currency; stored as cents. `id` / `type` are accepted and ignored. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Letters, digits and spaces; anything else becomes &#x60;_&#x60;. | 
**filter_type** | **str** | What a rule blocks / re-bids. Fixed after create in the panel. | [optional] 
**max_cpa** | **float** | Spend (account currency) on a source before it is judged. Required, non-zero. | 
**max_days** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**target_cpa** | **Dict[str, float]** | Conversion-type id → target CPA (account currency). Zero entries are dropped. | [optional] 
**min_margin** | **Dict[str, int]** | Conversion-type id → minimum margin %. | [optional] 
**min_ctr** | **float** |  | [optional] 
**min_ctr_imps** | **int** |  | [optional] 
**max_ctr** | **float** |  | [optional] 
**max_ctr_imps** | **int** |  | [optional] 
**bounce_id** | **int** | Conversion pixel used as the bounce signal; -1 &#x3D; off. | [optional] 
**bounce_min_imps** | **int** |  | [optional] 
**bounce_max_perc** | **int** |  | [optional] 
**bounce_check_type** | **str** |  | [optional] 
**cpa_action** | **str** |  | [optional] 
**keep_spots_blocked** | **int** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from goadserver.models.cpa_optimizer_body import CpaOptimizerBody

# TODO update the JSON string below
json = "{}"
# create an instance of CpaOptimizerBody from a JSON string
cpa_optimizer_body_instance = CpaOptimizerBody.from_json(json)
# print the JSON string representation of the object
print(CpaOptimizerBody.to_json())

# convert the object into a dict
cpa_optimizer_body_dict = cpa_optimizer_body_instance.to_dict()
# create an instance of CpaOptimizerBody from a dict
cpa_optimizer_body_from_dict = CpaOptimizerBody.from_dict(cpa_optimizer_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



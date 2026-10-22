# CpmOptimizerBody

CPM optimizer settings (the panel's Source Optimizer → CPM form). Money in the account currency, as entered. `id`, `type`, `userid` are accepted and ignored so a fetched record can be sent back. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**opt_type** | **str** | 0 &#x3D; start after min_spendings, 1 &#x3D; after min_impressions. | [optional] 
**min_spendings** | **float** | Spend (account currency) before a source is judged. Required, non-zero. | 
**min_impressions** | **int** |  | [optional] 
**max_days** | **int** | Stats look-back in days. | [optional] 
**start_date** | **date** |  | [optional] 
**conv_type** | **str** | Conversion-type id judged on. | [optional] 
**optimise_with** | **str** |  | [optional] 
**max_cpa** | **float** | optimise_with&#x3D;conv_count: max cost per conversion (account currency). | [optional] 
**allowed_margin** | **float** | optimise_with&#x3D;conv_earnings: allowed margin %. | [optional] 
**use_bidoptimiser** | **int** |  | [optional] 
**increase_bids** | **int** |  | [optional] 
**increase_bid_perc** | **int** | Percent per step. | [optional] 
**increase_bid_cap** | **int** | Hours between steps. | [optional] 
**decrease_bids** | **int** |  | [optional] 
**decrease_bid_perc** | **int** |  | [optional] 
**decrease_bid_cap** | **int** |  | [optional] 
**min_ctr** | **float** |  | [optional] 
**min_ctr_imps** | **int** |  | [optional] 
**max_ctr** | **float** |  | [optional] 
**max_ctr_imps** | **int** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**userid** | **int** |  | [optional] [readonly] 

## Example

```python
from goadserver.models.cpm_optimizer_body import CpmOptimizerBody

# TODO update the JSON string below
json = "{}"
# create an instance of CpmOptimizerBody from a JSON string
cpm_optimizer_body_instance = CpmOptimizerBody.from_json(json)
# print the JSON string representation of the object
print(CpmOptimizerBody.to_json())

# convert the object into a dict
cpm_optimizer_body_dict = cpm_optimizer_body_instance.to_dict()
# create an instance of CpmOptimizerBody from a dict
cpm_optimizer_body_from_dict = CpmOptimizerBody.from_dict(cpm_optimizer_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AccountBillingInvoicesGet200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**dateadded** | **str** |  | [optional] 
**pay_subject** | **str** |  | [optional] 
**money** | **int** | Cents. | [optional] 
**used_currency** | **str** |  | [optional] 
**ispayed** | **bool** |  | [optional] 
**paytype** | **int** |  | [optional] 
**paytype_string** | **str** |  | [optional] 
**bandwidth_costs** | **int** | Cents. | [optional] 
**credit_state** | **int** |  | [optional] 
**datepayed** | **str** | Date, empty when unpaid. | [optional] 
**pro_adearned** | **int** | Cents. | [optional] 
**paystatus_string** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_account_billing_invoices_get200_response_results_inner import ApiV1AccountBillingInvoicesGet200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountBillingInvoicesGet200ResponseResultsInner from a JSON string
api_v1_account_billing_invoices_get200_response_results_inner_instance = ApiV1AccountBillingInvoicesGet200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountBillingInvoicesGet200ResponseResultsInner.to_json())

# convert the object into a dict
api_v1_account_billing_invoices_get200_response_results_inner_dict = api_v1_account_billing_invoices_get200_response_results_inner_instance.to_dict()
# create an instance of ApiV1AccountBillingInvoicesGet200ResponseResultsInner from a dict
api_v1_account_billing_invoices_get200_response_results_inner_from_dict = ApiV1AccountBillingInvoicesGet200ResponseResultsInner.from_dict(api_v1_account_billing_invoices_get200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



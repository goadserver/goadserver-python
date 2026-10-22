# ApiV1AccountBillingInvoicesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ApiV1AccountBillingInvoicesGet200ResponseResultsInner]**](ApiV1AccountBillingInvoicesGet200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_account_billing_invoices_get200_response import ApiV1AccountBillingInvoicesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountBillingInvoicesGet200Response from a JSON string
api_v1_account_billing_invoices_get200_response_instance = ApiV1AccountBillingInvoicesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountBillingInvoicesGet200Response.to_json())

# convert the object into a dict
api_v1_account_billing_invoices_get200_response_dict = api_v1_account_billing_invoices_get200_response_instance.to_dict()
# create an instance of ApiV1AccountBillingInvoicesGet200Response from a dict
api_v1_account_billing_invoices_get200_response_from_dict = ApiV1AccountBillingInvoicesGet200Response.from_dict(api_v1_account_billing_invoices_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



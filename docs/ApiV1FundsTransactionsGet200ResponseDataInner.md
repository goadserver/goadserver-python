# ApiV1FundsTransactionsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**dateadded** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**money** | **int** | Cents. | [optional] 
**amount** | **float** | Currency units. | [optional] 
**used_currency** | **str** |  | [optional] 
**paytype** | **int** |  | [optional] 
**ispayed** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**accepts_txn_hash** | **bool** | Open manual crypto or Payoneer deposit — takes a transaction hash / ID (POST /api/v1/funds/deposits/{id}/txn-hash). Absent otherwise. | [optional] 
**txn_ref_kind** | **str** | With accepts_txn_hash: &#x60;hash&#x60; (crypto, checked on the blockchain) or &#x60;reference&#x60; (Payoneer transaction ID, stored as given). | [optional] 
**paytype_key** | **str** | Pay type key of an open manual crypto or Payoneer deposit (for GET /api/v1/funds/deposit/{type}/{fid}). | [optional] 
**txn_claim** | [**FundsTxnClaim**](FundsTxnClaim.md) |  | [optional] 
**accepts_proof** | **bool** | Open bank / Wise deposit on a tenant that takes a proof of payment (POST /api/v1/funds/deposits/{id}/proof). Absent otherwise. | [optional] 
**proof** | [**FundsDepositProof**](FundsDepositProof.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_transactions_get200_response_data_inner import ApiV1FundsTransactionsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsTransactionsGet200ResponseDataInner from a JSON string
api_v1_funds_transactions_get200_response_data_inner_instance = ApiV1FundsTransactionsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsTransactionsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_funds_transactions_get200_response_data_inner_dict = api_v1_funds_transactions_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1FundsTransactionsGet200ResponseDataInner from a dict
api_v1_funds_transactions_get200_response_data_inner_from_dict = ApiV1FundsTransactionsGet200ResponseDataInner.from_dict(api_v1_funds_transactions_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1FundsDepositTypeFidGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **str** |  | [optional] 
**url** | **str** | Hosted checkout URL (gateway types). | [optional] 
**deposit_id** | **int** |  | [optional] 
**transaction_id** | **int** | Invoice / transfer reference. | [optional] 
**money** | **int** | Cents | [optional] 
**totalmoney** | **int** | Cents to pay. | [optional] 
**used_currency** | **str** |  | [optional] 
**bank_details** | **List[str]** |  | [optional] 
**payee** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**wallet_network** | **str** |  | [optional] 
**accepts_txn_hash** | **bool** | Manual crypto wallet or Payoneer deposit: takes the payer&#39;s transaction hash / ID (POST /api/v1/funds/deposits/{id}/txn-hash). | [optional] 
**txn_ref_kind** | **str** | &#x60;hash&#x60; (crypto, checked on the blockchain) or &#x60;reference&#x60; (Payoneer transaction ID, stored as given). | [optional] 
**accepts_proof** | **bool** | Bank / Wise deposit on a tenant that takes a proof of payment (POST /api/v1/funds/deposits/{id}/proof). | [optional] 
**proof** | [**FundsDepositProof**](FundsDepositProof.md) |  | [optional] 
**txn_claim** | [**FundsTxnClaim**](FundsTxnClaim.md) | The transaction hash attached so far and its blockchain check; null when none. | [optional] 
**invoice_paid** | **bool** |  | [optional] 
**invoice_in_progress** | **bool** |  | [optional] 
**unknown_invoice** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_deposit_type_fid_get200_response import ApiV1FundsDepositTypeFidGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsDepositTypeFidGet200Response from a JSON string
api_v1_funds_deposit_type_fid_get200_response_instance = ApiV1FundsDepositTypeFidGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsDepositTypeFidGet200Response.to_json())

# convert the object into a dict
api_v1_funds_deposit_type_fid_get200_response_dict = api_v1_funds_deposit_type_fid_get200_response_instance.to_dict()
# create an instance of ApiV1FundsDepositTypeFidGet200Response from a dict
api_v1_funds_deposit_type_fid_get200_response_from_dict = ApiV1FundsDepositTypeFidGet200Response.from_dict(api_v1_funds_deposit_type_fid_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



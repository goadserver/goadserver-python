# FundsTxnClaim

The transaction hash attached to a manual crypto deposit and its last blockchain check, or the transaction ID attached to a Payoneer deposit (status `submitted`, not checked; network / asset / amount empty). It never credits the balance — an admin approves the deposit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_hash** | **str** | Crypto: canonical form, lowercase; Ethereum / BNB Chain with 0x. Payoneer: the transaction ID as given (trimmed). | [optional] 
**network** | **str** | Empty when the tenant&#39;s generic USDT wallet has no network set, and on Payoneer deposits. | [optional] 
**asset** | **str** |  | [optional] 
**status** | **str** | &#x60;submitted&#x60;: Payoneer transaction ID, stored as a reference for the finance team, never checked automatically. | [optional] 
**reason** | **str** | Human-readable result of the check. | [optional] 
**amount** | **str** | Amount of the asset the transaction sent to the tenant&#39;s wallet (decimal string). | [optional] 
**confirmations** | **int** | Block confirmations (Ethereum 12 / BNB Chain 15 / Bitcoin 2 needed; TRON is checked against the irreversible ledger and reports 0). | [optional] 
**checked_at** | **int** | Unix time of the check. | [optional] 
**explorer_url** | **str** | Public block explorer page of the transaction. | [optional] 

## Example

```python
from goadserver.models.funds_txn_claim import FundsTxnClaim

# TODO update the JSON string below
json = "{}"
# create an instance of FundsTxnClaim from a JSON string
funds_txn_claim_instance = FundsTxnClaim.from_json(json)
# print the JSON string representation of the object
print(FundsTxnClaim.to_json())

# convert the object into a dict
funds_txn_claim_dict = funds_txn_claim_instance.to_dict()
# create an instance of FundsTxnClaim from a dict
funds_txn_claim_from_dict = FundsTxnClaim.from_dict(funds_txn_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



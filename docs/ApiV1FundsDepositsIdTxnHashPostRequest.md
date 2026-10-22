# ApiV1FundsDepositsIdTxnHashPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_hash** | **str** | Transaction hash / TxID. TRON and Bitcoin: 64 hex characters; Ethereum / BNB Chain: 0x + 64 hex. Payoneer: the transaction ID, 4–64 characters. | 

## Example

```python
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post_request import ApiV1FundsDepositsIdTxnHashPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsDepositsIdTxnHashPostRequest from a JSON string
api_v1_funds_deposits_id_txn_hash_post_request_instance = ApiV1FundsDepositsIdTxnHashPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsDepositsIdTxnHashPostRequest.to_json())

# convert the object into a dict
api_v1_funds_deposits_id_txn_hash_post_request_dict = api_v1_funds_deposits_id_txn_hash_post_request_instance.to_dict()
# create an instance of ApiV1FundsDepositsIdTxnHashPostRequest from a dict
api_v1_funds_deposits_id_txn_hash_post_request_from_dict = ApiV1FundsDepositsIdTxnHashPostRequest.from_dict(api_v1_funds_deposits_id_txn_hash_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



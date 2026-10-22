# ApiV1FundsDepositsIdTxnHashPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**txn_claim** | [**FundsTxnClaim**](FundsTxnClaim.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post200_response import ApiV1FundsDepositsIdTxnHashPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsDepositsIdTxnHashPost200Response from a JSON string
api_v1_funds_deposits_id_txn_hash_post200_response_instance = ApiV1FundsDepositsIdTxnHashPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsDepositsIdTxnHashPost200Response.to_json())

# convert the object into a dict
api_v1_funds_deposits_id_txn_hash_post200_response_dict = api_v1_funds_deposits_id_txn_hash_post200_response_instance.to_dict()
# create an instance of ApiV1FundsDepositsIdTxnHashPost200Response from a dict
api_v1_funds_deposits_id_txn_hash_post200_response_from_dict = ApiV1FundsDepositsIdTxnHashPost200Response.from_dict(api_v1_funds_deposits_id_txn_hash_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



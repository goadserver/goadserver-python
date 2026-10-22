# FundsDepositProof

The proof of payment uploaded on a bank / Wise deposit (download: GET /api/v1/funds/deposits/{id}/proof). Null / absent when none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**size** | **int** | Bytes. | [optional] 
**uploaded_at** | **int** | Unix time of the upload. | [optional] 

## Example

```python
from goadserver.models.funds_deposit_proof import FundsDepositProof

# TODO update the JSON string below
json = "{}"
# create an instance of FundsDepositProof from a JSON string
funds_deposit_proof_instance = FundsDepositProof.from_json(json)
# print the JSON string representation of the object
print(FundsDepositProof.to_json())

# convert the object into a dict
funds_deposit_proof_dict = funds_deposit_proof_instance.to_dict()
# create an instance of FundsDepositProof from a dict
funds_deposit_proof_from_dict = FundsDepositProof.from_dict(funds_deposit_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



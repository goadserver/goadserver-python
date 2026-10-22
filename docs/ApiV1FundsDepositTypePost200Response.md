# ApiV1FundsDepositTypePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fid** | **int** | Deposit id for GET /api/v1/funds/deposit/{type}/{fid}. | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_deposit_type_post200_response import ApiV1FundsDepositTypePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsDepositTypePost200Response from a JSON string
api_v1_funds_deposit_type_post200_response_instance = ApiV1FundsDepositTypePost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsDepositTypePost200Response.to_json())

# convert the object into a dict
api_v1_funds_deposit_type_post200_response_dict = api_v1_funds_deposit_type_post200_response_instance.to_dict()
# create an instance of ApiV1FundsDepositTypePost200Response from a dict
api_v1_funds_deposit_type_post200_response_from_dict = ApiV1FundsDepositTypePost200Response.from_dict(api_v1_funds_deposit_type_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



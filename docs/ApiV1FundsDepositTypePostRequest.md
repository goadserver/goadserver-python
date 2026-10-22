# ApiV1FundsDepositTypePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Deposit amount in currency units. Required for pay types and &#x60;advertiser&#x60;; not used for bonus / coupon. | [optional] 
**bonus** | **str** | Bonus code (type &#x60;bonus&#x60;). | [optional] 
**code** | **str** | Voucher code (type &#x60;coupon&#x60;). | [optional] 
**connected_users** | **int** | Target user id (type &#x60;advertiser&#x60;). | [optional] 
**whitebit_mode** | **str** | WhiteBit only (default crypto). | [optional] 
**whitebit_ticker** | **str** | WhiteBit only (default USDT). | [optional] 
**whitebit_network** | **str** | WhiteBit only (default TRC20). | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_deposit_type_post_request import ApiV1FundsDepositTypePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsDepositTypePostRequest from a JSON string
api_v1_funds_deposit_type_post_request_instance = ApiV1FundsDepositTypePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsDepositTypePostRequest.to_json())

# convert the object into a dict
api_v1_funds_deposit_type_post_request_dict = api_v1_funds_deposit_type_post_request_instance.to_dict()
# create an instance of ApiV1FundsDepositTypePostRequest from a dict
api_v1_funds_deposit_type_post_request_from_dict = ApiV1FundsDepositTypePostRequest.from_dict(api_v1_funds_deposit_type_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



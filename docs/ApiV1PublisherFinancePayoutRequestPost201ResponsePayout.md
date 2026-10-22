# ApiV1PublisherFinancePayoutRequestPost201ResponsePayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction id (see GET …/transactions/{id}). | [optional] 
**amount** | **int** | Deducted from the balance, cents. | [optional] 
**fee** | **int** | Method fee, cents. | [optional] 
**net_amount** | **int** | amount − fee, cents. | [optional] 
**paid_currency** | **str** |  | [optional] 
**ispayed** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payout_request_post201_response_payout import ApiV1PublisherFinancePayoutRequestPost201ResponsePayout

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutRequestPost201ResponsePayout from a JSON string
api_v1_publisher_finance_payout_request_post201_response_payout_instance = ApiV1PublisherFinancePayoutRequestPost201ResponsePayout.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutRequestPost201ResponsePayout.to_json())

# convert the object into a dict
api_v1_publisher_finance_payout_request_post201_response_payout_dict = api_v1_publisher_finance_payout_request_post201_response_payout_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutRequestPost201ResponsePayout from a dict
api_v1_publisher_finance_payout_request_post201_response_payout_from_dict = ApiV1PublisherFinancePayoutRequestPost201ResponsePayout.from_dict(api_v1_publisher_finance_payout_request_post201_response_payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



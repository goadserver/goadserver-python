# ApiV1PublisherFinancePayoutsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transactionid** | **int** | Per-account payout / invoice number. | [optional] 
**transacttype** | **int** | Payout method id; 0 &#x3D; transfer to advertiser budget. | [optional] 
**dateadded** | **date** |  | [optional] 
**money** | **int** | Amount, cents. | [optional] 
**ispayed** | **int** |  | [optional] 
**datepayed** | **str** |  | [optional] 
**isunpayable** | **int** | 1 &#x3D; staff marked the request as not payable (e.g. unvalidated payment details). | [optional] 
**txt** | **str** |  | [optional] 
**refund_note** | **str** |  | [optional] 
**paid_currency** | **str** |  | [optional] 
**companyid** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payouts_get200_response_data_inner import ApiV1PublisherFinancePayoutsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutsGet200ResponseDataInner from a JSON string
api_v1_publisher_finance_payouts_get200_response_data_inner_instance = ApiV1PublisherFinancePayoutsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_publisher_finance_payouts_get200_response_data_inner_dict = api_v1_publisher_finance_payouts_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutsGet200ResponseDataInner from a dict
api_v1_publisher_finance_payouts_get200_response_data_inner_from_dict = ApiV1PublisherFinancePayoutsGet200ResponseDataInner.from_dict(api_v1_publisher_finance_payouts_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



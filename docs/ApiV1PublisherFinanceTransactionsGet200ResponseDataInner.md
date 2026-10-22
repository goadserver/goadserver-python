# ApiV1PublisherFinanceTransactionsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transactionid** | **int** |  | [optional] 
**transacttype** | **int** |  | [optional] 
**dateadded** | **date** |  | [optional] 
**money** | **int** | Amount, cents. | [optional] 
**ispaid** | **int** |  | [optional] 
**datepaid** | **str** |  | [optional] 
**isunpayable** | **int** |  | [optional] 
**txt** | **str** |  | [optional] 
**refund_note** | **str** |  | [optional] 
**paid_currency** | **str** |  | [optional] 
**totalusd** | **float** | USD equivalent, cents (0 when not converted). | [optional] 
**usdrate** | **float** |  | [optional] 
**companyid** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_transactions_get200_response_data_inner import ApiV1PublisherFinanceTransactionsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceTransactionsGet200ResponseDataInner from a JSON string
api_v1_publisher_finance_transactions_get200_response_data_inner_instance = ApiV1PublisherFinanceTransactionsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceTransactionsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_publisher_finance_transactions_get200_response_data_inner_dict = api_v1_publisher_finance_transactions_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1PublisherFinanceTransactionsGet200ResponseDataInner from a dict
api_v1_publisher_finance_transactions_get200_response_data_inner_from_dict = ApiV1PublisherFinanceTransactionsGet200ResponseDataInner.from_dict(api_v1_publisher_finance_transactions_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



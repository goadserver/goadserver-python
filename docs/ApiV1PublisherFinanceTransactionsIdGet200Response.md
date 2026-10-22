# ApiV1PublisherFinanceTransactionsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transactionid** | **int** |  | [optional] 
**transacttype** | **int** |  | [optional] 
**dateadded** | **str** |  | [optional] 
**money** | **int** | Amount, cents. | [optional] 
**ispaid** | **int** |  | [optional] 
**datepaid** | **str** |  | [optional] 
**isunpayable** | **int** |  | [optional] 
**txt** | **str** |  | [optional] 
**refund_note** | **str** |  | [optional] 
**paid_currency** | **str** |  | [optional] 
**companyid** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_transactions_id_get200_response import ApiV1PublisherFinanceTransactionsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceTransactionsIdGet200Response from a JSON string
api_v1_publisher_finance_transactions_id_get200_response_instance = ApiV1PublisherFinanceTransactionsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceTransactionsIdGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_finance_transactions_id_get200_response_dict = api_v1_publisher_finance_transactions_id_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherFinanceTransactionsIdGet200Response from a dict
api_v1_publisher_finance_transactions_id_get200_response_from_dict = ApiV1PublisherFinanceTransactionsIdGet200Response.from_dict(api_v1_publisher_finance_transactions_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



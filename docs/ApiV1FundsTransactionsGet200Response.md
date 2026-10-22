# ApiV1FundsTransactionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1FundsTransactionsGet200ResponseDataInner]**](ApiV1FundsTransactionsGet200ResponseDataInner.md) |  | [optional] 
**meta** | [**ApiV1PublisherFinancePayoutsGet200ResponseMeta**](ApiV1PublisherFinancePayoutsGet200ResponseMeta.md) |  | [optional] 
**payment_methods** | [**List[ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner]**](ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_transactions_get200_response import ApiV1FundsTransactionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsTransactionsGet200Response from a JSON string
api_v1_funds_transactions_get200_response_instance = ApiV1FundsTransactionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsTransactionsGet200Response.to_json())

# convert the object into a dict
api_v1_funds_transactions_get200_response_dict = api_v1_funds_transactions_get200_response_instance.to_dict()
# create an instance of ApiV1FundsTransactionsGet200Response from a dict
api_v1_funds_transactions_get200_response_from_dict = ApiV1FundsTransactionsGet200Response.from_dict(api_v1_funds_transactions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



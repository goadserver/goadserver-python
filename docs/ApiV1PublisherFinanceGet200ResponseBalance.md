# ApiV1PublisherFinanceGet200ResponseBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **float** | Withdrawable balance, cents. | [optional] 
**pending** | **float** | Sum of payout requests not yet paid and not marked unpayable, cents. | [optional] 
**total_earned** | **float** | Sum of payouts already paid, cents. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_get200_response_balance import ApiV1PublisherFinanceGet200ResponseBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceGet200ResponseBalance from a JSON string
api_v1_publisher_finance_get200_response_balance_instance = ApiV1PublisherFinanceGet200ResponseBalance.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceGet200ResponseBalance.to_json())

# convert the object into a dict
api_v1_publisher_finance_get200_response_balance_dict = api_v1_publisher_finance_get200_response_balance_instance.to_dict()
# create an instance of ApiV1PublisherFinanceGet200ResponseBalance from a dict
api_v1_publisher_finance_get200_response_balance_from_dict = ApiV1PublisherFinanceGet200ResponseBalance.from_dict(api_v1_publisher_finance_get200_response_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



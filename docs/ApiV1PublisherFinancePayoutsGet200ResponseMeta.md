# ApiV1PublisherFinancePayoutsGet200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payouts_get200_response_meta import ApiV1PublisherFinancePayoutsGet200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutsGet200ResponseMeta from a JSON string
api_v1_publisher_finance_payouts_get200_response_meta_instance = ApiV1PublisherFinancePayoutsGet200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutsGet200ResponseMeta.to_json())

# convert the object into a dict
api_v1_publisher_finance_payouts_get200_response_meta_dict = api_v1_publisher_finance_payouts_get200_response_meta_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutsGet200ResponseMeta from a dict
api_v1_publisher_finance_payouts_get200_response_meta_from_dict = ApiV1PublisherFinancePayoutsGet200ResponseMeta.from_dict(api_v1_publisher_finance_payouts_get200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



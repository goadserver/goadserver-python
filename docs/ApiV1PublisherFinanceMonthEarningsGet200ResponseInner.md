# ApiV1PublisherFinanceMonthEarningsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**yearmonth** | **str** |  | [optional] 
**earned** | **float** | Publisher earnings, cents. | [optional] 
**pro_earned** | **float** | Referral / promotion earnings, cents. | [optional] 
**ad_earned** | **float** | Advertiser-side earnings credited here, cents. | [optional] 
**total_earned** | **float** | earned + pro_earned + ad_earned, cents. | [optional] 
**ispaid** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_month_earnings_get200_response_inner import ApiV1PublisherFinanceMonthEarningsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceMonthEarningsGet200ResponseInner from a JSON string
api_v1_publisher_finance_month_earnings_get200_response_inner_instance = ApiV1PublisherFinanceMonthEarningsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceMonthEarningsGet200ResponseInner.to_json())

# convert the object into a dict
api_v1_publisher_finance_month_earnings_get200_response_inner_dict = api_v1_publisher_finance_month_earnings_get200_response_inner_instance.to_dict()
# create an instance of ApiV1PublisherFinanceMonthEarningsGet200ResponseInner from a dict
api_v1_publisher_finance_month_earnings_get200_response_inner_from_dict = ApiV1PublisherFinanceMonthEarningsGet200ResponseInner.from_dict(api_v1_publisher_finance_month_earnings_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



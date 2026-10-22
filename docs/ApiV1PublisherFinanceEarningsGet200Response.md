# ApiV1PublisherFinanceEarningsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings** | [**List[ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner]**](ApiV1PublisherFinanceEarningsGet200ResponseEarningsInner.md) |  | [optional] 
**period** | [**ApiV1PublisherFinanceEarningsGet200ResponsePeriod**](ApiV1PublisherFinanceEarningsGet200ResponsePeriod.md) |  | [optional] 
**summary** | [**ApiV1PublisherFinanceEarningsGet200ResponseSummary**](ApiV1PublisherFinanceEarningsGet200ResponseSummary.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_earnings_get200_response import ApiV1PublisherFinanceEarningsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceEarningsGet200Response from a JSON string
api_v1_publisher_finance_earnings_get200_response_instance = ApiV1PublisherFinanceEarningsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceEarningsGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_finance_earnings_get200_response_dict = api_v1_publisher_finance_earnings_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherFinanceEarningsGet200Response from a dict
api_v1_publisher_finance_earnings_get200_response_from_dict = ApiV1PublisherFinanceEarningsGet200Response.from_dict(api_v1_publisher_finance_earnings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



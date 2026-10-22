# ApiV1PublisherFinancePayoutsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1PublisherFinancePayoutsGet200ResponseDataInner]**](ApiV1PublisherFinancePayoutsGet200ResponseDataInner.md) |  | [optional] 
**meta** | [**ApiV1PublisherFinancePayoutsGet200ResponseMeta**](ApiV1PublisherFinancePayoutsGet200ResponseMeta.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payouts_get200_response import ApiV1PublisherFinancePayoutsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutsGet200Response from a JSON string
api_v1_publisher_finance_payouts_get200_response_instance = ApiV1PublisherFinancePayoutsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutsGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_finance_payouts_get200_response_dict = api_v1_publisher_finance_payouts_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutsGet200Response from a dict
api_v1_publisher_finance_payouts_get200_response_from_dict = ApiV1PublisherFinancePayoutsGet200Response.from_dict(api_v1_publisher_finance_payouts_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



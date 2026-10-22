# ApiV1PublisherFinancePayoutRequestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Whole currency units. Required unless total_amount is true. | [optional] 
**total_amount** | **bool** | Request the full balance. | [optional] [default to False]
**description** | **str** | Note shown on the payout. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payout_request_post_request import ApiV1PublisherFinancePayoutRequestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutRequestPostRequest from a JSON string
api_v1_publisher_finance_payout_request_post_request_instance = ApiV1PublisherFinancePayoutRequestPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutRequestPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_finance_payout_request_post_request_dict = api_v1_publisher_finance_payout_request_post_request_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutRequestPostRequest from a dict
api_v1_publisher_finance_payout_request_post_request_from_dict = ApiV1PublisherFinancePayoutRequestPostRequest.from_dict(api_v1_publisher_finance_payout_request_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



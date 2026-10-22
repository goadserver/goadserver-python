# ApiV1PublisherFinancePayoutRequestPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**payout** | [**ApiV1PublisherFinancePayoutRequestPost201ResponsePayout**](ApiV1PublisherFinancePayoutRequestPost201ResponsePayout.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payout_request_post201_response import ApiV1PublisherFinancePayoutRequestPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutRequestPost201Response from a JSON string
api_v1_publisher_finance_payout_request_post201_response_instance = ApiV1PublisherFinancePayoutRequestPost201Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutRequestPost201Response.to_json())

# convert the object into a dict
api_v1_publisher_finance_payout_request_post201_response_dict = api_v1_publisher_finance_payout_request_post201_response_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutRequestPost201Response from a dict
api_v1_publisher_finance_payout_request_post201_response_from_dict = ApiV1PublisherFinancePayoutRequestPost201Response.from_dict(api_v1_publisher_finance_payout_request_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



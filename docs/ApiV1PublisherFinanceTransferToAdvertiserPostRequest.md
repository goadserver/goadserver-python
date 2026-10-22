# ApiV1PublisherFinanceTransferToAdvertiserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Whole currency units. Ignored when total_amount is true. | [optional] 
**total_amount** | **bool** | Move the full balance. | [optional] [default to False]
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_transfer_to_advertiser_post_request import ApiV1PublisherFinanceTransferToAdvertiserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceTransferToAdvertiserPostRequest from a JSON string
api_v1_publisher_finance_transfer_to_advertiser_post_request_instance = ApiV1PublisherFinanceTransferToAdvertiserPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceTransferToAdvertiserPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_finance_transfer_to_advertiser_post_request_dict = api_v1_publisher_finance_transfer_to_advertiser_post_request_instance.to_dict()
# create an instance of ApiV1PublisherFinanceTransferToAdvertiserPostRequest from a dict
api_v1_publisher_finance_transfer_to_advertiser_post_request_from_dict = ApiV1PublisherFinanceTransferToAdvertiserPostRequest.from_dict(api_v1_publisher_finance_transfer_to_advertiser_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



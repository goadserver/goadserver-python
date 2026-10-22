# ApiV1PublisherFinanceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**ApiV1PublisherFinanceGet200ResponseBalance**](ApiV1PublisherFinanceGet200ResponseBalance.md) |  | [optional] 
**payout_threshold** | **float** | Network minimum for a payout request, whole currency units. | [optional] 
**manual_payouts_only** | **bool** | Payouts are only made on request (no automatic payout runs). | [optional] 
**manual_admin_only** | **bool** | Only staff can create a payout; a publisher request is not offered in the panel. | [optional] 
**can_transfer_to_advertiser** | **bool** | True when the tenant offers the advertiser-budget method AND this account is an advertiser — i.e. &#x60;POST …/transfer-to-advertiser&#x60; will not answer 403 not_advertiser. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_get200_response import ApiV1PublisherFinanceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceGet200Response from a JSON string
api_v1_publisher_finance_get200_response_instance = ApiV1PublisherFinanceGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_finance_get200_response_dict = api_v1_publisher_finance_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherFinanceGet200Response from a dict
api_v1_publisher_finance_get200_response_from_dict = ApiV1PublisherFinanceGet200Response.from_dict(api_v1_publisher_finance_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



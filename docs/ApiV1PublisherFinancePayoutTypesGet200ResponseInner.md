# ApiV1PublisherFinancePayoutTypesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | Config key of the method, e.g. bank, paypal, usdt. | [optional] 
**min_payout** | **float** | Method minimum, whole currency units (0 &#x3D; only the network threshold applies). | [optional] 
**currencies** | **List[str]** |  | [optional] 
**custom_logo_url** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_payout_types_get200_response_inner import ApiV1PublisherFinancePayoutTypesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinancePayoutTypesGet200ResponseInner from a JSON string
api_v1_publisher_finance_payout_types_get200_response_inner_instance = ApiV1PublisherFinancePayoutTypesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinancePayoutTypesGet200ResponseInner.to_json())

# convert the object into a dict
api_v1_publisher_finance_payout_types_get200_response_inner_dict = api_v1_publisher_finance_payout_types_get200_response_inner_instance.to_dict()
# create an instance of ApiV1PublisherFinancePayoutTypesGet200ResponseInner from a dict
api_v1_publisher_finance_payout_types_get200_response_inner_from_dict = ApiV1PublisherFinancePayoutTypesGet200ResponseInner.from_dict(api_v1_publisher_finance_payout_types_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



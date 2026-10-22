# ApiV1FundsPayTypesGet200ResponsePayTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The &#x60;{type}&#x60; path value. | [optional] 
**id** | **str** | Same as key. | [optional] 
**name** | **str** |  | [optional] 
**paytype_id** | **int** | Numeric id stored on transactions (&#x60;paytype&#x60;). | [optional] 
**initiates_payment** | **bool** |  | [optional] 
**min_amount** | **float** | Minimum deposit in currency units. | [optional] 
**fee_terms** | **Dict[str, object]** | Transaction-cost terms used to preview the fee. | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_pay_types_get200_response_pay_types_inner import ApiV1FundsPayTypesGet200ResponsePayTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsPayTypesGet200ResponsePayTypesInner from a JSON string
api_v1_funds_pay_types_get200_response_pay_types_inner_instance = ApiV1FundsPayTypesGet200ResponsePayTypesInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsPayTypesGet200ResponsePayTypesInner.to_json())

# convert the object into a dict
api_v1_funds_pay_types_get200_response_pay_types_inner_dict = api_v1_funds_pay_types_get200_response_pay_types_inner_instance.to_dict()
# create an instance of ApiV1FundsPayTypesGet200ResponsePayTypesInner from a dict
api_v1_funds_pay_types_get200_response_pay_types_inner_from_dict = ApiV1FundsPayTypesGet200ResponsePayTypesInner.from_dict(api_v1_funds_pay_types_get200_response_pay_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



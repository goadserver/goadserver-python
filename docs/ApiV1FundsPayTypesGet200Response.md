# ApiV1FundsPayTypesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_types** | [**List[ApiV1FundsPayTypesGet200ResponsePayTypesInner]**](ApiV1FundsPayTypesGet200ResponsePayTypesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_pay_types_get200_response import ApiV1FundsPayTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsPayTypesGet200Response from a JSON string
api_v1_funds_pay_types_get200_response_instance = ApiV1FundsPayTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsPayTypesGet200Response.to_json())

# convert the object into a dict
api_v1_funds_pay_types_get200_response_dict = api_v1_funds_pay_types_get200_response_instance.to_dict()
# create an instance of ApiV1FundsPayTypesGet200Response from a dict
api_v1_funds_pay_types_get200_response_from_dict = ApiV1FundsPayTypesGet200Response.from_dict(api_v1_funds_pay_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



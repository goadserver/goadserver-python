# ApiV1FundsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**pending** | **float** |  | [optional] 
**pending_count** | **int** |  | [optional] 
**min_balance** | **float** |  | [optional] 
**low_balance** | **bool** |  | [optional] 
**last_deposit** | **datetime** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_get200_response import ApiV1FundsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsGet200Response from a JSON string
api_v1_funds_get200_response_instance = ApiV1FundsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsGet200Response.to_json())

# convert the object into a dict
api_v1_funds_get200_response_dict = api_v1_funds_get200_response_instance.to_dict()
# create an instance of ApiV1FundsGet200Response from a dict
api_v1_funds_get200_response_from_dict = ApiV1FundsGet200Response.from_dict(api_v1_funds_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



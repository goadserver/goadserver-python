# ApiV1AccountGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**system_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**api_key** | [**ApiV1AccountGet200ResponseApiKey**](ApiV1AccountGet200ResponseApiKey.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_account_get200_response import ApiV1AccountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountGet200Response from a JSON string
api_v1_account_get200_response_instance = ApiV1AccountGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountGet200Response.to_json())

# convert the object into a dict
api_v1_account_get200_response_dict = api_v1_account_get200_response_instance.to_dict()
# create an instance of ApiV1AccountGet200Response from a dict
api_v1_account_get200_response_from_dict = ApiV1AccountGet200Response.from_dict(api_v1_account_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



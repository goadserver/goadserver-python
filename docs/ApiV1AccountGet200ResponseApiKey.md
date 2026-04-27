# ApiV1AccountGet200ResponseApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**resource_filter** | [**ResourceFilter**](ResourceFilter.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_account_get200_response_api_key import ApiV1AccountGet200ResponseApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountGet200ResponseApiKey from a JSON string
api_v1_account_get200_response_api_key_instance = ApiV1AccountGet200ResponseApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountGet200ResponseApiKey.to_json())

# convert the object into a dict
api_v1_account_get200_response_api_key_dict = api_v1_account_get200_response_api_key_instance.to_dict()
# create an instance of ApiV1AccountGet200ResponseApiKey from a dict
api_v1_account_get200_response_api_key_from_dict = ApiV1AccountGet200ResponseApiKey.from_dict(api_v1_account_get200_response_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



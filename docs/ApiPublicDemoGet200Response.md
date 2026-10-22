# ApiPublicDemoGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiPublicDemoGet200ResponseDataInner]**](ApiPublicDemoGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_public_demo_get200_response import ApiPublicDemoGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPublicDemoGet200Response from a JSON string
api_public_demo_get200_response_instance = ApiPublicDemoGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiPublicDemoGet200Response.to_json())

# convert the object into a dict
api_public_demo_get200_response_dict = api_public_demo_get200_response_instance.to_dict()
# create an instance of ApiPublicDemoGet200Response from a dict
api_public_demo_get200_response_from_dict = ApiPublicDemoGet200Response.from_dict(api_public_demo_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



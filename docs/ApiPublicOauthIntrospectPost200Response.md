# ApiPublicOauthIntrospectPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**scope** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**exp** | **int** |  | [optional] 
**sub** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_public_oauth_introspect_post200_response import ApiPublicOauthIntrospectPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPublicOauthIntrospectPost200Response from a JSON string
api_public_oauth_introspect_post200_response_instance = ApiPublicOauthIntrospectPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiPublicOauthIntrospectPost200Response.to_json())

# convert the object into a dict
api_public_oauth_introspect_post200_response_dict = api_public_oauth_introspect_post200_response_instance.to_dict()
# create an instance of ApiPublicOauthIntrospectPost200Response from a dict
api_public_oauth_introspect_post200_response_from_dict = ApiPublicOauthIntrospectPost200Response.from_dict(api_public_oauth_introspect_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



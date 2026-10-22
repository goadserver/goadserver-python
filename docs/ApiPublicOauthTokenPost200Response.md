# ApiPublicOauthTokenPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | oat_…, valid 1 hour | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**refresh_token** | **str** | ort_…, single use, 30 days | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_public_oauth_token_post200_response import ApiPublicOauthTokenPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPublicOauthTokenPost200Response from a JSON string
api_public_oauth_token_post200_response_instance = ApiPublicOauthTokenPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiPublicOauthTokenPost200Response.to_json())

# convert the object into a dict
api_public_oauth_token_post200_response_dict = api_public_oauth_token_post200_response_instance.to_dict()
# create an instance of ApiPublicOauthTokenPost200Response from a dict
api_public_oauth_token_post200_response_from_dict = ApiPublicOauthTokenPost200Response.from_dict(api_public_oauth_token_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiPublicOfferwallIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**offers** | [**List[ApiPublicOfferwallIdGet200ResponseOffersInner]**](ApiPublicOfferwallIdGet200ResponseOffersInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_public_offerwall_id_get200_response import ApiPublicOfferwallIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPublicOfferwallIdGet200Response from a JSON string
api_public_offerwall_id_get200_response_instance = ApiPublicOfferwallIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiPublicOfferwallIdGet200Response.to_json())

# convert the object into a dict
api_public_offerwall_id_get200_response_dict = api_public_offerwall_id_get200_response_instance.to_dict()
# create an instance of ApiPublicOfferwallIdGet200Response from a dict
api_public_offerwall_id_get200_response_from_dict = ApiPublicOfferwallIdGet200Response.from_dict(api_public_offerwall_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



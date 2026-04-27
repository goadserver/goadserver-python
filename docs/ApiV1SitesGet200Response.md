# ApiV1SitesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1SitesGet200ResponseDataInner]**](ApiV1SitesGet200ResponseDataInner.md) |  | [optional] 
**total_rows** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_sites_get200_response import ApiV1SitesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SitesGet200Response from a JSON string
api_v1_sites_get200_response_instance = ApiV1SitesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1SitesGet200Response.to_json())

# convert the object into a dict
api_v1_sites_get200_response_dict = api_v1_sites_get200_response_instance.to_dict()
# create an instance of ApiV1SitesGet200Response from a dict
api_v1_sites_get200_response_from_dict = ApiV1SitesGet200Response.from_dict(api_v1_sites_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AdspacesAddMultiplePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siteid** | **int** | One of your sites. | 
**adzone_typeid** | **int** | Numeric type id (&#x60;id&#x60; in /api/v1/lookups/adspace-types). Default 2 (bannerads). | [optional] [default to 2]
**sizeid** | **int** | Banner size id (/api/v1/lookups/banner-sizes) — required for banner types. | [optional] [default to 0]
**items** | [**List[ApiV1CreativesIdNamePutRequest]**](ApiV1CreativesIdNamePutRequest.md) |  | 

## Example

```python
from goadserver.models.api_v1_adspaces_add_multiple_post_request import ApiV1AdspacesAddMultiplePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesAddMultiplePostRequest from a JSON string
api_v1_adspaces_add_multiple_post_request_instance = ApiV1AdspacesAddMultiplePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesAddMultiplePostRequest.to_json())

# convert the object into a dict
api_v1_adspaces_add_multiple_post_request_dict = api_v1_adspaces_add_multiple_post_request_instance.to_dict()
# create an instance of ApiV1AdspacesAddMultiplePostRequest from a dict
api_v1_adspaces_add_multiple_post_request_from_dict = ApiV1AdspacesAddMultiplePostRequest.from_dict(api_v1_adspaces_add_multiple_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1DomainsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Bare hostname, no protocol or path. | 
**type** | **str** |  | [optional] [default to 'ads']
**notes** | **str** |  | [optional] 
**skip_ssl** | **bool** |  | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_domains_post_request import ApiV1DomainsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DomainsPostRequest from a JSON string
api_v1_domains_post_request_instance = ApiV1DomainsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1DomainsPostRequest.to_json())

# convert the object into a dict
api_v1_domains_post_request_dict = api_v1_domains_post_request_instance.to_dict()
# create an instance of ApiV1DomainsPostRequest from a dict
api_v1_domains_post_request_from_dict = ApiV1DomainsPostRequest.from_dict(api_v1_domains_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



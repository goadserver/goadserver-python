# ApiV1AdspacesTemplatesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | **object** |  | 

## Example

```python
from goadserver.models.api_v1_adspaces_templates_post_request import ApiV1AdspacesTemplatesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesTemplatesPostRequest from a JSON string
api_v1_adspaces_templates_post_request_instance = ApiV1AdspacesTemplatesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesTemplatesPostRequest.to_json())

# convert the object into a dict
api_v1_adspaces_templates_post_request_dict = api_v1_adspaces_templates_post_request_instance.to_dict()
# create an instance of ApiV1AdspacesTemplatesPostRequest from a dict
api_v1_adspaces_templates_post_request_from_dict = ApiV1AdspacesTemplatesPostRequest.from_dict(api_v1_adspaces_templates_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



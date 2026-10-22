# ApiV1SitesSchemaGet200ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**default** | **object** |  | [optional] 
**example** | **object** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_sites_schema_get200_response_fields_inner import ApiV1SitesSchemaGet200ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SitesSchemaGet200ResponseFieldsInner from a JSON string
api_v1_sites_schema_get200_response_fields_inner_instance = ApiV1SitesSchemaGet200ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1SitesSchemaGet200ResponseFieldsInner.to_json())

# convert the object into a dict
api_v1_sites_schema_get200_response_fields_inner_dict = api_v1_sites_schema_get200_response_fields_inner_instance.to_dict()
# create an instance of ApiV1SitesSchemaGet200ResponseFieldsInner from a dict
api_v1_sites_schema_get200_response_fields_inner_from_dict = ApiV1SitesSchemaGet200ResponseFieldsInner.from_dict(api_v1_sites_schema_get200_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



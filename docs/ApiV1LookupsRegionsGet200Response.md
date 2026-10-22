# ApiV1LookupsRegionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**truncated** | **bool** | Present (true) only when the response was capped at the 2000-item limit. | [optional] 
**limit** | **int** | Cap value, only present when truncated&#x3D;true. | [optional] 
**note** | **str** |  | [optional] 
**regions** | [**List[ApiV1LookupsRegionsGet200ResponseRegionsInner]**](ApiV1LookupsRegionsGet200ResponseRegionsInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_lookups_regions_get200_response import ApiV1LookupsRegionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LookupsRegionsGet200Response from a JSON string
api_v1_lookups_regions_get200_response_instance = ApiV1LookupsRegionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1LookupsRegionsGet200Response.to_json())

# convert the object into a dict
api_v1_lookups_regions_get200_response_dict = api_v1_lookups_regions_get200_response_instance.to_dict()
# create an instance of ApiV1LookupsRegionsGet200Response from a dict
api_v1_lookups_regions_get200_response_from_dict = ApiV1LookupsRegionsGet200Response.from_dict(api_v1_lookups_regions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



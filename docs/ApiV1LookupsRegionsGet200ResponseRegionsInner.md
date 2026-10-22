# ApiV1LookupsRegionsGet200ResponseRegionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**level** | **int** | 0&#x3D;continent, 1&#x3D;country, 2&#x3D;state/province, 3&#x3D;sub-region, 4&#x3D;city. | [optional] 
**parent_id** | **int** |  | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 code of the country the region lies in; empty for continents. | [optional] 

## Example

```python
from goadserver.models.api_v1_lookups_regions_get200_response_regions_inner import ApiV1LookupsRegionsGet200ResponseRegionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LookupsRegionsGet200ResponseRegionsInner from a JSON string
api_v1_lookups_regions_get200_response_regions_inner_instance = ApiV1LookupsRegionsGet200ResponseRegionsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1LookupsRegionsGet200ResponseRegionsInner.to_json())

# convert the object into a dict
api_v1_lookups_regions_get200_response_regions_inner_dict = api_v1_lookups_regions_get200_response_regions_inner_instance.to_dict()
# create an instance of ApiV1LookupsRegionsGet200ResponseRegionsInner from a dict
api_v1_lookups_regions_get200_response_regions_inner_from_dict = ApiV1LookupsRegionsGet200ResponseRegionsInner.from_dict(api_v1_lookups_regions_get200_response_regions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



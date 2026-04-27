# ResourceFilter

Pin a key to specific resources. Empty/missing = no restriction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_ids** | **List[int]** |  | [optional] 
**adzone_ids** | **List[int]** |  | [optional] 
**site_ids** | **List[int]** |  | [optional] 
**creative_ids** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.resource_filter import ResourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceFilter from a JSON string
resource_filter_instance = ResourceFilter.from_json(json)
# print the JSON string representation of the object
print(ResourceFilter.to_json())

# convert the object into a dict
resource_filter_dict = resource_filter_instance.to_dict()
# create an instance of ResourceFilter from a dict
resource_filter_from_dict = ResourceFilter.from_dict(resource_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



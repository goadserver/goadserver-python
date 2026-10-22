# ResourceFilter

Pin a key to specific resources. Empty/missing = no restriction. A call naming a resource outside the pin answers `403 forbidden_resource`; lists only return pinned resources.  - `campaign_ids` — campaigns and everything under   `/campaigns/{type}/{id}/…`, including its ads (list, show, create,   update, delete, clone, uploads, bids). - `site_ids` — sites and the adspaces on them; an adspace can't be   moved to a site outside the pin, and no new site can be created. - `adzone_ids` — adspaces. - `creative_ids` — the creatives library (list, show, used-in,   delete, bulk-move) and the creatives linked into a pool. A key   pinned to creatives can't upload new ones. 

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



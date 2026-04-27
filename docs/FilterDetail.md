# FilterDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**ad_type** | **int** | 0 &#x3D; applies to all ad types, otherwise the adtypeid this filter targets. | [optional] 
**item_count** | **int** | Number of items (domains/ISPs/etc.) currently in the filter. | [optional] 
**items** | **List[str]** | Domain IDs / adzone IDs / ISP IDs / SubID strings — depends on filter type. | [optional] 
**campaign_ids** | **List[str]** | Campaigns this filter applies to. Empty &#x3D; applies to all campaigns. (Exclusion filters only.) | [optional] 
**ranges** | [**List[FilterDetailAllOfRanges]**](FilterDetailAllOfRanges.md) | IP CIDR ranges with their captured IP counts. (&#x60;type&#x3D;ip&#x60; only.) | [optional] 

## Example

```python
from goadserver.models.filter_detail import FilterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDetail from a JSON string
filter_detail_instance = FilterDetail.from_json(json)
# print the JSON string representation of the object
print(FilterDetail.to_json())

# convert the object into a dict
filter_detail_dict = filter_detail_instance.to_dict()
# create an instance of FilterDetail from a dict
filter_detail_from_dict = FilterDetail.from_dict(filter_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FilterSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**ad_type** | **int** | 0 &#x3D; applies to all ad types, otherwise the adtypeid this filter targets. | [optional] 
**item_count** | **int** | Number of items (domains/ISPs/etc.) currently in the filter. | [optional] 

## Example

```python
from goadserver.models.filter_summary import FilterSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FilterSummary from a JSON string
filter_summary_instance = FilterSummary.from_json(json)
# print the JSON string representation of the object
print(FilterSummary.to_json())

# convert the object into a dict
filter_summary_dict = filter_summary_instance.to_dict()
# create an instance of FilterSummary from a dict
filter_summary_from_dict = FilterSummary.from_dict(filter_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



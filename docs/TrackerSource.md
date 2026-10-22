# TrackerSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_slug** | **str** | Macro preset the source&#39;s click URLs are built from. | [optional] 
**adzone_count** | **int** | Tracking links hanging off this source. | [optional] 
**postbacks** | **Dict[str, object]** | Per-source outbound postback configuration. conversions.is_active&#x3D;false keeps the conversions.urls rows stored but nothing fires until it is set back to true. | [optional] 

## Example

```python
from goadserver.models.tracker_source import TrackerSource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerSource from a JSON string
tracker_source_instance = TrackerSource.from_json(json)
# print the JSON string representation of the object
print(TrackerSource.to_json())

# convert the object into a dict
tracker_source_dict = tracker_source_instance.to_dict()
# create an instance of TrackerSource from a dict
tracker_source_from_dict = TrackerSource.from_dict(tracker_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



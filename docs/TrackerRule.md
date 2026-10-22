# TrackerRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**apply_actions** | **bool** | false &#x3D; the rule evaluates and records, but never writes back. | [optional] 
**last_run_at** | **str** | Empty until the rule has fired once. | [optional] 

## Example

```python
from goadserver.models.tracker_rule import TrackerRule

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerRule from a JSON string
tracker_rule_instance = TrackerRule.from_json(json)
# print the JSON string representation of the object
print(TrackerRule.to_json())

# convert the object into a dict
tracker_rule_dict = tracker_rule_instance.to_dict()
# create an instance of TrackerRule from a dict
tracker_rule_from_dict = TrackerRule.from_dict(tracker_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



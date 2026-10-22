# PushSegment

A saved audience filter over the network's captured push subscribers. Delivery rules reference one to decide who an auctioned send reaches. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Segment label. | [optional] 
**source_spaceid** | **int** | Only subscribers captured on this pushads adzone. 0 &#x3D; any. | [optional] 
**domainid** | **int** | Only subscribers captured on this landing domain. 0 &#x3D; any. | [optional] 
**clickid_only** | **bool** | Only subscribers that carried a tracker clickid at opt-in. | [optional] 
**age_min_days** | **int** | Subscribed at least this many days ago. 0 &#x3D; no lower bound. | [optional] 
**age_max_days** | **int** | Subscribed at most this many days ago. 0 &#x3D; no upper bound. | [optional] 
**active_only** | **bool** | Exclude subscribers that have been deactivated. | [optional] 
**subscriber_count** | **int** | Live count of subscribers the segment matches right now. | [optional] 
**created_at** | **str** | YYYY-MM-DD HH:MM. | [optional] 

## Example

```python
from goadserver.models.push_segment import PushSegment

# TODO update the JSON string below
json = "{}"
# create an instance of PushSegment from a JSON string
push_segment_instance = PushSegment.from_json(json)
# print the JSON string representation of the object
print(PushSegment.to_json())

# convert the object into a dict
push_segment_dict = push_segment_instance.to_dict()
# create an instance of PushSegment from a dict
push_segment_from_dict = PushSegment.from_dict(push_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



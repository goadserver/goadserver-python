# PushSubscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**captured** | **str** | Opt-in timestamp, YYYY-MM-DD HH:MM. | [optional] 
**last_seen** | **str** | YYYY-MM-DD HH:MM. | [optional] 
**spaceid** | **int** | The pushads adzone that captured the opt-in. | [optional] 
**source_name** | **str** | Name of that adzone, empty when it no longer exists. | [optional] 
**clickid** | **str** | Tracker clickid carried at opt-in, when there was one. | [optional] 
**lang** | **str** | Browser language at opt-in. | [optional] 
**ip** | **str** | Masked to a /24 (IPv4) or /48 (IPv6) prefix — the raw address never leaves the database. | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.push_subscriber import PushSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of PushSubscriber from a JSON string
push_subscriber_instance = PushSubscriber.from_json(json)
# print the JSON string representation of the object
print(PushSubscriber.to_json())

# convert the object into a dict
push_subscriber_dict = push_subscriber_instance.to_dict()
# create an instance of PushSubscriber from a dict
push_subscriber_from_dict = PushSubscriber.from_dict(push_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



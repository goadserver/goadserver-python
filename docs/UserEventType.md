# UserEventType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**scope** | **str** | The scope a credential needs to receive it. | [optional] 
**role** | **str** |  | [optional] 
**opt_in** | **bool** | Produced only while a webhook subscribes to it (conversion.received). | [optional] 
**account_wide** | **bool** | Not delivered to keys pinned to campaigns. | [optional] 

## Example

```python
from goadserver.models.user_event_type import UserEventType

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventType from a JSON string
user_event_type_instance = UserEventType.from_json(json)
# print the JSON string representation of the object
print(UserEventType.to_json())

# convert the object into a dict
user_event_type_dict = user_event_type_instance.to_dict()
# create an instance of UserEventType from a dict
user_event_type_from_dict = UserEventType.from_dict(user_event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



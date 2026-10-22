# TrackerConversion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**datetime** | **str** |  | [optional] 
**clickid** | **str** | Pass to /conversions/{clickid}/postbacks for what was forwarded upstream. | [optional] 
**offer_id** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**link_name** | **str** |  | [optional] 
**payout** | **float** |  | [optional] 
**state** | **int** | Settlement state. | [optional] 
**status** | **str** | Human-readable form of state. | [optional] 
**reason_id** | **int** | Why the conversion is held or rejected. 0 when clean. | [optional] 
**reason** | **str** |  | [optional] 
**conv_type** | **int** |  | [optional] 
**conv_type_letter** | **str** | A–Z. | [optional] 
**conv_type_name** | **str** | The account&#39;s label for that letter — see /conversion-types. | [optional] 
**subid** | **str** |  | [optional] 
**ipaddress** | **str** |  | [optional] 

## Example

```python
from goadserver.models.tracker_conversion import TrackerConversion

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerConversion from a JSON string
tracker_conversion_instance = TrackerConversion.from_json(json)
# print the JSON string representation of the object
print(TrackerConversion.to_json())

# convert the object into a dict
tracker_conversion_dict = tracker_conversion_instance.to_dict()
# create an instance of TrackerConversion from a dict
tracker_conversion_from_dict = TrackerConversion.from_dict(tracker_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



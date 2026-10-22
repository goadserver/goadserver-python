# Error

Every non-2xx response. See \"Errors\" in the API description for the code list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Stable machine-readable code. | 
**message** | **str** | Human-readable; do not branch on it. | 
**errors** | **Dict[str, List[str]]** | Field → messages, on field-level validation failures. | [optional] 
**scope** | **str** |  | [optional] 
**unknown_fields** | **List[str]** |  | [optional] 
**current_etag** | **str** |  | [optional] 

## Example

```python
from goadserver.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



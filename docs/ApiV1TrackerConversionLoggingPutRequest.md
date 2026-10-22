# ApiV1TrackerConversionLoggingPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_conversions** | **bool** |  | [optional] 
**pend_conversions** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_conversion_logging_put_request import ApiV1TrackerConversionLoggingPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerConversionLoggingPutRequest from a JSON string
api_v1_tracker_conversion_logging_put_request_instance = ApiV1TrackerConversionLoggingPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerConversionLoggingPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_conversion_logging_put_request_dict = api_v1_tracker_conversion_logging_put_request_instance.to_dict()
# create an instance of ApiV1TrackerConversionLoggingPutRequest from a dict
api_v1_tracker_conversion_logging_put_request_from_dict = ApiV1TrackerConversionLoggingPutRequest.from_dict(api_v1_tracker_conversion_logging_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



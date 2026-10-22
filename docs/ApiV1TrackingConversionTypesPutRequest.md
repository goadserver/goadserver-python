# ApiV1TrackingConversionTypesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[ApiV1TrackingConversionTypesPutRequestTypesInner]**](ApiV1TrackingConversionTypesPutRequestTypesInner.md) |  | [optional] 
**skip_dedup** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracking_conversion_types_put_request import ApiV1TrackingConversionTypesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackingConversionTypesPutRequest from a JSON string
api_v1_tracking_conversion_types_put_request_instance = ApiV1TrackingConversionTypesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackingConversionTypesPutRequest.to_json())

# convert the object into a dict
api_v1_tracking_conversion_types_put_request_dict = api_v1_tracking_conversion_types_put_request_instance.to_dict()
# create an instance of ApiV1TrackingConversionTypesPutRequest from a dict
api_v1_tracking_conversion_types_put_request_from_dict = ApiV1TrackingConversionTypesPutRequest.from_dict(api_v1_tracking_conversion_types_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



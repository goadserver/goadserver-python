# ApiV1TrackingConversionTypesPut200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**conversion_types** | [**List[ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner]**](ApiV1TrackingConversionTypesPut200ResponseConversionTypesInner.md) |  | [optional] 
**skip_dedup** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracking_conversion_types_put200_response import ApiV1TrackingConversionTypesPut200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackingConversionTypesPut200Response from a JSON string
api_v1_tracking_conversion_types_put200_response_instance = ApiV1TrackingConversionTypesPut200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackingConversionTypesPut200Response.to_json())

# convert the object into a dict
api_v1_tracking_conversion_types_put200_response_dict = api_v1_tracking_conversion_types_put200_response_instance.to_dict()
# create an instance of ApiV1TrackingConversionTypesPut200Response from a dict
api_v1_tracking_conversion_types_put200_response_from_dict = ApiV1TrackingConversionTypesPut200Response.from_dict(api_v1_tracking_conversion_types_put200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



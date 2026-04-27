# ApiV1TrackingConversionTypesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_types** | **List[object]** |  | [optional] 
**addomain** | **str** |  | [optional] 
**tracking_var_name** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracking_conversion_types_get200_response import ApiV1TrackingConversionTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackingConversionTypesGet200Response from a JSON string
api_v1_tracking_conversion_types_get200_response_instance = ApiV1TrackingConversionTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackingConversionTypesGet200Response.to_json())

# convert the object into a dict
api_v1_tracking_conversion_types_get200_response_dict = api_v1_tracking_conversion_types_get200_response_instance.to_dict()
# create an instance of ApiV1TrackingConversionTypesGet200Response from a dict
api_v1_tracking_conversion_types_get200_response_from_dict = ApiV1TrackingConversionTypesGet200Response.from_dict(api_v1_tracking_conversion_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1TrackingPixelsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**conversion_type_id** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracking_pixels_id_put_request import ApiV1TrackingPixelsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackingPixelsIdPutRequest from a JSON string
api_v1_tracking_pixels_id_put_request_instance = ApiV1TrackingPixelsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackingPixelsIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracking_pixels_id_put_request_dict = api_v1_tracking_pixels_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackingPixelsIdPutRequest from a dict
api_v1_tracking_pixels_id_put_request_from_dict = ApiV1TrackingPixelsIdPutRequest.from_dict(api_v1_tracking_pixels_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



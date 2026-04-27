# ApiV1TrackingPixelsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**conversion_type_id** | **int** |  | 

## Example

```python
from goadserver.models.api_v1_tracking_pixels_post_request import ApiV1TrackingPixelsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackingPixelsPostRequest from a JSON string
api_v1_tracking_pixels_post_request_instance = ApiV1TrackingPixelsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackingPixelsPostRequest.to_json())

# convert the object into a dict
api_v1_tracking_pixels_post_request_dict = api_v1_tracking_pixels_post_request_instance.to_dict()
# create an instance of ApiV1TrackingPixelsPostRequest from a dict
api_v1_tracking_pixels_post_request_from_dict = ApiV1TrackingPixelsPostRequest.from_dict(api_v1_tracking_pixels_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



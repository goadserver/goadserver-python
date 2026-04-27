# TrackingPixel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**conversion_type_id** | **int** |  | [optional] 
**pixel_code** | **str** | Server-generated 32-char hex; embed in tracking URL. | [optional] 

## Example

```python
from goadserver.models.tracking_pixel import TrackingPixel

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingPixel from a JSON string
tracking_pixel_instance = TrackingPixel.from_json(json)
# print the JSON string representation of the object
print(TrackingPixel.to_json())

# convert the object into a dict
tracking_pixel_dict = tracking_pixel_instance.to_dict()
# create an instance of TrackingPixel from a dict
tracking_pixel_from_dict = TrackingPixel.from_dict(tracking_pixel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



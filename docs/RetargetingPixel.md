# RetargetingPixel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**visitors** | **int** | Captured visitor count from ClickHouse. | [optional] 

## Example

```python
from goadserver.models.retargeting_pixel import RetargetingPixel

# TODO update the JSON string below
json = "{}"
# create an instance of RetargetingPixel from a JSON string
retargeting_pixel_instance = RetargetingPixel.from_json(json)
# print the JSON string representation of the object
print(RetargetingPixel.to_json())

# convert the object into a dict
retargeting_pixel_dict = retargeting_pixel_instance.to_dict()
# create an instance of RetargetingPixel from a dict
retargeting_pixel_from_dict = RetargetingPixel.from_dict(retargeting_pixel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RetargetingPixel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**visitors** | **int** | Captured visitor count from ClickHouse. | [optional] 
**purge_days_after** | **int** | Remove a visitor from the list this many days after capture (panel field &#x60;rmdays&#x60;). 0 &#x3D; off. | [optional] 
**skip_days_after** | **int** | Stop targeting a visitor this many days after capture (panel field &#x60;skipdays&#x60;). 0 &#x3D; off. | [optional] 
**skip_before_hours** | **int** | Don&#39;t target a visitor until this many hours after capture (panel field &#x60;skiphours&#x60;). 0 &#x3D; off. | [optional] 
**skip_visits_after** | **int** | Stop targeting a visitor after this many visits (panel field &#x60;skipvisits&#x60;). 0 &#x3D; off. | [optional] 

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



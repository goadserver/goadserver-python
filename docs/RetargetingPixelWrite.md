# RetargetingPixelWrite

Retargeting list write body. Takes the panel's request keys (`rmdays`, `skipdays`, `skiphours`, `skipvisits`) or the stored names the reads return (`purge_days_after`, `skip_days_after`, `skip_before_hours`, `skip_visits_after`) — so a fetched record can be sent back unchanged. Both names of one window with different values is a 422. `id`, `is_active` and `visitors` are accepted and ignored. Windows are whole numbers >= 0 (0 = off). The name has HTML tags stripped and is 1–255 characters. Unknown keys are a 422. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**rmdays** | **int** |  | [optional] 
**skipdays** | **int** |  | [optional] 
**skiphours** | **int** |  | [optional] 
**skipvisits** | **int** |  | [optional] 
**purge_days_after** | **int** |  | [optional] 
**skip_days_after** | **int** |  | [optional] 
**skip_before_hours** | **int** |  | [optional] 
**skip_visits_after** | **int** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**is_active** | **bool** |  | [optional] [readonly] 
**visitors** | **int** |  | [optional] [readonly] 

## Example

```python
from goadserver.models.retargeting_pixel_write import RetargetingPixelWrite

# TODO update the JSON string below
json = "{}"
# create an instance of RetargetingPixelWrite from a JSON string
retargeting_pixel_write_instance = RetargetingPixelWrite.from_json(json)
# print the JSON string representation of the object
print(RetargetingPixelWrite.to_json())

# convert the object into a dict
retargeting_pixel_write_dict = retargeting_pixel_write_instance.to_dict()
# create an instance of RetargetingPixelWrite from a dict
retargeting_pixel_write_from_dict = RetargetingPixelWrite.from_dict(retargeting_pixel_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



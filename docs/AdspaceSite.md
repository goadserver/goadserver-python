# AdspaceSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from goadserver.models.adspace_site import AdspaceSite

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceSite from a JSON string
adspace_site_instance = AdspaceSite.from_json(json)
# print the JSON string representation of the object
print(AdspaceSite.to_json())

# convert the object into a dict
adspace_site_dict = adspace_site_instance.to_dict()
# create an instance of AdspaceSite from a dict
adspace_site_from_dict = AdspaceSite.from_dict(adspace_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



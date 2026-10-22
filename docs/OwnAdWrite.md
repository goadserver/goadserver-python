# OwnAdWrite

An adzone's own (house) ad. On multipart uploads the same fields go as form fields next to the image file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Required on create. | [optional] 
**bannertype** | **int** | Creative kind as in the panel&#39;s Own ads form (image / HTML code / text). | [optional] 
**bannerurl** | **str** | Image or landing URL, per bannertype. | [optional] 
**bannercode** | **str** | HTML/JS code for code-type ads. | [optional] 
**weight** | **int** | Rotation weight among the zone&#39;s own ads. | [optional] 
**isactive** | **int** |  | [optional] 
**countries** | **str** | Comma-separated country codes; empty &#x3D; all. | [optional] 
**layerformat** | **str** |  | [optional] 
**bigimageurl** | **str** |  | [optional] 
**smallimageurl** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**displayurl** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.own_ad_write import OwnAdWrite

# TODO update the JSON string below
json = "{}"
# create an instance of OwnAdWrite from a JSON string
own_ad_write_instance = OwnAdWrite.from_json(json)
# print the JSON string representation of the object
print(OwnAdWrite.to_json())

# convert the object into a dict
own_ad_write_dict = own_ad_write_instance.to_dict()
# create an instance of OwnAdWrite from a dict
own_ad_write_from_dict = OwnAdWrite.from_dict(own_ad_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



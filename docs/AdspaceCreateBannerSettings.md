# AdspaceCreateBannerSettings

Banner-flavored zones (bannerads, fixim_banner, impopup, interstitialads, interstitial_banner, invideo_banner). bannerads inline (display_type 0) also takes `interscroller` (boolean): the banner shows fixed behind a window in the content that the page scrolls over, and GET /api/v1/adspaces/{id}/code switches to goCtrl's interscroller plugin; a non-boolean is refused with 422 `banner_settings.interscroller`. `inimage` (boolean): in-image ads — the banner shows in a closeable strip over the bottom of the publisher's own article images (goCtrl inimage plugin; fn_params container, min_width 400, max_images 3, label), each requested when its image scrolls into view with the image's alt text as keywords; interscroller and inimage together are refused with 422 `banner_settings.inimage`. Full field list: GET /api/v1/adspaces/bannerads/_schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sizeid** | **int** | Banner size id from /api/v1/lookups/banner-sizes. | [optional] 
**displaytype** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 

## Example

```python
from goadserver.models.adspace_create_banner_settings import AdspaceCreateBannerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreateBannerSettings from a JSON string
adspace_create_banner_settings_instance = AdspaceCreateBannerSettings.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreateBannerSettings.to_json())

# convert the object into a dict
adspace_create_banner_settings_dict = adspace_create_banner_settings_instance.to_dict()
# create an instance of AdspaceCreateBannerSettings from a dict
adspace_create_banner_settings_from_dict = AdspaceCreateBannerSettings.from_dict(adspace_create_banner_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



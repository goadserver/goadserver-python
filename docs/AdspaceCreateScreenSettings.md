# AdspaceCreateScreenSettings

DOOH screens (screens, adzone type 45): a digital-signage screen. The zone also needs its banner size (adsizeid / banner_settings.sizeid, e.g. 1920x1080). The screen's player pulls a playlist: GET https://<ad domain>/screen.go?spaceid=<zone>&key=<screen_key>[&n=1-20][&format=vast] → {screen:{spaceid, width, height, orientation, venue_type}, open, refresh_seconds, ads:[{id, type: image|video|iframe|html, url, html, width, height, duration, title, proof_url}]} (format=vast: VAST 4 with one Ad per item in play order, Impression = proof_url; iframe/html items are left out). Fire proof_url when an ad has really played — proof of play, counted once per play and only within 3 hours of the pull; it books one impression whose cost is the CPM bid × audience_per_play. Outside opening_hours the playlist is empty (open: false). act=player&spaceid=&key= is a ready full-screen web player for any browser in kiosk mode. Screens play only banner campaigns with options.screens.on (campaign field `screens`). screen_key is generated on create and returned read-only (also in GET /adspaces/{id}/code → screen); rotate_key: true issues a new one. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venue_type** | **str** | Where the screen hangs; campaigns can target venue types. Anything else is 422 &#x60;screen_settings.venue_type&#x60;. | [optional] [default to 'other']
**lat** | **float** | Latitude, for campaign geo-fences (out of range 422). | [optional] [default to 0]
**lon** | **float** | Longitude (out of range 422). | [optional] [default to 0]
**address** | **str** | For your own reference; plain text. | [optional] [default to '']
**width** | **int** | Screen width in px (clamped). | [optional] [default to 1920]
**height** | **int** | Screen height in px (clamped). | [optional] [default to 1080]
**orientation** | **str** |  | [optional] [default to 'landscape']
**audience_per_play** | **float** | People who see one play (clamped). A proof of play costs the CPM bid × this. | [optional] [default to 1]
**opening_hours** | **str** | Daily on-air window HH:MM-HH:MM in &#x60;timezone&#x60; (22:00-06:00 spans midnight); empty &#x3D; always. Malformed 422 &#x60;screen_settings.opening_hours&#x60;. | [optional] [default to '']
**timezone** | **str** | IANA time zone for opening_hours; empty &#x3D; the ad server&#39;s. Unknown 422. | [optional] [default to '']
**slot_seconds** | **int** | Seconds an image ad stays on screen (clamped); a video plays to its end. | [optional] [default to 10]
**playlist_size** | **int** | Ads per pull (clamped). | [optional] [default to 6]
**screen_key** | **str** | The key the player sends. Ignored on write. | [optional] [readonly] 
**rotate_key** | **bool** | true issues a new screen_key (the current player stops). | [optional] 

## Example

```python
from goadserver.models.adspace_create_screen_settings import AdspaceCreateScreenSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreateScreenSettings from a JSON string
adspace_create_screen_settings_instance = AdspaceCreateScreenSettings.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreateScreenSettings.to_json())

# convert the object into a dict
adspace_create_screen_settings_dict = adspace_create_screen_settings_instance.to_dict()
# create an instance of AdspaceCreateScreenSettings from a dict
adspace_create_screen_settings_from_dict = AdspaceCreateScreenSettings.from_dict(adspace_create_screen_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



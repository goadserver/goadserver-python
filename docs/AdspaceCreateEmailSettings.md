# AdspaceCreateEmailSettings

Email display zones (email_display, adzone type 44): image banners in a newsletter, picked when the email is opened. The zone also needs its banner size (adsizeid / banner_settings.sizeid). The code (GET /adspaces/{id}/code → ad_tag) is HTML for the newsletter template: per slot a linked image, https://<ad domain>/mailad.go?spaceid=<zone>&slot=<n>&rid=<merge tag>&act=img inside a link with act=click. The first image fetch per (zone, slot, recipient) picks a banner (image creatives only: html, iframe and video banners are skipped), counts the impression and keeps the choice for ttl_days; a re-open gets the same creative uncounted and the link goes to the ad that was shown. A click with no kept choice (images off) picks an ad then. No ad: the image is a transparent pixel, the link goes to fallback_link (or answers 204). Image proxies (Gmail, Apple Mail Privacy Protection) fetch from their own network: geo targeting sees the proxy, and Apple prefetches. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | **int** | Ad slots in the newsletter, each its own image + link (clamped). | [optional] [default to 1]
**merge_tag** | **str** | Your email tool&#39;s per-recipient merge tag, written into the code as rid. Use a recipient id, not the address. No spaces, quotes, &lt; &gt; or &amp;; anything else falls back to the default. | [optional] [default to '{{email_id}}']
**label** | **str** | Disclosure above each slot and the image alt text; plain text (empty &#x3D; the default). | [optional] [default to 'Advertisement']
**ttl_days** | **int** | Days the ad picked for a recipient&#39;s open is kept (clamped). | [optional] [default to 7]
**fallback_link** | **str** | http(s) URL a click goes to when no ad can be picked; anything else is stored empty. | [optional] [default to '']

## Example

```python
from goadserver.models.adspace_create_email_settings import AdspaceCreateEmailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreateEmailSettings from a JSON string
adspace_create_email_settings_instance = AdspaceCreateEmailSettings.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreateEmailSettings.to_json())

# convert the object into a dict
adspace_create_email_settings_dict = adspace_create_email_settings_instance.to_dict()
# create an instance of AdspaceCreateEmailSettings from a dict
adspace_create_email_settings_from_dict = AdspaceCreateEmailSettings.from_dict(adspace_create_email_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



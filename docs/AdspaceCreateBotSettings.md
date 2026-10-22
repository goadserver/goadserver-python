# AdspaceCreateBotSettings

Messenger / bot zones (bot_ads, adzone type 46): native ads a Telegram, Discord or WhatsApp bot posts as a sponsored message. Image orientation in native_settings. Server to server: GET https://<ad domain>/botad.go?spaceid=<zone>&chat=<chat id>[&q=<topic or last message>][&n=1-3][&subid=][&ip=<user ip>&agent=<user agent>] → {ads:[{title, description, text, url, button_text, display_url, image, impression_url}], label}. Post text (title + description) with a button button_text → url (the tracked click) and fire impression_url when the message is sent. A chat over cap_per_hour gets {ads:[], label, reason: \"capped\", retry_after: <seconds>}. q is matched against campaign keyword targeting; subid goes to the stats (don't send the chat id there). Messengers don't give bots the user's IP, so without ip geo targeting sees the bot's server. The code (GET /adspaces/{id}/code) returns the request URL as `alternative` and Python / Node examples as `ad_tag`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap_per_hour** | **int** | Ads per chat per hour; 0 &#x3D; no cap (clamped). | [optional] [default to 1]
**label** | **str** | Disclosure returned with every answer for the bot to show; plain text. | [optional] [default to 'Sponsored']
**button_text** | **str** | Text of the button that opens the ad; plain text. | [optional] [default to 'Open']

## Example

```python
from goadserver.models.adspace_create_bot_settings import AdspaceCreateBotSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreateBotSettings from a JSON string
adspace_create_bot_settings_instance = AdspaceCreateBotSettings.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreateBotSettings.to_json())

# convert the object into a dict
adspace_create_bot_settings_dict = adspace_create_bot_settings_instance.to_dict()
# create an instance of AdspaceCreateBotSettings from a dict
adspace_create_bot_settings_from_dict = AdspaceCreateBotSettings.from_dict(adspace_create_bot_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



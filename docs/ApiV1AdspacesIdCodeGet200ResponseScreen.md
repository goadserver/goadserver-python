# ApiV1AdspacesIdCodeGet200ResponseScreen

Screen zones (45): the web player, the playlist (JSON / VAST) and the screen key the player sends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **str** | Full-screen web player — open it in a kiosk browser on the screen. | [optional] 
**playlist** | **str** | GET → playlist JSON (see screen_settings). | [optional] 
**vast** | **str** | The playlist as VAST 4. | [optional] 
**screen_key** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_code_get200_response_screen import ApiV1AdspacesIdCodeGet200ResponseScreen

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdCodeGet200ResponseScreen from a JSON string
api_v1_adspaces_id_code_get200_response_screen_instance = ApiV1AdspacesIdCodeGet200ResponseScreen.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdCodeGet200ResponseScreen.to_json())

# convert the object into a dict
api_v1_adspaces_id_code_get200_response_screen_dict = api_v1_adspaces_id_code_get200_response_screen_instance.to_dict()
# create an instance of ApiV1AdspacesIdCodeGet200ResponseScreen from a dict
api_v1_adspaces_id_code_get200_response_screen_from_dict = ApiV1AdspacesIdCodeGet200ResponseScreen.from_dict(api_v1_adspaces_id_code_get200_response_screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



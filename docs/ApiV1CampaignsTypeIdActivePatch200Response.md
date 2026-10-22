# ApiV1CampaignsTypeIdActivePatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**pending_state** | **int** | Only when &#x60;changed&#x60; is true. 0 &#x3D; applied. 1 (pause) or 3 (resume) &#x3D; the network validates campaign changes, so the toggle also went to an admin as Pending Pause / Pending Active; the admin keeps it or reverts it. An admin acting on the user&#39;s behalf never pends (0) and settles a pause / resume the user still has waiting. RON only. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdActivePatch200Response from a JSON string
api_v1_campaigns_type_id_active_patch200_response_instance = ApiV1CampaignsTypeIdActivePatch200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdActivePatch200Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_active_patch200_response_dict = api_v1_campaigns_type_id_active_patch200_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdActivePatch200Response from a dict
api_v1_campaigns_type_id_active_patch200_response_from_dict = ApiV1CampaignsTypeIdActivePatch200Response.from_dict(api_v1_campaigns_type_id_active_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



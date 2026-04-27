# ApiV1CampaignsTypeIdClonePost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The cloned campaign&#39;s id. | [optional] 
**cloned_from** | **int** | The source campaign&#39;s id. | [optional] 
**is_active** | **bool** | Always false — the clone lands paused. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response import ApiV1CampaignsTypeIdClonePost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdClonePost201Response from a JSON string
api_v1_campaigns_type_id_clone_post201_response_instance = ApiV1CampaignsTypeIdClonePost201Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdClonePost201Response.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_clone_post201_response_dict = api_v1_campaigns_type_id_clone_post201_response_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdClonePost201Response from a dict
api_v1_campaigns_type_id_clone_post201_response_from_dict = ApiV1CampaignsTypeIdClonePost201Response.from_dict(api_v1_campaigns_type_id_clone_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



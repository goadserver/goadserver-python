# ApiV1CampaignsTypeIdClonePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Override the cloned campaign&#39;s name. Defaults to \&quot;&lt;original&gt; Copy\&quot;. | [optional] 

## Example

```python
from goadserver.models.api_v1_campaigns_type_id_clone_post_request import ApiV1CampaignsTypeIdClonePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypeIdClonePostRequest from a JSON string
api_v1_campaigns_type_id_clone_post_request_instance = ApiV1CampaignsTypeIdClonePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypeIdClonePostRequest.to_json())

# convert the object into a dict
api_v1_campaigns_type_id_clone_post_request_dict = api_v1_campaigns_type_id_clone_post_request_instance.to_dict()
# create an instance of ApiV1CampaignsTypeIdClonePostRequest from a dict
api_v1_campaigns_type_id_clone_post_request_from_dict = ApiV1CampaignsTypeIdClonePostRequest.from_dict(api_v1_campaigns_type_id_clone_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



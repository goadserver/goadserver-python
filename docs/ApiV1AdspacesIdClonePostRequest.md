# ApiV1AdspacesIdClonePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**copy_campaigns** | **bool** | Whitelisted campaigns + weights. | [optional] [default to False]
**copy_own_ads** | **bool** | The zone&#39;s own (house) ads. | [optional] [default to False]
**copy_settings** | **bool** | Costs, fixed payouts, subid and domain lists. | [optional] [default to False]
**start_active** | **bool** | Sets isvisible on the copy. | [optional] [default to False]
**copy_buying_policy** | **bool** | Media-buying policy (buying zones only). | [optional] [default to False]
**inherit_blocks** | **str** | Carry blocked placements to the copy&#39;s own network campaign on its first connection. | [optional] [default to '']

## Example

```python
from goadserver.models.api_v1_adspaces_id_clone_post_request import ApiV1AdspacesIdClonePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdClonePostRequest from a JSON string
api_v1_adspaces_id_clone_post_request_instance = ApiV1AdspacesIdClonePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdClonePostRequest.to_json())

# convert the object into a dict
api_v1_adspaces_id_clone_post_request_dict = api_v1_adspaces_id_clone_post_request_instance.to_dict()
# create an instance of ApiV1AdspacesIdClonePostRequest from a dict
api_v1_adspaces_id_clone_post_request_from_dict = ApiV1AdspacesIdClonePostRequest.from_dict(api_v1_adspaces_id_clone_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



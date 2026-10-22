# AdspaceNetworkBinding

External network binding (PUT /api/v1/adspaces/{id}/network-binding). adnetwork_id 0 = not bound.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adnetwork_id** | **int** |  | [optional] 
**adnetwork_campaignid** | **int** |  | [optional] 
**adnetwork_campaign_kind** | **str** |  | [optional] 
**auto_api** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.adspace_network_binding import AdspaceNetworkBinding

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceNetworkBinding from a JSON string
adspace_network_binding_instance = AdspaceNetworkBinding.from_json(json)
# print the JSON string representation of the object
print(AdspaceNetworkBinding.to_json())

# convert the object into a dict
adspace_network_binding_dict = adspace_network_binding_instance.to_dict()
# create an instance of AdspaceNetworkBinding from a dict
adspace_network_binding_from_dict = AdspaceNetworkBinding.from_dict(adspace_network_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



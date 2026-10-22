# ApiV1AdspacesIdNetworkBindingPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adnetwork_id** | **int** | One of your ad networks. | 
**adnetwork_campaignid** | **int** | Campaign id on that network. | 
**adnetwork_campaign_kind** | **str** | Only for a goadserver-type network (e.g. &#x60;ron&#x60;). | [optional] 
**auto_api** | **bool** | Pause/activate the network campaign via its API (otherwise report-only). | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_adspaces_id_network_binding_put_request import ApiV1AdspacesIdNetworkBindingPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdNetworkBindingPutRequest from a JSON string
api_v1_adspaces_id_network_binding_put_request_instance = ApiV1AdspacesIdNetworkBindingPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdNetworkBindingPutRequest.to_json())

# convert the object into a dict
api_v1_adspaces_id_network_binding_put_request_dict = api_v1_adspaces_id_network_binding_put_request_instance.to_dict()
# create an instance of ApiV1AdspacesIdNetworkBindingPutRequest from a dict
api_v1_adspaces_id_network_binding_put_request_from_dict = ApiV1AdspacesIdNetworkBindingPutRequest.from_dict(api_v1_adspaces_id_network_binding_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



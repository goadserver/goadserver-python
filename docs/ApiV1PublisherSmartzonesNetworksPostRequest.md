# ApiV1PublisherSmartzonesNetworksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Omit or 0 to create. | [optional] 
**name** | **str** |  | 
**prepend_name** | **str** |  | [optional] 
**networkid** | **int** | Catalogue network id (&#x60;available_networks[].id&#x60;). | [optional] 
**currency** | **str** | Currency the network reports earnings in. | [optional] [default to 'USD']
**is_active** | **int** |  | [optional] 
**pullstats** | **int** | Pull earnings from the network&#39;s API. | [optional] 
**apikey** | **str** |  | [optional] 
**api_data** | **object** | Network credentials, e.g. &#x60;userid&#x60;, &#x60;username&#x60;, &#x60;userpass&#x60;, &#x60;client_id&#x60;, &#x60;client_secret&#x60;, per the network&#39;s flags. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_smartzones_networks_post_request import ApiV1PublisherSmartzonesNetworksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSmartzonesNetworksPostRequest from a JSON string
api_v1_publisher_smartzones_networks_post_request_instance = ApiV1PublisherSmartzonesNetworksPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSmartzonesNetworksPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_smartzones_networks_post_request_dict = api_v1_publisher_smartzones_networks_post_request_instance.to_dict()
# create an instance of ApiV1PublisherSmartzonesNetworksPostRequest from a dict
api_v1_publisher_smartzones_networks_post_request_from_dict = ApiV1PublisherSmartzonesNetworksPostRequest.from_dict(api_v1_publisher_smartzones_networks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



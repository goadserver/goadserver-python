# ApiV1PublisherSmartzonesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**spaceid** | **int** |  | [optional] 
**smart_networkid** | **int** |  | [optional] 
**siteid** | **int** | Ignored unless &#x60;spaceid&#x60; is sent — then derived from it. | [optional] 
**countries** | **str** |  | [optional] 
**device_type_ids** | **str** |  | [optional] 
**is_active** | [**ApiV1PublisherSmartzonesIdPutRequestIsActive**](ApiV1PublisherSmartzonesIdPutRequestIsActive.md) |  | [optional] 
**select_type** | **int** | 0 &#x3D; percentage, 1 &#x3D; eCPM, 2 &#x3D; RTB, 3 &#x3D; eCPM + limit %. A numeric string is accepted too. | [optional] 
**select_pct** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**creative** | **str** | JSON-encoded string | [optional] 
**settings** | **str** | JSON-encoded string | [optional] 
**use_adblock** | **int** |  | [optional] 
**unique_only** | [**ApiV1PublisherSmartzonesIdPutRequestUniqueOnly**](ApiV1PublisherSmartzonesIdPutRequestUniqueOnly.md) |  | [optional] 
**network_zoneid** | **int** |  | [optional] 
**network_siteid** | **int** |  | [optional] 
**ssp_campaignid** | **int** |  | [optional] 
**scanning_enabled** | [**ApiV1PublisherSmartzonesIdPutRequestIsActive**](ApiV1PublisherSmartzonesIdPutRequestIsActive.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_smartzones_id_put_request import ApiV1PublisherSmartzonesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSmartzonesIdPutRequest from a JSON string
api_v1_publisher_smartzones_id_put_request_instance = ApiV1PublisherSmartzonesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSmartzonesIdPutRequest.to_json())

# convert the object into a dict
api_v1_publisher_smartzones_id_put_request_dict = api_v1_publisher_smartzones_id_put_request_instance.to_dict()
# create an instance of ApiV1PublisherSmartzonesIdPutRequest from a dict
api_v1_publisher_smartzones_id_put_request_from_dict = ApiV1PublisherSmartzonesIdPutRequest.from_dict(api_v1_publisher_smartzones_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



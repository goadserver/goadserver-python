# ApiV1PublisherSmartzonesImportPostRequestZonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spaceid** | **int** |  | 
**name** | **str** |  | [optional] 
**zoneid** | **str** | Zone id on the network. | [optional] 
**url** | **str** | The network&#39;s tag URL (VAST XML for video ad zones). | 
**network_siteid** | **int** |  | [optional] 
**device_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_smartzones_import_post_request_zones_inner import ApiV1PublisherSmartzonesImportPostRequestZonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSmartzonesImportPostRequestZonesInner from a JSON string
api_v1_publisher_smartzones_import_post_request_zones_inner_instance = ApiV1PublisherSmartzonesImportPostRequestZonesInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSmartzonesImportPostRequestZonesInner.to_json())

# convert the object into a dict
api_v1_publisher_smartzones_import_post_request_zones_inner_dict = api_v1_publisher_smartzones_import_post_request_zones_inner_instance.to_dict()
# create an instance of ApiV1PublisherSmartzonesImportPostRequestZonesInner from a dict
api_v1_publisher_smartzones_import_post_request_zones_inner_from_dict = ApiV1PublisherSmartzonesImportPostRequestZonesInner.from_dict(api_v1_publisher_smartzones_import_post_request_zones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



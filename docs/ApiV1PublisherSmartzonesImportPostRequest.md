# ApiV1PublisherSmartzonesImportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smart_network_id** | **int** | Your network account id. | 
**network_id** | **int** | Catalogue network id stored as the zones&#39; &#x60;networkid&#x60;. | [optional] 
**network_siteid** | **str** | Site id on the network | [optional] 
**siteid** | **int** | Ignored — each zone takes its ad zone&#39;s site. | [optional] 
**select_type** | **int** |  | [optional] 
**select_pct** | **int** |  | [optional] [default to 100]
**settings** | **object** | Zone settings object applied to every zone (stored as JSON), e.g. &#x60;{\&quot;skip_when_stats\&quot;: 1}&#x60;. | [optional] 
**zones** | [**List[ApiV1PublisherSmartzonesImportPostRequestZonesInner]**](ApiV1PublisherSmartzonesImportPostRequestZonesInner.md) |  | 

## Example

```python
from goadserver.models.api_v1_publisher_smartzones_import_post_request import ApiV1PublisherSmartzonesImportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSmartzonesImportPostRequest from a JSON string
api_v1_publisher_smartzones_import_post_request_instance = ApiV1PublisherSmartzonesImportPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSmartzonesImportPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_smartzones_import_post_request_dict = api_v1_publisher_smartzones_import_post_request_instance.to_dict()
# create an instance of ApiV1PublisherSmartzonesImportPostRequest from a dict
api_v1_publisher_smartzones_import_post_request_from_dict = ApiV1PublisherSmartzonesImportPostRequest.from_dict(api_v1_publisher_smartzones_import_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



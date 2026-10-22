# ApiV1UrlPoolsIdUrlsUrlIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**properties** | **str** |  | [optional] 
**keywords** | **str** | Comma-separated targeting keywords; empty &#x3D; a keyword fallback URL (serves when no targeted URL matches). | [optional] 
**is_fallback** | **bool** | Backup: used only while no other URL of the pool is live (\&quot;Backup\&quot; in the panel). | [optional] 
**start_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt.md) |  | [optional] 
**end_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_url_pools_id_urls_url_id_put_request import ApiV1UrlPoolsIdUrlsUrlIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UrlPoolsIdUrlsUrlIdPutRequest from a JSON string
api_v1_url_pools_id_urls_url_id_put_request_instance = ApiV1UrlPoolsIdUrlsUrlIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1UrlPoolsIdUrlsUrlIdPutRequest.to_json())

# convert the object into a dict
api_v1_url_pools_id_urls_url_id_put_request_dict = api_v1_url_pools_id_urls_url_id_put_request_instance.to_dict()
# create an instance of ApiV1UrlPoolsIdUrlsUrlIdPutRequest from a dict
api_v1_url_pools_id_urls_url_id_put_request_from_dict = ApiV1UrlPoolsIdUrlsUrlIdPutRequest.from_dict(api_v1_url_pools_id_urls_url_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1UrlPoolsIdUrlsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** | Required — handlers/advertiser/url_pools.go returns 422 NO_TITLE_GIVEN when omitted. | 
**weight** | **int** | Share under sort_type wr. Omitted &#x3D; 0, which a weighted rotation never picks — send a weight when the pool uses wr. | [optional] [default to 0]
**properties** | **str** |  | [optional] 
**keywords** | **str** | Comma-separated targeting keywords; empty &#x3D; a keyword fallback URL (serves when no targeted URL matches). | [optional] 
**is_fallback** | **bool** | Backup: used only while no other URL of the pool is live (\&quot;Backup\&quot; in the panel). | [optional] 
**start_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt.md) |  | [optional] 
**end_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_url_pools_id_urls_post_request import ApiV1UrlPoolsIdUrlsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UrlPoolsIdUrlsPostRequest from a JSON string
api_v1_url_pools_id_urls_post_request_instance = ApiV1UrlPoolsIdUrlsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1UrlPoolsIdUrlsPostRequest.to_json())

# convert the object into a dict
api_v1_url_pools_id_urls_post_request_dict = api_v1_url_pools_id_urls_post_request_instance.to_dict()
# create an instance of ApiV1UrlPoolsIdUrlsPostRequest from a dict
api_v1_url_pools_id_urls_post_request_from_dict = ApiV1UrlPoolsIdUrlsPostRequest.from_dict(api_v1_url_pools_id_urls_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



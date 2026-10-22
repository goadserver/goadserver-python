# ApiV1CreativePoolsIdItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_id** | **int** | Id of an uploaded creative (see /api/v1/creatives/upload). One of creative_id / banner_url required. | [optional] 
**banner_url** | **str** | Hotlink image/video URL — used when creative_id is omitted. | [optional] 
**bansizeid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_id_items_post_request import ApiV1CreativePoolsIdItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsIdItemsPostRequest from a JSON string
api_v1_creative_pools_id_items_post_request_instance = ApiV1CreativePoolsIdItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsIdItemsPostRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_id_items_post_request_dict = api_v1_creative_pools_id_items_post_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsIdItemsPostRequest from a dict
api_v1_creative_pools_id_items_post_request_from_dict = ApiV1CreativePoolsIdItemsPostRequest.from_dict(api_v1_creative_pools_id_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



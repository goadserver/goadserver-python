# ApiV1CreativePoolsIdAddUrlsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **str** | Newline-separated URLs. | 
**sizeid** | **int** | Banner pools: the banner size id (see /api/v1/lookups/banner-sizes). | [optional] 
**type** | **str** |  | [optional] [default to 'image_url']

## Example

```python
from goadserver.models.api_v1_creative_pools_id_add_urls_post_request import ApiV1CreativePoolsIdAddUrlsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsIdAddUrlsPostRequest from a JSON string
api_v1_creative_pools_id_add_urls_post_request_instance = ApiV1CreativePoolsIdAddUrlsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsIdAddUrlsPostRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_id_add_urls_post_request_dict = api_v1_creative_pools_id_add_urls_post_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsIdAddUrlsPostRequest from a dict
api_v1_creative_pools_id_add_urls_post_request_from_dict = ApiV1CreativePoolsIdAddUrlsPostRequest.from_dict(api_v1_creative_pools_id_add_urls_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



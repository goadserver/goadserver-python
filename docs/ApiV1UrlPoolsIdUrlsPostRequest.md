# ApiV1UrlPoolsIdUrlsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | [optional] 
**weight** | **int** |  | [optional] [default to 1]
**properties** | **str** |  | [optional] 

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



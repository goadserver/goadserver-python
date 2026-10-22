# ApiV1ProductFeedsPreviewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | native or left out &#x3D; card. | [optional] 
**template_html** | **str** |  | [optional] 
**cta** | **str** |  | [optional] 
**accent** | **str** | #rrggbb | [optional] 
**bansizeid** | **int** |  | [optional] 
**product** | [**ApiV1ProductFeedsPreviewPostRequestProduct**](ApiV1ProductFeedsPreviewPostRequestProduct.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_product_feeds_preview_post_request import ApiV1ProductFeedsPreviewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ProductFeedsPreviewPostRequest from a JSON string
api_v1_product_feeds_preview_post_request_instance = ApiV1ProductFeedsPreviewPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1ProductFeedsPreviewPostRequest.to_json())

# convert the object into a dict
api_v1_product_feeds_preview_post_request_dict = api_v1_product_feeds_preview_post_request_instance.to_dict()
# create an instance of ApiV1ProductFeedsPreviewPostRequest from a dict
api_v1_product_feeds_preview_post_request_from_dict = ApiV1ProductFeedsPreviewPostRequest.from_dict(api_v1_product_feeds_preview_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



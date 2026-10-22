# ApiV1ProductFeedsPreviewPostRequestProduct

Sample product to render; a built-in sample without it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**image_link** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_product_feeds_preview_post_request_product import ApiV1ProductFeedsPreviewPostRequestProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ProductFeedsPreviewPostRequestProduct from a JSON string
api_v1_product_feeds_preview_post_request_product_instance = ApiV1ProductFeedsPreviewPostRequestProduct.from_json(json)
# print the JSON string representation of the object
print(ApiV1ProductFeedsPreviewPostRequestProduct.to_json())

# convert the object into a dict
api_v1_product_feeds_preview_post_request_product_dict = api_v1_product_feeds_preview_post_request_product_instance.to_dict()
# create an instance of ApiV1ProductFeedsPreviewPostRequestProduct from a dict
api_v1_product_feeds_preview_post_request_product_from_dict = ApiV1ProductFeedsPreviewPostRequestProduct.from_dict(api_v1_product_feeds_preview_post_request_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



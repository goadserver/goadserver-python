# ApiV1ProductFeedsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | One of your RON campaigns (native 3, Search Ads 42 or banner 2). | 
**url** | **str** | Feed URL, http(s), public host, at most 20 MB. | 
**name** | **str** |  | [optional] 
**format** | **str** |  | [optional] [default to 'auto']
**refresh_hours** | **int** | 0 &#x3D; manual. | [optional] 
**max_items** | **int** |  | [optional] 
**price_in_title** | **bool** |  | [optional] 
**bid** | **float** | The new ads&#39; bid; 0 &#x3D; the bid of the campaign&#39;s newest ad. | [optional] 
**template** | **str** | Dynamic banners (banner campaigns): card, overlay, minimal or custom. native (or leaving it out) &#x3D; plain native ads. | [optional] 
**template_html** | **str** | custom template only. | [optional] 
**cta** | **str** |  | [optional] 
**accent** | **str** | #rrggbb | [optional] 
**bansizeid** | **int** | Dynamic banners: one of the campaign&#39;s banner_sizes. | [optional] 
**retarget** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_product_feeds_post_request import ApiV1ProductFeedsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ProductFeedsPostRequest from a JSON string
api_v1_product_feeds_post_request_instance = ApiV1ProductFeedsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1ProductFeedsPostRequest.to_json())

# convert the object into a dict
api_v1_product_feeds_post_request_dict = api_v1_product_feeds_post_request_instance.to_dict()
# create an instance of ApiV1ProductFeedsPostRequest from a dict
api_v1_product_feeds_post_request_from_dict = ApiV1ProductFeedsPostRequest.from_dict(api_v1_product_feeds_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



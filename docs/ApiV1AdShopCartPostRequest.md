# ApiV1AdShopCartPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** |  | [optional] 
**opportunity_ids** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_shop_cart_post_request import ApiV1AdShopCartPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdShopCartPostRequest from a JSON string
api_v1_ad_shop_cart_post_request_instance = ApiV1AdShopCartPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdShopCartPostRequest.to_json())

# convert the object into a dict
api_v1_ad_shop_cart_post_request_dict = api_v1_ad_shop_cart_post_request_instance.to_dict()
# create an instance of ApiV1AdShopCartPostRequest from a dict
api_v1_ad_shop_cart_post_request_from_dict = ApiV1AdShopCartPostRequest.from_dict(api_v1_ad_shop_cart_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



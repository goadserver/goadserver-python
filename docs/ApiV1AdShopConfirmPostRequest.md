# ApiV1AdShopConfirmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** | Client-chosen | 
**flat_start** | **date** |  | [optional] 
**flat_end** | **date** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_shop_confirm_post_request import ApiV1AdShopConfirmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdShopConfirmPostRequest from a JSON string
api_v1_ad_shop_confirm_post_request_instance = ApiV1AdShopConfirmPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdShopConfirmPostRequest.to_json())

# convert the object into a dict
api_v1_ad_shop_confirm_post_request_dict = api_v1_ad_shop_confirm_post_request_instance.to_dict()
# create an instance of ApiV1AdShopConfirmPostRequest from a dict
api_v1_ad_shop_confirm_post_request_from_dict = ApiV1AdShopConfirmPostRequest.from_dict(api_v1_ad_shop_confirm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CouponsSetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**end_date** | **date** | Last day the codes can be redeemed (YYYY-MM-DD). | 

## Example

```python
from goadserver.models.api_v1_coupons_sets_post_request import ApiV1CouponsSetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CouponsSetsPostRequest from a JSON string
api_v1_coupons_sets_post_request_instance = ApiV1CouponsSetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CouponsSetsPostRequest.to_json())

# convert the object into a dict
api_v1_coupons_sets_post_request_dict = api_v1_coupons_sets_post_request_instance.to_dict()
# create an instance of ApiV1CouponsSetsPostRequest from a dict
api_v1_coupons_sets_post_request_from_dict = ApiV1CouponsSetsPostRequest.from_dict(api_v1_coupons_sets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



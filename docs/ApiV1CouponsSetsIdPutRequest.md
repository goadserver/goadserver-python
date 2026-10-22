# ApiV1CouponsSetsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_coupons_sets_id_put_request import ApiV1CouponsSetsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CouponsSetsIdPutRequest from a JSON string
api_v1_coupons_sets_id_put_request_instance = ApiV1CouponsSetsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CouponsSetsIdPutRequest.to_json())

# convert the object into a dict
api_v1_coupons_sets_id_put_request_dict = api_v1_coupons_sets_id_put_request_instance.to_dict()
# create an instance of ApiV1CouponsSetsIdPutRequest from a dict
api_v1_coupons_sets_id_put_request_from_dict = ApiV1CouponsSetsIdPutRequest.from_dict(api_v1_coupons_sets_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



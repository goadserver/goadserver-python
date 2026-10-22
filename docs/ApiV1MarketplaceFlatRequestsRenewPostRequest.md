# ApiV1MarketplaceFlatRequestsRenewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | The flat (RON paytype 5) campaign. | 
**date_start** | **date** |  | 
**date_end** | **date** |  | 
**total_costs** | **float** | Deal amount in currency units. | 

## Example

```python
from goadserver.models.api_v1_marketplace_flat_requests_renew_post_request import ApiV1MarketplaceFlatRequestsRenewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MarketplaceFlatRequestsRenewPostRequest from a JSON string
api_v1_marketplace_flat_requests_renew_post_request_instance = ApiV1MarketplaceFlatRequestsRenewPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1MarketplaceFlatRequestsRenewPostRequest.to_json())

# convert the object into a dict
api_v1_marketplace_flat_requests_renew_post_request_dict = api_v1_marketplace_flat_requests_renew_post_request_instance.to_dict()
# create an instance of ApiV1MarketplaceFlatRequestsRenewPostRequest from a dict
api_v1_marketplace_flat_requests_renew_post_request_from_dict = ApiV1MarketplaceFlatRequestsRenewPostRequest.from_dict(api_v1_marketplace_flat_requests_renew_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



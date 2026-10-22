# ApiV1AdspacesIdPricesTypePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_typeid** | **int** |  | [optional] [default to 0]
**cpm_price** | [**List[ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner]**](ApiV1AdspacesIdPricesTypePostRequestCpmPriceInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_prices_type_post_request import ApiV1AdspacesIdPricesTypePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdPricesTypePostRequest from a JSON string
api_v1_adspaces_id_prices_type_post_request_instance = ApiV1AdspacesIdPricesTypePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdPricesTypePostRequest.to_json())

# convert the object into a dict
api_v1_adspaces_id_prices_type_post_request_dict = api_v1_adspaces_id_prices_type_post_request_instance.to_dict()
# create an instance of ApiV1AdspacesIdPricesTypePostRequest from a dict
api_v1_adspaces_id_prices_type_post_request_from_dict = ApiV1AdspacesIdPricesTypePostRequest.from_dict(api_v1_adspaces_id_prices_type_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



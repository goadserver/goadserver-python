# ApiV1FundsTransferPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_users** | **int** | Recipient user id (from the connected-transfer list). | 
**amount** | **float** | Currency units. | 

## Example

```python
from goadserver.models.api_v1_funds_transfer_post_request import ApiV1FundsTransferPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsTransferPostRequest from a JSON string
api_v1_funds_transfer_post_request_instance = ApiV1FundsTransferPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsTransferPostRequest.to_json())

# convert the object into a dict
api_v1_funds_transfer_post_request_dict = api_v1_funds_transfer_post_request_instance.to_dict()
# create an instance of ApiV1FundsTransferPostRequest from a dict
api_v1_funds_transfer_post_request_from_dict = ApiV1FundsTransferPostRequest.from_dict(api_v1_funds_transfer_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



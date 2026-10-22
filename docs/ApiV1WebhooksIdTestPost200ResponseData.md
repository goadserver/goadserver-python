# ApiV1WebhooksIdTestPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | [optional] 
**delivery_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**http_status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_webhooks_id_test_post200_response_data import ApiV1WebhooksIdTestPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksIdTestPost200ResponseData from a JSON string
api_v1_webhooks_id_test_post200_response_data_instance = ApiV1WebhooksIdTestPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1WebhooksIdTestPost200ResponseData.to_json())

# convert the object into a dict
api_v1_webhooks_id_test_post200_response_data_dict = api_v1_webhooks_id_test_post200_response_data_instance.to_dict()
# create an instance of ApiV1WebhooksIdTestPost200ResponseData from a dict
api_v1_webhooks_id_test_post200_response_data_from_dict = ApiV1WebhooksIdTestPost200ResponseData.from_dict(api_v1_webhooks_id_test_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



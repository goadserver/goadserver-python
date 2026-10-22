# ApiV1WebhooksIdDeliveriesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event_id** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**attempts** | **int** |  | [optional] 
**next_attempt_at** | **datetime** |  | [optional] 
**last_status** | **int** |  | [optional] 
**last_error** | **str** |  | [optional] 
**delivered_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_webhooks_id_deliveries_get200_response_data_inner import ApiV1WebhooksIdDeliveriesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksIdDeliveriesGet200ResponseDataInner from a JSON string
api_v1_webhooks_id_deliveries_get200_response_data_inner_instance = ApiV1WebhooksIdDeliveriesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1WebhooksIdDeliveriesGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_webhooks_id_deliveries_get200_response_data_inner_dict = api_v1_webhooks_id_deliveries_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1WebhooksIdDeliveriesGet200ResponseDataInner from a dict
api_v1_webhooks_id_deliveries_get200_response_data_inner_from_dict = ApiV1WebhooksIdDeliveriesGet200ResponseDataInner.from_dict(api_v1_webhooks_id_deliveries_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



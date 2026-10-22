# ApiV1PublisherPushDeliveryRulesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**segment_id** | **int** |  | [optional] 
**cadence_hours** | **int** |  | [optional] 
**freq_cap_hours** | **int** |  | [optional] 
**max_per_run** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_delivery_rules_id_put_request import ApiV1PublisherPushDeliveryRulesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushDeliveryRulesIdPutRequest from a JSON string
api_v1_publisher_push_delivery_rules_id_put_request_instance = ApiV1PublisherPushDeliveryRulesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushDeliveryRulesIdPutRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_delivery_rules_id_put_request_dict = api_v1_publisher_push_delivery_rules_id_put_request_instance.to_dict()
# create an instance of ApiV1PublisherPushDeliveryRulesIdPutRequest from a dict
api_v1_publisher_push_delivery_rules_id_put_request_from_dict = ApiV1PublisherPushDeliveryRulesIdPutRequest.from_dict(api_v1_publisher_push_delivery_rules_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



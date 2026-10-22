# ApiV1PublisherPushDeliveryRulesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**segment_id** | **int** | PushSegment id, or 0 for the whole active audience. | [optional] 
**cadence_hours** | **int** |  | [optional] 
**freq_cap_hours** | **int** |  | [optional] 
**max_per_run** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_delivery_rules_post_request import ApiV1PublisherPushDeliveryRulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushDeliveryRulesPostRequest from a JSON string
api_v1_publisher_push_delivery_rules_post_request_instance = ApiV1PublisherPushDeliveryRulesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushDeliveryRulesPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_delivery_rules_post_request_dict = api_v1_publisher_push_delivery_rules_post_request_instance.to_dict()
# create an instance of ApiV1PublisherPushDeliveryRulesPostRequest from a dict
api_v1_publisher_push_delivery_rules_post_request_from_dict = ApiV1PublisherPushDeliveryRulesPostRequest.from_dict(api_v1_publisher_push_delivery_rules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



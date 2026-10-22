# ApiV1PublisherPushSubscribersGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_days** | **int** |  | [optional] 
**total** | **int** | Lifetime subscribers. | [optional] 
**active** | **int** | Lifetime subscribers still active. | [optional] 
**window_count** | **int** | Opt-ins inside the window. | [optional] 
**source_count** | **int** | Distinct pushads adzones that captured them. | [optional] 
**subscribers** | [**List[PushSubscriber]**](PushSubscriber.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_subscribers_get200_response_data import ApiV1PublisherPushSubscribersGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSubscribersGet200ResponseData from a JSON string
api_v1_publisher_push_subscribers_get200_response_data_instance = ApiV1PublisherPushSubscribersGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSubscribersGet200ResponseData.to_json())

# convert the object into a dict
api_v1_publisher_push_subscribers_get200_response_data_dict = api_v1_publisher_push_subscribers_get200_response_data_instance.to_dict()
# create an instance of ApiV1PublisherPushSubscribersGet200ResponseData from a dict
api_v1_publisher_push_subscribers_get200_response_data_from_dict = ApiV1PublisherPushSubscribersGet200ResponseData.from_dict(api_v1_publisher_push_subscribers_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



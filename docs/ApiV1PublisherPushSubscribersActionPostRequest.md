# ApiV1PublisherPushSubscribersActionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**action** | **str** |  | 

## Example

```python
from goadserver.models.api_v1_publisher_push_subscribers_action_post_request import ApiV1PublisherPushSubscribersActionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSubscribersActionPostRequest from a JSON string
api_v1_publisher_push_subscribers_action_post_request_instance = ApiV1PublisherPushSubscribersActionPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSubscribersActionPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_subscribers_action_post_request_dict = api_v1_publisher_push_subscribers_action_post_request_instance.to_dict()
# create an instance of ApiV1PublisherPushSubscribersActionPostRequest from a dict
api_v1_publisher_push_subscribers_action_post_request_from_dict = ApiV1PublisherPushSubscribersActionPostRequest.from_dict(api_v1_publisher_push_subscribers_action_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



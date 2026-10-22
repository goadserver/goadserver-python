# ApiV1PublisherPushCampaignsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Internal label. | [optional] 
**title** | **str** |  | 
**body** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_campaigns_post_request import ApiV1PublisherPushCampaignsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushCampaignsPostRequest from a JSON string
api_v1_publisher_push_campaigns_post_request_instance = ApiV1PublisherPushCampaignsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushCampaignsPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_campaigns_post_request_dict = api_v1_publisher_push_campaigns_post_request_instance.to_dict()
# create an instance of ApiV1PublisherPushCampaignsPostRequest from a dict
api_v1_publisher_push_campaigns_post_request_from_dict = ApiV1PublisherPushCampaignsPostRequest.from_dict(api_v1_publisher_push_campaigns_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



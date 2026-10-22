# ApiV1PublisherPushSegmentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_spaceid** | **int** | Only subscribers captured on this pushads adzone. 0 &#x3D; any. | [optional] 
**domainid** | **int** | Only subscribers captured on this landing domain. 0 &#x3D; any. | [optional] 
**clickid_only** | **bool** |  | [optional] 
**age_min_days** | **int** |  | [optional] 
**age_max_days** | **int** |  | [optional] 
**active_only** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_segments_post_request import ApiV1PublisherPushSegmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSegmentsPostRequest from a JSON string
api_v1_publisher_push_segments_post_request_instance = ApiV1PublisherPushSegmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSegmentsPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_segments_post_request_dict = api_v1_publisher_push_segments_post_request_instance.to_dict()
# create an instance of ApiV1PublisherPushSegmentsPostRequest from a dict
api_v1_publisher_push_segments_post_request_from_dict = ApiV1PublisherPushSegmentsPostRequest.from_dict(api_v1_publisher_push_segments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



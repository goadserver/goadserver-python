# ApiV1PublisherPushSegmentsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_spaceid** | **int** |  | [optional] 
**domainid** | **int** |  | [optional] 
**clickid_only** | **bool** |  | [optional] 
**age_min_days** | **int** |  | [optional] 
**age_max_days** | **int** |  | [optional] 
**active_only** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_segments_id_put_request import ApiV1PublisherPushSegmentsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSegmentsIdPutRequest from a JSON string
api_v1_publisher_push_segments_id_put_request_instance = ApiV1PublisherPushSegmentsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSegmentsIdPutRequest.to_json())

# convert the object into a dict
api_v1_publisher_push_segments_id_put_request_dict = api_v1_publisher_push_segments_id_put_request_instance.to_dict()
# create an instance of ApiV1PublisherPushSegmentsIdPutRequest from a dict
api_v1_publisher_push_segments_id_put_request_from_dict = ApiV1PublisherPushSegmentsIdPutRequest.from_dict(api_v1_publisher_push_segments_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



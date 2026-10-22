# ApiV1TrackerSourcesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**template_slug** | **str** |  | [optional] 
**postbacks** | **Dict[str, object]** | Per-source outbound postback configuration. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_sources_post_request import ApiV1TrackerSourcesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerSourcesPostRequest from a JSON string
api_v1_tracker_sources_post_request_instance = ApiV1TrackerSourcesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerSourcesPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_sources_post_request_dict = api_v1_tracker_sources_post_request_instance.to_dict()
# create an instance of ApiV1TrackerSourcesPostRequest from a dict
api_v1_tracker_sources_post_request_from_dict = ApiV1TrackerSourcesPostRequest.from_dict(api_v1_tracker_sources_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



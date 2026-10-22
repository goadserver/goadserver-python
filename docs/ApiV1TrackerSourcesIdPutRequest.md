# ApiV1TrackerSourcesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_slug** | **str** |  | [optional] 
**postbacks** | **Dict[str, object]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_sources_id_put_request import ApiV1TrackerSourcesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerSourcesIdPutRequest from a JSON string
api_v1_tracker_sources_id_put_request_instance = ApiV1TrackerSourcesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerSourcesIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_sources_id_put_request_dict = api_v1_tracker_sources_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerSourcesIdPutRequest from a dict
api_v1_tracker_sources_id_put_request_from_dict = ApiV1TrackerSourcesIdPutRequest.from_dict(api_v1_tracker_sources_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



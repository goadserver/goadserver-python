# ApiV1TrackerCustomParamsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | [**List[ApiV1TrackerCustomParamsPutRequestSlotsInner]**](ApiV1TrackerCustomParamsPutRequestSlotsInner.md) |  | 

## Example

```python
from goadserver.models.api_v1_tracker_custom_params_put_request import ApiV1TrackerCustomParamsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerCustomParamsPutRequest from a JSON string
api_v1_tracker_custom_params_put_request_instance = ApiV1TrackerCustomParamsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerCustomParamsPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_custom_params_put_request_dict = api_v1_tracker_custom_params_put_request_instance.to_dict()
# create an instance of ApiV1TrackerCustomParamsPutRequest from a dict
api_v1_tracker_custom_params_put_request_from_dict = ApiV1TrackerCustomParamsPutRequest.from_dict(api_v1_tracker_custom_params_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



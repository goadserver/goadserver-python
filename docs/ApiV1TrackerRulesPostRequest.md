# ApiV1TrackerRulesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**scope** | **str** |  | 
**schedule** | **str** |  | 
**is_active** | **bool** |  | [optional] 
**apply_actions** | **bool** | false &#x3D; evaluate and record, never write back. | [optional] 
**conditions** | **List[Dict[str, object]]** |  | [optional] 
**action** | **Dict[str, object]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_rules_post_request import ApiV1TrackerRulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerRulesPostRequest from a JSON string
api_v1_tracker_rules_post_request_instance = ApiV1TrackerRulesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerRulesPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_rules_post_request_dict = api_v1_tracker_rules_post_request_instance.to_dict()
# create an instance of ApiV1TrackerRulesPostRequest from a dict
api_v1_tracker_rules_post_request_from_dict = ApiV1TrackerRulesPostRequest.from_dict(api_v1_tracker_rules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



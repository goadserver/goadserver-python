# ApiV1TrackerRulesIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**apply_actions** | **bool** |  | [optional] 
**conditions** | **List[Dict[str, object]]** |  | [optional] 
**action** | **Dict[str, object]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_rules_id_put_request import ApiV1TrackerRulesIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerRulesIdPutRequest from a JSON string
api_v1_tracker_rules_id_put_request_instance = ApiV1TrackerRulesIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerRulesIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_rules_id_put_request_dict = api_v1_tracker_rules_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerRulesIdPutRequest from a dict
api_v1_tracker_rules_id_put_request_from_dict = ApiV1TrackerRulesIdPutRequest.from_dict(api_v1_tracker_rules_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



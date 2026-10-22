# ApiV1TrackerRulesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrackerRule]**](TrackerRule.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_rules_get200_response import ApiV1TrackerRulesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerRulesGet200Response from a JSON string
api_v1_tracker_rules_get200_response_instance = ApiV1TrackerRulesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerRulesGet200Response.to_json())

# convert the object into a dict
api_v1_tracker_rules_get200_response_dict = api_v1_tracker_rules_get200_response_instance.to_dict()
# create an instance of ApiV1TrackerRulesGet200Response from a dict
api_v1_tracker_rules_get200_response_from_dict = ApiV1TrackerRulesGet200Response.from_dict(api_v1_tracker_rules_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



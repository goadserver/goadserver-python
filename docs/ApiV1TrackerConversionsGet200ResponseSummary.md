# ApiV1TrackerConversionsGet200ResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean** | **int** |  | [optional] 
**on_hold** | **int** |  | [optional] 
**approved** | **int** |  | [optional] 
**rejected** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**total_payout** | **float** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_conversions_get200_response_summary import ApiV1TrackerConversionsGet200ResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerConversionsGet200ResponseSummary from a JSON string
api_v1_tracker_conversions_get200_response_summary_instance = ApiV1TrackerConversionsGet200ResponseSummary.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerConversionsGet200ResponseSummary.to_json())

# convert the object into a dict
api_v1_tracker_conversions_get200_response_summary_dict = api_v1_tracker_conversions_get200_response_summary_instance.to_dict()
# create an instance of ApiV1TrackerConversionsGet200ResponseSummary from a dict
api_v1_tracker_conversions_get200_response_summary_from_dict = ApiV1TrackerConversionsGet200ResponseSummary.from_dict(api_v1_tracker_conversions_get200_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



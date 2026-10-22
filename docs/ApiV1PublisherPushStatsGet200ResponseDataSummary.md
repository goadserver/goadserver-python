# ApiV1PublisherPushStatsGet200ResponseDataSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impressions** | **int** |  | [optional] 
**clicks** | **int** |  | [optional] 
**revenue** | **float** |  | [optional] 
**ctr** | **float** | Percent. | [optional] 
**subscribers** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_stats_get200_response_data_summary import ApiV1PublisherPushStatsGet200ResponseDataSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushStatsGet200ResponseDataSummary from a JSON string
api_v1_publisher_push_stats_get200_response_data_summary_instance = ApiV1PublisherPushStatsGet200ResponseDataSummary.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushStatsGet200ResponseDataSummary.to_json())

# convert the object into a dict
api_v1_publisher_push_stats_get200_response_data_summary_dict = api_v1_publisher_push_stats_get200_response_data_summary_instance.to_dict()
# create an instance of ApiV1PublisherPushStatsGet200ResponseDataSummary from a dict
api_v1_publisher_push_stats_get200_response_data_summary_from_dict = ApiV1PublisherPushStatsGet200ResponseDataSummary.from_dict(api_v1_publisher_push_stats_get200_response_data_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1PublisherPushStatsGet200ResponseDataDailyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**impressions** | **int** |  | [optional] 
**clicks** | **int** |  | [optional] 
**revenue** | **float** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_stats_get200_response_data_daily_inner import ApiV1PublisherPushStatsGet200ResponseDataDailyInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushStatsGet200ResponseDataDailyInner from a JSON string
api_v1_publisher_push_stats_get200_response_data_daily_inner_instance = ApiV1PublisherPushStatsGet200ResponseDataDailyInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushStatsGet200ResponseDataDailyInner.to_json())

# convert the object into a dict
api_v1_publisher_push_stats_get200_response_data_daily_inner_dict = api_v1_publisher_push_stats_get200_response_data_daily_inner_instance.to_dict()
# create an instance of ApiV1PublisherPushStatsGet200ResponseDataDailyInner from a dict
api_v1_publisher_push_stats_get200_response_data_daily_inner_from_dict = ApiV1PublisherPushStatsGet200ResponseDataDailyInner.from_dict(api_v1_publisher_push_stats_get200_response_data_daily_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



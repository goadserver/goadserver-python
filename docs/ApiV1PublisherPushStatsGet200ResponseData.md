# ApiV1PublisherPushStatsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_days** | **int** |  | [optional] 
**summary** | [**ApiV1PublisherPushStatsGet200ResponseDataSummary**](ApiV1PublisherPushStatsGet200ResponseDataSummary.md) |  | [optional] 
**daily** | [**List[ApiV1PublisherPushStatsGet200ResponseDataDailyInner]**](ApiV1PublisherPushStatsGet200ResponseDataDailyInner.md) |  | [optional] 
**growth** | [**List[ApiV1PublisherPushStatsGet200ResponseDataGrowthInner]**](ApiV1PublisherPushStatsGet200ResponseDataGrowthInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_stats_get200_response_data import ApiV1PublisherPushStatsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushStatsGet200ResponseData from a JSON string
api_v1_publisher_push_stats_get200_response_data_instance = ApiV1PublisherPushStatsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushStatsGet200ResponseData.to_json())

# convert the object into a dict
api_v1_publisher_push_stats_get200_response_data_dict = api_v1_publisher_push_stats_get200_response_data_instance.to_dict()
# create an instance of ApiV1PublisherPushStatsGet200ResponseData from a dict
api_v1_publisher_push_stats_get200_response_data_from_dict = ApiV1PublisherPushStatsGet200ResponseData.from_dict(api_v1_publisher_push_stats_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



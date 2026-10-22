# StatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **date** |  | [optional] 
**to** | **date** |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**totals** | **Dict[str, Optional[float]]** | Same metric keys as a row. A ratio that cannot be formed (e.g. advertiser &#x60;roi&#x60; below 1.00 of spend) is &#x60;null&#x60;. | [optional] 
**rows** | **List[Dict[str, object]]** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_rows** | **int** |  | [optional] 
**timezone** | **str** | &#x60;/advertiser/stats&#x60;: the network&#39;s timezone — the clock dates and &#x60;interval&#x3D;hour&#x60; hours are counted in (and campaign &#x60;day_parting&#x60; runs on). | [optional] 
**ignored_metrics** | **List[str]** | Requested metric names the endpoint does not know (only where the endpoint documents lenient metric parsing; absent when empty). | [optional] 

## Example

```python
from goadserver.models.stats_response import StatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatsResponse from a JSON string
stats_response_instance = StatsResponse.from_json(json)
# print the JSON string representation of the object
print(StatsResponse.to_json())

# convert the object into a dict
stats_response_dict = stats_response_instance.to_dict()
# create an instance of StatsResponse from a dict
stats_response_from_dict = StatsResponse.from_dict(stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



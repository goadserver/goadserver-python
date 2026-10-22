# RtbTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** |  | [optional] 
**http_status** | **int** |  | [optional] 
**latency_ms** | **int** |  | [optional] 
**request_url** | **str** |  | [optional] 
**request_method** | **str** |  | [optional] 
**request_headers** | **Dict[str, str]** |  | [optional] 
**request_body** | **str** |  | [optional] 
**response_headers** | **Dict[str, str]** |  | [optional] 
**response_body** | **str** |  | [optional] 
**response_body_truncated** | **bool** |  | [optional] 
**error_category** | **str** | e.g. blocked_url, invalid_url, timeout. | [optional] 
**error_message** | **str** |  | [optional] 
**hints** | **List[str]** |  | [optional] 
**bid_count** | **int** |  | [optional] 
**best_price** | **float** |  | [optional] 

## Example

```python
from goadserver.models.rtb_test_result import RtbTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of RtbTestResult from a JSON string
rtb_test_result_instance = RtbTestResult.from_json(json)
# print the JSON string representation of the object
print(RtbTestResult.to_json())

# convert the object into a dict
rtb_test_result_dict = rtb_test_result_instance.to_dict()
# create an instance of RtbTestResult from a dict
rtb_test_result_from_dict = RtbTestResult.from_dict(rtb_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



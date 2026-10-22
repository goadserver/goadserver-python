# RtbTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_type** | **str** | Overrides the campaign&#39;s ad type. | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**country** | **str** | ISO-2 or ISO-3. | [optional] 
**domain** | **str** |  | [optional] 
**page_url** | **str** |  | [optional] 
**bidfloor** | **float** |  | [optional] 
**tmax** | **int** | Milliseconds. | [optional] 
**currency** | **str** |  | [optional] [default to 'USD']
**secure** | **int** | Default from the URL scheme. | [optional] 
**user_ua** | **str** | User agent to send (default the caller&#39;s). | [optional] 
**user_ip** | **str** | Device IP to send (default the caller&#39;s). | [optional] 
**override_url** | **str** | Test this URL instead of the saved one. | [optional] 

## Example

```python
from goadserver.models.rtb_test_request import RtbTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RtbTestRequest from a JSON string
rtb_test_request_instance = RtbTestRequest.from_json(json)
# print the JSON string representation of the object
print(RtbTestRequest.to_json())

# convert the object into a dict
rtb_test_request_dict = rtb_test_request_instance.to_dict()
# create an instance of RtbTestRequest from a dict
rtb_test_request_from_dict = RtbTestRequest.from_dict(rtb_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



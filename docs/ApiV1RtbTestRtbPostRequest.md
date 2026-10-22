# ApiV1RtbTestRtbPostRequest


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
**url** | **str** | Endpoint URL (required unless override_url is sent). | [optional] 
**rtbtype** | **str** |  | [optional] [default to 'openrtb']
**adtypeid** | **int** |  | [optional] [default to 1]

## Example

```python
from goadserver.models.api_v1_rtb_test_rtb_post_request import ApiV1RtbTestRtbPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RtbTestRtbPostRequest from a JSON string
api_v1_rtb_test_rtb_post_request_instance = ApiV1RtbTestRtbPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1RtbTestRtbPostRequest.to_json())

# convert the object into a dict
api_v1_rtb_test_rtb_post_request_dict = api_v1_rtb_test_rtb_post_request_instance.to_dict()
# create an instance of ApiV1RtbTestRtbPostRequest from a dict
api_v1_rtb_test_rtb_post_request_from_dict = ApiV1RtbTestRtbPostRequest.from_dict(api_v1_rtb_test_rtb_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



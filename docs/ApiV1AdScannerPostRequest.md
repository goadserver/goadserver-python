# ApiV1AdScannerPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**target** | **str** |  | [optional] 
**scan_type** | **str** |  | [optional] 
**adtypeid** | **int** |  | [optional] 
**tags** | [**ApiV1AdScannerPostRequestTags**](ApiV1AdScannerPostRequestTags.md) |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_scanner_post_request import ApiV1AdScannerPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdScannerPostRequest from a JSON string
api_v1_ad_scanner_post_request_instance = ApiV1AdScannerPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdScannerPostRequest.to_json())

# convert the object into a dict
api_v1_ad_scanner_post_request_dict = api_v1_ad_scanner_post_request_instance.to_dict()
# create an instance of ApiV1AdScannerPostRequest from a dict
api_v1_ad_scanner_post_request_from_dict = ApiV1AdScannerPostRequest.from_dict(api_v1_ad_scanner_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



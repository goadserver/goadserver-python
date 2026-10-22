# ApiV1AdScannerIdManualItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**value** | **str** |  | 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ad_width** | **int** |  | [optional] 
**ad_height** | **int** |  | [optional] 
**isactive** | **int** |  | [optional] 
**referrer** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_scanner_id_manual_items_post_request import ApiV1AdScannerIdManualItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdScannerIdManualItemsPostRequest from a JSON string
api_v1_ad_scanner_id_manual_items_post_request_instance = ApiV1AdScannerIdManualItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdScannerIdManualItemsPostRequest.to_json())

# convert the object into a dict
api_v1_ad_scanner_id_manual_items_post_request_dict = api_v1_ad_scanner_id_manual_items_post_request_instance.to_dict()
# create an instance of ApiV1AdScannerIdManualItemsPostRequest from a dict
api_v1_ad_scanner_id_manual_items_post_request_from_dict = ApiV1AdScannerIdManualItemsPostRequest.from_dict(api_v1_ad_scanner_id_manual_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



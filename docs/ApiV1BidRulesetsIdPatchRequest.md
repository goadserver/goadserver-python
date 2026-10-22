# ApiV1BidRulesetsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**paytype** | **str** | Omit to keep the current paytype. | [optional] 
**default_tz** | **str** | Omit to keep the current timezone. | [optional] 
**rules** | [**List[BidRule]**](BidRule.md) | Omit to keep the current rules; send &#x60;[]&#x60; to clear them. | [optional] 

## Example

```python
from goadserver.models.api_v1_bid_rulesets_id_patch_request import ApiV1BidRulesetsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1BidRulesetsIdPatchRequest from a JSON string
api_v1_bid_rulesets_id_patch_request_instance = ApiV1BidRulesetsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1BidRulesetsIdPatchRequest.to_json())

# convert the object into a dict
api_v1_bid_rulesets_id_patch_request_dict = api_v1_bid_rulesets_id_patch_request_instance.to_dict()
# create an instance of ApiV1BidRulesetsIdPatchRequest from a dict
api_v1_bid_rulesets_id_patch_request_from_dict = ApiV1BidRulesetsIdPatchRequest.from_dict(api_v1_bid_rulesets_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



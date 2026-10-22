# ApiV1BidRulesetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**paytype** | **str** |  | 
**default_tz** | **str** | IANA tz, e.g. \&quot;America/Los_Angeles\&quot;. Empty/missing &#x3D; UTC. | [optional] [default to 'UTC']
**rules** | [**List[BidRule]**](BidRule.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_bid_rulesets_post_request import ApiV1BidRulesetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1BidRulesetsPostRequest from a JSON string
api_v1_bid_rulesets_post_request_instance = ApiV1BidRulesetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1BidRulesetsPostRequest.to_json())

# convert the object into a dict
api_v1_bid_rulesets_post_request_dict = api_v1_bid_rulesets_post_request_instance.to_dict()
# create an instance of ApiV1BidRulesetsPostRequest from a dict
api_v1_bid_rulesets_post_request_from_dict = ApiV1BidRulesetsPostRequest.from_dict(api_v1_bid_rulesets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1BidRulesetsIdClonePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Override the cloned ruleset&#39;s name. Defaults to \&quot;&lt;original&gt; (copy)\&quot;. | [optional] 

## Example

```python
from goadserver.models.api_v1_bid_rulesets_id_clone_post_request import ApiV1BidRulesetsIdClonePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1BidRulesetsIdClonePostRequest from a JSON string
api_v1_bid_rulesets_id_clone_post_request_instance = ApiV1BidRulesetsIdClonePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1BidRulesetsIdClonePostRequest.to_json())

# convert the object into a dict
api_v1_bid_rulesets_id_clone_post_request_dict = api_v1_bid_rulesets_id_clone_post_request_instance.to_dict()
# create an instance of ApiV1BidRulesetsIdClonePostRequest from a dict
api_v1_bid_rulesets_id_clone_post_request_from_dict = ApiV1BidRulesetsIdClonePostRequest.from_dict(api_v1_bid_rulesets_id_clone_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



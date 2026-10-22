# BidRuleset

Full ruleset record. Returned by the show / create / update / clone endpoints. The `rules` array is pre-sorted by `priority` ASC. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**userid** | **int** | Owner advertiser id. | [optional] 
**name** | **str** |  | [optional] 
**paytype** | **str** | Pricing flavor of every bid in the ruleset. Must match the campaign&#39;s paytype at attach-time — a &#x60;cpc&#x60; ruleset can only attach to a CPC campaign, etc.  | [optional] 
**default_tz** | **str** | IANA timezone applied to any rule whose own &#x60;tz&#x60; is empty. Defaults to &#x60;UTC&#x60;.  | [optional] 
**rules** | [**List[BidRule]**](BidRule.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**created** | **int** | Unix seconds. | [optional] 
**updated** | **int** | Unix seconds. | [optional] 
**campaign_count** | **int** | Count of non-deleted campaigns currently attached to this ruleset. Useful as the \&quot;edit affects N other campaigns\&quot; heads-up before a destructive change.  | [optional] 

## Example

```python
from goadserver.models.bid_ruleset import BidRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of BidRuleset from a JSON string
bid_ruleset_instance = BidRuleset.from_json(json)
# print the JSON string representation of the object
print(BidRuleset.to_json())

# convert the object into a dict
bid_ruleset_dict = bid_ruleset_instance.to_dict()
# create an instance of BidRuleset from a dict
bid_ruleset_from_dict = BidRuleset.from_dict(bid_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



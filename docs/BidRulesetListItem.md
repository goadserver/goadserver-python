# BidRulesetListItem

Lightweight ruleset row returned by `GET /api/v1/bid-rulesets`. Same identity / metadata as `BidRuleset` minus the `rules` array — the list endpoint is meant for picker UIs and library views; load the full record via `GET /api/v1/bid-rulesets/{id}` when you need rule rows. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**userid** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**paytype** | **str** |  | [optional] 
**default_tz** | **str** |  | [optional] 
**rule_count** | **int** | Number of non-deleted rules in the ruleset. | [optional] 
**campaign_count** | **int** |  | [optional] 
**updated** | **int** | Unix seconds — list defaults to ordering by this DESC. | [optional] 
**created** | **int** | Unix seconds. | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.bid_ruleset_list_item import BidRulesetListItem

# TODO update the JSON string below
json = "{}"
# create an instance of BidRulesetListItem from a JSON string
bid_ruleset_list_item_instance = BidRulesetListItem.from_json(json)
# print the JSON string representation of the object
print(BidRulesetListItem.to_json())

# convert the object into a dict
bid_ruleset_list_item_dict = bid_ruleset_list_item_instance.to_dict()
# create an instance of BidRulesetListItem from a dict
bid_ruleset_list_item_from_dict = BidRulesetListItem.from_dict(bid_ruleset_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



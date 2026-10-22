# BidRule

One row in a ruleset's priority-ordered rule list. The first rule whose `conditions` match the incoming RTB request supplies the campaign's bid for that auction; lower `priority` = walked earlier. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rule id, read-only. Every save of the ruleset (create, PATCH, clone) soft-deletes the previous rule rows and inserts the submitted ones with **new** ids, so stats already stamped with an old rule id stay attributed to that old row. An &#x60;id&#x60; sent in a request is accepted and ignored.  | [optional] 
**priority** | **int** | Walk order — rules are evaluated by ascending &#x60;priority&#x60;. Lower &#x3D; higher priority. Ties broken by id.  | [optional] 
**bid** | **int** | Bid value in cents, interpreted per the parent ruleset&#39;s &#x60;paytype&#x60; (CPC bid per click, CPM bid per mille impressions, …).  | [optional] 
**tz** | **str** | IANA timezone the rule&#39;s daypart (&#x60;hour_start&#x60; / &#x60;hour_end&#x60;) is resolved in. Empty string &#x3D; inherit the ruleset&#39;s &#x60;default_tz&#x60;.  | [optional] 
**conditions** | [**BidRuleConditions**](BidRuleConditions.md) |  | [optional] 

## Example

```python
from goadserver.models.bid_rule import BidRule

# TODO update the JSON string below
json = "{}"
# create an instance of BidRule from a JSON string
bid_rule_instance = BidRule.from_json(json)
# print the JSON string representation of the object
print(BidRule.to_json())

# convert the object into a dict
bid_rule_dict = bid_rule_instance.to_dict()
# create an instance of BidRule from a dict
bid_rule_from_dict = BidRule.from_dict(bid_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



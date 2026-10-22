# BidRuleConditions

Structured per-rule match conditions. Every field is an independent include/exclude filter on one request dimension — missing or empty = \"no filter on this dimension\" (i.e. matches every value). A rule fires when **all** populated dimensions match the incoming RTB request.  Notes on specific dimensions:  - `regionids` is matched against the visitor's full geo lineage   (continent → country → region → region2 → city) — selecting   \"US\" (the country row from `/api/v1/lookups/regions`) at the   editor therefore fires for every US visitor regardless of   state / city. Send leaf ids when you want a tighter window. - `zone` / `domainids` are include-lists; `zone_block` /   `domainids_block` are exclude-lists. You can mix include +   exclude on the same rule — they're independent. - `domainids` / `domainids_block` reference the global   `bigdata.domains` catalogue (same id-space `xref.DomainId`   uses at serve time). The catalogue is far too large for a   list picker — IDs come from advertiser reports. - Daypart: `hour_start` and `hour_end` are integers 0..23   (inclusive), evaluated in the rule's `tz` (or the ruleset's   `default_tz` when the rule has `tz=\"\"`). When   `hour_end < hour_start` the window wraps past midnight —   e.g. `hour_start=18, hour_end=3` = 18:00 through 03:00 next   morning. - `conn_type` matches the visitor's connection class. Pair   `conn_type=[\"cellular\"]` with `carrier_id` for per-carrier   mobile targeting. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regionids** | **List[int]** | &#x60;geo2_locations.id&#x60; include-list. Visitor&#39;s lineage (continent / country / region / region2 / city) matches when **any** ancestor id is in this set. From &#x60;GET /api/v1/lookups/regions&#x60;.  | [optional] 
**os_id** | **List[int]** | OS id include-list. From &#x60;GET /api/v1/lookups/operating-systems&#x60;. | [optional] 
**browser_id** | **List[int]** | Browser id include-list. From &#x60;GET /api/v1/lookups/browsers&#x60;. | [optional] 
**device_id** | **List[int]** | Device-type id include-list. From &#x60;GET /api/v1/lookups/device-types&#x60;. | [optional] 
**zone** | **List[int]** | Adzone id include-list (&#x60;publisher_adzones.id&#x60;). | [optional] 
**domainids** | **List[int]** | Domain id include-list (&#x60;bigdata.domains.id&#x60;). | [optional] 
**zone_block** | **List[int]** | Adzone id exclude-list (&#x60;publisher_adzones.id&#x60;). | [optional] 
**domainids_block** | **List[int]** | Domain id exclude-list (&#x60;bigdata.domains.id&#x60;). | [optional] 
**carrier_id** | **List[int]** | Cellular carrier id include-list (&#x60;isp_carriers.id&#x60;). Only meaningful when paired with &#x60;conn_type&#x60; containing &#x60;\&quot;cellular\&quot;&#x60;.  | [optional] 
**conn_type** | **List[str]** | Connection-class include-list. | [optional] 
**lang** | **List[str]** | Two-letter ISO language code include-list (e.g. &#x60;[\&quot;en\&quot;, \&quot;de\&quot;]&#x60;). | [optional] 
**hour_start** | **int** | Inclusive start hour (0..23) of the daypart window in the rule&#39;s tz. Pair with &#x60;hour_end&#x60;. When omitted, the rule runs at any hour.  | [optional] 
**hour_end** | **int** | Inclusive end hour (0..23) of the daypart window in the rule&#39;s tz. When &#x60;hour_end &lt; hour_start&#x60; the window wraps past midnight (e.g. 18→3 &#x3D; 18:00 through 03:00 next day).  | [optional] 

## Example

```python
from goadserver.models.bid_rule_conditions import BidRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of BidRuleConditions from a JSON string
bid_rule_conditions_instance = BidRuleConditions.from_json(json)
# print the JSON string representation of the object
print(BidRuleConditions.to_json())

# convert the object into a dict
bid_rule_conditions_dict = bid_rule_conditions_instance.to_dict()
# create an instance of BidRuleConditions from a dict
bid_rule_conditions_from_dict = BidRuleConditions.from_dict(bid_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



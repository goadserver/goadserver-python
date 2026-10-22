# PushDeliveryRule

A standing, auction-driven send: every `cadence_hours` the worker picks an ad per subscriber in the target segment and delivers it. Distinct from a push campaign, which carries fixed creative content and is queued once. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**segment_id** | **int** | PushSegment id the rule targets. 0 &#x3D; the whole active audience. | [optional] 
**segment_name** | **str** | Empty when segment_id is 0. | [optional] 
**cadence_hours** | **int** | How often the rule fires. Minimum 1; defaults to 24. | [optional] 
**freq_cap_hours** | **int** | Minimum gap between two sends to the same subscriber. 0 &#x3D; uncapped. | [optional] 
**max_per_run** | **int** | Cap on subscribers reached per run. 0 &#x3D; unlimited. | [optional] 
**is_active** | **bool** |  | [optional] 
**last_run_at** | **str** | YYYY-MM-DD HH:MM, empty if the rule has never run. | [optional] 
**last_sent_count** | **int** | Deliveries accepted on the last run. | [optional] 
**last_failed_count** | **int** | Deliveries rejected by the push service on the last run. | [optional] 
**last_no_ads_count** | **int** | Subscribers skipped on the last run because the auction returned no ad. | [optional] 
**created_at** | **str** | YYYY-MM-DD HH:MM. | [optional] 

## Example

```python
from goadserver.models.push_delivery_rule import PushDeliveryRule

# TODO update the JSON string below
json = "{}"
# create an instance of PushDeliveryRule from a JSON string
push_delivery_rule_instance = PushDeliveryRule.from_json(json)
# print the JSON string representation of the object
print(PushDeliveryRule.to_json())

# convert the object into a dict
push_delivery_rule_dict = push_delivery_rule_instance.to_dict()
# create an instance of PushDeliveryRule from a dict
push_delivery_rule_from_dict = PushDeliveryRule.from_dict(push_delivery_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



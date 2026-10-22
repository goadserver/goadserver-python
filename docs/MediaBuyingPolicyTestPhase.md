# MediaBuyingPolicyTestPhase

Launch test phase: the network budget is not raised before its verdict. Set by a launch (`test_days`, default 3); `null` ends it (also after a failed verdict, to let the budget rule raise again). `days` 1-14 (the only key to send to start one on a connected zone); read-only: `from` (first judged day, set the day the zone is first seen connected), `result` (empty = running | `passed` | `failed` — raises stay held | `no_data` — less than min_spend in 3 x the days), `margin_pct`, `cost`, `revenue`, `judged_on`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | [optional] 
**var_from** | **str** |  | [optional] 
**result** | **str** |  | [optional] 
**margin_pct** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 
**judged_on** | **str** |  | [optional] 

## Example

```python
from goadserver.models.media_buying_policy_test_phase import MediaBuyingPolicyTestPhase

# TODO update the JSON string below
json = "{}"
# create an instance of MediaBuyingPolicyTestPhase from a JSON string
media_buying_policy_test_phase_instance = MediaBuyingPolicyTestPhase.from_json(json)
# print the JSON string representation of the object
print(MediaBuyingPolicyTestPhase.to_json())

# convert the object into a dict
media_buying_policy_test_phase_dict = media_buying_policy_test_phase_instance.to_dict()
# create an instance of MediaBuyingPolicyTestPhase from a dict
media_buying_policy_test_phase_from_dict = MediaBuyingPolicyTestPhase.from_dict(media_buying_policy_test_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CampaignsTypePostRequestAllOfPriority

**Priority Mode** (ron only, not offers; on networks that offer it — see `_schema`). When `on`, the campaign is served ahead of every non-priority campaign wherever it is eligible, regardless of eCPM or bid; among priority campaigns the lower `order` goes first. Either key may be sent alone — the other keeps its stored value. Not the same as `min_rank`, which is a minimum ad zone quality rank. Returned on list/show for ron campaigns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_true** | **bool** |  | [optional] [default to False]
**order** | **int** |  | [optional] [default to 1]

## Example

```python
from goadserver.models.api_v1_campaigns_type_post_request_all_of_priority import ApiV1CampaignsTypePostRequestAllOfPriority

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypePostRequestAllOfPriority from a JSON string
api_v1_campaigns_type_post_request_all_of_priority_instance = ApiV1CampaignsTypePostRequestAllOfPriority.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypePostRequestAllOfPriority.to_json())

# convert the object into a dict
api_v1_campaigns_type_post_request_all_of_priority_dict = api_v1_campaigns_type_post_request_all_of_priority_instance.to_dict()
# create an instance of ApiV1CampaignsTypePostRequestAllOfPriority from a dict
api_v1_campaigns_type_post_request_all_of_priority_from_dict = ApiV1CampaignsTypePostRequestAllOfPriority.from_dict(api_v1_campaigns_type_post_request_all_of_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



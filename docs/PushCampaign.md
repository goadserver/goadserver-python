# PushCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Internal label — not shown to subscribers. | [optional] 
**title** | **str** | Notification title. | [optional] 
**body** | **str** | Notification body. | [optional] 
**icon** | **str** | Small icon URL. | [optional] 
**image** | **str** | Large image URL. | [optional] 
**url** | **str** | Click destination. | [optional] 
**status** | **str** | Lifecycle state. Only draft / sent / failed campaigns can be (re)queued via /send. | [optional] 
**target_count** | **int** | Subscribers matched at send time. | [optional] 
**sent_count** | **int** |  | [optional] 
**fail_count** | **int** |  | [optional] 
**created_at** | **str** | YYYY-MM-DD HH:MM. | [optional] 
**sent_at** | **str** | YYYY-MM-DD HH:MM, or empty if never sent. | [optional] 

## Example

```python
from goadserver.models.push_campaign import PushCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of PushCampaign from a JSON string
push_campaign_instance = PushCampaign.from_json(json)
# print the JSON string representation of the object
print(PushCampaign.to_json())

# convert the object into a dict
push_campaign_dict = push_campaign_instance.to_dict()
# create an instance of PushCampaign from a dict
push_campaign_from_dict = PushCampaign.from_dict(push_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



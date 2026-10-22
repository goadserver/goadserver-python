# ApiV1CampaignsSaveTagsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**type** | **str** |  | [optional] [default to 'ron']
**tags** | **List[int]** |  | [optional] 
**clear** | **bool** |  | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_campaigns_save_tags_put_request import ApiV1CampaignsSaveTagsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsSaveTagsPutRequest from a JSON string
api_v1_campaigns_save_tags_put_request_instance = ApiV1CampaignsSaveTagsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsSaveTagsPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_save_tags_put_request_dict = api_v1_campaigns_save_tags_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsSaveTagsPutRequest from a dict
api_v1_campaigns_save_tags_put_request_from_dict = ApiV1CampaignsSaveTagsPutRequest.from_dict(api_v1_campaigns_save_tags_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



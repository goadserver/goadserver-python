# ApiV1CampaignsSaveCategoriesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**type** | **str** |  | [optional] [default to 'ron']
**categories** | **List[int]** |  | 
**overwrite** | **bool** |  | [optional] [default to False]

## Example

```python
from goadserver.models.api_v1_campaigns_save_categories_put_request import ApiV1CampaignsSaveCategoriesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsSaveCategoriesPutRequest from a JSON string
api_v1_campaigns_save_categories_put_request_instance = ApiV1CampaignsSaveCategoriesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsSaveCategoriesPutRequest.to_json())

# convert the object into a dict
api_v1_campaigns_save_categories_put_request_dict = api_v1_campaigns_save_categories_put_request_instance.to_dict()
# create an instance of ApiV1CampaignsSaveCategoriesPutRequest from a dict
api_v1_campaigns_save_categories_put_request_from_dict = ApiV1CampaignsSaveCategoriesPutRequest.from_dict(api_v1_campaigns_save_categories_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiPublicOfferwallIdGet200ResponseOffersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**payout** | **float** |  | [optional] 
**countries** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_public_offerwall_id_get200_response_offers_inner import ApiPublicOfferwallIdGet200ResponseOffersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPublicOfferwallIdGet200ResponseOffersInner from a JSON string
api_public_offerwall_id_get200_response_offers_inner_instance = ApiPublicOfferwallIdGet200ResponseOffersInner.from_json(json)
# print the JSON string representation of the object
print(ApiPublicOfferwallIdGet200ResponseOffersInner.to_json())

# convert the object into a dict
api_public_offerwall_id_get200_response_offers_inner_dict = api_public_offerwall_id_get200_response_offers_inner_instance.to_dict()
# create an instance of ApiPublicOfferwallIdGet200ResponseOffersInner from a dict
api_public_offerwall_id_get200_response_offers_inner_from_dict = ApiPublicOfferwallIdGet200ResponseOffersInner.from_dict(api_public_offerwall_id_get200_response_offers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



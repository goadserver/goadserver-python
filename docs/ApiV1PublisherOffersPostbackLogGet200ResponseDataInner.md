# ApiV1PublisherOffersPostbackLogGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**site_name** | **str** |  | [optional] 
**space_id** | **str** |  | [optional] 
**space_name** | **str** |  | [optional] 
**state** | **str** | HTTP status the postback URL answered with. | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** | The postback URL as fired, macros expanded. | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response_data_inner import ApiV1PublisherOffersPostbackLogGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherOffersPostbackLogGet200ResponseDataInner from a JSON string
api_v1_publisher_offers_postback_log_get200_response_data_inner_instance = ApiV1PublisherOffersPostbackLogGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherOffersPostbackLogGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_publisher_offers_postback_log_get200_response_data_inner_dict = api_v1_publisher_offers_postback_log_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1PublisherOffersPostbackLogGet200ResponseDataInner from a dict
api_v1_publisher_offers_postback_log_get200_response_data_inner_from_dict = ApiV1PublisherOffersPostbackLogGet200ResponseDataInner.from_dict(api_v1_publisher_offers_postback_log_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



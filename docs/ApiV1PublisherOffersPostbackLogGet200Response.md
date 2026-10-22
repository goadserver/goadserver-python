# ApiV1PublisherOffersPostbackLogGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1PublisherOffersPostbackLogGet200ResponseDataInner]**](ApiV1PublisherOffersPostbackLogGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response import ApiV1PublisherOffersPostbackLogGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherOffersPostbackLogGet200Response from a JSON string
api_v1_publisher_offers_postback_log_get200_response_instance = ApiV1PublisherOffersPostbackLogGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherOffersPostbackLogGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_offers_postback_log_get200_response_dict = api_v1_publisher_offers_postback_log_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherOffersPostbackLogGet200Response from a dict
api_v1_publisher_offers_postback_log_get200_response_from_dict = ApiV1PublisherOffersPostbackLogGet200Response.from_dict(api_v1_publisher_offers_postback_log_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



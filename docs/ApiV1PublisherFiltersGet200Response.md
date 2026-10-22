# ApiV1PublisherFiltersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | [**List[ApiV1PublisherFiltersGet200ResponseUrlsInner]**](ApiV1PublisherFiltersGet200ResponseUrlsInner.md) |  | [optional] 
**categories** | [**List[ApiV1PublisherFiltersGet200ResponseCategoriesInner]**](ApiV1PublisherFiltersGet200ResponseCategoriesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_filters_get200_response import ApiV1PublisherFiltersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFiltersGet200Response from a JSON string
api_v1_publisher_filters_get200_response_instance = ApiV1PublisherFiltersGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFiltersGet200Response.to_json())

# convert the object into a dict
api_v1_publisher_filters_get200_response_dict = api_v1_publisher_filters_get200_response_instance.to_dict()
# create an instance of ApiV1PublisherFiltersGet200Response from a dict
api_v1_publisher_filters_get200_response_from_dict = ApiV1PublisherFiltersGet200Response.from_dict(api_v1_publisher_filters_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



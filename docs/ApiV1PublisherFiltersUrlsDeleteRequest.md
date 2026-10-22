# ApiV1PublisherFiltersUrlsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_filters_urls_delete_request import ApiV1PublisherFiltersUrlsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFiltersUrlsDeleteRequest from a JSON string
api_v1_publisher_filters_urls_delete_request_instance = ApiV1PublisherFiltersUrlsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFiltersUrlsDeleteRequest.to_json())

# convert the object into a dict
api_v1_publisher_filters_urls_delete_request_dict = api_v1_publisher_filters_urls_delete_request_instance.to_dict()
# create an instance of ApiV1PublisherFiltersUrlsDeleteRequest from a dict
api_v1_publisher_filters_urls_delete_request_from_dict = ApiV1PublisherFiltersUrlsDeleteRequest.from_dict(api_v1_publisher_filters_urls_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



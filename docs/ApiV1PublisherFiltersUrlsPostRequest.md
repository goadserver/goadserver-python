# ApiV1PublisherFiltersUrlsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_filters_urls_post_request import ApiV1PublisherFiltersUrlsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFiltersUrlsPostRequest from a JSON string
api_v1_publisher_filters_urls_post_request_instance = ApiV1PublisherFiltersUrlsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFiltersUrlsPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_filters_urls_post_request_dict = api_v1_publisher_filters_urls_post_request_instance.to_dict()
# create an instance of ApiV1PublisherFiltersUrlsPostRequest from a dict
api_v1_publisher_filters_urls_post_request_from_dict = ApiV1PublisherFiltersUrlsPostRequest.from_dict(api_v1_publisher_filters_urls_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



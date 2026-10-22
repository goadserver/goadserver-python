# ApiV1PublisherPushSetupGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_domain** | **str** | Network ad host the collector + SW are served from. | [optional] 
**sw_path** | **str** |  | [optional] 
**subscriber_total** | **int** |  | [optional] 
**subscriber_active** | **int** |  | [optional] 
**adzones** | [**List[ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner]**](ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_setup_get200_response_data import ApiV1PublisherPushSetupGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSetupGet200ResponseData from a JSON string
api_v1_publisher_push_setup_get200_response_data_instance = ApiV1PublisherPushSetupGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSetupGet200ResponseData.to_json())

# convert the object into a dict
api_v1_publisher_push_setup_get200_response_data_dict = api_v1_publisher_push_setup_get200_response_data_instance.to_dict()
# create an instance of ApiV1PublisherPushSetupGet200ResponseData from a dict
api_v1_publisher_push_setup_get200_response_data_from_dict = ApiV1PublisherPushSetupGet200ResponseData.from_dict(api_v1_publisher_push_setup_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



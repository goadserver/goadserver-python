# ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**domain** | **str** | The site&#39;s own ad domain when set, else the network default. | [optional] 
**subscribers** | **int** |  | [optional] 
**last_optin** | **str** | YYYY-MM-DD HH:MM, empty when the zone has none. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_push_setup_get200_response_data_adzones_inner import ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner from a JSON string
api_v1_publisher_push_setup_get200_response_data_adzones_inner_instance = ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner.to_json())

# convert the object into a dict
api_v1_publisher_push_setup_get200_response_data_adzones_inner_dict = api_v1_publisher_push_setup_get200_response_data_adzones_inner_instance.to_dict()
# create an instance of ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner from a dict
api_v1_publisher_push_setup_get200_response_data_adzones_inner_from_dict = ApiV1PublisherPushSetupGet200ResponseDataAdzonesInner.from_dict(api_v1_publisher_push_setup_get200_response_data_adzones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



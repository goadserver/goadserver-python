# ApiV1XmlFeedsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** | Feed URL. | [optional] 
**itemspath** | **str** |  | [optional] 
**titlepath** | **str** |  | [optional] 
**descriptionpath** | **str** |  | [optional] 
**mediapath** | **str** |  | [optional] 
**linkpath** | **str** |  | [optional] 
**revisitminutes** | **int** |  | [optional] [default to 5]

## Example

```python
from goadserver.models.api_v1_xml_feeds_post_request import ApiV1XmlFeedsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1XmlFeedsPostRequest from a JSON string
api_v1_xml_feeds_post_request_instance = ApiV1XmlFeedsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1XmlFeedsPostRequest.to_json())

# convert the object into a dict
api_v1_xml_feeds_post_request_dict = api_v1_xml_feeds_post_request_instance.to_dict()
# create an instance of ApiV1XmlFeedsPostRequest from a dict
api_v1_xml_feeds_post_request_from_dict = ApiV1XmlFeedsPostRequest.from_dict(api_v1_xml_feeds_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



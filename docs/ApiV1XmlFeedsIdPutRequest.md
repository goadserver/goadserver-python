# ApiV1XmlFeedsIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**itemspath** | **str** |  | [optional] 
**titlepath** | **str** |  | [optional] 
**descriptionpath** | **str** |  | [optional] 
**mediapath** | **str** |  | [optional] 
**linkpath** | **str** |  | [optional] 
**revisitminutes** | **int** |  | [optional] 
**isactive** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_xml_feeds_id_put_request import ApiV1XmlFeedsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1XmlFeedsIdPutRequest from a JSON string
api_v1_xml_feeds_id_put_request_instance = ApiV1XmlFeedsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1XmlFeedsIdPutRequest.to_json())

# convert the object into a dict
api_v1_xml_feeds_id_put_request_dict = api_v1_xml_feeds_id_put_request_instance.to_dict()
# create an instance of ApiV1XmlFeedsIdPutRequest from a dict
api_v1_xml_feeds_id_put_request_from_dict = ApiV1XmlFeedsIdPutRequest.from_dict(api_v1_xml_feeds_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CreativesIdPutRequestTags

Tag ids from the tenant tag list (`tags` in the creatives setup data): an array of ids, or a comma-separated string. Replaces the current tags; [] clears them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from goadserver.models.api_v1_creatives_id_put_request_tags import ApiV1CreativesIdPutRequestTags

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativesIdPutRequestTags from a JSON string
api_v1_creatives_id_put_request_tags_instance = ApiV1CreativesIdPutRequestTags.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativesIdPutRequestTags.to_json())

# convert the object into a dict
api_v1_creatives_id_put_request_tags_dict = api_v1_creatives_id_put_request_tags_instance.to_dict()
# create an instance of ApiV1CreativesIdPutRequestTags from a dict
api_v1_creatives_id_put_request_tags_from_dict = ApiV1CreativesIdPutRequestTags.from_dict(api_v1_creatives_id_put_request_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1CreativesBulkMovePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | Destination folder; 0 unfiles. | 
**ids** | **List[int]** |  | [optional] 
**filter** | **Dict[str, str]** | Listing filter params, as strings. | [optional] 

## Example

```python
from goadserver.models.api_v1_creatives_bulk_move_post_request import ApiV1CreativesBulkMovePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativesBulkMovePostRequest from a JSON string
api_v1_creatives_bulk_move_post_request_instance = ApiV1CreativesBulkMovePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativesBulkMovePostRequest.to_json())

# convert the object into a dict
api_v1_creatives_bulk_move_post_request_dict = api_v1_creatives_bulk_move_post_request_instance.to_dict()
# create an instance of ApiV1CreativesBulkMovePostRequest from a dict
api_v1_creatives_bulk_move_post_request_from_dict = ApiV1CreativesBulkMovePostRequest.from_dict(api_v1_creatives_bulk_move_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



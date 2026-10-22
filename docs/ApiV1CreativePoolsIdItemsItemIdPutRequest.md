# ApiV1CreativePoolsIdItemsItemIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**properties** | **str** |  | [optional] 
**ratingid** | **int** |  | [optional] 
**url_prefix** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**is_fallback** | **bool** | Serve only while no other item of this pool + size is live. | [optional] 
**start_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestStartAt.md) |  | [optional] 
**end_at** | [**ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt**](ApiV1CreativePoolsIdItemsItemIdPutRequestEndAt.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request import ApiV1CreativePoolsIdItemsItemIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CreativePoolsIdItemsItemIdPutRequest from a JSON string
api_v1_creative_pools_id_items_item_id_put_request_instance = ApiV1CreativePoolsIdItemsItemIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1CreativePoolsIdItemsItemIdPutRequest.to_json())

# convert the object into a dict
api_v1_creative_pools_id_items_item_id_put_request_dict = api_v1_creative_pools_id_items_item_id_put_request_instance.to_dict()
# create an instance of ApiV1CreativePoolsIdItemsItemIdPutRequest from a dict
api_v1_creative_pools_id_items_item_id_put_request_from_dict = ApiV1CreativePoolsIdItemsItemIdPutRequest.from_dict(api_v1_creative_pools_id_items_item_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



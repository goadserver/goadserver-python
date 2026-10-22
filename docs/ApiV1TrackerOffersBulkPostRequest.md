# ApiV1TrackerOffersBulkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**ids** | **List[int]** |  | 

## Example

```python
from goadserver.models.api_v1_tracker_offers_bulk_post_request import ApiV1TrackerOffersBulkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerOffersBulkPostRequest from a JSON string
api_v1_tracker_offers_bulk_post_request_instance = ApiV1TrackerOffersBulkPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerOffersBulkPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_offers_bulk_post_request_dict = api_v1_tracker_offers_bulk_post_request_instance.to_dict()
# create an instance of ApiV1TrackerOffersBulkPostRequest from a dict
api_v1_tracker_offers_bulk_post_request_from_dict = ApiV1TrackerOffersBulkPostRequest.from_dict(api_v1_tracker_offers_bulk_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



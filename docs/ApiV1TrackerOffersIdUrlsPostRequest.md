# ApiV1TrackerOffersIdUrlsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**sort_weight** | **int** | Rotation weight relative to the offer&#39;s other URLs. | [optional] 
**is_active** | **bool** | Defaults to true. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_offers_id_urls_post_request import ApiV1TrackerOffersIdUrlsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerOffersIdUrlsPostRequest from a JSON string
api_v1_tracker_offers_id_urls_post_request_instance = ApiV1TrackerOffersIdUrlsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerOffersIdUrlsPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_offers_id_urls_post_request_dict = api_v1_tracker_offers_id_urls_post_request_instance.to_dict()
# create an instance of ApiV1TrackerOffersIdUrlsPostRequest from a dict
api_v1_tracker_offers_id_urls_post_request_from_dict = ApiV1TrackerOffersIdUrlsPostRequest.from_dict(api_v1_tracker_offers_id_urls_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



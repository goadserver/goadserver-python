# ApiV1TrackerOffersIdUrlsUrlIdPutRequest

Writes only the fields sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**sort_weight** | **int** | Rotation weight relative to the offer&#39;s other URLs. | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_offers_id_urls_url_id_put_request import ApiV1TrackerOffersIdUrlsUrlIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerOffersIdUrlsUrlIdPutRequest from a JSON string
api_v1_tracker_offers_id_urls_url_id_put_request_instance = ApiV1TrackerOffersIdUrlsUrlIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerOffersIdUrlsUrlIdPutRequest.to_json())

# convert the object into a dict
api_v1_tracker_offers_id_urls_url_id_put_request_dict = api_v1_tracker_offers_id_urls_url_id_put_request_instance.to_dict()
# create an instance of ApiV1TrackerOffersIdUrlsUrlIdPutRequest from a dict
api_v1_tracker_offers_id_urls_url_id_put_request_from_dict = ApiV1TrackerOffersIdUrlsUrlIdPutRequest.from_dict(api_v1_tracker_offers_id_urls_url_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



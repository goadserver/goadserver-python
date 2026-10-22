# ApiV1TrackerAdNetworksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**networkid** | **int** | Id of the network&#39;s reporting integration; 0 &#x3D; none. | [optional] 
**currency** | **str** | Three-letter currency the network reports in, lower-case (e.g. usd). | [optional] 
**apikey** | **str** | Credential for the network&#39;s reporting API, when it has one. | [optional] 
**api_data** | **str** | Extra API settings as a JSON string (per-network fields): &#x60;{\&quot;username\&quot;}&#x60; for traforama (the account e-mail); &#x60;{\&quot;username\&quot;,\&quot;password\&quot;}&#x60; for bidvertiser (the Bidvertiser login - its API needs it next to &#x60;apikey&#x60; for its access token). | [optional] 
**low_balance_threshold** | **float** | Low-balance alert line in the account&#39;s currency; 0 &#x3D; off. | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_ad_networks_post_request import ApiV1TrackerAdNetworksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerAdNetworksPostRequest from a JSON string
api_v1_tracker_ad_networks_post_request_instance = ApiV1TrackerAdNetworksPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerAdNetworksPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_ad_networks_post_request_dict = api_v1_tracker_ad_networks_post_request_instance.to_dict()
# create an instance of ApiV1TrackerAdNetworksPostRequest from a dict
api_v1_tracker_ad_networks_post_request_from_dict = ApiV1TrackerAdNetworksPostRequest.from_dict(api_v1_tracker_ad_networks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



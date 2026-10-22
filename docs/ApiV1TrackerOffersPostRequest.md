# ApiV1TrackerOffersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**destination_url** | **str** | Landing URL. Creates the offer&#39;s first URL row when the offer is created. | [optional] 
**urls** | [**List[ApiV1TrackerOffersPostRequestUrlsInner]**](ApiV1TrackerOffersPostRequestUrlsInner.md) | Multiple landing URLs with rotation weights. Use instead of destination_url for a rotator. | [optional] 
**payout** | **float** | Fixed payout per conversion, in account currency. | [optional] 
**revshare_pct** | **float** | Revenue share percentage, when the offer pays a share rather than a fixed amount. | [optional] 
**paytype** | **str** | Payout model — fixed CPA or revshare. | [optional] 
**conv_type** | **str** | Conversion type letter (A–Z) this offer settles against. See /conversion-types. | [optional] 
**country** | **str** | Comma-separated country codes the offer targets. Empty &#x3D; worldwide. | [optional] 
**affiliate_network_id** | **int** | Owning affiliate network (see /affiliate-networks). 0 &#x3D; none. | [optional] 
**failover_offer_id** | **int** | Offer to redirect to once this one caps out. 0 &#x3D; none. | [optional] 
**daily_cap** | **int** | Conversions per day before the offer stops serving. 0 &#x3D; uncapped. | [optional] 
**total_cap** | **int** | Lifetime conversion cap. 0 &#x3D; uncapped. | [optional] 
**notes** | **str** |  | [optional] 
**paused** | **bool** |  | [optional] 
**as_failover** | **bool** | Mark the offer as a failover-only destination — it is not picked directly. | [optional] 
**tags** | **str** | Comma-separated tracker tags. | [optional] 
**offertypeid** | **int** |  | [optional] 
**regionids** | **List[int]** |  | [optional] 
**device_type_ids** | **List[int]** |  | [optional] 
**osids** | **List[int]** |  | [optional] 
**browserids** | **List[int]** |  | [optional] 
**carrierids** | **List[int]** |  | [optional] 
**ispids** | **List[int]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_tracker_offers_post_request import ApiV1TrackerOffersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TrackerOffersPostRequest from a JSON string
api_v1_tracker_offers_post_request_instance = ApiV1TrackerOffersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TrackerOffersPostRequest.to_json())

# convert the object into a dict
api_v1_tracker_offers_post_request_dict = api_v1_tracker_offers_post_request_instance.to_dict()
# create an instance of ApiV1TrackerOffersPostRequest from a dict
api_v1_tracker_offers_post_request_from_dict = ApiV1TrackerOffersPostRequest.from_dict(api_v1_tracker_offers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



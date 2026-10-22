# ApiV1PublisherSspCampaignsIdTestRtbPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_type** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**page_url** | **str** |  | [optional] 
**bidfloor** | **float** | CPM floor in currency units. | [optional] 
**tmax** | **int** | Milliseconds. | [optional] 
**currency** | **str** |  | [optional] 
**secure** | **int** |  | [optional] 
**user_ua** | **str** |  | [optional] 
**user_ip** | **str** |  | [optional] 
**override_url** | **str** | Test this URL instead of the campaign&#39;s stored one. | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_ssp_campaigns_id_test_rtb_post_request import ApiV1PublisherSspCampaignsIdTestRtbPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSspCampaignsIdTestRtbPostRequest from a JSON string
api_v1_publisher_ssp_campaigns_id_test_rtb_post_request_instance = ApiV1PublisherSspCampaignsIdTestRtbPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSspCampaignsIdTestRtbPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_ssp_campaigns_id_test_rtb_post_request_dict = api_v1_publisher_ssp_campaigns_id_test_rtb_post_request_instance.to_dict()
# create an instance of ApiV1PublisherSspCampaignsIdTestRtbPostRequest from a dict
api_v1_publisher_ssp_campaigns_id_test_rtb_post_request_from_dict = ApiV1PublisherSspCampaignsIdTestRtbPostRequest.from_dict(api_v1_publisher_ssp_campaigns_id_test_rtb_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



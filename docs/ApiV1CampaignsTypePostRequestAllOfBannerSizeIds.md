# ApiV1CampaignsTypePostRequestAllOfBannerSizeIds

`type=rtb` only: the banner sizes the campaign bids on — comma-separated banner size ids, or a JSON array of ids. **Required for banner rtb campaigns (`ad_type: 2`)**; ignored for the other ad types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from goadserver.models.api_v1_campaigns_type_post_request_all_of_banner_size_ids import ApiV1CampaignsTypePostRequestAllOfBannerSizeIds

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1CampaignsTypePostRequestAllOfBannerSizeIds from a JSON string
api_v1_campaigns_type_post_request_all_of_banner_size_ids_instance = ApiV1CampaignsTypePostRequestAllOfBannerSizeIds.from_json(json)
# print the JSON string representation of the object
print(ApiV1CampaignsTypePostRequestAllOfBannerSizeIds.to_json())

# convert the object into a dict
api_v1_campaigns_type_post_request_all_of_banner_size_ids_dict = api_v1_campaigns_type_post_request_all_of_banner_size_ids_instance.to_dict()
# create an instance of ApiV1CampaignsTypePostRequestAllOfBannerSizeIds from a dict
api_v1_campaigns_type_post_request_all_of_banner_size_ids_from_dict = ApiV1CampaignsTypePostRequestAllOfBannerSizeIds.from_dict(api_v1_campaigns_type_post_request_all_of_banner_size_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



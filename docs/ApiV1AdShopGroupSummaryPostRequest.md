# ApiV1AdShopGroupSummaryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** |  | [optional] 
**group** | **str** | Single-dimension shorthand for groups. | [optional] 
**selected_ids** | **List[int]** | Opportunity ids to total as selected. | [optional] 
**filters** | [**ApiV1AdShopGroupSummaryPostRequestFilters**](ApiV1AdShopGroupSummaryPostRequestFilters.md) |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_shop_group_summary_post_request import ApiV1AdShopGroupSummaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdShopGroupSummaryPostRequest from a JSON string
api_v1_ad_shop_group_summary_post_request_instance = ApiV1AdShopGroupSummaryPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdShopGroupSummaryPostRequest.to_json())

# convert the object into a dict
api_v1_ad_shop_group_summary_post_request_dict = api_v1_ad_shop_group_summary_post_request_instance.to_dict()
# create an instance of ApiV1AdShopGroupSummaryPostRequest from a dict
api_v1_ad_shop_group_summary_post_request_from_dict = ApiV1AdShopGroupSummaryPostRequest.from_dict(api_v1_ad_shop_group_summary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



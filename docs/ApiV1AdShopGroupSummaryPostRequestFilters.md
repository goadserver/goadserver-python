# ApiV1AdShopGroupSummaryPostRequestFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | **List[int]** |  | [optional] 
**pay_types** | **List[int]** |  | [optional] 
**categories** | **List[int]** |  | [optional] 
**devices** | **List[int]** |  | [optional] 
**countries** | **List[str]** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_ad_shop_group_summary_post_request_filters import ApiV1AdShopGroupSummaryPostRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdShopGroupSummaryPostRequestFilters from a JSON string
api_v1_ad_shop_group_summary_post_request_filters_instance = ApiV1AdShopGroupSummaryPostRequestFilters.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdShopGroupSummaryPostRequestFilters.to_json())

# convert the object into a dict
api_v1_ad_shop_group_summary_post_request_filters_dict = api_v1_ad_shop_group_summary_post_request_filters_instance.to_dict()
# create an instance of ApiV1AdShopGroupSummaryPostRequestFilters from a dict
api_v1_ad_shop_group_summary_post_request_filters_from_dict = ApiV1AdShopGroupSummaryPostRequestFilters.from_dict(api_v1_ad_shop_group_summary_post_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



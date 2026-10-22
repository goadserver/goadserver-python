# ApiV1FiltersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FilterType**](FilterType.md) |  | 
**name** | **str** | HTML tags are stripped; unique per type. | 
**items** | **List[str]** | Required for every type but ip. | [optional] 
**campaign_ids** | **List[int]** | See Campaign scope above. Empty/omitted &#x3D; no campaign link (block lists: every campaign of ad_type). | [optional] 
**campaign_type** | **str** | Block lists: the kind of the campaign_ids. Default ron (rtb when ad_type is 14). | [optional] 
**ad_type** | **int** | Block lists and domain_incl: 0 &#x3D; all ad types / every campaign, otherwise the adtypeid this filter applies to. | [optional] [default to 0]
**ip_list** | **str** | type&#x3D;ip only: ranges, one per line. | [optional] 

## Example

```python
from goadserver.models.api_v1_filters_post_request import ApiV1FiltersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FiltersPostRequest from a JSON string
api_v1_filters_post_request_instance = ApiV1FiltersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FiltersPostRequest.to_json())

# convert the object into a dict
api_v1_filters_post_request_dict = api_v1_filters_post_request_instance.to_dict()
# create an instance of ApiV1FiltersPostRequest from a dict
api_v1_filters_post_request_from_dict = ApiV1FiltersPostRequest.from_dict(api_v1_filters_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



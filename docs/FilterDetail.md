# FilterDetail

One filter. GET, create (201), PUT and POST …/items all answer with this shape. SubIDs are shown ENCODED when the account has SubID encoding on (send them back the same way). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**ad_type** | **int** | 0 &#x3D; applies to all ad types, otherwise the adtypeid this filter targets. | [optional] 
**item_count** | **int** | Number of items (domains/ISPs/etc.) currently in the filter. | [optional] 
**items** | **List[str]** | Domain IDs / adzone IDs / ISP IDs / SubID strings — depends on filter type. Not present for &#x60;ip&#x60; (see ranges). | [optional] 
**campaign_ids** | **List[str]** | Block lists (&#x60;*_excl&#x60;): the campaigns in the filter&#39;s own list — read it together with &#x60;applies_to&#x60;. Allow-lists (&#x60;*_incl&#x60;) and &#x60;ip&#x60;: the RON campaigns whose allow-list / IP pool is this filter.  | [optional] 
**campaign_type** | **str** | Block lists only: which campaign kind the listed ids are. | [optional] 
**applies_to** | **str** | Block lists only — what the ad server does with the row: &#x60;ad_type&#x60; 0 blocks across every campaign (campaign_ids are ignored); &#x60;ad_type&#x60; &gt; 0 with no campaign_ids covers every campaign of that ad type; otherwise only the listed ones.  | [optional] 
**ranges** | [**List[FilterDetailAllOfRanges]**](FilterDetailAllOfRanges.md) | IP ranges with their captured IP counts. (&#x60;type&#x3D;ip&#x60; only.) &#x60;range&#x60; is a display string — either a single address or &#x60;start - end&#x60;; &#x60;ip_start&#x60; / &#x60;ip_end&#x60; carry the bounds separately. &#x60;id&#x60; addresses the range in the /ranges/{rangeId} and /items/{item} routes. | [optional] 
**imported** | **int** | &#x60;type&#x3D;ip&#x60; writes only: ranges imported by this call. | [optional] 

## Example

```python
from goadserver.models.filter_detail import FilterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDetail from a JSON string
filter_detail_instance = FilterDetail.from_json(json)
# print the JSON string representation of the object
print(FilterDetail.to_json())

# convert the object into a dict
filter_detail_dict = filter_detail_instance.to_dict()
# create an instance of FilterDetail from a dict
filter_detail_from_dict = FilterDetail.from_dict(filter_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



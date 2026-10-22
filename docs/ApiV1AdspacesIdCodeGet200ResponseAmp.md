# ApiV1AdspacesIdCodeGet200ResponseAmp

Banner, native, reel and creator widget zones: AMP page and Web Story code (see above).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_url** | **str** | The JSON endpoint behind both snippets (goadserver /ampad.go). | [optional] 
**head** | **str** | AMP page: scripts for &lt;head&gt; (amp-list, amp-mustache, amp-video for reels/creators). | [optional] 
**amp_ad** | **str** | AMP page: the &lt;amp-list&gt; with its amp-mustache template, placed where the ad goes. | [optional] 
**story_head** | **str** | Web Story: scripts for &lt;head&gt; (amp-list, amp-mustache). | [optional] 
**story** | **str** | Web Story: a sponsored &lt;amp-story-page&gt; (full-screen image, Sponsored label, Learn more link), pasted inside &lt;amp-story&gt; between the story&#39;s pages. | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_code_get200_response_amp import ApiV1AdspacesIdCodeGet200ResponseAmp

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdCodeGet200ResponseAmp from a JSON string
api_v1_adspaces_id_code_get200_response_amp_instance = ApiV1AdspacesIdCodeGet200ResponseAmp.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdCodeGet200ResponseAmp.to_json())

# convert the object into a dict
api_v1_adspaces_id_code_get200_response_amp_dict = api_v1_adspaces_id_code_get200_response_amp_instance.to_dict()
# create an instance of ApiV1AdspacesIdCodeGet200ResponseAmp from a dict
api_v1_adspaces_id_code_get200_response_amp_from_dict = ApiV1AdspacesIdCodeGet200ResponseAmp.from_dict(api_v1_adspaces_id_code_get200_response_amp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



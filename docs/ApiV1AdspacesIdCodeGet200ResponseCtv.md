# ApiV1AdspacesIdCodeGet200ResponseCtv

Video (4) and audio (43) zones: the ad server's player URLs. [MACROS] are IAB VAST 4.1 macros the player fills (app bundle, store URL, advertising id, limit-ad-tracking, CCPA string); the app bundle becomes the request's domain for targeting, blocklists and stats, and goes to DSPs as app.bundle. ssai=1 with the viewer's ip and user agent is honoured only on zones with player_settings.ssai (else 403). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vast** | **str** | VAST for one ad (or player_settings.pod_size ads). | [optional] 
**pod** | **str** | An ad pod of 3: &lt;Ad sequence&#x3D;1..3&gt;, no campaign or advertiser twice, at most pod_max_seconds. | [optional] 
**vmap** | **str** | VMAP 1.0 of the zone&#39;s breaks (pre-roll unless vmap_no_preroll, midroll_offsets, post-roll with vmap_postroll); each AdTagURI is this zone&#39;s VAST with the pod size. | [optional] 
**pause** | **str** | Pause ad as JSON {ad: {image, width, height, click_url, impression_url}} or {ad: null}; fire impression_url when shown. | [optional] 
**pause_vast** | **str** | The same pause ad as VAST 3 NonLinear (StaticResource + NonLinearClickThrough). | [optional] 
**ssai** | **str** | Server-side ad insertion: replace {viewer_ip} and {viewer_user_agent}. | [optional] 

## Example

```python
from goadserver.models.api_v1_adspaces_id_code_get200_response_ctv import ApiV1AdspacesIdCodeGet200ResponseCtv

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdspacesIdCodeGet200ResponseCtv from a JSON string
api_v1_adspaces_id_code_get200_response_ctv_instance = ApiV1AdspacesIdCodeGet200ResponseCtv.from_json(json)
# print the JSON string representation of the object
print(ApiV1AdspacesIdCodeGet200ResponseCtv.to_json())

# convert the object into a dict
api_v1_adspaces_id_code_get200_response_ctv_dict = api_v1_adspaces_id_code_get200_response_ctv_instance.to_dict()
# create an instance of ApiV1AdspacesIdCodeGet200ResponseCtv from a dict
api_v1_adspaces_id_code_get200_response_ctv_from_dict = ApiV1AdspacesIdCodeGet200ResponseCtv.from_dict(api_v1_adspaces_id_code_get200_response_ctv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



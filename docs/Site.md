# Site

Full site record returned by `GET /api/v1/sites/{id}`. Body shape is round-trippable with `SiteCreate` plus read-only fields (`id`, `domainid`, `is_verified`, `is_deleted`, `date_added`, and the review state `sitestate` / `sitestate_name` / `isvalid` / `rejectedreason`, which only staff change). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**typeid** | **int** |  | [optional] 
**main_catid** | **int** |  | [optional] 
**categories** | **List[int]** |  | [optional] 
**sitelanguages** | **List[str]** |  | [optional] 
**postbacks** | **object** |  | [optional] 
**ad_domainid** | **int** |  | [optional] 
**domainid** | **int** | Resolved tracker_domains.id for the site URL. | [optional] 
**is_verified** | **bool** | True after the publisher completes the verification flow. | [optional] 
**is_deleted** | **bool** |  | [optional] 
**date_added** | **date** |  | [optional] 
**tags** | **List[int]** | Site groups (campaign_groups ids). | [optional] 
**sitestate** | **int** | Review state: 1 &#x3D; validated, 0 &#x3D; pending review, -1 &#x3D; rejected. | [optional] 
**sitestate_name** | **str** |  | [optional] 
**isvalid** | **bool** | Approved by staff (or auto-validated). | [optional] 
**rejectedreason** | **str** | Why staff rejected the site (meaningful when sitestate &#x3D; -1). | [optional] 
**isapp** | **bool** | A mobile app (see SiteCreate.isapp); url is then its .inapp pseudo-domain. | [optional] 
**app_bundle** | **str** |  | [optional] 
**app_store_url** | **str** |  | [optional] 
**app_platform** | **str** |  | [optional] 
**verify_code** | **str** | MD5 of (userid + \&quot;_\&quot; + url) — the unique token the publisher must include in the verify meta tag. Only present when need_verification is on. | [optional] 
**verify_tag_prefix** | **str** | Tag-name prefix the verify meta tag uses (default \&quot;ero_verify\&quot;). Only present when need_verification is on. | [optional] 
**verify_meta_tag** | **str** | Pre-rendered &lt;meta&gt; tag the publisher pastes on the site root before POSTing /verify. Only present when need_verification is on. | [optional] 

## Example

```python
from goadserver.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print(Site.to_json())

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_from_dict = Site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



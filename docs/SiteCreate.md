# SiteCreate

Site (publisher_sites) create body. Required: `name` + `url`. Module-gated fields become required when their module is active on the tenant — see `GET /api/v1/sites/_schema`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | 
**description** | **str** |  | [optional] 
**main_catid** | **int** | Main-category id from /api/v1/lookups/main-categories. | [optional] [default to 1]
**typeid** | **int** | Website-type id from /api/v1/lookups/website-types. Module-gated. | [optional] [default to 0]
**categories** | **List[int]** | Category ids from /api/v1/lookups/categories. Module-gated (modules.global.categories). | [optional] 
**sitelanguages** | **List[str]** | ISO language codes from /api/v1/lookups/website-languages. Module-gated (modules.global.website_languages). | [optional] 
**postbacks** | **List[Dict[str, object]]** | Per-event postback URLs. Module-gated (modules.publisher.postbacks). | [optional] 
**ad_domainid** | **int** | Ad-domain id when the tenant uses a separate ad-serving domain. | [optional] [default to 0]
**tags** | **List[int]** | Site groups (campaign_groups ids). A zone with no groups of its own inherits these. | [optional] 
**isapp** | **bool** | A mobile app instead of a website (in-app ads through Prebid Mobile or an SSP&#39;s OpenRTB app requests, docs/IN_APP.md). &#x60;url&#x60; is then set by the server to https://&lt;bundle pseudo-domain&gt;.inapp (lowercase, other characters → &#39;-&#39;, e.g. com.example.game → com-example-game.inapp) — the address the ad server runs the app&#39;s traffic under — and the site skips the verification meta tag (publish the ads.txt line as app-ads.txt on the developer website). Campaign domain filters and blocklists take apps as &#x60;app:&lt;bundle&gt;&#x60;. | [optional] [default to False]
**app_bundle** | **str** | With isapp (required): the bundle the SDK sends as app.bundle — Android package name, iOS bundle id or numeric App Store id. | [optional] 
**app_store_url** | **str** | With isapp: the store page (http/https). | [optional] 
**app_platform** | **str** | With isapp; guessed from app_store_url when omitted. | [optional] 

## Example

```python
from goadserver.models.site_create import SiteCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteCreate from a JSON string
site_create_instance = SiteCreate.from_json(json)
# print the JSON string representation of the object
print(SiteCreate.to_json())

# convert the object into a dict
site_create_dict = site_create_instance.to_dict()
# create an instance of SiteCreate from a dict
site_create_from_dict = SiteCreate.from_dict(site_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



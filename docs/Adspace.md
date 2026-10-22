# Adspace

Full adspace record returned by `GET /api/v1/adspaces/{id}` and the create/update endpoints. Shape mirrors `AdspaceCreate` so round-trips work without translation, plus a few read-only identity fields (`id`, `uniq_name`, `adspace_type`, `is_active`, `date_added`, `time_changed`) and the parsed `json_settings`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**uniq_name** | **str** | MD5 of (name, type, system, site) — internal dedupe key. | [optional] 
**site** | [**AdspaceSite**](AdspaceSite.md) |  | [optional] 
**siteid** | **int** |  | [optional] 
**adspace_type** | **str** | Type config key (e.g. bannerads). | [optional] 
**adzone_typeid** | **int** |  | [optional] 
**adtype_id** | **int** |  | [optional] 
**ad_type** | **int** | Backward-compat alias for adtype_id. | [optional] 
**adsizeid** | **int** |  | [optional] 
**display_type** | **int** |  | [optional] 
**ratingid** | **int** |  | [optional] 
**main_catid** | **int** |  | [optional] 
**catid** | **int** |  | [optional] 
**locationid** | **int** |  | [optional] 
**quality_rank** | **int** |  | [optional] 
**is_active** | **bool** | Derived from publisher_adzones.isinuse — true when at least one campaign-spot link exists. | [optional] 
**autoapprove** | **bool** |  | [optional] 
**isvisible** | **bool** |  | [optional] 
**sendmails** | **bool** |  | [optional] 
**useownbanners** | **bool** |  | [optional] 
**usealtbanner** | **bool** |  | [optional] 
**usecpmbuys** | **bool** |  | [optional] 
**allow_iframes** | **bool** |  | [optional] 
**allow_animation** | **bool** |  | [optional] 
**run_rtb_after_smartzone** | **bool** |  | [optional] 
**use_pixel_log** | **bool** |  | [optional] 
**show_about** | **bool** |  | [optional] 
**skip_ron_if_cpm** | **bool** |  | [optional] 
**no_promotion** | **bool** |  | [optional] 
**hidecopy** | **bool** |  | [optional] 
**use_subid_list** | **bool** |  | [optional] 
**subid_list** | **str** |  | [optional] 
**use_domain_list** | **bool** |  | [optional] 
**domain_list** | **List[str]** |  | [optional] 
**use_costs** | **bool** |  | [optional] 
**costs_data** | **Dict[str, object]** |  | [optional] 
**use_dynamic_costs** | **bool** |  | [optional] 
**use_fixed_payouts** | **bool** |  | [optional] 
**fixed_payout_data** | **Dict[str, object]** |  | [optional] 
**use_fallback_campaign** | **bool** |  | [optional] 
**fallback_campaignid** | **int** |  | [optional] 
**excl_catids** | **str** |  | [optional] 
**exclproperties** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**rtb_name** | **str** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**time_changed** | **int** | Unix seconds of last update. | [optional] 
**useflatbuys** | **bool** |  | [optional] 
**only_wl_campaigns** | **bool** |  | [optional] 
**only_tagged_campaigns** | **bool** |  | [optional] 
**force_wl_targeting** | **bool** |  | [optional] 
**skip_rtb_when_wl** | **bool** | From json_settings.options. | [optional] 
**parentid** | **int** |  | [optional] 
**new_zoneid** | **int** |  | [optional] 
**network_binding** | [**AdspaceNetworkBinding**](AdspaceNetworkBinding.md) |  | [optional] 
**json_settings** | **Dict[str, object]** | Raw assembled blob — unioned hoisted to top level for convenience. | [optional] 

## Example

```python
from goadserver.models.adspace import Adspace

# TODO update the JSON string below
json = "{}"
# create an instance of Adspace from a JSON string
adspace_instance = Adspace.from_json(json)
# print the JSON string representation of the object
print(Adspace.to_json())

# convert the object into a dict
adspace_dict = adspace_instance.to_dict()
# create an instance of Adspace from a dict
adspace_from_dict = Adspace.from_dict(adspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



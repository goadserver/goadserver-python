# SspCampaignWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**adtype** | **int** | Ad type id (setup-data &#x60;ad_types[].id&#x60;). | [optional] 
**ssptype** | **str** |  | [optional] [default to 'ssp']
**rtbtype** | **str** | openrtb or a legacy XML/JSON template type, per setup-data. | [optional] [default to 'openrtb']
**header_bidding** | **bool** | external/exchange only; locked after create. | [optional] 
**rtb_network** | **int** | RTB network id (setup-data &#x60;rtb_networks&#x60;). Required for ssptype&#x3D;ssp. | [optional] 
**ssp_pct** | **int** | Revenue share in percent (required 1-100 for exchange). | [optional] [default to 80]
**siteid** | **int** | One of your sites. Required for external and header bidding. | [optional] 
**slots** | [**List[SspCampaignWriteSlotsInner]**](SspCampaignWriteSlotsInner.md) | Header-bidding slots. | [optional] 
**request_url** | **str** | Partner endpoint (ssptype&#x3D;ssp, use_type 0). | [optional] 
**use_type** | **int** | ssp only: 0 &#x3D; one URL, 1 &#x3D; per-ad-zone URLs, 2 &#x3D; smart-zone RTB feed. | [optional] 
**zoneurls** | [**List[SspCampaignWriteZoneurlsInner]**](SspCampaignWriteZoneurlsInner.md) | use_type 1: per-zone URLs (your own ad zones only; others are dropped). | [optional] 
**p_type** | **int** |  | [optional] 
**adm_response_type** | **str** |  | [optional] [default to 'html']
**rtb_tpl_id** | **int** |  | [optional] [default to 1]
**bid_action** | **int** |  | [optional] [default to 1]
**device_type_ids** | **List[int]** | Empty &#x3D; all. A comma-separated string is accepted too (same for every list below). | [optional] 
**osids** | **List[int]** |  | [optional] 
**browserids** | **List[int]** |  | [optional] 
**regionids** | **List[int]** |  | [optional] 
**browserlanguages** | **List[str]** |  | [optional] 
**connection_types** | **List[int]** |  | [optional] 
**ssp_ids** | **List[int]** |  | [optional] 
**wl_ron_campaign_ids** | **List[int]** | From GET .../wl-ron-campaigns. | [optional] 
**rtb_categories** | **List[str]** |  | [optional] 
**dsp_ids** | **List[int]** | Admin only (ignored for API keys). | [optional] 
**displayoptions** | **str** |  | [optional] [default to '0']
**log_skipped** | **int** |  | [optional] 
**use_adscan** | **int** |  | [optional] 
**bill_on_burl** | **int** | Bill on the OpenRTB burl (external/exchange, openrtb). | [optional] 
**use_optimiser** | **int** |  | [optional] 
**optimiser_data** | **object** | {disc_rules: [...]}, external/exchange only. | [optional] 
**use_api** | **int** |  | [optional] 
**api_data** | **object** | Partner reporting-API credentials (ssp/external). | [optional] 

## Example

```python
from goadserver.models.ssp_campaign_write import SspCampaignWrite

# TODO update the JSON string below
json = "{}"
# create an instance of SspCampaignWrite from a JSON string
ssp_campaign_write_instance = SspCampaignWrite.from_json(json)
# print the JSON string representation of the object
print(SspCampaignWrite.to_json())

# convert the object into a dict
ssp_campaign_write_dict = ssp_campaign_write_instance.to_dict()
# create an instance of SspCampaignWrite from a dict
ssp_campaign_write_from_dict = SspCampaignWrite.from_dict(ssp_campaign_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



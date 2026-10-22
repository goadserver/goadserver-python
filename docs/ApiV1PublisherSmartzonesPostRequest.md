# ApiV1PublisherSmartzonesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**spaceid** | **int** | Parent ad zone id (one of yours | 
**smart_networkid** | **int** | Your smart network account id from &#x60;GET /api/v1/publisher/smartzones/networks&#x60; (&#x60;data[].id&#x60;). 0 &#x3D; no network. | [optional] 
**siteid** | **int** | Ignored — derived from &#x60;spaceid&#x60;. | [optional] 
**countries** | **str** | Comma-separated ISO-3166 alpha-2 codes. &#x60;0&#x60; &#x3D; all countries. | [optional] 
**device_type_ids** | **str** | Comma-separated device type ids (setup-data &#x60;device_types&#x60;). &#x60;0&#x60; &#x3D; all. | [optional] 
**is_active** | **bool** | JSON boolean (an integer is refused as invalid JSON). | [optional] [default to True]
**select_type** | **int** | 0 &#x3D; percentage, 1 &#x3D; eCPM, 2 &#x3D; RTB, 3 &#x3D; eCPM + limit %. A numeric string is accepted too. | [optional] 
**select_pct** | **int** | Share of the ad zone&#39;s traffic (percent). | [optional] [default to 100]
**notes** | **str** |  | [optional] 
**creative** | **str** | JSON-encoded string &#x60;{\&quot;creative\&quot;: {\&quot;type\&quot;: \&quot;url\&quot;|\&quot;xml\&quot;|\&quot;code\&quot;, \&quot;value\&quot;: \&quot;…\&quot;}}&#x60; — the tag/URL the network gave you. | [optional] 
**settings** | **str** | JSON-encoded string of zone settings (e.g. &#x60;referrer_stopwords&#x60;, &#x60;keywords_include&#x60;, &#x60;keywords_exclude&#x60;, &#x60;skip_when_stats&#x60;, &#x60;nw_zoneid&#x60;, &#x60;nw_siteid&#x60;). Keyword and stopword lists are normalised (trimmed, lower-cased, de-duplicated). | [optional] 
**use_adblock** | **int** | Panel checkbox \&quot;Adblock enabled\&quot;: 1 &#x3D; the zone may serve ad-blocked visitors. | [optional] 
**network_zoneid** | **int** | Numeric zone id on the network (alphanumeric ids go into &#x60;settings.nw_zoneid&#x60; with this at 0). | [optional] 
**network_siteid** | **int** | Numeric site id on the network (alphanumeric ids go into &#x60;settings.nw_siteid&#x60;). | [optional] 
**ssp_campaignid** | **int** | One of your SSP campaigns (&#x60;GET /api/v1/publisher/smartzones/ssp-campaigns&#x60;) for RTB-type networks. 0 &#x3D; none. | [optional] 
**scanning_enabled** | **int** | Ad Scanner capture for this zone (when the tenant runs Ad Scanner). | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_smartzones_post_request import ApiV1PublisherSmartzonesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherSmartzonesPostRequest from a JSON string
api_v1_publisher_smartzones_post_request_instance = ApiV1PublisherSmartzonesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherSmartzonesPostRequest.to_json())

# convert the object into a dict
api_v1_publisher_smartzones_post_request_dict = api_v1_publisher_smartzones_post_request_instance.to_dict()
# create an instance of ApiV1PublisherSmartzonesPostRequest from a dict
api_v1_publisher_smartzones_post_request_from_dict = ApiV1PublisherSmartzonesPostRequest.from_dict(api_v1_publisher_smartzones_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



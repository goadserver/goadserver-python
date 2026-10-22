# goadserver.AdspacesApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_adspaces_add_multiple_post**](AdspacesApi.md#api_v1_adspaces_add_multiple_post) | **POST** /api/v1/adspaces/add-multiple | Create several ad zones of one type on one site.
[**api_v1_adspaces_export_codes_get**](AdspacesApi.md#api_v1_adspaces_export_codes_get) | **GET** /api/v1/adspaces/export-codes | Embed codes for many ad zones at once, grouped by site.
[**api_v1_adspaces_get**](AdspacesApi.md#api_v1_adspaces_get) | **GET** /api/v1/adspaces | List ad zones owned by the caller.
[**api_v1_adspaces_id_blocked_advertisers_get**](AdspacesApi.md#api_v1_adspaces_id_blocked_advertisers_get) | **GET** /api/v1/adspaces/{id}/blocked-advertisers | Advertiser block filters that exclude this ad zone.
[**api_v1_adspaces_id_children_get**](AdspacesApi.md#api_v1_adspaces_id_children_get) | **GET** /api/v1/adspaces/{id}/children | List an ad zone&#39;s child zones.
[**api_v1_adspaces_id_clone_post**](AdspacesApi.md#api_v1_adspaces_id_clone_post) | **POST** /api/v1/adspaces/{id}/clone | Duplicate an ad zone.
[**api_v1_adspaces_id_code_get**](AdspacesApi.md#api_v1_adspaces_id_code_get) | **GET** /api/v1/adspaces/{id}/code | Embed-code snippets for an adspace.
[**api_v1_adspaces_id_delete**](AdspacesApi.md#api_v1_adspaces_id_delete) | **DELETE** /api/v1/adspaces/{id} | Soft-delete an adspace.
[**api_v1_adspaces_id_get**](AdspacesApi.md#api_v1_adspaces_id_get) | **GET** /api/v1/adspaces/{id} | Get a single adspace.
[**api_v1_adspaces_id_network_binding_delete**](AdspacesApi.md#api_v1_adspaces_id_network_binding_delete) | **DELETE** /api/v1/adspaces/{id}/network-binding | Remove the zone&#39;s network binding.
[**api_v1_adspaces_id_network_binding_put**](AdspacesApi.md#api_v1_adspaces_id_network_binding_put) | **PUT** /api/v1/adspaces/{id}/network-binding | Bind the zone to a campaign on an external ad network (the Source tab).
[**api_v1_adspaces_id_own_ads_ad_id_delete**](AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_delete) | **DELETE** /api/v1/adspaces/{id}/own-ads/{adId} | Delete an own ad.
[**api_v1_adspaces_id_own_ads_ad_id_get**](AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_get) | **GET** /api/v1/adspaces/{id}/own-ads/{adId} | Get one own ad.
[**api_v1_adspaces_id_own_ads_ad_id_put**](AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_put) | **PUT** /api/v1/adspaces/{id}/own-ads/{adId} | Update an own ad.
[**api_v1_adspaces_id_own_ads_ad_id_toggle_put**](AdspacesApi.md#api_v1_adspaces_id_own_ads_ad_id_toggle_put) | **PUT** /api/v1/adspaces/{id}/own-ads/{adId}/toggle | Switch an own ad on/off.
[**api_v1_adspaces_id_own_ads_get**](AdspacesApi.md#api_v1_adspaces_id_own_ads_get) | **GET** /api/v1/adspaces/{id}/own-ads | List the zone&#39;s own (house / fallback) ads.
[**api_v1_adspaces_id_own_ads_mass_action_post**](AdspacesApi.md#api_v1_adspaces_id_own_ads_mass_action_post) | **POST** /api/v1/adspaces/{id}/own-ads/mass-action | Activate, deactivate or delete several own ads.
[**api_v1_adspaces_id_own_ads_post**](AdspacesApi.md#api_v1_adspaces_id_own_ads_post) | **POST** /api/v1/adspaces/{id}/own-ads | Add an own ad.
[**api_v1_adspaces_id_patch**](AdspacesApi.md#api_v1_adspaces_id_patch) | **PATCH** /api/v1/adspaces/{id} | Update an existing adspace.
[**api_v1_adspaces_id_prices_type_get**](AdspacesApi.md#api_v1_adspaces_id_prices_type_get) | **GET** /api/v1/adspaces/{id}/prices/{type} | Minimum (floor) prices per country for one device type.
[**api_v1_adspaces_id_prices_type_post**](AdspacesApi.md#api_v1_adspaces_id_prices_type_post) | **POST** /api/v1/adspaces/{id}/prices/{type} | Replace the floor prices for one device type.
[**api_v1_adspaces_id_recover_post**](AdspacesApi.md#api_v1_adspaces_id_recover_post) | **POST** /api/v1/adspaces/{id}/recover | Reverse a soft-delete on an adspace.
[**api_v1_adspaces_id_wl_campaigns_get**](AdspacesApi.md#api_v1_adspaces_id_wl_campaigns_get) | **GET** /api/v1/adspaces/{id}/wl-campaigns | Campaigns that can be whitelisted on this zone, and the current whitelist.
[**api_v1_adspaces_id_wl_campaigns_put**](AdspacesApi.md#api_v1_adspaces_id_wl_campaigns_put) | **PUT** /api/v1/adspaces/{id}/wl-campaigns | Replace the zone&#39;s whitelisted campaigns.
[**api_v1_adspaces_mass_delete_post**](AdspacesApi.md#api_v1_adspaces_mass_delete_post) | **POST** /api/v1/adspaces/mass-delete | Soft-delete several ad zones.
[**api_v1_adspaces_mass_recover_post**](AdspacesApi.md#api_v1_adspaces_mass_recover_post) | **POST** /api/v1/adspaces/mass-recover | Recover several soft-deleted ad zones.
[**api_v1_adspaces_templates_get**](AdspacesApi.md#api_v1_adspaces_templates_get) | **GET** /api/v1/adspaces/templates | List your saved ad zone templates.
[**api_v1_adspaces_templates_id_delete**](AdspacesApi.md#api_v1_adspaces_templates_id_delete) | **DELETE** /api/v1/adspaces/templates/{id} | Delete a template.
[**api_v1_adspaces_templates_id_put**](AdspacesApi.md#api_v1_adspaces_templates_id_put) | **PUT** /api/v1/adspaces/templates/{id} | Replace a template&#39;s data.
[**api_v1_adspaces_templates_post**](AdspacesApi.md#api_v1_adspaces_templates_post) | **POST** /api/v1/adspaces/templates | Save an ad zone template.
[**api_v1_adspaces_type_post**](AdspacesApi.md#api_v1_adspaces_type_post) | **POST** /api/v1/adspaces/{type} | Create a new adspace.
[**api_v1_adspaces_type_schema_get**](AdspacesApi.md#api_v1_adspaces_type_schema_get) | **GET** /api/v1/adspaces/{type}/_schema | Field metadata for create/update of one adspace type.


# **api_v1_adspaces_add_multiple_post**
> List[int] api_v1_adspaces_add_multiple_post(api_v1_adspaces_add_multiple_post_request)

Create several ad zones of one type on one site.

The panel's "Add multiple". Each item is created exactly as
`POST /api/v1/adspaces/{type}` would create it (same validation,
same defaults), with the type's default settings block and, for
banner types, `sizeid` as the banner size. Up to 100 items.

Items are created in order. The first refusal stops the run: the
response is that item's error (e.g. 422 `validation_error` for a
duplicate name) plus `failed_item` (index into `items`) and
`created_ids` (what was created before it). Items with an empty
name are skipped.

The type must be active, its module on and its right held; for an
API key it must also be exposed to the API (`in_api`) — same gate
and errors as `POST /api/v1/adspaces/{type}` (404
`unknown_adspace_type`, 403 `module_disabled` / `missing_right`).
Keys pinned to `adzone_ids` / `site_ids` are refused.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_add_multiple_post_request import ApiV1AdspacesAddMultiplePostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    api_v1_adspaces_add_multiple_post_request = {"siteid":30067,"adzone_typeid":2,"sizeid":1,"items":[{"name":"Header 728x90"},{"name":"Footer 728x90"}]} # ApiV1AdspacesAddMultiplePostRequest | 

    try:
        # Create several ad zones of one type on one site.
        api_response = api_instance.api_v1_adspaces_add_multiple_post(api_v1_adspaces_add_multiple_post_request)
        print("The response of AdspacesApi->api_v1_adspaces_add_multiple_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_add_multiple_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_adspaces_add_multiple_post_request** | [**ApiV1AdspacesAddMultiplePostRequest**](ApiV1AdspacesAddMultiplePostRequest.md)|  | 

### Return type

**List[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ids of the created zones, in item order. |  -  |
**400** | &#x60;invalid_request&#x60; (siteid or items missing) or &#x60;too_many_items&#x60; (more than 100). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Site not found, or &#x60;unknown_adspace_type&#x60;. |  -  |
**422** | &#x60;unknown_fields&#x60; (API keys: a body key this endpoint does not read), or an item&#39;s &#x60;validation_error&#x60; with &#x60;failed_item&#x60; and &#x60;created_ids&#x60; added.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_export_codes_get**
> List[ApiV1AdspacesExportCodesGet200ResponseInner] api_v1_adspaces_export_codes_get(siteid=siteid, all=all, sids=sids)

Embed codes for many ad zones at once, grouped by site.

The panel's bulk "Export codes". Returns one entry per site with the
site's controller tag (`ctrl_js`, paste once per page) and the
per-zone snippets. Without `sids` (or with `all=1`) every live zone of
the account is included; narrow with `siteid` or a `sids` list.
For one zone use `GET /api/v1/adspaces/{id}/code`.

Keys pinned to `adzone_ids` / `site_ids` are refused
(`403 forbidden_resource`) — the export spans the whole account.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_export_codes_get200_response_inner import ApiV1AdspacesExportCodesGet200ResponseInner
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    siteid = 56 # int | Only this site's zones. (optional)
    all = 1 # int | 1 = every zone; 0 = only the zones in `sids`. (optional) (default to 1)
    sids = '11865993,11865986' # str | Comma-separated ad zone ids (used with all=0). (optional)

    try:
        # Embed codes for many ad zones at once, grouped by site.
        api_response = api_instance.api_v1_adspaces_export_codes_get(siteid=siteid, all=all, sids=sids)
        print("The response of AdspacesApi->api_v1_adspaces_export_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_export_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteid** | **int**| Only this site&#39;s zones. | [optional] 
 **all** | **int**| 1 &#x3D; every zone; 0 &#x3D; only the zones in &#x60;sids&#x60;. | [optional] [default to 1]
 **sids** | **str**| Comma-separated ad zone ids (used with all&#x3D;0). | [optional] 

### Return type

[**List[ApiV1AdspacesExportCodesGet200ResponseInner]**](ApiV1AdspacesExportCodesGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Codes grouped by site. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_get**
> ApiV1AdspacesGet200Response api_v1_adspaces_get(site_id=site_id, state=state, type=type, parent_id=parent_id, search=search, sort=sort, page=page, per_page=per_page)

List ad zones owned by the caller.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_get200_response import ApiV1AdspacesGet200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    site_id = 56 # int | Filter to one site. (optional)
    state = live # str | `deleted` lists soft-deleted zones (for recover / mass-recover). (optional) (default to live)
    type = 'type_example' # str | Adspace type key (e.g. `popads`) or numeric adzone_typeid. Unknown key → 422. (optional)
    parent_id = 56 # int | Children of this zone; 0 = top-level zones only. (optional)
    search = 'search_example' # str | Substring of the name, or an exact zone id. (optional)
    sort = -id # str |  (optional) (default to -id)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List ad zones owned by the caller.
        api_response = api_instance.api_v1_adspaces_get(site_id=site_id, state=state, type=type, parent_id=parent_id, search=search, sort=sort, page=page, per_page=per_page)
        print("The response of AdspacesApi->api_v1_adspaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Filter to one site. | [optional] 
 **state** | **str**| &#x60;deleted&#x60; lists soft-deleted zones (for recover / mass-recover). | [optional] [default to live]
 **type** | **str**| Adspace type key (e.g. &#x60;popads&#x60;) or numeric adzone_typeid. Unknown key → 422. | [optional] 
 **parent_id** | **int**| Children of this zone; 0 &#x3D; top-level zones only. | [optional] 
 **search** | **str**| Substring of the name, or an exact zone id. | [optional] 
 **sort** | **str**|  | [optional] [default to -id]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ApiV1AdspacesGet200Response**](ApiV1AdspacesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adspace list (filtered by resource_filter.site_ids/adzone_ids when set). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_blocked_advertisers_get**
> api_v1_adspaces_id_blocked_advertisers_get(id)

Advertiser block filters that exclude this ad zone.

Read-only. The advertiser-side block lists (not hidden ones) that
name this zone. `campaignids` is the comma-separated campaigns the
filter applies to.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Advertiser block filters that exclude this ad zone.
        api_instance.api_v1_adspaces_id_blocked_advertisers_get(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_blocked_advertisers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filters (empty array when none, or the zone is not yours). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_children_get**
> api_v1_adspaces_id_children_get(id)

List an ad zone's child zones.

Live zones whose `parentid` is this zone — the in-video sub-zones
under a player zone. Rows are the stored zone records (all
`publisher_adzones` columns) plus `website_name`. Same data as
`GET /api/v1/adspaces?parent_id={id}` in the list shape.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # List an ad zone's child zones.
        api_instance.api_v1_adspaces_id_children_get(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Child zones. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_clone_post**
> api_v1_adspaces_id_clone_post(id, api_v1_adspaces_id_clone_post_request)

Duplicate an ad zone.

Copies the zone (type, site, settings) under a new name. Options
choose what comes along. `copy_campaigns` copies the whitelisted
campaigns only where the account may manage them (see
`PUT /api/v1/adspaces/{id}/wl-campaigns`); otherwise the zone is
still duplicated and `campaigns_skipped` is true.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_clone_post_request import ApiV1AdspacesIdClonePostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_adspaces_id_clone_post_request = {"name":"Homepage 300x250 (copy)","copy_campaigns":true,"copy_own_ads":true,"copy_settings":true} # ApiV1AdspacesIdClonePostRequest | 

    try:
        # Duplicate an ad zone.
        api_instance.api_v1_adspaces_id_clone_post(id, api_v1_adspaces_id_clone_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_adspaces_id_clone_post_request** | [**ApiV1AdspacesIdClonePostRequest**](ApiV1AdspacesIdClonePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Duplicated. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |
**422** | &#x60;validation_error&#x60; (name required) or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_code_get**
> ApiV1AdspacesIdCodeGet200Response api_v1_adspaces_id_code_get(id, layout=layout)

Embed-code snippets for an adspace.

Returns the JS embed snippets a publisher pastes into their site
— the natural last step of the create flow.

Three pieces, all server-rendered with the tenant's ad domain,
the publisher's user id, EaCtrl name, banner dimensions, and
per-type plugin call resolved:

- `site.ctrl_js` — controller `<script>` tag. Paste it once per
  page, before the per-zone snippets (typically in `<head>`).
- `site.ctrl_js_failover` — an alternative to `ctrl_js`, pasted
  instead of it: an inline loader that tries several ad domains in
  turn (the zone's own, the publisher's own, then the network's
  that are not on a block list) and uses the first one an ad
  blocker lets through; it queues the zones' `add()` calls until
  the controller is there. Empty when fewer than two usable ad
  domains are available.
- `js_code` — per-zone JavaScript call (wrap in `<script>` tags).
  This is what goes at each ad slot.
- `ad_tag` — `<iframe src="…">` alternative for callers that
  can't run JS.
- `alternative` — no-JS fallback `<a><img></a>` snippet.

Native zones (nativeads, type 3) take `?layout=<key>`: a
ready-made design, so a publisher does not have to write the
templates. The response then carries the layout's `tpl_body` /
`tpl_row` / `tpl_item` in `js_code` and a `<style>` block scoped to
the zone (`#id_<adspace_id>`) in front of the placement in
`ad_tag`. Keys: `default` (the stock template), `cards`, `list`
(sidebar list), `tiles` (image tiles), `feed`, `links` (text-only
sponsored links); the response of a native zone lists them in
`layouts`. The same layouts are the picker in the panel's Code tab.
Creator widget zones (creator_widget, type 34) take their own
keys: `default` (the example template), `caption` (avatar and text
under the clip), `overlay` (text on the clip), `card`, `clip` (clip
only); the template is `tpl_item` (the plugin has no body/row
templates) and the `<style>` block is scoped the same way.
An unknown key for the zone's type is refused with 422 (`layout`);
other zone types ignore the parameter.

Banner, native, reel and creator widget zones (types 2, 3, 31, 34)
also carry `amp`: the code for AMP pages and Web Stories, which
cannot run the controller. AMP fetches the ad itself through
`amp-list` + `amp-mustache` from goadserver's `/ampad.go?spaceid=<id>`
(JSON, AMP CORS; AMP removed `amp-ad type="custom"` in 2025). The
story code is a sponsored `<amp-story-page>` to paste between the
story's own pages (image ads; a video ad shows its poster). Image and
video ads only — HTML / iframe creatives are skipped. Impressions are
counted by a 1×1 pixel the template loads when the ad renders.

Resource-pinned keys (`resource_filter.adzone_ids` /
`resource_filter.site_ids`) reject reads outside the allow-list
with `403 forbidden_resource`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_code_get200_response import ApiV1AdspacesIdCodeGet200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    layout = 'layout_example' # str | Native (cards…links) and creator widget (caption…clip) zones: ready-made layout to render the code with (see above). (optional)

    try:
        # Embed-code snippets for an adspace.
        api_response = api_instance.api_v1_adspaces_id_code_get(id, layout=layout)
        print("The response of AdspacesApi->api_v1_adspaces_id_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **layout** | **str**| Native (cards…links) and creator widget (caption…clip) zones: ready-made layout to render the code with (see above). | [optional] 

### Return type

[**ApiV1AdspacesIdCodeGet200Response**](ApiV1AdspacesIdCodeGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Code snippets for the adspace. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Adspace not found or no code generated. |  -  |
**422** | Unknown layout (field &#x60;layout&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_delete**
> api_v1_adspaces_id_delete(id, confirm_smart_zones=confirm_smart_zones)

Soft-delete an adspace.

Sets `is_deleted = 1` — the row is hidden from listings but kept
for reporting joins. Undo with `POST /api/v1/adspaces/{id}/recover`.

Refused with **409 `has_flatrate_campaigns`** while a running or
pending flat-rate deal is booked on the zone. A zone with smart
zones attached answers **409 `has_smart_zones`** (with their count)
until you repeat the call with `?confirm_smart_zones=1`; those smart
zones are then closed with the zone and come back on recover.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    confirm_smart_zones = 56 # int | 1 = also close the zone's smart zones. (optional)

    try:
        # Soft-delete an adspace.
        api_instance.api_v1_adspaces_id_delete(id, confirm_smart_zones=confirm_smart_zones)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **confirm_smart_zones** | **int**| 1 &#x3D; also close the zone&#39;s smart zones. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. &#x60;smart_zones&#x60; &#x3D; smart zones closed with it. |  -  |
**409** | &#x60;has_flatrate_campaigns&#x60;, or &#x60;has_smart_zones&#x60; (retry with &#x60;?confirm_smart_zones&#x3D;1&#x60;). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_get**
> Adspace api_v1_adspaces_id_get(id)

Get a single adspace.

Returns the full adspace record. Body shape matches what
`POST /api/v1/adspaces/{type}` accepts, so a create-then-fetch
loop or an update round-trip works without translation:

- Common top-level fields (`name`, `siteid`, `autoapprove`,
  `isvisible`, …) — matching the create body
- `adspace_type` — the type config key (e.g. `bannerads`)
- `adzone_typeid` / `adtype_id` / `adsizeid` — numeric ids
- The type-specific settings block hoisted to top level
  (e.g. `banner_settings`, `pop_settings`, `native_settings`)
- `json_settings` — the raw assembled blob for inspection
- The Campaigns-tab switches (`only_wl_campaigns`,
  `only_tagged_campaigns`, `force_wl_targeting`,
  `skip_rtb_when_wl`), `useflatbuys`, `parentid`, `new_zoneid`,
  and the Source tab's `network_binding`

Keys pinned to `adzone_ids`, or to `site_ids` (checked against the
zone's site), get `403 forbidden_resource` for other zones.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.adspace import Adspace
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Get a single adspace.
        api_response = api_instance.api_v1_adspaces_id_get(id)
        print("The response of AdspacesApi->api_v1_adspaces_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Adspace**](Adspace.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adspace. |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_network_binding_delete**
> api_v1_adspaces_id_network_binding_delete(id)

Remove the zone's network binding.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Remove the zone's network binding.
        api_instance.api_v1_adspaces_id_network_binding_delete(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_network_binding_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unbound. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_network_binding_put**
> api_v1_adspaces_id_network_binding_put(id, api_v1_adspaces_id_network_binding_put_request)

Bind the zone to a campaign on an external ad network (the Source tab).

Records that this zone's traffic is bought from a campaign on one
of your ad networks (`GET /api/v1/tracker/ad-networks`). The
network's cost import then attributes cost to the zone and, with
`auto_api`, the campaign is paused/activated through the network's
API. The current binding is `network_binding` on
`GET /api/v1/adspaces/{id}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_network_binding_put_request import ApiV1AdspacesIdNetworkBindingPutRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_adspaces_id_network_binding_put_request = {"adnetwork_id":77,"adnetwork_campaignid":5512309,"auto_api":true} # ApiV1AdspacesIdNetworkBindingPutRequest | 

    try:
        # Bind the zone to a campaign on an external ad network (the Source tab).
        api_instance.api_v1_adspaces_id_network_binding_put(id, api_v1_adspaces_id_network_binding_put_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_network_binding_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_adspaces_id_network_binding_put_request** | [**ApiV1AdspacesIdNetworkBindingPutRequest**](ApiV1AdspacesIdNetworkBindingPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bound. |  -  |
**400** | &#x60;invalid_body&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found, or &#x60;network_not_found&#x60;. |  -  |
**422** | &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_ad_id_delete**
> api_v1_adspaces_id_own_ads_ad_id_delete(id, ad_id)

Delete an own ad.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Delete an own ad.
        api_instance.api_v1_adspaces_id_own_ads_ad_id_delete(id, ad_id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_ad_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_ad_id_get**
> api_v1_adspaces_id_own_ads_ad_id_get(id, ad_id)

Get one own ad.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Get one own ad.
        api_instance.api_v1_adspaces_id_own_ads_ad_id_get(id, ad_id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_ad_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#x60;{data: &lt;stored record&gt;}&#x60; — same fields as the list rows. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_ad_id_put**
> api_v1_adspaces_id_own_ads_ad_id_put(id, ad_id, own_ad_write)

Update an own ad.

Same fields as create; send the ones to change.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.own_ad_write import OwnAdWrite
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    ad_id = 56 # int | 
    own_ad_write = goadserver.OwnAdWrite() # OwnAdWrite | 

    try:
        # Update an own ad.
        api_instance.api_v1_adspaces_id_own_ads_ad_id_put(id, ad_id, own_ad_write)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_ad_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ad_id** | **int**|  | 
 **own_ad_write** | [**OwnAdWrite**](OwnAdWrite.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60; (API keys, JSON bodies). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_ad_id_toggle_put**
> api_v1_adspaces_id_own_ads_ad_id_toggle_put(id, ad_id)

Switch an own ad on/off.

Flips `isactive`. No body.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    ad_id = 56 # int | 

    try:
        # Switch an own ad on/off.
        api_instance.api_v1_adspaces_id_own_ads_ad_id_toggle_put(id, ad_id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_ad_id_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ad_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Toggled. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_get**
> api_v1_adspaces_id_own_ads_get(id)

List the zone's own (house / fallback) ads.

Ads the publisher runs on the zone itself (the panel's Own ads tab),
served when `useownbanners` is on. Rows are the stored records.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # List the zone's own (house / fallback) ads.
        api_instance.api_v1_adspaces_id_own_ads_get(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Own ads. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_mass_action_post**
> api_v1_adspaces_id_own_ads_mass_action_post(id, api_v1_adspaces_id_own_ads_mass_action_post_request)

Activate, deactivate or delete several own ads.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_own_ads_mass_action_post_request import ApiV1AdspacesIdOwnAdsMassActionPostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_adspaces_id_own_ads_mass_action_post_request = {"action":"deactivate","ids":[3301,3302]} # ApiV1AdspacesIdOwnAdsMassActionPostRequest | 

    try:
        # Activate, deactivate or delete several own ads.
        api_instance.api_v1_adspaces_id_own_ads_mass_action_post(id, api_v1_adspaces_id_own_ads_mass_action_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_mass_action_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_adspaces_id_own_ads_mass_action_post_request** | [**ApiV1AdspacesIdOwnAdsMassActionPostRequest**](ApiV1AdspacesIdOwnAdsMassActionPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Done. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; (ids / action) or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_own_ads_post**
> api_v1_adspaces_id_own_ads_post(id, own_ad_write)

Add an own ad.

JSON body, or `multipart/form-data` with the same fields plus an
image file (max 32 MB form). Unknown-field checking applies to JSON
bodies only.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.own_ad_write import OwnAdWrite
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    own_ad_write = {"title":"House promo","bannertype":1,"bannerurl":"https://example.com/promo","weight":10,"isactive":1,"width":300,"height":250} # OwnAdWrite | 

    try:
        # Add an own ad.
        api_instance.api_v1_adspaces_id_own_ads_post(id, own_ad_write)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_own_ads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **own_ad_write** | [**OwnAdWrite**](OwnAdWrite.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |
**413** | &#x60;payload_too_large&#x60;. |  -  |
**422** | &#x60;validation_error&#x60; (title required, …) or &#x60;unknown_fields&#x60; (API keys, JSON bodies). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_patch**
> ApiV1AdspacesIdPatch200Response api_v1_adspaces_id_patch(id, request_body)

Update an existing adspace.

Update fields on an existing adspace. Send only the keys you want
to change — omitted fields keep their current value. The
`adzone_typeid` is immutable; once an adspace is created its type
cannot be switched.

Use `GET /api/v1/adspaces/{type}/_schema` to enumerate the legal
field set for the type. The same body shape that creates an
adspace works for update.

**Settings blocks merge.** A `*_settings` block is merged into the
stored one: other blocks are kept, and keys of the block you do not
send are kept (one level deep — nested objects such as `closepop`
or `css` are replaced whole). Send a block as `null` to remove it.
So `{"banner_settings": {"sizeid": 7}}` changes only the size.

`parentid` must be another live zone of yours (0 detaches); `siteid`
moves the zone to another of your sites (historical stats stay on
the old site; a site-pinned key may only move it within its pin).
Whitelisted campaigns are set with
`PUT /api/v1/adspaces/{id}/wl-campaigns`, floor prices with
`POST /api/v1/adspaces/{id}/prices/{type}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_patch200_response import ApiV1AdspacesIdPatch200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    request_body = {"name":"Homepage 300x250 (renamed)","autoapprove":true,"banner_settings":{"sizeid":7}} # Dict[str, object] | 

    try:
        # Update an existing adspace.
        api_response = api_instance.api_v1_adspaces_id_patch(id, request_body)
        print("The response of AdspacesApi->api_v1_adspaces_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**ApiV1AdspacesIdPatch200Response**](ApiV1AdspacesIdPatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. &#x60;data&#x60; is the stored adspace after the update (same object as &#x60;GET /api/v1/adspaces/{id}&#x60;). |  -  |
**400** | &#x60;invalid_id&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |
**422** | &#x60;validation_error&#x60; — banner size not valid for the type, unknown rating, bad colour in native css, &#x60;parentid&#x60; / &#x60;siteid&#x60; not one of yours. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_prices_type_get**
> api_v1_adspaces_id_prices_type_get(id, type, device_typeid=device_typeid)

Minimum (floor) prices per country for one device type.

The panel's Prices tab. `{type}` = `cpm` (CPM buys) or `flatrate`
(flat-rate bookings). Prices are **currency units** (the account's
currency) per 1000 impressions; country `"0"` = all countries.

Shapes differ by type, as in the panel: `cpm` returns an array of
`{country, cpm}`, `flatrate` an object `{country: price}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    type = 'type_example' # str | 
    device_typeid = 0 # int | Device type (see /api/v1/lookups/device-types); 0 = all devices. (optional) (default to 0)

    try:
        # Minimum (floor) prices per country for one device type.
        api_instance.api_v1_adspaces_id_prices_type_get(id, type, device_typeid=device_typeid)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_prices_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**|  | 
 **device_typeid** | **int**| Device type (see /api/v1/lookups/device-types); 0 &#x3D; all devices. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prices. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |
**422** | Invalid &#x60;{type}&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_prices_type_post**
> api_v1_adspaces_id_prices_type_post(id, type, api_v1_adspaces_id_prices_type_post_request)

Replace the floor prices for one device type.

Replaces every price of this zone + `{type}` + `device_typeid` with
`cpm_price` (send `[]` to clear). Prices in **currency units** per
1000 impressions (flat-rate prices are stored in cents internally;
the API takes and returns currency units). Country `""` or `"0"` =
all countries.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_prices_type_post_request import ApiV1AdspacesIdPricesTypePostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    type = 'type_example' # str | 
    api_v1_adspaces_id_prices_type_post_request = {"device_typeid":0,"cpm_price":[{"country":"0","cpm":0.5},{"country":"US","cpm":1.2}]} # ApiV1AdspacesIdPricesTypePostRequest | 

    try:
        # Replace the floor prices for one device type.
        api_instance.api_v1_adspaces_id_prices_type_post(id, type, api_v1_adspaces_id_prices_type_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_prices_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**|  | 
 **api_v1_adspaces_id_prices_type_post_request** | [**ApiV1AdspacesIdPricesTypePostRequest**](ApiV1AdspacesIdPricesTypePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Saved. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |
**422** | Invalid &#x60;{type}&#x60;, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_recover_post**
> api_v1_adspaces_id_recover_post(id)

Reverse a soft-delete on an adspace.

Sets `is_deleted = 0` so the adspace appears in listings again, and
restores the smart zones that were closed with it. Returns 404 if
the adspace doesn't exist or isn't currently deleted. Find deleted
zones with `GET /api/v1/adspaces?state=deleted`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Reverse a soft-delete on an adspace.
        api_instance.api_v1_adspaces_id_recover_post(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_recover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recovered. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found or not deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_wl_campaigns_get**
> api_v1_adspaces_id_wl_campaigns_get(id)

Campaigns that can be whitelisted on this zone, and the current whitelist.

The panel's Campaigns tab. `data` lists the RON campaigns of this
zone's ad type (`connected` true for the whitelisted ones, with their
`weight`); `connected` is the stored whitelist `{campaign_id: weight}`.
`force_wl_targeting` and `skip_rtb_when_wl` are on
`GET /api/v1/adspaces/{id}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Campaigns that can be whitelisted on this zone, and the current whitelist.
        api_instance.api_v1_adspaces_id_wl_campaigns_get(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_wl_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Candidates + current whitelist. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ad zone not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_wl_campaigns_put**
> api_v1_adspaces_id_wl_campaigns_put(id, api_v1_adspaces_id_wl_campaigns_put_request)

Replace the zone's whitelisted campaigns.

Replaces the whitelist with `campaigns` (send `[]` to clear it) and
sets the two related switches. Weights are clamped to 0-100.
Campaign ids outside your network are dropped. `force_wl_targeting`
is only stored when at least one campaign remains.

Gated like the panel: the tenant's `connect_campaigns` module must
be on (else **403 `feature_disabled`**), and on a non-Ad-Manager
tenant only an administrator may manage it (**403 `forbidden`**).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_wl_campaigns_put_request import ApiV1AdspacesIdWlCampaignsPutRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_adspaces_id_wl_campaigns_put_request = {"campaigns":[{"id":1201,"weight":60},{"id":1207,"weight":40}],"force_wl_targeting":false,"skip_rtb_when_wl":true} # ApiV1AdspacesIdWlCampaignsPutRequest | 

    try:
        # Replace the zone's whitelisted campaigns.
        api_instance.api_v1_adspaces_id_wl_campaigns_put(id, api_v1_adspaces_id_wl_campaigns_put_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_id_wl_campaigns_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_adspaces_id_wl_campaigns_put_request** | [**ApiV1AdspacesIdWlCampaignsPutRequest**](ApiV1AdspacesIdWlCampaignsPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | &#x60;missing_scope&#x60;, &#x60;forbidden_resource&#x60;, &#x60;feature_disabled&#x60; or &#x60;forbidden&#x60; (see above). |  -  |
**404** | Ad zone not found. |  -  |
**422** | &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_mass_delete_post**
> api_v1_adspaces_mass_delete_post(api_v1_adspaces_mass_delete_post_request)

Soft-delete several ad zones.

Soft-deletes every listed zone you own (`is_deleted = 1`); ids that
are not yours or already deleted are ignored.

Refused with **409 `has_flatrate_campaigns`** when any of them
carries a running or pending flat-rate deal. Zones with smart zones
attached answer **409 `has_smart_zones`** (with the count) until you
repeat the call with `confirm_smart_zones: true` — the smart zones
are then closed with their zone and come back on recover.
Recover with `POST /api/v1/adspaces/mass-recover` (list deleted
zones with `GET /api/v1/adspaces?state=deleted`).

Keys pinned to `adzone_ids` / `site_ids` are refused.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_mass_delete_post_request import ApiV1AdspacesMassDeletePostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    api_v1_adspaces_mass_delete_post_request = {"ids":[11865993,11865986],"confirm_smart_zones":true} # ApiV1AdspacesMassDeletePostRequest | 

    try:
        # Soft-delete several ad zones.
        api_instance.api_v1_adspaces_mass_delete_post(api_v1_adspaces_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_mass_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_adspaces_mass_delete_post_request** | [**ApiV1AdspacesMassDeletePostRequest**](ApiV1AdspacesMassDeletePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. &#x60;smart_zones&#x60; &#x3D; smart zones closed with them. |  -  |
**400** | &#x60;no_ids&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**409** | &#x60;has_flatrate_campaigns&#x60;, or &#x60;has_smart_zones&#x60; (send &#x60;confirm_smart_zones: true&#x60;). |  -  |
**422** | &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_mass_recover_post**
> api_v1_adspaces_mass_recover_post(api_v1_adspaces_mass_recover_post_request)

Recover several soft-deleted ad zones.

Reverses `mass-delete` / `DELETE /api/v1/adspaces/{id}` for every
listed zone you own; the smart zones closed with them come back too.
Keys pinned to `adzone_ids` / `site_ids` are refused.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_mass_recover_post_request import ApiV1AdspacesMassRecoverPostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    api_v1_adspaces_mass_recover_post_request = {"ids":[11865993]} # ApiV1AdspacesMassRecoverPostRequest | 

    try:
        # Recover several soft-deleted ad zones.
        api_instance.api_v1_adspaces_mass_recover_post(api_v1_adspaces_mass_recover_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_mass_recover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_adspaces_mass_recover_post_request** | [**ApiV1AdspacesMassRecoverPostRequest**](ApiV1AdspacesMassRecoverPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recovered. &#x60;smart_zones&#x60; &#x3D; smart zones restored. |  -  |
**400** | &#x60;no_ids&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_templates_get**
> List[ApiV1AdspacesTemplatesGet200ResponseInner] api_v1_adspaces_templates_get()

List your saved ad zone templates.

Templates are the panel's saved "Add multiple" presets: a name plus
an opaque `data` object the panel stores and replays. The server
does not interpret `data`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_templates_get200_response_inner import ApiV1AdspacesTemplatesGet200ResponseInner
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)

    try:
        # List your saved ad zone templates.
        api_response = api_instance.api_v1_adspaces_templates_get()
        print("The response of AdspacesApi->api_v1_adspaces_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_templates_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiV1AdspacesTemplatesGet200ResponseInner]**](ApiV1AdspacesTemplatesGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_templates_id_delete**
> api_v1_adspaces_templates_id_delete(id)

Delete a template.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 

    try:
        # Delete a template.
        api_instance.api_v1_adspaces_templates_id_delete(id)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_templates_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_templates_id_put**
> api_v1_adspaces_templates_id_put(id, api_v1_adspaces_templates_id_put_request)

Replace a template's data.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_templates_id_put_request import ApiV1AdspacesTemplatesIdPutRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    id = 56 # int | 
    api_v1_adspaces_templates_id_put_request = goadserver.ApiV1AdspacesTemplatesIdPutRequest() # ApiV1AdspacesTemplatesIdPutRequest | 

    try:
        # Replace a template's data.
        api_instance.api_v1_adspaces_templates_id_put(id, api_v1_adspaces_templates_id_put_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_templates_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_adspaces_templates_id_put_request** | [**ApiV1AdspacesTemplatesIdPutRequest**](ApiV1AdspacesTemplatesIdPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |
**422** | &#x60;data is required&#x60;, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_templates_post**
> api_v1_adspaces_templates_post(api_v1_adspaces_templates_post_request)

Save an ad zone template.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_templates_post_request import ApiV1AdspacesTemplatesPostRequest
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    api_v1_adspaces_templates_post_request = {"name":"Blog layout","data":{"adzone_typeid":2,"sizeid":1,"items":[{"name":"Header"}]}} # ApiV1AdspacesTemplatesPostRequest | 

    try:
        # Save an ad zone template.
        api_instance.api_v1_adspaces_templates_post(api_v1_adspaces_templates_post_request)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_adspaces_templates_post_request** | [**ApiV1AdspacesTemplatesPostRequest**](ApiV1AdspacesTemplatesPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Saved. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;name and data are required&#x60;, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_type_post**
> ApiV1AdspacesIdPatch200Response api_v1_adspaces_type_post(type, adspace_create)

Create a new adspace.

Create an adspace of the given `{type}`. Required: `name` +
`siteid` (and `adsizeid` or `banner_settings.sizeid` for
banner-flavored types). Everything else has a sensible default.

**Type identity comes from the path, not the body.** The server
resolves the `{type}` path param to its `adzone_typeid` and
`adtype_id` and injects them server-side — you do **not** need to
pass `adzone_typeid` or `adtype_id` in the body. Any value sent
for those keys is overwritten.

The full per-type field list is at `GET /api/v1/adspaces/{type}/_schema`
— pass that schema's body shape here. The type-specific settings
go under the body key named in `settings_block.name`
(e.g. `banner_settings`, `pop_settings`, `native_settings`).

Discovery flow:
1. `GET /api/v1/lookups/adspace-types` — find the `{type}` keys
   the tenant exposes and their per-type `options` flags.
2. `GET /api/v1/sites` — pick a `siteid`.
3. `GET /api/v1/lookups/banner-sizes` — pick a banner size when
   creating banner-flavored zones.
4. `GET /api/v1/adspaces/{type}/_schema` — enumerate all fields.
5. `POST /api/v1/adspaces/{type}` with the body.

Resource-pinned keys (`resource_filter.site_ids`) reject creates
outside the allow-list with `403 forbidden_resource`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.adspace_create import AdspaceCreate
from goadserver.models.api_v1_adspaces_id_patch200_response import ApiV1AdspacesIdPatch200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    type = 'type_example' # str | 
    adspace_create = goadserver.AdspaceCreate() # AdspaceCreate | 

    try:
        # Create a new adspace.
        api_response = api_instance.api_v1_adspaces_type_post(type, adspace_create)
        print("The response of AdspacesApi->api_v1_adspaces_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **adspace_create** | [**AdspaceCreate**](AdspaceCreate.md)|  | 

### Return type

[**ApiV1AdspacesIdPatch200Response**](ApiV1AdspacesIdPatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. &#x60;data&#x60; is the stored adspace (same object as &#x60;GET /api/v1/adspaces/{id}&#x60;, so &#x60;data.id&#x60; is the new id). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Adspace type not exposable on this tenant. |  -  |
**422** | &#x60;validation_error&#x60; (name taken for this site + type, banner size missing/invalid, unknown rating, bad colour, &#x60;parentid&#x60; not yours) or &#x60;invalid_site&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_type_schema_get**
> AdspaceSchema api_v1_adspaces_type_schema_get(type)

Field metadata for create/update of one adspace type.

Discovery endpoint mirroring `GET /api/v1/campaigns/{type}/_schema`.
Returns the canonical list of public field names a `POST
/api/v1/adspaces/{type}` accepts, with type, required-flag,
default value, an example, and a one-line description.

Adspaces are polymorphic — each type carries its own
type-specific block (e.g. `banner_settings` for `bannerads`,
`pop_settings` for `popads`, `native_settings` for `nativeads`).
The `settings_block` field of the response describes that block;
send it under the body key `settings_block.name`.

Use `GET /api/v1/lookups/adspace-types` to discover which `{type}`
values are exposable on the calling tenant.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.adspace_schema import AdspaceSchema
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gas_live_<32 chars>): apiKey
configuration = goadserver.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.AdspacesApi(api_client)
    type = 'type_example' # str | Adspace type config key — see `GET /api/v1/lookups/adspace-types`.

    try:
        # Field metadata for create/update of one adspace type.
        api_response = api_instance.api_v1_adspaces_type_schema_get(type)
        print("The response of AdspacesApi->api_v1_adspaces_type_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdspacesApi->api_v1_adspaces_type_schema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Adspace type config key — see &#x60;GET /api/v1/lookups/adspace-types&#x60;. | 

### Return type

[**AdspaceSchema**](AdspaceSchema.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema for the adspace type. |  -  |
**404** | Type not exposable on this tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


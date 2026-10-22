# goadserver.FiltersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_filters_get**](FiltersApi.md#api_v1_filters_get) | **GET** /api/v1/filters | List all filters across types.
[**api_v1_filters_ip_id_ranges_range_id_delete**](FiltersApi.md#api_v1_filters_ip_id_ranges_range_id_delete) | **DELETE** /api/v1/filters/ip/{id}/ranges/{rangeId} | Delete one range from an IP pool.
[**api_v1_filters_ip_id_ranges_range_id_toggle_put**](FiltersApi.md#api_v1_filters_ip_id_ranges_range_id_toggle_put) | **PUT** /api/v1/filters/ip/{id}/ranges/{rangeId}/toggle | Pause / resume one range of an IP pool.
[**api_v1_filters_mass_action_post**](FiltersApi.md#api_v1_filters_mass_action_post) | **POST** /api/v1/filters/mass-action | Activate, deactivate or delete many filters.
[**api_v1_filters_post**](FiltersApi.md#api_v1_filters_post) | **POST** /api/v1/filters | Create a filter and populate it with items.
[**api_v1_filters_type_id_active_patch**](FiltersApi.md#api_v1_filters_type_id_active_patch) | **PATCH** /api/v1/filters/{type}/{id}/active | Activate or deactivate a filter (exclusion types only).
[**api_v1_filters_type_id_delete**](FiltersApi.md#api_v1_filters_type_id_delete) | **DELETE** /api/v1/filters/{type}/{id} | Delete a filter (and its items, for IP pools).
[**api_v1_filters_type_id_get**](FiltersApi.md#api_v1_filters_type_id_get) | **GET** /api/v1/filters/{type}/{id} | Get a single filter with its items.
[**api_v1_filters_type_id_items_item_delete**](FiltersApi.md#api_v1_filters_type_id_items_item_delete) | **DELETE** /api/v1/filters/{type}/{id}/items/{item} | Remove a single item from a filter.
[**api_v1_filters_type_id_items_post**](FiltersApi.md#api_v1_filters_type_id_items_post) | **POST** /api/v1/filters/{type}/{id}/items | Add items to an existing filter.
[**api_v1_filters_type_id_put**](FiltersApi.md#api_v1_filters_type_id_put) | **PUT** /api/v1/filters/{type}/{id} | Edit a filter (rename, replace items, change scope).


# **api_v1_filters_get**
> ApiV1FiltersGet200Response api_v1_filters_get(type=type, search=search)

List all filters across types.

Each filter has a **type** and may apply globally or to specific
campaigns. Types:

| type          | meaning                          | toggleable |
|---------------|----------------------------------|:----------:|
| `domain_excl` | Block these domains              | yes |
| `domain_incl` | Only allow these domains         | no |
| `adzone_excl` | Block these ad zones             | yes |
| `adzone_incl` | Only allow these ad zones        | no |
| `isp_excl`    | Block these ISPs                 | yes |
| `subid_excl`  | Block these SubIDs               | yes |
| `subid_incl`  | Only allow these SubIDs          | no |
| `publisher_excl` | Block every ad zone of these publishers, including zones they add later | yes |
| `ip`          | IP-pool blocking                 | no |

Unpaginated: `{data, total_rows}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_get200_response import ApiV1FiltersGet200Response
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | Filter to one type. (optional)
    search = 'search_example' # str | Name contains. (optional)

    try:
        # List all filters across types.
        api_response = api_instance.api_v1_filters_get(type=type, search=search)
        print("The response of FiltersApi->api_v1_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)| Filter to one type. | [optional] 
 **search** | **str**| Name contains. | [optional] 

### Return type

[**ApiV1FiltersGet200Response**](ApiV1FiltersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter list across types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_ip_id_ranges_range_id_delete**
> api_v1_filters_ip_id_ranges_range_id_delete(id, range_id)

Delete one range from an IP pool.

Same as `DELETE /api/v1/filters/ip/{id}/items/{rangeId}`; the panel's own route.

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
    api_instance = goadserver.FiltersApi(api_client)
    id = 56 # int | 
    range_id = 56 # int | 

    try:
        # Delete one range from an IP pool.
        api_instance.api_v1_filters_ip_id_ranges_range_id_delete(id, range_id)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_ip_id_ranges_range_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **range_id** | **int**|  | 

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
**404** | IP pool or range not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_ip_id_ranges_range_id_toggle_put**
> api_v1_filters_ip_id_ranges_range_id_toggle_put(id, range_id)

Pause / resume one range of an IP pool.

Flips one range's active state (an inactive range stops matching). `rangeId` is `ranges[].id` from GET /api/v1/filters/ip/{id}. Same handler as the panel; logged on the pool's history.

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
    api_instance = goadserver.FiltersApi(api_client)
    id = 56 # int | 
    range_id = 56 # int | 

    try:
        # Pause / resume one range of an IP pool.
        api_instance.api_v1_filters_ip_id_ranges_range_id_toggle_put(id, range_id)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_ip_id_ranges_range_id_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **range_id** | **int**|  | 

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
**200** | New state. |  -  |
**404** | IP pool or range not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_mass_action_post**
> api_v1_filters_mass_action_post(api_v1_filters_mass_action_post_request)

Activate, deactivate or delete many filters.

Each entry names a filter by `type` + `id` (as in `GET /filters`).
`delete` runs the single-delete path for each (audit snapshot, IP
list cascade, and campaigns linked to an allow-list / IP pool are
unlinked). Activate / deactivate only applies to the types that
have an on/off state; others are skipped. Filters that are not
yours are skipped. `affected` counts what changed.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_mass_action_post_request import ApiV1FiltersMassActionPostRequest
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
    api_instance = goadserver.FiltersApi(api_client)
    api_v1_filters_mass_action_post_request = {"action":"deactivate","filters":[{"id":1201,"type":"domain_excl"},{"id":88,"type":"isp_excl"}]} # ApiV1FiltersMassActionPostRequest | 

    try:
        # Activate, deactivate or delete many filters.
        api_instance.api_v1_filters_mass_action_post(api_v1_filters_mass_action_post_request)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_mass_action_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_filters_mass_action_post_request** | [**ApiV1FiltersMassActionPostRequest**](ApiV1FiltersMassActionPostRequest.md)|  | 

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
**400** | &#x60;no_filters&#x60;, &#x60;invalid_action&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_post**
> FilterDetail api_v1_filters_post(api_v1_filters_post_request)

Create a filter and populate it with items.

Saved through the panel's own create path (same rows, campaign
links and Action Log entries as the Filters page).

For `domain_excl` / `domain_incl`: items can be domain URLs
(`"https://evil.com/x"`) — automatically resolved to internal
domain IDs — or numeric domain IDs as strings.
For `adzone_excl` / `adzone_incl` / `isp_excl`: items must be
numeric IDs (find them with /api/v1/lookups/adzones and
/api/v1/lookups/isps).
For `publisher_excl`: publisher user ids (find them with
/api/v1/lookups/publishers). Ids that are not a publisher on your
network are dropped.
For `subid_excl` / `subid_incl`: SubID strings (the encoded form
when the account has SubID encoding on — stored decoded).
For `ip`: ranges in `ip_list` (one per line: an IP, `a - b` or a
CIDR) and/or `items`; `campaign_ids` is not accepted (link a pool
from the campaign side).

**Campaign scope** (`campaign_ids`):
* Block lists (`*_excl`) — `ad_type` 0 blocks across every campaign,
  so campaign_ids needs `ad_type > 0` (422 otherwise). Each id must
  be one of your live campaigns of that ad type and of
  `campaign_type` (`ron` default; `rtb` for DSP campaigns; omitted
  with `ad_type` 14 means rtb). Empty = every campaign of that ad
  type.
* Allow-lists (`*_incl`) — each id must be one of your live RON
  campaigns; the filter becomes that campaign's allow-list
  (replacing the one it had).
Ids outside the key's campaign pin are a 403.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_post_request import ApiV1FiltersPostRequest
from goadserver.models.filter_detail import FilterDetail
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
    api_instance = goadserver.FiltersApi(api_client)
    api_v1_filters_post_request = goadserver.ApiV1FiltersPostRequest() # ApiV1FiltersPostRequest | 

    try:
        # Create a filter and populate it with items.
        api_response = api_instance.api_v1_filters_post(api_v1_filters_post_request)
        print("The response of FiltersApi->api_v1_filters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_filters_post_request** | [**ApiV1FiltersPostRequest**](ApiV1FiltersPostRequest.md)|  | 

### Return type

[**FilterDetail**](FilterDetail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Filter created — the same FilterDetail GET returns (type&#x3D;ip adds &#x60;imported&#x60;). |  -  |
**403** | A campaign id outside the key&#39;s campaign pin (&#x60;forbidden_resource&#x60;). |  -  |
**422** | Validation error, &#x60;duplicate_name&#x60;, unknown field, or invalid campaign_ids. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_active_patch**
> ApiV1FiltersTypeIdActivePatch200Response api_v1_filters_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)

Activate or deactivate a filter (exclusion types only).

Only `*_excl` filters have an active/inactive state. Inclusion
filters and IP pools always apply when a campaign references them
— disable by removing the reference instead.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_filters_type_id_active_patch200_response import ApiV1FiltersTypeIdActivePatch200Response
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 
    api_v1_campaigns_type_id_active_patch_request = goadserver.ApiV1CampaignsTypeIdActivePatchRequest() # ApiV1CampaignsTypeIdActivePatchRequest | 

    try:
        # Activate or deactivate a filter (exclusion types only).
        api_response = api_instance.api_v1_filters_type_id_active_patch(type, id, api_v1_campaigns_type_id_active_patch_request)
        print("The response of FiltersApi->api_v1_filters_type_id_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 
 **api_v1_campaigns_type_id_active_patch_request** | [**ApiV1CampaignsTypeIdActivePatchRequest**](ApiV1CampaignsTypeIdActivePatchRequest.md)|  | 

### Return type

[**ApiV1FiltersTypeIdActivePatch200Response**](ApiV1FiltersTypeIdActivePatch200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New state |  -  |
**422** | Filter type not toggleable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_delete**
> api_v1_filters_type_id_delete(type, id)

Delete a filter (and its items, for IP pools).

Campaigns that use the filter as their allow-list or IP pool are
unlinked (set back to none), the same as deleting it in the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 

    try:
        # Delete a filter (and its items, for IP pools).
        api_instance.api_v1_filters_type_id_delete(type, id)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_get**
> FilterDetail api_v1_filters_type_id_get(type, id)

Get a single filter with its items.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.filter_detail import FilterDetail
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 

    try:
        # Get a single filter with its items.
        api_response = api_instance.api_v1_filters_type_id_get(type, id)
        print("The response of FiltersApi->api_v1_filters_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 

### Return type

[**FilterDetail**](FilterDetail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter details |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_items_item_delete**
> ApiV1FiltersTypeIdItemsItemDelete200Response api_v1_filters_type_id_items_item_delete(type, id, item)

Remove a single item from a filter.

`{item}` is the stored value — domain ID (or the hostname it was added with), adzone ID, ISP ID, or SubID string (encoded form when SubID encoding is on). For `ip` it is the range id (`ranges[].id`). URL-encode special characters.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_type_id_items_item_delete200_response import ApiV1FiltersTypeIdItemsItemDelete200Response
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 
    item = 'item_example' # str | 

    try:
        # Remove a single item from a filter.
        api_response = api_instance.api_v1_filters_type_id_items_item_delete(type, id, item)
        print("The response of FiltersApi->api_v1_filters_type_id_items_item_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_items_item_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 
 **item** | **str**|  | 

### Return type

[**ApiV1FiltersTypeIdItemsItemDelete200Response**](ApiV1FiltersTypeIdItemsItemDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removed |  -  |
**404** | Item not present in this filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_items_post**
> ApiV1FiltersTypeIdItemsPost200Response api_v1_filters_type_id_items_post(type, id, api_v1_filters_type_id_items_post_request)

Add items to an existing filter.

Same input format as creating a filter — domain URLs are
auto-resolved to IDs for domain filters, numeric IDs required
for adzone/ISP filters, SubID strings for SubID filters.
Already-present items are deduplicated silently. For `ip` each
item is one range line (IP, `a - b` or CIDR) and the answer is the
pool's FilterDetail with `imported`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_type_id_items_post200_response import ApiV1FiltersTypeIdItemsPost200Response
from goadserver.models.api_v1_filters_type_id_items_post_request import ApiV1FiltersTypeIdItemsPostRequest
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 
    api_v1_filters_type_id_items_post_request = goadserver.ApiV1FiltersTypeIdItemsPostRequest() # ApiV1FiltersTypeIdItemsPostRequest | 

    try:
        # Add items to an existing filter.
        api_response = api_instance.api_v1_filters_type_id_items_post(type, id, api_v1_filters_type_id_items_post_request)
        print("The response of FiltersApi->api_v1_filters_type_id_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 
 **api_v1_filters_type_id_items_post_request** | [**ApiV1FiltersTypeIdItemsPostRequest**](ApiV1FiltersTypeIdItemsPostRequest.md)|  | 

### Return type

[**ApiV1FiltersTypeIdItemsPost200Response**](ApiV1FiltersTypeIdItemsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New item set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filters_type_id_put**
> FilterDetail api_v1_filters_type_id_put(type, id, api_v1_filters_type_id_put_request)

Edit a filter (rename, replace items, change scope).

Partial edit: every field you leave out keeps its current value,
then the filter is saved through the panel's own edit path (same
rows, campaign links and Action Log entries as the Filters page).

* `items` **replaces** the whole item list (same input format as
  create). To add or remove single items use the `/items` routes.
* `campaign_ids` replaces the campaign scope and is validated like
  on create (needs `ad_type > 0` on block lists; campaigns must be
  yours, of that ad type, and of `campaign_type`). Sending `[]`
  makes a block list cover every campaign of its ad type, and
  unlinks every campaign from an allow-list.
* `ad_type` / `campaign_type` re-validate the kept campaign list.
* `type=ip`: `name`, `ip_list` (ranges to import, one per line) and
  `replace_ip_ranges` (true = drop the existing ranges first) only.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_filters_type_id_put_request import ApiV1FiltersTypeIdPutRequest
from goadserver.models.filter_detail import FilterDetail
from goadserver.models.filter_type import FilterType
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
    api_instance = goadserver.FiltersApi(api_client)
    type = goadserver.FilterType() # FilterType | 
    id = 56 # int | 
    api_v1_filters_type_id_put_request = {"name":"Fraud domains (Q4)"} # ApiV1FiltersTypeIdPutRequest | 

    try:
        # Edit a filter (rename, replace items, change scope).
        api_response = api_instance.api_v1_filters_type_id_put(type, id, api_v1_filters_type_id_put_request)
        print("The response of FiltersApi->api_v1_filters_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiltersApi->api_v1_filters_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FilterType**](.md)|  | 
 **id** | **int**|  | 
 **api_v1_filters_type_id_put_request** | [**ApiV1FiltersTypeIdPutRequest**](ApiV1FiltersTypeIdPutRequest.md)|  | 

### Return type

[**FilterDetail**](FilterDetail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved filter (same shape as GET). |  -  |
**403** | A campaign id outside the key&#39;s campaign pin (&#x60;forbidden_resource&#x60;). |  -  |
**404** | Not found |  -  |
**422** | Unknown field, unknown type, empty name / items, invalid campaign_ids, or a field the type does not store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


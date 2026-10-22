# goadserver.LookupsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_lookups_adspace_types_get**](LookupsApi.md#api_v1_lookups_adspace_types_get) | **GET** /api/v1/lookups/adspace-types | Adspace types the caller can publish on this tenant.
[**api_v1_lookups_adzone_locations_get**](LookupsApi.md#api_v1_lookups_adzone_locations_get) | **GET** /api/v1/lookups/adzone-locations | Adzone locations for the tenant.
[**api_v1_lookups_adzones_get**](LookupsApi.md#api_v1_lookups_adzones_get) | **GET** /api/v1/lookups/adzones | Find adzone ids (for adzone filters).
[**api_v1_lookups_banner_sizes_get**](LookupsApi.md#api_v1_lookups_banner_sizes_get) | **GET** /api/v1/lookups/banner-sizes | Banner sizes for banner-flavored adspaces.
[**api_v1_lookups_browsers_get**](LookupsApi.md#api_v1_lookups_browsers_get) | **GET** /api/v1/lookups/browsers | Browser ids (optionally scoped by device type).
[**api_v1_lookups_carriers_get**](LookupsApi.md#api_v1_lookups_carriers_get) | **GET** /api/v1/lookups/carriers | Mobile carriers (ids for carrier targeting).
[**api_v1_lookups_categories_get**](LookupsApi.md#api_v1_lookups_categories_get) | **GET** /api/v1/lookups/categories | Active sub-categories (optionally scoped to a main).
[**api_v1_lookups_device_types_get**](LookupsApi.md#api_v1_lookups_device_types_get) | **GET** /api/v1/lookups/device-types | Active device types for this tenant.
[**api_v1_lookups_domains_get**](LookupsApi.md#api_v1_lookups_domains_get) | **GET** /api/v1/lookups/domains | Resolve domains to the ids domain filters store.
[**api_v1_lookups_isps_get**](LookupsApi.md#api_v1_lookups_isps_get) | **GET** /api/v1/lookups/isps | Find ISP ids (for ISP filters).
[**api_v1_lookups_link_types_get**](LookupsApi.md#api_v1_lookups_link_types_get) | **GET** /api/v1/lookups/link-types | Active link types for the tenant.
[**api_v1_lookups_main_categories_get**](LookupsApi.md#api_v1_lookups_main_categories_get) | **GET** /api/v1/lookups/main-categories | Active main categories for the tenant.
[**api_v1_lookups_operating_systems_get**](LookupsApi.md#api_v1_lookups_operating_systems_get) | **GET** /api/v1/lookups/operating-systems | Operating-system ids (optionally scoped by device type).
[**api_v1_lookups_publishers_get**](LookupsApi.md#api_v1_lookups_publishers_get) | **GET** /api/v1/lookups/publishers | Find publisher ids (for publisher_excl filters).
[**api_v1_lookups_ratings_get**](LookupsApi.md#api_v1_lookups_ratings_get) | **GET** /api/v1/lookups/ratings | Active content ratings for the tenant.
[**api_v1_lookups_reel_types_get**](LookupsApi.md#api_v1_lookups_reel_types_get) | **GET** /api/v1/lookups/reel-types | Active reel types for the tenant.
[**api_v1_lookups_regions_get**](LookupsApi.md#api_v1_lookups_regions_get) | **GET** /api/v1/lookups/regions | Walk the geo region tree (one level per call).
[**api_v1_lookups_website_languages_get**](LookupsApi.md#api_v1_lookups_website_languages_get) | **GET** /api/v1/lookups/website-languages | Supported website languages (ISO codes).
[**api_v1_lookups_website_types_get**](LookupsApi.md#api_v1_lookups_website_types_get) | **GET** /api/v1/lookups/website-types | Active website types for the tenant.


# **api_v1_lookups_adspace_types_get**
> ApiV1LookupsAdspaceTypesGet200Response api_v1_lookups_adspace_types_get()

Adspace types the caller can publish on this tenant.

Returns the adspace types exposable via the public API for the
current tenant + caller. Filters applied (same as the panel
adspace-create page):

- `is_active = true` — tenant has enabled the type
- `in_api = true` — type is exposable via the public API
- `mod_enabled` chain enabled for the user
- `need_rights` gate satisfied (when set)

Each entry carries the metadata needed to drive a create form:

- `id` / `key` / `name` / `adtype_id`
- `settings_key` — the body key for the type-specific block
  on `POST /api/v1/adspaces/{type}` (e.g. `banner_settings`,
  `pop_settings`, `native_settings`). Empty string means the
  type takes no nested settings block.
- `selling_types` — `["ron"]`, `["ron","cpm"]`, etc.
- `use_min_price` / `use_smartzone` / `has_own_ads` / `has_preview`
- `options` — config-driven flag bag (boolean toggles, banner-size
  selects, country exclude lists, …) that map to top-level body
  fields on create. The same `options` shape is mirrored on
  `GET /api/v1/adspaces/{type}/_schema`.

Use the `key` value as the `{type}` path parameter on
`GET /api/v1/adspaces/{type}/_schema` and
`POST /api/v1/adspaces/{type}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_adspace_types_get200_response import ApiV1LookupsAdspaceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Adspace types the caller can publish on this tenant.
        api_response = api_instance.api_v1_lookups_adspace_types_get()
        print("The response of LookupsApi->api_v1_lookups_adspace_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_adspace_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsAdspaceTypesGet200Response**](ApiV1LookupsAdspaceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adspace types available for create on this tenant. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_adzone_locations_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_adzone_locations_get()

Adzone locations for the tenant.

Returns the configured adzone locations for the tenant. Use `id`
to fill `locationid` on adspace create, and in `location_ids` on a
banner campaign (ad type 2) — required on campaign create when this
list is non-empty (a campaign may not target every placement at the
floor price). Only meaningful when `modules.global.adzone_locations`
is enabled — empty list otherwise.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Adzone locations for the tenant.
        api_response = api_instance.api_v1_lookups_adzone_locations_get()
        print("The response of LookupsApi->api_v1_lookups_adzone_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_adzone_locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adzone locations. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_adzones_get**
> api_v1_lookups_adzones_get(term=term, bulk=bulk)

Find adzone ids (for adzone filters).

The panel's adzone picker. Two modes:

* `term` (≥ 2 characters) — up to 50 zones whose name or site URL
  contains it, or whose id equals it. Answer: a bare array
  `[{id, label}]` (label = `zone name (site url)`).
* `bulk` — newline-separated adzone ids; answer
  `{data: [{id, label}], not_found: [...]}`.

Labels follow the panel's source-name rule: an account without the
"see source names" right gets the id as the label, and `term` then
matches exact ids only.


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
    api_instance = goadserver.LookupsApi(api_client)
    term = 'term_example' # str |  (optional)
    bulk = 'bulk_example' # str | Newline-separated adzone ids; wins over term. (optional)

    try:
        # Find adzone ids (for adzone filters).
        api_instance.api_v1_lookups_adzones_get(term=term, bulk=bulk)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_adzones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 
 **bulk** | **str**| Newline-separated adzone ids; wins over term. | [optional] 

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
**200** | &#x60;term&#x60;: array of {id, label}; &#x60;bulk&#x60;: {data, not_found}. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_banner_sizes_get**
> ApiV1LookupsBannerSizesGet200Response api_v1_lookups_banner_sizes_get()

Banner sizes for banner-flavored adspaces.

Returns the active banner sizes for the tenant. Use the `id`
value as `adsizeid` (or `banner_settings.sizeid`) when creating
a banner-flavored adspace (`bannerads`, `fixim_banner`,
`impopup`, `interstitialads`, `interstitial_banner`,
`invideo_banner`).

Sizes are sorted with common IAB formats first
(300x250 → 728x90 → 160x600 → …).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_banner_sizes_get200_response import ApiV1LookupsBannerSizesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Banner sizes for banner-flavored adspaces.
        api_response = api_instance.api_v1_lookups_banner_sizes_get()
        print("The response of LookupsApi->api_v1_lookups_banner_sizes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_banner_sizes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsBannerSizesGet200Response**](ApiV1LookupsBannerSizesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active banner sizes. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_browsers_get**
> ApiV1LookupsBrowsersGet200Response api_v1_lookups_browsers_get(device_type_ids=device_type_ids)

Browser ids (optionally scoped by device type).

Returns `{id, name}` pairs for browsers known to the platform.
Browsers are stored **per device type**, so callers that already
know which devices their campaign targets should pass
`?device_type_ids=<csv>` to scope the listing — e.g.
`?device_type_ids=1,2` for desktop + mobile.

Without the filter, returns the tenant-active set across all
device types (some entries may not actually serve on every
device).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_browsers_get200_response import ApiV1LookupsBrowsersGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)
    device_type_ids = '1,2' # str | Comma-separated device-type ids from `GET /api/v1/lookups/device-types`. Empty = all. (optional)

    try:
        # Browser ids (optionally scoped by device type).
        api_response = api_instance.api_v1_lookups_browsers_get(device_type_ids=device_type_ids)
        print("The response of LookupsApi->api_v1_lookups_browsers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_browsers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_ids** | **str**| Comma-separated device-type ids from &#x60;GET /api/v1/lookups/device-types&#x60;. Empty &#x3D; all. | [optional] 

### Return type

[**ApiV1LookupsBrowsersGet200Response**](ApiV1LookupsBrowsersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Browsers matching the filter. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_carriers_get**
> ApiV1LookupsCarriersGet200Response api_v1_lookups_carriers_get()

Mobile carriers (ids for carrier targeting).

Every mobile carrier the ad server can target, with its country.
Use `id` for campaign carrier targeting (`carrier_id`) and for
`carrier_id` conditions in bid rulesets. Same cached list as the
panel's carrier dropdown (~1,150 rows, refreshed every 5 minutes).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_carriers_get200_response import ApiV1LookupsCarriersGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Mobile carriers (ids for carrier targeting).
        api_response = api_instance.api_v1_lookups_carriers_get()
        print("The response of LookupsApi->api_v1_lookups_carriers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_carriers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsCarriersGet200Response**](ApiV1LookupsCarriersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Carriers. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_categories_get**
> ApiV1LookupsCategoriesGet200Response api_v1_lookups_categories_get(main_catid=main_catid)

Active sub-categories (optionally scoped to a main).

Returns active categories. Pass `?main_catid=N` to limit the
result to categories belonging to that main category — the
legacy `main_categories` column on each row is a CSV of main-id
memberships, so a category can belong to several mains.

Use `id` to fill `catid` on adspace create or populate the
`categories` array on site create.

**Cross-resource lookup** — accessible to keys with any of
`sites.read`, `adspaces.read`, `tracking.read`, or
`campaigns.read`. (Any scope that legitimately needs category
ids opens it.)


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_categories_get200_response import ApiV1LookupsCategoriesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)
    main_catid = 56 # int | Filter to categories under this main. (optional)

    try:
        # Active sub-categories (optionally scoped to a main).
        api_response = api_instance.api_v1_lookups_categories_get(main_catid=main_catid)
        print("The response of LookupsApi->api_v1_lookups_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_catid** | **int**| Filter to categories under this main. | [optional] 

### Return type

[**ApiV1LookupsCategoriesGet200Response**](ApiV1LookupsCategoriesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active categories matching the filter. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_device_types_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_device_types_get()

Active device types for this tenant.

Returns `{id, name}` pairs for the device types active on this
tenant (typically Desktop, Mobile, Tablet, …). Use these ids:
  - in the `device_type_ids` field on campaign create / update,
  - and as the `device_type_ids` query filter for
    `/api/v1/lookups/browsers` and
    `/api/v1/lookups/operating-systems` (browsers + OSes are
    stored per device type).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active device types for this tenant.
        api_response = api_instance.api_v1_lookups_device_types_get()
        print("The response of LookupsApi->api_v1_lookups_device_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_device_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active device types. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_domains_get**
> api_v1_lookups_domains_get(bulk)

Resolve domains to the ids domain filters store.

The panel's bulk domain picker. `bulk` is a newline-separated list
of domains, URLs (protocol, path and `www.` are stripped) or domain
ids; each known one comes back as `{id, label}` and the rest are
listed in `not_found`. Domain filters accept hostnames directly too
(`items` on POST /api/v1/filters), so this is mostly for showing
what an id means. Without `bulk` the answer is an empty array `[]`.


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
    api_instance = goadserver.LookupsApi(api_client)
    bulk = 'example.com https://www.spam.test/x 123' # str | 

    try:
        # Resolve domains to the ids domain filters store.
        api_instance.api_v1_lookups_domains_get(bulk)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_domains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk** | **str**|  | 

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
**200** | Matches. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_isps_get**
> api_v1_lookups_isps_get(term=term, bulk=bulk)

Find ISP ids (for ISP filters).

The panel's ISP picker. `term` (≥ 2 characters) returns up to 50
ISPs whose name contains it as a bare array `[{id, label}]` (label
= `name (country) (connection type)`). `bulk` takes newline-separated
name fragments and returns every matching ISP (one organisation can
span many ASNs) as `{data, not_found, truncated, limit}` — capped at
`limit` (1000) rows, with `truncated: true` when the cap clipped it
(then `not_found` is not computed).


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
    api_instance = goadserver.LookupsApi(api_client)
    term = 'term_example' # str |  (optional)
    bulk = 'bulk_example' # str | Newline-separated name fragments; wins over term. (optional)

    try:
        # Find ISP ids (for ISP filters).
        api_instance.api_v1_lookups_isps_get(term=term, bulk=bulk)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_isps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 
 **bulk** | **str**| Newline-separated name fragments; wins over term. | [optional] 

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
**200** | &#x60;term&#x60;: array of {id, label}; &#x60;bulk&#x60;: {data, not_found, truncated, limit}. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_link_types_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_link_types_get()

Active link types for the tenant.

The tenant's link types. Use `id` in `location_ids` on a link
campaign (ad type 6); required on create when this list is non-empty.
Empty unless `modules.global.link_types` is active.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active link types for the tenant.
        api_response = api_instance.api_v1_lookups_link_types_get()
        print("The response of LookupsApi->api_v1_lookups_link_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_link_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The active types (empty when the module is off). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_main_categories_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_main_categories_get()

Active main categories for the tenant.

Returns active main categories. Use `id` to fill `main_catid` on
site create or adspace create, or as an input to
`/api/v1/lookups/categories?main_catid=N` for the sub-categories.

**Cross-resource lookup** — accessible to keys with any of
`sites.read`, `adspaces.read`, `tracking.read`, or
`campaigns.read`. (Any scope that legitimately needs category
ids opens it.)


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active main categories for the tenant.
        api_response = api_instance.api_v1_lookups_main_categories_get()
        print("The response of LookupsApi->api_v1_lookups_main_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_main_categories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active main categories. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_operating_systems_get**
> ApiV1LookupsBrowsersGet200Response api_v1_lookups_operating_systems_get(device_type_ids=device_type_ids)

Operating-system ids (optionally scoped by device type).

Returns `{id, name}` pairs for operating systems active on this
tenant. OS visibility is **per device type** — pass
`?device_type_ids=<csv>` to scope the listing to OSes valid on
those devices (e.g. iOS / Android only show under mobile).

Without the filter, returns the tenant-active union across all
device types (Mobile OSes will appear even when you're targeting
Desktop, etc.).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_browsers_get200_response import ApiV1LookupsBrowsersGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)
    device_type_ids = '2' # str | Comma-separated device-type ids from `GET /api/v1/lookups/device-types`. Empty = all. (optional)

    try:
        # Operating-system ids (optionally scoped by device type).
        api_response = api_instance.api_v1_lookups_operating_systems_get(device_type_ids=device_type_ids)
        print("The response of LookupsApi->api_v1_lookups_operating_systems_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_operating_systems_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_ids** | **str**| Comma-separated device-type ids from &#x60;GET /api/v1/lookups/device-types&#x60;. Empty &#x3D; all. | [optional] 

### Return type

[**ApiV1LookupsBrowsersGet200Response**](ApiV1LookupsBrowsersGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operating systems matching the filter. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_publishers_get**
> api_v1_lookups_publishers_get(term=term, bulk=bulk)

Find publisher ids (for publisher_excl filters).

The panel's publisher picker for the `publisher_excl` filter — only
publishers on your own network. `term` is either a publisher id
(exact match, `#` prefix allowed) or a name fragment (≥ 2
characters, company or contact name, up to 50 hits), answered as a
bare array `[{id, label}]` with label = company or contact name.
`bulk` takes newline-separated ids and returns `{data, not_found}`.
Where the network hides traffic-source names from advertisers, the
label is the bare id and only exact-id lookups match.


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
    api_instance = goadserver.LookupsApi(api_client)
    term = 'term_example' # str |  (optional)
    bulk = 'bulk_example' # str | Newline-separated publisher ids; wins over term. (optional)

    try:
        # Find publisher ids (for publisher_excl filters).
        api_instance.api_v1_lookups_publishers_get(term=term, bulk=bulk)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_publishers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 
 **bulk** | **str**| Newline-separated publisher ids; wins over term. | [optional] 

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
**200** | &#x60;term&#x60;: array of {id, label}; &#x60;bulk&#x60;: {data, not_found}. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_ratings_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_ratings_get()

Active content ratings for the tenant.

Returns active content ratings. Use `id` to fill `ratingid` on
adspace create. Only enforced when `modules.global.rating` is
active — empty list otherwise.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active content ratings for the tenant.
        api_response = api_instance.api_v1_lookups_ratings_get()
        print("The response of LookupsApi->api_v1_lookups_ratings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_ratings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active ratings. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_reel_types_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_reel_types_get()

Active reel types for the tenant.

The tenant's reel types. Use `id` in `location_ids` on a reel
campaign (ad type 20); required on create when this list is non-empty.
Empty unless `modules.global.reel_types` is active.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active reel types for the tenant.
        api_response = api_instance.api_v1_lookups_reel_types_get()
        print("The response of LookupsApi->api_v1_lookups_reel_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_reel_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The active types (empty when the module is off). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_regions_get**
> ApiV1LookupsRegionsGet200Response api_v1_lookups_regions_get(parent_id=parent_id, ids=ids)

Walk the geo region tree (one level per call).

Hierarchical drill-down browser for geo region targeting. Returns
only the direct children of `parent_id` per call so callers walk
the tree top-down, one level at a time:

```
parent_id absent / 0  → continents (level 0)
parent_id = <continent id>  → countries on that continent (level 1)
parent_id = <country id>    → states / provinces in that country (level 2)
parent_id = <state id>      → cities / sub-regions (level 3, if any)
parent_id = <city id>       → leaf items (level 4, if any)
```

Each item carries `level` so the caller can stop drilling once
they've hit the granularity they want. Campaigns most commonly
target countries (level 1) or states / provinces (level 2), but
deeper levels are valid too.

**The id you collect from this endpoint is what you send back to
`regions` on a campaign create / update.** Always send the most
specific (leaf) id you actually want — see the `regions` field
notes on `POST /api/v1/campaigns/{type}` and
`PATCH /api/v1/campaigns/{type}/{id}` for why.

**Performance:** the geo tree is preloaded into memory at server
startup (~158k rows), so every call is a map lookup, not a DB
query. A response is capped at 2000 children per call (no single
legitimate parent has more than that).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_regions_get200_response import ApiV1LookupsRegionsGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)
    parent_id = 0 # int | Parent region id to list children of. 0 (default) returns continents. (optional) (default to 0)
    ids = '2300660,2635167' # str | Comma-separated region ids to look up directly instead of walking the tree (e.g. the ids in a campaign's `regions` field), up to 500; unknown ids are left out. The answer then carries `ids: true` and no `parent_id`. (optional)

    try:
        # Walk the geo region tree (one level per call).
        api_response = api_instance.api_v1_lookups_regions_get(parent_id=parent_id, ids=ids)
        print("The response of LookupsApi->api_v1_lookups_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_regions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| Parent region id to list children of. 0 (default) returns continents. | [optional] [default to 0]
 **ids** | **str**| Comma-separated region ids to look up directly instead of walking the tree (e.g. the ids in a campaign&#39;s &#x60;regions&#x60; field), up to 500; unknown ids are left out. The answer then carries &#x60;ids: true&#x60; and no &#x60;parent_id&#x60;. | [optional] 

### Return type

[**ApiV1LookupsRegionsGet200Response**](ApiV1LookupsRegionsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Children of the requested parent. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_website_languages_get**
> ApiV1LookupsWebsiteLanguagesGet200Response api_v1_lookups_website_languages_get()

Supported website languages (ISO codes).

Returns the supported website languages from the `adlanguages`
table. Pass the `code` values in the `sitelanguages` array on
site create. Required when `modules.global.website_languages` is
active. Non-trusted publishers may select only one.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_website_languages_get200_response import ApiV1LookupsWebsiteLanguagesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Supported website languages (ISO codes).
        api_response = api_instance.api_v1_lookups_website_languages_get()
        print("The response of LookupsApi->api_v1_lookups_website_languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_website_languages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsWebsiteLanguagesGet200Response**](ApiV1LookupsWebsiteLanguagesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website languages. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_lookups_website_types_get**
> ApiV1LookupsDeviceTypesGet200Response api_v1_lookups_website_types_get()

Active website types for the tenant.

Returns the configured website types. Use `id` to fill `typeid`
on site create. Only meaningful when
`modules.global.website_types` is enabled — empty list otherwise.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_lookups_device_types_get200_response import ApiV1LookupsDeviceTypesGet200Response
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
    api_instance = goadserver.LookupsApi(api_client)

    try:
        # Active website types for the tenant.
        api_response = api_instance.api_v1_lookups_website_types_get()
        print("The response of LookupsApi->api_v1_lookups_website_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->api_v1_lookups_website_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1LookupsDeviceTypesGet200Response**](ApiV1LookupsDeviceTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website types. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.SmartZonesApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_smartzones_distribution_adspaces_id_get**](SmartZonesApi.md#api_v1_publisher_smartzones_distribution_adspaces_id_get) | **GET** /api/v1/publisher/smartzones/distribution/adspaces/{id} | Network split for one ad zone.
[**api_v1_publisher_smartzones_distribution_per_site_get**](SmartZonesApi.md#api_v1_publisher_smartzones_distribution_per_site_get) | **GET** /api/v1/publisher/smartzones/distribution/per-site | Traffic and earnings split across networks for one site.
[**api_v1_publisher_smartzones_distribution_sites_get**](SmartZonesApi.md#api_v1_publisher_smartzones_distribution_sites_get) | **GET** /api/v1/publisher/smartzones/distribution/sites | Sites that carry smart zones.
[**api_v1_publisher_smartzones_get**](SmartZonesApi.md#api_v1_publisher_smartzones_get) | **GET** /api/v1/publisher/smartzones | List smart zones.
[**api_v1_publisher_smartzones_id_delete**](SmartZonesApi.md#api_v1_publisher_smartzones_id_delete) | **DELETE** /api/v1/publisher/smartzones/{id} | Delete a smart zone.
[**api_v1_publisher_smartzones_id_get**](SmartZonesApi.md#api_v1_publisher_smartzones_id_get) | **GET** /api/v1/publisher/smartzones/{id} | Get one smart zone.
[**api_v1_publisher_smartzones_id_put**](SmartZonesApi.md#api_v1_publisher_smartzones_id_put) | **PUT** /api/v1/publisher/smartzones/{id} | Update a smart zone.
[**api_v1_publisher_smartzones_import_post**](SmartZonesApi.md#api_v1_publisher_smartzones_import_post) | **POST** /api/v1/publisher/smartzones/import | Bulk import smart zones.
[**api_v1_publisher_smartzones_networks_get**](SmartZonesApi.md#api_v1_publisher_smartzones_networks_get) | **GET** /api/v1/publisher/smartzones/networks | List your smart network accounts.
[**api_v1_publisher_smartzones_networks_id_delete**](SmartZonesApi.md#api_v1_publisher_smartzones_networks_id_delete) | **DELETE** /api/v1/publisher/smartzones/networks/{id} | Remove a smart network account.
[**api_v1_publisher_smartzones_networks_post**](SmartZonesApi.md#api_v1_publisher_smartzones_networks_post) | **POST** /api/v1/publisher/smartzones/networks | Add or update a smart network account.
[**api_v1_publisher_smartzones_post**](SmartZonesApi.md#api_v1_publisher_smartzones_post) | **POST** /api/v1/publisher/smartzones | Create a smart zone.
[**api_v1_publisher_smartzones_setup_data_get**](SmartZonesApi.md#api_v1_publisher_smartzones_setup_data_get) | **GET** /api/v1/publisher/smartzones/setup-data | Lookups for the smart-zone form.
[**api_v1_publisher_smartzones_ssp_campaigns_get**](SmartZonesApi.md#api_v1_publisher_smartzones_ssp_campaigns_get) | **GET** /api/v1/publisher/smartzones/ssp-campaigns | SSP campaigns usable as a smart zone&#39;s RTB feed.


# **api_v1_publisher_smartzones_distribution_adspaces_id_get**
> api_v1_publisher_smartzones_distribution_adspaces_id_get(id, var_from=var_from, to=to, basis=basis)

Network split for one ad zone.

Per-day share, eCPM and volume of each smart zone under one of your
ad zones, which zone led each day, a country heat map and a summary.
**Money is in currency units (not cents).**


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
    api_instance = goadserver.SmartZonesApi(api_client)
    id = 56 # int | Ad zone (adspace) id.
    var_from = '2013-10-20' # date |  (optional)
    to = '2013-10-20' # date |  (optional)
    basis = imp # str |  (optional) (default to imp)

    try:
        # Network split for one ad zone.
        api_instance.api_v1_publisher_smartzones_distribution_adspaces_id_get(id, var_from=var_from, to=to, basis=basis)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_distribution_adspaces_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ad zone (adspace) id. | 
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **basis** | **str**|  | [optional] [default to imp]

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
**200** | Distribution. |  -  |
**400** | &#x60;bad_request&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;adzone_not_found&#x60; — not one of your live ad zones. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_distribution_per_site_get**
> api_v1_publisher_smartzones_distribution_per_site_get(siteid, var_from=var_from, to=to, basis=basis)

Traffic and earnings split across networks for one site.

How one site's smart-zone traffic and earnings are spread over the
networks: daily series (revenue, impressions, clicks, share, eCPM
with the prior window), KPIs against the prior window of the same
length, and a per-ad-zone breakdown with a health hint.
**Money is in currency units (not cents)**: `earned*`, `avg_ecpm`,
`ecpm_*` and the revenue/eCPM series. Impressions count views +
clicks (click-only ad types log as clicks).


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
    api_instance = goadserver.SmartZonesApi(api_client)
    siteid = 56 # int | 
    var_from = '2013-10-20' # date | Inclusive start. Defaults to 6 days ago (both `from` and `to` must be sent to override). (optional)
    to = '2013-10-20' # date | Inclusive end. Defaults to today. (optional)
    basis = imp # str | Share basis — impressions or earnings. (optional) (default to imp)

    try:
        # Traffic and earnings split across networks for one site.
        api_instance.api_v1_publisher_smartzones_distribution_per_site_get(siteid, var_from=var_from, to=to, basis=basis)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_distribution_per_site_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteid** | **int**|  | 
 **var_from** | **date**| Inclusive start. Defaults to 6 days ago (both &#x60;from&#x60; and &#x60;to&#x60; must be sent to override). | [optional] 
 **to** | **date**| Inclusive end. Defaults to today. | [optional] 
 **basis** | **str**| Share basis — impressions or earnings. | [optional] [default to imp]

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
**200** | Distribution. |  -  |
**400** | &#x60;bad_request&#x60; — &#x60;siteid&#x60; missing. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_distribution_sites_get**
> api_v1_publisher_smartzones_distribution_sites_get()

Sites that carry smart zones.

Your sites with at least one live smart zone on a network, with ad zone and zone counts — the picker for the per-site distribution view.

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
    api_instance = goadserver.SmartZonesApi(api_client)

    try:
        # Sites that carry smart zones.
        api_instance.api_v1_publisher_smartzones_distribution_sites_get()
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_distribution_sites_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Sites. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_get**
> api_v1_publisher_smartzones_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, network_id=network_id, siteid=siteid, spaceid=spaceid, select_type=select_type, adzone_typeid=adzone_typeid, status=status, filter_id=filter_id, filter_name=filter_name, filter_adzone_name=filter_adzone_name)

List smart zones.

Smart zones hang under one of your ad zones and send part of its
traffic to an outside ad network (or, with `smart_networkid = 0`,
split your own inventory). The same list the panel's Smart Zones page
shows. Paginated with `page` / `per_page` (max 2000).

Keys pinned to `adzone_ids` or `site_ids` are refused with
`403 forbidden_resource` on every smart-zone route: a smart zone, its
network accounts and the import span zones the pin cannot follow.


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
    api_instance = goadserver.SmartZonesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    network_id = 56 # int | Only zones on this smart network account (`smart_networkid`). (optional)
    siteid = 56 # int | Only zones under this site. `site_id` is accepted too. (optional)
    spaceid = 56 # int | Only zones under this ad zone. (optional)
    select_type = 56 # int | 0 = percentage, 1 = eCPM, 2 = RTB, 3 = eCPM + limit %. (optional)
    adzone_typeid = 56 # int | Only zones whose parent ad zone has this type id. (optional)
    status = 'status_example' # str |  (optional)
    filter_id = 56 # int |  (optional)
    filter_name = 'filter_name_example' # str | Substring match on the zone name. (optional)
    filter_adzone_name = 'filter_adzone_name_example' # str | Substring match on the parent ad zone name. (optional)

    try:
        # List smart zones.
        api_instance.api_v1_publisher_smartzones_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, network_id=network_id, siteid=siteid, spaceid=spaceid, select_type=select_type, adzone_typeid=adzone_typeid, status=status, filter_id=filter_id, filter_name=filter_name, filter_adzone_name=filter_adzone_name)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **network_id** | **int**| Only zones on this smart network account (&#x60;smart_networkid&#x60;). | [optional] 
 **siteid** | **int**| Only zones under this site. &#x60;site_id&#x60; is accepted too. | [optional] 
 **spaceid** | **int**| Only zones under this ad zone. | [optional] 
 **select_type** | **int**| 0 &#x3D; percentage, 1 &#x3D; eCPM, 2 &#x3D; RTB, 3 &#x3D; eCPM + limit %. | [optional] 
 **adzone_typeid** | **int**| Only zones whose parent ad zone has this type id. | [optional] 
 **status** | **str**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_name** | **str**| Substring match on the zone name. | [optional] 
 **filter_adzone_name** | **str**| Substring match on the parent ad zone name. | [optional] 

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
**200** | One page of smart zones. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_id_delete**
> api_v1_publisher_smartzones_id_delete(id)

Delete a smart zone.

Soft delete (`isdeleted = 1`). There is no recover route; recreate the zone instead.

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
    api_instance = goadserver.SmartZonesApi(api_client)
    id = 56 # int | 

    try:
        # Delete a smart zone.
        api_instance.api_v1_publisher_smartzones_id_delete(id)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_id_delete: %s\n" % e)
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
**404** | &#x60;smart_zone_not_found&#x60; (also when already deleted). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_id_get**
> api_v1_publisher_smartzones_id_get(id)

Get one smart zone.

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
    api_instance = goadserver.SmartZonesApi(api_client)
    id = 56 # int | 

    try:
        # Get one smart zone.
        api_instance.api_v1_publisher_smartzones_id_get(id)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_id_get: %s\n" % e)
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
**200** | The zone. &#x60;creative&#x60; and &#x60;settings&#x60; are JSON-encoded strings, exactly as written. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;smart_zone_not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_id_put**
> api_v1_publisher_smartzones_id_put(id, api_v1_publisher_smartzones_id_put_request)

Update a smart zone.

Partial update: only the keys you send are written. Moving the zone
to another ad zone (`spaceid`) is allowed; the new ad zone must be
one of your live ones and `siteid` follows it (a bare `siteid` is
ignored). Changing `smart_networkid` re-derives the catalogue
`networkid`; both it and `ssp_campaignid` must be your own.
Booleans may be sent as `true`/`false` or `1`/`0`.

Unknown body fields are refused with `422 unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_smartzones_id_put_request import ApiV1PublisherSmartzonesIdPutRequest
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
    api_instance = goadserver.SmartZonesApi(api_client)
    id = 56 # int | 
    api_v1_publisher_smartzones_id_put_request = {"is_active":false} # ApiV1PublisherSmartzonesIdPutRequest | 

    try:
        # Update a smart zone.
        api_instance.api_v1_publisher_smartzones_id_put(id, api_v1_publisher_smartzones_id_put_request)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_publisher_smartzones_id_put_request** | [**ApiV1PublisherSmartzonesIdPutRequest**](ApiV1PublisherSmartzonesIdPutRequest.md)|  | 

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
**200** | Saved (also when nothing changed). |  -  |
**400** | &#x60;invalid_json&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;smart_zone_not_found&#x60;, or &#x60;network_not_found&#x60; for a &#x60;smart_networkid&#x60; that is not yours. |  -  |
**422** | &#x60;validation_error&#x60; (&#x60;select_type&#x60;, &#x60;spaceid&#x60;, &#x60;ssp_campaignid&#x60;) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_import_post**
> api_v1_publisher_smartzones_import_post(api_v1_publisher_smartzones_import_post_request)

Bulk import smart zones.

Creates (or, when a zone with the same name already exists under the
same ad zone, overwrites) one smart zone per `zones[]` entry, all on
one network account. Entries without a `spaceid` or `url`, or whose
ad zone is not one of your live ones, are skipped; `imported` counts
the rows written. Each zone's site is its ad zone's site (the
top-level `siteid` is ignored). Imported zones are active.

Unknown top-level body fields are refused with `422 unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_smartzones_import_post_request import ApiV1PublisherSmartzonesImportPostRequest
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
    api_instance = goadserver.SmartZonesApi(api_client)
    api_v1_publisher_smartzones_import_post_request = {"smart_network_id":14,"network_id":3,"select_type":1,"select_pct":20,"settings":{"skip_when_stats":1},"zones":[{"spaceid":4471,"name":"Exo 728 DE","zoneid":"12345","url":"https://a.network.example/zone/12345","device_type_ids":[1]}]} # ApiV1PublisherSmartzonesImportPostRequest | 

    try:
        # Bulk import smart zones.
        api_instance.api_v1_publisher_smartzones_import_post(api_v1_publisher_smartzones_import_post_request)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_smartzones_import_post_request** | [**ApiV1PublisherSmartzonesImportPostRequest**](ApiV1PublisherSmartzonesImportPostRequest.md)|  | 

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
**200** | Imported. |  -  |
**400** | &#x60;invalid_network&#x60; (no &#x60;smart_network_id&#x60;), &#x60;no_zones&#x60;, &#x60;invalid_select_type&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;network_not_found&#x60;. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_networks_get**
> api_v1_publisher_smartzones_networks_get()

List your smart network accounts.

Your accounts on outside ad networks (the "Networks" tab).
`available_networks` lists the catalogue networks you can add, with
the credential flags each needs.

**Credentials are masked on the API:** `apikey` and every string in
`api_data` come back as `****` + their last 4 characters
(`has_apikey` says whether a key is stored). Writing a masked value
back through `POST .../networks` keeps the stored secret, so a
read-modify-write round trip is safe; send the real value to change it.


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
    api_instance = goadserver.SmartZonesApi(api_client)

    try:
        # List your smart network accounts.
        api_instance.api_v1_publisher_smartzones_networks_get()
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_networks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Accounts. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_networks_id_delete**
> api_v1_publisher_smartzones_networks_id_delete(id)

Remove a smart network account.

Hard delete. Refused while any live smart zone still uses the account.

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
    api_instance = goadserver.SmartZonesApi(api_client)
    id = 56 # int | 

    try:
        # Remove a smart network account.
        api_instance.api_v1_publisher_smartzones_networks_id_delete(id)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_networks_id_delete: %s\n" % e)
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
**200** | Removed. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;network_not_found&#x60;. |  -  |
**422** | &#x60;has_active_zones&#x60; — delete or move its smart zones first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_networks_post**
> api_v1_publisher_smartzones_networks_post(api_v1_publisher_smartzones_networks_post_request)

Add or update a smart network account.

Without `id` (or `id: 0`) creates an account; with the `id` of one
of yours updates it (every field is rewritten — send the full
object). `name` + `prepend_name` must be unique among your accounts.
Empty credential pairs are dropped from `api_data`, and a set
`apikey` removes `username`/`userpass`.

Unknown body fields are refused with `422 unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_smartzones_networks_post_request import ApiV1PublisherSmartzonesNetworksPostRequest
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
    api_instance = goadserver.SmartZonesApi(api_client)
    api_v1_publisher_smartzones_networks_post_request = {"name":"ExoClick main","networkid":3,"currency":"USD","is_active":1,"pullstats":1,"apikey":"xxxxxxxx","api_data":{"userid":"998877"}} # ApiV1PublisherSmartzonesNetworksPostRequest | 

    try:
        # Add or update a smart network account.
        api_instance.api_v1_publisher_smartzones_networks_post(api_v1_publisher_smartzones_networks_post_request)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_smartzones_networks_post_request** | [**ApiV1PublisherSmartzonesNetworksPostRequest**](ApiV1PublisherSmartzonesNetworksPostRequest.md)|  | 

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; (&#x60;name&#x60; required or duplicate) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_post**
> api_v1_publisher_smartzones_post(api_v1_publisher_smartzones_post_request)

Create a smart zone.

Creates a smart zone under one of your live ad zones. The zone's
`siteid` is always taken from the ad zone (a `siteid` in the body is
ignored). With no network (`smart_networkid` 0 or omitted) the
selection type is forced to percentage, because eCPM and RTB need an
upstream network to rank against.

Unknown body fields are refused with `422 unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_smartzones_post_request import ApiV1PublisherSmartzonesPostRequest
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
    api_instance = goadserver.SmartZonesApi(api_client)
    api_v1_publisher_smartzones_post_request = {"name":"Exo backfill — DE mobile","spaceid":4471,"smart_networkid":14,"countries":"DE,AT","device_type_ids":"3","is_active":true,"select_type":1,"select_pct":30,"creative":"{\"creative\":{\"type\":\"url\",\"value\":\"https://a.network.example/zone/12345\"}}","settings":"{\"skip_when_stats\":1}","network_zoneid":12345} # ApiV1PublisherSmartzonesPostRequest | 

    try:
        # Create a smart zone.
        api_instance.api_v1_publisher_smartzones_post(api_v1_publisher_smartzones_post_request)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_smartzones_post_request** | [**ApiV1PublisherSmartzonesPostRequest**](ApiV1PublisherSmartzonesPostRequest.md)|  | 

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
**201** | Created. |  -  |
**400** | &#x60;invalid_json&#x60; — the body is not JSON or a field has the wrong JSON type. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | &#x60;network_not_found&#x60; — &#x60;smart_networkid&#x60; is not one of your network accounts. |  -  |
**422** | &#x60;validation_error&#x60; (&#x60;name&#x60;, &#x60;smart_networkid&#x60;, &#x60;select_type&#x60;, &#x60;spaceid&#x60; — not your live ad zone, &#x60;ssp_campaignid&#x60; — not your SSP campaign) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_setup_data_get**
> api_v1_publisher_smartzones_setup_data_get()

Lookups for the smart-zone form.

Everything the create/update body refers to: countries, device
types (empty when device targeting is off for the tenant), your
websites and live ad zones, the ad zone types you use, and the
network catalogue (`smartzone_networks`) with the per-network flags
that say which credentials and ids that network needs.


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
    api_instance = goadserver.SmartZonesApi(api_client)

    try:
        # Lookups for the smart-zone form.
        api_instance.api_v1_publisher_smartzones_setup_data_get()
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_setup_data_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Lookups. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_smartzones_ssp_campaigns_get**
> api_v1_publisher_smartzones_ssp_campaigns_get(networkid, adtypeid=adtypeid)

SSP campaigns usable as a smart zone's RTB feed.

Your active RTB-feed SSP campaigns (`ssptype = ssp`, `use_type = 2`)
on the RTB network that matches the catalogue network `networkid`,
optionally narrowed to one ad type. Empty when the network has no
RTB twin.


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
    api_instance = goadserver.SmartZonesApi(api_client)
    networkid = 56 # int | Catalogue network id (setup-data `smartzone_networks[].id`).
    adtypeid = 56 # int | Ad type id of the parent ad zone. (optional)

    try:
        # SSP campaigns usable as a smart zone's RTB feed.
        api_instance.api_v1_publisher_smartzones_ssp_campaigns_get(networkid, adtypeid=adtypeid)
    except Exception as e:
        print("Exception when calling SmartZonesApi->api_v1_publisher_smartzones_ssp_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkid** | **int**| Catalogue network id (setup-data &#x60;smartzone_networks[].id&#x60;). | 
 **adtypeid** | **int**| Ad type id of the parent ad zone. | [optional] 

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
**200** | Candidates. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


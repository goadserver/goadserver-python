# goadserver.AdScannerApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_ad_scanner_get**](AdScannerApi.md#api_v1_ad_scanner_get) | **GET** /api/v1/ad-scanner | List scan tasks.
[**api_v1_ad_scanner_id_delete**](AdScannerApi.md#api_v1_ad_scanner_id_delete) | **DELETE** /api/v1/ad-scanner/{id} | Delete a scan task.
[**api_v1_ad_scanner_id_ignore_domain_put**](AdScannerApi.md#api_v1_ad_scanner_id_ignore_domain_put) | **PUT** /api/v1/ad-scanner/{id}/ignore-domain | Ignore (or un-ignore) a flagged domain on a task.
[**api_v1_ad_scanner_id_manual_items_get**](AdScannerApi.md#api_v1_ad_scanner_id_manual_items_get) | **GET** /api/v1/ad-scanner/{id}/manual-items | List a manual task&#39;s items.
[**api_v1_ad_scanner_id_manual_items_item_id_state_put**](AdScannerApi.md#api_v1_ad_scanner_id_manual_items_item_id_state_put) | **PUT** /api/v1/ad-scanner/{id}/manual-items/{itemId}/state | Pause, resume or delete a manual item.
[**api_v1_ad_scanner_id_manual_items_post**](AdScannerApi.md#api_v1_ad_scanner_id_manual_items_post) | **POST** /api/v1/ad-scanner/{id}/manual-items | Add or edit a manual item.
[**api_v1_ad_scanner_id_put**](AdScannerApi.md#api_v1_ad_scanner_id_put) | **PUT** /api/v1/ad-scanner/{id} | Replace a task&#39;s name, tags and config.
[**api_v1_ad_scanner_id_toggle_active_put**](AdScannerApi.md#api_v1_ad_scanner_id_toggle_active_put) | **PUT** /api/v1/ad-scanner/{id}/toggle-active | Start or stop a scan task.
[**api_v1_ad_scanner_post**](AdScannerApi.md#api_v1_ad_scanner_post) | **POST** /api/v1/ad-scanner | Create a scan task.
[**api_v1_ad_scanner_report_hash_get**](AdScannerApi.md#api_v1_ad_scanner_report_hash_get) | **GET** /api/v1/ad-scanner/report/{hash} | One scan&#39;s full report.
[**api_v1_ad_scanner_reports_get**](AdScannerApi.md#api_v1_ad_scanner_reports_get) | **GET** /api/v1/ad-scanner/reports | List scan results.
[**api_v1_ad_scanner_stats_get**](AdScannerApi.md#api_v1_ad_scanner_stats_get) | **GET** /api/v1/ad-scanner/stats | Scan volume and proxy bandwidth.
[**api_v1_ad_scanner_tags_get**](AdScannerApi.md#api_v1_ad_scanner_tags_get) | **GET** /api/v1/ad-scanner/tags | Tags used on the account&#39;s scan tasks.


# **api_v1_ad_scanner_get**
> api_v1_ad_scanner_get()

List scan tasks.

A bare array; `config` decoded, `tags` split into an array.

`coverage` — what the task's next run would scan, `{count, reason}`
(`null` for `campaigns` targets). When `count` is 0 the task produces
no reports, and `reason` says why: `no_smart_zones`, `scanning_off`
(no smart zone the task covers has Scanning on), `no_matching_zones` (no zone of an
ad type this scan type covers, or none in the chosen networks),
`no_recent_traffic` (no matching zone served in the last 5 days),
`no_items` (manual task without active items) or
`no_matching_items` (manual items of the wrong type for this scan
type). `reason` is empty when `count` > 0.


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
    api_instance = goadserver.AdScannerApi(api_client)

    try:
        # List scan tasks.
        api_instance.api_v1_ad_scanner_get()
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_get: %s\n" % e)
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
**200** | Tasks. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_delete**
> api_v1_ad_scanner_id_delete(id)

Delete a scan task.

Soft delete; the task stops scanning.

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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 

    try:
        # Delete a scan task.
        api_instance.api_v1_ad_scanner_id_delete(id)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_delete: %s\n" % e)
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
**404** | Task not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_ignore_domain_put**
> api_v1_ad_scanner_id_ignore_domain_put(id, api_v1_ad_scanner_id_ignore_domain_put_request)

Ignore (or un-ignore) a flagged domain on a task.

Toggles `value` in the task's `config.detection.domains.ignored`
list: added when absent, removed when present. `type` must be
`detection.domains.ignore`. Answers 200 `{success: false}` when the
type / value is wrong or the task is not the caller's.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_id_ignore_domain_put_request import ApiV1AdScannerIdIgnoreDomainPutRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 
    api_v1_ad_scanner_id_ignore_domain_put_request = {"type":"detection.domains.ignore","value":"cdn.example.net"} # ApiV1AdScannerIdIgnoreDomainPutRequest | 

    try:
        # Ignore (or un-ignore) a flagged domain on a task.
        api_instance.api_v1_ad_scanner_id_ignore_domain_put(id, api_v1_ad_scanner_id_ignore_domain_put_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_ignore_domain_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_ad_scanner_id_ignore_domain_put_request** | [**ApiV1AdScannerIdIgnoreDomainPutRequest**](ApiV1AdScannerIdIgnoreDomainPutRequest.md)|  | 

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
**200** | Result. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_manual_items_get**
> api_v1_ad_scanner_id_manual_items_get(id)

List a manual task's items.

The URLs / tags a `target: manual` task scans. Bare array (empty for an unknown task).

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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 

    try:
        # List a manual task's items.
        api_instance.api_v1_ad_scanner_id_manual_items_get(id)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_manual_items_get: %s\n" % e)
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
**200** | Items. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_manual_items_item_id_state_put**
> api_v1_ad_scanner_id_manual_items_item_id_state_put(id, item_id, api_v1_ad_scanner_id_manual_items_item_id_state_put_request)

Pause, resume or delete a manual item.

`fld` = `isactive` (default) or `isdeleted`; `value` 0 / 1. Deleting
also deactivates. 200 `{success: false}` when the item is not the
caller's.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_id_manual_items_item_id_state_put_request import ApiV1AdScannerIdManualItemsItemIdStatePutRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 
    api_v1_ad_scanner_id_manual_items_item_id_state_put_request = {"fld":"isdeleted","value":1} # ApiV1AdScannerIdManualItemsItemIdStatePutRequest | 

    try:
        # Pause, resume or delete a manual item.
        api_instance.api_v1_ad_scanner_id_manual_items_item_id_state_put(id, item_id, api_v1_ad_scanner_id_manual_items_item_id_state_put_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_manual_items_item_id_state_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 
 **api_v1_ad_scanner_id_manual_items_item_id_state_put_request** | [**ApiV1AdScannerIdManualItemsItemIdStatePutRequest**](ApiV1AdScannerIdManualItemsItemIdStatePutRequest.md)|  | 

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
**200** | Result. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_manual_items_post**
> api_v1_ad_scanner_id_manual_items_post(id, api_v1_ad_scanner_id_manual_items_post_request)

Add or edit a manual item.

Without `id` adds an item; with `id` edits that item. `type` = url
(default), html, iframe or vast_url; `value` is required. Failures
(no value, task not the caller's) answer 200 `{success: false}`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_id_manual_items_post_request import ApiV1AdScannerIdManualItemsPostRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 
    api_v1_ad_scanner_id_manual_items_post_request = {"value":"https://lander.example.com/","type":"url","description":"Main lander","isactive":1} # ApiV1AdScannerIdManualItemsPostRequest | 

    try:
        # Add or edit a manual item.
        api_instance.api_v1_ad_scanner_id_manual_items_post(id, api_v1_ad_scanner_id_manual_items_post_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_manual_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_ad_scanner_id_manual_items_post_request** | [**ApiV1AdScannerIdManualItemsPostRequest**](ApiV1AdScannerIdManualItemsPostRequest.md)|  | 

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
**200** | Result. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_put**
> api_v1_ad_scanner_id_put(id, api_v1_ad_scanner_id_put_request)

Replace a task's name, tags and config.

Full replace of these three: a `config` or `tags` left out is
cleared, so send the whole task. `target` / `scan_type` /
`adtypeid` are fixed at create.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_id_put_request import ApiV1AdScannerIdPutRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 
    api_v1_ad_scanner_id_put_request = {"name":"Landing pages","tags":["daily"],"config":{"interval":{"type":"daily","amount":1}}} # ApiV1AdScannerIdPutRequest | 

    try:
        # Replace a task's name, tags and config.
        api_instance.api_v1_ad_scanner_id_put(id, api_v1_ad_scanner_id_put_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_ad_scanner_id_put_request** | [**ApiV1AdScannerIdPutRequest**](ApiV1AdScannerIdPutRequest.md)|  | 

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
**404** | Task not found. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_id_toggle_active_put**
> api_v1_ad_scanner_id_toggle_active_put(id, api_v1_ad_scanner_id_toggle_active_put_request=api_v1_ad_scanner_id_toggle_active_put_request)

Start or stop a scan task.

`is_active` > 0 starts it; 0 or no body stops it.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_id_toggle_active_put_request import ApiV1AdScannerIdToggleActivePutRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    id = 56 # int | 
    api_v1_ad_scanner_id_toggle_active_put_request = {"is_active":1} # ApiV1AdScannerIdToggleActivePutRequest |  (optional)

    try:
        # Start or stop a scan task.
        api_instance.api_v1_ad_scanner_id_toggle_active_put(id, api_v1_ad_scanner_id_toggle_active_put_request=api_v1_ad_scanner_id_toggle_active_put_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_id_toggle_active_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_ad_scanner_id_toggle_active_put_request** | [**ApiV1AdScannerIdToggleActivePutRequest**](ApiV1AdScannerIdToggleActivePutRequest.md)|  | [optional] 

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
**404** | Task not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_post**
> api_v1_ad_scanner_post(api_v1_ad_scanner_post_request)

Create a scan task.

- `target` — `campaigns` (your own campaigns' ads), `smartzones`
  (default) or `manual` (items you add under
  …/{id}/manual-items). Unknown values become `smartzones`.
- `scan_type` — `ad_scan` (default), `url_scan` or `vast_scan`.
- `config` — only these keys are kept: `smartzone_networks`,
  `device_types`, `browsers` `{items, random}`, `interval`
  `{type: minutely|hourly|daily, amount}`, `detection` (push,
  alerts, popups, cookies, crypto_miners, `domains` `{on, malicious,
  suspicious, ignored[], ignore_dates}`, `suspicious_dom`,
  `fingerprinting`, `obfuscated_js`, `permission`,
  `scan_landing_ads`, `max_landing_ad_scans`), `proxy` `{on,
  locations[]}`, `notify` `{enabled, level: all|serious, dest}`.
- `tags` — a CSV string or an array of strings.

`target`, `scan_type` and `adtypeid` cannot change later. The task
starts active. Proxy scans use metered bandwidth.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_ad_scanner_post_request import ApiV1AdScannerPostRequest
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
    api_instance = goadserver.AdScannerApi(api_client)
    api_v1_ad_scanner_post_request = {"name":"Landing pages","target":"campaigns","scan_type":"url_scan","tags":["daily"],"config":{"interval":{"type":"hourly","amount":1},"detection":{"push":true,"popups":true,"domains":{"true":true,"malicious":true,"suspicious":true}},"notify":{"enabled":true,"level":"serious","dest":0}}} # ApiV1AdScannerPostRequest | 

    try:
        # Create a scan task.
        api_instance.api_v1_ad_scanner_post(api_v1_ad_scanner_post_request)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_ad_scanner_post_request** | [**ApiV1AdScannerPostRequest**](ApiV1AdScannerPostRequest.md)|  | 

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; (name missing) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_report_hash_get**
> api_v1_ad_scanner_report_hash_get(hash)

One scan's full report.

The browser report of a single scan (`uid` from the results list):
events, redirects, requests, findings, plus the task config. Only
the caller's own scans — another account's uid is 404.


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
    api_instance = goadserver.AdScannerApi(api_client)
    hash = 'hash_example' # str | 

    try:
        # One scan's full report.
        api_instance.api_v1_ad_scanner_report_hash_get(hash)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_report_hash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  | 

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
**200** | Report. |  -  |
**404** | &#x60;HASH_DOES_NOT_EXIST&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_reports_get**
> api_v1_ad_scanner_reports_get(datestart=datestart, dateend=dateend, scan_type=scan_type, scan_target=scan_target, scan_state=scan_state, page=page)

List scan results.

One row per scan, 2500 per page (`page`). Defaults to today.
`scan_state` 1 = scans that found something, 0 = clean. Rows carry
`uid` (open the full report with GET …/report/{uid}), `task_name`
and `scanned_item`.


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
    api_instance = goadserver.AdScannerApi(api_client)
    datestart = '2013-10-20' # date |  (optional)
    dateend = '2013-10-20' # date |  (optional)
    scan_type = 'scan_type_example' # str |  (optional)
    scan_target = 'scan_target_example' # str |  (optional)
    scan_state = 56 # int |  (optional)
    page = 1 # int |  (optional) (default to 1)

    try:
        # List scan results.
        api_instance.api_v1_ad_scanner_reports_get(datestart=datestart, dateend=dateend, scan_type=scan_type, scan_target=scan_target, scan_state=scan_state, page=page)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datestart** | **date**|  | [optional] 
 **dateend** | **date**|  | [optional] 
 **scan_type** | **str**|  | [optional] 
 **scan_target** | **str**|  | [optional] 
 **scan_state** | **int**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]

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
**200** | Results. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_stats_get**
> api_v1_ad_scanner_stats_get(datestart=datestart, dateend=dateend, stats_selcols=stats_selcols, config_id=config_id, country=country, proxy_used=proxy_used)

Scan volume and proxy bandwidth.

Totals grouped by `stats_selcols` (CSV of scandate, config_id,
country; default scandate). `bandwidth` is proxy bytes used.


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
    api_instance = goadserver.AdScannerApi(api_client)
    datestart = '2013-10-20' # date |  (optional)
    dateend = '2013-10-20' # date |  (optional)
    stats_selcols = 'scandate,config_id' # str |  (optional)
    config_id = 56 # int |  (optional)
    country = 'country_example' # str |  (optional)
    proxy_used = 56 # int |  (optional)

    try:
        # Scan volume and proxy bandwidth.
        api_instance.api_v1_ad_scanner_stats_get(datestart=datestart, dateend=dateend, stats_selcols=stats_selcols, config_id=config_id, country=country, proxy_used=proxy_used)
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datestart** | **date**|  | [optional] 
 **dateend** | **date**|  | [optional] 
 **stats_selcols** | **str**|  | [optional] 
 **config_id** | **int**|  | [optional] 
 **country** | **str**|  | [optional] 
 **proxy_used** | **int**|  | [optional] 

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
**200** | Rows. |  -  |
**500** | Stats store unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ad_scanner_tags_get**
> api_v1_ad_scanner_tags_get()

Tags used on the account's scan tasks.

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
    api_instance = goadserver.AdScannerApi(api_client)

    try:
        # Tags used on the account's scan tasks.
        api_instance.api_v1_ad_scanner_tags_get()
    except Exception as e:
        print("Exception when calling AdScannerApi->api_v1_ad_scanner_tags_get: %s\n" % e)
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
**200** | Sorted distinct tags. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


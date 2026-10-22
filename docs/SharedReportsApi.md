# goadserver.SharedReportsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_shared_reports_get**](SharedReportsApi.md#api_v1_shared_reports_get) | **GET** /api/v1/shared-reports | List shared reports.
[**api_v1_shared_reports_id_delete**](SharedReportsApi.md#api_v1_shared_reports_id_delete) | **DELETE** /api/v1/shared-reports/{id} | Delete a shared report.
[**api_v1_shared_reports_id_get**](SharedReportsApi.md#api_v1_shared_reports_id_get) | **GET** /api/v1/shared-reports/{id} | Show a shared report.
[**api_v1_shared_reports_id_put**](SharedReportsApi.md#api_v1_shared_reports_id_put) | **PUT** /api/v1/shared-reports/{id} | Update a shared report.
[**api_v1_shared_reports_id_toggle_active_put**](SharedReportsApi.md#api_v1_shared_reports_id_toggle_active_put) | **PUT** /api/v1/shared-reports/{id}/toggle-active | Switch a report&#39;s link on or off.
[**api_v1_shared_reports_post**](SharedReportsApi.md#api_v1_shared_reports_post) | **POST** /api/v1/shared-reports | Create a shared report.
[**api_v1_shared_reports_setup_data_get**](SharedReportsApi.md#api_v1_shared_reports_setup_data_get) | **GET** /api/v1/shared-reports/setup-data | Campaigns and sites a report can cover.


# **api_v1_shared_reports_get**
> api_v1_shared_reports_get(page=page, per_page=per_page, search=search, filter_isactive=filter_isactive)

List shared reports.

Advertiser / publisher / SSP / DSP reports (tracker reports are listed
in the tracker section of the panel; they can still be read and
changed here by id). Each row carries the public `url` and the
DSA-transparency `dsa_url`. `filter_isactive` = 0 / 1, `search`
matches the name.


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
    api_instance = goadserver.SharedReportsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    filter_isactive = 56 # int |  (optional)

    try:
        # List shared reports.
        api_instance.api_v1_shared_reports_get(page=page, per_page=per_page, search=search, filter_isactive=filter_isactive)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **filter_isactive** | **int**|  | [optional] 

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
**200** | Reports. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_id_delete**
> api_v1_shared_reports_id_delete(id)

Delete a shared report.

The link stops working immediately.

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
    api_instance = goadserver.SharedReportsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a shared report.
        api_instance.api_v1_shared_reports_id_delete(id)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_id_delete: %s\n" % e)
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
**403** | Missing scope, or &#x60;forbidden_resource&#x60; (pinned key). |  -  |
**404** | Report not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_id_get**
> api_v1_shared_reports_id_get(id)

Show a shared report.

The stored row with `campaigns` / `sites` / `settings` / `options` decoded.

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
    api_instance = goadserver.SharedReportsApi(api_client)
    id = 56 # int | 

    try:
        # Show a shared report.
        api_instance.api_v1_shared_reports_id_get(id)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_id_get: %s\n" % e)
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
**200** | The report. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Report not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_id_put**
> api_v1_shared_reports_id_put(id, api_v1_shared_reports_id_put_request)

Update a shared report.

Partial: `name` (non-empty), `tagids` and each of `campaigns` /
`sites` / `settings` / `options` replace the stored value when
sent. `statstype` cannot change (create a new report) — sending it
is 422 `unknown_fields`. The link (`hash`) stays the same.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_shared_reports_id_put_request import ApiV1SharedReportsIdPutRequest
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
    api_instance = goadserver.SharedReportsApi(api_client)
    id = 56 # int | 
    api_v1_shared_reports_id_put_request = {"campaigns":[{"id":812,"type":"ron"},{"id":813,"type":"ron"}]} # ApiV1SharedReportsIdPutRequest | 

    try:
        # Update a shared report.
        api_instance.api_v1_shared_reports_id_put(id, api_v1_shared_reports_id_put_request)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_shared_reports_id_put_request** | [**ApiV1SharedReportsIdPutRequest**](ApiV1SharedReportsIdPutRequest.md)|  | 

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
**400** | &#x60;no_fields&#x60;. |  -  |
**403** | Missing scope, or &#x60;forbidden_resource&#x60; (pinned key). |  -  |
**404** | Report not found. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_id_toggle_active_put**
> api_v1_shared_reports_id_toggle_active_put(id)

Switch a report's link on or off.

No body — flips `isactive`; an inactive link answers 404 to viewers.

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
    api_instance = goadserver.SharedReportsApi(api_client)
    id = 56 # int | 

    try:
        # Switch a report's link on or off.
        api_instance.api_v1_shared_reports_id_toggle_active_put(id)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_id_toggle_active_put: %s\n" % e)
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
**200** | New state. |  -  |
**403** | Missing scope, or &#x60;forbidden_resource&#x60; (pinned key). |  -  |
**404** | Report not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_post**
> api_v1_shared_reports_post(shared_report_body)

Create a shared report.

Mints a public link (`data.url`) that shows the chosen stats to
anyone who has it, without a login. Scope:

- `statstype` — advertiser (default), publisher, ssp, dsp or tracker.
- `campaigns` — `[{id, type}]` (type ron / cpm / flatrate /
  directdeal); empty with no `settings` = an empty report.
  `settings.follow_groups: true` plus `tagids` adds every campaign
  currently filed under those tags (advertiser reports only).
- `sites` — `[{id}]` for publisher reports.
- `settings` — viewer filters and layout: `ad_types`,
  `selling_types`, `device_types` (id arrays), `countries` (codes),
  `visible_metrics`, `visible_conv_types`, `allowed_groupby`,
  `default_groupby` (default `period`), `allowed_viewtypes`,
  `viewer_filters`, `follow_groups`, `show_names` (false hides
  entity names).
- `options` — stats adjustment shown to viewers
  (`{on, impressions|clicks|paid: {on, type: increase|decrease, value}}`);
  dropped unless the account holds the `adjust_stats` right.

Ids are only ever reported within the caller's own stats. Unknown
top-level fields → 422 `unknown_fields`. GET
/api/v1/shared-reports/setup-data lists the pickable campaigns and
sites.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.shared_report_body import SharedReportBody
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
    api_instance = goadserver.SharedReportsApi(api_client)
    shared_report_body = {"name":"Client A — weekly","statstype":"advertiser","campaigns":[{"id":812,"type":"ron"}],"settings":{"countries":["us"],"visible_metrics":["views","clicks","ctr","spent"],"follow_groups":true},"tagids":"5"} # SharedReportBody | 

    try:
        # Create a shared report.
        api_instance.api_v1_shared_reports_post(shared_report_body)
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_report_body** | [**SharedReportBody**](SharedReportBody.md)|  | 

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
**403** | Missing scope, or &#x60;forbidden_resource&#x60; — the key is pinned to resources. |  -  |
**422** | &#x60;validation_error&#x60; (name missing) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_shared_reports_setup_data_get**
> api_v1_shared_reports_setup_data_get()

Campaigns and sites a report can cover.

The account's live campaigns (`{id, name, type}`) and sites, the
panel host the links are built on, and whether `options` (stats
adjustment) is honoured for this account.


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
    api_instance = goadserver.SharedReportsApi(api_client)

    try:
        # Campaigns and sites a report can cover.
        api_instance.api_v1_shared_reports_setup_data_get()
    except Exception as e:
        print("Exception when calling SharedReportsApi->api_v1_shared_reports_setup_data_get: %s\n" % e)
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
**200** | Pickers. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


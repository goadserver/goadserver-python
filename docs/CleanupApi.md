# goadserver.CleanupApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_cleanup_advertiser_archived_get**](CleanupApi.md#api_v1_cleanup_advertiser_archived_get) | **GET** /api/v1/cleanup/advertiser/archived | Archived advertiser items that can be purged.
[**api_v1_cleanup_advertiser_export_get**](CleanupApi.md#api_v1_cleanup_advertiser_export_get) | **GET** /api/v1/cleanup/advertiser/export | Download the advertiser cleanup candidates.
[**api_v1_cleanup_advertiser_get**](CleanupApi.md#api_v1_cleanup_advertiser_get) | **GET** /api/v1/cleanup/advertiser | List advertiser items that no longer serve.
[**api_v1_cleanup_advertiser_linked_get**](CleanupApi.md#api_v1_cleanup_advertiser_linked_get) | **GET** /api/v1/cleanup/advertiser/linked | What still uses advertiser cleanup rows.
[**api_v1_cleanup_advertiser_purge_post**](CleanupApi.md#api_v1_cleanup_advertiser_purge_post) | **POST** /api/v1/cleanup/advertiser/purge | Purge archived advertiser items for good.
[**api_v1_cleanup_advertiser_runs_get**](CleanupApi.md#api_v1_cleanup_advertiser_runs_get) | **GET** /api/v1/cleanup/advertiser/runs | Recent advertiser cleanup runs.
[**api_v1_cleanup_advertiser_runs_id_get**](CleanupApi.md#api_v1_cleanup_advertiser_runs_id_get) | **GET** /api/v1/cleanup/advertiser/runs/{id} | One advertiser cleanup run with its items.
[**api_v1_cleanup_advertiser_runs_id_undone_post**](CleanupApi.md#api_v1_cleanup_advertiser_runs_id_undone_post) | **POST** /api/v1/cleanup/advertiser/runs/{id}/undone | Mark a advertiser cleanup run as undone.
[**api_v1_cleanup_advertiser_runs_post**](CleanupApi.md#api_v1_cleanup_advertiser_runs_post) | **POST** /api/v1/cleanup/advertiser/runs | Record a advertiser cleanup run.
[**api_v1_cleanup_advertiser_summary_get**](CleanupApi.md#api_v1_cleanup_advertiser_summary_get) | **GET** /api/v1/cleanup/advertiser/summary | Count the advertiser cleanup candidates per kind.
[**api_v1_cleanup_publisher_archived_get**](CleanupApi.md#api_v1_cleanup_publisher_archived_get) | **GET** /api/v1/cleanup/publisher/archived | Archived publisher items that can be purged.
[**api_v1_cleanup_publisher_export_get**](CleanupApi.md#api_v1_cleanup_publisher_export_get) | **GET** /api/v1/cleanup/publisher/export | Download the publisher cleanup candidates.
[**api_v1_cleanup_publisher_get**](CleanupApi.md#api_v1_cleanup_publisher_get) | **GET** /api/v1/cleanup/publisher | List publisher items that no longer serve.
[**api_v1_cleanup_publisher_linked_get**](CleanupApi.md#api_v1_cleanup_publisher_linked_get) | **GET** /api/v1/cleanup/publisher/linked | What still uses publisher cleanup rows.
[**api_v1_cleanup_publisher_purge_post**](CleanupApi.md#api_v1_cleanup_publisher_purge_post) | **POST** /api/v1/cleanup/publisher/purge | Purge archived publisher items for good.
[**api_v1_cleanup_publisher_runs_get**](CleanupApi.md#api_v1_cleanup_publisher_runs_get) | **GET** /api/v1/cleanup/publisher/runs | Recent publisher cleanup runs.
[**api_v1_cleanup_publisher_runs_id_get**](CleanupApi.md#api_v1_cleanup_publisher_runs_id_get) | **GET** /api/v1/cleanup/publisher/runs/{id} | One publisher cleanup run with its items.
[**api_v1_cleanup_publisher_runs_id_undone_post**](CleanupApi.md#api_v1_cleanup_publisher_runs_id_undone_post) | **POST** /api/v1/cleanup/publisher/runs/{id}/undone | Mark a publisher cleanup run as undone.
[**api_v1_cleanup_publisher_runs_post**](CleanupApi.md#api_v1_cleanup_publisher_runs_post) | **POST** /api/v1/cleanup/publisher/runs | Record a publisher cleanup run.
[**api_v1_cleanup_publisher_summary_get**](CleanupApi.md#api_v1_cleanup_publisher_summary_get) | **GET** /api/v1/cleanup/publisher/summary | Count the publisher cleanup candidates per kind.


# **api_v1_cleanup_advertiser_archived_get**
> api_v1_cleanup_advertiser_archived_get()

Archived advertiser items that can be purged.

Per kind the caller may read, how many archived (deleted) items are still restorable, i.e. not purged.

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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Archived advertiser items that can be purged.
        api_instance.api_v1_cleanup_advertiser_archived_get()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_archived_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | &#x60;data&#x60; &#x3D; [{kind, archived}]. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_export_get**
> api_v1_cleanup_advertiser_export_get(format=format, kinds=kinds, inactive_days=inactive_days, never_served=never_served)

Download the advertiser cleanup candidates.

Every kind the caller may read (or the comma-separated `kinds`) with
the same filter, as one xlsx workbook with a sheet per kind (default)
or one csv where each kind starts with its own header row.


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
    api_instance = goadserver.CleanupApi(api_client)
    format = xlsx # str |  (optional) (default to xlsx)
    kinds = 'kinds_example' # str | Comma-separated subset of: campaign,ad,creative,creative_pool,url_pool. (optional)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)

    try:
        # Download the advertiser cleanup candidates.
        api_instance.api_v1_cleanup_advertiser_export_get(format=format, kinds=kinds, inactive_days=inactive_days, never_served=never_served)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to xlsx]
 **kinds** | **str**| Comma-separated subset of: campaign,ad,creative,creative_pool,url_pool. | [optional] 
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; for an unknown format or kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_get**
> api_v1_cleanup_advertiser_get(kind=kind, inactive_days=inactive_days, never_served=never_served, search=search, sort=sort, dir=dir, page=page, per_page=per_page)

List advertiser items that no longer serve.

One kind at a time (`campaign`, `ad`, `creative`, `creative_pool`, `url_pool` —
campaigns and ads need `campaigns.read`, the rest `creatives.read`): every not-deleted row
the account owns that has not served an impression for at least
`inactive_days` days (default 90; `0` lists everything), or with
`never_served=1` only the rows that never served at all. Each row
carries its first / last served date (`""` = never), `days_idle`
(`-1` = never served), lifetime impressions / clicks / spend
in the account's currency units, and a suggestion:

- `pause` — still switched on but idle (campaigns, ads).
- `archive` — off or not switchable and nothing depends on it.
- `review` — idle but still used (`used_by` live ads or pool
  items for creatives and pools, live adzones for websites).
- `keep` — served within the last 90 days; only appears with
  `inactive_days=0`, the full inventory.

Read-only: act through the kind's own endpoints (pause a campaign
or ad, mass-delete, delete a pool or site), which keep their own
checks. History comes from the full stats history (2021 onward)
and is cached for five minutes. RTB campaigns are not listed: their
delivery is reported separately. Each kind also needs its own scope
(campaigns.read, creatives.read); a kind the key or team member cannot read
is 403. The panel's Cleanup page uses the same handler.


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
    api_instance = goadserver.CleanupApi(api_client)
    kind = 'kind_example' # str |  (optional)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)
    search = 'search_example' # str | Substring of the name. (optional)
    sort = last_served # str | last_served ascending = never served first, then the longest idle. (optional) (default to last_served)
    dir = asc # str |  (optional) (default to asc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List advertiser items that no longer serve.
        api_instance.api_v1_cleanup_advertiser_get(kind=kind, inactive_days=inactive_days, never_served=never_served, search=search, sort=sort, dir=dir, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  | [optional] 
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]
 **search** | **str**| Substring of the name. | [optional] 
 **sort** | **str**| last_served ascending &#x3D; never served first, then the longest idle. | [optional] [default to last_served]
 **dir** | **str**|  | [optional] [default to asc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; for an unknown kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_linked_get**
> api_v1_cleanup_advertiser_linked_get(kind, ids)

What still uses advertiser cleanup rows.

For rows suggested `review` (still in use): the live ads in live
campaigns that use them (creatives, creative pools, URL pools), the
campaigns those ads would leave without any live ad, the live pool
items holding a creative, and the live ad zones on a website. Read
only; the panel's archive dialog archives these first when the user
ticks "archive linked too" (ads, then emptied campaigns, then ad
zones and pool items, then the rows).


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
    api_instance = goadserver.CleanupApi(api_client)
    kind = 'kind_example' # str | 
    ids = 'ids_example' # str | Comma-separated row ids, 1 to 5000.

    try:
        # What still uses advertiser cleanup rows.
        api_instance.api_v1_cleanup_advertiser_linked_get(kind, ids)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_linked_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  | 
 **ids** | **str**| Comma-separated row ids, 1 to 5000. | 

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
**200** | &#x60;data&#x60; &#x3D; {ads: [{id, name, campaign_id, campaign_type, campaign_name, uses_id}], campaigns_emptied: [{id, type, name}], pool_items: [{id, pool_id, pool_name, uses_id, is_active}], adzones: [{id, name, uses_id}]}. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; kind, or no / too many ids. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_purge_post**
> api_v1_cleanup_advertiser_purge_post()

Purge archived advertiser items for good.

Every archived item of the named kinds leaves the Deleted views and
can no longer be restored (each kind's recover / undelete route
answers 404 for it). The rows stay archived in the database, so past
statistics keep their names and serving is not affected. Cannot be
undone; logged in GET /runs as a `purge` entry. Body
`{kinds: [...], confirm: "PURGE"}` (campaign, ad, creative, creative_pool, url_pool).


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Purge archived advertiser items for good.
        api_instance.api_v1_cleanup_advertiser_purge_post()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_purge_post: %s\n" % e)
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
**200** | &#x60;purged&#x60; &#x3D; items per &#x60;purge:&lt;kind&gt;&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Missing confirm, no kinds, or an unknown kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_runs_get**
> api_v1_cleanup_advertiser_runs_get()

Recent advertiser cleanup runs.

Every pause / archive the Cleanup page (or an integration) recorded
in the last 90 days, newest first, at most 50: `id`, `source`
(selected | suggested | linked), `time`, `actor_userid`, `undone`,
and `counts` keyed `<op>:<kind>`. Item lists come from GET /runs/{id}.


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Recent advertiser cleanup runs.
        api_instance.api_v1_cleanup_advertiser_runs_get()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_runs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | &#x60;data&#x60; &#x3D; the runs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_runs_id_get**
> api_v1_cleanup_advertiser_runs_id_get(id)

One advertiser cleanup run with its items.

What to call to undo it, action by action, newest action first:
pause → resume (PUT /campaigns/mass-toggle pause false, PUT
/campaigns/{type}/{campaignId}/ads/mass-toggle activate true);
archive → restore (POST /campaigns/mass-undelete, POST
/campaigns/{type}/{campaignId}/ads/mass-undelete, POST
/creatives/bulk-undelete, POST /adspaces/mass-recover, POST
/creative-pools/{id}/recover, POST /url-pools/{id}/recover, POST
/sites/{id}/recover); remove_pool_item → POST
/creative-pools/{id}/items/recover. Then POST /runs/{id}/undone.


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
    api_instance = goadserver.CleanupApi(api_client)
    id = 56 # int | 

    try:
        # One advertiser cleanup run with its items.
        api_instance.api_v1_cleanup_advertiser_runs_id_get(id)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_runs_id_get: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#x60;data&#x60; &#x3D; the run with &#x60;actions&#x60;. |  -  |
**404** | Not this account&#39;s run on this side. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_runs_id_undone_post**
> api_v1_cleanup_advertiser_runs_id_undone_post(id)

Mark a advertiser cleanup run as undone.

Call after restoring / resuming its items. 409 `already_undone` when it already was.

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
    api_instance = goadserver.CleanupApi(api_client)
    id = 56 # int | 

    try:
        # Mark a advertiser cleanup run as undone.
        api_instance.api_v1_cleanup_advertiser_runs_id_undone_post(id)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_runs_id_undone_post: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marked. |  -  |
**404** | Not found. |  -  |
**409** | Already undone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_runs_post**
> api_v1_cleanup_advertiser_runs_post()

Record a advertiser cleanup run.

Record what you just changed so it can be listed and undone. Body
`{source, actions: [{op, kind, items: [{id, campaign_id, campaign_type, pool_id, was_active}]}]}`;
`op` is `pause` (campaigns, ads), `archive` (any kind of this side)
or `remove_pool_item` (kind `creative`; `pool_id`, `was_active`).
Ads need `campaign_id` + `campaign_type`, campaigns `campaign_type`.
At most 100000 items. Recording changes nothing by itself.


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Record a advertiser cleanup run.
        api_instance.api_v1_cleanup_advertiser_runs_post()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_runs_post: %s\n" % e)
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
**201** | &#x60;id&#x60; and &#x60;counts&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Unknown op or kind, nothing changed, or too many items. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_advertiser_summary_get**
> api_v1_cleanup_advertiser_summary_get(inactive_days=inactive_days, never_served=never_served)

Count the advertiser cleanup candidates per kind.

For every kind the caller may read: how many rows match the same
`inactive_days` / `never_served` filter, how many never served, and
the split by suggestion.


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
    api_instance = goadserver.CleanupApi(api_client)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)

    try:
        # Count the advertiser cleanup candidates per kind.
        api_instance.api_v1_cleanup_advertiser_summary_get(inactive_days=inactive_days, never_served=never_served)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_advertiser_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]

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
**200** | Per-kind counts. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_archived_get**
> api_v1_cleanup_publisher_archived_get()

Archived publisher items that can be purged.

Per kind the caller may read, how many archived (deleted) items are still restorable, i.e. not purged.

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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Archived publisher items that can be purged.
        api_instance.api_v1_cleanup_publisher_archived_get()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_archived_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | &#x60;data&#x60; &#x3D; [{kind, archived}]. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_export_get**
> api_v1_cleanup_publisher_export_get(format=format, kinds=kinds, inactive_days=inactive_days, never_served=never_served)

Download the publisher cleanup candidates.

Every kind the caller may read (or the comma-separated `kinds`) with
the same filter, as one xlsx workbook with a sheet per kind (default)
or one csv where each kind starts with its own header row.


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
    api_instance = goadserver.CleanupApi(api_client)
    format = xlsx # str |  (optional) (default to xlsx)
    kinds = 'kinds_example' # str | Comma-separated subset of: adzone,website. (optional)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)

    try:
        # Download the publisher cleanup candidates.
        api_instance.api_v1_cleanup_publisher_export_get(format=format, kinds=kinds, inactive_days=inactive_days, never_served=never_served)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to xlsx]
 **kinds** | **str**| Comma-separated subset of: adzone,website. | [optional] 
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; for an unknown format or kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_get**
> api_v1_cleanup_publisher_get(kind=kind, inactive_days=inactive_days, never_served=never_served, search=search, sort=sort, dir=dir, page=page, per_page=per_page)

List publisher items that no longer serve.

One kind at a time (`adzone` needs `adspaces.read`, `website` needs `sites.read`): every not-deleted row
the account owns that has not served an impression for at least
`inactive_days` days (default 90; `0` lists everything), or with
`never_served=1` only the rows that never served at all. Each row
carries its first / last served date (`""` = never), `days_idle`
(`-1` = never served), lifetime impressions / clicks / earnings
in the account's currency units, and a suggestion:

- `pause` — still switched on but idle (campaigns, ads).
- `archive` — off or not switchable and nothing depends on it.
- `review` — idle but still used (`used_by` live ads or pool
  items for creatives and pools, live adzones for websites).
- `keep` — served within the last 90 days; only appears with
  `inactive_days=0`, the full inventory.

Read-only: act through the kind's own endpoints (pause a campaign
or ad, mass-delete, delete a pool or site), which keep their own
checks. History comes from the full stats history (2021 onward)
and is cached for five minutes. RTB campaigns are not listed: their
delivery is reported separately. Each kind also needs its own scope
(adspaces.read, sites.read); a kind the key or team member cannot read
is 403. The panel's Cleanup page uses the same handler.


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
    api_instance = goadserver.CleanupApi(api_client)
    kind = 'kind_example' # str |  (optional)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)
    search = 'search_example' # str | Substring of the name. (optional)
    sort = last_served # str | last_served ascending = never served first, then the longest idle. (optional) (default to last_served)
    dir = asc # str |  (optional) (default to asc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        # List publisher items that no longer serve.
        api_instance.api_v1_cleanup_publisher_get(kind=kind, inactive_days=inactive_days, never_served=never_served, search=search, sort=sort, dir=dir, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  | [optional] 
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]
 **search** | **str**| Substring of the name. | [optional] 
 **sort** | **str**| last_served ascending &#x3D; never served first, then the longest idle. | [optional] [default to last_served]
 **dir** | **str**|  | [optional] [default to asc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; for an unknown kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_linked_get**
> api_v1_cleanup_publisher_linked_get(kind, ids)

What still uses publisher cleanup rows.

For rows suggested `review` (still in use): the live ads in live
campaigns that use them (creatives, creative pools, URL pools), the
campaigns those ads would leave without any live ad, the live pool
items holding a creative, and the live ad zones on a website. Read
only; the panel's archive dialog archives these first when the user
ticks "archive linked too" (ads, then emptied campaigns, then ad
zones and pool items, then the rows).


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
    api_instance = goadserver.CleanupApi(api_client)
    kind = 'kind_example' # str | 
    ids = 'ids_example' # str | Comma-separated row ids, 1 to 5000.

    try:
        # What still uses publisher cleanup rows.
        api_instance.api_v1_cleanup_publisher_linked_get(kind, ids)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_linked_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  | 
 **ids** | **str**| Comma-separated row ids, 1 to 5000. | 

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
**200** | &#x60;data&#x60; &#x3D; {ads: [{id, name, campaign_id, campaign_type, campaign_name, uses_id}], campaigns_emptied: [{id, type, name}], pool_items: [{id, pool_id, pool_name, uses_id, is_active}], adzones: [{id, name, uses_id}]}. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_enum&#x60; kind, or no / too many ids. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_purge_post**
> api_v1_cleanup_publisher_purge_post()

Purge archived publisher items for good.

Every archived item of the named kinds leaves the Deleted views and
can no longer be restored (each kind's recover / undelete route
answers 404 for it). The rows stay archived in the database, so past
statistics keep their names and serving is not affected. Cannot be
undone; logged in GET /runs as a `purge` entry. Body
`{kinds: [...], confirm: "PURGE"}` (adzone, website).


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Purge archived publisher items for good.
        api_instance.api_v1_cleanup_publisher_purge_post()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_purge_post: %s\n" % e)
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
**200** | &#x60;purged&#x60; &#x3D; items per &#x60;purge:&lt;kind&gt;&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Missing confirm, no kinds, or an unknown kind. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_runs_get**
> api_v1_cleanup_publisher_runs_get()

Recent publisher cleanup runs.

Every pause / archive the Cleanup page (or an integration) recorded
in the last 90 days, newest first, at most 50: `id`, `source`
(selected | suggested | linked), `time`, `actor_userid`, `undone`,
and `counts` keyed `<op>:<kind>`. Item lists come from GET /runs/{id}.


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Recent publisher cleanup runs.
        api_instance.api_v1_cleanup_publisher_runs_get()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_runs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | &#x60;data&#x60; &#x3D; the runs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_runs_id_get**
> api_v1_cleanup_publisher_runs_id_get(id)

One publisher cleanup run with its items.

What to call to undo it, action by action, newest action first:
pause → resume (PUT /campaigns/mass-toggle pause false, PUT
/campaigns/{type}/{campaignId}/ads/mass-toggle activate true);
archive → restore (POST /campaigns/mass-undelete, POST
/campaigns/{type}/{campaignId}/ads/mass-undelete, POST
/creatives/bulk-undelete, POST /adspaces/mass-recover, POST
/creative-pools/{id}/recover, POST /url-pools/{id}/recover, POST
/sites/{id}/recover); remove_pool_item → POST
/creative-pools/{id}/items/recover. Then POST /runs/{id}/undone.


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
    api_instance = goadserver.CleanupApi(api_client)
    id = 56 # int | 

    try:
        # One publisher cleanup run with its items.
        api_instance.api_v1_cleanup_publisher_runs_id_get(id)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_runs_id_get: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#x60;data&#x60; &#x3D; the run with &#x60;actions&#x60;. |  -  |
**404** | Not this account&#39;s run on this side. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_runs_id_undone_post**
> api_v1_cleanup_publisher_runs_id_undone_post(id)

Mark a publisher cleanup run as undone.

Call after restoring / resuming its items. 409 `already_undone` when it already was.

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
    api_instance = goadserver.CleanupApi(api_client)
    id = 56 # int | 

    try:
        # Mark a publisher cleanup run as undone.
        api_instance.api_v1_cleanup_publisher_runs_id_undone_post(id)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_runs_id_undone_post: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marked. |  -  |
**404** | Not found. |  -  |
**409** | Already undone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_runs_post**
> api_v1_cleanup_publisher_runs_post()

Record a publisher cleanup run.

Record what you just changed so it can be listed and undone. Body
`{source, actions: [{op, kind, items: [{id, campaign_id, campaign_type, pool_id, was_active}]}]}`;
`op` is `pause` (campaigns, ads), `archive` (any kind of this side)
or `remove_pool_item` (kind `creative`; `pool_id`, `was_active`).
Ads need `campaign_id` + `campaign_type`, campaigns `campaign_type`.
At most 100000 items. Recording changes nothing by itself.


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
    api_instance = goadserver.CleanupApi(api_client)

    try:
        # Record a publisher cleanup run.
        api_instance.api_v1_cleanup_publisher_runs_post()
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_runs_post: %s\n" % e)
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
**201** | &#x60;id&#x60; and &#x60;counts&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Unknown op or kind, nothing changed, or too many items. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cleanup_publisher_summary_get**
> api_v1_cleanup_publisher_summary_get(inactive_days=inactive_days, never_served=never_served)

Count the publisher cleanup candidates per kind.

For every kind the caller may read: how many rows match the same
`inactive_days` / `never_served` filter, how many never served, and
the split by suggestion.


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
    api_instance = goadserver.CleanupApi(api_client)
    inactive_days = 90 # int |  (optional) (default to 90)
    never_served = False # bool |  (optional) (default to False)

    try:
        # Count the publisher cleanup candidates per kind.
        api_instance.api_v1_cleanup_publisher_summary_get(inactive_days=inactive_days, never_served=never_served)
    except Exception as e:
        print("Exception when calling CleanupApi->api_v1_cleanup_publisher_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive_days** | **int**|  | [optional] [default to 90]
 **never_served** | **bool**|  | [optional] [default to False]

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
**200** | Per-kind counts. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


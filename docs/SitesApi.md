# goadserver.SitesApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_domains_get**](SitesApi.md#api_v1_domains_get) | **GET** /api/v1/domains | List your custom domains (Domain Manager).
[**api_v1_domains_id_delete**](SitesApi.md#api_v1_domains_id_delete) | **DELETE** /api/v1/domains/{id} | Delete a custom domain.
[**api_v1_domains_id_get**](SitesApi.md#api_v1_domains_id_get) | **GET** /api/v1/domains/{id} | Show one custom domain.
[**api_v1_domains_id_notes_put**](SitesApi.md#api_v1_domains_id_notes_put) | **PUT** /api/v1/domains/{id}/notes | Set your notes on a domain.
[**api_v1_domains_id_redo_post**](SitesApi.md#api_v1_domains_id_redo_post) | **POST** /api/v1/domains/{id}/redo | Retry setting up a domain (DNS / certificate check again).
[**api_v1_domains_id_toggle_active_post**](SitesApi.md#api_v1_domains_id_toggle_active_post) | **POST** /api/v1/domains/{id}/toggle-active | Switch a custom domain on or off.
[**api_v1_domains_post**](SitesApi.md#api_v1_domains_post) | **POST** /api/v1/domains | Add a custom domain.
[**api_v1_sites_get**](SitesApi.md#api_v1_sites_get) | **GET** /api/v1/sites | List the caller&#39;s websites.
[**api_v1_sites_id_clone_post**](SitesApi.md#api_v1_sites_id_clone_post) | **POST** /api/v1/sites/{id}/clone | Duplicate a site under a new name and URL, with its ad zones.
[**api_v1_sites_id_delete**](SitesApi.md#api_v1_sites_id_delete) | **DELETE** /api/v1/sites/{id} | Soft-delete a site.
[**api_v1_sites_id_get**](SitesApi.md#api_v1_sites_id_get) | **GET** /api/v1/sites/{id} | Get a single site.
[**api_v1_sites_id_patch**](SitesApi.md#api_v1_sites_id_patch) | **PATCH** /api/v1/sites/{id} | Update a site.
[**api_v1_sites_id_recover_post**](SitesApi.md#api_v1_sites_id_recover_post) | **POST** /api/v1/sites/{id}/recover | Reverse a soft-delete on a site.
[**api_v1_sites_id_snippets_get**](SitesApi.md#api_v1_sites_id_snippets_get) | **GET** /api/v1/sites/{id}/snippets | List the site&#39;s HTML snippets.
[**api_v1_sites_id_snippets_post**](SitesApi.md#api_v1_sites_id_snippets_post) | **POST** /api/v1/sites/{id}/snippets | Add an HTML snippet.
[**api_v1_sites_id_snippets_snippet_id_delete**](SitesApi.md#api_v1_sites_id_snippets_snippet_id_delete) | **DELETE** /api/v1/sites/{id}/snippets/{snippetId} | Delete an HTML snippet.
[**api_v1_sites_id_snippets_snippet_id_put**](SitesApi.md#api_v1_sites_id_snippets_snippet_id_put) | **PUT** /api/v1/sites/{id}/snippets/{snippetId} | Replace an HTML snippet.
[**api_v1_sites_id_verify_post**](SitesApi.md#api_v1_sites_id_verify_post) | **POST** /api/v1/sites/{id}/verify | Trigger HTTP re-check of the site verification meta tag.
[**api_v1_sites_post**](SitesApi.md#api_v1_sites_post) | **POST** /api/v1/sites | Create a new website.
[**api_v1_sites_schema_get**](SitesApi.md#api_v1_sites_schema_get) | **GET** /api/v1/sites/_schema | Field metadata for site create/update.


# **api_v1_domains_get**
> api_v1_domains_get(type=type, state=state, isactive=isactive, page=page, per_page=per_page)

List your custom domains (Domain Manager).

The domains you serve ads (`ads`), static files (`static`) or your
branded panel (`up`) from. `dns_target` is the host an `ads`/`static`
domain must CNAME to (your network's ad domain); `dns_target_up` the
host an `up` domain must CNAME to. Paginated like every list
(`page`, `per_page` ≤ 100); filters: `type`, `state`, `isactive`,
`domain` (LIKE).


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
    api_instance = goadserver.SitesApi(api_client)
    type = 'type_example' # str |  (optional)
    state = 56 # int |  (optional)
    isactive = 56 # int |  (optional)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)

    try:
        # List your custom domains (Domain Manager).
        api_instance.api_v1_domains_get(type=type, state=state, isactive=isactive, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **state** | **int**|  | [optional] 
 **isactive** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

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
**200** | Domains plus the CNAME targets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_id_delete**
> api_v1_domains_id_delete(id)

Delete a custom domain.

Refused with 409 `brand_in_use` while the domain is your branded panel domain.

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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Delete a custom domain.
        api_instance.api_v1_domains_id_delete(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_id_delete: %s\n" % e)
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
**200** | Deleted. |  -  |
**404** | domain_not_found |  -  |
**409** | brand_in_use |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_id_get**
> api_v1_domains_id_get(id)

Show one custom domain.

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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Show one custom domain.
        api_instance.api_v1_domains_id_get(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_id_get: %s\n" % e)
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
**200** | The domain. |  -  |
**404** | domain_not_found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_id_notes_put**
> api_v1_domains_id_notes_put(id, api_v1_domains_id_notes_put_request)

Set your notes on a domain.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_domains_id_notes_put_request import ApiV1DomainsIdNotesPutRequest
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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    api_v1_domains_id_notes_put_request = goadserver.ApiV1DomainsIdNotesPutRequest() # ApiV1DomainsIdNotesPutRequest | 

    try:
        # Set your notes on a domain.
        api_instance.api_v1_domains_id_notes_put(id, api_v1_domains_id_notes_put_request)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_id_notes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_domains_id_notes_put_request** | [**ApiV1DomainsIdNotesPutRequest**](ApiV1DomainsIdNotesPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_id_redo_post**
> api_v1_domains_id_redo_post(id)

Retry setting up a domain (DNS / certificate check again).

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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Retry setting up a domain (DNS / certificate check again).
        api_instance.api_v1_domains_id_redo_post(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_id_redo_post: %s\n" % e)
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
**200** | Queued for another attempt. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_id_toggle_active_post**
> api_v1_domains_id_toggle_active_post(id)

Switch a custom domain on or off.

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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Switch a custom domain on or off.
        api_instance.api_v1_domains_id_toggle_active_post(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_id_toggle_active_post: %s\n" % e)
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
**200** | Toggled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_domains_post**
> api_v1_domains_post(api_v1_domains_post_request)

Add a custom domain.

Create the CNAME first (see `dns_target` on GET /api/v1/domains),
then add the domain. The server checks that it resolves and that it
really reaches our servers before it is accepted; the certificate is
then issued automatically and `state` moves on as it goes live.
Errors (409): `invalid_domain`, `invalid_dns` (does not resolve),
`invalid_dns_point` (resolves, but not to us yet — DNS can take a few
hours), `domain_exists`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_domains_post_request import ApiV1DomainsPostRequest
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
    api_instance = goadserver.SitesApi(api_client)
    api_v1_domains_post_request = goadserver.ApiV1DomainsPostRequest() # ApiV1DomainsPostRequest | 

    try:
        # Add a custom domain.
        api_instance.api_v1_domains_post(api_v1_domains_post_request)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_domains_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_domains_post_request** | [**ApiV1DomainsPostRequest**](ApiV1DomainsPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain added. |  -  |
**409** | invalid_domain / invalid_dns / invalid_dns_point / domain_exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_get**
> ApiV1SitesGet200Response api_v1_sites_get(state=state, sitestate=sitestate, search=search, page=page, per_page=per_page)

List the caller's websites.

Paged list (sorted by name). `state=deleted` lists soft-deleted
sites so `POST /api/v1/sites/{id}/recover` has ids to work with.
Per-site period stats (the panel's Websites listing stats columns) come
from `GET /api/v1/publisher/stats?group_by=website&from=&to=`, keyed by
site id; per-zone ones from `group_by=adzone`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_sites_get200_response import ApiV1SitesGet200Response
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
    api_instance = goadserver.SitesApi(api_client)
    state = live # str |  (optional) (default to live)
    sitestate = 56 # int | Review state: 1 validated, 0 pending, -1 rejected. (optional)
    search = 'search_example' # str | Substring of name or URL. (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 500 # int |  (optional) (default to 500)

    try:
        # List the caller's websites.
        api_response = api_instance.api_v1_sites_get(state=state, sitestate=sitestate, search=search, page=page, per_page=per_page)
        print("The response of SitesApi->api_v1_sites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional] [default to live]
 **sitestate** | **int**| Review state: 1 validated, 0 pending, -1 rejected. | [optional] 
 **search** | **str**| Substring of name or URL. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 500]

### Return type

[**ApiV1SitesGet200Response**](ApiV1SitesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site list (filtered by &#x60;resource_filter.site_ids&#x60; when set). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_clone_post**
> api_v1_sites_id_clone_post(id, api_v1_sites_id_clone_post_request)

Duplicate a site under a new name and URL, with its ad zones.

Creates a new site from this one (same settings) and copies its
live ad zones onto it. The new URL goes through the same domain
checks as `POST /api/v1/sites`. Keys pinned to `site_ids` /
`adzone_ids` are refused (the copy could never be on the pin).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_sites_id_clone_post_request import ApiV1SitesIdClonePostRequest
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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    api_v1_sites_id_clone_post_request = {"name":"My Blog (DE)","url":"https://de.example.com"} # ApiV1SitesIdClonePostRequest | 

    try:
        # Duplicate a site under a new name and URL, with its ad zones.
        api_instance.api_v1_sites_id_clone_post(id, api_v1_sites_id_clone_post_request)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_sites_id_clone_post_request** | [**ApiV1SitesIdClonePostRequest**](ApiV1SitesIdClonePostRequest.md)|  | 

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
**201** | Cloned. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Site not found. |  -  |
**422** | &#x60;validation_error&#x60; (name/url required, name taken, URL invalid or blocked) or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_delete**
> api_v1_sites_id_delete(id)

Soft-delete a site.

Sets `isdeleted = 1`. Refused with **422 `has_adzones`** while the
site still has live ad zones — delete or move them first
(`POST /api/v1/adspaces/mass-delete`). Undo with
`POST /api/v1/sites/{id}/recover`.


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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a site.
        api_instance.api_v1_sites_id_delete(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_delete: %s\n" % e)
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
**422** | &#x60;has_adzones&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_get**
> Site api_v1_sites_id_get(id)

Get a single site.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.site import Site
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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Get a single site.
        api_response = api_instance.api_v1_sites_id_get(id)
        print("The response of SitesApi->api_v1_sites_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Site**](Site.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_patch**
> api_v1_sites_id_patch(id, request_body)

Update a site.

Update fields on an existing site. Send only the keys you want
to change — omitted fields keep their current value. The
`url` domain is re-validated when changed. A change of `url`,
`categories` or `sitelanguages` puts a validated site back to
pending review where the tenant reviews sites. `tags` (site groups)
replaces the list; `[]` clears it.


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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    request_body = {"description":"Updated description","categories":[12,47,99]} # Dict[str, object] | 

    try:
        # Update a site.
        api_instance.api_v1_sites_id_patch(id, request_body)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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
**400** | &#x60;no_fields&#x60; — the body changed nothing. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |
**422** | &#x60;validation_error&#x60; (same rules as create). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_recover_post**
> api_v1_sites_id_recover_post(id)

Reverse a soft-delete on a site.

Sets `isdeleted = 0` so the site appears in listings again (the
panel's Restore in the websites list's Deleted view). Returns 404
if the site doesn't exist, isn't currently soft-deleted, or was
purged.


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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Reverse a soft-delete on a site.
        api_instance.api_v1_sites_id_recover_post(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_recover_post: %s\n" % e)
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

# **api_v1_sites_id_snippets_get**
> api_v1_sites_id_snippets_get(id)

List the site's HTML snippets.

Managed `<meta>` / `<script>` / `<link>` / `<style>` tags injected
through the site's one container tag (the panel's HTML snippets
panel). Up to 100 per site.


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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # List the site's HTML snippets.
        api_instance.api_v1_sites_id_snippets_get(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_snippets_get: %s\n" % e)
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
**200** | Snippets. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Site not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_snippets_post**
> api_v1_sites_id_snippets_post(id, site_snippet_write)

Add an HTML snippet.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.site_snippet_write import SiteSnippetWrite
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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    site_snippet_write = {"snippet_key":"google-verify","tag_type":"meta","position":"head","enabled":true,"attrs":{"name":"google-site-verification","content":"abc123"}} # SiteSnippetWrite | 

    try:
        # Add an HTML snippet.
        api_instance.api_v1_sites_id_snippets_post(id, site_snippet_write)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_snippets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **site_snippet_write** | [**SiteSnippetWrite**](SiteSnippetWrite.md)|  | 

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
**200** | Created. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Site not found. |  -  |
**422** | &#x60;validation_error&#x60; (tag type, position, attribute not allowed for the tag, non-http URL, limits, 100-snippet cap) or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_snippets_snippet_id_delete**
> api_v1_sites_id_snippets_snippet_id_delete(id, snippet_id)

Delete an HTML snippet.

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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    snippet_id = 56 # int | 

    try:
        # Delete an HTML snippet.
        api_instance.api_v1_sites_id_snippets_snippet_id_delete(id, snippet_id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_snippets_snippet_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **snippet_id** | **int**|  | 

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

# **api_v1_sites_id_snippets_snippet_id_put**
> api_v1_sites_id_snippets_snippet_id_put(id, snippet_id, site_snippet_write)

Replace an HTML snippet.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.site_snippet_write import SiteSnippetWrite
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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 
    snippet_id = 56 # int | 
    site_snippet_write = goadserver.SiteSnippetWrite() # SiteSnippetWrite | 

    try:
        # Replace an HTML snippet.
        api_instance.api_v1_sites_id_snippets_snippet_id_put(id, snippet_id, site_snippet_write)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_snippets_snippet_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **snippet_id** | **int**|  | 
 **site_snippet_write** | [**SiteSnippetWrite**](SiteSnippetWrite.md)|  | 

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
**200** | Updated; body &#x60;{snippet}&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_id_verify_post**
> api_v1_sites_id_verify_post(id)

Trigger HTTP re-check of the site verification meta tag.

Tells the server to fetch the site URL and look for the verify
meta tag the publisher embedded. On success the site flips to
`is_verified=true` and can start serving ads.

The verify code + tag prefix are exposed on
`GET /api/v1/sites/{id}` (`verify_code`, `verify_tag_prefix`,
`verify_meta_tag`) — the publisher pastes the meta tag on the
site root, then POSTs here.

Only meaningful when
`modules.publisher.websites.options.need_verification` is on
(otherwise the site is auto-verified at create time).


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
    api_instance = goadserver.SitesApi(api_client)
    id = 56 # int | 

    try:
        # Trigger HTTP re-check of the site verification meta tag.
        api_instance.api_v1_sites_id_verify_post(id)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_id_verify_post: %s\n" % e)
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
**200** | Verified. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found |  -  |
**422** | Verification failed (meta tag not found) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_post**
> api_v1_sites_post(site_create)

Create a new website.

Create a website (publisher_sites row). Required: `name` + `url`.
The domain in `url` is checked against the publisher-domain
blocklist; subdomain duplicates of an existing site are rejected.

Module-gated fields become required when their module is active
on the tenant — see `GET /api/v1/sites/_schema` for the exact
field list applicable to this tenant.

On create, the server resolves the domain to a `domainid`. If
`modules.publisher.websites.options.need_verification` is on,
the new site starts at `is_verified=false` — the publisher must
complete the dashboard verification flow before the site can
serve ads.

API keys with `resource_filter.site_ids` set cannot create new
sites — pinning to a fixed list is incompatible with adding new
ones (returns 403).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.site_create import SiteCreate
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
    api_instance = goadserver.SitesApi(api_client)
    site_create = {"name":"My Blog","url":"https://www.example.com","description":"Personal blog about hiking","main_catid":12,"categories":[12,47],"sitelanguages":["en"]} # SiteCreate | 

    try:
        # Create a new website.
        api_instance.api_v1_sites_post(site_create)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_create** | [**SiteCreate**](SiteCreate.md)|  | 

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
**201** | Created. Fetch the record with &#x60;GET /api/v1/sites/{id}&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; — &#x60;errors&#x60; maps each field to its messages (name taken, URL invalid or blocked, categories/languages required, …). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_schema_get**
> ApiV1SitesSchemaGet200Response api_v1_sites_schema_get()

Field metadata for site create/update.

Returns the canonical field list for `POST /api/v1/sites` and
`PATCH /api/v1/sites/{id}`. Module-gated fields (`typeid`,
`categories`, `sitelanguages`, `postbacks`) only appear when
the relevant module is active on the calling tenant.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_sites_schema_get200_response import ApiV1SitesSchemaGet200Response
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
    api_instance = goadserver.SitesApi(api_client)

    try:
        # Field metadata for site create/update.
        api_response = api_instance.api_v1_sites_schema_get()
        print("The response of SitesApi->api_v1_sites_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->api_v1_sites_schema_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1SitesSchemaGet200Response**](ApiV1SitesSchemaGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# goadserver.XMLFeedsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_xml_feeds_get**](XMLFeedsApi.md#api_v1_xml_feeds_get) | **GET** /api/v1/xml-feeds | List XML feeds.
[**api_v1_xml_feeds_id_clone_post**](XMLFeedsApi.md#api_v1_xml_feeds_id_clone_post) | **POST** /api/v1/xml-feeds/{id}/clone | Clone an XML feed.
[**api_v1_xml_feeds_id_delete**](XMLFeedsApi.md#api_v1_xml_feeds_id_delete) | **DELETE** /api/v1/xml-feeds/{id} | Delete an XML feed.
[**api_v1_xml_feeds_id_get**](XMLFeedsApi.md#api_v1_xml_feeds_id_get) | **GET** /api/v1/xml-feeds/{id} | Show an XML feed.
[**api_v1_xml_feeds_id_put**](XMLFeedsApi.md#api_v1_xml_feeds_id_put) | **PUT** /api/v1/xml-feeds/{id} | Update an XML feed.
[**api_v1_xml_feeds_id_toggle_put**](XMLFeedsApi.md#api_v1_xml_feeds_id_toggle_put) | **PUT** /api/v1/xml-feeds/{id}/toggle | Flip an XML feed active / paused.
[**api_v1_xml_feeds_post**](XMLFeedsApi.md#api_v1_xml_feeds_post) | **POST** /api/v1/xml-feeds | Create an XML feed.


# **api_v1_xml_feeds_get**
> api_v1_xml_feeds_get(page=page, per_page=per_page, search=search, sort_by=sort_by, sort_dir=sort_dir)

List XML feeds.

The account's product feeds. `lastvisit` / `nextvisit` are the last
and next fetch times (null before the first fetch). `filter_name`,
`filter_url` (substring), `filter_id` and `search` narrow the list;
`sort_by` = id / name / isactive, `sort_dir` = asc / desc. Same
handler as the panel.


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
    api_instance = goadserver.XMLFeedsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_dir = 'sort_dir_example' # str |  (optional)

    try:
        # List XML feeds.
        api_instance.api_v1_xml_feeds_get(page=page, per_page=per_page, search=search, sort_by=sort_by, sort_dir=sort_dir)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_dir** | **str**|  | [optional] 

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
**200** | Feeds. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_id_clone_post**
> api_v1_xml_feeds_id_clone_post(id)

Clone an XML feed.

Copies the feed as "<name> Copy", paused. No body.

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
    api_instance = goadserver.XMLFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Clone an XML feed.
        api_instance.api_v1_xml_feeds_id_clone_post(id)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_id_clone_post: %s\n" % e)
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
**201** | Cloned. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_id_delete**
> api_v1_xml_feeds_id_delete(id)

Delete an XML feed.

Permanent (the row is removed, as in the panel). Refused with 422
`feed_in_use` while any of your non-deleted campaigns still uses the
feed (`feedid`) — the response lists them (up to 50); take the feed
off those campaigns (or delete them) first. Refused for a
campaign-pinned key.


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
    api_instance = goadserver.XMLFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Delete an XML feed.
        api_instance.api_v1_xml_feeds_id_delete(id)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_id_delete: %s\n" % e)
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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Feed not found. |  -  |
**422** | &#x60;feed_in_use&#x60; — campaigns still use this feed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_id_get**
> api_v1_xml_feeds_id_get(id)

Show an XML feed.

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
    api_instance = goadserver.XMLFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Show an XML feed.
        api_instance.api_v1_xml_feeds_id_get(id)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_id_get: %s\n" % e)
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
**200** | The feed row. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Feed not found (or module off). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_id_put**
> api_v1_xml_feeds_id_put(id, api_v1_xml_feeds_id_put_request)

Update an XML feed.

Partial: only the fields sent change. `revisitminutes` is raised to
5 at least; `isactive` 0/1 pauses or resumes fetching. A feed is
shared by every campaign that uses it, so a key pinned to campaigns
gets 403 `forbidden_resource`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_xml_feeds_id_put_request import ApiV1XmlFeedsIdPutRequest
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
    api_instance = goadserver.XMLFeedsApi(api_client)
    id = 56 # int | 
    api_v1_xml_feeds_id_put_request = {"revisitminutes":30} # ApiV1XmlFeedsIdPutRequest | 

    try:
        # Update an XML feed.
        api_instance.api_v1_xml_feeds_id_put(id, api_v1_xml_feeds_id_put_request)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_xml_feeds_id_put_request** | [**ApiV1XmlFeedsIdPutRequest**](ApiV1XmlFeedsIdPutRequest.md)|  | 

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
**400** | &#x60;no_fields&#x60; — nothing to update. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Feed not found. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_id_toggle_put**
> api_v1_xml_feeds_id_toggle_put(id)

Flip an XML feed active / paused.

No body — flips `isactive`. Refused for a campaign-pinned key.

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
    api_instance = goadserver.XMLFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Flip an XML feed active / paused.
        api_instance.api_v1_xml_feeds_id_toggle_put(id)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_id_toggle_put: %s\n" % e)
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
**200** | Flipped. Read the feed to see the new state. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_xml_feeds_post**
> api_v1_xml_feeds_post(api_v1_xml_feeds_post_request)

Create an XML feed.

The paths are the XML element paths the fetcher reads per item.
`revisitminutes` (how often the feed is re-fetched) is raised to the
minimum of 5. The feed starts active. Unknown body fields → 422
`unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_xml_feeds_post_request import ApiV1XmlFeedsPostRequest
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
    api_instance = goadserver.XMLFeedsApi(api_client)
    api_v1_xml_feeds_post_request = {"name":"Shop feed","url":"https://shop.example.com/feed.xml","itemspath":"rss/channel/item","titlepath":"title","descriptionpath":"description","mediapath":"enclosure@url","linkpath":"link","revisitminutes":60} # ApiV1XmlFeedsPostRequest | 

    try:
        # Create an XML feed.
        api_instance.api_v1_xml_feeds_post(api_v1_xml_feeds_post_request)
    except Exception as e:
        print("Exception when calling XMLFeedsApi->api_v1_xml_feeds_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_xml_feeds_post_request** | [**ApiV1XmlFeedsPostRequest**](ApiV1XmlFeedsPostRequest.md)|  | 

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
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**422** | &#x60;validation_error&#x60; (name missing) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


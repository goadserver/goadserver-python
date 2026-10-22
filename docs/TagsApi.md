# goadserver.TagsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tags_get**](TagsApi.md#api_v1_tags_get) | **GET** /api/v1/tags | List tags.
[**api_v1_tags_id_delete**](TagsApi.md#api_v1_tags_id_delete) | **DELETE** /api/v1/tags/{id} | Delete a tag.
[**api_v1_tags_id_get**](TagsApi.md#api_v1_tags_id_get) | **GET** /api/v1/tags/{id} | Show a tag.
[**api_v1_tags_id_put**](TagsApi.md#api_v1_tags_id_put) | **PUT** /api/v1/tags/{id} | Rename or move a tag.
[**api_v1_tags_mass_delete_post**](TagsApi.md#api_v1_tags_mass_delete_post) | **POST** /api/v1/tags/mass-delete | Delete several tags.
[**api_v1_tags_post**](TagsApi.md#api_v1_tags_post) | **POST** /api/v1/tags | Create a tag.


# **api_v1_tags_get**
> api_v1_tags_get(page=page, per_page=per_page, search=search)

List tags.

The account's tags with their parent (`pid`, 0 = top level) and
depth (`level`). `search` / `filter_name` match the name. Assign a
tag to campaigns with `groupid` on PATCH /api/v1/campaigns/{type}/{id}
or the bulk PUT /api/v1/campaigns/save-tags.


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
    api_instance = goadserver.TagsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = '20' # str | Max 100, or `all`. (optional) (default to '20')
    search = 'search_example' # str |  (optional)

    try:
        # List tags.
        api_instance.api_v1_tags_get(page=page, per_page=per_page, search=search)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **str**| Max 100, or &#x60;all&#x60;. | [optional] [default to &#39;20&#39;]
 **search** | **str**|  | [optional] 

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
**200** | Tags. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tags_id_delete**
> api_v1_tags_id_delete(id)

Delete a tag.

Same clean-up as mass-delete. Refused for a campaign-pinned key.

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
    api_instance = goadserver.TagsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a tag.
        api_instance.api_v1_tags_id_delete(id)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_id_delete: %s\n" % e)
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
**404** | Tag not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tags_id_get**
> api_v1_tags_id_get(id)

Show a tag.

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
    api_instance = goadserver.TagsApi(api_client)
    id = 56 # int | 

    try:
        # Show a tag.
        api_instance.api_v1_tags_id_get(id)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_id_get: %s\n" % e)
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
**200** | The tag. |  -  |
**404** | Tag not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tags_id_put**
> api_v1_tags_id_put(id, api_v1_tags_id_put_request)

Rename or move a tag.

`name` is required. Omit `pid` to keep the tag where it is; send it
to move the tag (and its sub-tree) under another parent, 0 = top
level. A move that makes a cycle or exceeds three levels → 422.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tags_id_put_request import ApiV1TagsIdPutRequest
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
    api_instance = goadserver.TagsApi(api_client)
    id = 56 # int | 
    api_v1_tags_id_put_request = {"name":"Push campaigns","pid":0} # ApiV1TagsIdPutRequest | 

    try:
        # Rename or move a tag.
        api_instance.api_v1_tags_id_put(id, api_v1_tags_id_put_request)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_tags_id_put_request** | [**ApiV1TagsIdPutRequest**](ApiV1TagsIdPutRequest.md)|  | 

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
**200** | Saved (&#x60;data&#x60; only when &#x60;pid&#x60; was sent). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Tag not found. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tags_mass_delete_post**
> api_v1_tags_mass_delete_post(api_v1_tags_mass_delete_post_request)

Delete several tags.

Removes the tags and strips their ids from every campaign / adzone
that carried them (`refs_cleaned_up` counts the rewritten rows);
sub-tags move up. Refused for a campaign-pinned key (it rewrites
campaigns outside the pin).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tags_mass_delete_post_request import ApiV1TagsMassDeletePostRequest
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
    api_instance = goadserver.TagsApi(api_client)
    api_v1_tags_mass_delete_post_request = {"ids":[6,7]} # ApiV1TagsMassDeletePostRequest | 

    try:
        # Delete several tags.
        api_instance.api_v1_tags_mass_delete_post(api_v1_tags_mass_delete_post_request)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_mass_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tags_mass_delete_post_request** | [**ApiV1TagsMassDeletePostRequest**](ApiV1TagsMassDeletePostRequest.md)|  | 

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
**200** | Deleted. |  -  |
**400** | &#x60;no_ids&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tags_post**
> api_v1_tags_post(api_v1_tags_post_request)

Create a tag.

A name that already exists under the same parent is not duplicated:
the existing tag comes back with 200 and `existing: true`.
`pid` must be one of the caller's tags and the tree may not exceed
three levels (422).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tags_post_request import ApiV1TagsPostRequest
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
    api_instance = goadserver.TagsApi(api_client)
    api_v1_tags_post_request = {"name":"Push","pid":5} # ApiV1TagsPostRequest | 

    try:
        # Create a tag.
        api_instance.api_v1_tags_post(api_v1_tags_post_request)
    except Exception as e:
        print("Exception when calling TagsApi->api_v1_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tags_post_request** | [**ApiV1TagsPostRequest**](ApiV1TagsPostRequest.md)|  | 

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
**200** | Already existed. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; (name missing, bad parent, too deep) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


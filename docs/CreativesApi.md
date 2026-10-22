# goadserver.CreativesApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_creative_folders_get**](CreativesApi.md#api_v1_creative_folders_get) | **GET** /api/v1/creative-folders | List media-bank folders.
[**api_v1_creative_folders_id_delete**](CreativesApi.md#api_v1_creative_folders_id_delete) | **DELETE** /api/v1/creative-folders/{id} | Delete a folder.
[**api_v1_creative_folders_id_put**](CreativesApi.md#api_v1_creative_folders_id_put) | **PUT** /api/v1/creative-folders/{id} | Rename or move a folder.
[**api_v1_creative_folders_post**](CreativesApi.md#api_v1_creative_folders_post) | **POST** /api/v1/creative-folders | Create a folder.
[**api_v1_creatives_bulk_move_post**](CreativesApi.md#api_v1_creatives_bulk_move_post) | **POST** /api/v1/creatives/bulk-move | File creatives into a folder.
[**api_v1_creatives_get**](CreativesApi.md#api_v1_creatives_get) | **GET** /api/v1/creatives | List the creative library.
[**api_v1_creatives_id_delete**](CreativesApi.md#api_v1_creatives_id_delete) | **DELETE** /api/v1/creatives/{id} | Delete a creative.
[**api_v1_creatives_id_get**](CreativesApi.md#api_v1_creatives_id_get) | **GET** /api/v1/creatives/{id} | Show one creative.
[**api_v1_creatives_id_name_put**](CreativesApi.md#api_v1_creatives_id_name_put) | **PUT** /api/v1/creatives/{id}/name | Rename a creative (panel inline edit).
[**api_v1_creatives_id_put**](CreativesApi.md#api_v1_creatives_id_put) | **PUT** /api/v1/creatives/{id} | Rename and/or re-tag a creative.
[**api_v1_creatives_id_tags_put**](CreativesApi.md#api_v1_creatives_id_tags_put) | **PUT** /api/v1/creatives/{id}/tags | Replace a creative&#39;s tags (panel inline edit).
[**api_v1_creatives_id_used_in_get**](CreativesApi.md#api_v1_creatives_id_used_in_get) | **GET** /api/v1/creatives/{id}/used-in | List ads / pools referencing this creative.
[**api_v1_creatives_upload_post**](CreativesApi.md#api_v1_creatives_upload_post) | **POST** /api/v1/creatives/upload | Upload creative files.


# **api_v1_creative_folders_get**
> api_v1_creative_folders_get(with_counts=with_counts, creative_type=creative_type)

List media-bank folders.

The account's folder tree: `{id, name, pid, level}` rows, `pid` 0 for a
root, nested at most 3 tiers deep. Folders are the media bank's
exclusive axis — one folder per creative — and are separate from the
multi-valued groups on `creatives.tags`.


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
    api_instance = goadserver.CreativesApi(api_client)
    with_counts = 'with_counts_example' # str | Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count. (optional)
    creative_type = 'creative_type_example' # str | Narrow the counts to one creative type (comma-separated list accepted). (optional)

    try:
        # List media-bank folders.
        api_instance.api_v1_creative_folders_get(with_counts=with_counts, creative_type=creative_type)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creative_folders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_counts** | **str**| Add &#x60;count&#x60; (live creatives) per folder plus meta.unfiled_count and meta.creative_count. | [optional] 
 **creative_type** | **str**| Narrow the counts to one creative type (comma-separated list accepted). | [optional] 

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
**200** | {data: [{id, name, pid, level, count?}], meta}. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_folders_id_delete**
> api_v1_creative_folders_id_delete(id, move_to=move_to)

Delete a folder.

Never deletes creatives. The folder's creatives become unfiled — or move
to `move_to` — and its subfolders are reparented to the deleted folder's
own parent.


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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 
    move_to = 56 # int | File the folder's creatives here instead of unfiling them. (optional)

    try:
        # Delete a folder.
        api_instance.api_v1_creative_folders_id_delete(id, move_to=move_to)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creative_folders_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **move_to** | **int**| File the folder&#39;s creatives here instead of unfiling them. | [optional] 

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
**200** | {creatives_moved, children_reparented}. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_folders_id_put**
> api_v1_creative_folders_id_put(id, api_v1_creative_folders_id_put_request)

Rename or move a folder.

`name` is required. `pid` is optional — omitting it leaves the folder
where it is; sending it reparents the folder and its whole subtree,
which is refused if that would exceed the depth cap or form a cycle.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_folders_id_put_request import ApiV1CreativeFoldersIdPutRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 
    api_v1_creative_folders_id_put_request = goadserver.ApiV1CreativeFoldersIdPutRequest() # ApiV1CreativeFoldersIdPutRequest | 

    try:
        # Rename or move a folder.
        api_instance.api_v1_creative_folders_id_put(id, api_v1_creative_folders_id_put_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creative_folders_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_folders_id_put_request** | [**ApiV1CreativeFoldersIdPutRequest**](ApiV1CreativeFoldersIdPutRequest.md)|  | 

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
**200** | Updated. |  -  |
**404** | Not found. |  -  |
**422** | Invalid name or parent. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_folders_post**
> api_v1_creative_folders_post(api_v1_creative_folders_post_request)

Create a folder.

A folder whose name already exists under the same parent is returned
as-is with `existing: true` rather than duplicated, so this is safe to
call as create-or-reuse.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_folders_post_request import ApiV1CreativeFoldersPostRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    api_v1_creative_folders_post_request = goadserver.ApiV1CreativeFoldersPostRequest() # ApiV1CreativeFoldersPostRequest | 

    try:
        # Create a folder.
        api_instance.api_v1_creative_folders_post(api_v1_creative_folders_post_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creative_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creative_folders_post_request** | [**ApiV1CreativeFoldersPostRequest**](ApiV1CreativeFoldersPostRequest.md)|  | 

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
**200** | Existing folder returned ({existing: true}). |  -  |
**201** | The new folder. |  -  |
**422** | Missing name, unknown parent, cycle, or past the 3-tier depth cap. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_bulk_move_post**
> api_v1_creatives_bulk_move_post(api_v1_creatives_bulk_move_post_request)

File creatives into a folder.

Moves creatives into one media-bank folder. A creative sits in exactly
one folder, so this is an assignment: rows already filed elsewhere are
moved, and `folder_id: 0` unfiles them.

Two mutually exclusive selections:

  * `ids` — an explicit list (max 20000, applied in chunks).
  * `filter` — every creative matching a listing filter, given as the
    same query params `GET /api/v1/creatives` accepts
    (`creative_type`, `sizeid`, `orientation`, `folder_id`,
    `include_subfolders`, `deleted`/`all`). Use this to file a whole
    library; it is applied in batches server-side.

Nothing outside the key's own account can be reached by either form.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_bulk_move_post_request import ApiV1CreativesBulkMovePostRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    api_v1_creatives_bulk_move_post_request = goadserver.ApiV1CreativesBulkMovePostRequest() # ApiV1CreativesBulkMovePostRequest | 

    try:
        # File creatives into a folder.
        api_instance.api_v1_creatives_bulk_move_post(api_v1_creatives_bulk_move_post_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_bulk_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creatives_bulk_move_post_request** | [**ApiV1CreativesBulkMovePostRequest**](ApiV1CreativesBulkMovePostRequest.md)|  | 

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
**200** | {moved: N, folder_id}. |  -  |
**400** | No selection given. |  -  |
**422** | Unknown destination folder. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_get**
> ApiV1CreativesGet200Response api_v1_creatives_get(creative_type=creative_type, sizeid=sizeid, orientation=orientation, deleted=deleted, all=all, filter_name=filter_name, search=search, sort_by=sort_by, sort_dir=sort_dir, folder_id=folder_id, include_subfolders=include_subfolders, page=page, per_page=per_page, limit=limit, offset=offset, filter_id=filter_id, filter_type=filter_type, filter_sizeid=filter_sizeid)

List the creative library.

Uploaded creatives (banner / icon / native / video / reel) owned by the key.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_get200_response import ApiV1CreativesGet200Response
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
    api_instance = goadserver.CreativesApi(api_client)
    creative_type = 'native,creator' # str | One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.) (optional)
    sizeid = 56 # int | Banner size id. (optional)
    orientation = 'orientation_example' # str |  (optional)
    deleted = 'deleted_example' # str | 1 = only deleted creatives. (optional)
    all = 'all_example' # str | 1 = live and deleted creatives together. (optional)
    filter_name = 'filter_name_example' # str | Name contains. (optional)
    search = 'search_example' # str | Name contains. (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    folder_id = 56 # int | Media-bank folder id. 0 selects the unfiled creatives; omit for every folder. (optional)
    include_subfolders = 1 # str | With folder_id, also return creatives filed in that folder's subfolders. (optional) (default to 1)
    page = 1 # int |  (optional) (default to 1)
    per_page = goadserver.ApiV1CreativesGetPerPageParameter() # ApiV1CreativesGetPerPageParameter | Page size (max 100), or `all` for the whole library in one page. (optional)
    limit = 56 # int | Offset paging: page size (per_page wins when both are sent). (optional)
    offset = 56 # int | Offset paging: rows to skip. (optional)
    filter_id = 56 # int |  (optional)
    filter_type = 'filter_type_example' # str | Exactly one type; creative_type also takes a list. (optional)
    filter_sizeid = 56 # int | Same as sizeid. (optional)

    try:
        # List the creative library.
        api_response = api_instance.api_v1_creatives_get(creative_type=creative_type, sizeid=sizeid, orientation=orientation, deleted=deleted, all=all, filter_name=filter_name, search=search, sort_by=sort_by, sort_dir=sort_dir, folder_id=folder_id, include_subfolders=include_subfolders, page=page, per_page=per_page, limit=limit, offset=offset, filter_id=filter_id, filter_type=filter_type, filter_sizeid=filter_sizeid)
        print("The response of CreativesApi->api_v1_creatives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creative_type** | **str**| One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare &#x60;type&#x60; parameter is not read.) | [optional] 
 **sizeid** | **int**| Banner size id. | [optional] 
 **orientation** | **str**|  | [optional] 
 **deleted** | **str**| 1 &#x3D; only deleted creatives. | [optional] 
 **all** | **str**| 1 &#x3D; live and deleted creatives together. | [optional] 
 **filter_name** | **str**| Name contains. | [optional] 
 **search** | **str**| Name contains. | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **folder_id** | **int**| Media-bank folder id. 0 selects the unfiled creatives; omit for every folder. | [optional] 
 **include_subfolders** | **str**| With folder_id, also return creatives filed in that folder&#39;s subfolders. | [optional] [default to 1]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | [**ApiV1CreativesGetPerPageParameter**](.md)| Page size (max 100), or &#x60;all&#x60; for the whole library in one page. | [optional] 
 **limit** | **int**| Offset paging: page size (per_page wins when both are sent). | [optional] 
 **offset** | **int**| Offset paging: rows to skip. | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_type** | **str**| Exactly one type; creative_type also takes a list. | [optional] 
 **filter_sizeid** | **int**| Same as sizeid. | [optional] 

### Return type

[**ApiV1CreativesGet200Response**](ApiV1CreativesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creatives. Each row carries folder_id (0 &#x3D; unfiled). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_delete**
> api_v1_creatives_id_delete(id)

Delete a creative.

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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 

    try:
        # Delete a creative.
        api_instance.api_v1_creatives_id_delete(id)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_get**
> api_v1_creatives_id_get(id)

Show one creative.

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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 

    try:
        # Show one creative.
        api_instance.api_v1_creatives_id_get(id)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_get: %s\n" % e)
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
**200** | The creative. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_name_put**
> api_v1_creatives_id_name_put(id, api_v1_creatives_id_name_put_request)

Rename a creative (panel inline edit).

The panel's own rename call. Also retitles the pool items built from
this creative. Prefer `PUT /api/v1/creatives/{id}` for new code.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_id_name_put_request import ApiV1CreativesIdNamePutRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 
    api_v1_creatives_id_name_put_request = goadserver.ApiV1CreativesIdNamePutRequest() # ApiV1CreativesIdNamePutRequest | 

    try:
        # Rename a creative (panel inline edit).
        api_instance.api_v1_creatives_id_name_put(id, api_v1_creatives_id_name_put_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creatives_id_name_put_request** | [**ApiV1CreativesIdNamePutRequest**](ApiV1CreativesIdNamePutRequest.md)|  | 

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
**200** | Renamed. |  -  |
**403** | Key pinned to other creatives, or a read-only member role. |  -  |
**404** | Creative not found. |  -  |
**422** | &#x60;name&#x60; missing or empty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_put**
> api_v1_creatives_id_put(id, api_v1_creatives_id_put_request)

Rename and/or re-tag a creative.

The panel's two inline creative edits in one strict call: `name`
(also retitles every pool item built from this creative, like the
panel rename) and `tags`. Send either or both; unknown fields are a
422. The creative's file / content cannot be changed — upload a new
creative instead. Same ownership and member-scope checks as the
panel (an own-scoped team member can only edit creatives they made).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_id_put_request import ApiV1CreativesIdPutRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 
    api_v1_creatives_id_put_request = {"name":"Summer promo 300x250","tags":[12,17]} # ApiV1CreativesIdPutRequest | 

    try:
        # Rename and/or re-tag a creative.
        api_instance.api_v1_creatives_id_put(id, api_v1_creatives_id_put_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creatives_id_put_request** | [**ApiV1CreativesIdPutRequest**](ApiV1CreativesIdPutRequest.md)|  | 

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
**403** | Key pinned to other creatives (&#x60;forbidden_resource&#x60;), or a read-only member role. |  -  |
**404** | Creative not found. |  -  |
**422** | Unknown field, empty name, nothing to update, or malformed tags. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_tags_put**
> api_v1_creatives_id_tags_put(id, api_v1_creatives_id_tags_put_request)

Replace a creative's tags (panel inline edit).

The panel's own tag edit. `tags` is an array of tenant tag ids; non-numeric entries are dropped and [] clears the tags.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_id_tags_put_request import ApiV1CreativesIdTagsPutRequest
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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 
    api_v1_creatives_id_tags_put_request = {"tags":[12,17]} # ApiV1CreativesIdTagsPutRequest | 

    try:
        # Replace a creative's tags (panel inline edit).
        api_instance.api_v1_creatives_id_tags_put(id, api_v1_creatives_id_tags_put_request)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creatives_id_tags_put_request** | [**ApiV1CreativesIdTagsPutRequest**](ApiV1CreativesIdTagsPutRequest.md)|  | 

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
**403** | Key pinned to other creatives, or a read-only member role. |  -  |
**404** | Creative not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_used_in_get**
> api_v1_creatives_id_used_in_get(id)

List ads / pools referencing this creative.

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
    api_instance = goadserver.CreativesApi(api_client)
    id = 56 # int | 

    try:
        # List ads / pools referencing this creative.
        api_instance.api_v1_creatives_id_used_in_get(id)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_id_used_in_get: %s\n" % e)
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
**200** | Usage list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_upload_post**
> api_v1_creatives_upload_post(files, type=type, banner_size=banner_size, tags=tags, folder_id=folder_id, folder_name=folder_name, upload_zip=upload_zip, folder_from_zip=folder_from_zip, folder_from_zip_paths=folder_from_zip_paths, zipfile=zipfile, icontags=icontags, properties=properties, skiperrors=skiperrors, use_overlays=use_overlays, clone_per_overlay=clone_per_overlay, overlay=overlay, overlays_zip=overlays_zip)

Upload creative files.

`multipart/form-data` upload of one or more real creative files.
The server stores each file, creates a `creatives` row and
returns the new ids — reference them later via `creative_id` on
ad-create or pool-item-add. Field `files` (repeatable) carries
the uploads (`files[]`, `files[0]`…, `image`, `image[]`,
`image[0]`… and a singular `file` / `file[]` are accepted too);
`type` selects the creative kind. `creator` takes a poster image
paired with a hover video; `skin` a site-skin image; `html5` takes
HTML5 rich-media banners — each file is one .zip with an index.html
at the top (or inside one top folder), max 5 MB zipped / 20 MB
unpacked / 300 files, only web file types (html, css, js, json,
images, fonts, mp4/webm/mp3). The size is `banner_size` or the
bundle's `<meta name="ad.size" content="width=300,height=250">`.
It is created as a banner creative (content_type `html5`) and served
as an iframe with the IAB `clickTag` query parameter (also
`clickTAG`, `clicktag`) set to its click URL — open it from the
creative's click handler (`window.open(clickTag)`) so the click is
counted. `upload_zip=1` is refused for html5 (each zip is one banner).


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
    api_instance = goadserver.CreativesApi(api_client)
    files = None # List[bytes] | One or more creative files.
    type = banner # str | audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43). (optional) (default to banner)
    banner_size = 56 # int | Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own. (optional)
    tags = 'tags_example' # str |  (optional)
    folder_id = 56 # int | File the batch into this existing media-bank folder. Omit or 0 for unfiled. (optional)
    folder_name = 'folder_name_example' # str | Create-or-reuse a folder with this name under folder_id and file the batch there. (optional)
    upload_zip = 'upload_zip_example' # str | Send one archive as `zipfile` instead of `files`; the server extracts it. (optional)
    folder_from_zip = 'folder_from_zip_example' # str | ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name. (optional)
    folder_from_zip_paths = 'folder_from_zip_paths_example' # str | ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers. (optional)
    zipfile = None # bytes | With upload_zip=1: the archive to extract. (optional)
    icontags = 'icontags_example' # str | type=icon only: tags for the icons; overrides `tags` when sent. (optional)
    properties = 'properties_example' # str | Comma-separated property ids stamped on every created creative. (optional)
    skiperrors = 'skiperrors_example' # str | 1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure. (optional)
    use_overlays = 'use_overlays_example' # str | 1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images. (optional)
    clone_per_overlay = 'clone_per_overlay_example' # str | With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files. (optional)
    overlay = None # List[bytes] | Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation. (optional)
    overlays_zip = None # List[bytes] | ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays. (optional)

    try:
        # Upload creative files.
        api_instance.api_v1_creatives_upload_post(files, type=type, banner_size=banner_size, tags=tags, folder_id=folder_id, folder_name=folder_name, upload_zip=upload_zip, folder_from_zip=folder_from_zip, folder_from_zip_paths=folder_from_zip_paths, zipfile=zipfile, icontags=icontags, properties=properties, skiperrors=skiperrors, use_overlays=use_overlays, clone_per_overlay=clone_per_overlay, overlay=overlay, overlays_zip=overlays_zip)
    except Exception as e:
        print("Exception when calling CreativesApi->api_v1_creatives_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytes]**| One or more creative files. | 
 **type** | **str**| audio &#x3D; audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as &lt;id&gt;.mp3, the duration measured. Use the id as creative_id with video_type&#x3D;creative on an audio ad (adtype 43). | [optional] [default to banner]
 **banner_size** | **int**| Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own. | [optional] 
 **tags** | **str**|  | [optional] 
 **folder_id** | **int**| File the batch into this existing media-bank folder. Omit or 0 for unfiled. | [optional] 
 **folder_name** | **str**| Create-or-reuse a folder with this name under folder_id and file the batch there. | [optional] 
 **upload_zip** | **str**| Send one archive as &#x60;zipfile&#x60; instead of &#x60;files&#x60;; the server extracts it. | [optional] 
 **folder_from_zip** | **str**| ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name. | [optional] 
 **folder_from_zip_paths** | **str**| ZIP uploads only: recreate the archive&#39;s own directories as subfolders, up to 3 tiers. | [optional] 
 **zipfile** | **bytes**| With upload_zip&#x3D;1: the archive to extract. | [optional] 
 **icontags** | **str**| type&#x3D;icon only: tags for the icons; overrides &#x60;tags&#x60; when sent. | [optional] 
 **properties** | **str**| Comma-separated property ids stamped on every created creative. | [optional] 
 **skiperrors** | **str**| 1 &#x3D; keep going past a file that fails and report it in &#x60;errors&#x60;; 0 stops at the first failure. | [optional] 
 **use_overlays** | **str**| 1 &#x3D; composite the PNG overlays sent on &#x60;overlay&#x60; / &#x60;overlays_zip&#x60; onto the uploaded images. | [optional] 
 **clone_per_overlay** | **str**| With use_overlays&#x3D;1: create one variant per overlay instead of rotating the overlays across the files. | [optional] 
 **overlay** | **List[bytes]**| Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation. | [optional] 
 **overlays_zip** | **List[bytes]**| ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {created: [{id, name, type, folder_id}], errors, folder_id}. |  -  |
**400** | No files / invalid type / invalid form. |  -  |
**409** | With skiperrors&#x3D;0: a file (or a ZIP entry) failed — body &#x60;{files: [{file, error}]}&#x60; names each one; nothing after it was stored. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


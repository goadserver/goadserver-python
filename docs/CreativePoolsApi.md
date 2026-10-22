# goadserver.CreativePoolsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_creative_pools_get**](CreativePoolsApi.md#api_v1_creative_pools_get) | **GET** /api/v1/creative-pools | List creative pools.
[**api_v1_creative_pools_id_add_creatives_post**](CreativePoolsApi.md#api_v1_creative_pools_id_add_creatives_post) | **POST** /api/v1/creative-pools/{id}/add-creatives | Add media-bank creatives to a pool.
[**api_v1_creative_pools_id_add_urls_post**](CreativePoolsApi.md#api_v1_creative_pools_id_add_urls_post) | **POST** /api/v1/creative-pools/{id}/add-urls | Add hotlinked image / video / HTML URLs to a pool.
[**api_v1_creative_pools_id_clone_post**](CreativePoolsApi.md#api_v1_creative_pools_id_clone_post) | **POST** /api/v1/creative-pools/{id}/clone | Clone a creative pool with all its items.
[**api_v1_creative_pools_id_delete**](CreativePoolsApi.md#api_v1_creative_pools_id_delete) | **DELETE** /api/v1/creative-pools/{id} | Soft-delete a creative pool.
[**api_v1_creative_pools_id_get**](CreativePoolsApi.md#api_v1_creative_pools_id_get) | **GET** /api/v1/creative-pools/{id} | Show a single creative pool.
[**api_v1_creative_pools_id_items_export_get**](CreativePoolsApi.md#api_v1_creative_pools_id_items_export_get) | **GET** /api/v1/creative-pools/{id}/items/export | Download pool items&#39; creative files as a ZIP.
[**api_v1_creative_pools_id_items_get**](CreativePoolsApi.md#api_v1_creative_pools_id_items_get) | **GET** /api/v1/creative-pools/{id}/items | List items in a creative pool.
[**api_v1_creative_pools_id_items_item_id_delete**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_delete) | **DELETE** /api/v1/creative-pools/{id}/items/{itemId} | Soft-delete a single pool item.
[**api_v1_creative_pools_id_items_item_id_put**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId} | Update a single pool item.
[**api_v1_creative_pools_id_items_item_id_toggle_put**](CreativePoolsApi.md#api_v1_creative_pools_id_items_item_id_toggle_put) | **PUT** /api/v1/creative-pools/{id}/items/{itemId}/toggle | Toggle a pool item on / off.
[**api_v1_creative_pools_id_items_mass_action_put**](CreativePoolsApi.md#api_v1_creative_pools_id_items_mass_action_put) | **PUT** /api/v1/creative-pools/{id}/items/mass-action | Bulk-change items of a creative pool.
[**api_v1_creative_pools_id_items_post**](CreativePoolsApi.md#api_v1_creative_pools_id_items_post) | **POST** /api/v1/creative-pools/{id}/items | Add an item to a creative pool.
[**api_v1_creative_pools_id_items_recover_post**](CreativePoolsApi.md#api_v1_creative_pools_id_items_recover_post) | **POST** /api/v1/creative-pools/{id}/items/recover | Put removed items back into a creative pool.
[**api_v1_creative_pools_id_put**](CreativePoolsApi.md#api_v1_creative_pools_id_put) | **PUT** /api/v1/creative-pools/{id} | Update creative pool meta.
[**api_v1_creative_pools_id_recover_post**](CreativePoolsApi.md#api_v1_creative_pools_id_recover_post) | **POST** /api/v1/creative-pools/{id}/recover | Restore an archived creative pool.
[**api_v1_creative_pools_id_used_in_get**](CreativePoolsApi.md#api_v1_creative_pools_id_used_in_get) | **GET** /api/v1/creative-pools/{id}/used-in | List campaigns / ads that reference this pool.
[**api_v1_creative_pools_post**](CreativePoolsApi.md#api_v1_creative_pools_post) | **POST** /api/v1/creative-pools | Create a creative pool.
[**api_v1_creatives_bulk_delete_post**](CreativePoolsApi.md#api_v1_creatives_bulk_delete_post) | **POST** /api/v1/creatives/bulk-delete | Soft-delete many media-bank creatives.
[**api_v1_creatives_bulk_undelete_post**](CreativePoolsApi.md#api_v1_creatives_bulk_undelete_post) | **POST** /api/v1/creatives/bulk-undelete | Restore many deleted creatives.
[**api_v1_creatives_id_undelete_put**](CreativePoolsApi.md#api_v1_creatives_id_undelete_put) | **PUT** /api/v1/creatives/{id}/undelete | Restore one deleted creative.


# **api_v1_creative_pools_get**
> ApiV1CreativePoolsGet200Response api_v1_creative_pools_get(filter_type=filter_type, filter_types=filter_types, filter_title=filter_title, filter_id=filter_id, filter_name=filter_name, filter_orientation=filter_orientation, state=state, search=search, fit_orientation=fit_orientation, select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir)

List creative pools.

Returns every creative pool owned by the caller. Each row carries
`items_count` (live items, `is_deleted=0`) and `total_sizes` (count
of distinct banner sizes). Tags are returned both as the raw CSV
string (`tags`) and as an array (`tagids`).

Filters use the `filter_` prefix (`filter_type`, `filter_title`,
`filter_id`, `filter_orientation`); `search` matches the title.
Sort with `sort_by` / `sort_dir`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_get200_response import ApiV1CreativePoolsGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    filter_type = 'filter_type_example' # str |  (optional)
    filter_types = 'native,creator' # str | Comma-separated list of pool types (banner, video, reel, image, native, creator). (optional)
    filter_title = 'filter_title_example' # str | Title contains. (optional)
    filter_id = 56 # int |  (optional)
    filter_name = 'filter_name_example' # str | Same as filter_title. (optional)
    filter_orientation = 'filter_orientation_example' # str | The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead. (optional)
    state = live # str | deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list. (optional) (default to live)
    search = 'search_example' # str | Title contains. (optional)
    fit_orientation = 'fit_orientation_example' # str | Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart. (optional)
    select_stats = 'select_stats_example' # str | 1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days). (optional)
    var_from = '2013-10-20' # date | With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. (optional)
    to = '2013-10-20' # date | With select_stats=1: last day of the stats window (YYYY-MM-DD). (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = goadserver.ApiV1CreativePoolsGetPerPageParameter() # ApiV1CreativePoolsGetPerPageParameter |  (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)

    try:
        # List creative pools.
        api_response = api_instance.api_v1_creative_pools_get(filter_type=filter_type, filter_types=filter_types, filter_title=filter_title, filter_id=filter_id, filter_name=filter_name, filter_orientation=filter_orientation, state=state, search=search, fit_orientation=fit_orientation, select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of CreativePoolsApi->api_v1_creative_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_type** | **str**|  | [optional] 
 **filter_types** | **str**| Comma-separated list of pool types (banner, video, reel, image, native, creator). | [optional] 
 **filter_title** | **str**| Title contains. | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_name** | **str**| Same as filter_title. | [optional] 
 **filter_orientation** | **str**| The pool&#39;s own orientation label — empty on most pools; fit_orientation looks at the creatives instead. | [optional] 
 **state** | **str**| deleted &#x3D; the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list. | [optional] [default to live]
 **search** | **str**| Title contains. | [optional] 
 **fit_orientation** | **str**| Adds how many of each pool&#39;s servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart. | [optional] 
 **select_stats** | **str**| 1 &#x3D; add views, clicks and conversions per pool for the from / to window (default the last 7 days). | [optional] 
 **var_from** | **date**| With select_stats&#x3D;1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. | [optional] 
 **to** | **date**| With select_stats&#x3D;1: last day of the stats window (YYYY-MM-DD). | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | [**ApiV1CreativePoolsGetPerPageParameter**](.md)|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]

### Return type

[**ApiV1CreativePoolsGet200Response**](ApiV1CreativePoolsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pools. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_add_creatives_post**
> api_v1_creative_pools_id_add_creatives_post(id, api_v1_creative_pools_id_add_creatives_post_request)

Add media-bank creatives to a pool.

Adds existing creatives (from `GET /api/v1/creatives` or
`POST /api/v1/creatives/upload`) to the pool by id — the panel's
"Add from library". Only creatives of the pool's own type are
added; ids that are not yours, not that type, or already in the
pool are skipped silently (`total` counts what was added). New
items need moderation unless the account auto-validates. A key
pinned to `creative_ids` may only add creatives on its pin (403
otherwise).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_add_creatives_post_request import ApiV1CreativePoolsIdAddCreativesPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_add_creatives_post_request = {"creative_ids":[1082426,1082427]} # ApiV1CreativePoolsIdAddCreativesPostRequest | 

    try:
        # Add media-bank creatives to a pool.
        api_instance.api_v1_creative_pools_id_add_creatives_post(id, api_v1_creative_pools_id_add_creatives_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_add_creatives_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_add_creatives_post_request** | [**ApiV1CreativePoolsIdAddCreativesPostRequest**](ApiV1CreativePoolsIdAddCreativesPostRequest.md)|  | 

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
**200** | Added. |  -  |
**403** | A creative id outside the key&#39;s creative pin (&#x60;forbidden_resource&#x60;). |  -  |
**404** | Pool not found. |  -  |
**422** | &#x60;creative_ids&#x60; empty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_add_urls_post**
> api_v1_creative_pools_id_add_urls_post(id, api_v1_creative_pools_id_add_urls_post_request)

Add hotlinked image / video / HTML URLs to a pool.

Bulk import of hotlinked creatives — the panel's "Add URLs". One
URL per line in `urls`; each becomes a media-bank creative plus a
pool item. The protocol is normalised to https. The file extension
decides the kind: jpg/jpeg/png/bmp/webp image, gif animated image,
mp4 video; anything else (or an image into a video pool) is
reported back in `err_data`. `type: html_url` hotlinks the URL as an
iframe banner instead. Creator pools refuse URLs (422). Keys pinned
to `creative_ids` cannot use this (it creates creatives).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_add_urls_post_request import ApiV1CreativePoolsIdAddUrlsPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_add_urls_post_request = {"urls":"https://cdn.example.com/a.jpg\nhttps://cdn.example.com/b.mp4","sizeid":71} # ApiV1CreativePoolsIdAddUrlsPostRequest | 

    try:
        # Add hotlinked image / video / HTML URLs to a pool.
        api_instance.api_v1_creative_pools_id_add_urls_post(id, api_v1_creative_pools_id_add_urls_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_add_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_add_urls_post_request** | [**ApiV1CreativePoolsIdAddUrlsPostRequest**](ApiV1CreativePoolsIdAddUrlsPostRequest.md)|  | 

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
**200** | Imported (per-URL failures listed, not fatal). |  -  |
**403** | Key pinned to creative_ids (&#x60;forbidden_resource&#x60;). |  -  |
**404** | Pool not found. |  -  |
**422** | &#x60;urls&#x60; empty, or a creator pool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_clone_post**
> ApiV1CreativePoolsIdClonePost201Response api_v1_creative_pools_id_clone_post(id)

Clone a creative pool with all its items.

Duplicates the pool row and every live item (`is_deleted=0`).
Cloned items share the same underlying `creative_id`, so the
binary creative file is not re-uploaded — both pools reference
the same row in the `creatives` table. The new pool's title is
suffixed with " (Copy)".


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_clone_post201_response import ApiV1CreativePoolsIdClonePost201Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Clone a creative pool with all its items.
        api_response = api_instance.api_v1_creative_pools_id_clone_post(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdClonePost201Response**](ApiV1CreativePoolsIdClonePost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pool cloned. |  -  |
**404** | Source pool not found. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_delete**
> ApiV1CreativePoolsIdDelete200Response api_v1_creative_pools_id_delete(id)

Soft-delete a creative pool.

Deletes the pool **and** its items. Inactive items always go; an
active item is kept only when it is the last active item of its
banner size / rating that campaign ads still use. If any item had
to be kept the call returns 409 (`total_items`, `deleted`) and the
pool itself stays — the deletable items ARE already gone. Note the
200 body spells the count `totalitems`, the 409 body `total_items`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_delete200_response import ApiV1CreativePoolsIdDelete200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a creative pool.
        api_response = api_instance.api_v1_creative_pools_id_delete(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdDelete200Response**](ApiV1CreativePoolsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pool deleted. |  -  |
**409** | Some items are still in use; pool not deleted. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_get**
> ApiV1CreativePoolsIdGet200Response api_v1_creative_pools_id_get(id)

Show a single creative pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_get200_response import ApiV1CreativePoolsIdGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Show a single creative pool.
        api_response = api_instance.api_v1_creative_pools_id_get(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdGet200Response**](ApiV1CreativePoolsIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pool detail. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_export_get**
> bytes api_v1_creative_pools_id_items_export_get(id, ids)

Download pool items' creative files as a ZIP.

Returns `application/zip` (`Content-Disposition: attachment;
filename="pool-{id}-export.zip"`) with one file per item plus a
`_manifest.txt` listing which items were exported, skipped (no
exportable source) or failed. Hotlinked items are fetched
server-side (public addresses only). Max 500 items.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    ids = 'ids_example' # str | Comma-separated item ids, e.g. `55120,55121`.

    try:
        # Download pool items' creative files as a ZIP.
        api_response = api_instance.api_v1_creative_pools_id_items_export_get(id, ids)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_items_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ids** | **str**| Comma-separated item ids, e.g. &#x60;55120,55121&#x60;. | 

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ZIP archive. |  -  |
**400** | &#x60;no_ids&#x60;, &#x60;too_many_ids&#x60; (&gt; 500). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Pool not found, or none of the ids is an exportable item. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_get**
> ApiV1CreativesGet200Response api_v1_creative_pools_id_items_get(id, include_sizes=include_sizes, select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, filter_bansizeid=filter_bansizeid, filter_isactive=filter_isactive, sort_by=sort_by, sort_dir=sort_dir)

List items in a creative pool.

Returns every banner / video / native item in the pool with size,
creative metadata and lifetime stats (views, clicks, ctr, conv), plus
its schedule: `start_at` / `end_at` (unix seconds, 0 = no limit) and
`is_fallback` (0/1) — see the item update endpoint.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    include_sizes = 'include_sizes_example' # str | Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request. (optional)
    select_stats = 'select_stats_example' # str | 1 = add stats per item for the from / to window (default the last 7 days). (optional)
    var_from = '2013-10-20' # date | With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. (optional)
    to = '2013-10-20' # date | With select_stats=1: last day of the stats window (YYYY-MM-DD). (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    filter_bansizeid = 56 # int | Banner size id. (optional)
    filter_isactive = 56 # int |  (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)

    try:
        # List items in a creative pool.
        api_response = api_instance.api_v1_creative_pools_id_items_get(id, include_sizes=include_sizes, select_stats=select_stats, var_from=var_from, to=to, page=page, per_page=per_page, filter_bansizeid=filter_bansizeid, filter_isactive=filter_isactive, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include_sizes** | **str**| Banner pools: 1 &#x3D; also return the pool&#39;s banner sizes with an item count each, saving a second request. | [optional] 
 **select_stats** | **str**| 1 &#x3D; add stats per item for the from / to window (default the last 7 days). | [optional] 
 **var_from** | **date**| With select_stats&#x3D;1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days. | [optional] 
 **to** | **date**| With select_stats&#x3D;1: last day of the stats window (YYYY-MM-DD). | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **filter_bansizeid** | **int**| Banner size id. | [optional] 
 **filter_isactive** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]

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
**200** | Items. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_delete**
> api_v1_creative_pools_id_items_item_id_delete(id, item_id)

Soft-delete a single pool item.

Refuses if the item is still referenced by a live ad — unhook
the ad first.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 

    try:
        # Soft-delete a single pool item.
        api_instance.api_v1_creative_pools_id_items_item_id_delete(id, item_id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 

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
**409** | Item still used in a live ad. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_put**
> api_v1_creative_pools_id_items_item_id_put(id, item_id, api_v1_creative_pools_id_items_item_id_put_request)

Update a single pool item.

Editable fields: `title`, `lang`, `properties`, `ratingid`,
`url_prefix`, `weight` (whole number 0–1000000; drives
`sort_type: wr` rotation — 400 `invalid_weight` otherwise),
`is_fallback`, `start_at`, `end_at`. Active state is toggled via the
`/toggle` endpoint below.

**Scheduling.** `start_at` / `end_at` make the item serve only inside
`[start_at, end_at)`. Send unix seconds or an RFC 3339 time with its
offset (`2026-10-20T09:00:00-04:00` = 9:00 AM New York); `null`, `0`
or `""` clears that side. The list endpoint returns both as unix
seconds (0 = no limit). The ad servers pick up an edit within
5 minutes and then switch on the exact second, so save a schedule a
few minutes ahead of its start.

**Fallback.** `is_fallback: true` makes the item serve only while no
other item of the same pool and size is live. Typical promo swap: mark
the regular creative as fallback and give the promo a `start_at` (and
`end_at`); the regular one steps aside while the promo runs and
returns when it ends.

A change that would leave a size still used by campaign ads with
nothing to serve at some moment is refused with 409
`SCHEDULE_LEAVES_POOL_EMPTY`; `gap_at` is the first uncovered unix
second. Pausing or deleting an item runs the same check over the
other items' schedules.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request import ApiV1CreativePoolsIdItemsItemIdPutRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 
    api_v1_creative_pools_id_items_item_id_put_request = {"is_fallback":false,"start_at":"2026-10-20T09:00:00-04:00","end_at":"2026-10-27T09:00:00-04:00"} # ApiV1CreativePoolsIdItemsItemIdPutRequest | 

    try:
        # Update a single pool item.
        api_instance.api_v1_creative_pools_id_items_item_id_put(id, item_id, api_v1_creative_pools_id_items_item_id_put_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 
 **api_v1_creative_pools_id_items_item_id_put_request** | [**ApiV1CreativePoolsIdItemsItemIdPutRequest**](ApiV1CreativePoolsIdItemsItemIdPutRequest.md)|  | 

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
**400** | &#x60;invalid_weight&#x60;. |  -  |
**404** | Item not found. |  -  |
**409** | &#x60;SCHEDULE_LEAVES_POOL_EMPTY&#x60; — the schedule would leave a size still used by campaign ads with nothing to serve. |  -  |
**422** | Validation error on &#x60;start_at&#x60; / &#x60;end_at&#x60; (bad format, or end not after start). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_item_id_toggle_put**
> api_v1_creative_pools_id_items_item_id_toggle_put(id, item_id)

Toggle a pool item on / off.

Flips `isactive` between 0 and 1. Inactive items are skipped by the
ad-server when picking a creative from the pool. Pausing the last
active item of a format that campaign ads still use is refused (409).


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    item_id = 56 # int | 

    try:
        # Toggle a pool item on / off.
        api_instance.api_v1_creative_pools_id_items_item_id_toggle_put(id, item_id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_item_id_toggle_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **item_id** | **int**|  | 

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
**200** | Toggled. |  -  |
**404** | Item not found. |  -  |
**409** | &#x60;THIS_AD_CAN_NOT_BE_PAUSED_BECAUSE_IT_IS_THE_ONLY_ONE_OF_THIS_FORMAT_AND_ITS_STILL_USED_IN_ONE_OR_MORE_ADS&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_mass_action_put**
> api_v1_creative_pools_id_items_mass_action_put(id, api_v1_creative_pools_id_items_mass_action_put_request)

Bulk-change items of a creative pool.

`action`:

- `activate` / `deactivate` — set `isactive`.
- `delete` — soft-delete the items.
- `url_prefix` — set each item's `url_prefix` to `url_prefix`.
- `language` — set each item's `lang` to `lang`.

Deactivate and delete refuse (409, nothing written) when an item is
the last active one of its size / rating still used by a campaign ad
— `blocked_ids` lists them, the same rule as the single-item
toggle / delete. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_items_mass_action_put_request import ApiV1CreativePoolsIdItemsMassActionPutRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_items_mass_action_put_request = {"action":"deactivate","ids":[55120,55121]} # ApiV1CreativePoolsIdItemsMassActionPutRequest | 

    try:
        # Bulk-change items of a creative pool.
        api_instance.api_v1_creative_pools_id_items_mass_action_put(id, api_v1_creative_pools_id_items_mass_action_put_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_mass_action_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_items_mass_action_put_request** | [**ApiV1CreativePoolsIdItemsMassActionPutRequest**](ApiV1CreativePoolsIdItemsMassActionPutRequest.md)|  | 

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
**400** | &#x60;invalid_action&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Creative pool not found. |  -  |
**409** | Some items are the last of their format still used in ads. |  -  |
**422** | No &#x60;ids&#x60;, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_post**
> api_v1_creative_pools_id_items_post(id, api_v1_creative_pools_id_items_post_request)

Add an item to a creative pool.

Adds one creative to the pool. Reference an uploaded creative by
`creative_id` (from `POST /api/v1/creatives/upload`; must be yours,
and on the key's creative pin if it has one) or supply a hotlink
`banner_url`. The pool's `type` decides the creative slot (banner /
video / image). To add many library creatives at once use
`POST …/{id}/add-creatives`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_items_post_request import ApiV1CreativePoolsIdItemsPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_items_post_request = {"creative_id":1082426,"title":"Q3 banner"} # ApiV1CreativePoolsIdItemsPostRequest | 

    try:
        # Add an item to a creative pool.
        api_instance.api_v1_creative_pools_id_items_post(id, api_v1_creative_pools_id_items_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_items_post_request** | [**ApiV1CreativePoolsIdItemsPostRequest**](ApiV1CreativePoolsIdItemsPostRequest.md)|  | 

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
**201** | Item added — body is {id, message}. |  -  |
**422** | Neither creative_id nor banner_url supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_items_recover_post**
> api_v1_creative_pools_id_items_recover_post(id, api_v1_creative_pools_id_items_recover_post_request)

Put removed items back into a creative pool.

The undo of DELETE /creative-pools/{id}/items/{itemId} (removing an
item also switches it off). `active_ids` are switched back on.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_items_recover_post_request import ApiV1CreativePoolsIdItemsRecoverPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_items_recover_post_request = goadserver.ApiV1CreativePoolsIdItemsRecoverPostRequest() # ApiV1CreativePoolsIdItemsRecoverPostRequest | 

    try:
        # Put removed items back into a creative pool.
        api_instance.api_v1_creative_pools_id_items_recover_post(id, api_v1_creative_pools_id_items_recover_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_items_recover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_items_recover_post_request** | [**ApiV1CreativePoolsIdItemsRecoverPostRequest**](ApiV1CreativePoolsIdItemsRecoverPostRequest.md)|  | 

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
**200** | &#x60;restored&#x60; &#x3D; items back. |  -  |
**404** | Pool not found or archived. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_put**
> api_v1_creative_pools_id_put(id, api_v1_creative_pools_id_put_request)

Update creative pool meta.

Updates any of `title` (alias `name`), `sort_type`, `conv_type`,
`tags`, `type`, `orientation`. `sort_type: wr` (weighted rotation
on item `weight`) needs the tenant's weighted-rotation option — 400
`weighted_rotation_disabled` otherwise.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_put_request import ApiV1CreativePoolsIdPutRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 
    api_v1_creative_pools_id_put_request = goadserver.ApiV1CreativePoolsIdPutRequest() # ApiV1CreativePoolsIdPutRequest | 

    try:
        # Update creative pool meta.
        api_instance.api_v1_creative_pools_id_put(id, api_v1_creative_pools_id_put_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_creative_pools_id_put_request** | [**ApiV1CreativePoolsIdPutRequest**](ApiV1CreativePoolsIdPutRequest.md)|  | 

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
**400** | &#x60;no_fields&#x60;, &#x60;invalid_sort_type&#x60;, &#x60;weighted_rotation_disabled&#x60; or &#x60;invalid_type&#x60;. |  -  |
**404** | Pool not found. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_recover_post**
> api_v1_creative_pools_id_recover_post(id)

Restore an archived creative pool.

Reverses the soft delete of DELETE /creative-pools/{id} (and of Cleanup's
Archive): the pool is listed and usable again. The items the delete took down come back as they were; for a pool deleted before 2026-10-16 every deleted item comes back paused (`items_paused: true`).
404 when the pool does not exist, is not archived, or was purged.


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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Restore an archived creative pool.
        api_instance.api_v1_creative_pools_id_recover_post(id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_recover_post: %s\n" % e)
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
**200** | Restored. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found, not archived or purged. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_id_used_in_get**
> ApiV1CreativePoolsIdUsedInGet200Response api_v1_creative_pools_id_used_in_get(id)

List campaigns / ads that reference this pool.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creative_pools_id_used_in_get200_response import ApiV1CreativePoolsIdUsedInGet200Response
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # List campaigns / ads that reference this pool.
        api_response = api_instance.api_v1_creative_pools_id_used_in_get(id)
        print("The response of CreativePoolsApi->api_v1_creative_pools_id_used_in_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_id_used_in_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1CreativePoolsIdUsedInGet200Response**](ApiV1CreativePoolsIdUsedInGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | References. |  -  |
**404** | Pool not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creative_pools_post**
> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response api_v1_creative_pools_post(api_v1_creative_pools_post_request)

Create a creative pool.

Creates an empty pool. Fill it with `POST …/{id}/add-creatives`
(media-bank ids), `POST …/{id}/add-urls` (hotlinks) or
`POST …/{id}/items` (one creative). Title collisions are
auto-suffixed with `_<unix>`. An unknown `type` is a 400
`invalid_type` (it used to fall back to banner).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_creative_pools_post_request import ApiV1CreativePoolsPostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    api_v1_creative_pools_post_request = goadserver.ApiV1CreativePoolsPostRequest() # ApiV1CreativePoolsPostRequest | 

    try:
        # Create a creative pool.
        api_response = api_instance.api_v1_creative_pools_post(api_v1_creative_pools_post_request)
        print("The response of CreativePoolsApi->api_v1_creative_pools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creative_pools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creative_pools_post_request** | [**ApiV1CreativePoolsPostRequest**](ApiV1CreativePoolsPostRequest.md)|  | 

### Return type

[**ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response**](ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. |  -  |
**400** | &#x60;invalid_type&#x60; — type not one of banner, video, native, creator. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Title missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_bulk_delete_post**
> api_v1_creatives_bulk_delete_post(api_v1_creatives_bulk_delete_post_request)

Soft-delete many media-bank creatives.

Sets `isdeleted = 1` on up to 500 of your creatives. Ads and pool
items already pointing at them keep working; deleted creatives just
leave the library. Restore with `POST /creatives/bulk-undelete` or
`PUT /creatives/{id}/undelete`. A key pinned to `creative_ids` may
only name pinned ids (403 `forbidden_resource`). Account members
with own-scoped creative rights only affect creatives they manage.
Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_bulk_delete_post_request import ApiV1CreativesBulkDeletePostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    api_v1_creatives_bulk_delete_post_request = {"ids":[99102,99103]} # ApiV1CreativesBulkDeletePostRequest | 

    try:
        # Soft-delete many media-bank creatives.
        api_instance.api_v1_creatives_bulk_delete_post(api_v1_creatives_bulk_delete_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creatives_bulk_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creatives_bulk_delete_post_request** | [**ApiV1CreativesBulkDeletePostRequest**](ApiV1CreativesBulkDeletePostRequest.md)|  | 

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
**200** | Number of creatives deleted. |  -  |
**400** | &#x60;no_ids&#x60;, &#x60;too_many_ids&#x60; (&gt; 500). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_bulk_undelete_post**
> api_v1_creatives_bulk_undelete_post(api_v1_creatives_bulk_undelete_post_request)

Restore many deleted creatives.

Inverse of `POST /creatives/bulk-delete` — same limits, pin and member rules.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_creatives_bulk_undelete_post_request import ApiV1CreativesBulkUndeletePostRequest
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
    api_instance = goadserver.CreativePoolsApi(api_client)
    api_v1_creatives_bulk_undelete_post_request = {ids=[99102, 99103]} # ApiV1CreativesBulkUndeletePostRequest | 

    try:
        # Restore many deleted creatives.
        api_instance.api_v1_creatives_bulk_undelete_post(api_v1_creatives_bulk_undelete_post_request)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creatives_bulk_undelete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_creatives_bulk_undelete_post_request** | [**ApiV1CreativesBulkUndeletePostRequest**](ApiV1CreativesBulkUndeletePostRequest.md)|  | 

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
**200** | Number of creatives restored. |  -  |
**400** | &#x60;no_ids&#x60;, &#x60;too_many_ids&#x60; (&gt; 500). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_creatives_id_undelete_put**
> api_v1_creatives_id_undelete_put(id)

Restore one deleted creative.

Undoes `DELETE /creatives/{id}`. Same handler as the panel. No body.

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
    api_instance = goadserver.CreativePoolsApi(api_client)
    id = 56 # int | 

    try:
        # Restore one deleted creative.
        api_instance.api_v1_creatives_id_undelete_put(id)
    except Exception as e:
        print("Exception when calling CreativePoolsApi->api_v1_creatives_id_undelete_put: %s\n" % e)
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
**200** | Restored. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Creative not found, or not deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


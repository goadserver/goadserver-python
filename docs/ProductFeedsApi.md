# goadserver.ProductFeedsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_feeds_get**](ProductFeedsApi.md#api_v1_product_feeds_get) | **GET** /api/v1/product-feeds | List product feeds.
[**api_v1_product_feeds_id_delete**](ProductFeedsApi.md#api_v1_product_feeds_id_delete) | **DELETE** /api/v1/product-feeds/{id} | Delete a product feed.
[**api_v1_product_feeds_id_get**](ProductFeedsApi.md#api_v1_product_feeds_id_get) | **GET** /api/v1/product-feeds/{id} | Show a product feed.
[**api_v1_product_feeds_id_items_get**](ProductFeedsApi.md#api_v1_product_feeds_id_items_get) | **GET** /api/v1/product-feeds/{id}/items | The feed&#39;s products and their ads.
[**api_v1_product_feeds_id_patch**](ProductFeedsApi.md#api_v1_product_feeds_id_patch) | **PATCH** /api/v1/product-feeds/{id} | Change a product feed.
[**api_v1_product_feeds_id_sync_post**](ProductFeedsApi.md#api_v1_product_feeds_id_sync_post) | **POST** /api/v1/product-feeds/{id}/sync | Sync a product feed now.
[**api_v1_product_feeds_post**](ProductFeedsApi.md#api_v1_product_feeds_post) | **POST** /api/v1/product-feeds | Add a product feed.
[**api_v1_product_feeds_preview_post**](ProductFeedsApi.md#api_v1_product_feeds_preview_post) | **POST** /api/v1/product-feeds/preview | Preview a dynamic banner.


# **api_v1_product_feeds_get**
> api_v1_product_feeds_get()

List product feeds.

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
    api_instance = goadserver.ProductFeedsApi(api_client)

    try:
        # List product feeds.
        api_instance.api_v1_product_feeds_get()
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_get: %s\n" % e)
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
**200** | &#x60;data&#x60; &#x3D; the feeds, newest first; &#x60;banner_sizes&#x60; &#x3D; the tenant&#39;s banner sizes {id, name, width, height} for &#x60;bansizeid&#x60;; &#x60;templates&#x60; &#x3D; the built-in layouts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_id_delete**
> api_v1_product_feeds_id_delete(id)

Delete a product feed.

The feed goes; its ads stay in the campaign, paused, so their stats remain.

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
    api_instance = goadserver.ProductFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a product feed.
        api_instance.api_v1_product_feeds_id_delete(id)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_id_delete: %s\n" % e)
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
**200** | &#x60;data&#x60; &#x3D; &#x60;{id, deleted: true}&#x60;. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_id_get**
> api_v1_product_feeds_id_get(id)

Show a product feed.

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
    api_instance = goadserver.ProductFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Show a product feed.
        api_instance.api_v1_product_feeds_id_get(id)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_id_get: %s\n" % e)
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
**200** | The feed with its last run. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_id_items_get**
> api_v1_product_feeds_id_items_get(id)

The feed's products and their ads.

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
    api_instance = goadserver.ProductFeedsApi(api_client)
    id = 56 # int | 

    try:
        # The feed's products and their ads.
        api_instance.api_v1_product_feeds_id_items_get(id)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_id_items_get: %s\n" % e)
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
**200** | &#x60;data&#x60; &#x3D; products (at most 5000): &#x60;external_id&#x60;, &#x60;ad_id&#x60;, &#x60;title&#x60;, &#x60;price&#x60;, &#x60;in_stock&#x60;, &#x60;seen_at&#x60;. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_id_patch**
> api_v1_product_feeds_id_patch(id)

Change a product feed.

Any of the POST fields, plus `is_active` (false stops scheduled syncs; existing ads stay as they are).

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
    api_instance = goadserver.ProductFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Change a product feed.
        api_instance.api_v1_product_feeds_id_patch(id)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_id_patch: %s\n" % e)
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
**200** | &#x60;data&#x60; &#x3D; the feed. |  -  |
**404** | Feed not found. |  -  |
**422** | &#x60;validation_error&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_id_sync_post**
> api_v1_product_feeds_id_sync_post(id)

Sync a product feed now.

Starts a run in the background (one at a time per feed); poll GET /product-feeds/{id} for the result. A run creates at most 1000 new ads.

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
    api_instance = goadserver.ProductFeedsApi(api_client)
    id = 56 # int | 

    try:
        # Sync a product feed now.
        api_instance.api_v1_product_feeds_id_sync_post(id)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_id_sync_post: %s\n" % e)
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
**202** | &#x60;data&#x60; &#x3D; &#x60;{id, running: true}&#x60;. |  -  |
**404** | Feed not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_post**
> api_v1_product_feeds_post(api_v1_product_feeds_post_request)

Add a product feed.

Saved, then synced once in the background (watch `running`,
`last_status`, `last_message`). Body: `campaign_id` (required — one
of your RON campaigns with ad type native 3 or Search Ads 42), `url`
(required, http(s), public host, at most 20 MB), `name`, `format`
(`auto` | `xml` | `csv`, default auto), `refresh_hours` (0 = manual,
1, 6, 12 or 24), `max_items` (1-5000), `price_in_title` (bool, the
price is appended to the ad title), `bid` (the new ads' bid; 0 =
the bid of the campaign's newest ad). Each product needs `id`, `title`, an http(s) `link`
and `image_link`; `sale_price` wins over `price`; availability
`out_of_stock` / `discontinued` pauses its ad.

Dynamic banners (banner campaigns, ad type 2 — required there,
refused on native ones): `template` (`card` | `overlay` | `minimal` |
`custom`), `bansizeid` (one of `banner_sizes`), `cta` (button text,
≤ 30, default "Shop now"), `accent` (#rrggbb button / price colour),
`template_html` (custom only, ≤ 20000 bytes; slots {{title}}
{{price}} {{image}} {{description}} {{display}} {{cta}}
{{accent}}, values HTML-escaped; link to {click_url} — without it
the whole banner is wrapped in the click link). Preview with POST
/product-feeds/preview. `retarget` (bool): every product ad carries
ad_options.feed {pk, rt}; put `pid=<product id>[,<id>…]` on your
retargeting pixel (`/rtpixel.go?id=<pixel>&pid=SKU-1`) on product
pages and a visitor who viewed products of this feed sees those
first (30 days).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_product_feeds_post_request import ApiV1ProductFeedsPostRequest
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
    api_instance = goadserver.ProductFeedsApi(api_client)
    api_v1_product_feeds_post_request = {"campaign_id":454450,"url":"https://shop.example.com/feed.xml","name":"Shop catalogue","refresh_hours":6,"max_items":500,"price_in_title":true} # ApiV1ProductFeedsPostRequest | 

    try:
        # Add a product feed.
        api_instance.api_v1_product_feeds_post(api_v1_product_feeds_post_request)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_product_feeds_post_request** | [**ApiV1ProductFeedsPostRequest**](ApiV1ProductFeedsPostRequest.md)|  | 

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
**201** | &#x60;data&#x60; &#x3D; the new feed. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60;: campaign_id, url, format, refresh_hours, max_items, bid, template, bansizeid, accent, template_html — or the 20-feed limit. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_feeds_preview_post**
> api_v1_product_feeds_preview_post(api_v1_product_feeds_preview_post_request)

Preview a dynamic banner.

Renders one product into a banner template without saving anything:
body `{template, template_html, cta, accent, bansizeid, product?}`
(`product` = {title, price, image_link, link, description}; a sample
product without it). Answers `{html, width, height}`; the html holds
the `{click_url}` placeholder the ad server fills when it serves.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_product_feeds_preview_post_request import ApiV1ProductFeedsPreviewPostRequest
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
    api_instance = goadserver.ProductFeedsApi(api_client)
    api_v1_product_feeds_preview_post_request = {"template":"card","bansizeid":3,"cta":"Shop now","accent":"#0b7a4b"} # ApiV1ProductFeedsPreviewPostRequest | 

    try:
        # Preview a dynamic banner.
        api_instance.api_v1_product_feeds_preview_post(api_v1_product_feeds_preview_post_request)
    except Exception as e:
        print("Exception when calling ProductFeedsApi->api_v1_product_feeds_preview_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_product_feeds_preview_post_request** | [**ApiV1ProductFeedsPreviewPostRequest**](ApiV1ProductFeedsPreviewPostRequest.md)|  | 

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
**200** | The rendered banner. |  -  |
**422** | &#x60;validation_error&#x60; (template, accent, template_html). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


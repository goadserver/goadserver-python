# goadserver.CouponsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_coupons_sets_get**](CouponsApi.md#api_v1_coupons_sets_get) | **GET** /api/v1/coupons/sets | List coupon sets.
[**api_v1_coupons_sets_id_delete**](CouponsApi.md#api_v1_coupons_sets_id_delete) | **DELETE** /api/v1/coupons/sets/{id} | Delete a set and all its codes.
[**api_v1_coupons_sets_id_export_get**](CouponsApi.md#api_v1_coupons_sets_id_export_get) | **GET** /api/v1/coupons/sets/{id}/export | Export a set&#39;s codes as CSV.
[**api_v1_coupons_sets_id_generate_post**](CouponsApi.md#api_v1_coupons_sets_id_generate_post) | **POST** /api/v1/coupons/sets/{id}/generate | Generate codes in a set.
[**api_v1_coupons_sets_id_put**](CouponsApi.md#api_v1_coupons_sets_id_put) | **PUT** /api/v1/coupons/sets/{id} | Rename a set or move its end date.
[**api_v1_coupons_sets_post**](CouponsApi.md#api_v1_coupons_sets_post) | **POST** /api/v1/coupons/sets | Create a coupon set.
[**api_v1_coupons_sets_set_id_coupons_get**](CouponsApi.md#api_v1_coupons_sets_set_id_coupons_get) | **GET** /api/v1/coupons/sets/{setId}/coupons | List the codes in a set.


# **api_v1_coupons_sets_get**
> api_v1_coupons_sets_get(page=page, per_page=per_page, search=search, sort_by=sort_by)

List coupon sets.

Each set carries `coupon_count` (non-deleted codes). `search` matches the name.

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
    api_instance = goadserver.CouponsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)

    try:
        # List coupon sets.
        api_instance.api_v1_coupons_sets_get(page=page, per_page=per_page, search=search, sort_by=sort_by)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 

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
**200** | Sets. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_id_delete**
> api_v1_coupons_sets_id_delete(id)

Delete a set and all its codes.

Soft delete of the set and every code in it.

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
    api_instance = goadserver.CouponsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a set and all its codes.
        api_instance.api_v1_coupons_sets_id_delete(id)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_id_delete: %s\n" % e)
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
**404** | Set not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_id_export_get**
> api_v1_coupons_sets_id_export_get(id)

Export a set's codes as CSV.

`text/csv` attachment `coupons-<id>.csv`, no header row; one line per
code: `code,amount,end_date`.


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
    api_instance = goadserver.CouponsApi(api_client)
    id = 56 # int | 

    try:
        # Export a set's codes as CSV.
        api_instance.api_v1_coupons_sets_id_export_get(id)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_id_export_get: %s\n" % e)
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
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV. |  -  |
**404** | Set not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_id_generate_post**
> api_v1_coupons_sets_id_generate_post(id, api_v1_coupons_sets_id_generate_post_request)

Generate codes in a set.

Adds `count` new random codes (capped at 10000 per call), each worth
`amount`. `amount` is a whole number stored as given — the panel
shows it raw, so use the unit your redemption flow expects.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_coupons_sets_id_generate_post_request import ApiV1CouponsSetsIdGeneratePostRequest
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
    api_instance = goadserver.CouponsApi(api_client)
    id = 56 # int | 
    api_v1_coupons_sets_id_generate_post_request = {"count":100,"amount":10} # ApiV1CouponsSetsIdGeneratePostRequest | 

    try:
        # Generate codes in a set.
        api_instance.api_v1_coupons_sets_id_generate_post(id, api_v1_coupons_sets_id_generate_post_request)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_id_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_coupons_sets_id_generate_post_request** | [**ApiV1CouponsSetsIdGeneratePostRequest**](ApiV1CouponsSetsIdGeneratePostRequest.md)|  | 

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
**200** | Generated. |  -  |
**404** | Set not found. |  -  |
**422** | &#x60;INVALID_QUANTITY&#x60; (errors.quantity), &#x60;INVALID_AMOUNT&#x60;, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_id_put**
> api_v1_coupons_sets_id_put(id, api_v1_coupons_sets_id_put_request)

Rename a set or move its end date.

Partial — send `name`, `end_date` or both (empty values are ignored).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_coupons_sets_id_put_request import ApiV1CouponsSetsIdPutRequest
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
    api_instance = goadserver.CouponsApi(api_client)
    id = 56 # int | 
    api_v1_coupons_sets_id_put_request = {"end_date":"2027-01-31"} # ApiV1CouponsSetsIdPutRequest | 

    try:
        # Rename a set or move its end date.
        api_instance.api_v1_coupons_sets_id_put(id, api_v1_coupons_sets_id_put_request)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_coupons_sets_id_put_request** | [**ApiV1CouponsSetsIdPutRequest**](ApiV1CouponsSetsIdPutRequest.md)|  | 

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
**404** | Set not found. |  -  |
**422** | &#x60;INVALID_ENDDATE_GIVEN&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_post**
> api_v1_coupons_sets_post(api_v1_coupons_sets_post_request)

Create a coupon set.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_coupons_sets_post_request import ApiV1CouponsSetsPostRequest
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
    api_instance = goadserver.CouponsApi(api_client)
    api_v1_coupons_sets_post_request = {"name":"Autumn promo","end_date":"2026-12-31"} # ApiV1CouponsSetsPostRequest | 

    try:
        # Create a coupon set.
        api_instance.api_v1_coupons_sets_post(api_v1_coupons_sets_post_request)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_coupons_sets_post_request** | [**ApiV1CouponsSetsPostRequest**](ApiV1CouponsSetsPostRequest.md)|  | 

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
**422** | &#x60;validation_error&#x60; (&#x60;NO_NAME_GIVEN&#x60;, &#x60;INVALID_ENDDATE_GIVEN&#x60;) or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coupons_sets_set_id_coupons_get**
> api_v1_coupons_sets_set_id_coupons_get(set_id, page=page, per_page=per_page, filter_is_used=filter_is_used)

List the codes in a set.

`filter_is_used` = 0 / 1, `filter_code` / `search` match the code;
`sort_by` = id / code / amount / is_used / date_used.


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
    api_instance = goadserver.CouponsApi(api_client)
    set_id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    filter_is_used = 56 # int |  (optional)

    try:
        # List the codes in a set.
        api_instance.api_v1_coupons_sets_set_id_coupons_get(set_id, page=page, per_page=per_page, filter_is_used=filter_is_used)
    except Exception as e:
        print("Exception when calling CouponsApi->api_v1_coupons_sets_set_id_coupons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **filter_is_used** | **int**|  | [optional] 

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
**200** | Codes. |  -  |
**404** | Set not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


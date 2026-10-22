# goadserver.SourceOptimizersApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_cpa_optimizers_get**](SourceOptimizersApi.md#api_v1_cpa_optimizers_get) | **GET** /api/v1/cpa-optimizers | List CPA optimizers.
[**api_v1_cpa_optimizers_id_delete**](SourceOptimizersApi.md#api_v1_cpa_optimizers_id_delete) | **DELETE** /api/v1/cpa-optimizers/{id} | Delete a CPA optimizer.
[**api_v1_cpa_optimizers_id_get**](SourceOptimizersApi.md#api_v1_cpa_optimizers_id_get) | **GET** /api/v1/cpa-optimizers/{id} | Show a CPA optimizer.
[**api_v1_cpa_optimizers_id_put**](SourceOptimizersApi.md#api_v1_cpa_optimizers_id_put) | **PUT** /api/v1/cpa-optimizers/{id} | Replace a CPA optimizer.
[**api_v1_cpa_optimizers_post**](SourceOptimizersApi.md#api_v1_cpa_optimizers_post) | **POST** /api/v1/cpa-optimizers | Create a CPA optimizer.
[**api_v1_cpm_optimizers_active_get**](SourceOptimizersApi.md#api_v1_cpm_optimizers_active_get) | **GET** /api/v1/cpm-optimizers/active | Does the account have any CPM optimizer?
[**api_v1_cpm_optimizers_get**](SourceOptimizersApi.md#api_v1_cpm_optimizers_get) | **GET** /api/v1/cpm-optimizers | List CPM optimizers.
[**api_v1_cpm_optimizers_id_delete**](SourceOptimizersApi.md#api_v1_cpm_optimizers_id_delete) | **DELETE** /api/v1/cpm-optimizers/{id} | Delete a CPM optimizer.
[**api_v1_cpm_optimizers_id_get**](SourceOptimizersApi.md#api_v1_cpm_optimizers_id_get) | **GET** /api/v1/cpm-optimizers/{id} | Show a CPM optimizer.
[**api_v1_cpm_optimizers_id_put**](SourceOptimizersApi.md#api_v1_cpm_optimizers_id_put) | **PUT** /api/v1/cpm-optimizers/{id} | Replace a CPM optimizer.
[**api_v1_cpm_optimizers_post**](SourceOptimizersApi.md#api_v1_cpm_optimizers_post) | **POST** /api/v1/cpm-optimizers | Create a CPM optimizer.
[**api_v1_source_optimizer_config_get**](SourceOptimizersApi.md#api_v1_source_optimizer_config_get) | **GET** /api/v1/source-optimizer/config | Option values for the optimizer forms.


# **api_v1_cpa_optimizers_get**
> api_v1_cpa_optimizers_get()

List CPA optimizers.

A bare array. Money (`max_cpa`, the `target_cpa` values) is in the
account currency — stored ×100 as cents and divided back here.
`target_cpa` / `min_margin` are keyed by conversion-type id (see
GET /api/v1/tracking/conversion-types); `min_margin` is a percent.


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
    api_instance = goadserver.SourceOptimizersApi(api_client)

    try:
        # List CPA optimizers.
        api_instance.api_v1_cpa_optimizers_get()
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpa_optimizers_get: %s\n" % e)
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
**200** | Optimizers. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpa_optimizers_id_delete**
> api_v1_cpa_optimizers_id_delete(id)

Delete a CPA optimizer.

Soft delete. Returns 202 with `true` when a row was deleted, `false` when none matched. Refused for a campaign-pinned key.

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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 

    try:
        # Delete a CPA optimizer.
        api_instance.api_v1_cpa_optimizers_id_delete(id)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpa_optimizers_id_delete: %s\n" % e)
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
**202** | Bare boolean. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpa_optimizers_id_get**
> api_v1_cpa_optimizers_id_get(id)

Show a CPA optimizer.

`targets` is a one-element array (empty when the id is not the
caller's — no 404); `conversion_types` are the account's
conversion-type slots the `target_cpa` keys refer to.


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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 

    try:
        # Show a CPA optimizer.
        api_instance.api_v1_cpa_optimizers_id_get(id)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpa_optimizers_id_get: %s\n" % e)
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
**200** | The optimizer + conversion types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpa_optimizers_id_put**
> api_v1_cpa_optimizers_id_put(id, cpa_optimizer_body)

Replace a CPA optimizer.

Full replace with the create validation; fields left out reset to
their zero value (`start_date` left out keeps the stored date).
Refused for a campaign-pinned key. Returns the id.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.cpa_optimizer_body import CpaOptimizerBody
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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 
    cpa_optimizer_body = goadserver.CpaOptimizerBody() # CpaOptimizerBody | 

    try:
        # Replace a CPA optimizer.
        api_instance.api_v1_cpa_optimizers_id_put(id, cpa_optimizer_body)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpa_optimizers_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cpa_optimizer_body** | [**CpaOptimizerBody**](CpaOptimizerBody.md)|  | 

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
**200** | Saved; the id. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Optimizer not found. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpa_optimizers_post**
> api_v1_cpa_optimizers_post(cpa_optimizer_body)

Create a CPA optimizer.

`title` (non-alphanumerics become `_`) and a non-zero `max_cpa` are
required (422 `NO_TITLE` / `NO_PRICE_GIVEN`); a malformed
`start_date` → 422 `NO_VALID_DATE`. Money in account currency
(stored as cents). `bounce_max_perc` outside 0–100 and a
`min_margin` outside 0–100 are stored as 0. Returns the new id as a
bare number. `id` / `type` are accepted and ignored; any other
unknown key → 422 `unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.cpa_optimizer_body import CpaOptimizerBody
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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    cpa_optimizer_body = {"title":"CPA 2 EUR","filter_type":"spaceid","max_cpa":20,"max_days":14,"start_date":"2026-10-01","target_cpa":{"1":2.5},"min_margin":{"1":10},"cpa_action":"block","bounce_id":-1,"bounce_check_type":"auto"} # CpaOptimizerBody | 

    try:
        # Create a CPA optimizer.
        api_instance.api_v1_cpa_optimizers_post(cpa_optimizer_body)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpa_optimizers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpa_optimizer_body** | [**CpaOptimizerBody**](CpaOptimizerBody.md)|  | 

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
**201** | New optimizer id. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_active_get**
> api_v1_cpm_optimizers_active_get()

Does the account have any CPM optimizer?

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
    api_instance = goadserver.SourceOptimizersApi(api_client)

    try:
        # Does the account have any CPM optimizer?
        api_instance.api_v1_cpm_optimizers_active_get()
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_active_get: %s\n" % e)
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
**200** | Bare boolean. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_get**
> api_v1_cpm_optimizers_get()

List CPM optimizers.

A bare array (no envelope), ordered by title. Each item is the
stored settings merged with `id`, `userid`, `title` and
`type: "cpm"`. Money fields (`min_spendings`, `max_cpa`) are in the
account currency, as entered.


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
    api_instance = goadserver.SourceOptimizersApi(api_client)

    try:
        # List CPM optimizers.
        api_instance.api_v1_cpm_optimizers_get()
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_get: %s\n" % e)
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
**200** | Optimizers. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_id_delete**
> api_v1_cpm_optimizers_id_delete(id)

Delete a CPM optimizer.

Soft delete. Refused for a campaign-pinned key.

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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 

    try:
        # Delete a CPM optimizer.
        api_instance.api_v1_cpm_optimizers_id_delete(id)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_id_delete: %s\n" % e)
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
**404** | Optimizer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_id_get**
> api_v1_cpm_optimizers_id_get(id)

Show a CPM optimizer.

Returns a one-element array (panel shape).

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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 

    try:
        # Show a CPM optimizer.
        api_instance.api_v1_cpm_optimizers_id_get(id)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_id_get: %s\n" % e)
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
**200** | The optimizer. |  -  |
**404** | Optimizer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_id_put**
> api_v1_cpm_optimizers_id_put(id, cpm_optimizer_body)

Replace a CPM optimizer.

Full replace — the settings become exactly the body (fields left
out are cleared). Same validation as create. Every campaign using
the optimizer follows the change, so a campaign-pinned key gets 403
`forbidden_resource`. Returns the id.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.cpm_optimizer_body import CpmOptimizerBody
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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    id = 56 # int | 
    cpm_optimizer_body = goadserver.CpmOptimizerBody() # CpmOptimizerBody | 

    try:
        # Replace a CPM optimizer.
        api_instance.api_v1_cpm_optimizers_id_put(id, cpm_optimizer_body)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cpm_optimizer_body** | [**CpmOptimizerBody**](CpmOptimizerBody.md)|  | 

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
**200** | Saved; the id. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Optimizer not found. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_cpm_optimizers_post**
> api_v1_cpm_optimizers_post(cpm_optimizer_body)

Create a CPM optimizer.

`title` and a non-zero `min_spendings` are required (422
`NO_TITLE_GIVEN` / `NO_PRICE_GIVEN`). Every other listed field is
stored as sent. `id`, `type` and `userid` are accepted (and
ignored) so a fetched optimizer can be sent back; any other key →
422 `unknown_fields`. Returns the new id as a bare number.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.cpm_optimizer_body import CpmOptimizerBody
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
    api_instance = goadserver.SourceOptimizersApi(api_client)
    cpm_optimizer_body = {"title":"Zone cleaner","opt_type":"0","min_spendings":5,"max_days":30,"start_date":"2026-10-01","conv_type":"1","optimise_with":"conv_count","max_cpa":2,"use_bidoptimiser":0} # CpmOptimizerBody | 

    try:
        # Create a CPM optimizer.
        api_instance.api_v1_cpm_optimizers_post(cpm_optimizer_body)
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_cpm_optimizers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpm_optimizer_body** | [**CpmOptimizerBody**](CpmOptimizerBody.md)|  | 

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
**200** | New optimizer id. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | &#x60;validation_error&#x60; or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_source_optimizer_config_get**
> api_v1_source_optimizer_config_get()

Option values for the optimizer forms.

The values `filter_type`, `cpa_action` and `bounce_check_type` accept.

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
    api_instance = goadserver.SourceOptimizersApi(api_client)

    try:
        # Option values for the optimizer forms.
        api_instance.api_v1_source_optimizer_config_get()
    except Exception as e:
        print("Exception when calling SourceOptimizersApi->api_v1_source_optimizer_config_get: %s\n" % e)
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
**200** | Static option lists. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


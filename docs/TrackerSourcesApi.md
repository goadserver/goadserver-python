# goadserver.TrackerSourcesApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_cost_drivers_get**](TrackerSourcesApi.md#api_v1_tracker_cost_drivers_get) | **GET** /api/v1/tracker/cost-drivers | List available cost drivers.
[**api_v1_tracker_source_accounts_get**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_get) | **GET** /api/v1/tracker/source-accounts | List connected ad accounts.
[**api_v1_tracker_source_accounts_id_campaigns_get**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_campaigns_get) | **GET** /api/v1/tracker/source-accounts/{id}/campaigns | Campaigns visible in a connected ad account.
[**api_v1_tracker_source_accounts_id_delete**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_delete) | **DELETE** /api/v1/tracker/source-accounts/{id} | Disconnect an ad account.
[**api_v1_tracker_source_accounts_id_get**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_get) | **GET** /api/v1/tracker/source-accounts/{id} | Get one connected ad account.
[**api_v1_tracker_source_accounts_id_put**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_put) | **PUT** /api/v1/tracker/source-accounts/{id} | Update a connected ad account.
[**api_v1_tracker_source_accounts_id_sync_post**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_id_sync_post) | **POST** /api/v1/tracker/source-accounts/{id}/sync | Pull spend from a connected ad account now.
[**api_v1_tracker_source_accounts_post**](TrackerSourcesApi.md#api_v1_tracker_source_accounts_post) | **POST** /api/v1/tracker/source-accounts | Connect an ad account.
[**api_v1_tracker_sources_get**](TrackerSourcesApi.md#api_v1_tracker_sources_get) | **GET** /api/v1/tracker/sources | List traffic sources.
[**api_v1_tracker_sources_id_delete**](TrackerSourcesApi.md#api_v1_tracker_sources_id_delete) | **DELETE** /api/v1/tracker/sources/{id} | Delete a traffic source.
[**api_v1_tracker_sources_id_put**](TrackerSourcesApi.md#api_v1_tracker_sources_id_put) | **PUT** /api/v1/tracker/sources/{id} | Update a traffic source.
[**api_v1_tracker_sources_post**](TrackerSourcesApi.md#api_v1_tracker_sources_post) | **POST** /api/v1/tracker/sources | Create a traffic source.
[**api_v1_tracker_sources_siteid_campaigns_get**](TrackerSourcesApi.md#api_v1_tracker_sources_siteid_campaigns_get) | **GET** /api/v1/tracker/sources/{siteid}/campaigns | Campaigns reported by a source&#39;s connected ad account.


# **api_v1_tracker_cost_drivers_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_cost_drivers_get()

List available cost drivers.

The traffic-source APIs this build can pull spend from, and which are
actually implemented — the valid values for `driver` above.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)

    try:
        # List available cost drivers.
        api_response = api_instance.api_v1_tracker_cost_drivers_get()
        print("The response of TrackerSourcesApi->api_v1_tracker_cost_drivers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_cost_drivers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_get**
> ApiV1TrackerSourceAccountsGet200Response api_v1_tracker_source_accounts_get()

List connected ad accounts.

The credentialed ad accounts a scheduler pulls spend from, each with the
outcome of its last sync. Credentials are never returned.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_source_accounts_get200_response import ApiV1TrackerSourceAccountsGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)

    try:
        # List connected ad accounts.
        api_response = api_instance.api_v1_tracker_source_accounts_get()
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerSourceAccountsGet200Response**](ApiV1TrackerSourceAccountsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_id_campaigns_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_source_accounts_id_campaigns_get(id)

Campaigns visible in a connected ad account.

Used to bind a tracking link to a campaign on the buying side.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source account ID.

    try:
        # Campaigns visible in a connected ad account.
        api_response = api_instance.api_v1_tracker_source_accounts_id_campaigns_get(id)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_id_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_id_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source account ID. | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_source_accounts_id_delete(id)

Disconnect an ad account.

Stops the spend pull. Already-imported cost stays.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source account ID.

    try:
        # Disconnect an ad account.
        api_response = api_instance.api_v1_tracker_source_accounts_id_delete(id)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source account ID. | 

### Return type

[**ApiV1PublisherPushCampaignsIdDelete200Response**](ApiV1PublisherPushCampaignsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_id_get**
> ApiV1TrackerSourceAccountsIdGet200Response api_v1_tracker_source_accounts_id_get(id)

Get one connected ad account.

Credentials are omitted.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_source_accounts_id_get200_response import ApiV1TrackerSourceAccountsIdGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source account ID.

    try:
        # Get one connected ad account.
        api_response = api_instance.api_v1_tracker_source_accounts_id_get(id)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source account ID. | 

### Return type

[**ApiV1TrackerSourceAccountsIdGet200Response**](ApiV1TrackerSourceAccountsIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_source_accounts_id_put(id, api_v1_tracker_source_accounts_id_put_request)

Update a connected ad account.

Omit `credentials` to leave the stored secrets untouched.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_source_accounts_id_put_request import ApiV1TrackerSourceAccountsIdPutRequest
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source account ID.
    api_v1_tracker_source_accounts_id_put_request = goadserver.ApiV1TrackerSourceAccountsIdPutRequest() # ApiV1TrackerSourceAccountsIdPutRequest | 

    try:
        # Update a connected ad account.
        api_response = api_instance.api_v1_tracker_source_accounts_id_put(id, api_v1_tracker_source_accounts_id_put_request)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source account ID. | 
 **api_v1_tracker_source_accounts_id_put_request** | [**ApiV1TrackerSourceAccountsIdPutRequest**](ApiV1TrackerSourceAccountsIdPutRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_id_sync_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_source_accounts_id_sync_post(id)

Pull spend from a connected ad account now.

Runs the driver immediately instead of waiting for the daily schedule.
Returns what the run imported, or the driver's error.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source account ID.

    try:
        # Pull spend from a connected ad account now.
        api_response = api_instance.api_v1_tracker_source_accounts_id_sync_post(id)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_id_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_id_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source account ID. | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_source_accounts_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_source_accounts_post(api_v1_tracker_source_accounts_post_request)

Connect an ad account.

`driver` names the traffic source's API (see /cost-drivers).
`credentials` is encrypted at rest and never read back.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_source_accounts_post_request import ApiV1TrackerSourceAccountsPostRequest
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    api_v1_tracker_source_accounts_post_request = goadserver.ApiV1TrackerSourceAccountsPostRequest() # ApiV1TrackerSourceAccountsPostRequest | 

    try:
        # Connect an ad account.
        api_response = api_instance.api_v1_tracker_source_accounts_post(api_v1_tracker_source_accounts_post_request)
        print("The response of TrackerSourcesApi->api_v1_tracker_source_accounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_source_accounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_source_accounts_post_request** | [**ApiV1TrackerSourceAccountsPostRequest**](ApiV1TrackerSourceAccountsPostRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_sources_get**
> ApiV1TrackerSourcesGet200Response api_v1_tracker_sources_get()

List traffic sources.

One row per traffic origin (an ad account, a network). A source carries
the macro template its click URLs are built from and its own outbound
postback configuration, and is the unit member access is delegated by.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_sources_get200_response import ApiV1TrackerSourcesGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)

    try:
        # List traffic sources.
        api_response = api_instance.api_v1_tracker_sources_get()
        print("The response of TrackerSourcesApi->api_v1_tracker_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_sources_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerSourcesGet200Response**](ApiV1TrackerSourcesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_sources_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_sources_id_delete(id)

Delete a traffic source.

Refused while live tracking links still hang off the source — they would
orphan. Delete or move the links first.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source ID.

    try:
        # Delete a traffic source.
        api_response = api_instance.api_v1_tracker_sources_id_delete(id)
        print("The response of TrackerSourcesApi->api_v1_tracker_sources_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_sources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source ID. | 

### Return type

[**ApiV1PublisherPushCampaignsIdDelete200Response**](ApiV1PublisherPushCampaignsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Source still has live tracking links. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_sources_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_sources_id_put(id, api_v1_tracker_sources_id_put_request)

Update a traffic source.

Partial update.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_sources_id_put_request import ApiV1TrackerSourcesIdPutRequest
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    id = 56 # int | Source ID.
    api_v1_tracker_sources_id_put_request = goadserver.ApiV1TrackerSourcesIdPutRequest() # ApiV1TrackerSourcesIdPutRequest | 

    try:
        # Update a traffic source.
        api_response = api_instance.api_v1_tracker_sources_id_put(id, api_v1_tracker_sources_id_put_request)
        print("The response of TrackerSourcesApi->api_v1_tracker_sources_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_sources_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Source ID. | 
 **api_v1_tracker_sources_id_put_request** | [**ApiV1TrackerSourcesIdPutRequest**](ApiV1TrackerSourcesIdPutRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_sources_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_sources_post(api_v1_tracker_sources_post_request)

Create a traffic source.

`template_slug` picks the macro set (see /source-templates); it decides
which placeholders the generated click URLs carry.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_sources_post_request import ApiV1TrackerSourcesPostRequest
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    api_v1_tracker_sources_post_request = goadserver.ApiV1TrackerSourcesPostRequest() # ApiV1TrackerSourcesPostRequest | 

    try:
        # Create a traffic source.
        api_response = api_instance.api_v1_tracker_sources_post(api_v1_tracker_sources_post_request)
        print("The response of TrackerSourcesApi->api_v1_tracker_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_sources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_sources_post_request** | [**ApiV1TrackerSourcesPostRequest**](ApiV1TrackerSourcesPostRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsPost200Response**](ApiV1PublisherPushCampaignsPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_sources_siteid_campaigns_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_sources_siteid_campaigns_get(siteid)

Campaigns reported by a source's connected ad account.

What the buying side calls its campaigns, for binding tracking links to.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_zone_costs_get200_response import ApiV1TrackerTrackingLinksIdZoneCostsGet200Response
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
    api_instance = goadserver.TrackerSourcesApi(api_client)
    siteid = 56 # int | Source ID.

    try:
        # Campaigns reported by a source's connected ad account.
        api_response = api_instance.api_v1_tracker_sources_siteid_campaigns_get(siteid)
        print("The response of TrackerSourcesApi->api_v1_tracker_sources_siteid_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerSourcesApi->api_v1_tracker_sources_siteid_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteid** | **int**| Source ID. | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


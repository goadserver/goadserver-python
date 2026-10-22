# goadserver.TrackerConversionsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_conversion_logging_get**](TrackerConversionsApi.md#api_v1_tracker_conversion_logging_get) | **GET** /api/v1/tracker/conversion-logging | Get conversion-logging settings.
[**api_v1_tracker_conversion_logging_put**](TrackerConversionsApi.md#api_v1_tracker_conversion_logging_put) | **PUT** /api/v1/tracker/conversion-logging | Change conversion-logging settings.
[**api_v1_tracker_conversion_types_get**](TrackerConversionsApi.md#api_v1_tracker_conversion_types_get) | **GET** /api/v1/tracker/conversion-types | Get the conversion-type labels.
[**api_v1_tracker_conversion_types_put**](TrackerConversionsApi.md#api_v1_tracker_conversion_types_put) | **PUT** /api/v1/tracker/conversion-types | Rename the conversion types.
[**api_v1_tracker_conversions_clickid_postbacks_get**](TrackerConversionsApi.md#api_v1_tracker_conversions_clickid_postbacks_get) | **GET** /api/v1/tracker/conversions/{clickid}/postbacks | Outbound postbacks fired for one conversion.
[**api_v1_tracker_conversions_get**](TrackerConversionsApi.md#api_v1_tracker_conversions_get) | **GET** /api/v1/tracker/conversions | List incoming conversions.
[**api_v1_tracker_conversions_id_state_put**](TrackerConversionsApi.md#api_v1_tracker_conversions_id_state_put) | **PUT** /api/v1/tracker/conversions/{id}/state | Approve or reject one conversion.
[**api_v1_tracker_conversions_rejected_get**](TrackerConversionsApi.md#api_v1_tracker_conversions_rejected_get) | **GET** /api/v1/tracker/conversions/rejected | List refused inbound postbacks.


# **api_v1_tracker_conversion_logging_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversion_logging_get()

Get conversion-logging settings.

Whether incoming conversions are logged, and whether they land pending
review rather than settled.


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
    api_instance = goadserver.TrackerConversionsApi(api_client)

    try:
        # Get conversion-logging settings.
        api_response = api_instance.api_v1_tracker_conversion_logging_get()
        print("The response of TrackerConversionsApi->api_v1_tracker_conversion_logging_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversion_logging_get: %s\n" % e)
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

# **api_v1_tracker_conversion_logging_put**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversion_logging_put(api_v1_tracker_conversion_logging_put_request)

Change conversion-logging settings.

Turning `pend_conversions` on routes new conversions to the pending queue
instead of settling them on arrival.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_conversion_logging_put_request import ApiV1TrackerConversionLoggingPutRequest
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
    api_instance = goadserver.TrackerConversionsApi(api_client)
    api_v1_tracker_conversion_logging_put_request = goadserver.ApiV1TrackerConversionLoggingPutRequest() # ApiV1TrackerConversionLoggingPutRequest | 

    try:
        # Change conversion-logging settings.
        api_response = api_instance.api_v1_tracker_conversion_logging_put(api_v1_tracker_conversion_logging_put_request)
        print("The response of TrackerConversionsApi->api_v1_tracker_conversion_logging_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversion_logging_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_conversion_logging_put_request** | [**ApiV1TrackerConversionLoggingPutRequest**](ApiV1TrackerConversionLoggingPutRequest.md)|  | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

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

# **api_v1_tracker_conversion_types_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversion_types_get()

Get the conversion-type labels.

The caller's A–Z map — which event each conversion-type letter means.


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
    api_instance = goadserver.TrackerConversionsApi(api_client)

    try:
        # Get the conversion-type labels.
        api_response = api_instance.api_v1_tracker_conversion_types_get()
        print("The response of TrackerConversionsApi->api_v1_tracker_conversion_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversion_types_get: %s\n" % e)
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

# **api_v1_tracker_conversion_types_put**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversion_types_put(api_v1_tracker_conversion_types_put_request)

Rename the conversion types.

Bulk replace of the letter → label map.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_conversion_types_put_request import ApiV1TrackerConversionTypesPutRequest
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
    api_instance = goadserver.TrackerConversionsApi(api_client)
    api_v1_tracker_conversion_types_put_request = goadserver.ApiV1TrackerConversionTypesPutRequest() # ApiV1TrackerConversionTypesPutRequest | 

    try:
        # Rename the conversion types.
        api_response = api_instance.api_v1_tracker_conversion_types_put(api_v1_tracker_conversion_types_put_request)
        print("The response of TrackerConversionsApi->api_v1_tracker_conversion_types_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversion_types_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_conversion_types_put_request** | [**ApiV1TrackerConversionTypesPutRequest**](ApiV1TrackerConversionTypesPutRequest.md)|  | 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

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

# **api_v1_tracker_conversions_clickid_postbacks_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversions_clickid_postbacks_get(clickid, conv_type=conv_type)

Outbound postbacks fired for one conversion.

Joined by clickid — what was forwarded upstream, when, and how it answered.


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
    api_instance = goadserver.TrackerConversionsApi(api_client)
    clickid = 'clickid_example' # str | The conversion's click id.
    conv_type = 'conv_type_example' # str | Narrow to one conversion type letter. (optional)

    try:
        # Outbound postbacks fired for one conversion.
        api_response = api_instance.api_v1_tracker_conversions_clickid_postbacks_get(clickid, conv_type=conv_type)
        print("The response of TrackerConversionsApi->api_v1_tracker_conversions_clickid_postbacks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversions_clickid_postbacks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickid** | **str**| The conversion&#39;s click id. | 
 **conv_type** | **str**| Narrow to one conversion type letter. | [optional] 

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

# **api_v1_tracker_conversions_get**
> ApiV1TrackerConversionsGet200Response api_v1_tracker_conversions_get(start_date=start_date, end_date=end_date, state=state, reason_id=reason_id, search=search, sort_by=sort_by, sort_dir=sort_dir, limit=limit)

List incoming conversions.

Conversions logged against the caller's offers, with the summary counts
(clean / on hold / approved / rejected) the settlement view sums.
Requires conversion logging to be on — see /conversion-logging.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_conversions_get200_response import ApiV1TrackerConversionsGet200Response
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
    api_instance = goadserver.TrackerConversionsApi(api_client)
    start_date = 'start_date_example' # str | Start of the window, YYYY-MM-DD. (optional)
    end_date = 'end_date_example' # str | End of the window, YYYY-MM-DD. (optional)
    state = 56 # int | Filter by settlement state. (optional)
    reason_id = 56 # int | Filter by hold/reject reason. (optional)
    search = 'search_example' # str | Match against clickid, offer or link name. (optional)
    sort_by = 'sort_by_example' # str | Column to sort on. (optional)
    sort_dir = 'sort_dir_example' # str | asc or desc. (optional)
    limit = 56 # int | Maximum rows to return. (optional)

    try:
        # List incoming conversions.
        api_response = api_instance.api_v1_tracker_conversions_get(start_date=start_date, end_date=end_date, state=state, reason_id=reason_id, search=search, sort_by=sort_by, sort_dir=sort_dir, limit=limit)
        print("The response of TrackerConversionsApi->api_v1_tracker_conversions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start of the window, YYYY-MM-DD. | [optional] 
 **end_date** | **str**| End of the window, YYYY-MM-DD. | [optional] 
 **state** | **int**| Filter by settlement state. | [optional] 
 **reason_id** | **int**| Filter by hold/reject reason. | [optional] 
 **search** | **str**| Match against clickid, offer or link name. | [optional] 
 **sort_by** | **str**| Column to sort on. | [optional] 
 **sort_dir** | **str**| asc or desc. | [optional] 
 **limit** | **int**| Maximum rows to return. | [optional] 

### Return type

[**ApiV1TrackerConversionsGet200Response**](ApiV1TrackerConversionsGet200Response.md)

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

# **api_v1_tracker_conversions_id_state_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_conversions_id_state_put(id, api_v1_tracker_conversions_id_state_put_request)

Approve or reject one conversion.

Settles a pending conversion. This is the one tracker write that moves
money-bearing state, which is why it carries its own scope rather than
riding on tracker.write.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_conversions_id_state_put_request import ApiV1TrackerConversionsIdStatePutRequest
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
    api_instance = goadserver.TrackerConversionsApi(api_client)
    id = 56 # int | Conversion ID.
    api_v1_tracker_conversions_id_state_put_request = goadserver.ApiV1TrackerConversionsIdStatePutRequest() # ApiV1TrackerConversionsIdStatePutRequest | 

    try:
        # Approve or reject one conversion.
        api_response = api_instance.api_v1_tracker_conversions_id_state_put(id, api_v1_tracker_conversions_id_state_put_request)
        print("The response of TrackerConversionsApi->api_v1_tracker_conversions_id_state_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversions_id_state_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Conversion ID. | 
 **api_v1_tracker_conversions_id_state_put_request** | [**ApiV1TrackerConversionsIdStatePutRequest**](ApiV1TrackerConversionsIdStatePutRequest.md)|  | 

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

# **api_v1_tracker_conversions_rejected_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_conversions_rejected_get()

List refused inbound postbacks.

The other half of the inbound stream: postbacks that never became a
conversion, with the reason each was refused. The first place to look when
a partner insists they fired one.


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
    api_instance = goadserver.TrackerConversionsApi(api_client)

    try:
        # List refused inbound postbacks.
        api_response = api_instance.api_v1_tracker_conversions_rejected_get()
        print("The response of TrackerConversionsApi->api_v1_tracker_conversions_rejected_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerConversionsApi->api_v1_tracker_conversions_rejected_get: %s\n" % e)
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


# goadserver.TrackerNetworksApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_ad_networks_delete_reports_put**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_delete_reports_put) | **PUT** /api/v1/tracker/ad-networks/delete-reports | Delete pulled spend reports.
[**api_v1_tracker_ad_networks_get**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_get) | **GET** /api/v1/tracker/ad-networks | List ad networks.
[**api_v1_tracker_ad_networks_id_campaigns_get**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_campaigns_get) | **GET** /api/v1/tracker/ad-networks/{id}/campaigns | Campaigns known on one ad network.
[**api_v1_tracker_ad_networks_id_delete**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_delete) | **DELETE** /api/v1/tracker/ad-networks/{id} | Delete an ad network.
[**api_v1_tracker_ad_networks_id_get**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_get) | **GET** /api/v1/tracker/ad-networks/{id} | Get one ad network.
[**api_v1_tracker_ad_networks_id_put**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_id_put) | **PUT** /api/v1/tracker/ad-networks/{id} | Update an ad network.
[**api_v1_tracker_ad_networks_post**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_post) | **POST** /api/v1/tracker/ad-networks | Create an ad network.
[**api_v1_tracker_ad_networks_reports_get**](TrackerNetworksApi.md#api_v1_tracker_ad_networks_reports_get) | **GET** /api/v1/tracker/ad-networks/reports | Spend reports pulled from the ad networks.
[**api_v1_tracker_affiliate_network_templates_get**](TrackerNetworksApi.md#api_v1_tracker_affiliate_network_templates_get) | **GET** /api/v1/tracker/affiliate-network-templates | List affiliate-network templates.
[**api_v1_tracker_affiliate_networks_get**](TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_get) | **GET** /api/v1/tracker/affiliate-networks | List affiliate networks.
[**api_v1_tracker_affiliate_networks_id_delete**](TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_id_delete) | **DELETE** /api/v1/tracker/affiliate-networks/{id} | Delete an affiliate network.
[**api_v1_tracker_affiliate_networks_id_put**](TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_id_put) | **PUT** /api/v1/tracker/affiliate-networks/{id} | Update an affiliate network.
[**api_v1_tracker_affiliate_networks_post**](TrackerNetworksApi.md#api_v1_tracker_affiliate_networks_post) | **POST** /api/v1/tracker/affiliate-networks | Create an affiliate network.


# **api_v1_tracker_ad_networks_delete_reports_put**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_ad_networks_delete_reports_put(api_v1_tracker_ad_networks_delete_reports_put_request)

Delete pulled spend reports.

Clears imported spend rows so a re-pull can replace them — the fix for a
driver that imported a bad day.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_id_delete200_response import ApiV1PublisherPushCampaignsIdDelete200Response
from goadserver.models.api_v1_tracker_ad_networks_delete_reports_put_request import ApiV1TrackerAdNetworksDeleteReportsPutRequest
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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    api_v1_tracker_ad_networks_delete_reports_put_request = goadserver.ApiV1TrackerAdNetworksDeleteReportsPutRequest() # ApiV1TrackerAdNetworksDeleteReportsPutRequest | 

    try:
        # Delete pulled spend reports.
        api_response = api_instance.api_v1_tracker_ad_networks_delete_reports_put(api_v1_tracker_ad_networks_delete_reports_put_request)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_delete_reports_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_delete_reports_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_ad_networks_delete_reports_put_request** | [**ApiV1TrackerAdNetworksDeleteReportsPutRequest**](ApiV1TrackerAdNetworksDeleteReportsPutRequest.md)|  | 

### Return type

[**ApiV1PublisherPushCampaignsIdDelete200Response**](ApiV1PublisherPushCampaignsIdDelete200Response.md)

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

# **api_v1_tracker_ad_networks_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_ad_networks_get(status=status, filter_id=filter_id, filter_name=filter_name, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)

List ad networks.

The buying side — traffic sources spend is pulled from and campaigns are
bound to.


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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    status = 'status_example' # str |  (optional)
    filter_id = 56 # int |  (optional)
    filter_name = 'filter_name_example' # str | Name contains. (optional)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List ad networks.
        api_response = api_instance.api_v1_tracker_ad_networks_get(status=status, filter_id=filter_id, filter_name=filter_name, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_name** | **str**| Name contains. | [optional] 
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

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

# **api_v1_tracker_ad_networks_id_campaigns_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_ad_networks_id_campaigns_get(id)

Campaigns known on one ad network.

The bindable campaigns for tracking links on this network.


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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Ad network ID.

    try:
        # Campaigns known on one ad network.
        api_response = api_instance.api_v1_tracker_ad_networks_id_campaigns_get(id)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_id_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_id_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ad network ID. | 

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

# **api_v1_tracker_ad_networks_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_ad_networks_id_delete(id)

Delete an ad network.

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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Ad network ID.

    try:
        # Delete an ad network.
        api_response = api_instance.api_v1_tracker_ad_networks_id_delete(id)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ad network ID. | 

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

# **api_v1_tracker_ad_networks_id_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_ad_networks_id_get(id)

Get one ad network.

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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Ad network ID.

    try:
        # Get one ad network.
        api_response = api_instance.api_v1_tracker_ad_networks_id_get(id)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ad network ID. | 

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

# **api_v1_tracker_ad_networks_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_ad_networks_id_put(id, api_v1_tracker_ad_networks_id_put_request)

Update an ad network.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_ad_networks_id_put_request import ApiV1TrackerAdNetworksIdPutRequest
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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Ad network ID.
    api_v1_tracker_ad_networks_id_put_request = goadserver.ApiV1TrackerAdNetworksIdPutRequest() # ApiV1TrackerAdNetworksIdPutRequest | 

    try:
        # Update an ad network.
        api_response = api_instance.api_v1_tracker_ad_networks_id_put(id, api_v1_tracker_ad_networks_id_put_request)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ad network ID. | 
 **api_v1_tracker_ad_networks_id_put_request** | [**ApiV1TrackerAdNetworksIdPutRequest**](ApiV1TrackerAdNetworksIdPutRequest.md)|  | 

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

# **api_v1_tracker_ad_networks_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_ad_networks_post(api_v1_tracker_ad_networks_post_request)

Create an ad network.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_ad_networks_post_request import ApiV1TrackerAdNetworksPostRequest
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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    api_v1_tracker_ad_networks_post_request = goadserver.ApiV1TrackerAdNetworksPostRequest() # ApiV1TrackerAdNetworksPostRequest | 

    try:
        # Create an ad network.
        api_response = api_instance.api_v1_tracker_ad_networks_post(api_v1_tracker_ad_networks_post_request)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_ad_networks_post_request** | [**ApiV1TrackerAdNetworksPostRequest**](ApiV1TrackerAdNetworksPostRequest.md)|  | 

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

# **api_v1_tracker_ad_networks_reports_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_ad_networks_reports_get(filter_id=filter_id, filter_ad_networkid=filter_ad_networkid, filter_state=filter_state, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)

Spend reports pulled from the ad networks.

What the cost pull has imported per network, the raw material behind
/cost-summary.


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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    filter_id = 56 # int |  (optional)
    filter_ad_networkid = 56 # int | Reports for one ad network. (optional)
    filter_state = 56 # int |  (optional)
    sort_by = r.id # str |  (optional) (default to r.id)
    sort_dir = desc # str |  (optional) (default to desc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # Spend reports pulled from the ad networks.
        api_response = api_instance.api_v1_tracker_ad_networks_reports_get(filter_id=filter_id, filter_ad_networkid=filter_ad_networkid, filter_state=filter_state, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)
        print("The response of TrackerNetworksApi->api_v1_tracker_ad_networks_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_ad_networks_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  | [optional] 
 **filter_ad_networkid** | **int**| Reports for one ad network. | [optional] 
 **filter_state** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to r.id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

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

# **api_v1_tracker_affiliate_network_templates_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_affiliate_network_templates_get()

List affiliate-network templates.

Known networks with their postback token mapping preset.


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
    api_instance = goadserver.TrackerNetworksApi(api_client)

    try:
        # List affiliate-network templates.
        api_response = api_instance.api_v1_tracker_affiliate_network_templates_get()
        print("The response of TrackerNetworksApi->api_v1_tracker_affiliate_network_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_affiliate_network_templates_get: %s\n" % e)
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

# **api_v1_tracker_affiliate_networks_get**
> ApiV1TrackerAffiliateNetworksGet200Response api_v1_tracker_affiliate_networks_get()

List affiliate networks.

Where offers come from, with their postback token mapping.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_affiliate_networks_get200_response import ApiV1TrackerAffiliateNetworksGet200Response
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
    api_instance = goadserver.TrackerNetworksApi(api_client)

    try:
        # List affiliate networks.
        api_response = api_instance.api_v1_tracker_affiliate_networks_get()
        print("The response of TrackerNetworksApi->api_v1_tracker_affiliate_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_affiliate_networks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerAffiliateNetworksGet200Response**](ApiV1TrackerAffiliateNetworksGet200Response.md)

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

# **api_v1_tracker_affiliate_networks_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_affiliate_networks_id_delete(id)

Delete an affiliate network.

Hard delete — the table carries no soft-delete flag. Offers pointing at it
keep their `affiliate_network_id` and simply resolve to no name.


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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Affiliate network ID.

    try:
        # Delete an affiliate network.
        api_response = api_instance.api_v1_tracker_affiliate_networks_id_delete(id)
        print("The response of TrackerNetworksApi->api_v1_tracker_affiliate_networks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_affiliate_networks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Affiliate network ID. | 

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

# **api_v1_tracker_affiliate_networks_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_affiliate_networks_id_put(id, api_v1_tracker_affiliate_networks_id_put_request)

Update an affiliate network.

Partial update.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_affiliate_networks_id_put_request import ApiV1TrackerAffiliateNetworksIdPutRequest
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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    id = 56 # int | Affiliate network ID.
    api_v1_tracker_affiliate_networks_id_put_request = goadserver.ApiV1TrackerAffiliateNetworksIdPutRequest() # ApiV1TrackerAffiliateNetworksIdPutRequest | 

    try:
        # Update an affiliate network.
        api_response = api_instance.api_v1_tracker_affiliate_networks_id_put(id, api_v1_tracker_affiliate_networks_id_put_request)
        print("The response of TrackerNetworksApi->api_v1_tracker_affiliate_networks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_affiliate_networks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Affiliate network ID. | 
 **api_v1_tracker_affiliate_networks_id_put_request** | [**ApiV1TrackerAffiliateNetworksIdPutRequest**](ApiV1TrackerAffiliateNetworksIdPutRequest.md)|  | 

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

# **api_v1_tracker_affiliate_networks_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_affiliate_networks_post(api_v1_tracker_affiliate_networks_post_request)

Create an affiliate network.

`template_slug` preloads a known network's token mapping — see
/affiliate-network-templates.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_affiliate_networks_post_request import ApiV1TrackerAffiliateNetworksPostRequest
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
    api_instance = goadserver.TrackerNetworksApi(api_client)
    api_v1_tracker_affiliate_networks_post_request = goadserver.ApiV1TrackerAffiliateNetworksPostRequest() # ApiV1TrackerAffiliateNetworksPostRequest | 

    try:
        # Create an affiliate network.
        api_response = api_instance.api_v1_tracker_affiliate_networks_post(api_v1_tracker_affiliate_networks_post_request)
        print("The response of TrackerNetworksApi->api_v1_tracker_affiliate_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerNetworksApi->api_v1_tracker_affiliate_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_affiliate_networks_post_request** | [**ApiV1TrackerAffiliateNetworksPostRequest**](ApiV1TrackerAffiliateNetworksPostRequest.md)|  | 

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


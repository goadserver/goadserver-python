# goadserver.TrackerAutomationApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tracker_export_type_get**](TrackerAutomationApi.md#api_v1_tracker_export_type_get) | **GET** /api/v1/tracker/export/{type} | Export tracker entities as CSV.
[**api_v1_tracker_import_type_post**](TrackerAutomationApi.md#api_v1_tracker_import_type_post) | **POST** /api/v1/tracker/import/{type} | Bulk-import offers from CSV.
[**api_v1_tracker_report_schedules_get**](TrackerAutomationApi.md#api_v1_tracker_report_schedules_get) | **GET** /api/v1/tracker/report-schedules | List scheduled report deliveries.
[**api_v1_tracker_report_schedules_id_delete**](TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_delete) | **DELETE** /api/v1/tracker/report-schedules/{id} | Delete a report schedule.
[**api_v1_tracker_report_schedules_id_get**](TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_get) | **GET** /api/v1/tracker/report-schedules/{id} | Get one report schedule.
[**api_v1_tracker_report_schedules_id_put**](TrackerAutomationApi.md#api_v1_tracker_report_schedules_id_put) | **PUT** /api/v1/tracker/report-schedules/{id} | Update a report schedule.
[**api_v1_tracker_report_schedules_post**](TrackerAutomationApi.md#api_v1_tracker_report_schedules_post) | **POST** /api/v1/tracker/report-schedules | Schedule a recurring report.
[**api_v1_tracker_rules_get**](TrackerAutomationApi.md#api_v1_tracker_rules_get) | **GET** /api/v1/tracker/rules | List automation rules.
[**api_v1_tracker_rules_id_delete**](TrackerAutomationApi.md#api_v1_tracker_rules_id_delete) | **DELETE** /api/v1/tracker/rules/{id} | Delete a rule.
[**api_v1_tracker_rules_id_executions_get**](TrackerAutomationApi.md#api_v1_tracker_rules_id_executions_get) | **GET** /api/v1/tracker/rules/{id}/executions | Execution history for one rule.
[**api_v1_tracker_rules_id_get**](TrackerAutomationApi.md#api_v1_tracker_rules_id_get) | **GET** /api/v1/tracker/rules/{id} | Get one rule.
[**api_v1_tracker_rules_id_put**](TrackerAutomationApi.md#api_v1_tracker_rules_id_put) | **PUT** /api/v1/tracker/rules/{id} | Update a rule.
[**api_v1_tracker_rules_id_run_post**](TrackerAutomationApi.md#api_v1_tracker_rules_id_run_post) | **POST** /api/v1/tracker/rules/{id}/run | Run a rule now.
[**api_v1_tracker_rules_post**](TrackerAutomationApi.md#api_v1_tracker_rules_post) | **POST** /api/v1/tracker/rules | Create an automation rule.


# **api_v1_tracker_export_type_get**
> str api_v1_tracker_export_type_get(type)

Export tracker entities as CSV.

Returns `text/csv`, not JSON — the same file the scheduled reports mail.
Scoped `tracker.read` rather than `stats.read`: this dumps configuration,
not statistics.


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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    type = 'type_example' # str | What to export.

    try:
        # Export tracker entities as CSV.
        api_response = api_instance.api_v1_tracker_export_type_get(type)
        print("The response of TrackerAutomationApi->api_v1_tracker_export_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_export_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| What to export. | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_import_type_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_import_type_post(type, file, commit=commit, overwrite=overwrite)

Bulk-import offers from CSV.

`multipart/form-data` with the CSV as `file`. Two flags decide how far it
goes: without `commit` the upload is validated and reported on but nothing
is written, and without `overwrite` every row inserts and any `id` column
is ignored, so a spreadsheet cannot clobber live rows by accident. An id
that resolves to no row the caller owns is a row error, never a silent
insert.


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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    type = 'type_example' # str | What to import.
    file = None # bytes | The CSV, at most 10 MiB.
    commit = 'commit_example' # str | \\\"true\\\" to write. Absent = validate and report only. (optional)
    overwrite = 'overwrite_example' # str | \\\"true\\\" to update rows whose id column matches one of the caller's own. (optional)

    try:
        # Bulk-import offers from CSV.
        api_response = api_instance.api_v1_tracker_import_type_post(type, file, commit=commit, overwrite=overwrite)
        print("The response of TrackerAutomationApi->api_v1_tracker_import_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_import_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| What to import. | 
 **file** | **bytes**| The CSV, at most 10 MiB. | 
 **commit** | **str**| \\\&quot;true\\\&quot; to write. Absent &#x3D; validate and report only. | [optional] 
 **overwrite** | **str**| \\\&quot;true\\\&quot; to update rows whose id column matches one of the caller&#39;s own. | [optional] 

### Return type

[**ApiV1TrackerTrackingLinksIdZoneCostsGet200Response**](ApiV1TrackerTrackingLinksIdZoneCostsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad_upload, or the CSV header does not match. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_report_schedules_get**
> ApiV1TrackerReportSchedulesGet200Response api_v1_tracker_report_schedules_get()

List scheduled report deliveries.

Recurring CSV exports mailed to a list of recipients.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_report_schedules_get200_response import ApiV1TrackerReportSchedulesGet200Response
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
    api_instance = goadserver.TrackerAutomationApi(api_client)

    try:
        # List scheduled report deliveries.
        api_response = api_instance.api_v1_tracker_report_schedules_get()
        print("The response of TrackerAutomationApi->api_v1_tracker_report_schedules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_report_schedules_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerReportSchedulesGet200Response**](ApiV1TrackerReportSchedulesGet200Response.md)

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

# **api_v1_tracker_report_schedules_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_report_schedules_id_delete(id)

Delete a report schedule.

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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Schedule ID.

    try:
        # Delete a report schedule.
        api_response = api_instance.api_v1_tracker_report_schedules_id_delete(id)
        print("The response of TrackerAutomationApi->api_v1_tracker_report_schedules_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_report_schedules_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Schedule ID. | 

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

# **api_v1_tracker_report_schedules_id_get**
> ApiV1TrackerReportSchedulesIdGet200Response api_v1_tracker_report_schedules_id_get(id)

Get one report schedule.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_report_schedules_id_get200_response import ApiV1TrackerReportSchedulesIdGet200Response
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Schedule ID.

    try:
        # Get one report schedule.
        api_response = api_instance.api_v1_tracker_report_schedules_id_get(id)
        print("The response of TrackerAutomationApi->api_v1_tracker_report_schedules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_report_schedules_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Schedule ID. | 

### Return type

[**ApiV1TrackerReportSchedulesIdGet200Response**](ApiV1TrackerReportSchedulesIdGet200Response.md)

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

# **api_v1_tracker_report_schedules_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_report_schedules_id_put(id, api_v1_tracker_report_schedules_id_put_request)

Update a report schedule.

Partial update.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_report_schedules_id_put_request import ApiV1TrackerReportSchedulesIdPutRequest
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Schedule ID.
    api_v1_tracker_report_schedules_id_put_request = goadserver.ApiV1TrackerReportSchedulesIdPutRequest() # ApiV1TrackerReportSchedulesIdPutRequest | 

    try:
        # Update a report schedule.
        api_response = api_instance.api_v1_tracker_report_schedules_id_put(id, api_v1_tracker_report_schedules_id_put_request)
        print("The response of TrackerAutomationApi->api_v1_tracker_report_schedules_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_report_schedules_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Schedule ID. | 
 **api_v1_tracker_report_schedules_id_put_request** | [**ApiV1TrackerReportSchedulesIdPutRequest**](ApiV1TrackerReportSchedulesIdPutRequest.md)|  | 

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

# **api_v1_tracker_report_schedules_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_report_schedules_post(api_v1_tracker_report_schedules_post_request)

Schedule a recurring report.

`report_type` names the same three exports `/export/{type}` serves.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_report_schedules_post_request import ApiV1TrackerReportSchedulesPostRequest
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    api_v1_tracker_report_schedules_post_request = goadserver.ApiV1TrackerReportSchedulesPostRequest() # ApiV1TrackerReportSchedulesPostRequest | 

    try:
        # Schedule a recurring report.
        api_response = api_instance.api_v1_tracker_report_schedules_post(api_v1_tracker_report_schedules_post_request)
        print("The response of TrackerAutomationApi->api_v1_tracker_report_schedules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_report_schedules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_report_schedules_post_request** | [**ApiV1TrackerReportSchedulesPostRequest**](ApiV1TrackerReportSchedulesPostRequest.md)|  | 

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

# **api_v1_tracker_rules_get**
> ApiV1TrackerRulesGet200Response api_v1_tracker_rules_get()

List automation rules.

Standing rules that watch performance and act — pause an offer, block a
placement, adjust a bid, or raise an alert.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_rules_get200_response import ApiV1TrackerRulesGet200Response
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
    api_instance = goadserver.TrackerAutomationApi(api_client)

    try:
        # List automation rules.
        api_response = api_instance.api_v1_tracker_rules_get()
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1TrackerRulesGet200Response**](ApiV1TrackerRulesGet200Response.md)

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

# **api_v1_tracker_rules_id_delete**
> ApiV1PublisherPushCampaignsIdDelete200Response api_v1_tracker_rules_id_delete(id)

Delete a rule.

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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Rule ID.

    try:
        # Delete a rule.
        api_response = api_instance.api_v1_tracker_rules_id_delete(id)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 

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

# **api_v1_tracker_rules_id_executions_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_rules_id_executions_get(id)

Execution history for one rule.

Every firing, what matched, and what the rule did — including the runs it
only reported because `apply_actions` was off.


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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Rule ID.

    try:
        # Execution history for one rule.
        api_response = api_instance.api_v1_tracker_rules_id_executions_get(id)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_id_executions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_id_executions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 

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

# **api_v1_tracker_rules_id_get**
> ApiV1TrackerRulesIdGet200Response api_v1_tracker_rules_id_get(id)

Get one rule.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_rules_id_get200_response import ApiV1TrackerRulesIdGet200Response
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Rule ID.

    try:
        # Get one rule.
        api_response = api_instance.api_v1_tracker_rules_id_get(id)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 

### Return type

[**ApiV1TrackerRulesIdGet200Response**](ApiV1TrackerRulesIdGet200Response.md)

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

# **api_v1_tracker_rules_id_put**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_rules_id_put(id, api_v1_tracker_rules_id_put_request)

Update a rule.

Partial update.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_rules_id_put_request import ApiV1TrackerRulesIdPutRequest
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Rule ID.
    api_v1_tracker_rules_id_put_request = goadserver.ApiV1TrackerRulesIdPutRequest() # ApiV1TrackerRulesIdPutRequest | 

    try:
        # Update a rule.
        api_response = api_instance.api_v1_tracker_rules_id_put(id, api_v1_tracker_rules_id_put_request)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 
 **api_v1_tracker_rules_id_put_request** | [**ApiV1TrackerRulesIdPutRequest**](ApiV1TrackerRulesIdPutRequest.md)|  | 

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

# **api_v1_tracker_rules_id_run_post**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_tracker_rules_id_run_post(id, window=window)

Run a rule now.

Evaluates immediately instead of waiting for the schedule. Honours the
rule's own `apply_actions`, so a reporting-only rule stays harmless.


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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    id = 56 # int | Rule ID.
    window = 'window_example' # str | Override the evaluation window for this run. (optional)

    try:
        # Run a rule now.
        api_response = api_instance.api_v1_tracker_rules_id_run_post(id, window=window)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_id_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rule ID. | 
 **window** | **str**| Override the evaluation window for this run. | [optional] 

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

# **api_v1_tracker_rules_post**
> ApiV1PublisherPushCampaignsPost200Response api_v1_tracker_rules_post(api_v1_tracker_rules_post_request)

Create an automation rule.

`conditions` is the list the evaluator ANDs; `action` is what fires when
they all hold. With `apply_actions` false the rule reports what it would
have done without touching anything — the way to trust one before arming it.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_push_campaigns_post200_response import ApiV1PublisherPushCampaignsPost200Response
from goadserver.models.api_v1_tracker_rules_post_request import ApiV1TrackerRulesPostRequest
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
    api_instance = goadserver.TrackerAutomationApi(api_client)
    api_v1_tracker_rules_post_request = goadserver.ApiV1TrackerRulesPostRequest() # ApiV1TrackerRulesPostRequest | 

    try:
        # Create an automation rule.
        api_response = api_instance.api_v1_tracker_rules_post(api_v1_tracker_rules_post_request)
        print("The response of TrackerAutomationApi->api_v1_tracker_rules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerAutomationApi->api_v1_tracker_rules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_tracker_rules_post_request** | [**ApiV1TrackerRulesPostRequest**](ApiV1TrackerRulesPostRequest.md)|  | 

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


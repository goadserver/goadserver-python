# goadserver.AccountBillingApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_account_billing_affiliated_payments_get**](AccountBillingApi.md#api_v1_account_billing_affiliated_payments_get) | **GET** /api/v1/account/billing/affiliated-payments | Payments made to affiliated accounts.
[**api_v1_account_billing_averages_get**](AccountBillingApi.md#api_v1_account_billing_averages_get) | **GET** /api/v1/account/billing/averages | Average costs and overcharges.
[**api_v1_account_billing_invoices_get**](AccountBillingApi.md#api_v1_account_billing_invoices_get) | **GET** /api/v1/account/billing/invoices | List invoices.
[**api_v1_account_billing_invoices_id_pdf_get**](AccountBillingApi.md#api_v1_account_billing_invoices_id_pdf_get) | **GET** /api/v1/account/billing/invoices/{id}/pdf | Download an invoice PDF.
[**api_v1_account_billing_settings_get**](AccountBillingApi.md#api_v1_account_billing_settings_get) | **GET** /api/v1/account/billing/settings | The account&#39;s billing plan.


# **api_v1_account_billing_affiliated_payments_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_billing_affiliated_payments_get()

Payments made to affiliated accounts.

Payouts recorded against accounts affiliated with this one.


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
    api_instance = goadserver.AccountBillingApi(api_client)

    try:
        # Payments made to affiliated accounts.
        api_response = api_instance.api_v1_account_billing_affiliated_payments_get()
        print("The response of AccountBillingApi->api_v1_account_billing_affiliated_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBillingApi->api_v1_account_billing_affiliated_payments_get: %s\n" % e)
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

# **api_v1_account_billing_averages_get**
> ApiV1AccountBillingAveragesGet200Response api_v1_account_billing_averages_get()

Average costs and overcharges.

This month's usage projected to month end and priced with the
account's billing plan (the tenant default fills any rate the plan
leaves out) — the same pricing the monthly invoice uses. Not wrapped
in `data`. With no active plan every field is zero / empty.

`modules` lists the charges of the plan's add-on modules (CRM,
Agentic Media Buying), already included in `costs`. Media buying is
a percentage of the managed network spend of your ad zones with
Agentic Media Buying switched on, with a monthly minimum in a month
that has managed spend.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_billing_averages_get200_response import ApiV1AccountBillingAveragesGet200Response
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
    api_instance = goadserver.AccountBillingApi(api_client)

    try:
        # Average costs and overcharges.
        api_response = api_instance.api_v1_account_billing_averages_get()
        print("The response of AccountBillingApi->api_v1_account_billing_averages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBillingApi->api_v1_account_billing_averages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1AccountBillingAveragesGet200Response**](ApiV1AccountBillingAveragesGet200Response.md)

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

# **api_v1_account_billing_invoices_get**
> ApiV1AccountBillingInvoicesGet200Response api_v1_account_billing_invoices_get()

List invoices.

Every invoice raised against the account, paid or not, newest first,
unpaginated, under `results` (not `data`). `money`,
`bandwidth_costs` and `pro_adearned` are **cents** (unlike
GET /api/v1/funds, which reports currency units). `paystatus_string`
is Open / Processing / Paid / Prevalidated. A database error answers
200 with an empty list.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_account_billing_invoices_get200_response import ApiV1AccountBillingInvoicesGet200Response
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
    api_instance = goadserver.AccountBillingApi(api_client)

    try:
        # List invoices.
        api_response = api_instance.api_v1_account_billing_invoices_get()
        print("The response of AccountBillingApi->api_v1_account_billing_invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBillingApi->api_v1_account_billing_invoices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1AccountBillingInvoicesGet200Response**](ApiV1AccountBillingInvoicesGet200Response.md)

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

# **api_v1_account_billing_invoices_id_pdf_get**
> bytes api_v1_account_billing_invoices_id_pdf_get(id)

Download an invoice PDF.

Returns `application/pdf`, not JSON. 404 for an invoice that is not the
caller's.


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
    api_instance = goadserver.AccountBillingApi(api_client)
    id = 56 # int | Invoice ID.

    try:
        # Download an invoice PDF.
        api_response = api_instance.api_v1_account_billing_invoices_id_pdf_get(id)
        print("The response of AccountBillingApi->api_v1_account_billing_invoices_id_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBillingApi->api_v1_account_billing_invoices_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID. | 

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  -  |
**404** | Invoice not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_account_billing_settings_get**
> ApiV1TrackerTrackingLinksIdZoneCostsGet200Response api_v1_account_billing_settings_get()

The account's billing plan.

The plan the account is on, its fixed costs and currency, and whether this
membership may manage billing at all.


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
    api_instance = goadserver.AccountBillingApi(api_client)

    try:
        # The account's billing plan.
        api_response = api_instance.api_v1_account_billing_settings_get()
        print("The response of AccountBillingApi->api_v1_account_billing_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBillingApi->api_v1_account_billing_settings_get: %s\n" % e)
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


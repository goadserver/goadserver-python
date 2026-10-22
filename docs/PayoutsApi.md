# goadserver.PayoutsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_publisher_finance_earnings_get**](PayoutsApi.md#api_v1_publisher_finance_earnings_get) | **GET** /api/v1/publisher/finance/earnings | Earnings per day, week or month.
[**api_v1_publisher_finance_get**](PayoutsApi.md#api_v1_publisher_finance_get) | **GET** /api/v1/publisher/finance | Publisher balance and payout rules.
[**api_v1_publisher_finance_month_earnings_get**](PayoutsApi.md#api_v1_publisher_finance_month_earnings_get) | **GET** /api/v1/publisher/finance/month-earnings | Monthly earnings statements.
[**api_v1_publisher_finance_payout_request_post**](PayoutsApi.md#api_v1_publisher_finance_payout_request_post) | **POST** /api/v1/publisher/finance/payout-request | Request a payout of the balance.
[**api_v1_publisher_finance_payout_types_get**](PayoutsApi.md#api_v1_publisher_finance_payout_types_get) | **GET** /api/v1/publisher/finance/payout-types | Payout methods this account may choose.
[**api_v1_publisher_finance_payouts_get**](PayoutsApi.md#api_v1_publisher_finance_payouts_get) | **GET** /api/v1/publisher/finance/payouts | List payout requests and payouts.
[**api_v1_publisher_finance_settings_get**](PayoutsApi.md#api_v1_publisher_finance_settings_get) | **GET** /api/v1/publisher/finance/settings | Payout method and payment details.
[**api_v1_publisher_finance_settings_put**](PayoutsApi.md#api_v1_publisher_finance_settings_put) | **PUT** /api/v1/publisher/finance/settings | Change the payout method or payment details.
[**api_v1_publisher_finance_transactions_get**](PayoutsApi.md#api_v1_publisher_finance_transactions_get) | **GET** /api/v1/publisher/finance/transactions | List payout transactions (with USD totals).
[**api_v1_publisher_finance_transactions_id_get**](PayoutsApi.md#api_v1_publisher_finance_transactions_id_get) | **GET** /api/v1/publisher/finance/transactions/{id} | One payout transaction.
[**api_v1_publisher_finance_transactions_id_invoice_pdf_get**](PayoutsApi.md#api_v1_publisher_finance_transactions_id_invoice_pdf_get) | **GET** /api/v1/publisher/finance/transactions/{id}/invoice-pdf | Download the self-billing invoice PDF of a paid payout.
[**api_v1_publisher_finance_transfer_to_advertiser_post**](PayoutsApi.md#api_v1_publisher_finance_transfer_to_advertiser_post) | **POST** /api/v1/publisher/finance/transfer-to-advertiser | Move publisher balance to the advertiser budget.


# **api_v1_publisher_finance_earnings_get**
> ApiV1PublisherFinanceEarningsGet200Response api_v1_publisher_finance_earnings_get(var_from=var_from, to=to, group_by=group_by)

Earnings per day, week or month.

Publisher earnings from the stats store, bucketed by `group_by`.

**Money units.** `amount` and `summary.total` are **whole currency
units** rounded to 2 decimals (unlike the balance fields, which are
cents). Recent hours may still be incomplete.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_earnings_get200_response import ApiV1PublisherFinanceEarningsGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)
    var_from = '2013-10-20' # date | Inclusive start (YYYY-MM-DD). Both `from` and `to` must be given, else the last 30 days are used. (optional)
    to = '2013-10-20' # date | Inclusive end (YYYY-MM-DD). (optional)
    group_by = day # str | `week` buckets are labelled `YYYY-WW` (ISO week), `month` buckets `YYYY-MM`. (optional) (default to day)

    try:
        # Earnings per day, week or month.
        api_response = api_instance.api_v1_publisher_finance_earnings_get(var_from=var_from, to=to, group_by=group_by)
        print("The response of PayoutsApi->api_v1_publisher_finance_earnings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_earnings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Inclusive start (YYYY-MM-DD). Both &#x60;from&#x60; and &#x60;to&#x60; must be given, else the last 30 days are used. | [optional] 
 **to** | **date**| Inclusive end (YYYY-MM-DD). | [optional] 
 **group_by** | **str**| &#x60;week&#x60; buckets are labelled &#x60;YYYY-WW&#x60; (ISO week), &#x60;month&#x60; buckets &#x60;YYYY-MM&#x60;. | [optional] [default to day]

### Return type

[**ApiV1PublisherFinanceEarningsGet200Response**](ApiV1PublisherFinanceEarningsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Earnings series. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_get**
> ApiV1PublisherFinanceGet200Response api_v1_publisher_finance_get()

Publisher balance and payout rules.

The publisher's current balance, the sum of open payout requests, the
total already paid out, and the network's payout rules — the header of
the panel's Billing page.

**Money units.** `balance.current`, `balance.pending` and
`balance.total_earned` are **cents** of the network's main currency.
`payout_threshold` is **whole currency units** (50 = 50.00).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_get200_response import ApiV1PublisherFinanceGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)

    try:
        # Publisher balance and payout rules.
        api_response = api_instance.api_v1_publisher_finance_get()
        print("The response of PayoutsApi->api_v1_publisher_finance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherFinanceGet200Response**](ApiV1PublisherFinanceGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance overview. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_month_earnings_get**
> List[ApiV1PublisherFinanceMonthEarningsGet200ResponseInner] api_v1_publisher_finance_month_earnings_get()

Monthly earnings statements.

One row per month from the monthly earnings ledger (the panel's
Earnings tab), newest first. Not paginated.

**Money units.** `earned`, `pro_earned`, `ad_earned` and
`total_earned` are **cents**.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_month_earnings_get200_response_inner import ApiV1PublisherFinanceMonthEarningsGet200ResponseInner
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
    api_instance = goadserver.PayoutsApi(api_client)

    try:
        # Monthly earnings statements.
        api_response = api_instance.api_v1_publisher_finance_month_earnings_get()
        print("The response of PayoutsApi->api_v1_publisher_finance_month_earnings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_month_earnings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiV1PublisherFinanceMonthEarningsGet200ResponseInner]**](ApiV1PublisherFinanceMonthEarningsGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monthly rows. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**500** | &#x60;query_failed&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_payout_request_post**
> ApiV1PublisherFinancePayoutRequestPost201Response api_v1_publisher_finance_payout_request_post(api_v1_publisher_finance_payout_request_post_request=api_v1_publisher_finance_payout_request_post_request)

Request a payout of the balance.

Creates a payout request (paid out by staff, by the method in the
payout settings) and deducts the amount from the balance at once.

**Money units.** The request `amount` is **whole currency units**
(`12.50`); every amount in the response is **cents**.

Rules (same as the panel):

- `total_amount: true` requests the whole balance; otherwise `amount`
  is required and is capped to the balance.
- The balance must reach the network `payout_threshold`, and the
  requested amount must reach the larger of that threshold and the
  payout method's `min_payout`.
- Only one open request at a time.
- A fee is deducted when the method has one configured for amounts
  below its `fee_below`; `net_amount` is what is paid.
- Payouts go to the payment details on file. If those are not yet
  approved by staff (`isvalidbanking: 0` in the settings) the request
  is still recorded, and staff validate the details before paying.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_payout_request_post201_response import ApiV1PublisherFinancePayoutRequestPost201Response
from goadserver.models.api_v1_publisher_finance_payout_request_post_request import ApiV1PublisherFinancePayoutRequestPostRequest
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
    api_instance = goadserver.PayoutsApi(api_client)
    api_v1_publisher_finance_payout_request_post_request = {"total_amount":true} # ApiV1PublisherFinancePayoutRequestPostRequest |  (optional)

    try:
        # Request a payout of the balance.
        api_response = api_instance.api_v1_publisher_finance_payout_request_post(api_v1_publisher_finance_payout_request_post_request=api_v1_publisher_finance_payout_request_post_request)
        print("The response of PayoutsApi->api_v1_publisher_finance_payout_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_payout_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_finance_payout_request_post_request** | [**ApiV1PublisherFinancePayoutRequestPostRequest**](ApiV1PublisherFinancePayoutRequestPostRequest.md)|  | [optional] 

### Return type

[**ApiV1PublisherFinancePayoutRequestPost201Response**](ApiV1PublisherFinancePayoutRequestPost201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request created. |  -  |
**400** | &#x60;insufficient_balance&#x60; (balance below the payout threshold), &#x60;below_minimum&#x60; (amount below the threshold / method minimum), &#x60;invalid_amount&#x60; (missing, ≤ 0 or not a valid number), &#x60;pending_request_exists&#x60; (an open request already exists).  |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**409** | &#x60;balance_changed&#x60; — the balance moved while the request ran; nothing was deducted. Retry. |  -  |
**422** | &#x60;unknown_fields&#x60; — the body has keys other than amount, total_amount, description. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_payout_types_get**
> List[ApiV1PublisherFinancePayoutTypesGet200ResponseInner] api_v1_publisher_finance_payout_types_get()

Payout methods this account may choose.

The methods offered in the panel's payout-method picker — active on the
tenant, allowed by the account's rights. The advertiser-budget method
is not listed here (use `POST …/transfer-to-advertiser`). `id` is the
value for `payouttype` in `PUT /api/v1/publisher/finance/settings`;
any other id is refused there.

**Money units.** `min_payout` is **whole currency units**.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_payout_types_get200_response_inner import ApiV1PublisherFinancePayoutTypesGet200ResponseInner
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
    api_instance = goadserver.PayoutsApi(api_client)

    try:
        # Payout methods this account may choose.
        api_response = api_instance.api_v1_publisher_finance_payout_types_get()
        print("The response of PayoutsApi->api_v1_publisher_finance_payout_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_payout_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiV1PublisherFinancePayoutTypesGet200ResponseInner]**](ApiV1PublisherFinancePayoutTypesGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout methods. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_payouts_get**
> ApiV1PublisherFinancePayoutsGet200Response api_v1_publisher_finance_payouts_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_ispayed=filter_ispayed, filter_transacttype=filter_transacttype)

List payout requests and payouts.

Rows of `publisher_transactions` — every payout request (paid or not)
and every transfer to the advertiser budget. Paginated.

**Money units.** `money` is **cents** in the network's main currency;
`paid_currency` is the currency the payout is made in.

`transacttype` is the payout method id (see
`GET /api/v1/publisher/finance/payout-types`); `0` is a transfer to the
advertiser budget.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_payouts_get200_response import ApiV1PublisherFinancePayoutsGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    filter_id = 56 # int |  (optional)
    filter_ispayed = 56 # int |  (optional)
    filter_transacttype = 56 # int |  (optional)

    try:
        # List payout requests and payouts.
        api_response = api_instance.api_v1_publisher_finance_payouts_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_ispayed=filter_ispayed, filter_transacttype=filter_transacttype)
        print("The response of PayoutsApi->api_v1_publisher_finance_payouts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_payouts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **filter_id** | **int**|  | [optional] 
 **filter_ispayed** | **int**|  | [optional] 
 **filter_transacttype** | **int**|  | [optional] 

### Return type

[**ApiV1PublisherFinancePayoutsGet200Response**](ApiV1PublisherFinancePayoutsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of payouts. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_settings_get**
> ApiV1PublisherFinanceSettingsGet200Response api_v1_publisher_finance_settings_get()

Payout method and payment details.

The account's payout settings. When none were ever saved, the defaults
are returned with `payouttype: -1`.

**Money units.** `minimum_payout` is **whole currency units**.

Read-only here: `isvalidbanking` (staff approval of the payment
details — reset whenever the destination changes), `isvalidcompany`,
`last_time_validated`, `allowweeklypayments` (whether
`directpayout: 2` is permitted) and the invoice-address block
(`inv_*`, `useaccountadress`), which is edited through the account
settings, not here.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_settings_get200_response import ApiV1PublisherFinanceSettingsGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)

    try:
        # Payout method and payment details.
        api_response = api_instance.api_v1_publisher_finance_settings_get()
        print("The response of PayoutsApi->api_v1_publisher_finance_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1PublisherFinanceSettingsGet200Response**](ApiV1PublisherFinanceSettingsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_settings_put**
> ApiV1RetargetingPixelsIdDelete200Response api_v1_publisher_finance_settings_put(api_v1_publisher_finance_settings_put_request)

Change the payout method or payment details.

Partial update: send only the fields to change. Needs its own scope,
`payouts.method` — a key holding `payouts.write` (request a payout)
cannot redirect where the money goes.

Same rules as the panel's Billing → Payout settings save:

- `payouttype` must be one of `GET …/payout-types` (or ≤ 0).
- `minimum_payout` (**whole currency units**) may not be below the
  selected method's `min_payout`.
- `p_currency` must be `eur` or `usd`.
- `directpayout: 2` (weekly) silently becomes `0` without the
  `weekly_payout` right; values outside 0–2 become `0`.
- IBAN / BIC are stored uppercased, IBAN without separators. Strings
  longer than the column are truncated to its width.
- **Changing a destination** (`bankaccountnumber`, `ibancode`,
  `routingnumber`, `paypaladress`, `paxumadress`, `payoneeradress`,
  `paymentdata`) **resets `isvalidbanking` to 0**: the new details
  need staff approval again before payouts are made to them.

Neither the panel nor this endpoint asks for 2FA or an email
confirmation. Read-only fields of the GET (`isvalidbanking`,
`isvalidcompany`, `last_time_validated`, `allowweeklypayments`) and the
invoice-address block (`inv_*`, `useaccountadress` — edited via the
account settings) are not accepted: strip them before sending a GET
body back, or the call answers 422 `unknown_fields`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_settings_put_request import ApiV1PublisherFinanceSettingsPutRequest
from goadserver.models.api_v1_retargeting_pixels_id_delete200_response import ApiV1RetargetingPixelsIdDelete200Response
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
    api_instance = goadserver.PayoutsApi(api_client)
    api_v1_publisher_finance_settings_put_request = {"payouttype":1,"ibancode":"NL91 ABNA 0417 1643 00","biccode":"abnanl2a","bankaccountname":"Example Media BV","minimum_payout":100} # ApiV1PublisherFinanceSettingsPutRequest | 

    try:
        # Change the payout method or payment details.
        api_response = api_instance.api_v1_publisher_finance_settings_put(api_v1_publisher_finance_settings_put_request)
        print("The response of PayoutsApi->api_v1_publisher_finance_settings_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_finance_settings_put_request** | [**ApiV1PublisherFinanceSettingsPutRequest**](ApiV1PublisherFinanceSettingsPutRequest.md)|  | 

### Return type

[**ApiV1RetargetingPixelsIdDelete200Response**](ApiV1RetargetingPixelsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved. |  -  |
**400** | &#x60;no_fields&#x60; — nothing writable in the body; &#x60;bad_request&#x60; — body is not valid JSON. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**413** | &#x60;payload_too_large&#x60; — body over 32 KB. |  -  |
**422** | &#x60;validation_error&#x60; (&#x60;errors.payouttype&#x60; — method not offered to this account; &#x60;errors.minimum_payout&#x60; — below the method minimum or not a valid amount; &#x60;errors.p_currency&#x60;), or &#x60;unknown_fields&#x60; with the offending keys listed in &#x60;unknown_fields&#x60;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_transactions_get**
> ApiV1PublisherFinanceTransactionsGet200Response api_v1_publisher_finance_transactions_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_ispayed=filter_ispayed, filter_transacttype=filter_transacttype, filter_dateadded=filter_dateadded)

List payout transactions (with USD totals).

Same rows as `GET /api/v1/publisher/finance/payouts` with the field
names the panel's Transactions tab uses (`ispaid`, `datepaid`) plus the
USD conversion of paid rows.

**Money units.** `money` and `totalusd` are **cents**; `usdrate` is the
conversion rate applied.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_transactions_get200_response import ApiV1PublisherFinanceTransactionsGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)
    sort_by = id # str |  (optional) (default to id)
    sort_dir = desc # str |  (optional) (default to desc)
    filter_id = 56 # int |  (optional)
    filter_ispayed = 56 # int |  (optional)
    filter_transacttype = 56 # int |  (optional)
    filter_dateadded = '2013-10-20' # date |  (optional)

    try:
        # List payout transactions (with USD totals).
        api_response = api_instance.api_v1_publisher_finance_transactions_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, filter_id=filter_id, filter_ispayed=filter_ispayed, filter_transacttype=filter_transacttype, filter_dateadded=filter_dateadded)
        print("The response of PayoutsApi->api_v1_publisher_finance_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]
 **sort_by** | **str**|  | [optional] [default to id]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **filter_id** | **int**|  | [optional] 
 **filter_ispayed** | **int**|  | [optional] 
 **filter_transacttype** | **int**|  | [optional] 
 **filter_dateadded** | **date**|  | [optional] 

### Return type

[**ApiV1PublisherFinanceTransactionsGet200Response**](ApiV1PublisherFinanceTransactionsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of transactions. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_transactions_id_get**
> ApiV1PublisherFinanceTransactionsIdGet200Response api_v1_publisher_finance_transactions_id_get(id)

One payout transaction.

A single row of the caller's `publisher_transactions`. **`money` is
cents.** Another account's id answers 404.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_transactions_id_get200_response import ApiV1PublisherFinanceTransactionsIdGet200Response
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
    api_instance = goadserver.PayoutsApi(api_client)
    id = 56 # int | 

    try:
        # One payout transaction.
        api_response = api_instance.api_v1_publisher_finance_transactions_id_get(id)
        print("The response of PayoutsApi->api_v1_publisher_finance_transactions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_transactions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1PublisherFinanceTransactionsIdGet200Response**](ApiV1PublisherFinanceTransactionsIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Transaction not found (or the finance module is off — see ModuleDisabled). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_transactions_id_invoice_pdf_get**
> bytes api_v1_publisher_finance_transactions_id_invoice_pdf_get(id)

Download the self-billing invoice PDF of a paid payout.

Returns `application/pdf` as an attachment named after the invoice
number. Only **paid** payouts have an invoice; an unpaid or unknown id
answers 404.


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
    api_instance = goadserver.PayoutsApi(api_client)
    id = 56 # int | 

    try:
        # Download the self-billing invoice PDF of a paid payout.
        api_response = api_instance.api_v1_publisher_finance_transactions_id_invoice_pdf_get(id)
        print("The response of PayoutsApi->api_v1_publisher_finance_transactions_id_invoice_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_transactions_id_invoice_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The PDF. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Transaction not found or not yet paid. |  -  |
**500** | &#x60;pdf_error&#x60; — the PDF could not be generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_publisher_finance_transfer_to_advertiser_post**
> ApiV1PublisherFinanceTransferToAdvertiserPost200Response api_v1_publisher_finance_transfer_to_advertiser_post(api_v1_publisher_finance_transfer_to_advertiser_post_request)

Move publisher balance to the advertiser budget.

Moves money from the publisher balance to the same account's
advertiser budget, immediately (recorded as a paid transaction with
`transacttype: 0`). Only for accounts that are also advertisers on a
tenant offering the advertiser-budget method — see
`can_transfer_to_advertiser` in `GET /api/v1/publisher/finance`.

**Money units.** Request `amount` and response `amount_transferred`
are both **whole currency units**.

The amount must reach the network `payout_threshold`; a larger amount
than the balance is capped to the balance.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_publisher_finance_transfer_to_advertiser_post200_response import ApiV1PublisherFinanceTransferToAdvertiserPost200Response
from goadserver.models.api_v1_publisher_finance_transfer_to_advertiser_post_request import ApiV1PublisherFinanceTransferToAdvertiserPostRequest
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
    api_instance = goadserver.PayoutsApi(api_client)
    api_v1_publisher_finance_transfer_to_advertiser_post_request = {"amount":75.0} # ApiV1PublisherFinanceTransferToAdvertiserPostRequest | 

    try:
        # Move publisher balance to the advertiser budget.
        api_response = api_instance.api_v1_publisher_finance_transfer_to_advertiser_post(api_v1_publisher_finance_transfer_to_advertiser_post_request)
        print("The response of PayoutsApi->api_v1_publisher_finance_transfer_to_advertiser_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->api_v1_publisher_finance_transfer_to_advertiser_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_publisher_finance_transfer_to_advertiser_post_request** | [**ApiV1PublisherFinanceTransferToAdvertiserPostRequest**](ApiV1PublisherFinanceTransferToAdvertiserPostRequest.md)|  | 

### Return type

[**ApiV1PublisherFinanceTransferToAdvertiserPost200Response**](ApiV1PublisherFinanceTransferToAdvertiserPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transferred. |  -  |
**400** | &#x60;invalid_amount&#x60;, &#x60;below_minimum&#x60; (below the payout threshold), &#x60;no_balance&#x60;, or &#x60;bad_request&#x60; (body not valid JSON). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Missing scope (see Forbidden), or &#x60;not_advertiser&#x60; — the account has no advertiser role. |  -  |
**404** | The tenant has this feature&#39;s module switched off, or the account lacks the per-user right it needs. Deliberately &#x60;404&#x60; and not &#x60;403&#x60; so an ungranted caller cannot map which routes exist. The same endpoints are hidden from this tenant&#39;s rendered docs.  |  -  |
**409** | &#x60;balance_changed&#x60; — the balance moved while the request ran; nothing was deducted. |  -  |
**422** | &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


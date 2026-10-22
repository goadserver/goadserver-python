# goadserver.FundsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_funds_balance_settings_put**](FundsApi.md#api_v1_funds_balance_settings_put) | **PUT** /api/v1/funds/balance-settings | Set the low-balance warning.
[**api_v1_funds_deposit_type_fid_get**](FundsApi.md#api_v1_funds_deposit_type_fid_get) | **GET** /api/v1/funds/deposit/{type}/{fid} | Checkout data for an open deposit — or its paid state.
[**api_v1_funds_deposit_type_post**](FundsApi.md#api_v1_funds_deposit_type_post) | **POST** /api/v1/funds/deposit/{type} | Open a deposit (or redeem a bonus / coupon code).
[**api_v1_funds_deposits_id_delete**](FundsApi.md#api_v1_funds_deposits_id_delete) | **DELETE** /api/v1/funds/deposits/{id} | Cancel an unpaid deposit.
[**api_v1_funds_deposits_id_proof_get**](FundsApi.md#api_v1_funds_deposits_id_proof_get) | **GET** /api/v1/funds/deposits/{id}/proof | Download the proof of payment you uploaded on a deposit.
[**api_v1_funds_deposits_id_proof_post**](FundsApi.md#api_v1_funds_deposits_id_proof_post) | **POST** /api/v1/funds/deposits/{id}/proof | Upload the proof of payment of an open bank or Wise deposit.
[**api_v1_funds_deposits_id_txn_hash_post**](FundsApi.md#api_v1_funds_deposits_id_txn_hash_post) | **POST** /api/v1/funds/deposits/{id}/txn-hash | Attach the transaction hash of a manual crypto deposit, or the transaction ID of a Payoneer deposit.
[**api_v1_funds_get**](FundsApi.md#api_v1_funds_get) | **GET** /api/v1/funds | Current advertiser balance + pending deposits.
[**api_v1_funds_pay_types_get**](FundsApi.md#api_v1_funds_pay_types_get) | **GET** /api/v1/funds/pay-types | Payment methods this account can deposit with.
[**api_v1_funds_transactions_get**](FundsApi.md#api_v1_funds_transactions_get) | **GET** /api/v1/funds/transactions | Funds ledger — deposits, bonuses, transfers, refunds.
[**api_v1_funds_transfer_post**](FundsApi.md#api_v1_funds_transfer_post) | **POST** /api/v1/funds/transfer | Move balance to a connected advertiser account.


# **api_v1_funds_balance_settings_put**
> api_v1_funds_balance_settings_put(api_v1_funds_balance_settings_put_request)

Set the low-balance warning.

`ad_sendbalancemail` (0/1) turns the low-balance email on or off;
`ad_minbalance` is the threshold in **currency units** (your account
currency, e.g. `50.00`; stored as cents). Send either or both — an
omitted field keeps its value. Read them back as `min_balance` /
`low_balance` on `GET /funds`. Same handler as the panel.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_balance_settings_put_request import ApiV1FundsBalanceSettingsPutRequest
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
    api_instance = goadserver.FundsApi(api_client)
    api_v1_funds_balance_settings_put_request = {"ad_sendbalancemail":1,"ad_minbalance":50} # ApiV1FundsBalanceSettingsPutRequest | 

    try:
        # Set the low-balance warning.
        api_instance.api_v1_funds_balance_settings_put(api_v1_funds_balance_settings_put_request)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_balance_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_funds_balance_settings_put_request** | [**ApiV1FundsBalanceSettingsPutRequest**](ApiV1FundsBalanceSettingsPutRequest.md)|  | 

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
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Nothing sent, &#x60;ad_sendbalancemail&#x60; not 0/1, &#x60;ad_minbalance&#x60; negative / out of range, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposit_type_fid_get**
> ApiV1FundsDepositTypeFidGet200Response api_v1_funds_deposit_type_fid_get(type, fid)

Checkout data for an open deposit — or its paid state.

Same handler as the panel's pay dialog. For an unpaid deposit it
returns what is needed to pay: `view` names the method; hosted
gateways (mollie, inxy, payhound, bybitpay, capitalist, trustpay,
commercegate, yaadpay, whitebit fiat) return a checkout `url` to send
the payer to (they come back to the tenant's panel); bank returns
`bank_details` + `payee` + the transfer reference
(`transaction_id`); wallet types return `wallet_id` /
`wallet_network`; `wise` returns `bank_details` + `payee` like bank
(the tenant's Wise account details for the deposit currency). Manual
crypto wallets (btc_wallet, usdt_wallet*, usdc_wallet_erc20) also
return `accepts_txn_hash: true` and the last `txn_claim` — after
sending, POST the transaction hash to
/api/v1/funds/deposits/{id}/txn-hash. `payoneer` returns the same
(with `txn_ref_kind: reference`): POST the Payoneer transaction ID
there. `bank` / `wise` return `accepts_proof: true` and the current
`proof` where the tenant takes a proof of payment — upload it to
/api/v1/funds/deposits/{id}/proof. `paypal`, `revolut` and `stripe` need the browser
widget (client secret / order id) and are not completable by a
server-side caller — use a URL-based type for agents. Amounts
(`money`, `totalmoney`, `vat_amount`, `transaction_costs`) are cents.

Calling it can open a new order at the gateway (some types issue a
fresh checkout each call), so it needs `funds.deposit`, not
`funds.read`.

Once the deposit can no longer be paid the body is a single flag
instead: `{"invoice_paid": true}` (paid), `{"invoice_in_progress":
true}` (payment being processed) or `{"unknown_invoice": true}` (not
yours / cancelled) — poll for `invoice_paid`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_deposit_type_fid_get200_response import ApiV1FundsDepositTypeFidGet200Response
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
    api_instance = goadserver.FundsApi(api_client)
    type = 'bank' # str | The pay type the deposit was opened with.
    fid = 56 # int | Deposit id from POST /api/v1/funds/deposit/{type}.

    try:
        # Checkout data for an open deposit — or its paid state.
        api_response = api_instance.api_v1_funds_deposit_type_fid_get(type, fid)
        print("The response of FundsApi->api_v1_funds_deposit_type_fid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposit_type_fid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The pay type the deposit was opened with. | 
 **fid** | **int**| Deposit id from POST /api/v1/funds/deposit/{type}. | 

### Return type

[**ApiV1FundsDepositTypeFidGet200Response**](ApiV1FundsDepositTypeFidGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout payload, or a status flag |  -  |
**400** | Unknown pay type or deposit id (&#x60;invalid_request&#x60;), or a type with no checkout (&#x60;unsupported_paytype&#x60;). |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**409** | Stripe not configured for the tenant. |  -  |
**500** | The gateway refused to open the order (&#x60;&lt;type&gt;_failed&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposit_type_post**
> ApiV1FundsDepositTypePost200Response api_v1_funds_deposit_type_post(type, api_v1_funds_deposit_type_post_request)

Open a deposit (or redeem a bonus / coupon code).

Same handler as the panel. For a payment type from
GET /api/v1/funds/pay-types this books an unpaid deposit of `amount`
(currency units, >= the type's `min_amount`) and returns its id as
`fid` — no payment happens yet. Then call
GET /api/v1/funds/deposit/{type}/{fid} for the checkout URL / bank
details, and poll it (or GET /api/v1/funds/transactions) for the paid
state.

Special `{type}` values that settle directly and need no pay type:
- `bonus` — redeem a bonus code: body `{bonus: "CODE"}`, no amount.
- `coupon` — redeem a voucher: body `{code: "CODE"}`, no amount.
- `advertiser` — transfer `amount` to a connected advertiser
  (`connectedUsers` = its user id).

`amount_deduction` and `credit_no_invoice` exist but need an admin
session — an API key always gets 403.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_deposit_type_post200_response import ApiV1FundsDepositTypePost200Response
from goadserver.models.api_v1_funds_deposit_type_post_request import ApiV1FundsDepositTypePostRequest
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
    api_instance = goadserver.FundsApi(api_client)
    type = 'bank' # str | A `key` from GET /api/v1/funds/pay-types, or bonus / coupon / advertiser.
    api_v1_funds_deposit_type_post_request = {"amount":250} # ApiV1FundsDepositTypePostRequest | 

    try:
        # Open a deposit (or redeem a bonus / coupon code).
        api_response = api_instance.api_v1_funds_deposit_type_post(type, api_v1_funds_deposit_type_post_request)
        print("The response of FundsApi->api_v1_funds_deposit_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposit_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| A &#x60;key&#x60; from GET /api/v1/funds/pay-types, or bonus / coupon / advertiser. | 
 **api_v1_funds_deposit_type_post_request** | [**ApiV1FundsDepositTypePostRequest**](ApiV1FundsDepositTypePostRequest.md)|  | 

### Return type

[**ApiV1FundsDepositTypePost200Response**](ApiV1FundsDepositTypePost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pay type: &#x60;{fid}&#x60; (the deposit id). bonus / coupon / advertiser: a message about the credited / transferred amount.  |  -  |
**400** | Missing or unavailable payment type (&#x60;invalid_paytype&#x60;), or a coupon without &#x60;code&#x60;. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**413** | Body over 16 KB. |  -  |
**422** | Amount missing / below the minimum, or an invalid bonus (&#x60;errors.bonus: [FALSE_CODE_GIVEN]&#x60;) / coupon code (&#x60;invalid_coupon&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposits_id_delete**
> ApiV1RetargetingPixelsIdDelete200Response api_v1_funds_deposits_id_delete(id)

Cancel an unpaid deposit.

Deletes an open deposit of yours (same handler as the panel). A paid
deposit, or one a card / PayPal / Stripe payment is already
processing, can't be cancelled (404).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
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
    api_instance = goadserver.FundsApi(api_client)
    id = 56 # int | Deposit id (`fid`).

    try:
        # Cancel an unpaid deposit.
        api_response = api_instance.api_v1_funds_deposits_id_delete(id)
        print("The response of FundsApi->api_v1_funds_deposits_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposits_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Deposit id (&#x60;fid&#x60;). | 

### Return type

[**ApiV1RetargetingPixelsIdDelete200Response**](ApiV1RetargetingPixelsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancelled |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found or cannot be cancelled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposits_id_proof_get**
> bytes api_v1_funds_deposits_id_proof_get(id)

Download the proof of payment you uploaded on a deposit.

Streams your uploaded proof inline with its type (`application/pdf`,
`image/jpeg` or `image/png`). 404 when the deposit is not yours or
has no proof.


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
    api_instance = goadserver.FundsApi(api_client)
    id = 56 # int | Deposit id (`fid`).

    try:
        # Download the proof of payment you uploaded on a deposit.
        api_response = api_instance.api_v1_funds_deposits_id_proof_get(id)
        print("The response of FundsApi->api_v1_funds_deposits_id_proof_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposits_id_proof_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Deposit id (&#x60;fid&#x60;). | 

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | No proof on this deposit, or not your deposit. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposits_id_proof_post**
> ApiV1FundsDepositsIdProofPost200Response api_v1_funds_deposits_id_proof_post(id, file)

Upload the proof of payment of an open bank or Wise deposit.

Same handler as the panel's deposit list and pay dialog. After paying
an open `bank` or `wise` deposit by transfer, upload the proof of
payment (bank receipt / transfer confirmation) so the tenant's finance
team can approve the deposit without waiting for the money to show up.
Only where the tenant switched it on for that method — the deposit
rows and the deposit payload say so with `accepts_proof: true`.

Multipart, field `file`: a PDF, JPG or PNG of at most 10 MB. The type
is read from the file content, not its name. A new upload replaces
the earlier proof; cancelling the deposit removes it. **The proof
never credits the balance** — an admin approves the deposit. At most
30 uploads per hour per account.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_deposits_id_proof_post200_response import ApiV1FundsDepositsIdProofPost200Response
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
    api_instance = goadserver.FundsApi(api_client)
    id = 56 # int | Deposit id (`fid`).
    file = None # bytes | PDF, JPG or PNG, max 10 MB.

    try:
        # Upload the proof of payment of an open bank or Wise deposit.
        api_response = api_instance.api_v1_funds_deposits_id_proof_post(id, file)
        print("The response of FundsApi->api_v1_funds_deposits_id_proof_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposits_id_proof_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Deposit id (&#x60;fid&#x60;). | 
 **file** | **bytes**| PDF, JPG or PNG, max 10 MB. | 

### Return type

[**ApiV1FundsDepositsIdProofPost200Response**](ApiV1FundsDepositsIdProofPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Deposit not found (not yours). |  -  |
**413** | File larger than 10 MB. |  -  |
**422** | &#x60;errors.file&#x60;: no file, not a PDF / JPG / PNG, the deposit is paid, or its payment method takes no proof (not bank / Wise, or switched off by the tenant). |  -  |
**429** | Too many uploads; see Retry-After. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_deposits_id_txn_hash_post**
> ApiV1FundsDepositsIdTxnHashPost200Response api_v1_funds_deposits_id_txn_hash_post(id, api_v1_funds_deposits_id_txn_hash_post_request)

Attach the transaction hash of a manual crypto deposit, or the transaction ID of a Payoneer deposit.

Same handler as the panel's pay dialog. After sending a manual
crypto deposit (btc_wallet, usdt_wallet, usdt_wallet_trc20 /
_bep20 / _erc20, usdc_wallet_erc20) to the tenant's wallet, post the
transaction hash. It is looked up on the public blockchain and the
result is stored on the deposit for the tenant's finance team.

**The hash never credits the balance.** An admin approves the
deposit after the check (or with a written override). The check
confirms: the tenant's wallet received the deposit's asset (the real
USDT / USDC contract, or BTC), at least the invoice total, in a final
block, sent no earlier than the deposit was opened.

`txn_claim.status`: `verified`, `pending` (not final yet — post the
same hash again later to re-check), `mismatch` (wrong asset / wallet
/ amount / date — see `reason`), `not_found`, `unchecked` (the
tenant's wallet or network is not configured) or `error` (the
explorer could not be reached). Posting a different hash replaces the
earlier one while the deposit is open. A hash already used on another
deposit is refused. At most 20 checks per hour per account.

**Payoneer deposits** take the Payoneer transaction ID on the same
route: 4–64 letters, digits and `. _ / # : -`, no spaces. It is
stored as given for the finance team to match with the payment
(`txn_claim.status: submitted`) and not checked automatically; one
ID per deposit, an ID already on another deposit is refused, posting
a new one replaces it while the deposit is open.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post200_response import ApiV1FundsDepositsIdTxnHashPost200Response
from goadserver.models.api_v1_funds_deposits_id_txn_hash_post_request import ApiV1FundsDepositsIdTxnHashPostRequest
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
    api_instance = goadserver.FundsApi(api_client)
    id = 56 # int | Deposit id (`fid`).
    api_v1_funds_deposits_id_txn_hash_post_request = {"txn_hash":"d6f659cce4d1bf2f1c724593fde8d9bb7c0385d5224ad410557f85297cdc8f71"} # ApiV1FundsDepositsIdTxnHashPostRequest | 

    try:
        # Attach the transaction hash of a manual crypto deposit, or the transaction ID of a Payoneer deposit.
        api_response = api_instance.api_v1_funds_deposits_id_txn_hash_post(id, api_v1_funds_deposits_id_txn_hash_post_request)
        print("The response of FundsApi->api_v1_funds_deposits_id_txn_hash_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_deposits_id_txn_hash_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Deposit id (&#x60;fid&#x60;). | 
 **api_v1_funds_deposits_id_txn_hash_post_request** | [**ApiV1FundsDepositsIdTxnHashPostRequest**](ApiV1FundsDepositsIdTxnHashPostRequest.md)|  | 

### Return type

[**ApiV1FundsDepositsIdTxnHashPost200Response**](ApiV1FundsDepositsIdTxnHashPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored, with the check result |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Deposit not found (not yours). |  -  |
**422** | &#x60;errors.txn_hash&#x60;: empty, not a valid hash for the network (or not a valid Payoneer transaction ID), already used on another deposit, the deposit is paid, or its payment method takes no hash. |  -  |
**429** | Too many checks; see Retry-After. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_get**
> ApiV1FundsGet200Response api_v1_funds_get()

Current advertiser balance + pending deposits.

Use this before deciding to launch or pause a campaign — `low_balance`
is true when current balance is below the user-configured minimum.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_get200_response import ApiV1FundsGet200Response
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
    api_instance = goadserver.FundsApi(api_client)

    try:
        # Current advertiser balance + pending deposits.
        api_response = api_instance.api_v1_funds_get()
        print("The response of FundsApi->api_v1_funds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1FundsGet200Response**](ApiV1FundsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance snapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_pay_types_get**
> ApiV1FundsPayTypesGet200Response api_v1_funds_pay_types_get()

Payment methods this account can deposit with.

The `{type}` values POST /api/v1/funds/deposit/{type} accepts for this
account: active on the tenant, allowed by the account's rights and
offered in its currency. Same handler as the panel's Add Funds page.
`initiates_payment: false` means the deposit only books an invoice to
settle out of band (bank transfer, wallet address, Pay ID).
`min_amount` is in currency units.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_pay_types_get200_response import ApiV1FundsPayTypesGet200Response
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
    api_instance = goadserver.FundsApi(api_client)

    try:
        # Payment methods this account can deposit with.
        api_response = api_instance.api_v1_funds_pay_types_get()
        print("The response of FundsApi->api_v1_funds_pay_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_pay_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1FundsPayTypesGet200Response**](ApiV1FundsPayTypesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pay types |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_transactions_get**
> ApiV1FundsTransactionsGet200Response api_v1_funds_transactions_get(var_from=var_from, to=to, filter_id=filter_id, filter_paytype=filter_paytype, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)

Funds ledger — deposits, bonuses, transfers, refunds.

Paginated `advertiser_money` rows for the account (paid and unpaid,
incl. transfers received). Same handler as the panel's Transactions
tab. `money` is in cents; `amount` is the same value in currency units
(negative for a transfer you sent). `status` is `pending`,
`processing` or `completed`. `payment_methods` lists every paytype the
history carries, for filtering with `filter_paytype`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_transactions_get200_response import ApiV1FundsTransactionsGet200Response
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
    api_instance = goadserver.FundsApi(api_client)
    var_from = '2013-10-20' # date | dateadded >= from (optional)
    to = '2013-10-20' # date | dateadded <= to (optional)
    filter_id = 56 # int |  (optional)
    filter_paytype = 56 # int | Numeric paytype (negative = internal: -1 bonus, -2 transfer, -3 flat refund, -4 coupon, -5 from publisher, -6 RON refund, -7 credit, -8 deduction). (optional)
    sort_by = dateadded # str |  (optional) (default to dateadded)
    sort_dir = desc # str |  (optional) (default to desc)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # Funds ledger — deposits, bonuses, transfers, refunds.
        api_response = api_instance.api_v1_funds_transactions_get(var_from=var_from, to=to, filter_id=filter_id, filter_paytype=filter_paytype, sort_by=sort_by, sort_dir=sort_dir, page=page, per_page=per_page)
        print("The response of FundsApi->api_v1_funds_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| dateadded &gt;&#x3D; from | [optional] 
 **to** | **date**| dateadded &lt;&#x3D; to | [optional] 
 **filter_id** | **int**|  | [optional] 
 **filter_paytype** | **int**| Numeric paytype (negative &#x3D; internal: -1 bonus, -2 transfer, -3 flat refund, -4 coupon, -5 from publisher, -6 RON refund, -7 credit, -8 deduction). | [optional] 
 **sort_by** | **str**|  | [optional] [default to dateadded]
 **sort_dir** | **str**|  | [optional] [default to desc]
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**ApiV1FundsTransactionsGet200Response**](ApiV1FundsTransactionsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ledger page |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_transfer_post**
> api_v1_funds_transfer_post(api_v1_funds_transfer_post_request)

Move balance to a connected advertiser account.

Transfers `amount` from your advertiser balance to another account
your network has connected to yours. Every panel safeguard applies:

- the account needs the `transfer_money_other_advertiser` right
  (403 otherwise);
- `connectedUsers` must be on the account's connected-transfer list,
  which only network staff maintain (403 otherwise);
- `amount` is in **currency units** of your account currency, at
  least 5.00;
- the balance is checked and debited atomically (422 `insufficient`,
  409 `balance_changed` on a race); the recipient is credited in
  their own currency at the current rate, and a ledger row
  (paytype −2) plus an action-log entry record it.

`funds.write` is required for every key path that moves money,
including `POST /funds/deposit/advertiser`. Not idempotent — do not
blindly retry a timed-out call; check `GET /funds/transactions`.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_funds_transfer_post_request import ApiV1FundsTransferPostRequest
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
    api_instance = goadserver.FundsApi(api_client)
    api_v1_funds_transfer_post_request = {"connectedUsers":10234,"amount":250} # ApiV1FundsTransferPostRequest | 

    try:
        # Move balance to a connected advertiser account.
        api_instance.api_v1_funds_transfer_post(api_v1_funds_transfer_post_request)
    except Exception as e:
        print("Exception when calling FundsApi->api_v1_funds_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_funds_transfer_post_request** | [**ApiV1FundsTransferPostRequest**](ApiV1FundsTransferPostRequest.md)|  | 

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
**200** | Transferred. The body is the bare string &#x60;SUCCESS_TRANSFER&#x60;. |  -  |
**400** | &#x60;invalid_request&#x60;, &#x60;missing_target&#x60;. |  -  |
**403** | &#x60;missing_scope&#x60; (funds.write), right missing, or recipient not connected. |  -  |
**409** | &#x60;balance_changed&#x60; — retry after reading the balance. |  -  |
**422** | Amount invalid / below 5.00, &#x60;insufficient&#x60; balance, or &#x60;unknown_fields&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


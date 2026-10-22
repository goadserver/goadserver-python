# goadserver.BidRulesetsApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_bid_rulesets_get**](BidRulesetsApi.md#api_v1_bid_rulesets_get) | **GET** /api/v1/bid-rulesets | List the caller&#39;s bid rulesets (lightweight rows).
[**api_v1_bid_rulesets_id_clone_post**](BidRulesetsApi.md#api_v1_bid_rulesets_id_clone_post) | **POST** /api/v1/bid-rulesets/{id}/clone | Clone a ruleset with all its rules.
[**api_v1_bid_rulesets_id_delete**](BidRulesetsApi.md#api_v1_bid_rulesets_id_delete) | **DELETE** /api/v1/bid-rulesets/{id} | Soft-delete a ruleset.
[**api_v1_bid_rulesets_id_get**](BidRulesetsApi.md#api_v1_bid_rulesets_id_get) | **GET** /api/v1/bid-rulesets/{id} | Show one ruleset, including all rules.
[**api_v1_bid_rulesets_id_patch**](BidRulesetsApi.md#api_v1_bid_rulesets_id_patch) | **PATCH** /api/v1/bid-rulesets/{id} | Update a ruleset&#39;s metadata and/or replace its rules.
[**api_v1_bid_rulesets_post**](BidRulesetsApi.md#api_v1_bid_rulesets_post) | **POST** /api/v1/bid-rulesets | Create a new bid ruleset (with rules in one shot).


# **api_v1_bid_rulesets_get**
> ApiV1BidRulesetsGet200Response api_v1_bid_rulesets_get(paytype=paytype, include_deleted=include_deleted)

List the caller's bid rulesets (lightweight rows).

Returns every non-deleted ruleset of the authenticated user,
optionally filtered by paytype. Not paginated: `page` is always
1 and `per_page` / `total_rows` equal the number of rows
returned (users typically hold fewer than 50 rulesets). Each row
carries identity + summary counts (`rule_count`,
`campaign_count`) but **not** the rule rows themselves — fetch
the full record via `GET /api/v1/bid-rulesets/{id}` when you
need the conditions JSON for editing.

Use this endpoint to populate ruleset-picker UIs (e.g. the
campaign-edit "Use bid rules" picker) and library views.

Default sort is `updated DESC`. Soft-deleted rulesets are
excluded.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_bid_rulesets_get200_response import ApiV1BidRulesetsGet200Response
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    paytype = 'paytype_example' # str | Filter to rulesets of one paytype. (optional)
    include_deleted = False # bool | Also return soft-deleted rulesets (`is_deleted: true`). (optional) (default to False)

    try:
        # List the caller's bid rulesets (lightweight rows).
        api_response = api_instance.api_v1_bid_rulesets_get(paytype=paytype, include_deleted=include_deleted)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paytype** | **str**| Filter to rulesets of one paytype. | [optional] 
 **include_deleted** | **bool**| Also return soft-deleted rulesets (&#x60;is_deleted: true&#x60;). | [optional] [default to False]

### Return type

[**ApiV1BidRulesetsGet200Response**](ApiV1BidRulesetsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ruleset list (all rows in one page). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_bid_rulesets_id_clone_post**
> BidRuleset api_v1_bid_rulesets_id_clone_post(id, api_v1_bid_rulesets_id_clone_post_request=api_v1_bid_rulesets_id_clone_post_request)

Clone a ruleset with all its rules.

Duplicates the ruleset row and every non-deleted rule on it.
New ruleset name defaults to `<original> (copy)` — override
via the body. Same `paytype` and `default_tz` as the source.
Ad / campaign attachments are **not** copied — the clone
starts unattached (`campaign_count: 0`).

Use this to fork a working ruleset for an experiment without
affecting the live campaigns that reference the original.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_bid_rulesets_id_clone_post_request import ApiV1BidRulesetsIdClonePostRequest
from goadserver.models.bid_ruleset import BidRuleset
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    id = 56 # int | 
    api_v1_bid_rulesets_id_clone_post_request = goadserver.ApiV1BidRulesetsIdClonePostRequest() # ApiV1BidRulesetsIdClonePostRequest |  (optional)

    try:
        # Clone a ruleset with all its rules.
        api_response = api_instance.api_v1_bid_rulesets_id_clone_post(id, api_v1_bid_rulesets_id_clone_post_request=api_v1_bid_rulesets_id_clone_post_request)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_bid_rulesets_id_clone_post_request** | [**ApiV1BidRulesetsIdClonePostRequest**](ApiV1BidRulesetsIdClonePostRequest.md)|  | [optional] 

### Return type

[**BidRuleset**](BidRuleset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ruleset cloned. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Source ruleset not found or not owned by caller. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_bid_rulesets_id_delete**
> ApiV1BidRulesetsIdDelete200Response api_v1_bid_rulesets_id_delete(id)

Soft-delete a ruleset.

Sets `isdeleted=1` on the ruleset (rule rows stay in place for
audit; goadserver simply stops loading them on next refresh).
Idempotent.

**Hard-blocked while attached to a non-deleted campaign** —
the response is a 422 whose message gives the number of
attached campaigns (`ruleset is attached to N active
campaign(s); detach first`). Find them with
`GET /api/v1/campaigns` and detach each one (set `bidruleset_id=0` via
`PATCH /api/v1/campaigns/{type}/{id}`) first. The list
endpoint's `campaign_count` flags this ahead of time.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_bid_rulesets_id_delete200_response import ApiV1BidRulesetsIdDelete200Response
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    id = 56 # int | 

    try:
        # Soft-delete a ruleset.
        api_response = api_instance.api_v1_bid_rulesets_id_delete(id)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiV1BidRulesetsIdDelete200Response**](ApiV1BidRulesetsIdDelete200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ruleset not found or already deleted. |  -  |
**422** | Ruleset is still attached to one or more non-deleted campaigns. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_bid_rulesets_id_get**
> BidRuleset api_v1_bid_rulesets_id_get(id)

Show one ruleset, including all rules.

Returns the full ruleset record with the rule rows in
priority order — this is what an editor UI loads to render
the rule list and condition pickers.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.bid_ruleset import BidRuleset
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    id = 56 # int | 

    try:
        # Show one ruleset, including all rules.
        api_response = api_instance.api_v1_bid_rulesets_id_get(id)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BidRuleset**](BidRuleset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ruleset detail (with rules pre-sorted by priority). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ruleset not found or not owned by caller. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_bid_rulesets_id_patch**
> BidRuleset api_v1_bid_rulesets_id_patch(id, api_v1_bid_rulesets_id_patch_request)

Update a ruleset's metadata and/or replace its rules.

Fields you leave out keep their stored value:

- `name`, `paytype`, `default_tz` omitted → unchanged.
- `rules` omitted → the current rules are kept.
- `rules` present → the array **replaces** the whole rule list
  in one transaction; `rules: []` clears it.

Every save rewrites the rule rows: the previous rows are
soft-deleted and the resulting list is inserted with **new**
rule ids (stats already attributed to an old rule id stay on the
old row). Rule `id`s in the body are ignored.

`paytype` can be changed, as in the panel editor — make sure the
attached campaigns use the same paytype.

You can send back a record fetched with `GET` unchanged: the
read-only fields (`id`, `userid`, `is_deleted`, `created`,
`updated`, `campaign_count`, `rule_count`) are accepted and
ignored, also in strict mode.

Reorder by changing `priority` values — rules walk in
ascending priority at serve time.

Editing a ruleset that's attached to multiple campaigns
affects all of them — no per-campaign override exists. The
list endpoint surfaces `campaign_count` so a UI can warn
before save.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_bid_rulesets_id_patch_request import ApiV1BidRulesetsIdPatchRequest
from goadserver.models.bid_ruleset import BidRuleset
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    id = 56 # int | 
    api_v1_bid_rulesets_id_patch_request = {"name":"RTB CPC playbook v2"} # ApiV1BidRulesetsIdPatchRequest | 

    try:
        # Update a ruleset's metadata and/or replace its rules.
        api_response = api_instance.api_v1_bid_rulesets_id_patch(id, api_v1_bid_rulesets_id_patch_request)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **api_v1_bid_rulesets_id_patch_request** | [**ApiV1BidRulesetsIdPatchRequest**](ApiV1BidRulesetsIdPatchRequest.md)|  | 

### Return type

[**BidRuleset**](BidRuleset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. Body is the freshly-updated ruleset. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Ruleset not found or not owned by caller. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_bid_rulesets_post**
> BidRuleset api_v1_bid_rulesets_post(api_v1_bid_rulesets_post_request)

Create a new bid ruleset (with rules in one shot).

Creates a ruleset and the full rule list in a single
transaction. Rules without an `id` are inserted; the supplied
`priority` is honored — sort the array client-side or just set
`priority` to the desired walk order.

`paytype` must match the paytype of the campaigns you attach the
ruleset to. `default_tz` defaults to `UTC` when omitted. Rule
`bid` values are whole cents.

Reference: [`docs/BID_RULES.md`](BID_RULES.md).


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_bid_rulesets_post_request import ApiV1BidRulesetsPostRequest
from goadserver.models.bid_ruleset import BidRuleset
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
    api_instance = goadserver.BidRulesetsApi(api_client)
    api_v1_bid_rulesets_post_request = {"name":"RTB CPC playbook","paytype":"cpc","default_tz":"UTC"} # ApiV1BidRulesetsPostRequest | 

    try:
        # Create a new bid ruleset (with rules in one shot).
        api_response = api_instance.api_v1_bid_rulesets_post(api_v1_bid_rulesets_post_request)
        print("The response of BidRulesetsApi->api_v1_bid_rulesets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRulesetsApi->api_v1_bid_rulesets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_bid_rulesets_post_request** | [**ApiV1BidRulesetsPostRequest**](ApiV1BidRulesetsPostRequest.md)|  | 

### Return type

[**BidRuleset**](BidRuleset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. Body is the freshly-created ruleset (&#x60;BidRuleset&#x60; shape, with &#x60;rules&#x60; populated and a fresh &#x60;id&#x60; per rule). |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**422** | Validation error (missing name/paytype, bad enum, malformed conditions, …). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


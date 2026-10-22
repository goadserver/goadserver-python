# goadserver.OAuthApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_public_integrations_hooks_token_post**](OAuthApi.md#api_public_integrations_hooks_token_post) | **POST** /api/public/integrations/hooks/{token} | Incoming webhook — create a lead, contact or task from JSON.
[**api_public_oauth_introspect_post**](OAuthApi.md#api_public_oauth_introspect_post) | **POST** /api/public/oauth/introspect | Introspect one of the calling app&#39;s tokens (RFC 7662).
[**api_public_oauth_metadata_get**](OAuthApi.md#api_public_oauth_metadata_get) | **GET** /api/public/oauth/metadata | Authorization server metadata (RFC 8414) for this host.
[**api_public_oauth_revoke_post**](OAuthApi.md#api_public_oauth_revoke_post) | **POST** /api/public/oauth/revoke | Revoke an access or refresh token (RFC 7009).
[**api_public_oauth_token_post**](OAuthApi.md#api_public_oauth_token_post) | **POST** /api/public/oauth/token | Exchange an authorization code, or rotate a refresh token.


# **api_public_integrations_hooks_token_post**
> ApiPublicIntegrationsHooksTokenPost200Response api_public_integrations_hooks_token_post(token, request_body)

Incoming webhook — create a lead, contact or task from JSON.

The URL of an *Incoming webhook* connector (Admin → Integrations). The
path token is the credential; a connector can additionally require
`X-Integration-Signature: t=<unix>,v1=<hex HMAC-SHA256(secret, "<t>.<body>")>`.
What the body becomes is the connector's field mapping. Max 64 KB.


### Example


```python
import goadserver
from goadserver.models.api_public_integrations_hooks_token_post200_response import ApiPublicIntegrationsHooksTokenPost200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.OAuthApi(api_client)
    token = 'token_example' # str | whin_… from the connector.
    request_body = None # Dict[str, object] | 

    try:
        # Incoming webhook — create a lead, contact or task from JSON.
        api_response = api_instance.api_public_integrations_hooks_token_post(token, request_body)
        print("The response of OAuthApi->api_public_integrations_hooks_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->api_public_integrations_hooks_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| whin_… from the connector. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**ApiPublicIntegrationsHooksTokenPost200Response**](ApiPublicIntegrationsHooksTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created. |  -  |
**401** | Signature required and missing or wrong. |  -  |
**404** | Unknown webhook. |  -  |
**422** | The mapped fields did not make a valid record. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_oauth_introspect_post**
> ApiPublicOauthIntrospectPost200Response api_public_oauth_introspect_post(token, client_id=client_id, client_secret=client_secret)

Introspect one of the calling app's tokens (RFC 7662).

### Example


```python
import goadserver
from goadserver.models.api_public_oauth_introspect_post200_response import ApiPublicOauthIntrospectPost200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.OAuthApi(api_client)
    token = 'token_example' # str | 
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Introspect one of the calling app's tokens (RFC 7662).
        api_response = api_instance.api_public_oauth_introspect_post(token, client_id=client_id, client_secret=client_secret)
        print("The response of OAuthApi->api_public_oauth_introspect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->api_public_oauth_introspect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**ApiPublicOauthIntrospectPost200Response**](ApiPublicOauthIntrospectPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#x60;{active: false}&#x60; for anything that is not a live token of this app. |  -  |
**401** | invalid_client. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_oauth_metadata_get**
> Dict[str, object] api_public_oauth_metadata_get()

Authorization server metadata (RFC 8414) for this host.

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.OAuthApi(api_client)

    try:
        # Authorization server metadata (RFC 8414) for this host.
        api_response = api_instance.api_public_oauth_metadata_get()
        print("The response of OAuthApi->api_public_oauth_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->api_public_oauth_metadata_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Endpoints and supported flows. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_oauth_revoke_post**
> api_public_oauth_revoke_post(token, client_id=client_id, client_secret=client_secret)

Revoke an access or refresh token (RFC 7009).

Revoking a refresh token revokes every token of its authorization. Always 200 for an authenticated client.

### Example


```python
import goadserver
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.OAuthApi(api_client)
    token = 'token_example' # str | 
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Revoke an access or refresh token (RFC 7009).
        api_instance.api_public_oauth_revoke_post(token, client_id=client_id, client_secret=client_secret)
    except Exception as e:
        print("Exception when calling OAuthApi->api_public_oauth_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Revoked (or unknown — indistinguishable by design). |  -  |
**401** | invalid_client. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_oauth_token_post**
> ApiPublicOauthTokenPost200Response api_public_oauth_token_post(grant_type, code=code, redirect_uri=redirect_uri, code_verifier=code_verifier, refresh_token=refresh_token, scope=scope, client_id=client_id, client_secret=client_secret)

Exchange an authorization code, or rotate a refresh token.

`grant_type=authorization_code` needs `code`, `redirect_uri` (exactly as
sent to `/oauth/authorize`) and `code_verifier`. `grant_type=refresh_token`
needs `refresh_token` and may narrow with `scope`; the presented refresh
token is spent and a new one returned — presenting a spent one again
revokes every token of that authorization. Confidential apps
authenticate with HTTP Basic (`client_id:client_secret`) or
`client_id` + `client_secret` in the body; public apps send `client_id` only.


### Example


```python
import goadserver
from goadserver.models.api_public_oauth_token_post200_response import ApiPublicOauthTokenPost200Response
from goadserver.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://up.go-adserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goadserver.Configuration(
    host = "https://up.go-adserver.com"
)


# Enter a context with an instance of the API client
with goadserver.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goadserver.OAuthApi(api_client)
    grant_type = 'grant_type_example' # str | 
    code = 'code_example' # str | oac_… (authorization_code) (optional)
    redirect_uri = 'redirect_uri_example' # str |  (optional)
    code_verifier = 'code_verifier_example' # str | 43–128 chars (optional)
    refresh_token = 'refresh_token_example' # str | ort_… (refresh_token) (optional)
    scope = 'scope_example' # str | Space-separated; refresh may only narrow. (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Exchange an authorization code, or rotate a refresh token.
        api_response = api_instance.api_public_oauth_token_post(grant_type, code=code, redirect_uri=redirect_uri, code_verifier=code_verifier, refresh_token=refresh_token, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of OAuthApi->api_public_oauth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->api_public_oauth_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | 
 **code** | **str**| oac_… (authorization_code) | [optional] 
 **redirect_uri** | **str**|  | [optional] 
 **code_verifier** | **str**| 43–128 chars | [optional] 
 **refresh_token** | **str**| ort_… (refresh_token) | [optional] 
 **scope** | **str**| Space-separated; refresh may only narrow. | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**ApiPublicOauthTokenPost200Response**](ApiPublicOauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tokens. |  -  |
**400** | invalid_request, invalid_grant, invalid_scope or unsupported_grant_type (RFC 6749 §5.2). |  -  |
**401** | invalid_client. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


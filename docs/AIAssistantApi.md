# goadserver.AIAssistantApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_mcp_post**](AIAssistantApi.md#api_v1_mcp_post) | **POST** /api/v1/mcp | MCP endpoint — connect an AI assistant to this account.


# **api_v1_mcp_post**
> ApiV1McpPost200Response api_v1_mcp_post(api_v1_mcp_post_request)

MCP endpoint — connect an AI assistant to this account.

Model Context Protocol server (JSON-RPC 2.0 over HTTP). Point an MCP
client at this URL with `Authorization: Bearer gas_live_…` and the
assistant can use the account through a curated set of tools.

The key must be marked **"Allow this key to connect an AI assistant"**
in MyAccount → API access; keys minted before that option existed are
not agent-capable. The tools an assistant sees are filtered by the
key's scopes, so a read-only key is never shown a write tool.

Methods: `initialize`, `ping`, `tools/list`, `tools/call`. One
JSON-RPC request per POST — batching is not accepted. Tool calls are
rate limited separately from the REST API (default 240/min per key);
`initialize`, `ping` and `tools/list` are free.


### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_mcp_post200_response import ApiV1McpPost200Response
from goadserver.models.api_v1_mcp_post_request import ApiV1McpPostRequest
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
    api_instance = goadserver.AIAssistantApi(api_client)
    api_v1_mcp_post_request = goadserver.ApiV1McpPostRequest() # ApiV1McpPostRequest | 

    try:
        # MCP endpoint — connect an AI assistant to this account.
        api_response = api_instance.api_v1_mcp_post(api_v1_mcp_post_request)
        print("The response of AIAssistantApi->api_v1_mcp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantApi->api_v1_mcp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_mcp_post_request** | [**ApiV1McpPostRequest**](ApiV1McpPostRequest.md)|  | 

### Return type

[**ApiV1McpPost200Response**](ApiV1McpPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-RPC response. |  -  |
**202** | Notification accepted (no response body). |  -  |
**404** | MCP is not available on this instance or for this network. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


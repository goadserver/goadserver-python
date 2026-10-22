# goadserver.AgenticMediaBuyingApi

All URIs are relative to *https://up.go-adserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_adspaces_id_media_buying_actions_action_id_decide_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_actions_action_id_decide_post) | **POST** /api/v1/adspaces/{id}/media-buying/actions/{actionId}/decide | Approve or reject a proposal.
[**api_v1_adspaces_id_media_buying_actions_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_actions_get) | **GET** /api/v1/adspaces/{id}/media-buying/actions | Activity log: every block, bid, budget and other change, and open proposals.
[**api_v1_adspaces_id_media_buying_agent_run_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_agent_run_post) | **POST** /api/v1/adspaces/{id}/media-buying/agent/run | Run the buying agent now.
[**api_v1_adspaces_id_media_buying_agent_runs_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_agent_runs_get) | **GET** /api/v1/adspaces/{id}/media-buying/agent/runs | The buying agent&#39;s recent runs with their summaries and proposals.
[**api_v1_adspaces_id_media_buying_block_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_block_post) | **POST** /api/v1/adspaces/{id}/media-buying/block | Block or unblock one source zone at the network.
[**api_v1_adspaces_id_media_buying_compare_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_compare_get) | **GET** /api/v1/adspaces/{id}/media-buying/compare | Compare with another buy (A/B, e.g. against a control left to the network&#39;s own optimiser).
[**api_v1_adspaces_id_media_buying_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_get) | **GET** /api/v1/adspaces/{id}/media-buying | Overview: the connected network, what it supports, the policy and open proposals.
[**api_v1_adspaces_id_media_buying_ips_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_ips_get) | **GET** /api/v1/adspaces/{id}/media-buying/ips | The IP preblock list: ranges on the network&#39;s exclusion list and proposals.
[**api_v1_adspaces_id_media_buying_ips_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_ips_post) | **POST** /api/v1/adspaces/{id}/media-buying/ips | Change the IP preblock list.
[**api_v1_adspaces_id_media_buying_launch_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_get) | **GET** /api/v1/adspaces/{id}/media-buying/launch | What a new campaign can be launched with (unconnected ad zones).
[**api_v1_adspaces_id_media_buying_launch_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_post) | **POST** /api/v1/adspaces/{id}/media-buying/launch | Launch a new campaign at the network for this ad zone.
[**api_v1_adspaces_id_media_buying_launch_templates_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_launch_templates_get) | **GET** /api/v1/adspaces/{id}/media-buying/launch/templates | Existing campaigns that can be cloned for a launch.
[**api_v1_adspaces_id_media_buying_network_budget_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_network_budget_get) | **GET** /api/v1/adspaces/{id}/media-buying/network-budget | The campaign&#39;s daily budget at the network.
[**api_v1_adspaces_id_media_buying_policy_put**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_policy_put) | **PUT** /api/v1/adspaces/{id}/media-buying/policy | Save the buying policy (any subset of its fields).
[**api_v1_adspaces_id_media_buying_policy_suggest_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_policy_suggest_get) | **GET** /api/v1/adspaces/{id}/media-buying/policy/suggest | Suggested policy from the zone&#39;s own traffic, with a reason per field.
[**api_v1_adspaces_id_media_buying_report_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_report_post) | **POST** /api/v1/adspaces/{id}/media-buying/report | Send the media buying report now.
[**api_v1_adspaces_id_media_buying_segments_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_segments_get) | **GET** /api/v1/adspaces/{id}/media-buying/segments | Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
[**api_v1_adspaces_id_media_buying_source_bid_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_bid_get) | **GET** /api/v1/adspaces/{id}/media-buying/source/bid | The campaign&#39;s current bid at the network.
[**api_v1_adspaces_id_media_buying_source_bid_put**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_bid_put) | **PUT** /api/v1/adspaces/{id}/media-buying/source/bid | Set the campaign&#39;s bid at the network.
[**api_v1_adspaces_id_media_buying_source_retry_post**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_source_retry_post) | **POST** /api/v1/adspaces/{id}/media-buying/source/retry | Retry the connection to the source campaign.
[**api_v1_adspaces_id_media_buying_targeting_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_get) | **GET** /api/v1/adspaces/{id}/media-buying/targeting | The campaign&#39;s placement targeting (all, or an allow-list).
[**api_v1_adspaces_id_media_buying_targeting_put**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_put) | **PUT** /api/v1/adspaces/{id}/media-buying/targeting | Switch to / edit the allow-list, or back to all placements.
[**api_v1_adspaces_id_media_buying_targeting_suggest_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_targeting_suggest_get) | **GET** /api/v1/adspaces/{id}/media-buying/targeting/suggest | Suggested allow-list: the profitable placements of the policy window.
[**api_v1_adspaces_id_media_buying_track_record_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_track_record_get) | **GET** /api/v1/adspaces/{id}/media-buying/track-record | Track record: did each change do what it was meant to?
[**api_v1_adspaces_id_media_buying_zones_get**](AgenticMediaBuyingApi.md#api_v1_adspaces_id_media_buying_zones_get) | **GET** /api/v1/adspaces/{id}/media-buying/zones | Source-zone report: revenue against cost per placement.
[**api_v1_media_buying_portfolio_get**](AgenticMediaBuyingApi.md#api_v1_media_buying_portfolio_get) | **GET** /api/v1/media-buying/portfolio | Every buy side by side: margin against target, spend, proposals, the agent&#39;s latest summary.
[**api_v1_tracker_media_buying_portfolio_get**](AgenticMediaBuyingApi.md#api_v1_tracker_media_buying_portfolio_get) | **GET** /api/v1/tracker/media-buying/portfolio | Every buy side by side (tracker accounts — the same overview): margin against target, spend, proposals, the agent&#39;s latest summary.
[**api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/actions/{actionId}/decide | Approve or reject a proposal.
[**api_v1_tracker_tracking_links_id_media_buying_actions_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_actions_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/actions | Activity log: every block, bid, budget and other change, and open proposals.
[**api_v1_tracker_tracking_links_id_media_buying_agent_run_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_agent_run_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/agent/run | Run the buying agent now.
[**api_v1_tracker_tracking_links_id_media_buying_agent_runs_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_agent_runs_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/agent/runs | The buying agent&#39;s recent runs with their summaries and proposals.
[**api_v1_tracker_tracking_links_id_media_buying_block_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_block_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/block | Block or unblock one source zone at the network.
[**api_v1_tracker_tracking_links_id_media_buying_compare_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_compare_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/compare | Compare with another buy (A/B, e.g. against a control left to the network&#39;s own optimiser).
[**api_v1_tracker_tracking_links_id_media_buying_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying | Overview: the connected network, what it supports, the policy and open proposals.
[**api_v1_tracker_tracking_links_id_media_buying_ips_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_ips_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/ips | The IP preblock list: ranges on the network&#39;s exclusion list and proposals.
[**api_v1_tracker_tracking_links_id_media_buying_ips_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_ips_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/ips | Change the IP preblock list.
[**api_v1_tracker_tracking_links_id_media_buying_network_budget_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_network_budget_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/network-budget | The campaign&#39;s daily budget at the network.
[**api_v1_tracker_tracking_links_id_media_buying_policy_put**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_policy_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/policy | Save the buying policy (any subset of its fields).
[**api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/policy/suggest | Suggested policy from the zone&#39;s own traffic, with a reason per field.
[**api_v1_tracker_tracking_links_id_media_buying_report_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_report_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/report | Send the media buying report now.
[**api_v1_tracker_tracking_links_id_media_buying_segments_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_segments_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/segments | Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
[**api_v1_tracker_tracking_links_id_media_buying_source_bid_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_bid_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/source/bid | The campaign&#39;s current bid at the network.
[**api_v1_tracker_tracking_links_id_media_buying_source_bid_put**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_bid_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/source/bid | Set the campaign&#39;s bid at the network.
[**api_v1_tracker_tracking_links_id_media_buying_source_retry_post**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_source_retry_post) | **POST** /api/v1/tracker/tracking-links/{id}/media-buying/source/retry | Retry the connection to the source campaign.
[**api_v1_tracker_tracking_links_id_media_buying_targeting_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/targeting | The campaign&#39;s placement targeting (all, or an allow-list).
[**api_v1_tracker_tracking_links_id_media_buying_targeting_put**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_put) | **PUT** /api/v1/tracker/tracking-links/{id}/media-buying/targeting | Switch to / edit the allow-list, or back to all placements.
[**api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/targeting/suggest | Suggested allow-list: the profitable placements of the policy window.
[**api_v1_tracker_tracking_links_id_media_buying_track_record_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_track_record_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/track-record | Track record: did each change do what it was meant to?
[**api_v1_tracker_tracking_links_id_media_buying_zones_get**](AgenticMediaBuyingApi.md#api_v1_tracker_tracking_links_id_media_buying_zones_get) | **GET** /api/v1/tracker/tracking-links/{id}/media-buying/zones | Source-zone report: revenue against cost per placement.


# **api_v1_adspaces_id_media_buying_actions_action_id_decide_post**
> api_v1_adspaces_id_media_buying_actions_action_id_decide_post(id, action_id, api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request)

Approve or reject a proposal.

Approving carries the proposal out at the network (a block, a bid, a budget, a segment exclusion). Approving an `expand_country` proposal (ad zones only) duplicates the ad zone — linked campaigns, own ads, settings, buying policy — and launches its own network campaign for that one country at the proposed bid and test budget, with the source zone's quality blocks as its blacklist; answers `{id, action, status, zone_id, new_spaceid, launch}`; a failure removes the duplicate again (422).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request import ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    action_id = 56 # int | The proposal id from the activity log.
    api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request = goadserver.ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest() # ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest | 

    try:
        # Approve or reject a proposal.
        api_instance.api_v1_adspaces_id_media_buying_actions_action_id_decide_post(id, action_id, api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_actions_action_id_decide_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **action_id** | **int**| The proposal id from the activity log. | 
 **api_v1_adspaces_id_media_buying_actions_action_id_decide_post_request** | [**ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest**](ApiV1AdspacesIdMediaBuyingActionsActionIdDecidePostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_actions_get**
> api_v1_adspaces_id_media_buying_actions_get(id, status=status, actor=actor, action=action, zone=zone, var_from=var_from, to=to, limit=limit, format=format)

Activity log: every block, bid, budget and other change, and open proposals.

Newest first. A `bid_change` on a network with a bid per country carries `metrics.countries` [{country, pct, old, new, margin, cost, revenue}].

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    status = 'status_example' # str | `proposed` | `applied` | `rejected` | `failed` | `expired`. (optional)
    actor = 'actor_example' # str | `policy` | `agent` | `advertiser` | `manual` | `inherited`. (optional)
    action = 'action_example' # str | e.g. `block`, `unblock`, `zone_bid`, `bid_change`, `net_budget`, `exclude_segment`, `expand_country`, `ip_block`, `report`. (optional)
    zone = 'zone_example' # str | One source zone id. (optional)
    var_from = 'var_from_example' # str | YYYY-MM-DD. (optional)
    to = 'to_example' # str | YYYY-MM-DD. (optional)
    limit = 56 # int | 1-1000, default 200. (optional)
    format = 'format_example' # str | `csv` for a CSV download (up to 5000 rows). (optional)

    try:
        # Activity log: every block, bid, budget and other change, and open proposals.
        api_instance.api_v1_adspaces_id_media_buying_actions_get(id, status=status, actor=actor, action=action, zone=zone, var_from=var_from, to=to, limit=limit, format=format)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **status** | **str**| &#x60;proposed&#x60; | &#x60;applied&#x60; | &#x60;rejected&#x60; | &#x60;failed&#x60; | &#x60;expired&#x60;. | [optional] 
 **actor** | **str**| &#x60;policy&#x60; | &#x60;agent&#x60; | &#x60;advertiser&#x60; | &#x60;manual&#x60; | &#x60;inherited&#x60;. | [optional] 
 **action** | **str**| e.g. &#x60;block&#x60;, &#x60;unblock&#x60;, &#x60;zone_bid&#x60;, &#x60;bid_change&#x60;, &#x60;net_budget&#x60;, &#x60;exclude_segment&#x60;, &#x60;expand_country&#x60;, &#x60;ip_block&#x60;, &#x60;report&#x60;. | [optional] 
 **zone** | **str**| One source zone id. | [optional] 
 **var_from** | **str**| YYYY-MM-DD. | [optional] 
 **to** | **str**| YYYY-MM-DD. | [optional] 
 **limit** | **int**| 1-1000, default 200. | [optional] 
 **format** | **str**| &#x60;csv&#x60; for a CSV download (up to 5000 rows). | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_agent_run_post**
> api_v1_adspaces_id_media_buying_agent_run_post(id, body=body)

Run the buying agent now.

At most once per 10 minutes per zone (429 `too_soon`). Refused while the zone is switched off. Returns the new run.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    body = None # object |  (optional)

    try:
        # Run the buying agent now.
        api_instance.api_v1_adspaces_id_media_buying_agent_run_post(id, body=body)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_agent_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **body** | **object**|  | [optional] 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_agent_runs_get**
> api_v1_adspaces_id_media_buying_agent_runs_get(id)

The buying agent's recent runs with their summaries and proposals.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # The buying agent's recent runs with their summaries and proposals.
        api_instance.api_v1_adspaces_id_media_buying_agent_runs_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_agent_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_block_post**
> api_v1_adspaces_id_media_buying_block_post(id, api_v1_adspaces_id_media_buying_block_post_request)

Block or unblock one source zone at the network.

Writes the change to the network campaign right away and logs it as a manual action. 502 when the network refuses.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_block_post_request import ApiV1AdspacesIdMediaBuyingBlockPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_block_post_request = goadserver.ApiV1AdspacesIdMediaBuyingBlockPostRequest() # ApiV1AdspacesIdMediaBuyingBlockPostRequest | 

    try:
        # Block or unblock one source zone at the network.
        api_instance.api_v1_adspaces_id_media_buying_block_post(id, api_v1_adspaces_id_media_buying_block_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_block_post_request** | [**ApiV1AdspacesIdMediaBuyingBlockPostRequest**](ApiV1AdspacesIdMediaBuyingBlockPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_compare_get**
> api_v1_adspaces_id_media_buying_compare_get(id, var_with=var_with, days=days)

Compare with another buy (A/B, e.g. against a control left to the network's own optimiser).

This buy against another of yours over the same days (default: its control — policy `control_for` — or the buy it is the control of). Per buy: revenue, network cost, profit, margin, profit and volume per day, and each day's figures. Verdict: a paired test on the daily margins — `a_better` / `b_better` (a = this buy) only when the mean difference is at least twice its standard error over at least 5 days with revenue on both sides, else `too_close` or `too_little_data`; `note` says it in a sentence. Database only, no network call.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    var_with = 56 # int | The other buy (ad zone or tracking link id); default its control. (optional)
    days = 14 # int | Full days, ending yesterday. (optional) (default to 14)

    try:
        # Compare with another buy (A/B, e.g. against a control left to the network's own optimiser).
        api_instance.api_v1_adspaces_id_media_buying_compare_get(id, var_with=var_with, days=days)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_compare_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **var_with** | **int**| The other buy (ad zone or tracking link id); default its control. | [optional] 
 **days** | **int**| Full days, ending yesterday. | [optional] [default to 14]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60; {days, from, to, currency, a, b, paired_days, margin_diff_pts, margin_diff_se, verdict, note}. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | No buy to compare with, not one of yours, or &#x60;days&#x60; outside 5-90. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_get**
> api_v1_adspaces_id_media_buying_get(id)

Overview: the connected network, what it supports, the policy and open proposals.

Everything the panel shows before the report: network and campaign, capability flags (`supports_*`; `supports_country_bids` = the campaign bid is an absolute bid per country, judged and moved per country), the URL suffix that captures the source zone id (`capture`), the stored `policy`, `pending_proposals`, the source campaign state and `owner_gets_report`. 404 when the ad space is not connected to an external network campaign.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # Overview: the connected network, what it supports, the policy and open proposals.
        api_instance.api_v1_adspaces_id_media_buying_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_ips_get**
> api_v1_adspaces_id_media_buying_ips_get(id)

The IP preblock list: ranges on the network's exclusion list and proposals.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # The IP preblock list: ranges on the network's exclusion list and proposals.
        api_instance.api_v1_adspaces_id_media_buying_ips_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_ips_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_ips_post**
> api_v1_adspaces_id_media_buying_ips_post(id, api_v1_adspaces_id_media_buying_ips_post_request)

Change the IP preblock list.

`add` blocks the given ranges now, `approve` / `reject` decide proposals, `remove` takes ranges off, `refresh` builds the list now (no `cidrs`).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_ips_post_request import ApiV1AdspacesIdMediaBuyingIpsPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_ips_post_request = goadserver.ApiV1AdspacesIdMediaBuyingIpsPostRequest() # ApiV1AdspacesIdMediaBuyingIpsPostRequest | 

    try:
        # Change the IP preblock list.
        api_instance.api_v1_adspaces_id_media_buying_ips_post(id, api_v1_adspaces_id_media_buying_ips_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_ips_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_ips_post_request** | [**ApiV1AdspacesIdMediaBuyingIpsPostRequest**](ApiV1AdspacesIdMediaBuyingIpsPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_launch_get**
> api_v1_adspaces_id_media_buying_launch_get(id, adnetwork_id=adnetwork_id)

What a new campaign can be launched with (unconnected ad zones).

Without `adnetwork_id`: the network accounts that can launch. With it: that network's launch options (formats, countries, minimum bids).

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    adnetwork_id = 56 # int | One of the owner's network accounts. (optional)

    try:
        # What a new campaign can be launched with (unconnected ad zones).
        api_instance.api_v1_adspaces_id_media_buying_launch_get(id, adnetwork_id=adnetwork_id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_launch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **adnetwork_id** | **int**| One of the owner&#39;s network accounts. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_launch_post**
> api_v1_adspaces_id_media_buying_launch_post(id, api_v1_adspaces_id_media_buying_launch_post_request)

Launch a new campaign at the network for this ad zone.

Files the create request; once the network approves it the campaign is connected to the zone (auto pause/activate on).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_launch_post_request import ApiV1AdspacesIdMediaBuyingLaunchPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_launch_post_request = goadserver.ApiV1AdspacesIdMediaBuyingLaunchPostRequest() # ApiV1AdspacesIdMediaBuyingLaunchPostRequest | 

    try:
        # Launch a new campaign at the network for this ad zone.
        api_instance.api_v1_adspaces_id_media_buying_launch_post(id, api_v1_adspaces_id_media_buying_launch_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_launch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_launch_post_request** | [**ApiV1AdspacesIdMediaBuyingLaunchPostRequest**](ApiV1AdspacesIdMediaBuyingLaunchPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_launch_templates_get**
> api_v1_adspaces_id_media_buying_launch_templates_get(id, adnetwork_id=adnetwork_id)

Existing campaigns that can be cloned for a launch.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    adnetwork_id = 56 # int | The network account. (optional)

    try:
        # Existing campaigns that can be cloned for a launch.
        api_instance.api_v1_adspaces_id_media_buying_launch_templates_get(id, adnetwork_id=adnetwork_id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_launch_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **adnetwork_id** | **int**| The network account. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;: &#x60;[{id, name, ad_type, ads}]&#x60;. &#x60;ads&#x60; is the campaign&#39;s ad count, or -1 when the network was too slow to count them all. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_network_budget_get**
> api_v1_adspaces_id_media_buying_network_budget_get(id)

The campaign's daily budget at the network.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # The campaign's daily budget at the network.
        api_instance.api_v1_adspaces_id_media_buying_network_budget_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_network_budget_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_policy_put**
> api_v1_adspaces_id_media_buying_policy_put(id, media_buying_policy)

Save the buying policy (any subset of its fields).

Fields left out keep their stored value. Returns the stored, normalized policy.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.media_buying_policy import MediaBuyingPolicy
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    media_buying_policy = goadserver.MediaBuyingPolicy() # MediaBuyingPolicy | 

    try:
        # Save the buying policy (any subset of its fields).
        api_instance.api_v1_adspaces_id_media_buying_policy_put(id, media_buying_policy)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_policy_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **media_buying_policy** | [**MediaBuyingPolicy**](MediaBuyingPolicy.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_policy_suggest_get**
> api_v1_adspaces_id_media_buying_policy_suggest_get(id, preset=preset)

Suggested policy from the zone's own traffic, with a reason per field.

Nothing is saved. `data.policy` is the full suggested policy; `data.suggestions` lists `{field, value, why}`; with `preset` the preset's own changes follow, each with its reason.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    preset = 'preset_example' # str | On top of the suggestion: conservative (every lever proposes, 95% certainty, twice the minimum cost and traffic, 5% bid steps, at most 20 changes a day), balanced (the suggestion as it is) or aggressive (placement blocks, bids per placement and segment exclusions in auto, the agent in auto, 80% certainty, 15% bid steps). No preset touches the network budget, the campaign bid or the IP preblock. Unknown value: 422. (optional)

    try:
        # Suggested policy from the zone's own traffic, with a reason per field.
        api_instance.api_v1_adspaces_id_media_buying_policy_suggest_get(id, preset=preset)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_policy_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **preset** | **str**| On top of the suggestion: conservative (every lever proposes, 95% certainty, twice the minimum cost and traffic, 5% bid steps, at most 20 changes a day), balanced (the suggestion as it is) or aggressive (placement blocks, bids per placement and segment exclusions in auto, the agent in auto, 80% certainty, 15% bid steps). No preset touches the network budget, the campaign bid or the IP preblock. Unknown value: 422. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_report_post**
> api_v1_adspaces_id_media_buying_report_post(id, api_v1_adspaces_id_media_buying_report_post_request)

Send the media buying report now.

The same report the daily / weekly schedule sends: to the admins' notification event and, where the owner runs the buy (admanager, tracking links), the owner's email and the `media_buying.report` event. Returns the report and where it went.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_report_post_request import ApiV1AdspacesIdMediaBuyingReportPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_report_post_request = goadserver.ApiV1AdspacesIdMediaBuyingReportPostRequest() # ApiV1AdspacesIdMediaBuyingReportPostRequest | 

    try:
        # Send the media buying report now.
        api_instance.api_v1_adspaces_id_media_buying_report_post(id, api_v1_adspaces_id_media_buying_report_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_report_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_report_post_request** | [**ApiV1AdspacesIdMediaBuyingReportPostRequest**](ApiV1AdspacesIdMediaBuyingReportPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_segments_get**
> api_v1_adspaces_id_media_buying_segments_get(id, dim=dim, refresh=refresh)

Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.

`data.cost_basis`: `network` (country / os / hour: the network's exact cost per segment; 400 `not_supported` when the network does not report it), `daily` (weekday: the network's cost per day over 28 days, keys 1 = Monday … 7 = Sunday, `days` per row = how many of that day were charged; judged from 3) or `estimated` (browser / region / carrier / language: the period's cost split by each value's share of the traffic, `cost_estimated: true`; a candidate needs twice `segment_min_spend`). On ExoClick browser and language are `network` (its own cost per value); a row keyed `n:<name>` is cost for a value our stats do not have and is never a candidate. The weekday and estimated dimensions work on every network and are always proposals (never written by `segment_mode` auto); approving a browser or language exclusion on ExoClick or TrafficStars writes it there (`writable: true`; TrafficStars only takes include lists, so it is refused on a campaign that targets every browser / language), every other one is applied by hand.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    dim = 'dim_example' # str | `country` (default where the network reports cost per segment) | `os` | `hour` | `weekday` (default otherwise) | `browser` | `region` | `carrier` | `language`. The overview's `segment_dims` lists the ones this zone has. (optional)
    refresh = 'refresh_example' # str | `1` re-reads the network instead of the cache. (optional)

    try:
        # Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
        api_instance.api_v1_adspaces_id_media_buying_segments_get(id, dim=dim, refresh=refresh)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **dim** | **str**| &#x60;country&#x60; (default where the network reports cost per segment) | &#x60;os&#x60; | &#x60;hour&#x60; | &#x60;weekday&#x60; (default otherwise) | &#x60;browser&#x60; | &#x60;region&#x60; | &#x60;carrier&#x60; | &#x60;language&#x60;. The overview&#39;s &#x60;segment_dims&#x60; lists the ones this zone has. | [optional] 
 **refresh** | **str**| &#x60;1&#x60; re-reads the network instead of the cache. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_source_bid_get**
> api_v1_adspaces_id_media_buying_source_bid_get(id)

The campaign's current bid at the network.

400 `not_supported` when the network does not report bids.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # The campaign's current bid at the network.
        api_instance.api_v1_adspaces_id_media_buying_source_bid_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_source_bid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_source_bid_put**
> api_v1_adspaces_id_media_buying_source_bid_put(id, api_v1_adspaces_id_media_buying_source_bid_put_request)

Set the campaign's bid at the network.

In the network's currency and bid unit.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_source_bid_put_request import ApiV1AdspacesIdMediaBuyingSourceBidPutRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_source_bid_put_request = goadserver.ApiV1AdspacesIdMediaBuyingSourceBidPutRequest() # ApiV1AdspacesIdMediaBuyingSourceBidPutRequest | 

    try:
        # Set the campaign's bid at the network.
        api_instance.api_v1_adspaces_id_media_buying_source_bid_put(id, api_v1_adspaces_id_media_buying_source_bid_put_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_source_bid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_source_bid_put_request** | [**ApiV1AdspacesIdMediaBuyingSourceBidPutRequest**](ApiV1AdspacesIdMediaBuyingSourceBidPutRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_source_retry_post**
> api_v1_adspaces_id_media_buying_source_retry_post(id, body=body)

Retry the connection to the source campaign.

Clears a failed pause/activate state so goadserver tries the network again.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    body = None # object |  (optional)

    try:
        # Retry the connection to the source campaign.
        api_instance.api_v1_adspaces_id_media_buying_source_retry_post(id, body=body)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_source_retry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **body** | **object**|  | [optional] 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_targeting_get**
> api_v1_adspaces_id_media_buying_targeting_get(id)

The campaign's placement targeting (all, or an allow-list).

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # The campaign's placement targeting (all, or an allow-list).
        api_instance.api_v1_adspaces_id_media_buying_targeting_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_targeting_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_targeting_put**
> api_v1_adspaces_id_media_buying_targeting_put(id, api_v1_adspaces_id_media_buying_targeting_put_request)

Switch to / edit the allow-list, or back to all placements.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_adspaces_id_media_buying_targeting_put_request import ApiV1AdspacesIdMediaBuyingTargetingPutRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    api_v1_adspaces_id_media_buying_targeting_put_request = goadserver.ApiV1AdspacesIdMediaBuyingTargetingPutRequest() # ApiV1AdspacesIdMediaBuyingTargetingPutRequest | 

    try:
        # Switch to / edit the allow-list, or back to all placements.
        api_instance.api_v1_adspaces_id_media_buying_targeting_put(id, api_v1_adspaces_id_media_buying_targeting_put_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_targeting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **api_v1_adspaces_id_media_buying_targeting_put_request** | [**ApiV1AdspacesIdMediaBuyingTargetingPutRequest**](ApiV1AdspacesIdMediaBuyingTargetingPutRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_targeting_suggest_get**
> api_v1_adspaces_id_media_buying_targeting_suggest_get(id)

Suggested allow-list: the profitable placements of the policy window.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # Suggested allow-list: the profitable placements of the policy window.
        api_instance.api_v1_adspaces_id_media_buying_targeting_suggest_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_targeting_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_track_record_get**
> api_v1_adspaces_id_media_buying_track_record_get(id)

Track record: did each change do what it was meant to?

Every change of the last 60 days (blocks, bid per placement, campaign bid, network budget, segment exclusions…) measured on the money: the policy window of full days before the change against the same after it, per lever and actor (`policy` / `agent` / `manual`). Per lever: proposed / approved / rejected / expired / auto / failed counts, measured right / wrong (`no_data` under 0.05 cost a side, `pending` until the after-window is complete, `not_judged` for quality blocks), `right_pct`, `approval_pct`, `profit_per_day` (blocks: the loss stopped per day) and `ready_for_auto` (>= 10 measured and >= 70% right — a hint, no mode is switched); the 20 newest measured actions with their before / after. Cached 15 minutes.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.

    try:
        # Track record: did each change do what it was meant to?
        api_instance.api_v1_adspaces_id_media_buying_track_record_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_track_record_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_adspaces_id_media_buying_zones_get**
> api_v1_adspaces_id_media_buying_zones_get(id, days=days, revenue_metric=revenue_metric)

Source-zone report: revenue against cost per placement.

Per source zone (placement) of the connected campaign over the policy window: cost (exact from the network or estimated), revenue, margin, CPA, traffic, delivery, off-geo share, confidence fields and whether it is blocked.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The ad space id.
    days = 56 # int | Days to report (1-30); default the policy window. (optional)
    revenue_metric = 'revenue_metric_example' # str | `paid` or `earned`; default the policy's. (optional)

    try:
        # Source-zone report: revenue against cost per placement.
        api_instance.api_v1_adspaces_id_media_buying_zones_get(id, days=days, revenue_metric=revenue_metric)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_adspaces_id_media_buying_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ad space id. | 
 **days** | **int**| Days to report (1-30); default the policy window. | [optional] 
 **revenue_metric** | **str**| &#x60;paid&#x60; or &#x60;earned&#x60;; default the policy&#39;s. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_media_buying_portfolio_get**
> api_v1_media_buying_portfolio_get(days=days)

Every buy side by side: margin against target, spend, proposals, the agent's latest summary.

One row per ad zone or tracking link connected to a network campaign (`kind` adzone | tracking_link): network and campaign, the linked campaigns' countries, the policy's modes and target, revenue / network cost / profit / margin over the last `days` full days, cost per day, today's revenue and cost, `status` (losing | below_target | on_target | no_data — worst first), open proposals, last action and the agent's latest summary; plus `totals`. Database only, no network call. A key pinned to ad spaces or sites sees only those.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    days = 7 # int | Full days, ending yesterday. (optional) (default to 7)

    try:
        # Every buy side by side: margin against target, spend, proposals, the agent's latest summary.
        api_instance.api_v1_media_buying_portfolio_get(days=days)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_media_buying_portfolio_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Full days, ending yesterday. | [optional] [default to 7]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60; {days, from, to, currency, buys[], totals, generated}. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Media buying is not available on this account. |  -  |
**422** | &#x60;days&#x60; outside 1-90. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_media_buying_portfolio_get**
> api_v1_tracker_media_buying_portfolio_get(days=days)

Every buy side by side (tracker accounts — the same overview): margin against target, spend, proposals, the agent's latest summary.

One row per ad zone or tracking link connected to a network campaign (`kind` adzone | tracking_link): network and campaign, the linked campaigns' countries, the policy's modes and target, revenue / network cost / profit / margin over the last `days` full days, cost per day, today's revenue and cost, `status` (losing | below_target | on_target | no_data — worst first), open proposals, last action and the agent's latest summary; plus `totals`. Database only, no network call. A key pinned to ad spaces or sites sees only those.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    days = 7 # int | Full days, ending yesterday. (optional) (default to 7)

    try:
        # Every buy side by side (tracker accounts — the same overview): margin against target, spend, proposals, the agent's latest summary.
        api_instance.api_v1_tracker_media_buying_portfolio_get(days=days)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_media_buying_portfolio_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Full days, ending yesterday. | [optional] [default to 7]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60; {days, from, to, currency, buys[], totals, generated}. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Media buying is not available on this account. |  -  |
**422** | &#x60;days&#x60; outside 1-90. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post**
> api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post(id, action_id, api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request)

Approve or reject a proposal.

Approving carries the proposal out at the network (a block, a bid, a budget, a segment exclusion). Approving an `expand_country` proposal (ad zones only) duplicates the ad zone — linked campaigns, own ads, settings, buying policy — and launches its own network campaign for that one country at the proposed bid and test budget, with the source zone's quality blocks as its blacklist; answers `{id, action, status, zone_id, new_spaceid, launch}`; a failure removes the duplicate again (422).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    action_id = 56 # int | The proposal id from the activity log.
    api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest | 

    try:
        # Approve or reject a proposal.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post(id, action_id, api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **action_id** | **int**| The proposal id from the activity log. | 
 **api_v1_tracker_tracking_links_id_media_buying_actions_action_id_decide_post_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingActionsActionIdDecidePostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_actions_get**
> api_v1_tracker_tracking_links_id_media_buying_actions_get(id, status=status, actor=actor, action=action, zone=zone, var_from=var_from, to=to, limit=limit, format=format)

Activity log: every block, bid, budget and other change, and open proposals.

Newest first. A `bid_change` on a network with a bid per country carries `metrics.countries` [{country, pct, old, new, margin, cost, revenue}].

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    status = 'status_example' # str | `proposed` | `applied` | `rejected` | `failed` | `expired`. (optional)
    actor = 'actor_example' # str | `policy` | `agent` | `advertiser` | `manual` | `inherited`. (optional)
    action = 'action_example' # str | e.g. `block`, `unblock`, `zone_bid`, `bid_change`, `net_budget`, `exclude_segment`, `expand_country`, `ip_block`, `report`. (optional)
    zone = 'zone_example' # str | One source zone id. (optional)
    var_from = 'var_from_example' # str | YYYY-MM-DD. (optional)
    to = 'to_example' # str | YYYY-MM-DD. (optional)
    limit = 56 # int | 1-1000, default 200. (optional)
    format = 'format_example' # str | `csv` for a CSV download (up to 5000 rows). (optional)

    try:
        # Activity log: every block, bid, budget and other change, and open proposals.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_actions_get(id, status=status, actor=actor, action=action, zone=zone, var_from=var_from, to=to, limit=limit, format=format)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **status** | **str**| &#x60;proposed&#x60; | &#x60;applied&#x60; | &#x60;rejected&#x60; | &#x60;failed&#x60; | &#x60;expired&#x60;. | [optional] 
 **actor** | **str**| &#x60;policy&#x60; | &#x60;agent&#x60; | &#x60;advertiser&#x60; | &#x60;manual&#x60; | &#x60;inherited&#x60;. | [optional] 
 **action** | **str**| e.g. &#x60;block&#x60;, &#x60;unblock&#x60;, &#x60;zone_bid&#x60;, &#x60;bid_change&#x60;, &#x60;net_budget&#x60;, &#x60;exclude_segment&#x60;, &#x60;expand_country&#x60;, &#x60;ip_block&#x60;, &#x60;report&#x60;. | [optional] 
 **zone** | **str**| One source zone id. | [optional] 
 **var_from** | **str**| YYYY-MM-DD. | [optional] 
 **to** | **str**| YYYY-MM-DD. | [optional] 
 **limit** | **int**| 1-1000, default 200. | [optional] 
 **format** | **str**| &#x60;csv&#x60; for a CSV download (up to 5000 rows). | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_agent_run_post**
> api_v1_tracker_tracking_links_id_media_buying_agent_run_post(id, body=body)

Run the buying agent now.

At most once per 10 minutes per zone (429 `too_soon`). Refused while the zone is switched off. Returns the new run.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    body = None # object |  (optional)

    try:
        # Run the buying agent now.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_agent_run_post(id, body=body)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_agent_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **body** | **object**|  | [optional] 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_agent_runs_get**
> api_v1_tracker_tracking_links_id_media_buying_agent_runs_get(id)

The buying agent's recent runs with their summaries and proposals.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # The buying agent's recent runs with their summaries and proposals.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_agent_runs_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_agent_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_block_post**
> api_v1_tracker_tracking_links_id_media_buying_block_post(id, api_v1_tracker_tracking_links_id_media_buying_block_post_request)

Block or unblock one source zone at the network.

Writes the change to the network campaign right away and logs it as a manual action. 502 when the network refuses.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_block_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    api_v1_tracker_tracking_links_id_media_buying_block_post_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest | 

    try:
        # Block or unblock one source zone at the network.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_block_post(id, api_v1_tracker_tracking_links_id_media_buying_block_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **api_v1_tracker_tracking_links_id_media_buying_block_post_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingBlockPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_compare_get**
> api_v1_tracker_tracking_links_id_media_buying_compare_get(id, var_with=var_with, days=days)

Compare with another buy (A/B, e.g. against a control left to the network's own optimiser).

This buy against another of yours over the same days (default: its control — policy `control_for` — or the buy it is the control of). Per buy: revenue, network cost, profit, margin, profit and volume per day, and each day's figures. Verdict: a paired test on the daily margins — `a_better` / `b_better` (a = this buy) only when the mean difference is at least twice its standard error over at least 5 days with revenue on both sides, else `too_close` or `too_little_data`; `note` says it in a sentence. Database only, no network call.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    var_with = 56 # int | The other buy (ad zone or tracking link id); default its control. (optional)
    days = 14 # int | Full days, ending yesterday. (optional) (default to 14)

    try:
        # Compare with another buy (A/B, e.g. against a control left to the network's own optimiser).
        api_instance.api_v1_tracker_tracking_links_id_media_buying_compare_get(id, var_with=var_with, days=days)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_compare_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **var_with** | **int**| The other buy (ad zone or tracking link id); default its control. | [optional] 
 **days** | **int**| Full days, ending yesterday. | [optional] [default to 14]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60; {days, from, to, currency, a, b, paired_days, margin_diff_pts, margin_diff_se, verdict, note}. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | No buy to compare with, not one of yours, or &#x60;days&#x60; outside 5-90. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_get**
> api_v1_tracker_tracking_links_id_media_buying_get(id)

Overview: the connected network, what it supports, the policy and open proposals.

Everything the panel shows before the report: network and campaign, capability flags (`supports_*`; `supports_country_bids` = the campaign bid is an absolute bid per country, judged and moved per country), the URL suffix that captures the source zone id (`capture`), the stored `policy`, `pending_proposals`, the source campaign state and `owner_gets_report`. 404 when the tracking link is not connected to an external network campaign.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # Overview: the connected network, what it supports, the policy and open proposals.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_ips_get**
> api_v1_tracker_tracking_links_id_media_buying_ips_get(id)

The IP preblock list: ranges on the network's exclusion list and proposals.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # The IP preblock list: ranges on the network's exclusion list and proposals.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_ips_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_ips_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_ips_post**
> api_v1_tracker_tracking_links_id_media_buying_ips_post(id, api_v1_tracker_tracking_links_id_media_buying_ips_post_request)

Change the IP preblock list.

`add` blocks the given ranges now, `approve` / `reject` decide proposals, `remove` takes ranges off, `refresh` builds the list now (no `cidrs`).

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_ips_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    api_v1_tracker_tracking_links_id_media_buying_ips_post_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest | 

    try:
        # Change the IP preblock list.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_ips_post(id, api_v1_tracker_tracking_links_id_media_buying_ips_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_ips_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **api_v1_tracker_tracking_links_id_media_buying_ips_post_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingIpsPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_network_budget_get**
> api_v1_tracker_tracking_links_id_media_buying_network_budget_get(id)

The campaign's daily budget at the network.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # The campaign's daily budget at the network.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_network_budget_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_network_budget_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_policy_put**
> api_v1_tracker_tracking_links_id_media_buying_policy_put(id, media_buying_policy)

Save the buying policy (any subset of its fields).

Fields left out keep their stored value. Returns the stored, normalized policy.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.media_buying_policy import MediaBuyingPolicy
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    media_buying_policy = goadserver.MediaBuyingPolicy() # MediaBuyingPolicy | 

    try:
        # Save the buying policy (any subset of its fields).
        api_instance.api_v1_tracker_tracking_links_id_media_buying_policy_put(id, media_buying_policy)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_policy_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **media_buying_policy** | [**MediaBuyingPolicy**](MediaBuyingPolicy.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get**
> api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get(id, preset=preset)

Suggested policy from the zone's own traffic, with a reason per field.

Nothing is saved. `data.policy` is the full suggested policy; `data.suggestions` lists `{field, value, why}`; with `preset` the preset's own changes follow, each with its reason.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    preset = 'preset_example' # str | On top of the suggestion: conservative (every lever proposes, 95% certainty, twice the minimum cost and traffic, 5% bid steps, at most 20 changes a day), balanced (the suggestion as it is) or aggressive (placement blocks, bids per placement and segment exclusions in auto, the agent in auto, 80% certainty, 15% bid steps). No preset touches the network budget, the campaign bid or the IP preblock. Unknown value: 422. (optional)

    try:
        # Suggested policy from the zone's own traffic, with a reason per field.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get(id, preset=preset)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_policy_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **preset** | **str**| On top of the suggestion: conservative (every lever proposes, 95% certainty, twice the minimum cost and traffic, 5% bid steps, at most 20 changes a day), balanced (the suggestion as it is) or aggressive (placement blocks, bids per placement and segment exclusions in auto, the agent in auto, 80% certainty, 15% bid steps). No preset touches the network budget, the campaign bid or the IP preblock. Unknown value: 422. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_report_post**
> api_v1_tracker_tracking_links_id_media_buying_report_post(id, api_v1_tracker_tracking_links_id_media_buying_report_post_request)

Send the media buying report now.

The same report the daily / weekly schedule sends: to the admins' notification event and, where the owner runs the buy (admanager, tracking links), the owner's email and the `media_buying.report` event. Returns the report and where it went.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_report_post_request import ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    api_v1_tracker_tracking_links_id_media_buying_report_post_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest | 

    try:
        # Send the media buying report now.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_report_post(id, api_v1_tracker_tracking_links_id_media_buying_report_post_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_report_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **api_v1_tracker_tracking_links_id_media_buying_report_post_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingReportPostRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_segments_get**
> api_v1_tracker_tracking_links_id_media_buying_segments_get(id, dim=dim, refresh=refresh)

Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.

`data.cost_basis`: `network` (country / os / hour: the network's exact cost per segment; 400 `not_supported` when the network does not report it), `daily` (weekday: the network's cost per day over 28 days, keys 1 = Monday … 7 = Sunday, `days` per row = how many of that day were charged; judged from 3) or `estimated` (browser / region / carrier / language: the period's cost split by each value's share of the traffic, `cost_estimated: true`; a candidate needs twice `segment_min_spend`). On ExoClick browser and language are `network` (its own cost per value); a row keyed `n:<name>` is cost for a value our stats do not have and is never a candidate. The weekday and estimated dimensions work on every network and are always proposals (never written by `segment_mode` auto); approving a browser or language exclusion on ExoClick or TrafficStars writes it there (`writable: true`; TrafficStars only takes include lists, so it is refused on a campaign that targets every browser / language), every other one is applied by hand.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    dim = 'dim_example' # str | `country` (default where the network reports cost per segment) | `os` | `hour` | `weekday` (default otherwise) | `browser` | `region` | `carrier` | `language`. The overview's `segment_dims` lists the ones this zone has. (optional)
    refresh = 'refresh_example' # str | `1` re-reads the network instead of the cache. (optional)

    try:
        # Cost and revenue per segment: country, OS, hour, day of week, browser, region, carrier, language.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_segments_get(id, dim=dim, refresh=refresh)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **dim** | **str**| &#x60;country&#x60; (default where the network reports cost per segment) | &#x60;os&#x60; | &#x60;hour&#x60; | &#x60;weekday&#x60; (default otherwise) | &#x60;browser&#x60; | &#x60;region&#x60; | &#x60;carrier&#x60; | &#x60;language&#x60;. The overview&#39;s &#x60;segment_dims&#x60; lists the ones this zone has. | [optional] 
 **refresh** | **str**| &#x60;1&#x60; re-reads the network instead of the cache. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_source_bid_get**
> api_v1_tracker_tracking_links_id_media_buying_source_bid_get(id)

The campaign's current bid at the network.

400 `not_supported` when the network does not report bids.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # The campaign's current bid at the network.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_source_bid_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_source_bid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_source_bid_put**
> api_v1_tracker_tracking_links_id_media_buying_source_bid_put(id, api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request)

Set the campaign's bid at the network.

In the network's currency and bid unit.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request import ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest | 

    try:
        # Set the campaign's bid at the network.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_source_bid_put(id, api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_source_bid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **api_v1_tracker_tracking_links_id_media_buying_source_bid_put_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingSourceBidPutRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_source_retry_post**
> api_v1_tracker_tracking_links_id_media_buying_source_retry_post(id, body=body)

Retry the connection to the source campaign.

Clears a failed pause/activate state so goadserver tries the network again.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    body = None # object |  (optional)

    try:
        # Retry the connection to the source campaign.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_source_retry_post(id, body=body)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_source_retry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **body** | **object**|  | [optional] 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_targeting_get**
> api_v1_tracker_tracking_links_id_media_buying_targeting_get(id)

The campaign's placement targeting (all, or an allow-list).

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # The campaign's placement targeting (all, or an allow-list).
        api_instance.api_v1_tracker_tracking_links_id_media_buying_targeting_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_targeting_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_targeting_put**
> api_v1_tracker_tracking_links_id_media_buying_targeting_put(id, api_v1_tracker_tracking_links_id_media_buying_targeting_put_request)

Switch to / edit the allow-list, or back to all placements.

### Example

* Bearer (gas_live_<32 chars>) Authentication (apiKey):

```python
import goadserver
from goadserver.models.api_v1_tracker_tracking_links_id_media_buying_targeting_put_request import ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest
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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    api_v1_tracker_tracking_links_id_media_buying_targeting_put_request = goadserver.ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest() # ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest | 

    try:
        # Switch to / edit the allow-list, or back to all placements.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_targeting_put(id, api_v1_tracker_tracking_links_id_media_buying_targeting_put_request)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_targeting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **api_v1_tracker_tracking_links_id_media_buying_targeting_put_request** | [**ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest**](ApiV1TrackerTrackingLinksIdMediaBuyingTargetingPutRequest.md)|  | 

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
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |
**422** | Validation, or &#x60;unknown_fields&#x60; (API keys). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get**
> api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get(id)

Suggested allow-list: the profitable placements of the policy window.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # Suggested allow-list: the profitable placements of the policy window.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_targeting_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_track_record_get**
> api_v1_tracker_tracking_links_id_media_buying_track_record_get(id)

Track record: did each change do what it was meant to?

Every change of the last 60 days (blocks, bid per placement, campaign bid, network budget, segment exclusions…) measured on the money: the policy window of full days before the change against the same after it, per lever and actor (`policy` / `agent` / `manual`). Per lever: proposed / approved / rejected / expired / auto / failed counts, measured right / wrong (`no_data` under 0.05 cost a side, `pending` until the after-window is complete, `not_judged` for quality blocks), `right_pct`, `approval_pct`, `profit_per_day` (blocks: the loss stopped per day) and `ready_for_auto` (>= 10 measured and >= 70% right — a hint, no mode is switched); the 20 newest measured actions with their before / after. Cached 15 minutes.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.

    try:
        # Track record: did each change do what it was meant to?
        api_instance.api_v1_tracker_tracking_links_id_media_buying_track_record_get(id)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_track_record_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tracker_tracking_links_id_media_buying_zones_get**
> api_v1_tracker_tracking_links_id_media_buying_zones_get(id, days=days, revenue_metric=revenue_metric)

Source-zone report: revenue against cost per placement.

Per source zone (placement) of the connected campaign over the policy window: cost (exact from the network or estimated), revenue, margin, CPA, traffic, delivery, off-geo share, confidence fields and whether it is blocked.

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
    api_instance = goadserver.AgenticMediaBuyingApi(api_client)
    id = 56 # int | The tracking link id.
    days = 56 # int | Days to report (1-30); default the policy window. (optional)
    revenue_metric = 'revenue_metric_example' # str | `paid` or `earned`; default the policy's. (optional)

    try:
        # Source-zone report: revenue against cost per placement.
        api_instance.api_v1_tracker_tracking_links_id_media_buying_zones_get(id, days=days, revenue_metric=revenue_metric)
    except Exception as e:
        print("Exception when calling AgenticMediaBuyingApi->api_v1_tracker_tracking_links_id_media_buying_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The tracking link id. | 
 **days** | **int**| Days to report (1-30); default the policy window. | [optional] 
 **revenue_metric** | **str**| &#x60;paid&#x60; or &#x60;earned&#x60;; default the policy&#39;s. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — &#x60;data&#x60;. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Key lacks the required scope, or IP not in allowlist, or account suspended. |  -  |
**404** | Not found: not yours, not connected to a network campaign, or media buying is not available on this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


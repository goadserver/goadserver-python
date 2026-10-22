"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictBool, StrictBytes, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
from goadserver.models.api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request import ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
from goadserver.models.api_v1_campaigns_get200_response import ApiV1CampaignsGet200Response
from goadserver.models.api_v1_campaigns_mass_delete_post_request import ApiV1CampaignsMassDeletePostRequest
from goadserver.models.api_v1_campaigns_mass_toggle_put_request import ApiV1CampaignsMassTogglePutRequest
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete200_response import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response
from goadserver.models.api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request import ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
from goadserver.models.api_v1_campaigns_ron_id_site_list_site_id_put_request import ApiV1CampaignsRonIdSiteListSiteIdPutRequest
from goadserver.models.api_v1_campaigns_ron_id_zones_get200_response import ApiV1CampaignsRonIdZonesGet200Response
from goadserver.models.api_v1_campaigns_save_categories_put_request import ApiV1CampaignsSaveCategoriesPutRequest
from goadserver.models.api_v1_campaigns_save_tags_put_request import ApiV1CampaignsSaveTagsPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_put_request import ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_csv_import_post200_response import ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_from_pool_post_request import ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_get200_response import ApiV1CampaignsTypeCampaignIdAdsGet200Response
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request import ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request import ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request import ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_post_request import ApiV1CampaignsTypeCampaignIdAdsPostRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_url_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_update_weight_put_request import ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
from goadserver.models.api_v1_campaigns_type_id_active_patch200_response import ApiV1CampaignsTypeIdActivePatch200Response
from goadserver.models.api_v1_campaigns_type_id_active_patch_request import ApiV1CampaignsTypeIdActivePatchRequest
from goadserver.models.api_v1_campaigns_type_id_bids_patch200_response import ApiV1CampaignsTypeIdBidsPatch200Response
from goadserver.models.api_v1_campaigns_type_id_bids_patch_request import ApiV1CampaignsTypeIdBidsPatchRequest
from goadserver.models.api_v1_campaigns_type_id_budget_patch200_response import ApiV1CampaignsTypeIdBudgetPatch200Response
from goadserver.models.api_v1_campaigns_type_id_budget_patch_request import ApiV1CampaignsTypeIdBudgetPatchRequest
from goadserver.models.api_v1_campaigns_type_id_clone_post201_response import ApiV1CampaignsTypeIdClonePost201Response
from goadserver.models.api_v1_campaigns_type_id_clone_post_request import ApiV1CampaignsTypeIdClonePostRequest
from goadserver.models.api_v1_campaigns_type_id_delete200_response import ApiV1CampaignsTypeIdDelete200Response
from goadserver.models.api_v1_campaigns_type_id_filters_get200_response import ApiV1CampaignsTypeIdFiltersGet200Response
from goadserver.models.api_v1_campaigns_type_id_filters_post200_response import ApiV1CampaignsTypeIdFiltersPost200Response
from goadserver.models.api_v1_campaigns_type_id_filters_post_request import ApiV1CampaignsTypeIdFiltersPostRequest
from goadserver.models.api_v1_campaigns_type_id_min_bid_get200_response import ApiV1CampaignsTypeIdMinBidGet200Response
from goadserver.models.api_v1_campaigns_type_id_patch_request import ApiV1CampaignsTypeIdPatchRequest
from goadserver.models.api_v1_campaigns_type_id_zones_post_request import ApiV1CampaignsTypeIdZonesPostRequest
from goadserver.models.api_v1_campaigns_type_id_zones_zone_id_weight_put_request import ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
from goadserver.models.api_v1_campaigns_type_post_request import ApiV1CampaignsTypePostRequest
from goadserver.models.api_v1_campaigns_type_schema_ads_get200_response import ApiV1CampaignsTypeSchemaAdsGet200Response
from goadserver.models.api_v1_campaigns_type_schema_get200_response import ApiV1CampaignsTypeSchemaGet200Response
from goadserver.models.api_v1_rtb_test_rtb_post_request import ApiV1RtbTestRtbPostRequest
from goadserver.models.api_v1_tools_replace_domain_put_request import ApiV1ToolsReplaceDomainPutRequest
from goadserver.models.rtb_test_request import RtbTestRequest
from goadserver.models.rtb_test_result import RtbTestResult

from goadserver.api_client import ApiClient, RequestSerialized
from goadserver.api_response import ApiResponse
from goadserver.rest import RESTResponseType


class CampaignsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_delete(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Remove an ad zone from a CPM campaign.


        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_with_http_info(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Remove an ad zone from a CPM campaign.


        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_without_preload_content(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Remove an ad zone from a CPM campaign.


        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_cpm_campaign_id_spots_space_id_delete_serialize(
        self,
        campaign_id,
        space_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if space_id is not None:
            _path_params['spaceId'] = space_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_post(
        self,
        campaign_id: StrictInt,
        space_id: Annotated[StrictInt, Field(description="Ad zone id.")],
        api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: Optional[ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Add an ad zone to a CPM campaign (or re-price it).

        Adds the zone as a spot of the campaign, or updates the bid when it is already one. `cpm` 0 / omitted takes the zone's minimum CPM; a `cpm` under the minimum is raised to it; a Mini Network peer zone is also raised to the floor its publisher set for you. The zone must be yours or shared with you through an accepted Mini Network pair. Spot activity is recalculated from the campaign's ads. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: Ad zone id. (required)
        :type space_id: int
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request:
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_post_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': None,
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_post_with_http_info(
        self,
        campaign_id: StrictInt,
        space_id: Annotated[StrictInt, Field(description="Ad zone id.")],
        api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: Optional[ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Add an ad zone to a CPM campaign (or re-price it).

        Adds the zone as a spot of the campaign, or updates the bid when it is already one. `cpm` 0 / omitted takes the zone's minimum CPM; a `cpm` under the minimum is raised to it; a Mini Network peer zone is also raised to the floor its publisher set for you. The zone must be yours or shared with you through an accepted Mini Network pair. Spot activity is recalculated from the campaign's ads. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: Ad zone id. (required)
        :type space_id: int
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request:
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_post_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': None,
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_post_without_preload_content(
        self,
        campaign_id: StrictInt,
        space_id: Annotated[StrictInt, Field(description="Ad zone id.")],
        api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: Optional[ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Add an ad zone to a CPM campaign (or re-price it).

        Adds the zone as a spot of the campaign, or updates the bid when it is already one. `cpm` 0 / omitted takes the zone's minimum CPM; a `cpm` under the minimum is raised to it; a Mini Network peer zone is also raised to the floor its publisher set for you. The zone must be yours or shared with you through an accepted Mini Network pair. Spot activity is recalculated from the campaign's ads. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: Ad zone id. (required)
        :type space_id: int
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request:
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_post_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': None,
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_cpm_campaign_id_spots_space_id_post_serialize(
        self,
        campaign_id,
        space_id,
        api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if space_id is not None:
            _path_params['spaceId'] = space_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request is not None:
            _body_params = api_v1_campaigns_cpm_campaign_id_spots_space_id_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_put(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Switch a CPM campaign's zone spot on or off.

        Without a sub-path this toggles the spot's `isinuse`. Use `PUT …/spots/{spaceId}/bidding` to set the bid and `…/state` to set state explicitly. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_put_with_http_info(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Switch a CPM campaign's zone spot on or off.

        Without a sub-path this toggles the spot's `isinuse`. Use `PUT …/spots/{spaceId}/bidding` to set the bid and `…/state` to set state explicitly. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_put_without_preload_content(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Switch a CPM campaign's zone spot on or off.

        Without a sub-path this toggles the spot's `isinuse`. Use `PUT …/spots/{spaceId}/bidding` to set the bid and `…/state` to set state explicitly. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_cpm_campaign_id_spots_space_id_put_serialize(
        self,
        campaign_id,
        space_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if space_id is not None:
            _path_params['spaceId'] = space_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        type: StrictStr,
        api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set a CPM zone spot's bid or state.

        `type=bidding`: `cpm` (cents CPM) > 0 sets the bid, raised to the zone's minimum and any Mini Network floor; `user_bid` defaults to `cpm`. `bid_type` (1 = smart bidding) and `isinuse` (1 on, 0 off) change only when sent.  `type=state`: `state` (-1, 0 or 1) and/or `isinuse`, each only when sent. The state is recalculated from the campaign's ads right after, so it mostly reflects ad availability.  Any other `type` toggles `isinuse` like the plain PUT. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param type: (required)
        :type type: str
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: (required)
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            type=type,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_with_http_info(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        type: StrictStr,
        api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set a CPM zone spot's bid or state.

        `type=bidding`: `cpm` (cents CPM) > 0 sets the bid, raised to the zone's minimum and any Mini Network floor; `user_bid` defaults to `cpm`. `bid_type` (1 = smart bidding) and `isinuse` (1 on, 0 off) change only when sent.  `type=state`: `state` (-1, 0 or 1) and/or `isinuse`, each only when sent. The state is recalculated from the campaign's ads right after, so it mostly reflects ad availability.  Any other `type` toggles `isinuse` like the plain PUT. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param type: (required)
        :type type: str
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: (required)
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            type=type,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_without_preload_content(
        self,
        campaign_id: StrictInt,
        space_id: StrictInt,
        type: StrictStr,
        api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set a CPM zone spot's bid or state.

        `type=bidding`: `cpm` (cents CPM) > 0 sets the bid, raised to the zone's minimum and any Mini Network floor; `user_bid` defaults to `cpm`. `bid_type` (1 = smart bidding) and `isinuse` (1 on, 0 off) change only when sent.  `type=state`: `state` (-1, 0 or 1) and/or `isinuse`, each only when sent. The state is recalculated from the campaign's ads right after, so it mostly reflects ad availability.  Any other `type` toggles `isinuse` like the plain PUT. Same handler as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param space_id: (required)
        :type space_id: int
        :param type: (required)
        :type type: str
        :param api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: (required)
        :type api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request: ApiV1CampaignsCpmCampaignIdSpotsSpaceIdTypePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_serialize(
            campaign_id=campaign_id,
            space_id=space_id,
            type=type,
            api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request=api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_serialize(
        self,
        campaign_id,
        space_id,
        type,
        api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if space_id is not None:
            _path_params['spaceId'] = space_id
        if type is not None:
            _path_params['type'] = type
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request is not None:
            _body_params = api_v1_campaigns_cpm_campaign_id_spots_space_id_type_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/cpm/{campaignId}/spots/{spaceId}/{type}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_get(
        self,
        type: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictBool], Field(description="true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.")] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        fields: Annotated[Optional[StrictStr], Field(description="CSV of fields to return; `*` returns everything available.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsGet200Response:
        """List the caller's campaigns across all types (or one type).

        Returns the caller's campaigns. By default each row carries a rich-but-bounded projection: identity (`id`, `name`, `campaign_type`, `ad_type` + `ad_type_label`, `selling_type`), lifecycle (`is_paused`, `is_active`, `is_deleted`, `is_complete`, `pending_state`), budget in main currency units (`daily_budget`, `total_budget`, `total_spent`, `use_campaign_budget`), impression limits (`use_maxday_impressions` / `maxday_impressions` per day and `use_maxtotal_impressions` / `maxtotal_impressions` for the campaign's lifetime), targeting summary (`countries`, `languages`, `categories`, `device_type_ids`, …), capping, schedule (`use_start_date` / `start_date`, `use_end_date` / `end_date`), linked filter/pool ids, the campaign-form fields of `CampaignPanelFields` the row carries, and timestamps. The list does not read the options column, so option fields other than `priority` (`day_parting`, `av_check`, …) are returned by `GET /api/v1/campaigns/{type}/{id}` only. Spend per day and ad bids are not part of the campaign row — use `/api/v1/stats` and the ad endpoints.  Use `?fields=` to opt in or out of fields:    - `?fields=*` — return **every** column on the underlying     campaign row (70+ fields, type-dependent). Convenient for     AI agents that want the full picture in one call.   - `?fields=name,daily_budget,countries` — narrow to just     those fields. `id` is always included.   - (omitted) — default rich projection above. 

        :param type:
        :type type: str
        :param deleted: true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.
        :type deleted: bool
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param fields: CSV of fields to return; `*` returns everything available.
        :type fields: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_get_serialize(
            type=type,
            deleted=deleted,
            page=page,
            per_page=per_page,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsGet200Response",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_get_with_http_info(
        self,
        type: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictBool], Field(description="true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.")] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        fields: Annotated[Optional[StrictStr], Field(description="CSV of fields to return; `*` returns everything available.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsGet200Response]:
        """List the caller's campaigns across all types (or one type).

        Returns the caller's campaigns. By default each row carries a rich-but-bounded projection: identity (`id`, `name`, `campaign_type`, `ad_type` + `ad_type_label`, `selling_type`), lifecycle (`is_paused`, `is_active`, `is_deleted`, `is_complete`, `pending_state`), budget in main currency units (`daily_budget`, `total_budget`, `total_spent`, `use_campaign_budget`), impression limits (`use_maxday_impressions` / `maxday_impressions` per day and `use_maxtotal_impressions` / `maxtotal_impressions` for the campaign's lifetime), targeting summary (`countries`, `languages`, `categories`, `device_type_ids`, …), capping, schedule (`use_start_date` / `start_date`, `use_end_date` / `end_date`), linked filter/pool ids, the campaign-form fields of `CampaignPanelFields` the row carries, and timestamps. The list does not read the options column, so option fields other than `priority` (`day_parting`, `av_check`, …) are returned by `GET /api/v1/campaigns/{type}/{id}` only. Spend per day and ad bids are not part of the campaign row — use `/api/v1/stats` and the ad endpoints.  Use `?fields=` to opt in or out of fields:    - `?fields=*` — return **every** column on the underlying     campaign row (70+ fields, type-dependent). Convenient for     AI agents that want the full picture in one call.   - `?fields=name,daily_budget,countries` — narrow to just     those fields. `id` is always included.   - (omitted) — default rich projection above. 

        :param type:
        :type type: str
        :param deleted: true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.
        :type deleted: bool
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param fields: CSV of fields to return; `*` returns everything available.
        :type fields: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_get_serialize(
            type=type,
            deleted=deleted,
            page=page,
            per_page=per_page,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsGet200Response",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_get_without_preload_content(
        self,
        type: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictBool], Field(description="true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.")] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        fields: Annotated[Optional[StrictStr], Field(description="CSV of fields to return; `*` returns everything available.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List the caller's campaigns across all types (or one type).

        Returns the caller's campaigns. By default each row carries a rich-but-bounded projection: identity (`id`, `name`, `campaign_type`, `ad_type` + `ad_type_label`, `selling_type`), lifecycle (`is_paused`, `is_active`, `is_deleted`, `is_complete`, `pending_state`), budget in main currency units (`daily_budget`, `total_budget`, `total_spent`, `use_campaign_budget`), impression limits (`use_maxday_impressions` / `maxday_impressions` per day and `use_maxtotal_impressions` / `maxtotal_impressions` for the campaign's lifetime), targeting summary (`countries`, `languages`, `categories`, `device_type_ids`, …), capping, schedule (`use_start_date` / `start_date`, `use_end_date` / `end_date`), linked filter/pool ids, the campaign-form fields of `CampaignPanelFields` the row carries, and timestamps. The list does not read the options column, so option fields other than `priority` (`day_parting`, `av_check`, …) are returned by `GET /api/v1/campaigns/{type}/{id}` only. Spend per day and ad bids are not part of the campaign row — use `/api/v1/stats` and the ad endpoints.  Use `?fields=` to opt in or out of fields:    - `?fields=*` — return **every** column on the underlying     campaign row (70+ fields, type-dependent). Convenient for     AI agents that want the full picture in one call.   - `?fields=name,daily_budget,countries` — narrow to just     those fields. `id` is always included.   - (omitted) — default rich projection above. 

        :param type:
        :type type: str
        :param deleted: true / 1 = list the soft-deleted campaigns instead (the panel's Deleted view); restore them with POST /api/v1/campaigns/mass-undelete.
        :type deleted: bool
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param fields: CSV of fields to return; `*` returns everything available.
        :type fields: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_get_serialize(
            type=type,
            deleted=deleted,
            page=page,
            per_page=per_page,
            fields=fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsGet200Response",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_get_serialize(
        self,
        type,
        deleted,
        page,
        per_page,
        fields,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if type is not None:
            
            _query_params.append(('type', type))
            
        if deleted is not None:
            
            _query_params.append(('deleted', deleted))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if fields is not None:
            
            _query_params.append(('fields', fields))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_mass_delete_post(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Soft-delete many campaigns.

        Marks every listed campaign you own deleted (`isdeleted = 1`; flat deals and direct deals: `iscancelled = 1`). Their live ads are soft-deleted with them (marked as deleted-with-the-campaign), and `POST /api/v1/campaigns/mass-undelete` brings the campaigns and those ads back exactly as they were. A ron flat campaign's pending marketplace flat-deal request is cancelled. Unlike the single `DELETE /api/v1/campaigns/{type}/{id}` this does not refuse a flat campaign with a live deal. Same handler as the panel. On a network that reviews campaign deletes, live ron campaigns go to Pending Delete instead and keep running until approved: `affected` counts what was deleted, `pending_review` what was sent for approval. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_delete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_mass_delete_post_with_http_info(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Soft-delete many campaigns.

        Marks every listed campaign you own deleted (`isdeleted = 1`; flat deals and direct deals: `iscancelled = 1`). Their live ads are soft-deleted with them (marked as deleted-with-the-campaign), and `POST /api/v1/campaigns/mass-undelete` brings the campaigns and those ads back exactly as they were. A ron flat campaign's pending marketplace flat-deal request is cancelled. Unlike the single `DELETE /api/v1/campaigns/{type}/{id}` this does not refuse a flat campaign with a live deal. Same handler as the panel. On a network that reviews campaign deletes, live ron campaigns go to Pending Delete instead and keep running until approved: `affected` counts what was deleted, `pending_review` what was sent for approval. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_delete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_mass_delete_post_without_preload_content(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Soft-delete many campaigns.

        Marks every listed campaign you own deleted (`isdeleted = 1`; flat deals and direct deals: `iscancelled = 1`). Their live ads are soft-deleted with them (marked as deleted-with-the-campaign), and `POST /api/v1/campaigns/mass-undelete` brings the campaigns and those ads back exactly as they were. A ron flat campaign's pending marketplace flat-deal request is cancelled. Unlike the single `DELETE /api/v1/campaigns/{type}/{id}` this does not refuse a flat campaign with a live deal. Same handler as the panel. On a network that reviews campaign deletes, live ron campaigns go to Pending Delete instead and keep running until approved: `affected` counts what was deleted, `pending_review` what was sent for approval. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_delete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_mass_delete_post_serialize(
        self,
        api_v1_campaigns_mass_delete_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_mass_delete_post_request is not None:
            _body_params = api_v1_campaigns_mass_delete_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/mass-delete',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_mass_toggle_put(
        self,
        api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Pause or resume many campaigns at once.

        Writes `ispaused` for every listed campaign you own. Same handler as the panel's bulk Pause / Resume buttons, and like them it skips the per-campaign checks `PATCH …/{id}/active` makes (flat-deal rules, lifetime-budget cap): a campaign resumed here that is at its budget cap pauses itself again within about a minute. Use `PATCH /api/v1/campaigns/{type}/{id}/active` when you want those checks. 

        :param api_v1_campaigns_mass_toggle_put_request: (required)
        :type api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_toggle_put_serialize(
            api_v1_campaigns_mass_toggle_put_request=api_v1_campaigns_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_mass_toggle_put_with_http_info(
        self,
        api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Pause or resume many campaigns at once.

        Writes `ispaused` for every listed campaign you own. Same handler as the panel's bulk Pause / Resume buttons, and like them it skips the per-campaign checks `PATCH …/{id}/active` makes (flat-deal rules, lifetime-budget cap): a campaign resumed here that is at its budget cap pauses itself again within about a minute. Use `PATCH /api/v1/campaigns/{type}/{id}/active` when you want those checks. 

        :param api_v1_campaigns_mass_toggle_put_request: (required)
        :type api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_toggle_put_serialize(
            api_v1_campaigns_mass_toggle_put_request=api_v1_campaigns_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_mass_toggle_put_without_preload_content(
        self,
        api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Pause or resume many campaigns at once.

        Writes `ispaused` for every listed campaign you own. Same handler as the panel's bulk Pause / Resume buttons, and like them it skips the per-campaign checks `PATCH …/{id}/active` makes (flat-deal rules, lifetime-budget cap): a campaign resumed here that is at its budget cap pauses itself again within about a minute. Use `PATCH /api/v1/campaigns/{type}/{id}/active` when you want those checks. 

        :param api_v1_campaigns_mass_toggle_put_request: (required)
        :type api_v1_campaigns_mass_toggle_put_request: ApiV1CampaignsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_toggle_put_serialize(
            api_v1_campaigns_mass_toggle_put_request=api_v1_campaigns_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_mass_toggle_put_serialize(
        self,
        api_v1_campaigns_mass_toggle_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_mass_toggle_put_request is not None:
            _body_params = api_v1_campaigns_mass_toggle_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/mass-toggle',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_mass_undelete_post(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Restore soft-deleted campaigns.

        Undoes a delete: `isdeleted = 0` (flat / direct deals: `iscancelled = 0`) for every listed campaign you own that is currently deleted. This is how a `DELETE /api/v1/campaigns/{type}/{id}` or a `mass-delete` is reversed. Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  The ads the delete took down with the campaign come back too; ads you had deleted one by one before stay deleted. A ron / cpm / rtb campaign returns paused or running as it was before the delete; a flat / direct deal deleted with the single `DELETE` comes back paused (resume it with `PATCH …/{id}/active`). Ads deleted together with a campaign before 2026-10-13 cannot be told apart from ones deleted individually and stay deleted — bring RON ads back with `PUT /api/v1/campaigns/ron/{campaignId}/ads/{adId}/restore` (list them with `GET …/ads?ad_state=3`). A purged campaign cannot be restored. Same handler as the panel. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_undelete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_mass_undelete_post_with_http_info(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Restore soft-deleted campaigns.

        Undoes a delete: `isdeleted = 0` (flat / direct deals: `iscancelled = 0`) for every listed campaign you own that is currently deleted. This is how a `DELETE /api/v1/campaigns/{type}/{id}` or a `mass-delete` is reversed. Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  The ads the delete took down with the campaign come back too; ads you had deleted one by one before stay deleted. A ron / cpm / rtb campaign returns paused or running as it was before the delete; a flat / direct deal deleted with the single `DELETE` comes back paused (resume it with `PATCH …/{id}/active`). Ads deleted together with a campaign before 2026-10-13 cannot be told apart from ones deleted individually and stay deleted — bring RON ads back with `PUT /api/v1/campaigns/ron/{campaignId}/ads/{adId}/restore` (list them with `GET …/ads?ad_state=3`). A purged campaign cannot be restored. Same handler as the panel. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_undelete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_mass_undelete_post_without_preload_content(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restore soft-deleted campaigns.

        Undoes a delete: `isdeleted = 0` (flat / direct deals: `iscancelled = 0`) for every listed campaign you own that is currently deleted. This is how a `DELETE /api/v1/campaigns/{type}/{id}` or a `mass-delete` is reversed. Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  The ads the delete took down with the campaign come back too; ads you had deleted one by one before stay deleted. A ron / cpm / rtb campaign returns paused or running as it was before the delete; a flat / direct deal deleted with the single `DELETE` comes back paused (resume it with `PATCH …/{id}/active`). Ads deleted together with a campaign before 2026-10-13 cannot be told apart from ones deleted individually and stay deleted — bring RON ads back with `PUT /api/v1/campaigns/ron/{campaignId}/ads/{adId}/restore` (list them with `GET …/ads?ad_state=3`). A purged campaign cannot be restored. Same handler as the panel. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_mass_undelete_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_mass_undelete_post_serialize(
        self,
        api_v1_campaigns_mass_delete_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_mass_delete_post_request is not None:
            _body_params = api_v1_campaigns_mass_delete_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/mass-undelete',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_purge_post(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Permanently delete soft-deleted campaigns and their ads.

        Hard-deletes listed campaigns that are already soft-deleted, with their ads. Irreversible — the rows are snapshotted into the action log first, but nothing can restore them. Ids that are not deleted (or not yours) are skipped. Same handler as the panel's Purge. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_purge_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_purge_post_with_http_info(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Permanently delete soft-deleted campaigns and their ads.

        Hard-deletes listed campaigns that are already soft-deleted, with their ads. Irreversible — the rows are snapshotted into the action log first, but nothing can restore them. Ids that are not deleted (or not yours) are skipped. Same handler as the panel's Purge. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_purge_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_purge_post_without_preload_content(
        self,
        api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Permanently delete soft-deleted campaigns and their ads.

        Hard-deletes listed campaigns that are already soft-deleted, with their ads. Irreversible — the rows are snapshotted into the action log first, but nothing can restore them. Ids that are not deleted (or not yours) are skipped. Same handler as the panel's Purge. 

        :param api_v1_campaigns_mass_delete_post_request: (required)
        :type api_v1_campaigns_mass_delete_post_request: ApiV1CampaignsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_purge_post_serialize(
            api_v1_campaigns_mass_delete_post_request=api_v1_campaigns_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_purge_post_serialize(
        self,
        api_v1_campaigns_mass_delete_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_mass_delete_post_request is not None:
            _body_params = api_v1_campaigns_mass_delete_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/purge',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response:
        """List per-zone bid overrides for a RON ad.

        RON ads carry a per-adzone bid map (`bids_per_zone` JSON), letting an advertiser bid different amounts on different publisher zones. This endpoint returns each override enriched with the zone + site names, so an auto-optimiser can correlate ids ↔ human labels in one call.  Empty list if the ad has no overrides — the global ad bid applies to every zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_with_http_info(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response]:
        """List per-zone bid overrides for a RON ad.

        RON ads carry a per-adzone bid map (`bids_per_zone` JSON), letting an advertiser bid different amounts on different publisher zones. This endpoint returns each override enriched with the zone + site names, so an auto-optimiser can correlate ids ↔ human labels in one call.  Empty list if the ad has no overrides — the global ad bid applies to every zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_without_preload_content(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List per-zone bid overrides for a RON ad.

        RON ads carry a per-adzone bid map (`bids_per_zone` JSON), letting an advertiser bid different amounts on different publisher zones. This endpoint returns each override enriched with the zone + site names, so an auto-optimiser can correlate ids ↔ human labels in one call.  Empty list if the ad has no overrides — the global ad bid applies to every zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_get_serialize(
        self,
        campaign_id,
        ad_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response:
        """Replace the per-zone bid overrides on a RON ad.

        Full-replace semantics — any zone NOT in the request body has its override cleared. If you only want to update a few zones, pass the complete current set merged with your changes. Auto-optimisers usually recompute the full bid sheet per cycle so this fits the common loop.  Negative or zero `zone_id` and negative `bid` entries are silently dropped. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_with_http_info(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response]:
        """Replace the per-zone bid overrides on a RON ad.

        Full-replace semantics — any zone NOT in the request body has its override cleared. If you only want to update a few zones, pass the complete current set merged with your changes. Auto-optimisers usually recompute the full bid sheet per cycle so this fits the common loop.  Negative or zero `zone_id` and negative `bid` entries are silently dropped. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_without_preload_content(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Replace the per-zone bid overrides on a RON ad.

        Full-replace semantics — any zone NOT in the request body has its override cleared. If you only want to update a few zones, pass the complete current set merged with your changes. Auto-optimisers usually recompute the full bid sheet per cycle so this fits the common loop.  Negative or zero `zone_id` and negative `bid` entries are silently dropped. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsPut200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_serialize(
        self,
        campaign_id,
        ad_id,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request is not None:
            _body_params = api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response:
        """Clear a single per-zone bid override.

        Removes the override for one zone. The global ad bid takes over again for that zone. Returns 404 if no override exists for the given zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_with_http_info(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response]:
        """Clear a single per-zone bid override.

        Removes the override for one zone. The global ad bid takes over again for that zone. Returns 404 if no override exists for the given zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_without_preload_content(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Clear a single per-zone bid override.

        Removes the override for one zone. The global ad bid takes over again for that zone. Returns 404 if no override exists for the given zone. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZoneIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zone_id_delete_serialize(
        self,
        campaign_id,
        ad_id,
        zone_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        if zone_id is not None:
            _path_params['zoneId'] = zone_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/{zoneId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Switch \"only these zones\" mode for a RON ad's per-zone bids.

        When on, the ad serves **only** on the zones listed in its per-zone bid map (`GET/PUT …/zone-bids`) — the panel's \"only these zones\" switch on the Bids per zone tab. When off (default) the zone bids are overrides and every other zone uses the ad bid. Same write as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_with_http_info(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Switch \"only these zones\" mode for a RON ad's per-zone bids.

        When on, the ad serves **only** on the zones listed in its per-zone bid map (`GET/PUT …/zone-bids`) — the panel's \"only these zones\" switch on the Bids per zone tab. When off (default) the zone bids are overrides and every other zone uses the ad bid. Same write as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_without_preload_content(
        self,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Switch \"only these zones\" mode for a RON ad's per-zone bids.

        When on, the ad serves **only** on the zones listed in its per-zone bid map (`GET/PUT …/zone-bids`) — the panel's \"only these zones\" switch on the Bids per zone tab. When off (default) the zone bids are overrides and every other zone uses the ad bid. Same write as the panel. 

        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: (required)
        :type api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request: ApiV1CampaignsRonCampaignIdAdsAdIdZoneBidsZonesOnlyPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_serialize(
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request=api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_serialize(
        self,
        campaign_id,
        ad_id,
        api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request is not None:
            _body_params = api_v1_campaigns_ron_campaign_id_ads_ad_id_zone_bids_zones_only_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/ron/{campaignId}/ads/{adId}/zone-bids/zones-only',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_id_site_list_get(
        self,
        id: StrictInt,
        main_catid: Optional[StrictInt] = None,
        catids: Annotated[Optional[StrictStr], Field(description="Comma-separated category ids, with main_catid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """The Premium-sites box of a RON campaign.

        The tenant's site list filtered to the campaign's categories, each with this campaign's status (1 active, 0 blocked). Shown only when the tenant switched the Sites box on for your account or for all users; otherwise `visible: false` and an empty `data`. `editable` is false when an admin made this campaign's list read only. Optional `main_catid` + `catids` filter on categories other than the saved ones. Display only — the ad server does not read it. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param main_catid:
        :type main_catid: int
        :param catids: Comma-separated category ids, with main_catid.
        :type catids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_get_serialize(
            id=id,
            main_catid=main_catid,
            catids=catids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_id_site_list_get_with_http_info(
        self,
        id: StrictInt,
        main_catid: Optional[StrictInt] = None,
        catids: Annotated[Optional[StrictStr], Field(description="Comma-separated category ids, with main_catid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """The Premium-sites box of a RON campaign.

        The tenant's site list filtered to the campaign's categories, each with this campaign's status (1 active, 0 blocked). Shown only when the tenant switched the Sites box on for your account or for all users; otherwise `visible: false` and an empty `data`. `editable` is false when an admin made this campaign's list read only. Optional `main_catid` + `catids` filter on categories other than the saved ones. Display only — the ad server does not read it. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param main_catid:
        :type main_catid: int
        :param catids: Comma-separated category ids, with main_catid.
        :type catids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_get_serialize(
            id=id,
            main_catid=main_catid,
            catids=catids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_id_site_list_get_without_preload_content(
        self,
        id: StrictInt,
        main_catid: Optional[StrictInt] = None,
        catids: Annotated[Optional[StrictStr], Field(description="Comma-separated category ids, with main_catid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """The Premium-sites box of a RON campaign.

        The tenant's site list filtered to the campaign's categories, each with this campaign's status (1 active, 0 blocked). Shown only when the tenant switched the Sites box on for your account or for all users; otherwise `visible: false` and an empty `data`. `editable` is false when an admin made this campaign's list read only. Optional `main_catid` + `catids` filter on categories other than the saved ones. Display only — the ad server does not read it. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param main_catid:
        :type main_catid: int
        :param catids: Comma-separated category ids, with main_catid.
        :type catids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_get_serialize(
            id=id,
            main_catid=main_catid,
            catids=catids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_id_site_list_get_serialize(
        self,
        id,
        main_catid,
        catids,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if main_catid is not None:
            
            _query_params.append(('main_catid', main_catid))
            
        if catids is not None:
            
            _query_params.append(('catids', catids))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/ron/{id}/site-list',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_id_site_list_site_id_put(
        self,
        id: StrictInt,
        site_id: StrictInt,
        api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set one site of the Premium-sites box active or blocked.

        `status` 1 = active, 0 = blocked. Refused (403) when the Sites box is not on for you or the campaign's list is read only. Setting a site active needs the tenant's minimum balance for Premium sites (422 with code `premium_sites_min_balance` and `amount`); blocking is always allowed. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param site_id: (required)
        :type site_id: int
        :param api_v1_campaigns_ron_id_site_list_site_id_put_request: (required)
        :type api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_site_id_put_serialize(
            id=id,
            site_id=site_id,
            api_v1_campaigns_ron_id_site_list_site_id_put_request=api_v1_campaigns_ron_id_site_list_site_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_id_site_list_site_id_put_with_http_info(
        self,
        id: StrictInt,
        site_id: StrictInt,
        api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set one site of the Premium-sites box active or blocked.

        `status` 1 = active, 0 = blocked. Refused (403) when the Sites box is not on for you or the campaign's list is read only. Setting a site active needs the tenant's minimum balance for Premium sites (422 with code `premium_sites_min_balance` and `amount`); blocking is always allowed. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param site_id: (required)
        :type site_id: int
        :param api_v1_campaigns_ron_id_site_list_site_id_put_request: (required)
        :type api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_site_id_put_serialize(
            id=id,
            site_id=site_id,
            api_v1_campaigns_ron_id_site_list_site_id_put_request=api_v1_campaigns_ron_id_site_list_site_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_id_site_list_site_id_put_without_preload_content(
        self,
        id: StrictInt,
        site_id: StrictInt,
        api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set one site of the Premium-sites box active or blocked.

        `status` 1 = active, 0 = blocked. Refused (403) when the Sites box is not on for you or the campaign's list is read only. Setting a site active needs the tenant's minimum balance for Premium sites (422 with code `premium_sites_min_balance` and `amount`); blocking is always allowed. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param site_id: (required)
        :type site_id: int
        :param api_v1_campaigns_ron_id_site_list_site_id_put_request: (required)
        :type api_v1_campaigns_ron_id_site_list_site_id_put_request: ApiV1CampaignsRonIdSiteListSiteIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_site_list_site_id_put_serialize(
            id=id,
            site_id=site_id,
            api_v1_campaigns_ron_id_site_list_site_id_put_request=api_v1_campaigns_ron_id_site_list_site_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_id_site_list_site_id_put_serialize(
        self,
        id,
        site_id,
        api_v1_campaigns_ron_id_site_list_site_id_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        if site_id is not None:
            _path_params['siteId'] = site_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_ron_id_site_list_site_id_put_request is not None:
            _body_params = api_v1_campaigns_ron_id_site_list_site_id_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/ron/{id}/site-list/{siteId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_ron_id_zones_get(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsRonIdZonesGet200Response:
        """List the zones a RON campaign is linked to.

        The campaign's whitelist zones, the same list the panel shows on the campaign's Ad Zones step: zone id, zone name, site and the campaign's weight on that zone. The raw id list is also available as `wl_zoneids` on `GET /api/v1/campaigns/ron/{id}?fields=*`. 

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_zones_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonIdZonesGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_ron_id_zones_get_with_http_info(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsRonIdZonesGet200Response]:
        """List the zones a RON campaign is linked to.

        The campaign's whitelist zones, the same list the panel shows on the campaign's Ad Zones step: zone id, zone name, site and the campaign's weight on that zone. The raw id list is also available as `wl_zoneids` on `GET /api/v1/campaigns/ron/{id}?fields=*`. 

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_zones_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonIdZonesGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_ron_id_zones_get_without_preload_content(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List the zones a RON campaign is linked to.

        The campaign's whitelist zones, the same list the panel shows on the campaign's Ad Zones step: zone id, zone name, site and the campaign's weight on that zone. The raw id list is also available as `wl_zoneids` on `GET /api/v1/campaigns/ron/{id}?fields=*`. 

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_ron_id_zones_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsRonIdZonesGet200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_ron_id_zones_get_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/ron/{id}/zones',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_get(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Context for testing an RTB campaign's endpoint.

        The campaign's `request_url`, `rtbtype` and ad type, the network's common banner sizes, and the caller's IP / user agent (the defaults the test sends). Same handler as the panel.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_get_with_http_info(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Context for testing an RTB campaign's endpoint.

        The campaign's `request_url`, `rtbtype` and ad type, the network's common banner sizes, and the caller's IP / user agent (the defaults the test sends). Same handler as the panel.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_get_without_preload_content(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Context for testing an RTB campaign's endpoint.

        The campaign's `request_url`, `rtbtype` and ad type, the network's common banner sizes, and the caller's IP / user agent (the defaults the test sends). Same handler as the panel.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_rtb_id_test_rtb_get_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/rtb/{id}/test-rtb',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_post(
        self,
        id: StrictInt,
        rtb_test_request: Optional[RtbTestRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RtbTestResult:
        """Fire a test bid request at an RTB campaign's endpoint.

        Sends one bid-style request to the campaign's `request_url` (or `override_url`) the way the ad server would — OpenRTB 2.6 POST for `openrtb`, GET with macros for `json` / `json_bidder` / `xml` — and returns what was sent, what came back and a `verdict`: `ok` (a bid), `no_bid`, `http_error`, `network_error`. Only public hosts are reached (private / loopback / metadata addresses are refused with `error_category: blocked_url`). `bidfloor` and `best_price` are in the request's currency units (`currency`, default USD). Nothing is stored. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param rtb_test_request:
        :type rtb_test_request: RtbTestRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_post_serialize(
            id=id,
            rtb_test_request=rtb_test_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_post_with_http_info(
        self,
        id: StrictInt,
        rtb_test_request: Optional[RtbTestRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RtbTestResult]:
        """Fire a test bid request at an RTB campaign's endpoint.

        Sends one bid-style request to the campaign's `request_url` (or `override_url`) the way the ad server would — OpenRTB 2.6 POST for `openrtb`, GET with macros for `json` / `json_bidder` / `xml` — and returns what was sent, what came back and a `verdict`: `ok` (a bid), `no_bid`, `http_error`, `network_error`. Only public hosts are reached (private / loopback / metadata addresses are refused with `error_category: blocked_url`). `bidfloor` and `best_price` are in the request's currency units (`currency`, default USD). Nothing is stored. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param rtb_test_request:
        :type rtb_test_request: RtbTestRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_post_serialize(
            id=id,
            rtb_test_request=rtb_test_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_rtb_id_test_rtb_post_without_preload_content(
        self,
        id: StrictInt,
        rtb_test_request: Optional[RtbTestRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Fire a test bid request at an RTB campaign's endpoint.

        Sends one bid-style request to the campaign's `request_url` (or `override_url`) the way the ad server would — OpenRTB 2.6 POST for `openrtb`, GET with macros for `json` / `json_bidder` / `xml` — and returns what was sent, what came back and a `verdict`: `ok` (a bid), `no_bid`, `http_error`, `network_error`. Only public hosts are reached (private / loopback / metadata addresses are refused with `error_category: blocked_url`). `bidfloor` and `best_price` are in the request's currency units (`currency`, default USD). Nothing is stored. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param rtb_test_request:
        :type rtb_test_request: RtbTestRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_rtb_id_test_rtb_post_serialize(
            id=id,
            rtb_test_request=rtb_test_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_rtb_id_test_rtb_post_serialize(
        self,
        id,
        rtb_test_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if rtb_test_request is not None:
            _body_params = rtb_test_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/rtb/{id}/test-rtb',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_save_categories_put(
        self,
        api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Assign categories to many campaigns.

        Adds the category ids in `categories` (GET /api/v1/lookups/categories) to every listed campaign; `overwrite: true` replaces the campaigns' categories instead. Unknown category ids are dropped; none left → 400 `no_categories`. Same handler as the panel's bulk Categories. 

        :param api_v1_campaigns_save_categories_put_request: (required)
        :type api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_categories_put_serialize(
            api_v1_campaigns_save_categories_put_request=api_v1_campaigns_save_categories_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_save_categories_put_with_http_info(
        self,
        api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Assign categories to many campaigns.

        Adds the category ids in `categories` (GET /api/v1/lookups/categories) to every listed campaign; `overwrite: true` replaces the campaigns' categories instead. Unknown category ids are dropped; none left → 400 `no_categories`. Same handler as the panel's bulk Categories. 

        :param api_v1_campaigns_save_categories_put_request: (required)
        :type api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_categories_put_serialize(
            api_v1_campaigns_save_categories_put_request=api_v1_campaigns_save_categories_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_save_categories_put_without_preload_content(
        self,
        api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Assign categories to many campaigns.

        Adds the category ids in `categories` (GET /api/v1/lookups/categories) to every listed campaign; `overwrite: true` replaces the campaigns' categories instead. Unknown category ids are dropped; none left → 400 `no_categories`. Same handler as the panel's bulk Categories. 

        :param api_v1_campaigns_save_categories_put_request: (required)
        :type api_v1_campaigns_save_categories_put_request: ApiV1CampaignsSaveCategoriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_categories_put_serialize(
            api_v1_campaigns_save_categories_put_request=api_v1_campaigns_save_categories_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_save_categories_put_serialize(
        self,
        api_v1_campaigns_save_categories_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_save_categories_put_request is not None:
            _body_params = api_v1_campaigns_save_categories_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/save-categories',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_save_tags_put(
        self,
        api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Assign tags (campaign groups) to many campaigns.

        Adds the tag ids in `tags` to every listed campaign (`groupid`); with `clear: true` the campaigns' tags are replaced by `tags` (an empty `tags` + `clear: true` removes all). Tag ids come from the campaign tags list. Same handler as the panel's bulk Tags. 

        :param api_v1_campaigns_save_tags_put_request: (required)
        :type api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_tags_put_serialize(
            api_v1_campaigns_save_tags_put_request=api_v1_campaigns_save_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_save_tags_put_with_http_info(
        self,
        api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Assign tags (campaign groups) to many campaigns.

        Adds the tag ids in `tags` to every listed campaign (`groupid`); with `clear: true` the campaigns' tags are replaced by `tags` (an empty `tags` + `clear: true` removes all). Tag ids come from the campaign tags list. Same handler as the panel's bulk Tags. 

        :param api_v1_campaigns_save_tags_put_request: (required)
        :type api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_tags_put_serialize(
            api_v1_campaigns_save_tags_put_request=api_v1_campaigns_save_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_save_tags_put_without_preload_content(
        self,
        api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Assign tags (campaign groups) to many campaigns.

        Adds the tag ids in `tags` to every listed campaign (`groupid`); with `clear: true` the campaigns' tags are replaced by `tags` (an empty `tags` + `clear: true` removes all). Tag ids come from the campaign tags list. Same handler as the panel's bulk Tags. 

        :param api_v1_campaigns_save_tags_put_request: (required)
        :type api_v1_campaigns_save_tags_put_request: ApiV1CampaignsSaveTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_save_tags_put_serialize(
            api_v1_campaigns_save_tags_put_request=api_v1_campaigns_save_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_save_tags_put_serialize(
        self,
        api_v1_campaigns_save_tags_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_save_tags_put_request is not None:
            _body_params = api_v1_campaigns_save_tags_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/save-tags',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response:
        """Pause or unpause a single ad.

        Idempotent set. `active=true` activates the ad, `active=false` pauses it. Useful for granular pause/resume from an optimiser without touching the campaign-level pause state.  Same effect as the panel's ad toggle: the pause/activate notification is sent, CPM zone states are recomputed, and on networks that validate changes to whitelist-zone RON campaigns the change is queued for approval — `pending_validation: true` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response]:
        """Pause or unpause a single ad.

        Idempotent set. `active=true` activates the ad, `active=false` pauses it. Useful for granular pause/resume from an optimiser without touching the campaign-level pause state.  Same effect as the panel's ad toggle: the pause/activate notification is sent, CPM zone states are recomputed, and on networks that validate changes to whitelist-zone RON campaigns the change is queued for approval — `pending_validation: true` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Pause or unpause a single ad.

        Idempotent set. `active=true` activates the ad, `active=false` pauses it. Useful for granular pause/resume from an optimiser without touching the campaign-level pause state.  Same effect as the panel's ad toggle: the pause/activate notification is sent, CPM zone states are recomputed, and on networks that validate changes to whitelist-zone RON campaigns the change is queued for approval — `pending_validation: true` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_active_patch_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        api_v1_campaigns_type_id_active_patch_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_active_patch_request is not None:
            _body_params = api_v1_campaigns_type_id_active_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/active',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response:
        """Set a single ad's bid.

        Updates one ad's bid.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response]:
        """Set a single ad's bid.

        Updates one ad's bid.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set a single ad's bid.

        Updates one ad's bid.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdBidPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_ad_id_bid_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bid',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set per-country bids for a RON ad.

        Replaces the ad's whole per-country bid map (`ronads.bids_per_geo`) — send every country you want to keep; `[]` clears it. A bid of 0 removes that country. On CPC / CPM campaigns the ad server uses the visitor country's bid in place of the ad bid (and skips smart bidding for that impression).  **Unit** — the same contract as the ad `bid` writes, echoed as `bid_unit`:  - `currency` (every key minted normally): the bid is in the   advertiser's own currency, e.g. `0.08`. Stored as sent — this   column is kept in currency units (the ad server multiplies by 100   and converts to the network currency when it loads the ad), the   same as the panel's Bids per country tab. - `raw_cents` (keys on the grandfathered raw-bid contract): send   cents, as for that key's ad bids (`8` = 0.08); divided by 100   before storage.  Per-country bids are not held to the ad format's minimum bid (the panel does not check it either). Codes are two-letter country codes (case-insensitive, stored lowercase). Unknown fields → 422. RON campaigns only (`type` must be `ron`, else 400 `invalid_type`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set per-country bids for a RON ad.

        Replaces the ad's whole per-country bid map (`ronads.bids_per_geo`) — send every country you want to keep; `[]` clears it. A bid of 0 removes that country. On CPC / CPM campaigns the ad server uses the visitor country's bid in place of the ad bid (and skips smart bidding for that impression).  **Unit** — the same contract as the ad `bid` writes, echoed as `bid_unit`:  - `currency` (every key minted normally): the bid is in the   advertiser's own currency, e.g. `0.08`. Stored as sent — this   column is kept in currency units (the ad server multiplies by 100   and converts to the network currency when it loads the ad), the   same as the panel's Bids per country tab. - `raw_cents` (keys on the grandfathered raw-bid contract): send   cents, as for that key's ad bids (`8` = 0.08); divided by 100   before storage.  Per-country bids are not held to the ad format's minimum bid (the panel does not check it either). Codes are two-letter country codes (case-insensitive, stored lowercase). Unknown fields → 422. RON campaigns only (`type` must be `ron`, else 400 `invalid_type`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set per-country bids for a RON ad.

        Replaces the ad's whole per-country bid map (`ronads.bids_per_geo`) — send every country you want to keep; `[]` clears it. A bid of 0 removes that country. On CPC / CPM campaigns the ad server uses the visitor country's bid in place of the ad bid (and skips smart bidding for that impression).  **Unit** — the same contract as the ad `bid` writes, echoed as `bid_unit`:  - `currency` (every key minted normally): the bid is in the   advertiser's own currency, e.g. `0.08`. Stored as sent — this   column is kept in currency units (the ad server multiplies by 100   and converts to the network currency when it loads the ad), the   same as the panel's Bids per country tab. - `raw_cents` (keys on the grandfathered raw-bid contract): send   cents, as for that key's ad bids (`8` = 0.08); divided by 100   before storage.  Per-country bids are not held to the ad format's minimum bid (the panel does not check it either). Codes are two-letter country codes (case-insensitive, stored lowercase). Unknown fields → 422. RON campaigns only (`type` must be `ron`, else 400 `invalid_type`). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdBidsPerGeoPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_ad_id_bids_per_geo_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/bids-per-geo',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response:
        """Clone a single ad within a campaign.

        Duplicates one ad. The clone is attached to the same campaign as the source. Useful for A/B-testing creative variants without rebuilding the whole record from scratch. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response]:
        """Clone a single ad within a campaign.

        Duplicates one ad. The clone is attached to the same campaign as the source. Useful for A/B-testing creative variants without rebuilding the whole record from scratch. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Clone a single ad within a campaign.

        Duplicates one ad. The clone is attached to the same campaign as the source. Useful for A/B-testing creative variants without rebuilding the whole record from scratch. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/clone',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set per-ad country targeting for a RON ad.

        Narrows one ad to a subset of countries (`ronads.countries`). An empty list means the ad runs wherever the campaign runs (the default). Codes are lowercased, de-duplicated and checked against the country table; unknown codes are dropped. The stored list is capped at 255 characters (~85 countries) → 422. Applies to every paytype. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set per-ad country targeting for a RON ad.

        Narrows one ad to a subset of countries (`ronads.countries`). An empty list means the ad runs wherever the campaign runs (the default). Codes are lowercased, de-duplicated and checked against the country table; unknown codes are dropped. The stored list is capped at 255 characters (~85 countries) → 422. Applies to every paytype. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set per-ad country targeting for a RON ad.

        Narrows one ad to a subset of countries (`ronads.countries`). An empty list means the ad runs wherever the campaign runs (the default). Codes are lowercased, de-duplicated and checked against the country table; unknown codes are dropped. The stored list is capped at 255 characters (~85 countries) → 422. Applies to every paytype. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdCountriesPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_ad_id_countries_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/countries',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_delete(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Soft-delete an ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_delete_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_delete_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Soft-delete an ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_delete_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_delete_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Soft-delete an ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_delete_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_delete_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_get(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Show one ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_get_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Show one ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_get_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show one ad.


        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_get_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        var_from: Optional[date] = None,
        to: Optional[date] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Shoppable video — shown and clicks per overlay.

        Per overlay of the ad's video_overlays (index = position in the list): how often it came on screen and how often it was clicked, with the click-through rate in percent. `from` / `to` (YYYY-MM-DD, UTC days, default the last 30 days, at most a year). Overlays removed from the ad since keep their numbers as type `removed`. The clicks are also the ad's own clicks in the normal stats. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param var_from:
        :type var_from: date
        :param to:
        :type to: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        var_from: Optional[date] = None,
        to: Optional[date] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Shoppable video — shown and clicks per overlay.

        Per overlay of the ad's video_overlays (index = position in the list): how often it came on screen and how often it was clicked, with the click-through rate in percent. `from` / `to` (YYYY-MM-DD, UTC days, default the last 30 days, at most a year). Overlays removed from the ad since keep their numbers as type `removed`. The clicks are also the ad's own clicks in the normal stats. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param var_from:
        :type var_from: date
        :param to:
        :type to: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        var_from: Optional[date] = None,
        to: Optional[date] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Shoppable video — shown and clicks per overlay.

        Per overlay of the ad's video_overlays (index = position in the list): how often it came on screen and how often it was clicked, with the click-through rate in percent. `from` / `to` (YYYY-MM-DD, UTC days, default the last 30 days, at most a year). Overlays removed from the ad since keep their numbers as type `removed`. The clicks are also the ad's own clicks in the normal stats. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param var_from:
        :type var_from: date
        :param to:
        :type to: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_overlay_stats_get_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        var_from,
        to,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        if var_from is not None:
            if isinstance(var_from, date):
                _query_params.append(
                    (
                        'from',
                        var_from.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('from', var_from))
            
        if to is not None:
            if isinstance(to, date):
                _query_params.append(
                    (
                        'to',
                        to.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('to', to))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/overlay-stats',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Update an ad.

        Partial update — the same handler the panel's ad form saves through, with the same validation (per-format minimum bid, destination-URL rules, SmartAds `{spaceid}`, html video zones, native SmartAd html-only, creator pool orientation). Send only the fields to change. Accepts JSON or `multipart/form-data` (multipart adds the file inputs `banner_file`, `icon_file`, `image_file`, `video_file`, which replace that creative slot).  Field names are the ad's column names. The create-style names `destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id` are accepted as aliases (the column name wins if both are sent), so a create payload can be reused here.  Which columns exist depends on the campaign type: ron / cpm ads take every field below; flatrate / directdeal ads have no bid / sort / keyword / imptracking / icon / SmartAds columns, and those keys are dropped there. Unknown keys are ignored (not an error). `bansizeid` is locked after create and ignored.  Changing the destination URL (or rebuilding the creative) sends the ad back to review unless your account is auto-validated.  **Creative inputs** (rebuild the `creatives` blob, panel vocabulary): `banner_type` (`creative` / `pool` / `hotlink_image` / `hotlink_video` / `iframe` / `html`) with `creative_id` / `banner_pool_id` / `banner_url` / `banner_iframe_url` / `banner_html`; `image_type` (`creative` / `pool` / `html` / `none`) with `creative_id` / `image_pool_id` / `image_url` / `html_code` + `html_total_items` (`none` = native text-only ad); `video_type` (`url` / `xml` / `html` / `creative` / `pool`) with `video_url` / `html_code` / `creative_id` / `video_pool_id`; `icon_type: creative` + `icon_id` (push icon). Or send `creatives` itself (object, as GET returns it, or a JSON string) to write the blob verbatim. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '413': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Update an ad.

        Partial update — the same handler the panel's ad form saves through, with the same validation (per-format minimum bid, destination-URL rules, SmartAds `{spaceid}`, html video zones, native SmartAd html-only, creator pool orientation). Send only the fields to change. Accepts JSON or `multipart/form-data` (multipart adds the file inputs `banner_file`, `icon_file`, `image_file`, `video_file`, which replace that creative slot).  Field names are the ad's column names. The create-style names `destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id` are accepted as aliases (the column name wins if both are sent), so a create payload can be reused here.  Which columns exist depends on the campaign type: ron / cpm ads take every field below; flatrate / directdeal ads have no bid / sort / keyword / imptracking / icon / SmartAds columns, and those keys are dropped there. Unknown keys are ignored (not an error). `bansizeid` is locked after create and ignored.  Changing the destination URL (or rebuilding the creative) sends the ad back to review unless your account is auto-validated.  **Creative inputs** (rebuild the `creatives` blob, panel vocabulary): `banner_type` (`creative` / `pool` / `hotlink_image` / `hotlink_video` / `iframe` / `html`) with `creative_id` / `banner_pool_id` / `banner_url` / `banner_iframe_url` / `banner_html`; `image_type` (`creative` / `pool` / `html` / `none`) with `creative_id` / `image_pool_id` / `image_url` / `html_code` + `html_total_items` (`none` = native text-only ad); `video_type` (`url` / `xml` / `html` / `creative` / `pool`) with `video_url` / `html_code` / `creative_id` / `video_pool_id`; `icon_type: creative` + `icon_id` (push icon). Or send `creatives` itself (object, as GET returns it, or a JSON string) to write the blob verbatim. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '413': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update an ad.

        Partial update — the same handler the panel's ad form saves through, with the same validation (per-format minimum bid, destination-URL rules, SmartAds `{spaceid}`, html video zones, native SmartAd html-only, creator pool orientation). Send only the fields to change. Accepts JSON or `multipart/form-data` (multipart adds the file inputs `banner_file`, `icon_file`, `image_file`, `video_file`, which replace that creative slot).  Field names are the ad's column names. The create-style names `destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id` are accepted as aliases (the column name wins if both are sent), so a create payload can be reused here.  Which columns exist depends on the campaign type: ron / cpm ads take every field below; flatrate / directdeal ads have no bid / sort / keyword / imptracking / icon / SmartAds columns, and those keys are dropped there. Unknown keys are ignored (not an error). `bansizeid` is locked after create and ignored.  Changing the destination URL (or rebuilding the creative) sends the ad back to review unless your account is auto-validated.  **Creative inputs** (rebuild the `creatives` blob, panel vocabulary): `banner_type` (`creative` / `pool` / `hotlink_image` / `hotlink_video` / `iframe` / `html`) with `creative_id` / `banner_pool_id` / `banner_url` / `banner_iframe_url` / `banner_html`; `image_type` (`creative` / `pool` / `html` / `none`) with `creative_id` / `image_pool_id` / `image_url` / `html_code` + `html_total_items` (`none` = native text-only ad); `video_type` (`url` / `xml` / `html` / `creative` / `pool`) with `video_url` / `html_code` / `creative_id` / `video_pool_id`; `icon_type: creative` + `icon_id` (push icon). Or send `creatives` itself (object, as GET returns it, or a JSON string) to write the blob verbatim. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_ad_id_put_request: ApiV1CampaignsTypeCampaignIdAdsAdIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            api_v1_campaigns_type_campaign_id_ads_ad_id_put_request=api_v1_campaigns_type_campaign_id_ads_ad_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '413': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_put_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        api_v1_campaigns_type_campaign_id_ads_ad_id_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_ad_id_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_ad_id_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Restore a deleted RON ad.

        Undoes a soft delete (`is_deleted = 0`, `pending_state = 0`). The ad comes back in the state it was deleted in. List deleted ads with `GET …/ads?ad_state=3`. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Restore a deleted RON ad.

        Undoes a soft delete (`is_deleted = 0`, `pending_state = 0`). The ad comes back in the state it was deleted in. List deleted ads with `GET …/ads?ad_state=3`. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restore a deleted RON ad.

        Undoes a soft delete (`is_deleted = 0`, `pending_state = 0`). The ad comes back in the state it was deleted in. List deleted ads with `GET …/ads?ad_state=3`. Same handler as the panel. RON campaigns only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_id: (required)
        :type ad_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_id=ad_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_ad_id_restore_put_serialize(
        self,
        type,
        campaign_id,
        ad_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        if ad_id is not None:
            _path_params['adId'] = ad_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/{adId}/restore',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_copy_targets_get(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Campaigns this campaign's ads can be copied into.

        Your live campaigns (other than this one) whose ads share this campaign's ad format: RON and CPM, flat deals and direct deals, RTB alone. Use an `id` as `target_campaign_id` on `…/ads/mass-clone`. Narrowed to a key's campaign pin. Same handler as the panel's Copy to campaign… picker. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_copy_targets_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_copy_targets_get_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Campaigns this campaign's ads can be copied into.

        Your live campaigns (other than this one) whose ads share this campaign's ad format: RON and CPM, flat deals and direct deals, RTB alone. Use an `id` as `target_campaign_id` on `…/ads/mass-clone`. Narrowed to a key's campaign pin. Same handler as the panel's Copy to campaign… picker. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_copy_targets_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_copy_targets_get_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Campaigns this campaign's ads can be copied into.

        Your live campaigns (other than this one) whose ads share this campaign's ad format: RON and CPM, flat deals and direct deals, RTB alone. Use an `id` as `target_campaign_id` on `…/ads/mass-clone`. Narrowed to a key's campaign pin. Same handler as the panel's Copy to campaign… picker. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_copy_targets_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_copy_targets_get_serialize(
        self,
        type,
        campaign_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/copy-targets',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_csv_import_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        file: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        image_column: Optional[StrictStr] = None,
        url_column: Optional[StrictStr] = None,
        name_column: Optional[StrictStr] = None,
        group_column: Annotated[Optional[StrictStr], Field(description="Header to group rows by. Omit for one ad per row. Never guessed.")] = None,
        groups: Annotated[Optional[StrictStr], Field(description="The previous request's `groups` answer, verbatim, when a group spans requests.")] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Existing media-bank folder to file the creatives into. 0/absent = unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder of this name under folder_id and file into it.")] = None,
        folder_per_group: Annotated[Optional[StrictStr], Field(description="Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.")] = None,
        name_prefix: Annotated[Optional[StrictStr], Field(description="Prepended to every ad name, separated by a space.")] = None,
        square_mode: Annotated[Optional[StrictStr], Field(description="How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.")] = None,
        pad_color: Annotated[Optional[StrictStr], Field(description="Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.")] = None,
        crop_square: Annotated[Optional[StrictStr], Field(description="Legacy: 0 = none, anything else = crop. square_mode takes precedence.")] = None,
        set_active: Optional[StrictStr] = None,
        bid: Optional[Union[StrictFloat, StrictInt]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response:
        """Import native ads from a CSV — one ad per row, or one ad per group.

        `multipart/form-data`. Field `file` is a CSV (comma, semicolon or tab separated) with a header row. Each row names an image URL, a destination URL and optionally an ad name; the server fetches the image (public http/https only, max 20 MB), centre-crops it to 1:1 — by default PADDING the whole image onto a square canvas rather than cropping it, since a centre crop on a wide video still routinely removes the subject (`square_mode`) — and creates one native ad. Columns are chosen by header name via `image_column` / `url_column` / `name_column`, or guessed from common names (`image_url`, `thumbnail_url`, `destination_url`, `url`, `name`, ...). At most 100 rows per request; rows not started within 180s are reported as not attempted. Native campaigns only.  With `group_column` set the import switches to GROUPED mode: rows sharing that column's value become ONE ad whose creatives live in a creative pool of their own, each pool item carrying its row's destination URL tail in `url_prefix` so the image and its page stay paired. The ad's destination URL is the group's common base, cut back to the last `/`; rows of a group whose URL shares no base with the rest get their own pool + ad, named `<group> (2)`. Answer `groups` must be echoed back in the next request's `groups` field when a group spans several requests, or it gets a second ad instead of reusing the first. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param file: (required)
        :type file: bytes
        :param image_column:
        :type image_column: str
        :param url_column:
        :type url_column: str
        :param name_column:
        :type name_column: str
        :param group_column: Header to group rows by. Omit for one ad per row. Never guessed.
        :type group_column: str
        :param groups: The previous request's `groups` answer, verbatim, when a group spans requests.
        :type groups: str
        :param folder_id: Existing media-bank folder to file the creatives into. 0/absent = unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder of this name under folder_id and file into it.
        :type folder_name: str
        :param folder_per_group: Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.
        :type folder_per_group: str
        :param name_prefix: Prepended to every ad name, separated by a space.
        :type name_prefix: str
        :param square_mode: How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.
        :type square_mode: str
        :param pad_color: Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.
        :type pad_color: str
        :param crop_square: Legacy: 0 = none, anything else = crop. square_mode takes precedence.
        :type crop_square: str
        :param set_active:
        :type set_active: str
        :param bid:
        :type bid: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_csv_import_post_serialize(
            type=type,
            campaign_id=campaign_id,
            file=file,
            image_column=image_column,
            url_column=url_column,
            name_column=name_column,
            group_column=group_column,
            groups=groups,
            folder_id=folder_id,
            folder_name=folder_name,
            folder_per_group=folder_per_group,
            name_prefix=name_prefix,
            square_mode=square_mode,
            pad_color=pad_color,
            crop_square=crop_square,
            set_active=set_active,
            bid=bid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_csv_import_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        file: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        image_column: Optional[StrictStr] = None,
        url_column: Optional[StrictStr] = None,
        name_column: Optional[StrictStr] = None,
        group_column: Annotated[Optional[StrictStr], Field(description="Header to group rows by. Omit for one ad per row. Never guessed.")] = None,
        groups: Annotated[Optional[StrictStr], Field(description="The previous request's `groups` answer, verbatim, when a group spans requests.")] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Existing media-bank folder to file the creatives into. 0/absent = unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder of this name under folder_id and file into it.")] = None,
        folder_per_group: Annotated[Optional[StrictStr], Field(description="Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.")] = None,
        name_prefix: Annotated[Optional[StrictStr], Field(description="Prepended to every ad name, separated by a space.")] = None,
        square_mode: Annotated[Optional[StrictStr], Field(description="How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.")] = None,
        pad_color: Annotated[Optional[StrictStr], Field(description="Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.")] = None,
        crop_square: Annotated[Optional[StrictStr], Field(description="Legacy: 0 = none, anything else = crop. square_mode takes precedence.")] = None,
        set_active: Optional[StrictStr] = None,
        bid: Optional[Union[StrictFloat, StrictInt]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response]:
        """Import native ads from a CSV — one ad per row, or one ad per group.

        `multipart/form-data`. Field `file` is a CSV (comma, semicolon or tab separated) with a header row. Each row names an image URL, a destination URL and optionally an ad name; the server fetches the image (public http/https only, max 20 MB), centre-crops it to 1:1 — by default PADDING the whole image onto a square canvas rather than cropping it, since a centre crop on a wide video still routinely removes the subject (`square_mode`) — and creates one native ad. Columns are chosen by header name via `image_column` / `url_column` / `name_column`, or guessed from common names (`image_url`, `thumbnail_url`, `destination_url`, `url`, `name`, ...). At most 100 rows per request; rows not started within 180s are reported as not attempted. Native campaigns only.  With `group_column` set the import switches to GROUPED mode: rows sharing that column's value become ONE ad whose creatives live in a creative pool of their own, each pool item carrying its row's destination URL tail in `url_prefix` so the image and its page stay paired. The ad's destination URL is the group's common base, cut back to the last `/`; rows of a group whose URL shares no base with the rest get their own pool + ad, named `<group> (2)`. Answer `groups` must be echoed back in the next request's `groups` field when a group spans several requests, or it gets a second ad instead of reusing the first. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param file: (required)
        :type file: bytes
        :param image_column:
        :type image_column: str
        :param url_column:
        :type url_column: str
        :param name_column:
        :type name_column: str
        :param group_column: Header to group rows by. Omit for one ad per row. Never guessed.
        :type group_column: str
        :param groups: The previous request's `groups` answer, verbatim, when a group spans requests.
        :type groups: str
        :param folder_id: Existing media-bank folder to file the creatives into. 0/absent = unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder of this name under folder_id and file into it.
        :type folder_name: str
        :param folder_per_group: Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.
        :type folder_per_group: str
        :param name_prefix: Prepended to every ad name, separated by a space.
        :type name_prefix: str
        :param square_mode: How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.
        :type square_mode: str
        :param pad_color: Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.
        :type pad_color: str
        :param crop_square: Legacy: 0 = none, anything else = crop. square_mode takes precedence.
        :type crop_square: str
        :param set_active:
        :type set_active: str
        :param bid:
        :type bid: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_csv_import_post_serialize(
            type=type,
            campaign_id=campaign_id,
            file=file,
            image_column=image_column,
            url_column=url_column,
            name_column=name_column,
            group_column=group_column,
            groups=groups,
            folder_id=folder_id,
            folder_name=folder_name,
            folder_per_group=folder_per_group,
            name_prefix=name_prefix,
            square_mode=square_mode,
            pad_color=pad_color,
            crop_square=crop_square,
            set_active=set_active,
            bid=bid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_csv_import_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        file: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        image_column: Optional[StrictStr] = None,
        url_column: Optional[StrictStr] = None,
        name_column: Optional[StrictStr] = None,
        group_column: Annotated[Optional[StrictStr], Field(description="Header to group rows by. Omit for one ad per row. Never guessed.")] = None,
        groups: Annotated[Optional[StrictStr], Field(description="The previous request's `groups` answer, verbatim, when a group spans requests.")] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Existing media-bank folder to file the creatives into. 0/absent = unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder of this name under folder_id and file into it.")] = None,
        folder_per_group: Annotated[Optional[StrictStr], Field(description="Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.")] = None,
        name_prefix: Annotated[Optional[StrictStr], Field(description="Prepended to every ad name, separated by a space.")] = None,
        square_mode: Annotated[Optional[StrictStr], Field(description="How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.")] = None,
        pad_color: Annotated[Optional[StrictStr], Field(description="Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.")] = None,
        crop_square: Annotated[Optional[StrictStr], Field(description="Legacy: 0 = none, anything else = crop. square_mode takes precedence.")] = None,
        set_active: Optional[StrictStr] = None,
        bid: Optional[Union[StrictFloat, StrictInt]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Import native ads from a CSV — one ad per row, or one ad per group.

        `multipart/form-data`. Field `file` is a CSV (comma, semicolon or tab separated) with a header row. Each row names an image URL, a destination URL and optionally an ad name; the server fetches the image (public http/https only, max 20 MB), centre-crops it to 1:1 — by default PADDING the whole image onto a square canvas rather than cropping it, since a centre crop on a wide video still routinely removes the subject (`square_mode`) — and creates one native ad. Columns are chosen by header name via `image_column` / `url_column` / `name_column`, or guessed from common names (`image_url`, `thumbnail_url`, `destination_url`, `url`, `name`, ...). At most 100 rows per request; rows not started within 180s are reported as not attempted. Native campaigns only.  With `group_column` set the import switches to GROUPED mode: rows sharing that column's value become ONE ad whose creatives live in a creative pool of their own, each pool item carrying its row's destination URL tail in `url_prefix` so the image and its page stay paired. The ad's destination URL is the group's common base, cut back to the last `/`; rows of a group whose URL shares no base with the rest get their own pool + ad, named `<group> (2)`. Answer `groups` must be echoed back in the next request's `groups` field when a group spans several requests, or it gets a second ad instead of reusing the first. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param file: (required)
        :type file: bytes
        :param image_column:
        :type image_column: str
        :param url_column:
        :type url_column: str
        :param name_column:
        :type name_column: str
        :param group_column: Header to group rows by. Omit for one ad per row. Never guessed.
        :type group_column: str
        :param groups: The previous request's `groups` answer, verbatim, when a group spans requests.
        :type groups: str
        :param folder_id: Existing media-bank folder to file the creatives into. 0/absent = unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder of this name under folder_id and file into it.
        :type folder_name: str
        :param folder_per_group: Grouped mode only: a subfolder per group that has more than one creative. A one-image group stays in the parent.
        :type folder_per_group: str
        :param name_prefix: Prepended to every ad name, separated by a space.
        :type name_prefix: str
        :param square_mode: How each image is squared. pad keeps the whole image and adds bars; crop keeps the centre square; none leaves it alone.
        :type square_mode: str
        :param pad_color: Bar colour for pad on a source with no alpha. PNG/GIF sources pad transparent instead.
        :type pad_color: str
        :param crop_square: Legacy: 0 = none, anything else = crop. square_mode takes precedence.
        :type crop_square: str
        :param set_active:
        :type set_active: str
        :param bid:
        :type bid: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_csv_import_post_serialize(
            type=type,
            campaign_id=campaign_id,
            file=file,
            image_column=image_column,
            url_column=url_column,
            name_column=name_column,
            group_column=group_column,
            groups=groups,
            folder_id=folder_id,
            folder_name=folder_name,
            folder_per_group=folder_per_group,
            name_prefix=name_prefix,
            square_mode=square_mode,
            pad_color=pad_color,
            crop_square=crop_square,
            set_active=set_active,
            bid=bid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsCsvImportPost200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_csv_import_post_serialize(
        self,
        type,
        campaign_id,
        file,
        image_column,
        url_column,
        name_column,
        group_column,
        groups,
        folder_id,
        folder_name,
        folder_per_group,
        name_prefix,
        square_mode,
        pad_color,
        crop_square,
        set_active,
        bid,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if file is not None:
            _files['file'] = file
        if image_column is not None:
            _form_params.append(('image_column', image_column))
        if url_column is not None:
            _form_params.append(('url_column', url_column))
        if name_column is not None:
            _form_params.append(('name_column', name_column))
        if group_column is not None:
            _form_params.append(('group_column', group_column))
        if groups is not None:
            _form_params.append(('groups', groups))
        if folder_id is not None:
            _form_params.append(('folder_id', folder_id))
        if folder_name is not None:
            _form_params.append(('folder_name', folder_name))
        if folder_per_group is not None:
            _form_params.append(('folder_per_group', folder_per_group))
        if name_prefix is not None:
            _form_params.append(('name_prefix', name_prefix))
        if square_mode is not None:
            _form_params.append(('square_mode', square_mode))
        if pad_color is not None:
            _form_params.append(('pad_color', pad_color))
        if crop_square is not None:
            _form_params.append(('crop_square', crop_square))
        if set_active is not None:
            _form_params.append(('set_active', set_active))
        if bid is not None:
            _form_params.append(('bid', bid))
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/csv-import',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_from_pool_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Create ads from a creative pool.

        A banner pool yields one ad per banner size it holds; a native / creator / video pool yields one ad referencing the whole pool. The pool must be yours and of a flavour the campaign's ad type renders (422 otherwise), and for creator campaigns it must hold creatives of the campaign's orientation.  `bid` uses the same unit contract as the other ad bid writes: **currency units** (the advertiser's currency, e.g. `0.05`), checked against the ad format's minimum bid and converted to the stored cents; keys on the grandfathered raw-bid contract write raw cents. Omit it (or 0) to leave the bid empty. `destinationurl` passes the single-ad checks (format, blocked domains). New ads start unvalidated unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_from_pool_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_from_pool_post_request=api_v1_campaigns_type_campaign_id_ads_from_pool_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_from_pool_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Create ads from a creative pool.

        A banner pool yields one ad per banner size it holds; a native / creator / video pool yields one ad referencing the whole pool. The pool must be yours and of a flavour the campaign's ad type renders (422 otherwise), and for creator campaigns it must hold creatives of the campaign's orientation.  `bid` uses the same unit contract as the other ad bid writes: **currency units** (the advertiser's currency, e.g. `0.05`), checked against the ad format's minimum bid and converted to the stored cents; keys on the grandfathered raw-bid contract write raw cents. Omit it (or 0) to leave the bid empty. `destinationurl` passes the single-ad checks (format, blocked domains). New ads start unvalidated unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_from_pool_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_from_pool_post_request=api_v1_campaigns_type_campaign_id_ads_from_pool_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_from_pool_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create ads from a creative pool.

        A banner pool yields one ad per banner size it holds; a native / creator / video pool yields one ad referencing the whole pool. The pool must be yours and of a flavour the campaign's ad type renders (422 otherwise), and for creator campaigns it must hold creatives of the campaign's orientation.  `bid` uses the same unit contract as the other ad bid writes: **currency units** (the advertiser's currency, e.g. `0.05`), checked against the ad format's minimum bid and converted to the stored cents; keys on the grandfathered raw-bid contract write raw cents. Omit it (or 0) to leave the bid empty. `destinationurl` passes the single-ad checks (format, blocked domains). New ads start unvalidated unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_from_pool_post_request: ApiV1CampaignsTypeCampaignIdAdsFromPoolPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_from_pool_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_from_pool_post_request=api_v1_campaigns_type_campaign_id_ads_from_pool_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_from_pool_post_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_from_pool_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_from_pool_post_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_from_pool_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/from-pool',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_get(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_state: Annotated[Optional[StrictStr], Field(description="1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches the ad id (exact, when numeric), title, destination URL and display URL.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Omit for the panel's order: active first, then by position.")] = None,
        sort_dir: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeCampaignIdAdsGet200Response:
        """List ads on a campaign.

        Returns every ad attached to the campaign (paginated). Each row carries `id`, `bid`, `isactive`, `bansizeid`, the underlying `creatives` JSON (banner/video/native, with file paths and creative_id refs), and lifetime stats from the campaign-side rollup. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_state: 1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.
        :type ad_state: str
        :param search: Matches the ad id (exact, when numeric), title, destination URL and display URL.
        :type search: str
        :param sort_by: Omit for the panel's order: active first, then by position.
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_state=ad_state,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_get_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_state: Annotated[Optional[StrictStr], Field(description="1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches the ad id (exact, when numeric), title, destination URL and display URL.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Omit for the panel's order: active first, then by position.")] = None,
        sort_dir: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeCampaignIdAdsGet200Response]:
        """List ads on a campaign.

        Returns every ad attached to the campaign (paginated). Each row carries `id`, `bid`, `isactive`, `bansizeid`, the underlying `creatives` JSON (banner/video/native, with file paths and creative_id refs), and lifetime stats from the campaign-side rollup. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_state: 1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.
        :type ad_state: str
        :param search: Matches the ad id (exact, when numeric), title, destination URL and display URL.
        :type search: str
        :param sort_by: Omit for the panel's order: active first, then by position.
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_state=ad_state,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_get_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        ad_state: Annotated[Optional[StrictStr], Field(description="1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches the ad id (exact, when numeric), title, destination URL and display URL.")] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="Omit for the panel's order: active first, then by position.")] = None,
        sort_dir: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=100, strict=True)]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List ads on a campaign.

        Returns every ad attached to the campaign (paginated). Each row carries `id`, `bid`, `isactive`, `bansizeid`, the underlying `creatives` JSON (banner/video/native, with file paths and creative_id refs), and lifetime stats from the campaign-side rollup. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param ad_state: 1 = active only, 2 = inactive only, 3 = deleted only. Omit for every ad that isn't deleted.
        :type ad_state: str
        :param search: Matches the ad id (exact, when numeric), title, destination URL and display URL.
        :type search: str
        :param sort_by: Omit for the panel's order: active first, then by position.
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            ad_state=ad_state,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeCampaignIdAdsGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_get_serialize(
        self,
        type,
        campaign_id,
        ad_state,
        search,
        sort_by,
        sort_dir,
        page,
        per_page,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        if ad_state is not None:
            
            _query_params.append(('ad_state', ad_state))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if sort_dir is not None:
            
            _query_params.append(('sort_dir', sort_dir))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_clone_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Copy many ads of a campaign.

        Bulk form of `POST …/ads/{adId}/clone`: each copy keeps every column of its source (including the active state) and starts unvalidated. At most 50 ids per call. An id that fails to copy (not in this campaign, deleted meanwhile) is listed in `failed`; the call fails only when nothing was copied. Same handler as the panel.  `target_campaign_id` copies into another of your campaigns instead (the panel's Mass Actions → Copy to campaign…). The target must be live and take the same ads: RON ↔ CPM, flat deal ↔ direct deal, RTB → RTB — list them with `GET …/ads/copy-targets`. Copies into another campaign keep their title; all copies start unvalidated. A key pinned to campaigns needs the target on its pin too. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request=api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_clone_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Copy many ads of a campaign.

        Bulk form of `POST …/ads/{adId}/clone`: each copy keeps every column of its source (including the active state) and starts unvalidated. At most 50 ids per call. An id that fails to copy (not in this campaign, deleted meanwhile) is listed in `failed`; the call fails only when nothing was copied. Same handler as the panel.  `target_campaign_id` copies into another of your campaigns instead (the panel's Mass Actions → Copy to campaign…). The target must be live and take the same ads: RON ↔ CPM, flat deal ↔ direct deal, RTB → RTB — list them with `GET …/ads/copy-targets`. Copies into another campaign keep their title; all copies start unvalidated. A key pinned to campaigns needs the target on its pin too. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request=api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_clone_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Copy many ads of a campaign.

        Bulk form of `POST …/ads/{adId}/clone`: each copy keeps every column of its source (including the active state) and starts unvalidated. At most 50 ids per call. An id that fails to copy (not in this campaign, deleted meanwhile) is listed in `failed`; the call fails only when nothing was copied. Same handler as the panel.  `target_campaign_id` copies into another of your campaigns instead (the panel's Mass Actions → Copy to campaign…). The target must be live and take the same ads: RON ↔ CPM, flat deal ↔ direct deal, RTB → RTB — list them with `GET …/ads/copy-targets`. Copies into another campaign keep their title; all copies start unvalidated. A key pinned to campaigns needs the target on its pin too. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request: ApiV1CampaignsTypeCampaignIdAdsMassClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_clone_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request=api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_mass_clone_post_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_mass_clone_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/mass-clone',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_delete_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Soft-delete many ads of a campaign.

        Soft delete (`is_deleted = 1`); restore one with `PUT …/ads/{adId}/restore`. Ids outside the campaign are ignored. On tenants that validate connect-campaign changes the deletion is queued for publisher approval; a CPM campaign's zone states are recomputed. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_delete_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request=api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_delete_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Soft-delete many ads of a campaign.

        Soft delete (`is_deleted = 1`); restore one with `PUT …/ads/{adId}/restore`. Ids outside the campaign are ignored. On tenants that validate connect-campaign changes the deletion is queued for publisher approval; a CPM campaign's zone states are recomputed. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_delete_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request=api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_delete_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Soft-delete many ads of a campaign.

        Soft delete (`is_deleted = 1`); restore one with `PUT …/ads/{adId}/restore`. Ids outside the campaign are ignored. On tenants that validate connect-campaign changes the deletion is queued for publisher approval; a CPM campaign's zone states are recomputed. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request: ApiV1CampaignsTypeCampaignIdAdsMassDeletePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_delete_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request=api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_mass_delete_post_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_mass_delete_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/mass-delete',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_toggle_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Activate or pause many ads of a campaign at once.

        The panel's Mass Actions → Activate / Deactivate. `ids` selects ads of this campaign; an empty or missing list means **every** live ad of the campaign. Runs the same steps as the single toggle (`PATCH …/ads/{adId}/active`): on tenants that validate connect-campaign changes the ads are queued for publisher approval, one pause/activate notification is sent for the whole action, and a CPM campaign's zone states are recomputed. Ids outside the campaign are ignored (not counted in `affected`). Same handler as the panel. Unknown body fields → 422 `unknown_fields`. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request=api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Activate or pause many ads of a campaign at once.

        The panel's Mass Actions → Activate / Deactivate. `ids` selects ads of this campaign; an empty or missing list means **every** live ad of the campaign. Runs the same steps as the single toggle (`PATCH …/ads/{adId}/active`): on tenants that validate connect-campaign changes the ads are queued for publisher approval, one pause/activate notification is sent for the whole action, and a CPM campaign's zone states are recomputed. Ids outside the campaign are ignored (not counted in `affected`). Same handler as the panel. Unknown body fields → 422 `unknown_fields`. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request=api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Activate or pause many ads of a campaign at once.

        The panel's Mass Actions → Activate / Deactivate. `ids` selects ads of this campaign; an empty or missing list means **every** live ad of the campaign. Runs the same steps as the single toggle (`PATCH …/ads/{adId}/active`): on tenants that validate connect-campaign changes the ads are queued for publisher approval, one pause/activate notification is sent for the whole action, and a CPM campaign's zone states are recomputed. Ids outside the campaign are ignored (not counted in `affected`). Same handler as the panel. Unknown body fields → 422 `unknown_fields`. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request: ApiV1CampaignsTypeCampaignIdAdsMassTogglePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request=api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_mass_toggle_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/mass-toggle',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_multi_upload_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One creative file per ad (also accepted as files[]).")],
        title: Annotated[Optional[StrictStr], Field(description="Native campaigns only: headline for every ad in the batch. Empty = each file name.")] = None,
        description: Annotated[Optional[StrictStr], Field(description="Native campaigns only: description for every ad in the batch.")] = None,
        use_overlays: Annotated[Optional[StrictStr], Field(description="1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.")] = None,
        clone_per_overlay: Annotated[Optional[StrictStr], Field(description="With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.")] = None,
        overlay: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.")] = None,
        overlays_zip: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Bulk-upload ads — one ad per creative file.

        `multipart/form-data` upload of multiple creative files; the server creates one ad per file on the campaign. Field `files` (repeatable) carries the uploads. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param files: One creative file per ad (also accepted as files[]). (required)
        :type files: List[bytes]
        :param title: Native campaigns only: headline for every ad in the batch. Empty = each file name.
        :type title: str
        :param description: Native campaigns only: description for every ad in the batch.
        :type description: str
        :param use_overlays: 1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.
        :type use_overlays: str
        :param clone_per_overlay: With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.
        :type clone_per_overlay: str
        :param overlay: Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.
        :type overlay: List[bytes]
        :param overlays_zip: ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.
        :type overlays_zip: List[bytes]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_multi_upload_post_serialize(
            type=type,
            campaign_id=campaign_id,
            files=files,
            title=title,
            description=description,
            use_overlays=use_overlays,
            clone_per_overlay=clone_per_overlay,
            overlay=overlay,
            overlays_zip=overlays_zip,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '201': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_multi_upload_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One creative file per ad (also accepted as files[]).")],
        title: Annotated[Optional[StrictStr], Field(description="Native campaigns only: headline for every ad in the batch. Empty = each file name.")] = None,
        description: Annotated[Optional[StrictStr], Field(description="Native campaigns only: description for every ad in the batch.")] = None,
        use_overlays: Annotated[Optional[StrictStr], Field(description="1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.")] = None,
        clone_per_overlay: Annotated[Optional[StrictStr], Field(description="With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.")] = None,
        overlay: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.")] = None,
        overlays_zip: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Bulk-upload ads — one ad per creative file.

        `multipart/form-data` upload of multiple creative files; the server creates one ad per file on the campaign. Field `files` (repeatable) carries the uploads. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param files: One creative file per ad (also accepted as files[]). (required)
        :type files: List[bytes]
        :param title: Native campaigns only: headline for every ad in the batch. Empty = each file name.
        :type title: str
        :param description: Native campaigns only: description for every ad in the batch.
        :type description: str
        :param use_overlays: 1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.
        :type use_overlays: str
        :param clone_per_overlay: With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.
        :type clone_per_overlay: str
        :param overlay: Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.
        :type overlay: List[bytes]
        :param overlays_zip: ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.
        :type overlays_zip: List[bytes]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_multi_upload_post_serialize(
            type=type,
            campaign_id=campaign_id,
            files=files,
            title=title,
            description=description,
            use_overlays=use_overlays,
            clone_per_overlay=clone_per_overlay,
            overlay=overlay,
            overlays_zip=overlays_zip,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '201': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_multi_upload_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One creative file per ad (also accepted as files[]).")],
        title: Annotated[Optional[StrictStr], Field(description="Native campaigns only: headline for every ad in the batch. Empty = each file name.")] = None,
        description: Annotated[Optional[StrictStr], Field(description="Native campaigns only: description for every ad in the batch.")] = None,
        use_overlays: Annotated[Optional[StrictStr], Field(description="1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.")] = None,
        clone_per_overlay: Annotated[Optional[StrictStr], Field(description="With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.")] = None,
        overlay: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.")] = None,
        overlays_zip: Annotated[Optional[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]]], Field(description="ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Bulk-upload ads — one ad per creative file.

        `multipart/form-data` upload of multiple creative files; the server creates one ad per file on the campaign. Field `files` (repeatable) carries the uploads. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param files: One creative file per ad (also accepted as files[]). (required)
        :type files: List[bytes]
        :param title: Native campaigns only: headline for every ad in the batch. Empty = each file name.
        :type title: str
        :param description: Native campaigns only: description for every ad in the batch.
        :type description: str
        :param use_overlays: 1 = composite the PNG overlays sent on `overlay` / `overlays_zip` onto the uploaded images.
        :type use_overlays: str
        :param clone_per_overlay: With use_overlays=1: create one variant per overlay instead of rotating the overlays across the files.
        :type clone_per_overlay: str
        :param overlay: Overlay PNGs (repeatable, also accepted as overlay[]). Order sets the rotation.
        :type overlay: List[bytes]
        :param overlays_zip: ZIP archives of overlay PNGs (repeatable, also overlays_zip[]); entries are used in name order after the loose overlays.
        :type overlays_zip: List[bytes]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_multi_upload_post_serialize(
            type=type,
            campaign_id=campaign_id,
            files=files,
            title=title,
            description=description,
            use_overlays=use_overlays,
            clone_per_overlay=clone_per_overlay,
            overlay=overlay,
            overlays_zip=overlays_zip,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '201': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_multi_upload_post_serialize(
        self,
        type,
        campaign_id,
        files,
        title,
        description,
        use_overlays,
        clone_per_overlay,
        overlay,
        overlays_zip,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'files': 'csv',
            'overlay': 'csv',
            'overlays_zip': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if files is not None:
            _files['files'] = files
        if title is not None:
            _form_params.append(('title', title))
        if description is not None:
            _form_params.append(('description', description))
        if use_overlays is not None:
            _form_params.append(('use_overlays', use_overlays))
        if clone_per_overlay is not None:
            _form_params.append(('clone_per_overlay', clone_per_overlay))
        if overlay is not None:
            _files['overlay'] = overlay
        if overlays_zip is not None:
            _files['overlays_zip'] = overlays_zip
        # process the body parameter



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/multi-upload',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_post(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Create an ad on a campaign (smart-default).

        Creates a new ad attached to the campaign. Two request modes, selected by `Content-Type`:  - **`application/json`** — reference an existing creative   (banner pool, single creative, URL, HTML or a native image);   no file upload. - **`multipart/form-data`** — upload a real creative file   directly: `banner_file` (banner image / HTML5 zip),   `icon_file`, `image_file` (native), or `video_file`,   alongside the text fields (`title`, `bid`,   `destination_url`, …). The server stores the file, creates   the creative row and attaches it — no pre-uploaded   `creative_id` needed.  Required (JSON mode): `title` + `bid` + exactly **one** creative reference (`banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `banner_iframe_url` / `video_url` / `video_pool_id` / `native_image_url` / `image_pool_id` / `html_code`). Push ads add their icon with `icon_id` on top of the image reference. `destination_url` is required unless the creative carries its own URL (popunder/JS, VAST, html video) or you set `url_pool_id`. In multipart mode the uploaded file *is* the creative reference.  **Same validation as the panel.** Both modes run the panel's create checks: the per-format minimum bid, the destination-URL rules (format, blocked domains), the SmartAds `{spaceid}` macro requirement (paytype 4 campaigns), the html-video zone rule (an `html_code` video ad needs a Video Slider / In-page Video zone in the campaign whitelist), native SmartAds html-only, and the creator-pool orientation fit (`image_pool_id` on adtype 22). CPM campaigns get their zone states recomputed after the insert. `creative_id` / `icon_id` must be creatives from your own library.  **Field names.** The create names (`destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id`) and the panel / PUT column names (`destinationurl`, `displayurl`, `previewurl`, `isactive`, `url_poolid`) are both accepted on create and on PUT, so one payload works for both. When both spellings are sent the create name wins here and the column name wins on PUT.  **Native ads (uploading a native creative by URL):**  The canonical field is `native_image_url` — a direct image URL. The native headline/body are taken from `title` + `description`, and `destination_url` is the click target; no creative pool needed. The server saves `creatives = {\"image\": {\"type\": \"url\", \"url\": \"…\"}}`, which is the only shape the panel preview and the goadserver native-ad poll render.  Convenience for callers that don't know the campaign's ad type: on a native campaign (adtypeid 3 / 21 / 22 / 42) a `banner_url`, `banner_pool_id` or `creative_id` is **auto-routed** into `creatives.image.*` using the matching shape — i.e. `banner_url` becomes `{image:{type:url,url:…}}`, `banner_pool_id` becomes `{image:{type:pool,poolid:…}}`, `creative_id` becomes `{image:{type:creative,creative_id:…}}`. Banner-only shapes that have no native equivalent (`banner_html`, `banner_iframe_url`, `video_url`, `video_pool_id`) are rejected with a 422 on native campaigns rather than persisted as an unrenderable row.  New integrations should still send `native_image_url` explicitly — it's the unambiguous, type-correct path.  **Modes:**   - `?dry_run=1` — return the resolved field map + computed     `creatives` JSON without inserting.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_post_request=api_v1_campaigns_type_campaign_id_ads_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '404': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_post_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Create an ad on a campaign (smart-default).

        Creates a new ad attached to the campaign. Two request modes, selected by `Content-Type`:  - **`application/json`** — reference an existing creative   (banner pool, single creative, URL, HTML or a native image);   no file upload. - **`multipart/form-data`** — upload a real creative file   directly: `banner_file` (banner image / HTML5 zip),   `icon_file`, `image_file` (native), or `video_file`,   alongside the text fields (`title`, `bid`,   `destination_url`, …). The server stores the file, creates   the creative row and attaches it — no pre-uploaded   `creative_id` needed.  Required (JSON mode): `title` + `bid` + exactly **one** creative reference (`banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `banner_iframe_url` / `video_url` / `video_pool_id` / `native_image_url` / `image_pool_id` / `html_code`). Push ads add their icon with `icon_id` on top of the image reference. `destination_url` is required unless the creative carries its own URL (popunder/JS, VAST, html video) or you set `url_pool_id`. In multipart mode the uploaded file *is* the creative reference.  **Same validation as the panel.** Both modes run the panel's create checks: the per-format minimum bid, the destination-URL rules (format, blocked domains), the SmartAds `{spaceid}` macro requirement (paytype 4 campaigns), the html-video zone rule (an `html_code` video ad needs a Video Slider / In-page Video zone in the campaign whitelist), native SmartAds html-only, and the creator-pool orientation fit (`image_pool_id` on adtype 22). CPM campaigns get their zone states recomputed after the insert. `creative_id` / `icon_id` must be creatives from your own library.  **Field names.** The create names (`destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id`) and the panel / PUT column names (`destinationurl`, `displayurl`, `previewurl`, `isactive`, `url_poolid`) are both accepted on create and on PUT, so one payload works for both. When both spellings are sent the create name wins here and the column name wins on PUT.  **Native ads (uploading a native creative by URL):**  The canonical field is `native_image_url` — a direct image URL. The native headline/body are taken from `title` + `description`, and `destination_url` is the click target; no creative pool needed. The server saves `creatives = {\"image\": {\"type\": \"url\", \"url\": \"…\"}}`, which is the only shape the panel preview and the goadserver native-ad poll render.  Convenience for callers that don't know the campaign's ad type: on a native campaign (adtypeid 3 / 21 / 22 / 42) a `banner_url`, `banner_pool_id` or `creative_id` is **auto-routed** into `creatives.image.*` using the matching shape — i.e. `banner_url` becomes `{image:{type:url,url:…}}`, `banner_pool_id` becomes `{image:{type:pool,poolid:…}}`, `creative_id` becomes `{image:{type:creative,creative_id:…}}`. Banner-only shapes that have no native equivalent (`banner_html`, `banner_iframe_url`, `video_url`, `video_pool_id`) are rejected with a 422 on native campaigns rather than persisted as an unrenderable row.  New integrations should still send `native_image_url` explicitly — it's the unambiguous, type-correct path.  **Modes:**   - `?dry_run=1` — return the resolved field map + computed     `creatives` JSON without inserting.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_post_request=api_v1_campaigns_type_campaign_id_ads_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '404': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_post_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create an ad on a campaign (smart-default).

        Creates a new ad attached to the campaign. Two request modes, selected by `Content-Type`:  - **`application/json`** — reference an existing creative   (banner pool, single creative, URL, HTML or a native image);   no file upload. - **`multipart/form-data`** — upload a real creative file   directly: `banner_file` (banner image / HTML5 zip),   `icon_file`, `image_file` (native), or `video_file`,   alongside the text fields (`title`, `bid`,   `destination_url`, …). The server stores the file, creates   the creative row and attaches it — no pre-uploaded   `creative_id` needed.  Required (JSON mode): `title` + `bid` + exactly **one** creative reference (`banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `banner_iframe_url` / `video_url` / `video_pool_id` / `native_image_url` / `image_pool_id` / `html_code`). Push ads add their icon with `icon_id` on top of the image reference. `destination_url` is required unless the creative carries its own URL (popunder/JS, VAST, html video) or you set `url_pool_id`. In multipart mode the uploaded file *is* the creative reference.  **Same validation as the panel.** Both modes run the panel's create checks: the per-format minimum bid, the destination-URL rules (format, blocked domains), the SmartAds `{spaceid}` macro requirement (paytype 4 campaigns), the html-video zone rule (an `html_code` video ad needs a Video Slider / In-page Video zone in the campaign whitelist), native SmartAds html-only, and the creator-pool orientation fit (`image_pool_id` on adtype 22). CPM campaigns get their zone states recomputed after the insert. `creative_id` / `icon_id` must be creatives from your own library.  **Field names.** The create names (`destination_url`, `display_url`, `preview_url`, `is_active`, `url_pool_id`) and the panel / PUT column names (`destinationurl`, `displayurl`, `previewurl`, `isactive`, `url_poolid`) are both accepted on create and on PUT, so one payload works for both. When both spellings are sent the create name wins here and the column name wins on PUT.  **Native ads (uploading a native creative by URL):**  The canonical field is `native_image_url` — a direct image URL. The native headline/body are taken from `title` + `description`, and `destination_url` is the click target; no creative pool needed. The server saves `creatives = {\"image\": {\"type\": \"url\", \"url\": \"…\"}}`, which is the only shape the panel preview and the goadserver native-ad poll render.  Convenience for callers that don't know the campaign's ad type: on a native campaign (adtypeid 3 / 21 / 22 / 42) a `banner_url`, `banner_pool_id` or `creative_id` is **auto-routed** into `creatives.image.*` using the matching shape — i.e. `banner_url` becomes `{image:{type:url,url:…}}`, `banner_pool_id` becomes `{image:{type:pool,poolid:…}}`, `creative_id` becomes `{image:{type:creative,creative_id:…}}`. Banner-only shapes that have no native equivalent (`banner_html`, `banner_iframe_url`, `video_url`, `video_pool_id`) are rejected with a 422 on native campaigns rather than persisted as an unrenderable row.  New integrations should still send `native_image_url` explicitly — it's the unambiguous, type-correct path.  **Modes:**   - `?dry_run=1` — return the resolved field map + computed     `creatives` JSON without inserting.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_post_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_post_request: ApiV1CampaignsTypeCampaignIdAdsPostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_post_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_post_request=api_v1_campaigns_type_campaign_id_ads_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '404': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_post_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_post_request,
        dry_run,
        strict,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        if dry_run is not None:
            
            _query_params.append(('dry_run', dry_run))
            
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_post_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_pool_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Point many ads at a different creative pool.

        The panel's bulk \"Change creative pool\". `ids` selects ads (max 200; empty = every ad of the campaign). Give either one `pool_id` for the whole selection or `pool_by_size` (`{bansizeid: poolid}`) for a banner selection running several sizes (it wins when both are sent). Only ads with a pool-shaped slot are touched; `include_unpooled: true` also converts ads that carry their own uploaded / hotlinked creative (that creative reference is replaced). Every target pool must be yours; native / creator pools must fit the campaign's orientation (422 names the mismatch). List the pools a selection can take with the panel picker rules described on the ad schema. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_pool_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Point many ads at a different creative pool.

        The panel's bulk \"Change creative pool\". `ids` selects ads (max 200; empty = every ad of the campaign). Give either one `pool_id` for the whole selection or `pool_by_size` (`{bansizeid: poolid}`) for a banner selection running several sizes (it wins when both are sent). Only ads with a pool-shaped slot are touched; `include_unpooled: true` also converts ads that carry their own uploaded / hotlinked creative (that creative reference is replaced). Every target pool must be yours; native / creator pools must fit the campaign's orientation (422 names the mismatch). List the pools a selection can take with the panel picker rules described on the ad schema. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_pool_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Point many ads at a different creative pool.

        The panel's bulk \"Change creative pool\". `ids` selects ads (max 200; empty = every ad of the campaign). Give either one `pool_id` for the whole selection or `pool_by_size` (`{bansizeid: poolid}`) for a banner selection running several sizes (it wins when both are sent). Only ads with a pool-shaped slot are touched; `include_unpooled: true` also converts ads that carry their own uploaded / hotlinked creative (that creative reference is replaced). Every target pool must be yours; native / creator pools must fit the campaign's orientation (422 names the mismatch). List the pools a selection can take with the panel picker rules described on the ad schema. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdatePoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_update_pool_put_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_update_pool_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_update_pool_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_update_pool_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/update-pool',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_pool_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Point many ads at a URL pool, or detach it.

        The panel's bulk \"Change URL pool\". `pool_id` > 0 attaches that URL pool (it must be yours and hold at least one active URL); `pool_id: 0` detaches, so each ad falls back to its own destination URL — an ad with none stays on its pool and is counted in `no_fallback`. Ads whose creative links itself (html / iframe / VAST / phone) are `skipped`. `ids` max 200, empty = every ad. Changed ads go back to review unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Point many ads at a URL pool, or detach it.

        The panel's bulk \"Change URL pool\". `pool_id` > 0 attaches that URL pool (it must be yours and hold at least one active URL); `pool_id: 0` detaches, so each ad falls back to its own destination URL — an ad with none stays on its pool and is counted in `no_fallback`. Ads whose creative links itself (html / iframe / VAST / phone) are `skipped`. `ids` max 200, empty = every ad. Changed ads go back to review unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Point many ads at a URL pool, or detach it.

        The panel's bulk \"Change URL pool\". `pool_id` > 0 attaches that URL pool (it must be yours and hold at least one active URL); `pool_id: 0` detaches, so each ad falls back to its own destination URL — an ad with none stays on its pool and is counted in `no_fallback`. Ads whose creative links itself (html / iframe / VAST / phone) are `skipped`. `ids` max 200, empty = every ad. Changed ads go back to review unless the account is auto-validated. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPoolPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_update_url_pool_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/update-url-pool',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Rewrite the destination URL of many ads at once.

        The panel's bulk \"Change URL\" action. Two modes:  - `set` (default) — write `url` onto every selected ad. - `replace` — substring find/replace (`find` → `replace`) inside   each ad's own URL, e.g. to move a campaign to a new domain or   tracker id while per-ad paths and macros differ.  `ids` selects ads (max 200); empty = every ad of the campaign. Only ads whose click target is their own destination URL are touched — ads on a URL pool, with a self-linking creative (html / iframe / VAST) or a phone number are reported as `skipped`. Every new URL passes the single-ad checks first (format, blocked domains); one bad URL fails the whole call before anything is written. Changed ads go back to review unless the account is auto-validated. Legacy shape `{adids, destinationurl}` is also accepted. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Rewrite the destination URL of many ads at once.

        The panel's bulk \"Change URL\" action. Two modes:  - `set` (default) — write `url` onto every selected ad. - `replace` — substring find/replace (`find` → `replace`) inside   each ad's own URL, e.g. to move a campaign to a new domain or   tracker id while per-ad paths and macros differ.  `ids` selects ads (max 200); empty = every ad of the campaign. Only ads whose click target is their own destination URL are touched — ads on a URL pool, with a self-linking creative (html / iframe / VAST) or a phone number are reported as `skipped`. Every new URL passes the single-ad checks first (format, blocked domains); one bad URL fails the whole call before anything is written. Changed ads go back to review unless the account is auto-validated. Legacy shape `{adids, destinationurl}` is also accepted. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_url_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Rewrite the destination URL of many ads at once.

        The panel's bulk \"Change URL\" action. Two modes:  - `set` (default) — write `url` onto every selected ad. - `replace` — substring find/replace (`find` → `replace`) inside   each ad's own URL, e.g. to move a campaign to a new domain or   tracker id while per-ad paths and macros differ.  `ids` selects ads (max 200); empty = every ad of the campaign. Only ads whose click target is their own destination URL are touched — ads on a URL pool, with a self-linking creative (html / iframe / VAST) or a phone number are reported as `skipped`. Every new URL passes the single-ad checks first (format, blocked domains); one bad URL fails the whole call before anything is written. Changed ads go back to review unless the account is auto-validated. Legacy shape `{adids, destinationurl}` is also accepted. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_url_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_url_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateUrlPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_url_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_url_put_request=api_v1_campaigns_type_campaign_id_ads_update_url_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_update_url_put_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_update_url_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_update_url_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_update_url_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/update-url',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_weight_put(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set the rotation weight of one or more RON ads.

        Writes `sort_weight` on every listed ad of this campaign (the relative share an ad gets when the campaign rotates its ads by weight). Same handler as the panel. RON only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_weight_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_weight_put_request=api_v1_campaigns_type_campaign_id_ads_update_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_weight_put_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set the rotation weight of one or more RON ads.

        Writes `sort_weight` on every listed ad of this campaign (the relative share an ad gets when the campaign rotates its ads by weight). Same handler as the panel. RON only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_weight_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_weight_put_request=api_v1_campaigns_type_campaign_id_ads_update_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_ads_update_weight_put_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set the rotation weight of one or more RON ads.

        Writes `sort_weight` on every listed ad of this campaign (the relative share an ad gets when the campaign rotates its ads by weight). Same handler as the panel. RON only. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: (required)
        :type api_v1_campaigns_type_campaign_id_ads_update_weight_put_request: ApiV1CampaignsTypeCampaignIdAdsUpdateWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_ads_update_weight_put_serialize(
            type=type,
            campaign_id=campaign_id,
            api_v1_campaigns_type_campaign_id_ads_update_weight_put_request=api_v1_campaigns_type_campaign_id_ads_update_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_ads_update_weight_put_serialize(
        self,
        type,
        campaign_id,
        api_v1_campaigns_type_campaign_id_ads_update_weight_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_campaign_id_ads_update_weight_put_request is not None:
            _body_params = api_v1_campaigns_type_campaign_id_ads_update_weight_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/ads/update-weight',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_campaign_id_schema_ads_get(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Field metadata for ad creation, scoped to a campaign.

        Same as `/_schema/ads` above, but uses the campaign's ad type to return only the fields that apply (e.g. video pools omitted for a banner-only campaign). Sets `campaign_ad_type` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_schema_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_campaign_id_schema_ads_get_with_http_info(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Field metadata for ad creation, scoped to a campaign.

        Same as `/_schema/ads` above, but uses the campaign's ad type to return only the fields that apply (e.g. video pools omitted for a banner-only campaign). Sets `campaign_ad_type` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_schema_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_campaign_id_schema_ads_get_without_preload_content(
        self,
        type: StrictStr,
        campaign_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Field metadata for ad creation, scoped to a campaign.

        Same as `/_schema/ads` above, but uses the campaign's ad type to return only the fields that apply (e.g. video pools omitted for a banner-only campaign). Sets `campaign_ad_type` in the response. 

        :param type: (required)
        :type type: str
        :param campaign_id: (required)
        :type campaign_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_campaign_id_schema_ads_get_serialize(
            type=type,
            campaign_id=campaign_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_campaign_id_schema_ads_get_serialize(
        self,
        type,
        campaign_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if campaign_id is not None:
            _path_params['campaignId'] = campaign_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{campaignId}/_schema/ads',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_active_patch(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdActivePatch200Response:
        """Pause or unpause a campaign.

        Idempotent. `active=true` unpauses, `active=false` pauses. Reuses the same panel-side guards: flat-rate campaigns with running deals cannot be paused; offer campaigns require >= 5 ads to be unpaused.  This is the endpoint behind the **\"On / off only\"** key preset. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_active_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_active_patch_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdActivePatch200Response]:
        """Pause or unpause a campaign.

        Idempotent. `active=true` unpauses, `active=false` pauses. Reuses the same panel-side guards: flat-rate campaigns with running deals cannot be paused; offer campaigns require >= 5 ads to be unpaused.  This is the endpoint behind the **\"On / off only\"** key preset. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_active_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_active_patch_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Pause or unpause a campaign.

        Idempotent. `active=true` unpauses, `active=false` pauses. Reuses the same panel-side guards: flat-rate campaigns with running deals cannot be paused; offer campaigns require >= 5 ads to be unpaused.  This is the endpoint behind the **\"On / off only\"** key preset. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_active_patch_request: (required)
        :type api_v1_campaigns_type_id_active_patch_request: ApiV1CampaignsTypeIdActivePatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_active_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_active_patch_request=api_v1_campaigns_type_id_active_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdActivePatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_active_patch_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_active_patch_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_active_patch_request is not None:
            _body_params = api_v1_campaigns_type_id_active_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{id}/active',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_available_zones_get(
        self,
        type: StrictStr,
        id: StrictInt,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches zone name, site name or zone id.")] = None,
        site_id: Annotated[Optional[StrictInt], Field(description="Only zones of this site (GET …/sites).")] = None,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out.")] = None,
        only_used_sizes: Annotated[Optional[StrictBool], Field(description="Banner campaigns: only zones whose size one of the campaign's live ads has.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """List your ad zones that can be attached to a campaign.

        Your own, non-deleted ad zones matching the campaign's ad type (and main category / native orientation where they apply), newest first, with `is_whitelisted` for the ones already attached. Paginated (`per_page` default 50, max 200). Same handler as the panel's zone picker. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param search: Matches zone name, site name or zone id.
        :type search: str
        :param site_id: Only zones of this site (GET …/sites).
        :type site_id: int
        :param exclude_ids: Comma-separated zone ids to leave out.
        :type exclude_ids: str
        :param only_used_sizes: Banner campaigns: only zones whose size one of the campaign's live ads has.
        :type only_used_sizes: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_available_zones_get_serialize(
            type=type,
            id=id,
            page=page,
            per_page=per_page,
            search=search,
            site_id=site_id,
            exclude_ids=exclude_ids,
            only_used_sizes=only_used_sizes,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_available_zones_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches zone name, site name or zone id.")] = None,
        site_id: Annotated[Optional[StrictInt], Field(description="Only zones of this site (GET …/sites).")] = None,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out.")] = None,
        only_used_sizes: Annotated[Optional[StrictBool], Field(description="Banner campaigns: only zones whose size one of the campaign's live ads has.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """List your ad zones that can be attached to a campaign.

        Your own, non-deleted ad zones matching the campaign's ad type (and main category / native orientation where they apply), newest first, with `is_whitelisted` for the ones already attached. Paginated (`per_page` default 50, max 200). Same handler as the panel's zone picker. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param search: Matches zone name, site name or zone id.
        :type search: str
        :param site_id: Only zones of this site (GET …/sites).
        :type site_id: int
        :param exclude_ids: Comma-separated zone ids to leave out.
        :type exclude_ids: str
        :param only_used_sizes: Banner campaigns: only zones whose size one of the campaign's live ads has.
        :type only_used_sizes: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_available_zones_get_serialize(
            type=type,
            id=id,
            page=page,
            per_page=per_page,
            search=search,
            site_id=site_id,
            exclude_ids=exclude_ids,
            only_used_sizes=only_used_sizes,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_available_zones_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = None,
        search: Annotated[Optional[StrictStr], Field(description="Matches zone name, site name or zone id.")] = None,
        site_id: Annotated[Optional[StrictInt], Field(description="Only zones of this site (GET …/sites).")] = None,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out.")] = None,
        only_used_sizes: Annotated[Optional[StrictBool], Field(description="Banner campaigns: only zones whose size one of the campaign's live ads has.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List your ad zones that can be attached to a campaign.

        Your own, non-deleted ad zones matching the campaign's ad type (and main category / native orientation where they apply), newest first, with `is_whitelisted` for the ones already attached. Paginated (`per_page` default 50, max 200). Same handler as the panel's zone picker. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param search: Matches zone name, site name or zone id.
        :type search: str
        :param site_id: Only zones of this site (GET …/sites).
        :type site_id: int
        :param exclude_ids: Comma-separated zone ids to leave out.
        :type exclude_ids: str
        :param only_used_sizes: Banner campaigns: only zones whose size one of the campaign's live ads has.
        :type only_used_sizes: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_available_zones_get_serialize(
            type=type,
            id=id,
            page=page,
            per_page=per_page,
            search=search,
            site_id=site_id,
            exclude_ids=exclude_ids,
            only_used_sizes=only_used_sizes,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_available_zones_get_serialize(
        self,
        type,
        id,
        page,
        per_page,
        search,
        site_id,
        exclude_ids,
        only_used_sizes,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if site_id is not None:
            
            _query_params.append(('site_id', site_id))
            
        if exclude_ids is not None:
            
            _query_params.append(('exclude_ids', exclude_ids))
            
        if only_used_sizes is not None:
            
            _query_params.append(('only_used_sizes', only_used_sizes))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}/available-zones',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_bids_patch(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdBidsPatch200Response:
        """Mass update bids on every ad in a campaign.

        Update every (or a subset of) ad's bid in one call. Three modes:    - `set`     — overwrite each target ad's bid with `value`.   - `pct_inc` — raise each target ad's bid by `pct` percent.   - `pct_dec` — lower each target ad's bid by `pct` percent.  Optional `ad_ids` narrows the update to a subset (omit or empty list = every non-deleted ad on the campaign). Bids are clamped at 0 — anything that would resolve below 0 is set to 0.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`).  `pct_inc` / `pct_dec` scale the stored bid and user_bid alike. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_bids_patch_request: (required)
        :type api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_bids_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_bids_patch_request=api_v1_campaigns_type_id_bids_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBidsPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_bids_patch_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdBidsPatch200Response]:
        """Mass update bids on every ad in a campaign.

        Update every (or a subset of) ad's bid in one call. Three modes:    - `set`     — overwrite each target ad's bid with `value`.   - `pct_inc` — raise each target ad's bid by `pct` percent.   - `pct_dec` — lower each target ad's bid by `pct` percent.  Optional `ad_ids` narrows the update to a subset (omit or empty list = every non-deleted ad on the campaign). Bids are clamped at 0 — anything that would resolve below 0 is set to 0.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`).  `pct_inc` / `pct_dec` scale the stored bid and user_bid alike. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_bids_patch_request: (required)
        :type api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_bids_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_bids_patch_request=api_v1_campaigns_type_id_bids_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBidsPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_bids_patch_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Mass update bids on every ad in a campaign.

        Update every (or a subset of) ad's bid in one call. Three modes:    - `set`     — overwrite each target ad's bid with `value`.   - `pct_inc` — raise each target ad's bid by `pct` percent.   - `pct_dec` — lower each target ad's bid by `pct` percent.  Optional `ad_ids` narrows the update to a subset (omit or empty list = every non-deleted ad on the campaign). Bids are clamped at 0 — anything that would resolve below 0 is set to 0.  Bids are in **currency units of your account's currency** (`0.05` = 0.05), the same as the panel, and must be at least `GET /api/v1/campaigns/{type}/{id}/min-bid` (422 otherwise; `0` is allowed and stops the ad bidding). Reads return the bid as `bid_amount` in the same unit; `user_bid` / `bid` are the stored values in cents (your currency / the network's main currency). Keys that wrote bids before 2026-10-12 keep the old raw-cents contract; every bid write echoes `bid_unit` (`currency` or `raw_cents`).  `pct_inc` / `pct_dec` scale the stored bid and user_bid alike. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_bids_patch_request: (required)
        :type api_v1_campaigns_type_id_bids_patch_request: ApiV1CampaignsTypeIdBidsPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_bids_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_bids_patch_request=api_v1_campaigns_type_id_bids_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBidsPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_bids_patch_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_bids_patch_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_bids_patch_request is not None:
            _body_params = api_v1_campaigns_type_id_bids_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{id}/bids',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_budget_patch(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdBudgetPatch200Response:
        """Update a campaign's total and/or daily budget.

        Sets the campaign (total) budget and/or the max daily budget, plus the flags that enable each cap. All four fields are optional — send only the ones you want to change. Amounts are in the account currency. Documented in audit_20260723_1117 (was implemented but unspecified).  `max_day_budget` is corrected upward to the ad type's configured minimum daily budget rather than rejected, matching every other write path. The stored amount is returned as `max_day_budget` in the response — read it back instead of assuming the value you sent. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_budget_patch_request: (required)
        :type api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_budget_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_budget_patch_request=api_v1_campaigns_type_id_budget_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBudgetPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_budget_patch_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdBudgetPatch200Response]:
        """Update a campaign's total and/or daily budget.

        Sets the campaign (total) budget and/or the max daily budget, plus the flags that enable each cap. All four fields are optional — send only the ones you want to change. Amounts are in the account currency. Documented in audit_20260723_1117 (was implemented but unspecified).  `max_day_budget` is corrected upward to the ad type's configured minimum daily budget rather than rejected, matching every other write path. The stored amount is returned as `max_day_budget` in the response — read it back instead of assuming the value you sent. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_budget_patch_request: (required)
        :type api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_budget_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_budget_patch_request=api_v1_campaigns_type_id_budget_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBudgetPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_budget_patch_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update a campaign's total and/or daily budget.

        Sets the campaign (total) budget and/or the max daily budget, plus the flags that enable each cap. All four fields are optional — send only the ones you want to change. Amounts are in the account currency. Documented in audit_20260723_1117 (was implemented but unspecified).  `max_day_budget` is corrected upward to the ad type's configured minimum daily budget rather than rejected, matching every other write path. The stored amount is returned as `max_day_budget` in the response — read it back instead of assuming the value you sent. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_budget_patch_request: (required)
        :type api_v1_campaigns_type_id_budget_patch_request: ApiV1CampaignsTypeIdBudgetPatchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_budget_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_budget_patch_request=api_v1_campaigns_type_id_budget_patch_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdBudgetPatch200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_budget_patch_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_budget_patch_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_budget_patch_request is not None:
            _body_params = api_v1_campaigns_type_id_budget_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{id}/budget',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_clone_post(
        self,
        type: StrictStr,
        id: StrictInt,
        strict: Annotated[Optional[StrictInt], Field(description="1 = reject unknown body keys (422).")] = None,
        api_v1_campaigns_type_id_clone_post_request: Optional[ApiV1CampaignsTypeIdClonePostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdClonePost201Response:
        """Clone a campaign — everything, or the parts you pick.

        Same core as the panel's Duplicate button. The clone lands paused (`is_active=false`; a network can make ron clones start active, and one that reviews new campaigns puts them in Pending Created) and named \"<original> Copy\" unless `name` is sent. By default every part is copied; the four `copy_*` switches (the Duplicate dialog's choices, each default `true`) leave a part out, in which case the clone gets the table defaults for it:  - `copy_ads` — the campaign's ads and creatives. - `copy_targeting` — countries/regions, categories, devices,   browsers, OS, languages, location, connection / carrier / ISP,   keywords, webview / adblock, orientation and the linked domain /   IP / retargeting filters. - `copy_budget` — total and daily budget, impression limits,   frequency capping, conversion capping. - `copy_schedule` — day/time parting and the start / end dates.  Bookkeeping (`num_ads`, `pending_state`, `dateadded`, `wl_zoneids`) is always reset. A RON clone also drops any flat-deal records, copies offer screenshots, and goes to review when the network validates campaigns. A flat campaign (paytype 5) can only be cloned by an administrator → 403 for API keys.  `copied` in the response echoes which parts were copied. Unknown body keys are ignored, or a 422 with `?strict=1`. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param strict: 1 = reject unknown body keys (422).
        :type strict: int
        :param api_v1_campaigns_type_id_clone_post_request:
        :type api_v1_campaigns_type_id_clone_post_request: ApiV1CampaignsTypeIdClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_clone_post_serialize(
            type=type,
            id=id,
            strict=strict,
            api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeIdClonePost201Response",
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_clone_post_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        strict: Annotated[Optional[StrictInt], Field(description="1 = reject unknown body keys (422).")] = None,
        api_v1_campaigns_type_id_clone_post_request: Optional[ApiV1CampaignsTypeIdClonePostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdClonePost201Response]:
        """Clone a campaign — everything, or the parts you pick.

        Same core as the panel's Duplicate button. The clone lands paused (`is_active=false`; a network can make ron clones start active, and one that reviews new campaigns puts them in Pending Created) and named \"<original> Copy\" unless `name` is sent. By default every part is copied; the four `copy_*` switches (the Duplicate dialog's choices, each default `true`) leave a part out, in which case the clone gets the table defaults for it:  - `copy_ads` — the campaign's ads and creatives. - `copy_targeting` — countries/regions, categories, devices,   browsers, OS, languages, location, connection / carrier / ISP,   keywords, webview / adblock, orientation and the linked domain /   IP / retargeting filters. - `copy_budget` — total and daily budget, impression limits,   frequency capping, conversion capping. - `copy_schedule` — day/time parting and the start / end dates.  Bookkeeping (`num_ads`, `pending_state`, `dateadded`, `wl_zoneids`) is always reset. A RON clone also drops any flat-deal records, copies offer screenshots, and goes to review when the network validates campaigns. A flat campaign (paytype 5) can only be cloned by an administrator → 403 for API keys.  `copied` in the response echoes which parts were copied. Unknown body keys are ignored, or a 422 with `?strict=1`. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param strict: 1 = reject unknown body keys (422).
        :type strict: int
        :param api_v1_campaigns_type_id_clone_post_request:
        :type api_v1_campaigns_type_id_clone_post_request: ApiV1CampaignsTypeIdClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_clone_post_serialize(
            type=type,
            id=id,
            strict=strict,
            api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeIdClonePost201Response",
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_clone_post_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        strict: Annotated[Optional[StrictInt], Field(description="1 = reject unknown body keys (422).")] = None,
        api_v1_campaigns_type_id_clone_post_request: Optional[ApiV1CampaignsTypeIdClonePostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Clone a campaign — everything, or the parts you pick.

        Same core as the panel's Duplicate button. The clone lands paused (`is_active=false`; a network can make ron clones start active, and one that reviews new campaigns puts them in Pending Created) and named \"<original> Copy\" unless `name` is sent. By default every part is copied; the four `copy_*` switches (the Duplicate dialog's choices, each default `true`) leave a part out, in which case the clone gets the table defaults for it:  - `copy_ads` — the campaign's ads and creatives. - `copy_targeting` — countries/regions, categories, devices,   browsers, OS, languages, location, connection / carrier / ISP,   keywords, webview / adblock, orientation and the linked domain /   IP / retargeting filters. - `copy_budget` — total and daily budget, impression limits,   frequency capping, conversion capping. - `copy_schedule` — day/time parting and the start / end dates.  Bookkeeping (`num_ads`, `pending_state`, `dateadded`, `wl_zoneids`) is always reset. A RON clone also drops any flat-deal records, copies offer screenshots, and goes to review when the network validates campaigns. A flat campaign (paytype 5) can only be cloned by an administrator → 403 for API keys.  `copied` in the response echoes which parts were copied. Unknown body keys are ignored, or a 422 with `?strict=1`. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param strict: 1 = reject unknown body keys (422).
        :type strict: int
        :param api_v1_campaigns_type_id_clone_post_request:
        :type api_v1_campaigns_type_id_clone_post_request: ApiV1CampaignsTypeIdClonePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_clone_post_serialize(
            type=type,
            id=id,
            strict=strict,
            api_v1_campaigns_type_id_clone_post_request=api_v1_campaigns_type_id_clone_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeIdClonePost201Response",
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_clone_post_serialize(
        self,
        type,
        id,
        strict,
        api_v1_campaigns_type_id_clone_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_clone_post_request is not None:
            _body_params = api_v1_campaigns_type_id_clone_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{id}/clone',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_delete(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdDelete200Response:
        """Soft-delete a campaign.

        Sets `isdeleted=1`, `dayactive=0` (flatrate / directdeal: `iscancelled=1`, `ispaused=1`, `dayactive=0`). The campaign and its history remain in the database for billing/stats reconciliation but stop serving immediately. Idempotent — deleting an already-deleted campaign returns 404. The campaign's live ads are soft-deleted with it (marked as deleted-with-the-campaign; ads you had deleted yourself before stay as they were).  Undo with `POST /api/v1/campaigns/mass-undelete` `{ids:[id], type}`: the ads the delete took down come back, and a ron / cpm / rtb campaign returns paused or running as it was before the delete (a flat / direct deal comes back paused). Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  On a network that reviews campaign deletes, a live ron campaign (not a flat one) is not deleted: the answer is `deleted: false, pending_review: true`, the campaign keeps running with `pending_state: 2` (Pending Delete), and an admin's approval deletes it. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_delete_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_delete_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdDelete200Response]:
        """Soft-delete a campaign.

        Sets `isdeleted=1`, `dayactive=0` (flatrate / directdeal: `iscancelled=1`, `ispaused=1`, `dayactive=0`). The campaign and its history remain in the database for billing/stats reconciliation but stop serving immediately. Idempotent — deleting an already-deleted campaign returns 404. The campaign's live ads are soft-deleted with it (marked as deleted-with-the-campaign; ads you had deleted yourself before stay as they were).  Undo with `POST /api/v1/campaigns/mass-undelete` `{ids:[id], type}`: the ads the delete took down come back, and a ron / cpm / rtb campaign returns paused or running as it was before the delete (a flat / direct deal comes back paused). Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  On a network that reviews campaign deletes, a live ron campaign (not a flat one) is not deleted: the answer is `deleted: false, pending_review: true`, the campaign keeps running with `pending_state: 2` (Pending Delete), and an admin's approval deletes it. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_delete_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_delete_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Soft-delete a campaign.

        Sets `isdeleted=1`, `dayactive=0` (flatrate / directdeal: `iscancelled=1`, `ispaused=1`, `dayactive=0`). The campaign and its history remain in the database for billing/stats reconciliation but stop serving immediately. Idempotent — deleting an already-deleted campaign returns 404. The campaign's live ads are soft-deleted with it (marked as deleted-with-the-campaign; ads you had deleted yourself before stay as they were).  Undo with `POST /api/v1/campaigns/mass-undelete` `{ids:[id], type}`: the ads the delete took down come back, and a ron / cpm / rtb campaign returns paused or running as it was before the delete (a flat / direct deal comes back paused). Find deleted campaigns with `GET /api/v1/campaigns?deleted=1`.  On a network that reviews campaign deletes, a live ron campaign (not a flat one) is not deleted: the answer is `deleted: false, pending_review: true`, the campaign keeps running with `pending_state: 2` (Pending Delete), and an admin's approval deletes it. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_delete_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdDelete200Response",
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_delete_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/{type}/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_filters_filter_type_filter_id_delete(
        self,
        type: StrictStr,
        id: StrictInt,
        filter_type: StrictStr,
        filter_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Detach a filter from this campaign.

        Block list: removes the campaign from the filter's campaign list. Refused with 409 when that would widen the filter instead — `last_campaign` (it is the only listed campaign; an empty list means every campaign of the ad type) or `filter_not_campaign_scoped` (the filter covers every campaign anyway). Deactivate, delete or re-scope the filter (PUT /api/v1/filters/{type}/{id}) instead. Allow-list / `ip`: clears the campaign's FK column only if it currently points to this filter; otherwise returns 404. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param filter_type: (required)
        :type filter_type: str
        :param filter_id: (required)
        :type filter_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_serialize(
            type=type,
            id=id,
            filter_type=filter_type,
            filter_id=filter_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '409': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        filter_type: StrictStr,
        filter_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Detach a filter from this campaign.

        Block list: removes the campaign from the filter's campaign list. Refused with 409 when that would widen the filter instead — `last_campaign` (it is the only listed campaign; an empty list means every campaign of the ad type) or `filter_not_campaign_scoped` (the filter covers every campaign anyway). Deactivate, delete or re-scope the filter (PUT /api/v1/filters/{type}/{id}) instead. Allow-list / `ip`: clears the campaign's FK column only if it currently points to this filter; otherwise returns 404. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param filter_type: (required)
        :type filter_type: str
        :param filter_id: (required)
        :type filter_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_serialize(
            type=type,
            id=id,
            filter_type=filter_type,
            filter_id=filter_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '409': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        filter_type: StrictStr,
        filter_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Detach a filter from this campaign.

        Block list: removes the campaign from the filter's campaign list. Refused with 409 when that would widen the filter instead — `last_campaign` (it is the only listed campaign; an empty list means every campaign of the ad type) or `filter_not_campaign_scoped` (the filter covers every campaign anyway). Deactivate, delete or re-scope the filter (PUT /api/v1/filters/{type}/{id}) instead. Allow-list / `ip`: clears the campaign's FK column only if it currently points to this filter; otherwise returns 404. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param filter_type: (required)
        :type filter_type: str
        :param filter_id: (required)
        :type filter_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_serialize(
            type=type,
            id=id,
            filter_type=filter_type,
            filter_id=filter_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
            '409': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_filters_filter_type_filter_id_delete_serialize(
        self,
        type,
        id,
        filter_type,
        filter_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        if filter_type is not None:
            _path_params['filter_type'] = filter_type
        if filter_id is not None:
            _path_params['filter_id'] = filter_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/{type}/{id}/filters/{filter_type}/{filter_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_filters_get(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdFiltersGet200Response:
        """List filters attached to this campaign.

        Returns every filter that reaches this campaign: allow-lists and the IP pool via the campaign's FK columns, and block lists that either list it (`applies_to: listed_campaigns`, matching campaign_type) or cover it without a list (`all_campaigns` = ad_type 0; `all_campaigns_of_ad_type` = same ad type, empty list). `ron`, `cpm` and `rtb` campaigns support filter linkage. A cpm campaign takes `subid_incl`, `subid_excl`, `ip` and the domain / adzone / ISP block lists (block lists hold it as a `ron` campaign); `domain_incl` / `adzone_incl` are ron / rtb only → 422 `validation_error`. Any other type → 422 \"Filter linking is only supported for campaign types: ron, cpm, rtb.\" 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersGet200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_filters_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdFiltersGet200Response]:
        """List filters attached to this campaign.

        Returns every filter that reaches this campaign: allow-lists and the IP pool via the campaign's FK columns, and block lists that either list it (`applies_to: listed_campaigns`, matching campaign_type) or cover it without a list (`all_campaigns` = ad_type 0; `all_campaigns_of_ad_type` = same ad type, empty list). `ron`, `cpm` and `rtb` campaigns support filter linkage. A cpm campaign takes `subid_incl`, `subid_excl`, `ip` and the domain / adzone / ISP block lists (block lists hold it as a `ron` campaign); `domain_incl` / `adzone_incl` are ron / rtb only → 422 `validation_error`. Any other type → 422 \"Filter linking is only supported for campaign types: ron, cpm, rtb.\" 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersGet200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_filters_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List filters attached to this campaign.

        Returns every filter that reaches this campaign: allow-lists and the IP pool via the campaign's FK columns, and block lists that either list it (`applies_to: listed_campaigns`, matching campaign_type) or cover it without a list (`all_campaigns` = ad_type 0; `all_campaigns_of_ad_type` = same ad type, empty list). `ron`, `cpm` and `rtb` campaigns support filter linkage. A cpm campaign takes `subid_incl`, `subid_excl`, `ip` and the domain / adzone / ISP block lists (block lists hold it as a `ron` campaign); `domain_incl` / `adzone_incl` are ron / rtb only → 422 `validation_error`. Any other type → 422 \"Filter linking is only supported for campaign types: ron, cpm, rtb.\" 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersGet200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_filters_get_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}/filters',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_filters_post(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdFiltersPost200Response:
        """Attach a filter to this campaign.

        Block lists (`*_excl`): adds the campaign to the filter's campaign list. A filter that already covers the campaign (ad_type 0, or an empty list of the campaign's ad type) is left alone — `changed: false` + `applies_to` — instead of being narrowed to this one campaign. Refused with 422 when the filter's ad type differs from the campaign's (the block would never apply) or when its list holds the other campaign kind (ron vs rtb). Allow-lists (`*_incl`) and `ip`: sets the campaign's FK column to this filter (replacing any previous one of the same kind). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_filters_post_request: (required)
        :type api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_filters_post_request=api_v1_campaigns_type_id_filters_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersPost200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_filters_post_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdFiltersPost200Response]:
        """Attach a filter to this campaign.

        Block lists (`*_excl`): adds the campaign to the filter's campaign list. A filter that already covers the campaign (ad_type 0, or an empty list of the campaign's ad type) is left alone — `changed: false` + `applies_to` — instead of being narrowed to this one campaign. Refused with 422 when the filter's ad type differs from the campaign's (the block would never apply) or when its list holds the other campaign kind (ron vs rtb). Allow-lists (`*_incl`) and `ip`: sets the campaign's FK column to this filter (replacing any previous one of the same kind). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_filters_post_request: (required)
        :type api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_filters_post_request=api_v1_campaigns_type_id_filters_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersPost200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_filters_post_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Attach a filter to this campaign.

        Block lists (`*_excl`): adds the campaign to the filter's campaign list. A filter that already covers the campaign (ad_type 0, or an empty list of the campaign's ad type) is left alone — `changed: false` + `applies_to` — instead of being narrowed to this one campaign. Refused with 422 when the filter's ad type differs from the campaign's (the block would never apply) or when its list holds the other campaign kind (ron vs rtb). Allow-lists (`*_incl`) and `ip`: sets the campaign's FK column to this filter (replacing any previous one of the same kind). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_filters_post_request: (required)
        :type api_v1_campaigns_type_id_filters_post_request: ApiV1CampaignsTypeIdFiltersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_filters_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_filters_post_request=api_v1_campaigns_type_id_filters_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdFiltersPost200Response",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_filters_post_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_filters_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_filters_post_request is not None:
            _body_params = api_v1_campaigns_type_id_filters_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{id}/filters',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_get(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Get a single campaign.


        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Get a single campaign.


        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get a single campaign.


        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_get_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_min_bid_get(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeIdMinBidGet200Response:
        """Get the campaign's minimum acceptable CPC bid.

        Returns the floor the platform will accept for this campaign, derived from the same logic the panel uses (admanager → effectively zero, custom `fx_minprice`, or the `min_prices_ron` table matched against the campaign's targeting). Use this before bulk-updating bids so the optimiser doesn't push values below the floor and have them clamped or rejected. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_min_bid_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdMinBidGet200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_min_bid_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeIdMinBidGet200Response]:
        """Get the campaign's minimum acceptable CPC bid.

        Returns the floor the platform will accept for this campaign, derived from the same logic the panel uses (admanager → effectively zero, custom `fx_minprice`, or the `min_prices_ron` table matched against the campaign's targeting). Use this before bulk-updating bids so the optimiser doesn't push values below the floor and have them clamped or rejected. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_min_bid_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdMinBidGet200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_min_bid_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get the campaign's minimum acceptable CPC bid.

        Returns the floor the platform will accept for this campaign, derived from the same logic the panel uses (admanager → effectively zero, custom `fx_minprice`, or the `min_prices_ron` table matched against the campaign's targeting). Use this before bulk-updating bids so the optimiser doesn't push values below the floor and have them clamped or rejected. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_min_bid_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeIdMinBidGet200Response",
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_min_bid_get_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}/min-bid',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_patch(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Partially update a campaign.

        Updates one or more writable fields on an existing campaign. Send only the fields you want to change — anything you omit is left alone. Field names are the public ones from `GET /api/v1/campaigns/{type}/_schema` (`daily_budget`, `regions`, `device_type_ids`, …).  **Region targeting (`regions`):** the server defensively trims any ancestor id whose descendant is also in the list, at any depth (continent → country → state → sub-region → city). If you send a higher-level id alongside one of its descendants, the higher-level id is dropped — sending both would otherwise broaden targeting back up to the whole subtree and undo the leaf pick. Use `GET /api/v1/lookups/regions` to walk the geo tree and pick the leaf id you actually want.  **`directdeal` / `flatrate`** take their own field set: `name`, `is_paused`, `start_date`, `total_days` (either alone — the other keeps its stored value; the end date is recomputed), `deal_type`, `total_budget`, `regions` (or legacy `countries`), `languages`, `device_type_ids`, `os_ids`, `browser_ids`, `max_impressions`, `percentage` (0-100), `use_keywords`, `keywords`, `keywords_exclude`. Any other field — including `ad_space_id`, which is fixed at create — answers `422 unsupported_fields` with the list, rather than being ignored.  Some fields cannot be changed via this endpoint:   - `ad_type` — the ads table layout differs per type, change     requires recreating the campaign.   - `id`, `userid`, `systemid`, `isdeleted`, `dateadded`, audit     stamps — system-managed.   - Read-only projection fields — `total_spent`, `sites_locked`,     `pending_state`, `num_ads`, `is_deleted`, `is_complete`,     `created_at`, `started_at`, `ended_at`, `last_paid_at` — are     ignored (rejected in strict mode).   - `selling_type` — a change is refused with 409; change it in     the panel.  The same save rules as the panel apply: `daily_budget` is raised to the system minimum, `total_budget` must be > 0 while `use_campaign_budget` is true, an impression limit that is switched on needs a value > 0, and `start_date` / `end_date` must be YYYY-MM-DD. Every campaign-form field of `CampaignPanelFields` is writable here too, with the same gates as on create (a field that does not apply is a `422`); object fields (`day_parting`, `conversion_capping`, …) merge with the stored value, and the other option keys are kept. `banner_size_ids` (rtb banner) replaces the size set. The change is recorded in the campaign history and mailed like a panel save.  **Modes:**   - `?dry_run=1` — return the resolved field map without writing.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_patch_request: (required)
        :type api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_patch_request=api_v1_campaigns_type_id_patch_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_patch_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Partially update a campaign.

        Updates one or more writable fields on an existing campaign. Send only the fields you want to change — anything you omit is left alone. Field names are the public ones from `GET /api/v1/campaigns/{type}/_schema` (`daily_budget`, `regions`, `device_type_ids`, …).  **Region targeting (`regions`):** the server defensively trims any ancestor id whose descendant is also in the list, at any depth (continent → country → state → sub-region → city). If you send a higher-level id alongside one of its descendants, the higher-level id is dropped — sending both would otherwise broaden targeting back up to the whole subtree and undo the leaf pick. Use `GET /api/v1/lookups/regions` to walk the geo tree and pick the leaf id you actually want.  **`directdeal` / `flatrate`** take their own field set: `name`, `is_paused`, `start_date`, `total_days` (either alone — the other keeps its stored value; the end date is recomputed), `deal_type`, `total_budget`, `regions` (or legacy `countries`), `languages`, `device_type_ids`, `os_ids`, `browser_ids`, `max_impressions`, `percentage` (0-100), `use_keywords`, `keywords`, `keywords_exclude`. Any other field — including `ad_space_id`, which is fixed at create — answers `422 unsupported_fields` with the list, rather than being ignored.  Some fields cannot be changed via this endpoint:   - `ad_type` — the ads table layout differs per type, change     requires recreating the campaign.   - `id`, `userid`, `systemid`, `isdeleted`, `dateadded`, audit     stamps — system-managed.   - Read-only projection fields — `total_spent`, `sites_locked`,     `pending_state`, `num_ads`, `is_deleted`, `is_complete`,     `created_at`, `started_at`, `ended_at`, `last_paid_at` — are     ignored (rejected in strict mode).   - `selling_type` — a change is refused with 409; change it in     the panel.  The same save rules as the panel apply: `daily_budget` is raised to the system minimum, `total_budget` must be > 0 while `use_campaign_budget` is true, an impression limit that is switched on needs a value > 0, and `start_date` / `end_date` must be YYYY-MM-DD. Every campaign-form field of `CampaignPanelFields` is writable here too, with the same gates as on create (a field that does not apply is a `422`); object fields (`day_parting`, `conversion_capping`, …) merge with the stored value, and the other option keys are kept. `banner_size_ids` (rtb banner) replaces the size set. The change is recorded in the campaign history and mailed like a panel save.  **Modes:**   - `?dry_run=1` — return the resolved field map without writing.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_patch_request: (required)
        :type api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_patch_request=api_v1_campaigns_type_id_patch_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_patch_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Partially update a campaign.

        Updates one or more writable fields on an existing campaign. Send only the fields you want to change — anything you omit is left alone. Field names are the public ones from `GET /api/v1/campaigns/{type}/_schema` (`daily_budget`, `regions`, `device_type_ids`, …).  **Region targeting (`regions`):** the server defensively trims any ancestor id whose descendant is also in the list, at any depth (continent → country → state → sub-region → city). If you send a higher-level id alongside one of its descendants, the higher-level id is dropped — sending both would otherwise broaden targeting back up to the whole subtree and undo the leaf pick. Use `GET /api/v1/lookups/regions` to walk the geo tree and pick the leaf id you actually want.  **`directdeal` / `flatrate`** take their own field set: `name`, `is_paused`, `start_date`, `total_days` (either alone — the other keeps its stored value; the end date is recomputed), `deal_type`, `total_budget`, `regions` (or legacy `countries`), `languages`, `device_type_ids`, `os_ids`, `browser_ids`, `max_impressions`, `percentage` (0-100), `use_keywords`, `keywords`, `keywords_exclude`. Any other field — including `ad_space_id`, which is fixed at create — answers `422 unsupported_fields` with the list, rather than being ignored.  Some fields cannot be changed via this endpoint:   - `ad_type` — the ads table layout differs per type, change     requires recreating the campaign.   - `id`, `userid`, `systemid`, `isdeleted`, `dateadded`, audit     stamps — system-managed.   - Read-only projection fields — `total_spent`, `sites_locked`,     `pending_state`, `num_ads`, `is_deleted`, `is_complete`,     `created_at`, `started_at`, `ended_at`, `last_paid_at` — are     ignored (rejected in strict mode).   - `selling_type` — a change is refused with 409; change it in     the panel.  The same save rules as the panel apply: `daily_budget` is raised to the system minimum, `total_budget` must be > 0 while `use_campaign_budget` is true, an impression limit that is switched on needs a value > 0, and `start_date` / `end_date` must be YYYY-MM-DD. Every campaign-form field of `CampaignPanelFields` is writable here too, with the same gates as on create (a field that does not apply is a `422`); object fields (`day_parting`, `conversion_capping`, …) merge with the stored value, and the other option keys are kept. `banner_size_ids` (rtb banner) replaces the size set. The change is recorded in the campaign history and mailed like a panel save.  **Modes:**   - `?dry_run=1` — return the resolved field map without writing.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     (default: the key's setting, strict for keys created from 2026-10-12). 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_patch_request: (required)
        :type api_v1_campaigns_type_id_patch_request: ApiV1CampaignsTypeIdPatchRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_patch_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_patch_request=api_v1_campaigns_type_id_patch_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_patch_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_patch_request,
        dry_run,
        strict,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if dry_run is not None:
            
            _query_params.append(('dry_run', dry_run))
            
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_patch_request is not None:
            _body_params = api_v1_campaigns_type_id_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/campaigns/{type}/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_reset_max_budget_put(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Reset a campaign's lifetime-budget spend.

        Zeroes the spend counted against the campaign's total budget (`campaignbudget`) and re-arms the \"budget reached\" email, so a campaign stopped by its lifetime budget can spend it again. The budget value itself is unchanged. Not for flatrate / directdeal (422 `budget_reset_not_supported`). Same handler as the panel's Reset button. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_reset_max_budget_put_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_reset_max_budget_put_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Reset a campaign's lifetime-budget spend.

        Zeroes the spend counted against the campaign's total budget (`campaignbudget`) and re-arms the \"budget reached\" email, so a campaign stopped by its lifetime budget can spend it again. The budget value itself is unchanged. Not for flatrate / directdeal (422 `budget_reset_not_supported`). Same handler as the panel's Reset button. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_reset_max_budget_put_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_reset_max_budget_put_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Reset a campaign's lifetime-budget spend.

        Zeroes the spend counted against the campaign's total budget (`campaignbudget`) and re-arms the \"budget reached\" email, so a campaign stopped by its lifetime budget can spend it again. The budget value itself is unchanged. Not for flatrate / directdeal (422 `budget_reset_not_supported`). Same handler as the panel's Reset button. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_reset_max_budget_put_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_reset_max_budget_put_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{id}/reset-max-budget',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_sites_get(
        self,
        type: StrictStr,
        id: StrictInt,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out of the counts.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Your sites that have zones attachable to a campaign.

        Your own sites with the number of their zones that match the campaign (same rules as available-zones); sites with none are left out. Use a site's `id` as `site_id` on available-zones. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param exclude_ids: Comma-separated zone ids to leave out of the counts.
        :type exclude_ids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_sites_get_serialize(
            type=type,
            id=id,
            exclude_ids=exclude_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_sites_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out of the counts.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Your sites that have zones attachable to a campaign.

        Your own sites with the number of their zones that match the campaign (same rules as available-zones); sites with none are left out. Use a site's `id` as `site_id` on available-zones. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param exclude_ids: Comma-separated zone ids to leave out of the counts.
        :type exclude_ids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_sites_get_serialize(
            type=type,
            id=id,
            exclude_ids=exclude_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_sites_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        exclude_ids: Annotated[Optional[StrictStr], Field(description="Comma-separated zone ids to leave out of the counts.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Your sites that have zones attachable to a campaign.

        Your own sites with the number of their zones that match the campaign (same rules as available-zones); sites with none are left out. Use a site's `id` as `site_id` on available-zones. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param exclude_ids: Comma-separated zone ids to leave out of the counts.
        :type exclude_ids: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_sites_get_serialize(
            type=type,
            id=id,
            exclude_ids=exclude_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_sites_get_serialize(
        self,
        type,
        id,
        exclude_ids,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if exclude_ids is not None:
            
            _query_params.append(('exclude_ids', exclude_ids))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}/sites',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_whitelist_zones_get(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """List the ad zones attached to a campaign.

        The campaign's zone allow-list with each zone's weight for this campaign (0–100, default 100). Only zones you own are returned. `owned` is false for a zone that is deleted. On an Ad Shop campaign the zone name is masked (\"Space #N\") and `site` / `siteid` are left out unless you hold the source-names right. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_whitelist_zones_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_whitelist_zones_get_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """List the ad zones attached to a campaign.

        The campaign's zone allow-list with each zone's weight for this campaign (0–100, default 100). Only zones you own are returned. `owned` is false for a zone that is deleted. On an Ad Shop campaign the zone name is masked (\"Space #N\") and `site` / `siteid` are left out unless you hold the source-names right. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_whitelist_zones_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_whitelist_zones_get_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List the ad zones attached to a campaign.

        The campaign's zone allow-list with each zone's weight for this campaign (0–100, default 100). Only zones you own are returned. `owned` is false for a zone that is deleted. On an Ad Shop campaign the zone name is masked (\"Space #N\") and `site` / `siteid` are left out unless you hold the source-names right. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_whitelist_zones_get_serialize(
            type=type,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_whitelist_zones_get_serialize(
        self,
        type,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/{id}/whitelist-zones',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_zones_post(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Attach ad zones to a campaign.

        Adds zones to the campaign's allow-list (kept ones stay) and connects each zone to the campaign at weight 100. Ids that are not yours, deleted, or don't match the campaign's ad type / main category / orientation are dropped; when none is left → 403 `not_allowed`. An empty list is a no-op 200. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_zones_post_request: (required)
        :type api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_zones_post_request=api_v1_campaigns_type_id_zones_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_zones_post_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Attach ad zones to a campaign.

        Adds zones to the campaign's allow-list (kept ones stay) and connects each zone to the campaign at weight 100. Ids that are not yours, deleted, or don't match the campaign's ad type / main category / orientation are dropped; when none is left → 403 `not_allowed`. An empty list is a no-op 200. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_zones_post_request: (required)
        :type api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_zones_post_request=api_v1_campaigns_type_id_zones_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_zones_post_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Attach ad zones to a campaign.

        Adds zones to the campaign's allow-list (kept ones stay) and connects each zone to the campaign at weight 100. Ids that are not yours, deleted, or don't match the campaign's ad type / main category / orientation are dropped; when none is left → 403 `not_allowed`. An empty list is a no-op 200. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param api_v1_campaigns_type_id_zones_post_request: (required)
        :type api_v1_campaigns_type_id_zones_post_request: ApiV1CampaignsTypeIdZonesPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_post_serialize(
            type=type,
            id=id,
            api_v1_campaigns_type_id_zones_post_request=api_v1_campaigns_type_id_zones_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_zones_post_serialize(
        self,
        type,
        id,
        api_v1_campaigns_type_id_zones_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_zones_post_request is not None:
            _body_params = api_v1_campaigns_type_id_zones_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}/{id}/zones',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_delete(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Detach an ad zone from a campaign.

        Removes the zone from the allow-list and the campaign from the zone's connected campaigns. Removing the last zone stores `0` (no allow-list). Detaching a zone that isn't attached is a 200 no-op. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_delete_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_delete_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Detach an ad zone from a campaign.

        Removes the zone from the allow-list and the campaign from the zone's connected campaigns. Removing the last zone stores `0` (no allow-list). Detaching a zone that isn't attached is a 200 no-op. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_delete_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_delete_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Detach an ad zone from a campaign.

        Removes the zone from the allow-list and the campaign from the zone's connected campaigns. Removing the last zone stores `0` (no allow-list). Detaching a zone that isn't attached is a 200 no-op. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_delete_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_zones_zone_id_delete_serialize(
        self,
        type,
        id,
        zone_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        if zone_id is not None:
            _path_params['zoneId'] = zone_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/campaigns/{type}/{id}/zones/{zoneId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_weight_put(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Set an attached zone's weight for this campaign.

        The share of the zone's traffic this campaign gets relative to the zone's other connected campaigns, 0–100 (values outside are clamped). The zone must be yours and connected to the campaign. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param api_v1_campaigns_type_id_zones_zone_id_weight_put_request: (required)
        :type api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_weight_put_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            api_v1_campaigns_type_id_zones_zone_id_weight_put_request=api_v1_campaigns_type_id_zones_zone_id_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_weight_put_with_http_info(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Set an attached zone's weight for this campaign.

        The share of the zone's traffic this campaign gets relative to the zone's other connected campaigns, 0–100 (values outside are clamped). The zone must be yours and connected to the campaign. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param api_v1_campaigns_type_id_zones_zone_id_weight_put_request: (required)
        :type api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_weight_put_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            api_v1_campaigns_type_id_zones_zone_id_weight_put_request=api_v1_campaigns_type_id_zones_zone_id_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_id_zones_zone_id_weight_put_without_preload_content(
        self,
        type: StrictStr,
        id: StrictInt,
        zone_id: StrictInt,
        api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set an attached zone's weight for this campaign.

        The share of the zone's traffic this campaign gets relative to the zone's other connected campaigns, 0–100 (values outside are clamped). The zone must be yours and connected to the campaign. Same handler as the panel. 

        :param type: (required)
        :type type: str
        :param id: (required)
        :type id: int
        :param zone_id: (required)
        :type zone_id: int
        :param api_v1_campaigns_type_id_zones_zone_id_weight_put_request: (required)
        :type api_v1_campaigns_type_id_zones_zone_id_weight_put_request: ApiV1CampaignsTypeIdZonesZoneIdWeightPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_id_zones_zone_id_weight_put_serialize(
            type=type,
            id=id,
            zone_id=zone_id,
            api_v1_campaigns_type_id_zones_zone_id_weight_put_request=api_v1_campaigns_type_id_zones_zone_id_weight_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '404': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_id_zones_zone_id_weight_put_serialize(
        self,
        type,
        id,
        zone_id,
        api_v1_campaigns_type_id_zones_zone_id_weight_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        if id is not None:
            _path_params['id'] = id
        if zone_id is not None:
            _path_params['zoneId'] = zone_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_id_zones_zone_id_weight_put_request is not None:
            _body_params = api_v1_campaigns_type_id_zones_zone_id_weight_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/campaigns/{type}/{id}/zones/{zoneId}/weight',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_post(
        self,
        type: StrictStr,
        api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Create a new campaign (smart-default).

        Creates a new campaign with sensible defaults applied for any field you don't send. Everything not supplied defaults to \"all/none\" — see `GET /api/v1/campaigns/{type}/_schema` for the exact field list, which **differs by `type`**.  **Per campaign type:**   - `ron` / `cpm` / `rtb` — required `name` + `ad_type`; the     request body documented below applies.   - `directdeal` — books one of your own ad zones for a date     range. Required `name` + `ad_space_id` + `start_date` +     `total_days`; `ad_type` is taken from the zone and is not     accepted. Geo targeting takes `regions` (region ids from     `/api/v1/lookups/regions`, states and cities included), the     same as the other types; the legacy `countries` codes are     still accepted when `regions` is not sent. See     `GET /api/v1/campaigns/directdeal/_schema`.   - `rtb` — also requires `request_url` (unless `use_type: 1`, a     URL per zone in `zone_urls`), and for banner campaigns     (`ad_type: 2`) `banner_size_ids`. The daily cap applies only     with `use_daily_budget: true`; there is no total budget     (exchange-paced). A user locked to one RTB network always     lands on it.  Every campaign-form field is accepted (`CampaignPanelFields`: day parting and the other options, language / connection / carrier / IP / SubID targeting, pricing extras, RTB config, offers) with the panel's own rules: the minimum daily budget, IP list syntax, source-optimizer ownership, and — on create — a real ad zone location for ron banner (2), ron/rtb link (6) and ron reel (20) campaigns where the network defines locations, link types or reel types (`location_ids` empty or `\"0\"` is a `422` there, as in the panel).   - `flatrate` — **not creatable through the public API** (the     legacy self-service ad-space buy is heading EOL). A POST     returns `422 unsupported_type`.  The campaign starts paused (`is_paused=true`) so you can attach ads via `POST /api/v1/campaigns/{type}/{id}/ads` and verify before activating — unless you send `is_paused`, or the network has new ron campaigns start active. On a network that reviews new campaigns, a new ron campaign also shows `pending_state: 5` (Pending Created) until an admin approves it. Flip the active flag when ready via `PATCH /api/v1/campaigns/{type}/{id}/active`.  **Modes:**   - `?dry_run=1` — validate and return the resolved field map     without inserting. Useful for previewing what an LLM would     create before charging it.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     for this request (422 `unknown_fields` listing them). Without     it the key's default applies: keys created from 2026-10-12 are     strict, older keys ignore unknown fields. 

        :param type: (required)
        :type type: str
        :param api_v1_campaigns_type_post_request: (required)
        :type api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_post_serialize(
            type=type,
            api_v1_campaigns_type_post_request=api_v1_campaigns_type_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_post_with_http_info(
        self,
        type: StrictStr,
        api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Create a new campaign (smart-default).

        Creates a new campaign with sensible defaults applied for any field you don't send. Everything not supplied defaults to \"all/none\" — see `GET /api/v1/campaigns/{type}/_schema` for the exact field list, which **differs by `type`**.  **Per campaign type:**   - `ron` / `cpm` / `rtb` — required `name` + `ad_type`; the     request body documented below applies.   - `directdeal` — books one of your own ad zones for a date     range. Required `name` + `ad_space_id` + `start_date` +     `total_days`; `ad_type` is taken from the zone and is not     accepted. Geo targeting takes `regions` (region ids from     `/api/v1/lookups/regions`, states and cities included), the     same as the other types; the legacy `countries` codes are     still accepted when `regions` is not sent. See     `GET /api/v1/campaigns/directdeal/_schema`.   - `rtb` — also requires `request_url` (unless `use_type: 1`, a     URL per zone in `zone_urls`), and for banner campaigns     (`ad_type: 2`) `banner_size_ids`. The daily cap applies only     with `use_daily_budget: true`; there is no total budget     (exchange-paced). A user locked to one RTB network always     lands on it.  Every campaign-form field is accepted (`CampaignPanelFields`: day parting and the other options, language / connection / carrier / IP / SubID targeting, pricing extras, RTB config, offers) with the panel's own rules: the minimum daily budget, IP list syntax, source-optimizer ownership, and — on create — a real ad zone location for ron banner (2), ron/rtb link (6) and ron reel (20) campaigns where the network defines locations, link types or reel types (`location_ids` empty or `\"0\"` is a `422` there, as in the panel).   - `flatrate` — **not creatable through the public API** (the     legacy self-service ad-space buy is heading EOL). A POST     returns `422 unsupported_type`.  The campaign starts paused (`is_paused=true`) so you can attach ads via `POST /api/v1/campaigns/{type}/{id}/ads` and verify before activating — unless you send `is_paused`, or the network has new ron campaigns start active. On a network that reviews new campaigns, a new ron campaign also shows `pending_state: 5` (Pending Created) until an admin approves it. Flip the active flag when ready via `PATCH /api/v1/campaigns/{type}/{id}/active`.  **Modes:**   - `?dry_run=1` — validate and return the resolved field map     without inserting. Useful for previewing what an LLM would     create before charging it.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     for this request (422 `unknown_fields` listing them). Without     it the key's default applies: keys created from 2026-10-12 are     strict, older keys ignore unknown fields. 

        :param type: (required)
        :type type: str
        :param api_v1_campaigns_type_post_request: (required)
        :type api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_post_serialize(
            type=type,
            api_v1_campaigns_type_post_request=api_v1_campaigns_type_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_post_without_preload_content(
        self,
        type: StrictStr,
        api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest,
        dry_run: Optional[StrictStr] = None,
        strict: Annotated[Optional[StrictStr], Field(description="`1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create a new campaign (smart-default).

        Creates a new campaign with sensible defaults applied for any field you don't send. Everything not supplied defaults to \"all/none\" — see `GET /api/v1/campaigns/{type}/_schema` for the exact field list, which **differs by `type`**.  **Per campaign type:**   - `ron` / `cpm` / `rtb` — required `name` + `ad_type`; the     request body documented below applies.   - `directdeal` — books one of your own ad zones for a date     range. Required `name` + `ad_space_id` + `start_date` +     `total_days`; `ad_type` is taken from the zone and is not     accepted. Geo targeting takes `regions` (region ids from     `/api/v1/lookups/regions`, states and cities included), the     same as the other types; the legacy `countries` codes are     still accepted when `regions` is not sent. See     `GET /api/v1/campaigns/directdeal/_schema`.   - `rtb` — also requires `request_url` (unless `use_type: 1`, a     URL per zone in `zone_urls`), and for banner campaigns     (`ad_type: 2`) `banner_size_ids`. The daily cap applies only     with `use_daily_budget: true`; there is no total budget     (exchange-paced). A user locked to one RTB network always     lands on it.  Every campaign-form field is accepted (`CampaignPanelFields`: day parting and the other options, language / connection / carrier / IP / SubID targeting, pricing extras, RTB config, offers) with the panel's own rules: the minimum daily budget, IP list syntax, source-optimizer ownership, and — on create — a real ad zone location for ron banner (2), ron/rtb link (6) and ron reel (20) campaigns where the network defines locations, link types or reel types (`location_ids` empty or `\"0\"` is a `422` there, as in the panel).   - `flatrate` — **not creatable through the public API** (the     legacy self-service ad-space buy is heading EOL). A POST     returns `422 unsupported_type`.  The campaign starts paused (`is_paused=true`) so you can attach ads via `POST /api/v1/campaigns/{type}/{id}/ads` and verify before activating — unless you send `is_paused`, or the network has new ron campaigns start active. On a network that reviews new campaigns, a new ron campaign also shows `pending_state: 5` (Pending Created) until an admin approves it. Flip the active flag when ready via `PATCH /api/v1/campaigns/{type}/{id}/active`.  **Modes:**   - `?dry_run=1` — validate and return the resolved field map     without inserting. Useful for previewing what an LLM would     create before charging it.   - `?strict=1` / `?strict=0` — reject / ignore unknown field names     for this request (422 `unknown_fields` listing them). Without     it the key's default applies: keys created from 2026-10-12 are     strict, older keys ignore unknown fields. 

        :param type: (required)
        :type type: str
        :param api_v1_campaigns_type_post_request: (required)
        :type api_v1_campaigns_type_post_request: ApiV1CampaignsTypePostRequest
        :param dry_run:
        :type dry_run: str
        :param strict: `1` rejects unknown body fields (422 `unknown_fields`), `0` ignores them, for this request only. Omitted: the key's `strict_fields` setting (strict for keys created from 2026-10-12). 
        :type strict: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_post_serialize(
            type=type,
            api_v1_campaigns_type_post_request=api_v1_campaigns_type_post_request,
            dry_run=dry_run,
            strict=strict,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '200': None,
            '422': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_post_serialize(
        self,
        type,
        api_v1_campaigns_type_post_request,
        dry_run,
        strict,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        # process the query parameters
        if dry_run is not None:
            
            _query_params.append(('dry_run', dry_run))
            
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_campaigns_type_post_request is not None:
            _body_params = api_v1_campaigns_type_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/campaigns/{type}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_schema_ads_get(
        self,
        type: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeSchemaAdsGet200Response:
        """Field metadata for ad creation.

        Discovery endpoint mirroring `/_schema` for campaigns, scoped to ads. Lists every public field a `POST /campaigns/{type}/{campaignId}/ads` accepts, with type, required-flag, default, example, and description. Also returns a `creative_choice` block reminding the caller that exactly one of `banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `video_pool_id` must be set.  Use the campaign-scoped variant `/api/v1/campaigns/{type}/{campaignId}/_schema/ads` to get the same payload narrowed to fields that apply to that specific campaign's ad type (returns `campaign_ad_type` so AI agents know which creative shape is appropriate). For native ad types (`campaign_ad_type` 3 / 21 / 22) the canonical URL field is `native_image_url`; `banner_url` works too because the server auto-routes it to `creatives.image` on a native campaign. 

        :param type: (required)
        :type type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_ads_get_serialize(
            type=type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaAdsGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_schema_ads_get_with_http_info(
        self,
        type: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeSchemaAdsGet200Response]:
        """Field metadata for ad creation.

        Discovery endpoint mirroring `/_schema` for campaigns, scoped to ads. Lists every public field a `POST /campaigns/{type}/{campaignId}/ads` accepts, with type, required-flag, default, example, and description. Also returns a `creative_choice` block reminding the caller that exactly one of `banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `video_pool_id` must be set.  Use the campaign-scoped variant `/api/v1/campaigns/{type}/{campaignId}/_schema/ads` to get the same payload narrowed to fields that apply to that specific campaign's ad type (returns `campaign_ad_type` so AI agents know which creative shape is appropriate). For native ad types (`campaign_ad_type` 3 / 21 / 22) the canonical URL field is `native_image_url`; `banner_url` works too because the server auto-routes it to `creatives.image` on a native campaign. 

        :param type: (required)
        :type type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_ads_get_serialize(
            type=type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaAdsGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_schema_ads_get_without_preload_content(
        self,
        type: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Field metadata for ad creation.

        Discovery endpoint mirroring `/_schema` for campaigns, scoped to ads. Lists every public field a `POST /campaigns/{type}/{campaignId}/ads` accepts, with type, required-flag, default, example, and description. Also returns a `creative_choice` block reminding the caller that exactly one of `banner_pool_id` / `creative_id` / `banner_url` / `banner_html` / `video_pool_id` must be set.  Use the campaign-scoped variant `/api/v1/campaigns/{type}/{campaignId}/_schema/ads` to get the same payload narrowed to fields that apply to that specific campaign's ad type (returns `campaign_ad_type` so AI agents know which creative shape is appropriate). For native ad types (`campaign_ad_type` 3 / 21 / 22) the canonical URL field is `native_image_url`; `banner_url` works too because the server auto-routes it to `creatives.image` on a native campaign. 

        :param type: (required)
        :type type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_ads_get_serialize(
            type=type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaAdsGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_schema_ads_get_serialize(
        self,
        type,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/_schema/ads',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_campaigns_type_schema_get(
        self,
        type: StrictStr,
        ad_type: Annotated[Optional[StrictInt], Field(description="Only list the fields that apply to this ad type.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiV1CampaignsTypeSchemaGet200Response:
        """Field metadata for create/update.

        Discovery endpoint for AI agents and integrators. Returns the canonical list of public field names a `POST /api/v1/campaigns/{type}` accepts, with type, required-flag, default value, an example, and a one-line description. `ad_type` enumerates the active ad-type ids on the caller's tenant.  The field set differs by `type` — `directdeal` returns its own ad-zone-booking fields (`ad_space_id`, `start_date`, `total_days`, …), not the RON-shaped targeting fields. `flatrate` is not creatable through the public API: its `_schema` returns `{creatable: false}` instead of a field list.  For `ron` / `cpm` / `rtb` the list is built from the campaign table's real columns and the network's modules: a field the type cannot store (keywords or schedule dates on rtb, total budget on rtb) or the network does not offer is not listed. It is exactly the set `?strict=1` accepts on **both** `POST` and `PATCH`. `ad_types` / `selling_types` / `not_selling_types` on a field mean it only applies to those ad types / pay types; sending it to any other campaign is a `422`. `?ad_type=<id>` narrows the list to one ad type.  Use this to drive form UIs, validate agent-generated payloads client-side, or feed into a function-calling LLM. 

        :param type: (required)
        :type type: str
        :param ad_type: Only list the fields that apply to this ad type.
        :type ad_type: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_get_serialize(
            type=type,
            ad_type=ad_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_campaigns_type_schema_get_with_http_info(
        self,
        type: StrictStr,
        ad_type: Annotated[Optional[StrictInt], Field(description="Only list the fields that apply to this ad type.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiV1CampaignsTypeSchemaGet200Response]:
        """Field metadata for create/update.

        Discovery endpoint for AI agents and integrators. Returns the canonical list of public field names a `POST /api/v1/campaigns/{type}` accepts, with type, required-flag, default value, an example, and a one-line description. `ad_type` enumerates the active ad-type ids on the caller's tenant.  The field set differs by `type` — `directdeal` returns its own ad-zone-booking fields (`ad_space_id`, `start_date`, `total_days`, …), not the RON-shaped targeting fields. `flatrate` is not creatable through the public API: its `_schema` returns `{creatable: false}` instead of a field list.  For `ron` / `cpm` / `rtb` the list is built from the campaign table's real columns and the network's modules: a field the type cannot store (keywords or schedule dates on rtb, total budget on rtb) or the network does not offer is not listed. It is exactly the set `?strict=1` accepts on **both** `POST` and `PATCH`. `ad_types` / `selling_types` / `not_selling_types` on a field mean it only applies to those ad types / pay types; sending it to any other campaign is a `422`. `?ad_type=<id>` narrows the list to one ad type.  Use this to drive form UIs, validate agent-generated payloads client-side, or feed into a function-calling LLM. 

        :param type: (required)
        :type type: str
        :param ad_type: Only list the fields that apply to this ad type.
        :type ad_type: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_get_serialize(
            type=type,
            ad_type=ad_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_campaigns_type_schema_get_without_preload_content(
        self,
        type: StrictStr,
        ad_type: Annotated[Optional[StrictInt], Field(description="Only list the fields that apply to this ad type.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Field metadata for create/update.

        Discovery endpoint for AI agents and integrators. Returns the canonical list of public field names a `POST /api/v1/campaigns/{type}` accepts, with type, required-flag, default value, an example, and a one-line description. `ad_type` enumerates the active ad-type ids on the caller's tenant.  The field set differs by `type` — `directdeal` returns its own ad-zone-booking fields (`ad_space_id`, `start_date`, `total_days`, …), not the RON-shaped targeting fields. `flatrate` is not creatable through the public API: its `_schema` returns `{creatable: false}` instead of a field list.  For `ron` / `cpm` / `rtb` the list is built from the campaign table's real columns and the network's modules: a field the type cannot store (keywords or schedule dates on rtb, total budget on rtb) or the network does not offer is not listed. It is exactly the set `?strict=1` accepts on **both** `POST` and `PATCH`. `ad_types` / `selling_types` / `not_selling_types` on a field mean it only applies to those ad types / pay types; sending it to any other campaign is a `422`. `?ad_type=<id>` narrows the list to one ad type.  Use this to drive form UIs, validate agent-generated payloads client-side, or feed into a function-calling LLM. 

        :param type: (required)
        :type type: str
        :param ad_type: Only list the fields that apply to this ad type.
        :type ad_type: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_campaigns_type_schema_get_serialize(
            type=type,
            ad_type=ad_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CampaignsTypeSchemaGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_campaigns_type_schema_get_serialize(
        self,
        type,
        ad_type,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if type is not None:
            _path_params['type'] = type
        # process the query parameters
        if ad_type is not None:
            
            _query_params.append(('ad_type', ad_type))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/campaigns/{type}/_schema',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_rtb_test_rtb_context_get(
        self,
        adtypeid: Optional[StrictInt] = None,
        rtbtype: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Context for testing an endpoint before the campaign exists.

        Same as the per-campaign context, for an unsaved endpoint — resolves `adtypeid` to the bid-request ad type. Same handler as the panel.

        :param adtypeid:
        :type adtypeid: int
        :param rtbtype:
        :type rtbtype: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_context_get_serialize(
            adtypeid=adtypeid,
            rtbtype=rtbtype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_rtb_test_rtb_context_get_with_http_info(
        self,
        adtypeid: Optional[StrictInt] = None,
        rtbtype: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Context for testing an endpoint before the campaign exists.

        Same as the per-campaign context, for an unsaved endpoint — resolves `adtypeid` to the bid-request ad type. Same handler as the panel.

        :param adtypeid:
        :type adtypeid: int
        :param rtbtype:
        :type rtbtype: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_context_get_serialize(
            adtypeid=adtypeid,
            rtbtype=rtbtype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_rtb_test_rtb_context_get_without_preload_content(
        self,
        adtypeid: Optional[StrictInt] = None,
        rtbtype: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Context for testing an endpoint before the campaign exists.

        Same as the per-campaign context, for an unsaved endpoint — resolves `adtypeid` to the bid-request ad type. Same handler as the panel.

        :param adtypeid:
        :type adtypeid: int
        :param rtbtype:
        :type rtbtype: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_context_get_serialize(
            adtypeid=adtypeid,
            rtbtype=rtbtype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_rtb_test_rtb_context_get_serialize(
        self,
        adtypeid,
        rtbtype,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if adtypeid is not None:
            
            _query_params.append(('adtypeid', adtypeid))
            
        if rtbtype is not None:
            
            _query_params.append(('rtbtype', rtbtype))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/rtb/test-rtb/context',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_rtb_test_rtb_post(
        self,
        api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RtbTestResult:
        """Fire a test bid request at any endpoint URL.

        The tester for an endpoint you are about to save on an RTB campaign: `url` (or `override_url`) + `rtbtype` + `adtypeid` come from the body instead of a campaign. Same safety rules and result as `POST /api/v1/campaigns/rtb/{id}/test-rtb`. Same handler as the panel. 

        :param api_v1_rtb_test_rtb_post_request: (required)
        :type api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_post_serialize(
            api_v1_rtb_test_rtb_post_request=api_v1_rtb_test_rtb_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_rtb_test_rtb_post_with_http_info(
        self,
        api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RtbTestResult]:
        """Fire a test bid request at any endpoint URL.

        The tester for an endpoint you are about to save on an RTB campaign: `url` (or `override_url`) + `rtbtype` + `adtypeid` come from the body instead of a campaign. Same safety rules and result as `POST /api/v1/campaigns/rtb/{id}/test-rtb`. Same handler as the panel. 

        :param api_v1_rtb_test_rtb_post_request: (required)
        :type api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_post_serialize(
            api_v1_rtb_test_rtb_post_request=api_v1_rtb_test_rtb_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_rtb_test_rtb_post_without_preload_content(
        self,
        api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Fire a test bid request at any endpoint URL.

        The tester for an endpoint you are about to save on an RTB campaign: `url` (or `override_url`) + `rtbtype` + `adtypeid` come from the body instead of a campaign. Same safety rules and result as `POST /api/v1/campaigns/rtb/{id}/test-rtb`. Same handler as the panel. 

        :param api_v1_rtb_test_rtb_post_request: (required)
        :type api_v1_rtb_test_rtb_post_request: ApiV1RtbTestRtbPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_rtb_test_rtb_post_serialize(
            api_v1_rtb_test_rtb_post_request=api_v1_rtb_test_rtb_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RtbTestResult",
            '403': "Error",
            '404': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_rtb_test_rtb_post_serialize(
        self,
        api_v1_rtb_test_rtb_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_rtb_test_rtb_post_request is not None:
            _body_params = api_v1_rtb_test_rtb_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/rtb/test-rtb',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_v1_tools_replace_domain_put(
        self,
        api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Replace the landing domain across your RON ads.

        The panel's Tools → Replace domain: in every live RON ad whose destination URL contains `search`, the first occurrence is replaced with `replace` (a domain). `campaignids` narrows it to those campaigns; empty = every RON ad of the account. A key pinned to campaigns must list `campaignids`, all within its pin (403 `forbidden_resource` otherwise).  Same safeguards as a single-ad save: a resulting URL on a blocked domain fails the whole call before anything is written, and the changed ads go back to review unless the account is auto-validated. 

        :param api_v1_tools_replace_domain_put_request: (required)
        :type api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_tools_replace_domain_put_serialize(
            api_v1_tools_replace_domain_put_request=api_v1_tools_replace_domain_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_v1_tools_replace_domain_put_with_http_info(
        self,
        api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Replace the landing domain across your RON ads.

        The panel's Tools → Replace domain: in every live RON ad whose destination URL contains `search`, the first occurrence is replaced with `replace` (a domain). `campaignids` narrows it to those campaigns; empty = every RON ad of the account. A key pinned to campaigns must list `campaignids`, all within its pin (403 `forbidden_resource` otherwise).  Same safeguards as a single-ad save: a resulting URL on a blocked domain fails the whole call before anything is written, and the changed ads go back to review unless the account is auto-validated. 

        :param api_v1_tools_replace_domain_put_request: (required)
        :type api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_tools_replace_domain_put_serialize(
            api_v1_tools_replace_domain_put_request=api_v1_tools_replace_domain_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_v1_tools_replace_domain_put_without_preload_content(
        self,
        api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Replace the landing domain across your RON ads.

        The panel's Tools → Replace domain: in every live RON ad whose destination URL contains `search`, the first occurrence is replaced with `replace` (a domain). `campaignids` narrows it to those campaigns; empty = every RON ad of the account. A key pinned to campaigns must list `campaignids`, all within its pin (403 `forbidden_resource` otherwise).  Same safeguards as a single-ad save: a resulting URL on a blocked domain fails the whole call before anything is written, and the changed ads go back to review unless the account is auto-validated. 

        :param api_v1_tools_replace_domain_put_request: (required)
        :type api_v1_tools_replace_domain_put_request: ApiV1ToolsReplaceDomainPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_tools_replace_domain_put_serialize(
            api_v1_tools_replace_domain_put_request=api_v1_tools_replace_domain_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_tools_replace_domain_put_serialize(
        self,
        api_v1_tools_replace_domain_put_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_tools_replace_domain_put_request is not None:
            _body_params = api_v1_tools_replace_domain_put_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/tools/replace-domain',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



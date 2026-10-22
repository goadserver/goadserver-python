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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from goadserver.models.api_v1_publisher_offers_postback_log_get200_response import ApiV1PublisherOffersPostbackLogGet200Response
from goadserver.models.stats_response import StatsResponse

from goadserver.api_client import ApiClient, RequestSerialized
from goadserver.api_response import ApiResponse
from goadserver.rest import RESTResponseType


class StatsAffiliateApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_v1_publisher_offers_postback_log_get(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        site_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Only postbacks for this site.")] = None,
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
    ) -> ApiV1PublisherOffersPostbackLogGet200Response:
        """Postback log — the conversion postbacks fired to your URLs.

        The panel's Offer Reports → Postback Log. One row per postback the platform fired to the publisher's postback URL, newest first, capped at 1000 rows (no paging). `status` is `Success` for HTTP 200 (or an unrecorded state) and `Failed (<state>)` otherwise. Date params that are missing or not `YYYY-MM-DD` fall back to the last 7 days. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param site_id: Only postbacks for this site.
        :type site_id: int
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

        _param = self._api_v1_publisher_offers_postback_log_get_serialize(
            var_from=var_from,
            to=to,
            site_id=site_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1PublisherOffersPostbackLogGet200Response",
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
    def api_v1_publisher_offers_postback_log_get_with_http_info(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        site_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Only postbacks for this site.")] = None,
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
    ) -> ApiResponse[ApiV1PublisherOffersPostbackLogGet200Response]:
        """Postback log — the conversion postbacks fired to your URLs.

        The panel's Offer Reports → Postback Log. One row per postback the platform fired to the publisher's postback URL, newest first, capped at 1000 rows (no paging). `status` is `Success` for HTTP 200 (or an unrecorded state) and `Failed (<state>)` otherwise. Date params that are missing or not `YYYY-MM-DD` fall back to the last 7 days. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param site_id: Only postbacks for this site.
        :type site_id: int
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

        _param = self._api_v1_publisher_offers_postback_log_get_serialize(
            var_from=var_from,
            to=to,
            site_id=site_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1PublisherOffersPostbackLogGet200Response",
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
    def api_v1_publisher_offers_postback_log_get_without_preload_content(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        site_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Only postbacks for this site.")] = None,
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
        """Postback log — the conversion postbacks fired to your URLs.

        The panel's Offer Reports → Postback Log. One row per postback the platform fired to the publisher's postback URL, newest first, capped at 1000 rows (no paging). `status` is `Success` for HTTP 200 (or an unrecorded state) and `Failed (<state>)` otherwise. Date params that are missing or not `YYYY-MM-DD` fall back to the last 7 days. 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param site_id: Only postbacks for this site.
        :type site_id: int
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

        _param = self._api_v1_publisher_offers_postback_log_get_serialize(
            var_from=var_from,
            to=to,
            site_id=site_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1PublisherOffersPostbackLogGet200Response",
            '401': "Error",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_publisher_offers_postback_log_get_serialize(
        self,
        var_from,
        to,
        site_id,
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
            
        if site_id is not None:
            
            _query_params.append(('site_id', site_id))
            
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
            resource_path='/api/v1/publisher/offers/postback-log',
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
    def api_v1_publisher_offers_stats_get(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return. Multi-pick — leave empty for all.")] = None,
        filter_offer_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer ID. Look up via `GET /api/v1/offers`.")] = None,
        filter_offer_type_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer-type ID.")] = None,
        filter_website: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Site ID — look up via `GET /api/v1/sites`.")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_subid: Annotated[Optional[StrictStr], Field(description="SubID (free-form publisher identifier).")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Field name. Prefix with `-` for descending (e.g. `-views`).")] = None,
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
    ) -> StatsResponse:
        """Affiliate / smartlink offer performance — publisher side.

        Affiliate / smartlink offer performance for the publisher. `earned` and `epc` are in the account currency (currency units, not cents). 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. 
        :type group_by: List[str]
        :param metrics: Metrics to return. Multi-pick — leave empty for all.
        :type metrics: List[str]
        :param filter_offer_id: Offer ID. Look up via `GET /api/v1/offers`.
        :type filter_offer_id: int
        :param filter_offer_type_id: Offer-type ID.
        :type filter_offer_type_id: int
        :param filter_website: Site ID — look up via `GET /api/v1/sites`.
        :type filter_website: int
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_subid: SubID (free-form publisher identifier).
        :type filter_subid: str
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Field name. Prefix with `-` for descending (e.g. `-views`).
        :type sort: str
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

        _param = self._api_v1_publisher_offers_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_offer_id=filter_offer_id,
            filter_offer_type_id=filter_offer_type_id,
            filter_website=filter_website,
            filter_adzone_id=filter_adzone_id,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_subid=filter_subid,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
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
    def api_v1_publisher_offers_stats_get_with_http_info(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return. Multi-pick — leave empty for all.")] = None,
        filter_offer_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer ID. Look up via `GET /api/v1/offers`.")] = None,
        filter_offer_type_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer-type ID.")] = None,
        filter_website: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Site ID — look up via `GET /api/v1/sites`.")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_subid: Annotated[Optional[StrictStr], Field(description="SubID (free-form publisher identifier).")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Field name. Prefix with `-` for descending (e.g. `-views`).")] = None,
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
    ) -> ApiResponse[StatsResponse]:
        """Affiliate / smartlink offer performance — publisher side.

        Affiliate / smartlink offer performance for the publisher. `earned` and `epc` are in the account currency (currency units, not cents). 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. 
        :type group_by: List[str]
        :param metrics: Metrics to return. Multi-pick — leave empty for all.
        :type metrics: List[str]
        :param filter_offer_id: Offer ID. Look up via `GET /api/v1/offers`.
        :type filter_offer_id: int
        :param filter_offer_type_id: Offer-type ID.
        :type filter_offer_type_id: int
        :param filter_website: Site ID — look up via `GET /api/v1/sites`.
        :type filter_website: int
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_subid: SubID (free-form publisher identifier).
        :type filter_subid: str
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Field name. Prefix with `-` for descending (e.g. `-views`).
        :type sort: str
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

        _param = self._api_v1_publisher_offers_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_offer_id=filter_offer_id,
            filter_offer_type_id=filter_offer_type_id,
            filter_website=filter_website,
            filter_adzone_id=filter_adzone_id,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_subid=filter_subid,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
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
    def api_v1_publisher_offers_stats_get_without_preload_content(
        self,
        var_from: Annotated[Optional[date], Field(description="ISO date — inclusive start. Defaults to 7 days ago.")] = None,
        to: Annotated[Optional[date], Field(description="ISO date — inclusive end. Defaults to today. Max range 92 days.")] = None,
        interval: Optional[StrictStr] = None,
        group_by: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=8)]], Field(description="Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. ")] = None,
        metrics: Annotated[Optional[List[StrictStr]], Field(description="Metrics to return. Multi-pick — leave empty for all.")] = None,
        filter_offer_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer ID. Look up via `GET /api/v1/offers`.")] = None,
        filter_offer_type_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Offer-type ID.")] = None,
        filter_website: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Site ID — look up via `GET /api/v1/sites`.")] = None,
        filter_adzone_id: Annotated[Optional[StrictStr], Field(description="Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.")] = None,
        filter_device: Annotated[Optional[StrictInt], Field(description="Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | ")] = None,
        filter_country: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]], Field(description="ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).")] = None,
        filter_subid: Annotated[Optional[StrictStr], Field(description="SubID (free-form publisher identifier).")] = None,
        format: Optional[StrictStr] = None,
        page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Field name. Prefix with `-` for descending (e.g. `-views`).")] = None,
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
        """Affiliate / smartlink offer performance — publisher side.

        Affiliate / smartlink offer performance for the publisher. `earned` and `epc` are in the account currency (currency units, not cents). 

        :param var_from: ISO date — inclusive start. Defaults to 7 days ago.
        :type var_from: date
        :param to: ISO date — inclusive end. Defaults to today. Max range 92 days.
        :type to: date
        :param interval:
        :type interval: str
        :param group_by: Dimensions to aggregate by. Multi-pick up to 8. High-cardinality dims (`subid`, `clickid`, `sid*`, `domain`) explode row count. `clickid` is the advertiser-side click id passed back on the conversion (the panel's ClickID tab) and comes back as plain text. 
        :type group_by: List[str]
        :param metrics: Metrics to return. Multi-pick — leave empty for all.
        :type metrics: List[str]
        :param filter_offer_id: Offer ID. Look up via `GET /api/v1/offers`.
        :type filter_offer_id: int
        :param filter_offer_type_id: Offer-type ID.
        :type filter_offer_type_id: int
        :param filter_website: Site ID — look up via `GET /api/v1/sites`.
        :type filter_website: int
        :param filter_adzone_id: Adspace ID, or comma-separated list. Look up via `GET /api/v1/adspaces`.
        :type filter_adzone_id: str
        :param filter_device: Device type:  | ID | Device | |----|--------| | 1  | Computer | | 2  | Tablet | | 3  | Phone | | 4  | Console | | 5  | Wearable | | 6  | TV | 
        :type filter_device: int
        :param filter_country: ISO-3166 alpha-2 country code (e.g. `US`, `DE`, `BR`).
        :type filter_country: str
        :param filter_subid: SubID (free-form publisher identifier).
        :type filter_subid: str
        :param format:
        :type format: str
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param sort: Field name. Prefix with `-` for descending (e.g. `-views`).
        :type sort: str
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

        _param = self._api_v1_publisher_offers_stats_get_serialize(
            var_from=var_from,
            to=to,
            interval=interval,
            group_by=group_by,
            metrics=metrics,
            filter_offer_id=filter_offer_id,
            filter_offer_type_id=filter_offer_type_id,
            filter_website=filter_website,
            filter_adzone_id=filter_adzone_id,
            filter_device=filter_device,
            filter_country=filter_country,
            filter_subid=filter_subid,
            format=format,
            page=page,
            per_page=per_page,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_publisher_offers_stats_get_serialize(
        self,
        var_from,
        to,
        interval,
        group_by,
        metrics,
        filter_offer_id,
        filter_offer_type_id,
        filter_website,
        filter_adzone_id,
        filter_device,
        filter_country,
        filter_subid,
        format,
        page,
        per_page,
        sort,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'group_by': 'csv',
            'metrics': 'csv',
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
            
        if interval is not None:
            
            _query_params.append(('interval', interval))
            
        if group_by is not None:
            
            _query_params.append(('group_by', group_by))
            
        if metrics is not None:
            
            _query_params.append(('metrics', metrics))
            
        if filter_offer_id is not None:
            
            _query_params.append(('filter[offer_id]', filter_offer_id))
            
        if filter_offer_type_id is not None:
            
            _query_params.append(('filter[offer_type_id]', filter_offer_type_id))
            
        if filter_website is not None:
            
            _query_params.append(('filter[website]', filter_website))
            
        if filter_adzone_id is not None:
            
            _query_params.append(('filter[adzone_id]', filter_adzone_id))
            
        if filter_device is not None:
            
            _query_params.append(('filter[device]', filter_device))
            
        if filter_country is not None:
            
            _query_params.append(('filter[country]', filter_country))
            
        if filter_subid is not None:
            
            _query_params.append(('filter[subid]', filter_subid))
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
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
            resource_path='/api/v1/publisher/offers/stats',
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



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
from pydantic import Field, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, Optional, Tuple, Union
from typing_extensions import Annotated
from goadserver.models.api_v1_campaigns_type_campaign_id_ads_ad_id_clone_post200_response import ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response
from goadserver.models.api_v1_creative_pools_get200_response import ApiV1CreativePoolsGet200Response
from goadserver.models.api_v1_creative_pools_id_add_creatives_post_request import ApiV1CreativePoolsIdAddCreativesPostRequest
from goadserver.models.api_v1_creative_pools_id_add_urls_post_request import ApiV1CreativePoolsIdAddUrlsPostRequest
from goadserver.models.api_v1_creative_pools_id_clone_post201_response import ApiV1CreativePoolsIdClonePost201Response
from goadserver.models.api_v1_creative_pools_id_delete200_response import ApiV1CreativePoolsIdDelete200Response
from goadserver.models.api_v1_creative_pools_id_get200_response import ApiV1CreativePoolsIdGet200Response
from goadserver.models.api_v1_creative_pools_id_items_item_id_put_request import ApiV1CreativePoolsIdItemsItemIdPutRequest
from goadserver.models.api_v1_creative_pools_id_items_mass_action_put_request import ApiV1CreativePoolsIdItemsMassActionPutRequest
from goadserver.models.api_v1_creative_pools_id_items_post_request import ApiV1CreativePoolsIdItemsPostRequest
from goadserver.models.api_v1_creative_pools_id_items_recover_post_request import ApiV1CreativePoolsIdItemsRecoverPostRequest
from goadserver.models.api_v1_creative_pools_id_put_request import ApiV1CreativePoolsIdPutRequest
from goadserver.models.api_v1_creative_pools_id_used_in_get200_response import ApiV1CreativePoolsIdUsedInGet200Response
from goadserver.models.api_v1_creative_pools_post_request import ApiV1CreativePoolsPostRequest
from goadserver.models.api_v1_creatives_bulk_delete_post_request import ApiV1CreativesBulkDeletePostRequest
from goadserver.models.api_v1_creatives_bulk_undelete_post_request import ApiV1CreativesBulkUndeletePostRequest
from goadserver.models.api_v1_creatives_get200_response import ApiV1CreativesGet200Response

from goadserver.api_client import ApiClient, RequestSerialized
from goadserver.api_response import ApiResponse
from goadserver.rest import RESTResponseType


class CreativePoolsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_v1_creative_pools_get(
        self,
        filter_type: Optional[StrictStr] = None,
        filter_types: Annotated[Optional[StrictStr], Field(description="Comma-separated list of pool types (banner, video, reel, image, native, creator).")] = None,
        filter_title: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Same as filter_title.")] = None,
        filter_orientation: Annotated[Optional[StrictStr], Field(description="The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        fit_orientation: Annotated[Optional[StrictStr], Field(description="Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Any] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
    ) -> ApiV1CreativePoolsGet200Response:
        """List creative pools.

        Returns every creative pool owned by the caller. Each row carries `items_count` (live items, `is_deleted=0`) and `total_sizes` (count of distinct banner sizes). Tags are returned both as the raw CSV string (`tags`) and as an array (`tagids`).  Filters use the `filter_` prefix (`filter_type`, `filter_title`, `filter_id`, `filter_orientation`); `search` matches the title. Sort with `sort_by` / `sort_dir`. 

        :param filter_type:
        :type filter_type: str
        :param filter_types: Comma-separated list of pool types (banner, video, reel, image, native, creator).
        :type filter_types: str
        :param filter_title: Title contains.
        :type filter_title: str
        :param filter_id:
        :type filter_id: int
        :param filter_name: Same as filter_title.
        :type filter_name: str
        :param filter_orientation: The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.
        :type filter_orientation: str
        :param state: deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.
        :type state: str
        :param search: Title contains.
        :type search: str
        :param fit_orientation: Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.
        :type fit_orientation: str
        :param select_stats: 1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: ApiV1CreativePoolsGetPerPageParameter
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_get_serialize(
            filter_type=filter_type,
            filter_types=filter_types,
            filter_title=filter_title,
            filter_id=filter_id,
            filter_name=filter_name,
            filter_orientation=filter_orientation,
            state=state,
            search=search,
            fit_orientation=fit_orientation,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsGet200Response",
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
    def api_v1_creative_pools_get_with_http_info(
        self,
        filter_type: Optional[StrictStr] = None,
        filter_types: Annotated[Optional[StrictStr], Field(description="Comma-separated list of pool types (banner, video, reel, image, native, creator).")] = None,
        filter_title: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Same as filter_title.")] = None,
        filter_orientation: Annotated[Optional[StrictStr], Field(description="The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        fit_orientation: Annotated[Optional[StrictStr], Field(description="Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Any] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
    ) -> ApiResponse[ApiV1CreativePoolsGet200Response]:
        """List creative pools.

        Returns every creative pool owned by the caller. Each row carries `items_count` (live items, `is_deleted=0`) and `total_sizes` (count of distinct banner sizes). Tags are returned both as the raw CSV string (`tags`) and as an array (`tagids`).  Filters use the `filter_` prefix (`filter_type`, `filter_title`, `filter_id`, `filter_orientation`); `search` matches the title. Sort with `sort_by` / `sort_dir`. 

        :param filter_type:
        :type filter_type: str
        :param filter_types: Comma-separated list of pool types (banner, video, reel, image, native, creator).
        :type filter_types: str
        :param filter_title: Title contains.
        :type filter_title: str
        :param filter_id:
        :type filter_id: int
        :param filter_name: Same as filter_title.
        :type filter_name: str
        :param filter_orientation: The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.
        :type filter_orientation: str
        :param state: deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.
        :type state: str
        :param search: Title contains.
        :type search: str
        :param fit_orientation: Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.
        :type fit_orientation: str
        :param select_stats: 1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: ApiV1CreativePoolsGetPerPageParameter
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_get_serialize(
            filter_type=filter_type,
            filter_types=filter_types,
            filter_title=filter_title,
            filter_id=filter_id,
            filter_name=filter_name,
            filter_orientation=filter_orientation,
            state=state,
            search=search,
            fit_orientation=fit_orientation,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsGet200Response",
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
    def api_v1_creative_pools_get_without_preload_content(
        self,
        filter_type: Optional[StrictStr] = None,
        filter_types: Annotated[Optional[StrictStr], Field(description="Comma-separated list of pool types (banner, video, reel, image, native, creator).")] = None,
        filter_title: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Same as filter_title.")] = None,
        filter_orientation: Annotated[Optional[StrictStr], Field(description="The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.")] = None,
        state: Annotated[Optional[StrictStr], Field(description="deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Title contains.")] = None,
        fit_orientation: Annotated[Optional[StrictStr], Field(description="Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Any] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
        """List creative pools.

        Returns every creative pool owned by the caller. Each row carries `items_count` (live items, `is_deleted=0`) and `total_sizes` (count of distinct banner sizes). Tags are returned both as the raw CSV string (`tags`) and as an array (`tagids`).  Filters use the `filter_` prefix (`filter_type`, `filter_title`, `filter_id`, `filter_orientation`); `search` matches the title. Sort with `sort_by` / `sort_dir`. 

        :param filter_type:
        :type filter_type: str
        :param filter_types: Comma-separated list of pool types (banner, video, reel, image, native, creator).
        :type filter_types: str
        :param filter_title: Title contains.
        :type filter_title: str
        :param filter_id:
        :type filter_id: int
        :param filter_name: Same as filter_title.
        :type filter_name: str
        :param filter_orientation: The pool's own orientation label — empty on most pools; fit_orientation looks at the creatives instead.
        :type filter_orientation: str
        :param state: deleted = the archived pools (deleted from the pool page or archived from Cleanup), to restore with POST /{id}/recover. Purged pools are in neither list.
        :type state: str
        :param search: Title contains.
        :type search: str
        :param fit_orientation: Adds how many of each pool's servable creatives have this orientation, so a pool that would produce an unservable ad can be told apart.
        :type fit_orientation: str
        :param select_stats: 1 = add views, clicks and conversions per pool for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: ApiV1CreativePoolsGetPerPageParameter
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_get_serialize(
            filter_type=filter_type,
            filter_types=filter_types,
            filter_title=filter_title,
            filter_id=filter_id,
            filter_name=filter_name,
            filter_orientation=filter_orientation,
            state=state,
            search=search,
            fit_orientation=fit_orientation,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsGet200Response",
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_get_serialize(
        self,
        filter_type,
        filter_types,
        filter_title,
        filter_id,
        filter_name,
        filter_orientation,
        state,
        search,
        fit_orientation,
        select_stats,
        var_from,
        to,
        page,
        per_page,
        sort_by,
        sort_dir,
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
        if filter_type is not None:
            
            _query_params.append(('filter_type', filter_type))
            
        if filter_types is not None:
            
            _query_params.append(('filter_types', filter_types))
            
        if filter_title is not None:
            
            _query_params.append(('filter_title', filter_title))
            
        if filter_id is not None:
            
            _query_params.append(('filter_id', filter_id))
            
        if filter_name is not None:
            
            _query_params.append(('filter_name', filter_name))
            
        if filter_orientation is not None:
            
            _query_params.append(('filter_orientation', filter_orientation))
            
        if state is not None:
            
            _query_params.append(('state', state))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if fit_orientation is not None:
            
            _query_params.append(('fit_orientation', fit_orientation))
            
        if select_stats is not None:
            
            _query_params.append(('select_stats', select_stats))
            
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
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if sort_dir is not None:
            
            _query_params.append(('sort_dir', sort_dir))
            
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
            resource_path='/api/v1/creative-pools',
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
    def api_v1_creative_pools_id_add_creatives_post(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest,
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
        """Add media-bank creatives to a pool.

        Adds existing creatives (from `GET /api/v1/creatives` or `POST /api/v1/creatives/upload`) to the pool by id — the panel's \"Add from library\". Only creatives of the pool's own type are added; ids that are not yours, not that type, or already in the pool are skipped silently (`total` counts what was added). New items need moderation unless the account auto-validates. A key pinned to `creative_ids` may only add creatives on its pin (403 otherwise). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_creatives_post_request: (required)
        :type api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest
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

        _param = self._api_v1_creative_pools_id_add_creatives_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_creatives_post_request=api_v1_creative_pools_id_add_creatives_post_request,
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
    def api_v1_creative_pools_id_add_creatives_post_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest,
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
        """Add media-bank creatives to a pool.

        Adds existing creatives (from `GET /api/v1/creatives` or `POST /api/v1/creatives/upload`) to the pool by id — the panel's \"Add from library\". Only creatives of the pool's own type are added; ids that are not yours, not that type, or already in the pool are skipped silently (`total` counts what was added). New items need moderation unless the account auto-validates. A key pinned to `creative_ids` may only add creatives on its pin (403 otherwise). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_creatives_post_request: (required)
        :type api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest
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

        _param = self._api_v1_creative_pools_id_add_creatives_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_creatives_post_request=api_v1_creative_pools_id_add_creatives_post_request,
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
    def api_v1_creative_pools_id_add_creatives_post_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest,
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
        """Add media-bank creatives to a pool.

        Adds existing creatives (from `GET /api/v1/creatives` or `POST /api/v1/creatives/upload`) to the pool by id — the panel's \"Add from library\". Only creatives of the pool's own type are added; ids that are not yours, not that type, or already in the pool are skipped silently (`total` counts what was added). New items need moderation unless the account auto-validates. A key pinned to `creative_ids` may only add creatives on its pin (403 otherwise). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_creatives_post_request: (required)
        :type api_v1_creative_pools_id_add_creatives_post_request: ApiV1CreativePoolsIdAddCreativesPostRequest
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

        _param = self._api_v1_creative_pools_id_add_creatives_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_creatives_post_request=api_v1_creative_pools_id_add_creatives_post_request,
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


    def _api_v1_creative_pools_id_add_creatives_post_serialize(
        self,
        id,
        api_v1_creative_pools_id_add_creatives_post_request,
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
        if api_v1_creative_pools_id_add_creatives_post_request is not None:
            _body_params = api_v1_creative_pools_id_add_creatives_post_request


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
            resource_path='/api/v1/creative-pools/{id}/add-creatives',
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
    def api_v1_creative_pools_id_add_urls_post(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest,
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
        """Add hotlinked image / video / HTML URLs to a pool.

        Bulk import of hotlinked creatives — the panel's \"Add URLs\". One URL per line in `urls`; each becomes a media-bank creative plus a pool item. The protocol is normalised to https. The file extension decides the kind: jpg/jpeg/png/bmp/webp image, gif animated image, mp4 video; anything else (or an image into a video pool) is reported back in `err_data`. `type: html_url` hotlinks the URL as an iframe banner instead. Creator pools refuse URLs (422). Keys pinned to `creative_ids` cannot use this (it creates creatives). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_urls_post_request: (required)
        :type api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest
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

        _param = self._api_v1_creative_pools_id_add_urls_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_urls_post_request=api_v1_creative_pools_id_add_urls_post_request,
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
    def api_v1_creative_pools_id_add_urls_post_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest,
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
        """Add hotlinked image / video / HTML URLs to a pool.

        Bulk import of hotlinked creatives — the panel's \"Add URLs\". One URL per line in `urls`; each becomes a media-bank creative plus a pool item. The protocol is normalised to https. The file extension decides the kind: jpg/jpeg/png/bmp/webp image, gif animated image, mp4 video; anything else (or an image into a video pool) is reported back in `err_data`. `type: html_url` hotlinks the URL as an iframe banner instead. Creator pools refuse URLs (422). Keys pinned to `creative_ids` cannot use this (it creates creatives). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_urls_post_request: (required)
        :type api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest
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

        _param = self._api_v1_creative_pools_id_add_urls_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_urls_post_request=api_v1_creative_pools_id_add_urls_post_request,
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
    def api_v1_creative_pools_id_add_urls_post_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest,
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
        """Add hotlinked image / video / HTML URLs to a pool.

        Bulk import of hotlinked creatives — the panel's \"Add URLs\". One URL per line in `urls`; each becomes a media-bank creative plus a pool item. The protocol is normalised to https. The file extension decides the kind: jpg/jpeg/png/bmp/webp image, gif animated image, mp4 video; anything else (or an image into a video pool) is reported back in `err_data`. `type: html_url` hotlinks the URL as an iframe banner instead. Creator pools refuse URLs (422). Keys pinned to `creative_ids` cannot use this (it creates creatives). 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_add_urls_post_request: (required)
        :type api_v1_creative_pools_id_add_urls_post_request: ApiV1CreativePoolsIdAddUrlsPostRequest
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

        _param = self._api_v1_creative_pools_id_add_urls_post_serialize(
            id=id,
            api_v1_creative_pools_id_add_urls_post_request=api_v1_creative_pools_id_add_urls_post_request,
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


    def _api_v1_creative_pools_id_add_urls_post_serialize(
        self,
        id,
        api_v1_creative_pools_id_add_urls_post_request,
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
        if api_v1_creative_pools_id_add_urls_post_request is not None:
            _body_params = api_v1_creative_pools_id_add_urls_post_request


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
            resource_path='/api/v1/creative-pools/{id}/add-urls',
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
    def api_v1_creative_pools_id_clone_post(
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
    ) -> ApiV1CreativePoolsIdClonePost201Response:
        """Clone a creative pool with all its items.

        Duplicates the pool row and every live item (`is_deleted=0`). Cloned items share the same underlying `creative_id`, so the binary creative file is not re-uploaded — both pools reference the same row in the `creatives` table. The new pool's title is suffixed with \" (Copy)\". 

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

        _param = self._api_v1_creative_pools_id_clone_post_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CreativePoolsIdClonePost201Response",
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
    def api_v1_creative_pools_id_clone_post_with_http_info(
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
    ) -> ApiResponse[ApiV1CreativePoolsIdClonePost201Response]:
        """Clone a creative pool with all its items.

        Duplicates the pool row and every live item (`is_deleted=0`). Cloned items share the same underlying `creative_id`, so the binary creative file is not re-uploaded — both pools reference the same row in the `creatives` table. The new pool's title is suffixed with \" (Copy)\". 

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

        _param = self._api_v1_creative_pools_id_clone_post_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CreativePoolsIdClonePost201Response",
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
    def api_v1_creative_pools_id_clone_post_without_preload_content(
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
        """Clone a creative pool with all its items.

        Duplicates the pool row and every live item (`is_deleted=0`). Cloned items share the same underlying `creative_id`, so the binary creative file is not re-uploaded — both pools reference the same row in the `creatives` table. The new pool's title is suffixed with \" (Copy)\". 

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

        _param = self._api_v1_creative_pools_id_clone_post_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CreativePoolsIdClonePost201Response",
            '404': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_clone_post_serialize(
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
            method='POST',
            resource_path='/api/v1/creative-pools/{id}/clone',
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
    def api_v1_creative_pools_id_delete(
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
    ) -> ApiV1CreativePoolsIdDelete200Response:
        """Soft-delete a creative pool.

        Deletes the pool **and** its items. Inactive items always go; an active item is kept only when it is the last active item of its banner size / rating that campaign ads still use. If any item had to be kept the call returns 409 (`total_items`, `deleted`) and the pool itself stays — the deletable items ARE already gone. Note the 200 body spells the count `totalitems`, the 409 body `total_items`. 

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

        _param = self._api_v1_creative_pools_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdDelete200Response",
            '409': "ApiV1CreativePoolsIdDelete409Response",
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
    def api_v1_creative_pools_id_delete_with_http_info(
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
    ) -> ApiResponse[ApiV1CreativePoolsIdDelete200Response]:
        """Soft-delete a creative pool.

        Deletes the pool **and** its items. Inactive items always go; an active item is kept only when it is the last active item of its banner size / rating that campaign ads still use. If any item had to be kept the call returns 409 (`total_items`, `deleted`) and the pool itself stays — the deletable items ARE already gone. Note the 200 body spells the count `totalitems`, the 409 body `total_items`. 

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

        _param = self._api_v1_creative_pools_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdDelete200Response",
            '409': "ApiV1CreativePoolsIdDelete409Response",
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
    def api_v1_creative_pools_id_delete_without_preload_content(
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
        """Soft-delete a creative pool.

        Deletes the pool **and** its items. Inactive items always go; an active item is kept only when it is the last active item of its banner size / rating that campaign ads still use. If any item had to be kept the call returns 409 (`total_items`, `deleted`) and the pool itself stays — the deletable items ARE already gone. Note the 200 body spells the count `totalitems`, the 409 body `total_items`. 

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

        _param = self._api_v1_creative_pools_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdDelete200Response",
            '409': "ApiV1CreativePoolsIdDelete409Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_delete_serialize(
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
            method='DELETE',
            resource_path='/api/v1/creative-pools/{id}',
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
    def api_v1_creative_pools_id_get(
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
    ) -> ApiV1CreativePoolsIdGet200Response:
        """Show a single creative pool.


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

        _param = self._api_v1_creative_pools_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdGet200Response",
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
    def api_v1_creative_pools_id_get_with_http_info(
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
    ) -> ApiResponse[ApiV1CreativePoolsIdGet200Response]:
        """Show a single creative pool.


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

        _param = self._api_v1_creative_pools_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdGet200Response",
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
    def api_v1_creative_pools_id_get_without_preload_content(
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
        """Show a single creative pool.


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

        _param = self._api_v1_creative_pools_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_get_serialize(
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
            resource_path='/api/v1/creative-pools/{id}',
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
    def api_v1_creative_pools_id_items_export_get(
        self,
        id: StrictInt,
        ids: Annotated[StrictStr, Field(description="Comma-separated item ids, e.g. `55120,55121`.")],
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
    ) -> bytes:
        """Download pool items' creative files as a ZIP.

        Returns `application/zip` (`Content-Disposition: attachment; filename=\"pool-{id}-export.zip\"`) with one file per item plus a `_manifest.txt` listing which items were exported, skipped (no exportable source) or failed. Hotlinked items are fetched server-side (public addresses only). Max 500 items. 

        :param id: (required)
        :type id: int
        :param ids: Comma-separated item ids, e.g. `55120,55121`. (required)
        :type ids: str
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

        _param = self._api_v1_creative_pools_id_items_export_get_serialize(
            id=id,
            ids=ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytes",
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
    def api_v1_creative_pools_id_items_export_get_with_http_info(
        self,
        id: StrictInt,
        ids: Annotated[StrictStr, Field(description="Comma-separated item ids, e.g. `55120,55121`.")],
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
    ) -> ApiResponse[bytes]:
        """Download pool items' creative files as a ZIP.

        Returns `application/zip` (`Content-Disposition: attachment; filename=\"pool-{id}-export.zip\"`) with one file per item plus a `_manifest.txt` listing which items were exported, skipped (no exportable source) or failed. Hotlinked items are fetched server-side (public addresses only). Max 500 items. 

        :param id: (required)
        :type id: int
        :param ids: Comma-separated item ids, e.g. `55120,55121`. (required)
        :type ids: str
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

        _param = self._api_v1_creative_pools_id_items_export_get_serialize(
            id=id,
            ids=ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytes",
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
    def api_v1_creative_pools_id_items_export_get_without_preload_content(
        self,
        id: StrictInt,
        ids: Annotated[StrictStr, Field(description="Comma-separated item ids, e.g. `55120,55121`.")],
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
        """Download pool items' creative files as a ZIP.

        Returns `application/zip` (`Content-Disposition: attachment; filename=\"pool-{id}-export.zip\"`) with one file per item plus a `_manifest.txt` listing which items were exported, skipped (no exportable source) or failed. Hotlinked items are fetched server-side (public addresses only). Max 500 items. 

        :param id: (required)
        :type id: int
        :param ids: Comma-separated item ids, e.g. `55120,55121`. (required)
        :type ids: str
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

        _param = self._api_v1_creative_pools_id_items_export_get_serialize(
            id=id,
            ids=ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytes",
            '400': None,
            '403': "Error",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_export_get_serialize(
        self,
        id,
        ids,
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
        if ids is not None:
            
            _query_params.append(('ids', ids))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/zip', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/creative-pools/{id}/items/export',
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
    def api_v1_creative_pools_id_items_get(
        self,
        id: StrictInt,
        include_sizes: Annotated[Optional[StrictStr], Field(description="Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add stats per item for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=5000, strict=True)]] = None,
        filter_bansizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        filter_isactive: Optional[StrictInt] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
    ) -> ApiV1CreativesGet200Response:
        """List items in a creative pool.

        Returns every banner / video / native item in the pool with size, creative metadata and lifetime stats (views, clicks, ctr, conv), plus its schedule: `start_at` / `end_at` (unix seconds, 0 = no limit) and `is_fallback` (0/1) — see the item update endpoint. 

        :param id: (required)
        :type id: int
        :param include_sizes: Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.
        :type include_sizes: str
        :param select_stats: 1 = add stats per item for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param filter_bansizeid: Banner size id.
        :type filter_bansizeid: int
        :param filter_isactive:
        :type filter_isactive: int
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_id_items_get_serialize(
            id=id,
            include_sizes=include_sizes,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            filter_bansizeid=filter_bansizeid,
            filter_isactive=filter_isactive,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
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
    def api_v1_creative_pools_id_items_get_with_http_info(
        self,
        id: StrictInt,
        include_sizes: Annotated[Optional[StrictStr], Field(description="Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add stats per item for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=5000, strict=True)]] = None,
        filter_bansizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        filter_isactive: Optional[StrictInt] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
    ) -> ApiResponse[ApiV1CreativesGet200Response]:
        """List items in a creative pool.

        Returns every banner / video / native item in the pool with size, creative metadata and lifetime stats (views, clicks, ctr, conv), plus its schedule: `start_at` / `end_at` (unix seconds, 0 = no limit) and `is_fallback` (0/1) — see the item update endpoint. 

        :param id: (required)
        :type id: int
        :param include_sizes: Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.
        :type include_sizes: str
        :param select_stats: 1 = add stats per item for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param filter_bansizeid: Banner size id.
        :type filter_bansizeid: int
        :param filter_isactive:
        :type filter_isactive: int
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_id_items_get_serialize(
            id=id,
            include_sizes=include_sizes,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            filter_bansizeid=filter_bansizeid,
            filter_isactive=filter_isactive,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
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
    def api_v1_creative_pools_id_items_get_without_preload_content(
        self,
        id: StrictInt,
        include_sizes: Annotated[Optional[StrictStr], Field(description="Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.")] = None,
        select_stats: Annotated[Optional[StrictStr], Field(description="1 = add stats per item for the from / to window (default the last 7 days).")] = None,
        var_from: Annotated[Optional[date], Field(description="With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.")] = None,
        to: Annotated[Optional[date], Field(description="With select_stats=1: last day of the stats window (YYYY-MM-DD).")] = None,
        page: Optional[StrictInt] = None,
        per_page: Optional[Annotated[int, Field(le=5000, strict=True)]] = None,
        filter_bansizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        filter_isactive: Optional[StrictInt] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
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
        """List items in a creative pool.

        Returns every banner / video / native item in the pool with size, creative metadata and lifetime stats (views, clicks, ctr, conv), plus its schedule: `start_at` / `end_at` (unix seconds, 0 = no limit) and `is_fallback` (0/1) — see the item update endpoint. 

        :param id: (required)
        :type id: int
        :param include_sizes: Banner pools: 1 = also return the pool's banner sizes with an item count each, saving a second request.
        :type include_sizes: str
        :param select_stats: 1 = add stats per item for the from / to window (default the last 7 days).
        :type select_stats: str
        :param var_from: With select_stats=1: first day of the stats window (YYYY-MM-DD). Both from and to are needed; otherwise the last 7 days.
        :type var_from: date
        :param to: With select_stats=1: last day of the stats window (YYYY-MM-DD).
        :type to: date
        :param page:
        :type page: int
        :param per_page:
        :type per_page: int
        :param filter_bansizeid: Banner size id.
        :type filter_bansizeid: int
        :param filter_isactive:
        :type filter_isactive: int
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
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

        _param = self._api_v1_creative_pools_id_items_get_serialize(
            id=id,
            include_sizes=include_sizes,
            select_stats=select_stats,
            var_from=var_from,
            to=to,
            page=page,
            per_page=per_page,
            filter_bansizeid=filter_bansizeid,
            filter_isactive=filter_isactive,
            sort_by=sort_by,
            sort_dir=sort_dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_get_serialize(
        self,
        id,
        include_sizes,
        select_stats,
        var_from,
        to,
        page,
        per_page,
        filter_bansizeid,
        filter_isactive,
        sort_by,
        sort_dir,
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
        if include_sizes is not None:
            
            _query_params.append(('include_sizes', include_sizes))
            
        if select_stats is not None:
            
            _query_params.append(('select_stats', select_stats))
            
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
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if filter_bansizeid is not None:
            
            _query_params.append(('filter_bansizeid', filter_bansizeid))
            
        if filter_isactive is not None:
            
            _query_params.append(('filter_isactive', filter_isactive))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if sort_dir is not None:
            
            _query_params.append(('sort_dir', sort_dir))
            
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
            resource_path='/api/v1/creative-pools/{id}/items',
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
    def api_v1_creative_pools_id_items_item_id_delete(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Soft-delete a single pool item.

        Refuses if the item is still referenced by a live ad — unhook the ad first. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_delete_serialize(
            id=id,
            item_id=item_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '409': None,
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
    def api_v1_creative_pools_id_items_item_id_delete_with_http_info(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Soft-delete a single pool item.

        Refuses if the item is still referenced by a live ad — unhook the ad first. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_delete_serialize(
            id=id,
            item_id=item_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '409': None,
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
    def api_v1_creative_pools_id_items_item_id_delete_without_preload_content(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Soft-delete a single pool item.

        Refuses if the item is still referenced by a live ad — unhook the ad first. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_delete_serialize(
            id=id,
            item_id=item_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '409': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_item_id_delete_serialize(
        self,
        id,
        item_id,
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
        if item_id is not None:
            _path_params['itemId'] = item_id
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
            resource_path='/api/v1/creative-pools/{id}/items/{itemId}',
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
    def api_v1_creative_pools_id_items_item_id_put(
        self,
        id: StrictInt,
        item_id: StrictInt,
        api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest,
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
        """Update a single pool item.

        Editable fields: `title`, `lang`, `properties`, `ratingid`, `url_prefix`, `weight` (whole number 0–1000000; drives `sort_type: wr` rotation — 400 `invalid_weight` otherwise), `is_fallback`, `start_at`, `end_at`. Active state is toggled via the `/toggle` endpoint below.  **Scheduling.** `start_at` / `end_at` make the item serve only inside `[start_at, end_at)`. Send unix seconds or an RFC 3339 time with its offset (`2026-10-20T09:00:00-04:00` = 9:00 AM New York); `null`, `0` or `\"\"` clears that side. The list endpoint returns both as unix seconds (0 = no limit). The ad servers pick up an edit within 5 minutes and then switch on the exact second, so save a schedule a few minutes ahead of its start.  **Fallback.** `is_fallback: true` makes the item serve only while no other item of the same pool and size is live. Typical promo swap: mark the regular creative as fallback and give the promo a `start_at` (and `end_at`); the regular one steps aside while the promo runs and returns when it ends.  A change that would leave a size still used by campaign ads with nothing to serve at some moment is refused with 409 `SCHEDULE_LEAVES_POOL_EMPTY`; `gap_at` is the first uncovered unix second. Pausing or deleting an item runs the same check over the other items' schedules. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
        :param api_v1_creative_pools_id_items_item_id_put_request: (required)
        :type api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest
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

        _param = self._api_v1_creative_pools_id_items_item_id_put_serialize(
            id=id,
            item_id=item_id,
            api_v1_creative_pools_id_items_item_id_put_request=api_v1_creative_pools_id_items_item_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '409': "ApiV1CreativePoolsIdItemsItemIdPut409Response",
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
    def api_v1_creative_pools_id_items_item_id_put_with_http_info(
        self,
        id: StrictInt,
        item_id: StrictInt,
        api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest,
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
        """Update a single pool item.

        Editable fields: `title`, `lang`, `properties`, `ratingid`, `url_prefix`, `weight` (whole number 0–1000000; drives `sort_type: wr` rotation — 400 `invalid_weight` otherwise), `is_fallback`, `start_at`, `end_at`. Active state is toggled via the `/toggle` endpoint below.  **Scheduling.** `start_at` / `end_at` make the item serve only inside `[start_at, end_at)`. Send unix seconds or an RFC 3339 time with its offset (`2026-10-20T09:00:00-04:00` = 9:00 AM New York); `null`, `0` or `\"\"` clears that side. The list endpoint returns both as unix seconds (0 = no limit). The ad servers pick up an edit within 5 minutes and then switch on the exact second, so save a schedule a few minutes ahead of its start.  **Fallback.** `is_fallback: true` makes the item serve only while no other item of the same pool and size is live. Typical promo swap: mark the regular creative as fallback and give the promo a `start_at` (and `end_at`); the regular one steps aside while the promo runs and returns when it ends.  A change that would leave a size still used by campaign ads with nothing to serve at some moment is refused with 409 `SCHEDULE_LEAVES_POOL_EMPTY`; `gap_at` is the first uncovered unix second. Pausing or deleting an item runs the same check over the other items' schedules. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
        :param api_v1_creative_pools_id_items_item_id_put_request: (required)
        :type api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest
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

        _param = self._api_v1_creative_pools_id_items_item_id_put_serialize(
            id=id,
            item_id=item_id,
            api_v1_creative_pools_id_items_item_id_put_request=api_v1_creative_pools_id_items_item_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '409': "ApiV1CreativePoolsIdItemsItemIdPut409Response",
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
    def api_v1_creative_pools_id_items_item_id_put_without_preload_content(
        self,
        id: StrictInt,
        item_id: StrictInt,
        api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest,
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
        """Update a single pool item.

        Editable fields: `title`, `lang`, `properties`, `ratingid`, `url_prefix`, `weight` (whole number 0–1000000; drives `sort_type: wr` rotation — 400 `invalid_weight` otherwise), `is_fallback`, `start_at`, `end_at`. Active state is toggled via the `/toggle` endpoint below.  **Scheduling.** `start_at` / `end_at` make the item serve only inside `[start_at, end_at)`. Send unix seconds or an RFC 3339 time with its offset (`2026-10-20T09:00:00-04:00` = 9:00 AM New York); `null`, `0` or `\"\"` clears that side. The list endpoint returns both as unix seconds (0 = no limit). The ad servers pick up an edit within 5 minutes and then switch on the exact second, so save a schedule a few minutes ahead of its start.  **Fallback.** `is_fallback: true` makes the item serve only while no other item of the same pool and size is live. Typical promo swap: mark the regular creative as fallback and give the promo a `start_at` (and `end_at`); the regular one steps aside while the promo runs and returns when it ends.  A change that would leave a size still used by campaign ads with nothing to serve at some moment is refused with 409 `SCHEDULE_LEAVES_POOL_EMPTY`; `gap_at` is the first uncovered unix second. Pausing or deleting an item runs the same check over the other items' schedules. 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
        :param api_v1_creative_pools_id_items_item_id_put_request: (required)
        :type api_v1_creative_pools_id_items_item_id_put_request: ApiV1CreativePoolsIdItemsItemIdPutRequest
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

        _param = self._api_v1_creative_pools_id_items_item_id_put_serialize(
            id=id,
            item_id=item_id,
            api_v1_creative_pools_id_items_item_id_put_request=api_v1_creative_pools_id_items_item_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '409': "ApiV1CreativePoolsIdItemsItemIdPut409Response",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_item_id_put_serialize(
        self,
        id,
        item_id,
        api_v1_creative_pools_id_items_item_id_put_request,
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
        if item_id is not None:
            _path_params['itemId'] = item_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if api_v1_creative_pools_id_items_item_id_put_request is not None:
            _body_params = api_v1_creative_pools_id_items_item_id_put_request


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
            resource_path='/api/v1/creative-pools/{id}/items/{itemId}',
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
    def api_v1_creative_pools_id_items_item_id_toggle_put(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Toggle a pool item on / off.

        Flips `isactive` between 0 and 1. Inactive items are skipped by the ad-server when picking a creative from the pool. Pausing the last active item of a format that campaign ads still use is refused (409). 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_toggle_put_serialize(
            id=id,
            item_id=item_id,
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
    def api_v1_creative_pools_id_items_item_id_toggle_put_with_http_info(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Toggle a pool item on / off.

        Flips `isactive` between 0 and 1. Inactive items are skipped by the ad-server when picking a creative from the pool. Pausing the last active item of a format that campaign ads still use is refused (409). 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_toggle_put_serialize(
            id=id,
            item_id=item_id,
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
    def api_v1_creative_pools_id_items_item_id_toggle_put_without_preload_content(
        self,
        id: StrictInt,
        item_id: StrictInt,
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
        """Toggle a pool item on / off.

        Flips `isactive` between 0 and 1. Inactive items are skipped by the ad-server when picking a creative from the pool. Pausing the last active item of a format that campaign ads still use is refused (409). 

        :param id: (required)
        :type id: int
        :param item_id: (required)
        :type item_id: int
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

        _param = self._api_v1_creative_pools_id_items_item_id_toggle_put_serialize(
            id=id,
            item_id=item_id,
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


    def _api_v1_creative_pools_id_items_item_id_toggle_put_serialize(
        self,
        id,
        item_id,
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
        if item_id is not None:
            _path_params['itemId'] = item_id
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
            resource_path='/api/v1/creative-pools/{id}/items/{itemId}/toggle',
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
    def api_v1_creative_pools_id_items_mass_action_put(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest,
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
        """Bulk-change items of a creative pool.

        `action`:  - `activate` / `deactivate` — set `isactive`. - `delete` — soft-delete the items. - `url_prefix` — set each item's `url_prefix` to `url_prefix`. - `language` — set each item's `lang` to `lang`.  Deactivate and delete refuse (409, nothing written) when an item is the last active one of its size / rating still used by a campaign ad — `blocked_ids` lists them, the same rule as the single-item toggle / delete. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_mass_action_put_request: (required)
        :type api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest
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

        _param = self._api_v1_creative_pools_id_items_mass_action_put_serialize(
            id=id,
            api_v1_creative_pools_id_items_mass_action_put_request=api_v1_creative_pools_id_items_mass_action_put_request,
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
            '409': None,
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
    def api_v1_creative_pools_id_items_mass_action_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest,
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
        """Bulk-change items of a creative pool.

        `action`:  - `activate` / `deactivate` — set `isactive`. - `delete` — soft-delete the items. - `url_prefix` — set each item's `url_prefix` to `url_prefix`. - `language` — set each item's `lang` to `lang`.  Deactivate and delete refuse (409, nothing written) when an item is the last active one of its size / rating still used by a campaign ad — `blocked_ids` lists them, the same rule as the single-item toggle / delete. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_mass_action_put_request: (required)
        :type api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest
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

        _param = self._api_v1_creative_pools_id_items_mass_action_put_serialize(
            id=id,
            api_v1_creative_pools_id_items_mass_action_put_request=api_v1_creative_pools_id_items_mass_action_put_request,
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
            '409': None,
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
    def api_v1_creative_pools_id_items_mass_action_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest,
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
        """Bulk-change items of a creative pool.

        `action`:  - `activate` / `deactivate` — set `isactive`. - `delete` — soft-delete the items. - `url_prefix` — set each item's `url_prefix` to `url_prefix`. - `language` — set each item's `lang` to `lang`.  Deactivate and delete refuse (409, nothing written) when an item is the last active one of its size / rating still used by a campaign ad — `blocked_ids` lists them, the same rule as the single-item toggle / delete. Same handler as the panel. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_mass_action_put_request: (required)
        :type api_v1_creative_pools_id_items_mass_action_put_request: ApiV1CreativePoolsIdItemsMassActionPutRequest
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

        _param = self._api_v1_creative_pools_id_items_mass_action_put_serialize(
            id=id,
            api_v1_creative_pools_id_items_mass_action_put_request=api_v1_creative_pools_id_items_mass_action_put_request,
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
            '409': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_mass_action_put_serialize(
        self,
        id,
        api_v1_creative_pools_id_items_mass_action_put_request,
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
        if api_v1_creative_pools_id_items_mass_action_put_request is not None:
            _body_params = api_v1_creative_pools_id_items_mass_action_put_request


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
            resource_path='/api/v1/creative-pools/{id}/items/mass-action',
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
    def api_v1_creative_pools_id_items_post(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest,
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
        """Add an item to a creative pool.

        Adds one creative to the pool. Reference an uploaded creative by `creative_id` (from `POST /api/v1/creatives/upload`; must be yours, and on the key's creative pin if it has one) or supply a hotlink `banner_url`. The pool's `type` decides the creative slot (banner / video / image). To add many library creatives at once use `POST …/{id}/add-creatives`. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_post_request: (required)
        :type api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest
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

        _param = self._api_v1_creative_pools_id_items_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_post_request=api_v1_creative_pools_id_items_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
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
    def api_v1_creative_pools_id_items_post_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest,
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
        """Add an item to a creative pool.

        Adds one creative to the pool. Reference an uploaded creative by `creative_id` (from `POST /api/v1/creatives/upload`; must be yours, and on the key's creative pin if it has one) or supply a hotlink `banner_url`. The pool's `type` decides the creative slot (banner / video / image). To add many library creatives at once use `POST …/{id}/add-creatives`. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_post_request: (required)
        :type api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest
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

        _param = self._api_v1_creative_pools_id_items_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_post_request=api_v1_creative_pools_id_items_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
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
    def api_v1_creative_pools_id_items_post_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest,
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
        """Add an item to a creative pool.

        Adds one creative to the pool. Reference an uploaded creative by `creative_id` (from `POST /api/v1/creatives/upload`; must be yours, and on the key's creative pin if it has one) or supply a hotlink `banner_url`. The pool's `type` decides the creative slot (banner / video / image). To add many library creatives at once use `POST …/{id}/add-creatives`. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_post_request: (required)
        :type api_v1_creative_pools_id_items_post_request: ApiV1CreativePoolsIdItemsPostRequest
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

        _param = self._api_v1_creative_pools_id_items_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_post_request=api_v1_creative_pools_id_items_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_items_post_serialize(
        self,
        id,
        api_v1_creative_pools_id_items_post_request,
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
        if api_v1_creative_pools_id_items_post_request is not None:
            _body_params = api_v1_creative_pools_id_items_post_request



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
            resource_path='/api/v1/creative-pools/{id}/items',
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
    def api_v1_creative_pools_id_items_recover_post(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest,
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
        """Put removed items back into a creative pool.

        The undo of DELETE /creative-pools/{id}/items/{itemId} (removing an item also switches it off). `active_ids` are switched back on. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_recover_post_request: (required)
        :type api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest
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

        _param = self._api_v1_creative_pools_id_items_recover_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_recover_post_request=api_v1_creative_pools_id_items_recover_post_request,
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
    def api_v1_creative_pools_id_items_recover_post_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest,
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
        """Put removed items back into a creative pool.

        The undo of DELETE /creative-pools/{id}/items/{itemId} (removing an item also switches it off). `active_ids` are switched back on. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_recover_post_request: (required)
        :type api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest
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

        _param = self._api_v1_creative_pools_id_items_recover_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_recover_post_request=api_v1_creative_pools_id_items_recover_post_request,
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
    def api_v1_creative_pools_id_items_recover_post_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest,
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
        """Put removed items back into a creative pool.

        The undo of DELETE /creative-pools/{id}/items/{itemId} (removing an item also switches it off). `active_ids` are switched back on. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_items_recover_post_request: (required)
        :type api_v1_creative_pools_id_items_recover_post_request: ApiV1CreativePoolsIdItemsRecoverPostRequest
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

        _param = self._api_v1_creative_pools_id_items_recover_post_serialize(
            id=id,
            api_v1_creative_pools_id_items_recover_post_request=api_v1_creative_pools_id_items_recover_post_request,
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


    def _api_v1_creative_pools_id_items_recover_post_serialize(
        self,
        id,
        api_v1_creative_pools_id_items_recover_post_request,
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
        if api_v1_creative_pools_id_items_recover_post_request is not None:
            _body_params = api_v1_creative_pools_id_items_recover_post_request



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
            resource_path='/api/v1/creative-pools/{id}/items/recover',
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
    def api_v1_creative_pools_id_put(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest,
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
        """Update creative pool meta.

        Updates any of `title` (alias `name`), `sort_type`, `conv_type`, `tags`, `type`, `orientation`. `sort_type: wr` (weighted rotation on item `weight`) needs the tenant's weighted-rotation option — 400 `weighted_rotation_disabled` otherwise. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_put_request: (required)
        :type api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest
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

        _param = self._api_v1_creative_pools_id_put_serialize(
            id=id,
            api_v1_creative_pools_id_put_request=api_v1_creative_pools_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
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
    def api_v1_creative_pools_id_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest,
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
        """Update creative pool meta.

        Updates any of `title` (alias `name`), `sort_type`, `conv_type`, `tags`, `type`, `orientation`. `sort_type: wr` (weighted rotation on item `weight`) needs the tenant's weighted-rotation option — 400 `weighted_rotation_disabled` otherwise. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_put_request: (required)
        :type api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest
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

        _param = self._api_v1_creative_pools_id_put_serialize(
            id=id,
            api_v1_creative_pools_id_put_request=api_v1_creative_pools_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
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
    def api_v1_creative_pools_id_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest,
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
        """Update creative pool meta.

        Updates any of `title` (alias `name`), `sort_type`, `conv_type`, `tags`, `type`, `orientation`. `sort_type: wr` (weighted rotation on item `weight`) needs the tenant's weighted-rotation option — 400 `weighted_rotation_disabled` otherwise. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_pools_id_put_request: (required)
        :type api_v1_creative_pools_id_put_request: ApiV1CreativePoolsIdPutRequest
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

        _param = self._api_v1_creative_pools_id_put_serialize(
            id=id,
            api_v1_creative_pools_id_put_request=api_v1_creative_pools_id_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '404': None,
            '403': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_put_serialize(
        self,
        id,
        api_v1_creative_pools_id_put_request,
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
        if api_v1_creative_pools_id_put_request is not None:
            _body_params = api_v1_creative_pools_id_put_request


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
            resource_path='/api/v1/creative-pools/{id}',
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
    def api_v1_creative_pools_id_recover_post(
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
        """Restore an archived creative pool.

        Reverses the soft delete of DELETE /creative-pools/{id} (and of Cleanup's Archive): the pool is listed and usable again. The items the delete took down come back as they were; for a pool deleted before 2026-10-16 every deleted item comes back paused (`items_paused: true`). 404 when the pool does not exist, is not archived, or was purged. 

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

        _param = self._api_v1_creative_pools_id_recover_post_serialize(
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
    def api_v1_creative_pools_id_recover_post_with_http_info(
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
        """Restore an archived creative pool.

        Reverses the soft delete of DELETE /creative-pools/{id} (and of Cleanup's Archive): the pool is listed and usable again. The items the delete took down come back as they were; for a pool deleted before 2026-10-16 every deleted item comes back paused (`items_paused: true`). 404 when the pool does not exist, is not archived, or was purged. 

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

        _param = self._api_v1_creative_pools_id_recover_post_serialize(
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
    def api_v1_creative_pools_id_recover_post_without_preload_content(
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
        """Restore an archived creative pool.

        Reverses the soft delete of DELETE /creative-pools/{id} (and of Cleanup's Archive): the pool is listed and usable again. The items the delete took down come back as they were; for a pool deleted before 2026-10-16 every deleted item comes back paused (`items_paused: true`). 404 when the pool does not exist, is not archived, or was purged. 

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

        _param = self._api_v1_creative_pools_id_recover_post_serialize(
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


    def _api_v1_creative_pools_id_recover_post_serialize(
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
            method='POST',
            resource_path='/api/v1/creative-pools/{id}/recover',
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
    def api_v1_creative_pools_id_used_in_get(
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
    ) -> ApiV1CreativePoolsIdUsedInGet200Response:
        """List campaigns / ads that reference this pool.


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

        _param = self._api_v1_creative_pools_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdUsedInGet200Response",
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
    def api_v1_creative_pools_id_used_in_get_with_http_info(
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
    ) -> ApiResponse[ApiV1CreativePoolsIdUsedInGet200Response]:
        """List campaigns / ads that reference this pool.


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

        _param = self._api_v1_creative_pools_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdUsedInGet200Response",
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
    def api_v1_creative_pools_id_used_in_get_without_preload_content(
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
        """List campaigns / ads that reference this pool.


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

        _param = self._api_v1_creative_pools_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativePoolsIdUsedInGet200Response",
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_id_used_in_get_serialize(
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
            resource_path='/api/v1/creative-pools/{id}/used-in',
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
    def api_v1_creative_pools_post(
        self,
        api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest,
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
        """Create a creative pool.

        Creates an empty pool. Fill it with `POST …/{id}/add-creatives` (media-bank ids), `POST …/{id}/add-urls` (hotlinks) or `POST …/{id}/items` (one creative). Title collisions are auto-suffixed with `_<unix>`. An unknown `type` is a 400 `invalid_type` (it used to fall back to banner). 

        :param api_v1_creative_pools_post_request: (required)
        :type api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest
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

        _param = self._api_v1_creative_pools_post_serialize(
            api_v1_creative_pools_post_request=api_v1_creative_pools_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
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
    def api_v1_creative_pools_post_with_http_info(
        self,
        api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest,
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
        """Create a creative pool.

        Creates an empty pool. Fill it with `POST …/{id}/add-creatives` (media-bank ids), `POST …/{id}/add-urls` (hotlinks) or `POST …/{id}/items` (one creative). Title collisions are auto-suffixed with `_<unix>`. An unknown `type` is a 400 `invalid_type` (it used to fall back to banner). 

        :param api_v1_creative_pools_post_request: (required)
        :type api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest
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

        _param = self._api_v1_creative_pools_post_serialize(
            api_v1_creative_pools_post_request=api_v1_creative_pools_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
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
    def api_v1_creative_pools_post_without_preload_content(
        self,
        api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest,
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
        """Create a creative pool.

        Creates an empty pool. Fill it with `POST …/{id}/add-creatives` (media-bank ids), `POST …/{id}/add-urls` (hotlinks) or `POST …/{id}/items` (one creative). Title collisions are auto-suffixed with `_<unix>`. An unknown `type` is a 400 `invalid_type` (it used to fall back to banner). 

        :param api_v1_creative_pools_post_request: (required)
        :type api_v1_creative_pools_post_request: ApiV1CreativePoolsPostRequest
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

        _param = self._api_v1_creative_pools_post_serialize(
            api_v1_creative_pools_post_request=api_v1_creative_pools_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApiV1CampaignsTypeCampaignIdAdsAdIdClonePost200Response",
            '400': None,
            '403': "Error",
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_pools_post_serialize(
        self,
        api_v1_creative_pools_post_request,
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
        if api_v1_creative_pools_post_request is not None:
            _body_params = api_v1_creative_pools_post_request


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
            resource_path='/api/v1/creative-pools',
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
    def api_v1_creatives_bulk_delete_post(
        self,
        api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest,
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
        """Soft-delete many media-bank creatives.

        Sets `isdeleted = 1` on up to 500 of your creatives. Ads and pool items already pointing at them keep working; deleted creatives just leave the library. Restore with `POST /creatives/bulk-undelete` or `PUT /creatives/{id}/undelete`. A key pinned to `creative_ids` may only name pinned ids (403 `forbidden_resource`). Account members with own-scoped creative rights only affect creatives they manage. Same handler as the panel. 

        :param api_v1_creatives_bulk_delete_post_request: (required)
        :type api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest
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

        _param = self._api_v1_creatives_bulk_delete_post_serialize(
            api_v1_creatives_bulk_delete_post_request=api_v1_creatives_bulk_delete_post_request,
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
    def api_v1_creatives_bulk_delete_post_with_http_info(
        self,
        api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest,
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
        """Soft-delete many media-bank creatives.

        Sets `isdeleted = 1` on up to 500 of your creatives. Ads and pool items already pointing at them keep working; deleted creatives just leave the library. Restore with `POST /creatives/bulk-undelete` or `PUT /creatives/{id}/undelete`. A key pinned to `creative_ids` may only name pinned ids (403 `forbidden_resource`). Account members with own-scoped creative rights only affect creatives they manage. Same handler as the panel. 

        :param api_v1_creatives_bulk_delete_post_request: (required)
        :type api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest
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

        _param = self._api_v1_creatives_bulk_delete_post_serialize(
            api_v1_creatives_bulk_delete_post_request=api_v1_creatives_bulk_delete_post_request,
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
    def api_v1_creatives_bulk_delete_post_without_preload_content(
        self,
        api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest,
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
        """Soft-delete many media-bank creatives.

        Sets `isdeleted = 1` on up to 500 of your creatives. Ads and pool items already pointing at them keep working; deleted creatives just leave the library. Restore with `POST /creatives/bulk-undelete` or `PUT /creatives/{id}/undelete`. A key pinned to `creative_ids` may only name pinned ids (403 `forbidden_resource`). Account members with own-scoped creative rights only affect creatives they manage. Same handler as the panel. 

        :param api_v1_creatives_bulk_delete_post_request: (required)
        :type api_v1_creatives_bulk_delete_post_request: ApiV1CreativesBulkDeletePostRequest
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

        _param = self._api_v1_creatives_bulk_delete_post_serialize(
            api_v1_creatives_bulk_delete_post_request=api_v1_creatives_bulk_delete_post_request,
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


    def _api_v1_creatives_bulk_delete_post_serialize(
        self,
        api_v1_creatives_bulk_delete_post_request,
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
        if api_v1_creatives_bulk_delete_post_request is not None:
            _body_params = api_v1_creatives_bulk_delete_post_request


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
            resource_path='/api/v1/creatives/bulk-delete',
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
    def api_v1_creatives_bulk_undelete_post(
        self,
        api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest,
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
        """Restore many deleted creatives.

        Inverse of `POST /creatives/bulk-delete` — same limits, pin and member rules.

        :param api_v1_creatives_bulk_undelete_post_request: (required)
        :type api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest
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

        _param = self._api_v1_creatives_bulk_undelete_post_serialize(
            api_v1_creatives_bulk_undelete_post_request=api_v1_creatives_bulk_undelete_post_request,
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
    def api_v1_creatives_bulk_undelete_post_with_http_info(
        self,
        api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest,
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
        """Restore many deleted creatives.

        Inverse of `POST /creatives/bulk-delete` — same limits, pin and member rules.

        :param api_v1_creatives_bulk_undelete_post_request: (required)
        :type api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest
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

        _param = self._api_v1_creatives_bulk_undelete_post_serialize(
            api_v1_creatives_bulk_undelete_post_request=api_v1_creatives_bulk_undelete_post_request,
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
    def api_v1_creatives_bulk_undelete_post_without_preload_content(
        self,
        api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest,
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
        """Restore many deleted creatives.

        Inverse of `POST /creatives/bulk-delete` — same limits, pin and member rules.

        :param api_v1_creatives_bulk_undelete_post_request: (required)
        :type api_v1_creatives_bulk_undelete_post_request: ApiV1CreativesBulkUndeletePostRequest
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

        _param = self._api_v1_creatives_bulk_undelete_post_serialize(
            api_v1_creatives_bulk_undelete_post_request=api_v1_creatives_bulk_undelete_post_request,
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


    def _api_v1_creatives_bulk_undelete_post_serialize(
        self,
        api_v1_creatives_bulk_undelete_post_request,
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
        if api_v1_creatives_bulk_undelete_post_request is not None:
            _body_params = api_v1_creatives_bulk_undelete_post_request


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
            resource_path='/api/v1/creatives/bulk-undelete',
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
    def api_v1_creatives_id_undelete_put(
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
        """Restore one deleted creative.

        Undoes `DELETE /creatives/{id}`. Same handler as the panel. No body.

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

        _param = self._api_v1_creatives_id_undelete_put_serialize(
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
    def api_v1_creatives_id_undelete_put_with_http_info(
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
        """Restore one deleted creative.

        Undoes `DELETE /creatives/{id}`. Same handler as the panel. No body.

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

        _param = self._api_v1_creatives_id_undelete_put_serialize(
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
    def api_v1_creatives_id_undelete_put_without_preload_content(
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
        """Restore one deleted creative.

        Undoes `DELETE /creatives/{id}`. Same handler as the panel. No body.

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

        _param = self._api_v1_creatives_id_undelete_put_serialize(
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


    def _api_v1_creatives_id_undelete_put_serialize(
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
            method='PUT',
            resource_path='/api/v1/creatives/{id}/undelete',
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



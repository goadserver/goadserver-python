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

from pydantic import Field, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional, Tuple, Union
from typing_extensions import Annotated
from goadserver.models.api_v1_creative_folders_id_put_request import ApiV1CreativeFoldersIdPutRequest
from goadserver.models.api_v1_creative_folders_post_request import ApiV1CreativeFoldersPostRequest
from goadserver.models.api_v1_creatives_bulk_move_post_request import ApiV1CreativesBulkMovePostRequest
from goadserver.models.api_v1_creatives_get200_response import ApiV1CreativesGet200Response
from goadserver.models.api_v1_creatives_id_name_put_request import ApiV1CreativesIdNamePutRequest
from goadserver.models.api_v1_creatives_id_put_request import ApiV1CreativesIdPutRequest
from goadserver.models.api_v1_creatives_id_tags_put_request import ApiV1CreativesIdTagsPutRequest

from goadserver.api_client import ApiClient, RequestSerialized
from goadserver.api_response import ApiResponse
from goadserver.rest import RESTResponseType


class CreativesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_v1_creative_folders_get(
        self,
        with_counts: Annotated[Optional[StrictStr], Field(description="Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.")] = None,
        creative_type: Annotated[Optional[StrictStr], Field(description="Narrow the counts to one creative type (comma-separated list accepted).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List media-bank folders.

        The account's folder tree: `{id, name, pid, level}` rows, `pid` 0 for a root, nested at most 3 tiers deep. Folders are the media bank's exclusive axis — one folder per creative — and are separate from the multi-valued groups on `creatives.tags`. 

        :param with_counts: Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.
        :type with_counts: str
        :param creative_type: Narrow the counts to one creative type (comma-separated list accepted).
        :type creative_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_get_serialize(
            with_counts=with_counts,
            creative_type=creative_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creative_folders_get_with_http_info(
        self,
        with_counts: Annotated[Optional[StrictStr], Field(description="Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.")] = None,
        creative_type: Annotated[Optional[StrictStr], Field(description="Narrow the counts to one creative type (comma-separated list accepted).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List media-bank folders.

        The account's folder tree: `{id, name, pid, level}` rows, `pid` 0 for a root, nested at most 3 tiers deep. Folders are the media bank's exclusive axis — one folder per creative — and are separate from the multi-valued groups on `creatives.tags`. 

        :param with_counts: Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.
        :type with_counts: str
        :param creative_type: Narrow the counts to one creative type (comma-separated list accepted).
        :type creative_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_get_serialize(
            with_counts=with_counts,
            creative_type=creative_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creative_folders_get_without_preload_content(
        self,
        with_counts: Annotated[Optional[StrictStr], Field(description="Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.")] = None,
        creative_type: Annotated[Optional[StrictStr], Field(description="Narrow the counts to one creative type (comma-separated list accepted).")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List media-bank folders.

        The account's folder tree: `{id, name, pid, level}` rows, `pid` 0 for a root, nested at most 3 tiers deep. Folders are the media bank's exclusive axis — one folder per creative — and are separate from the multi-valued groups on `creatives.tags`. 

        :param with_counts: Add `count` (live creatives) per folder plus meta.unfiled_count and meta.creative_count.
        :type with_counts: str
        :param creative_type: Narrow the counts to one creative type (comma-separated list accepted).
        :type creative_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_get_serialize(
            with_counts=with_counts,
            creative_type=creative_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_folders_get_serialize(
        self,
        with_counts,
        creative_type,
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
        if with_counts is not None:
            
            _query_params.append(('with_counts', with_counts))
            
        if creative_type is not None:
            
            _query_params.append(('creative_type', creative_type))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/creative-folders',
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
    def api_v1_creative_folders_id_delete(
        self,
        id: StrictInt,
        move_to: Annotated[Optional[StrictInt], Field(description="File the folder's creatives here instead of unfiling them.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Delete a folder.

        Never deletes creatives. The folder's creatives become unfiled — or move to `move_to` — and its subfolders are reparented to the deleted folder's own parent. 

        :param id: (required)
        :type id: int
        :param move_to: File the folder's creatives here instead of unfiling them.
        :type move_to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_delete_serialize(
            id=id,
            move_to=move_to,
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
    def api_v1_creative_folders_id_delete_with_http_info(
        self,
        id: StrictInt,
        move_to: Annotated[Optional[StrictInt], Field(description="File the folder's creatives here instead of unfiling them.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Delete a folder.

        Never deletes creatives. The folder's creatives become unfiled — or move to `move_to` — and its subfolders are reparented to the deleted folder's own parent. 

        :param id: (required)
        :type id: int
        :param move_to: File the folder's creatives here instead of unfiling them.
        :type move_to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_delete_serialize(
            id=id,
            move_to=move_to,
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
    def api_v1_creative_folders_id_delete_without_preload_content(
        self,
        id: StrictInt,
        move_to: Annotated[Optional[StrictInt], Field(description="File the folder's creatives here instead of unfiling them.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Delete a folder.

        Never deletes creatives. The folder's creatives become unfiled — or move to `move_to` — and its subfolders are reparented to the deleted folder's own parent. 

        :param id: (required)
        :type id: int
        :param move_to: File the folder's creatives here instead of unfiling them.
        :type move_to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_delete_serialize(
            id=id,
            move_to=move_to,
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


    def _api_v1_creative_folders_id_delete_serialize(
        self,
        id,
        move_to,
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
        if move_to is not None:
            
            _query_params.append(('move_to', move_to))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/creative-folders/{id}',
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
    def api_v1_creative_folders_id_put(
        self,
        id: StrictInt,
        api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename or move a folder.

        `name` is required. `pid` is optional — omitting it leaves the folder where it is; sending it reparents the folder and its whole subtree, which is refused if that would exceed the depth cap or form a cycle. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_folders_id_put_request: (required)
        :type api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_put_serialize(
            id=id,
            api_v1_creative_folders_id_put_request=api_v1_creative_folders_id_put_request,
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
    def api_v1_creative_folders_id_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename or move a folder.

        `name` is required. `pid` is optional — omitting it leaves the folder where it is; sending it reparents the folder and its whole subtree, which is refused if that would exceed the depth cap or form a cycle. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_folders_id_put_request: (required)
        :type api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_put_serialize(
            id=id,
            api_v1_creative_folders_id_put_request=api_v1_creative_folders_id_put_request,
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
    def api_v1_creative_folders_id_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename or move a folder.

        `name` is required. `pid` is optional — omitting it leaves the folder where it is; sending it reparents the folder and its whole subtree, which is refused if that would exceed the depth cap or form a cycle. 

        :param id: (required)
        :type id: int
        :param api_v1_creative_folders_id_put_request: (required)
        :type api_v1_creative_folders_id_put_request: ApiV1CreativeFoldersIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_id_put_serialize(
            id=id,
            api_v1_creative_folders_id_put_request=api_v1_creative_folders_id_put_request,
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


    def _api_v1_creative_folders_id_put_serialize(
        self,
        id,
        api_v1_creative_folders_id_put_request,
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
        if api_v1_creative_folders_id_put_request is not None:
            _body_params = api_v1_creative_folders_id_put_request



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
            resource_path='/api/v1/creative-folders/{id}',
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
    def api_v1_creative_folders_post(
        self,
        api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Create a folder.

        A folder whose name already exists under the same parent is returned as-is with `existing: true` rather than duplicated, so this is safe to call as create-or-reuse. 

        :param api_v1_creative_folders_post_request: (required)
        :type api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_post_serialize(
            api_v1_creative_folders_post_request=api_v1_creative_folders_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creative_folders_post_with_http_info(
        self,
        api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Create a folder.

        A folder whose name already exists under the same parent is returned as-is with `existing: true` rather than duplicated, so this is safe to call as create-or-reuse. 

        :param api_v1_creative_folders_post_request: (required)
        :type api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_post_serialize(
            api_v1_creative_folders_post_request=api_v1_creative_folders_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creative_folders_post_without_preload_content(
        self,
        api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Create a folder.

        A folder whose name already exists under the same parent is returned as-is with `existing: true` rather than duplicated, so this is safe to call as create-or-reuse. 

        :param api_v1_creative_folders_post_request: (required)
        :type api_v1_creative_folders_post_request: ApiV1CreativeFoldersPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creative_folders_post_serialize(
            api_v1_creative_folders_post_request=api_v1_creative_folders_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '201': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creative_folders_post_serialize(
        self,
        api_v1_creative_folders_post_request,
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
        if api_v1_creative_folders_post_request is not None:
            _body_params = api_v1_creative_folders_post_request



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
            resource_path='/api/v1/creative-folders',
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
    def api_v1_creatives_bulk_move_post(
        self,
        api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """File creatives into a folder.

        Moves creatives into one media-bank folder. A creative sits in exactly one folder, so this is an assignment: rows already filed elsewhere are moved, and `folder_id: 0` unfiles them.  Two mutually exclusive selections:    * `ids` — an explicit list (max 20000, applied in chunks).   * `filter` — every creative matching a listing filter, given as the     same query params `GET /api/v1/creatives` accepts     (`creative_type`, `sizeid`, `orientation`, `folder_id`,     `include_subfolders`, `deleted`/`all`). Use this to file a whole     library; it is applied in batches server-side.  Nothing outside the key's own account can be reached by either form. 

        :param api_v1_creatives_bulk_move_post_request: (required)
        :type api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_bulk_move_post_serialize(
            api_v1_creatives_bulk_move_post_request=api_v1_creatives_bulk_move_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
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
    def api_v1_creatives_bulk_move_post_with_http_info(
        self,
        api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """File creatives into a folder.

        Moves creatives into one media-bank folder. A creative sits in exactly one folder, so this is an assignment: rows already filed elsewhere are moved, and `folder_id: 0` unfiles them.  Two mutually exclusive selections:    * `ids` — an explicit list (max 20000, applied in chunks).   * `filter` — every creative matching a listing filter, given as the     same query params `GET /api/v1/creatives` accepts     (`creative_type`, `sizeid`, `orientation`, `folder_id`,     `include_subfolders`, `deleted`/`all`). Use this to file a whole     library; it is applied in batches server-side.  Nothing outside the key's own account can be reached by either form. 

        :param api_v1_creatives_bulk_move_post_request: (required)
        :type api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_bulk_move_post_serialize(
            api_v1_creatives_bulk_move_post_request=api_v1_creatives_bulk_move_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
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
    def api_v1_creatives_bulk_move_post_without_preload_content(
        self,
        api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """File creatives into a folder.

        Moves creatives into one media-bank folder. A creative sits in exactly one folder, so this is an assignment: rows already filed elsewhere are moved, and `folder_id: 0` unfiles them.  Two mutually exclusive selections:    * `ids` — an explicit list (max 20000, applied in chunks).   * `filter` — every creative matching a listing filter, given as the     same query params `GET /api/v1/creatives` accepts     (`creative_type`, `sizeid`, `orientation`, `folder_id`,     `include_subfolders`, `deleted`/`all`). Use this to file a whole     library; it is applied in batches server-side.  Nothing outside the key's own account can be reached by either form. 

        :param api_v1_creatives_bulk_move_post_request: (required)
        :type api_v1_creatives_bulk_move_post_request: ApiV1CreativesBulkMovePostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_bulk_move_post_serialize(
            api_v1_creatives_bulk_move_post_request=api_v1_creatives_bulk_move_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '422': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_bulk_move_post_serialize(
        self,
        api_v1_creatives_bulk_move_post_request,
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
        if api_v1_creatives_bulk_move_post_request is not None:
            _body_params = api_v1_creatives_bulk_move_post_request



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
            resource_path='/api/v1/creatives/bulk-move',
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
    def api_v1_creatives_get(
        self,
        creative_type: Annotated[Optional[StrictStr], Field(description="One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)")] = None,
        sizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        orientation: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictStr], Field(description="1 = only deleted creatives.")] = None,
        all: Annotated[Optional[StrictStr], Field(description="1 = live and deleted creatives together.")] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.")] = None,
        include_subfolders: Annotated[Optional[StrictStr], Field(description="With folder_id, also return creatives filed in that folder's subfolders.")] = None,
        page: Optional[StrictInt] = None,
        per_page: Annotated[Optional[Any], Field(description="Page size (max 100), or `all` for the whole library in one page.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Offset paging: page size (per_page wins when both are sent).")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Offset paging: rows to skip.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_type: Annotated[Optional[StrictStr], Field(description="Exactly one type; creative_type also takes a list.")] = None,
        filter_sizeid: Annotated[Optional[StrictInt], Field(description="Same as sizeid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List the creative library.

        Uploaded creatives (banner / icon / native / video / reel) owned by the key.

        :param creative_type: One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)
        :type creative_type: str
        :param sizeid: Banner size id.
        :type sizeid: int
        :param orientation:
        :type orientation: str
        :param deleted: 1 = only deleted creatives.
        :type deleted: str
        :param all: 1 = live and deleted creatives together.
        :type all: str
        :param filter_name: Name contains.
        :type filter_name: str
        :param search: Name contains.
        :type search: str
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param folder_id: Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.
        :type folder_id: int
        :param include_subfolders: With folder_id, also return creatives filed in that folder's subfolders.
        :type include_subfolders: str
        :param page:
        :type page: int
        :param per_page: Page size (max 100), or `all` for the whole library in one page.
        :type per_page: ApiV1CreativesGetPerPageParameter
        :param limit: Offset paging: page size (per_page wins when both are sent).
        :type limit: int
        :param offset: Offset paging: rows to skip.
        :type offset: int
        :param filter_id:
        :type filter_id: int
        :param filter_type: Exactly one type; creative_type also takes a list.
        :type filter_type: str
        :param filter_sizeid: Same as sizeid.
        :type filter_sizeid: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_get_serialize(
            creative_type=creative_type,
            sizeid=sizeid,
            orientation=orientation,
            deleted=deleted,
            all=all,
            filter_name=filter_name,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            folder_id=folder_id,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            limit=limit,
            offset=offset,
            filter_id=filter_id,
            filter_type=filter_type,
            filter_sizeid=filter_sizeid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
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
    def api_v1_creatives_get_with_http_info(
        self,
        creative_type: Annotated[Optional[StrictStr], Field(description="One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)")] = None,
        sizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        orientation: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictStr], Field(description="1 = only deleted creatives.")] = None,
        all: Annotated[Optional[StrictStr], Field(description="1 = live and deleted creatives together.")] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.")] = None,
        include_subfolders: Annotated[Optional[StrictStr], Field(description="With folder_id, also return creatives filed in that folder's subfolders.")] = None,
        page: Optional[StrictInt] = None,
        per_page: Annotated[Optional[Any], Field(description="Page size (max 100), or `all` for the whole library in one page.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Offset paging: page size (per_page wins when both are sent).")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Offset paging: rows to skip.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_type: Annotated[Optional[StrictStr], Field(description="Exactly one type; creative_type also takes a list.")] = None,
        filter_sizeid: Annotated[Optional[StrictInt], Field(description="Same as sizeid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List the creative library.

        Uploaded creatives (banner / icon / native / video / reel) owned by the key.

        :param creative_type: One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)
        :type creative_type: str
        :param sizeid: Banner size id.
        :type sizeid: int
        :param orientation:
        :type orientation: str
        :param deleted: 1 = only deleted creatives.
        :type deleted: str
        :param all: 1 = live and deleted creatives together.
        :type all: str
        :param filter_name: Name contains.
        :type filter_name: str
        :param search: Name contains.
        :type search: str
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param folder_id: Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.
        :type folder_id: int
        :param include_subfolders: With folder_id, also return creatives filed in that folder's subfolders.
        :type include_subfolders: str
        :param page:
        :type page: int
        :param per_page: Page size (max 100), or `all` for the whole library in one page.
        :type per_page: ApiV1CreativesGetPerPageParameter
        :param limit: Offset paging: page size (per_page wins when both are sent).
        :type limit: int
        :param offset: Offset paging: rows to skip.
        :type offset: int
        :param filter_id:
        :type filter_id: int
        :param filter_type: Exactly one type; creative_type also takes a list.
        :type filter_type: str
        :param filter_sizeid: Same as sizeid.
        :type filter_sizeid: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_get_serialize(
            creative_type=creative_type,
            sizeid=sizeid,
            orientation=orientation,
            deleted=deleted,
            all=all,
            filter_name=filter_name,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            folder_id=folder_id,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            limit=limit,
            offset=offset,
            filter_id=filter_id,
            filter_type=filter_type,
            filter_sizeid=filter_sizeid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
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
    def api_v1_creatives_get_without_preload_content(
        self,
        creative_type: Annotated[Optional[StrictStr], Field(description="One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)")] = None,
        sizeid: Annotated[Optional[StrictInt], Field(description="Banner size id.")] = None,
        orientation: Optional[StrictStr] = None,
        deleted: Annotated[Optional[StrictStr], Field(description="1 = only deleted creatives.")] = None,
        all: Annotated[Optional[StrictStr], Field(description="1 = live and deleted creatives together.")] = None,
        filter_name: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Name contains.")] = None,
        sort_by: Optional[StrictStr] = None,
        sort_dir: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.")] = None,
        include_subfolders: Annotated[Optional[StrictStr], Field(description="With folder_id, also return creatives filed in that folder's subfolders.")] = None,
        page: Optional[StrictInt] = None,
        per_page: Annotated[Optional[Any], Field(description="Page size (max 100), or `all` for the whole library in one page.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Offset paging: page size (per_page wins when both are sent).")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Offset paging: rows to skip.")] = None,
        filter_id: Optional[StrictInt] = None,
        filter_type: Annotated[Optional[StrictStr], Field(description="Exactly one type; creative_type also takes a list.")] = None,
        filter_sizeid: Annotated[Optional[StrictInt], Field(description="Same as sizeid.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """List the creative library.

        Uploaded creatives (banner / icon / native / video / reel) owned by the key.

        :param creative_type: One creative type, or a comma-separated list: banner, icon, native, push, video, reel, image, creator. (A bare `type` parameter is not read.)
        :type creative_type: str
        :param sizeid: Banner size id.
        :type sizeid: int
        :param orientation:
        :type orientation: str
        :param deleted: 1 = only deleted creatives.
        :type deleted: str
        :param all: 1 = live and deleted creatives together.
        :type all: str
        :param filter_name: Name contains.
        :type filter_name: str
        :param search: Name contains.
        :type search: str
        :param sort_by:
        :type sort_by: str
        :param sort_dir:
        :type sort_dir: str
        :param folder_id: Media-bank folder id. 0 selects the unfiled creatives; omit for every folder.
        :type folder_id: int
        :param include_subfolders: With folder_id, also return creatives filed in that folder's subfolders.
        :type include_subfolders: str
        :param page:
        :type page: int
        :param per_page: Page size (max 100), or `all` for the whole library in one page.
        :type per_page: ApiV1CreativesGetPerPageParameter
        :param limit: Offset paging: page size (per_page wins when both are sent).
        :type limit: int
        :param offset: Offset paging: rows to skip.
        :type offset: int
        :param filter_id:
        :type filter_id: int
        :param filter_type: Exactly one type; creative_type also takes a list.
        :type filter_type: str
        :param filter_sizeid: Same as sizeid.
        :type filter_sizeid: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_get_serialize(
            creative_type=creative_type,
            sizeid=sizeid,
            orientation=orientation,
            deleted=deleted,
            all=all,
            filter_name=filter_name,
            search=search,
            sort_by=sort_by,
            sort_dir=sort_dir,
            folder_id=folder_id,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            limit=limit,
            offset=offset,
            filter_id=filter_id,
            filter_type=filter_type,
            filter_sizeid=filter_sizeid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiV1CreativesGet200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_get_serialize(
        self,
        creative_type,
        sizeid,
        orientation,
        deleted,
        all,
        filter_name,
        search,
        sort_by,
        sort_dir,
        folder_id,
        include_subfolders,
        page,
        per_page,
        limit,
        offset,
        filter_id,
        filter_type,
        filter_sizeid,
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
        if creative_type is not None:
            
            _query_params.append(('creative_type', creative_type))
            
        if sizeid is not None:
            
            _query_params.append(('sizeid', sizeid))
            
        if orientation is not None:
            
            _query_params.append(('orientation', orientation))
            
        if deleted is not None:
            
            _query_params.append(('deleted', deleted))
            
        if all is not None:
            
            _query_params.append(('all', all))
            
        if filter_name is not None:
            
            _query_params.append(('filter_name', filter_name))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if sort_dir is not None:
            
            _query_params.append(('sort_dir', sort_dir))
            
        if folder_id is not None:
            
            _query_params.append(('folder_id', folder_id))
            
        if include_subfolders is not None:
            
            _query_params.append(('include_subfolders', include_subfolders))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if filter_id is not None:
            
            _query_params.append(('filter_id', filter_id))
            
        if filter_type is not None:
            
            _query_params.append(('filter_type', filter_type))
            
        if filter_sizeid is not None:
            
            _query_params.append(('filter_sizeid', filter_sizeid))
            
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
            resource_path='/api/v1/creatives',
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
    def api_v1_creatives_id_delete(
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
        """Delete a creative.


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

        _param = self._api_v1_creatives_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creatives_id_delete_with_http_info(
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
        """Delete a creative.


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

        _param = self._api_v1_creatives_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creatives_id_delete_without_preload_content(
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
        """Delete a creative.


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

        _param = self._api_v1_creatives_id_delete_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_id_delete_serialize(
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




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/creatives/{id}',
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
    def api_v1_creatives_id_get(
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
        """Show one creative.


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

        _param = self._api_v1_creatives_id_get_serialize(
            id=id,
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
    def api_v1_creatives_id_get_with_http_info(
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
        """Show one creative.


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

        _param = self._api_v1_creatives_id_get_serialize(
            id=id,
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
    def api_v1_creatives_id_get_without_preload_content(
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
        """Show one creative.


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

        _param = self._api_v1_creatives_id_get_serialize(
            id=id,
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


    def _api_v1_creatives_id_get_serialize(
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




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/creatives/{id}',
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
    def api_v1_creatives_id_name_put(
        self,
        id: StrictInt,
        api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename a creative (panel inline edit).

        The panel's own rename call. Also retitles the pool items built from this creative. Prefer `PUT /api/v1/creatives/{id}` for new code. 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_name_put_request: (required)
        :type api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_name_put_serialize(
            id=id,
            api_v1_creatives_id_name_put_request=api_v1_creatives_id_name_put_request,
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
    def api_v1_creatives_id_name_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename a creative (panel inline edit).

        The panel's own rename call. Also retitles the pool items built from this creative. Prefer `PUT /api/v1/creatives/{id}` for new code. 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_name_put_request: (required)
        :type api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_name_put_serialize(
            id=id,
            api_v1_creatives_id_name_put_request=api_v1_creatives_id_name_put_request,
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
    def api_v1_creatives_id_name_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename a creative (panel inline edit).

        The panel's own rename call. Also retitles the pool items built from this creative. Prefer `PUT /api/v1/creatives/{id}` for new code. 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_name_put_request: (required)
        :type api_v1_creatives_id_name_put_request: ApiV1CreativesIdNamePutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_name_put_serialize(
            id=id,
            api_v1_creatives_id_name_put_request=api_v1_creatives_id_name_put_request,
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


    def _api_v1_creatives_id_name_put_serialize(
        self,
        id,
        api_v1_creatives_id_name_put_request,
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
        if api_v1_creatives_id_name_put_request is not None:
            _body_params = api_v1_creatives_id_name_put_request


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
            resource_path='/api/v1/creatives/{id}/name',
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
    def api_v1_creatives_id_put(
        self,
        id: StrictInt,
        api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename and/or re-tag a creative.

        The panel's two inline creative edits in one strict call: `name` (also retitles every pool item built from this creative, like the panel rename) and `tags`. Send either or both; unknown fields are a 422. The creative's file / content cannot be changed — upload a new creative instead. Same ownership and member-scope checks as the panel (an own-scoped team member can only edit creatives they made). 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_put_request: (required)
        :type api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_put_serialize(
            id=id,
            api_v1_creatives_id_put_request=api_v1_creatives_id_put_request,
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
    def api_v1_creatives_id_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename and/or re-tag a creative.

        The panel's two inline creative edits in one strict call: `name` (also retitles every pool item built from this creative, like the panel rename) and `tags`. Send either or both; unknown fields are a 422. The creative's file / content cannot be changed — upload a new creative instead. Same ownership and member-scope checks as the panel (an own-scoped team member can only edit creatives they made). 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_put_request: (required)
        :type api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_put_serialize(
            id=id,
            api_v1_creatives_id_put_request=api_v1_creatives_id_put_request,
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
    def api_v1_creatives_id_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Rename and/or re-tag a creative.

        The panel's two inline creative edits in one strict call: `name` (also retitles every pool item built from this creative, like the panel rename) and `tags`. Send either or both; unknown fields are a 422. The creative's file / content cannot be changed — upload a new creative instead. Same ownership and member-scope checks as the panel (an own-scoped team member can only edit creatives they made). 

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_put_request: (required)
        :type api_v1_creatives_id_put_request: ApiV1CreativesIdPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_put_serialize(
            id=id,
            api_v1_creatives_id_put_request=api_v1_creatives_id_put_request,
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


    def _api_v1_creatives_id_put_serialize(
        self,
        id,
        api_v1_creatives_id_put_request,
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
        if api_v1_creatives_id_put_request is not None:
            _body_params = api_v1_creatives_id_put_request


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
            resource_path='/api/v1/creatives/{id}',
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
    def api_v1_creatives_id_tags_put(
        self,
        id: StrictInt,
        api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Replace a creative's tags (panel inline edit).

        The panel's own tag edit. `tags` is an array of tenant tag ids; non-numeric entries are dropped and [] clears the tags.

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_tags_put_request: (required)
        :type api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_tags_put_serialize(
            id=id,
            api_v1_creatives_id_tags_put_request=api_v1_creatives_id_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
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
    def api_v1_creatives_id_tags_put_with_http_info(
        self,
        id: StrictInt,
        api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Replace a creative's tags (panel inline edit).

        The panel's own tag edit. `tags` is an array of tenant tag ids; non-numeric entries are dropped and [] clears the tags.

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_tags_put_request: (required)
        :type api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_tags_put_serialize(
            id=id,
            api_v1_creatives_id_tags_put_request=api_v1_creatives_id_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
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
    def api_v1_creatives_id_tags_put_without_preload_content(
        self,
        id: StrictInt,
        api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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
        """Replace a creative's tags (panel inline edit).

        The panel's own tag edit. `tags` is an array of tenant tag ids; non-numeric entries are dropped and [] clears the tags.

        :param id: (required)
        :type id: int
        :param api_v1_creatives_id_tags_put_request: (required)
        :type api_v1_creatives_id_tags_put_request: ApiV1CreativesIdTagsPutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_creatives_id_tags_put_serialize(
            id=id,
            api_v1_creatives_id_tags_put_request=api_v1_creatives_id_tags_put_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '403': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_id_tags_put_serialize(
        self,
        id,
        api_v1_creatives_id_tags_put_request,
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
        if api_v1_creatives_id_tags_put_request is not None:
            _body_params = api_v1_creatives_id_tags_put_request


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
            resource_path='/api/v1/creatives/{id}/tags',
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
    def api_v1_creatives_id_used_in_get(
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
        """List ads / pools referencing this creative.


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

        _param = self._api_v1_creatives_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creatives_id_used_in_get_with_http_info(
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
        """List ads / pools referencing this creative.


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

        _param = self._api_v1_creatives_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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
    def api_v1_creatives_id_used_in_get_without_preload_content(
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
        """List ads / pools referencing this creative.


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

        _param = self._api_v1_creatives_id_used_in_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_id_used_in_get_serialize(
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




        # authentication setting
        _auth_settings: List[str] = [
            'apiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/creatives/{id}/used-in',
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
    def api_v1_creatives_upload_post(
        self,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One or more creative files.")],
        type: Annotated[Optional[StrictStr], Field(description="audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).")] = None,
        banner_size: Annotated[Optional[StrictInt], Field(description="Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.")] = None,
        tags: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="File the batch into this existing media-bank folder. Omit or 0 for unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder with this name under folder_id and file the batch there.")] = None,
        upload_zip: Annotated[Optional[StrictStr], Field(description="Send one archive as `zipfile` instead of `files`; the server extracts it.")] = None,
        folder_from_zip: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.")] = None,
        folder_from_zip_paths: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.")] = None,
        zipfile: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="With upload_zip=1: the archive to extract.")] = None,
        icontags: Annotated[Optional[StrictStr], Field(description="type=icon only: tags for the icons; overrides `tags` when sent.")] = None,
        properties: Annotated[Optional[StrictStr], Field(description="Comma-separated property ids stamped on every created creative.")] = None,
        skiperrors: Annotated[Optional[StrictStr], Field(description="1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.")] = None,
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
        """Upload creative files.

        `multipart/form-data` upload of one or more real creative files. The server stores each file, creates a `creatives` row and returns the new ids — reference them later via `creative_id` on ad-create or pool-item-add. Field `files` (repeatable) carries the uploads (`files[]`, `files[0]`…, `image`, `image[]`, `image[0]`… and a singular `file` / `file[]` are accepted too); `type` selects the creative kind. `creator` takes a poster image paired with a hover video; `skin` a site-skin image; `html5` takes HTML5 rich-media banners — each file is one .zip with an index.html at the top (or inside one top folder), max 5 MB zipped / 20 MB unpacked / 300 files, only web file types (html, css, js, json, images, fonts, mp4/webm/mp3). The size is `banner_size` or the bundle's `<meta name=\"ad.size\" content=\"width=300,height=250\">`. It is created as a banner creative (content_type `html5`) and served as an iframe with the IAB `clickTag` query parameter (also `clickTAG`, `clicktag`) set to its click URL — open it from the creative's click handler (`window.open(clickTag)`) so the click is counted. `upload_zip=1` is refused for html5 (each zip is one banner). 

        :param files: One or more creative files. (required)
        :type files: List[bytes]
        :param type: audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).
        :type type: str
        :param banner_size: Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.
        :type banner_size: int
        :param tags:
        :type tags: str
        :param folder_id: File the batch into this existing media-bank folder. Omit or 0 for unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder with this name under folder_id and file the batch there.
        :type folder_name: str
        :param upload_zip: Send one archive as `zipfile` instead of `files`; the server extracts it.
        :type upload_zip: str
        :param folder_from_zip: ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.
        :type folder_from_zip: str
        :param folder_from_zip_paths: ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.
        :type folder_from_zip_paths: str
        :param zipfile: With upload_zip=1: the archive to extract.
        :type zipfile: bytes
        :param icontags: type=icon only: tags for the icons; overrides `tags` when sent.
        :type icontags: str
        :param properties: Comma-separated property ids stamped on every created creative.
        :type properties: str
        :param skiperrors: 1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.
        :type skiperrors: str
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

        _param = self._api_v1_creatives_upload_post_serialize(
            files=files,
            type=type,
            banner_size=banner_size,
            tags=tags,
            folder_id=folder_id,
            folder_name=folder_name,
            upload_zip=upload_zip,
            folder_from_zip=folder_from_zip,
            folder_from_zip_paths=folder_from_zip_paths,
            zipfile=zipfile,
            icontags=icontags,
            properties=properties,
            skiperrors=skiperrors,
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
            '400': None,
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
    def api_v1_creatives_upload_post_with_http_info(
        self,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One or more creative files.")],
        type: Annotated[Optional[StrictStr], Field(description="audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).")] = None,
        banner_size: Annotated[Optional[StrictInt], Field(description="Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.")] = None,
        tags: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="File the batch into this existing media-bank folder. Omit or 0 for unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder with this name under folder_id and file the batch there.")] = None,
        upload_zip: Annotated[Optional[StrictStr], Field(description="Send one archive as `zipfile` instead of `files`; the server extracts it.")] = None,
        folder_from_zip: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.")] = None,
        folder_from_zip_paths: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.")] = None,
        zipfile: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="With upload_zip=1: the archive to extract.")] = None,
        icontags: Annotated[Optional[StrictStr], Field(description="type=icon only: tags for the icons; overrides `tags` when sent.")] = None,
        properties: Annotated[Optional[StrictStr], Field(description="Comma-separated property ids stamped on every created creative.")] = None,
        skiperrors: Annotated[Optional[StrictStr], Field(description="1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.")] = None,
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
        """Upload creative files.

        `multipart/form-data` upload of one or more real creative files. The server stores each file, creates a `creatives` row and returns the new ids — reference them later via `creative_id` on ad-create or pool-item-add. Field `files` (repeatable) carries the uploads (`files[]`, `files[0]`…, `image`, `image[]`, `image[0]`… and a singular `file` / `file[]` are accepted too); `type` selects the creative kind. `creator` takes a poster image paired with a hover video; `skin` a site-skin image; `html5` takes HTML5 rich-media banners — each file is one .zip with an index.html at the top (or inside one top folder), max 5 MB zipped / 20 MB unpacked / 300 files, only web file types (html, css, js, json, images, fonts, mp4/webm/mp3). The size is `banner_size` or the bundle's `<meta name=\"ad.size\" content=\"width=300,height=250\">`. It is created as a banner creative (content_type `html5`) and served as an iframe with the IAB `clickTag` query parameter (also `clickTAG`, `clicktag`) set to its click URL — open it from the creative's click handler (`window.open(clickTag)`) so the click is counted. `upload_zip=1` is refused for html5 (each zip is one banner). 

        :param files: One or more creative files. (required)
        :type files: List[bytes]
        :param type: audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).
        :type type: str
        :param banner_size: Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.
        :type banner_size: int
        :param tags:
        :type tags: str
        :param folder_id: File the batch into this existing media-bank folder. Omit or 0 for unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder with this name under folder_id and file the batch there.
        :type folder_name: str
        :param upload_zip: Send one archive as `zipfile` instead of `files`; the server extracts it.
        :type upload_zip: str
        :param folder_from_zip: ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.
        :type folder_from_zip: str
        :param folder_from_zip_paths: ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.
        :type folder_from_zip_paths: str
        :param zipfile: With upload_zip=1: the archive to extract.
        :type zipfile: bytes
        :param icontags: type=icon only: tags for the icons; overrides `tags` when sent.
        :type icontags: str
        :param properties: Comma-separated property ids stamped on every created creative.
        :type properties: str
        :param skiperrors: 1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.
        :type skiperrors: str
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

        _param = self._api_v1_creatives_upload_post_serialize(
            files=files,
            type=type,
            banner_size=banner_size,
            tags=tags,
            folder_id=folder_id,
            folder_name=folder_name,
            upload_zip=upload_zip,
            folder_from_zip=folder_from_zip,
            folder_from_zip_paths=folder_from_zip_paths,
            zipfile=zipfile,
            icontags=icontags,
            properties=properties,
            skiperrors=skiperrors,
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
            '400': None,
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
    def api_v1_creatives_upload_post_without_preload_content(
        self,
        files: Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="One or more creative files.")],
        type: Annotated[Optional[StrictStr], Field(description="audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).")] = None,
        banner_size: Annotated[Optional[StrictInt], Field(description="Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.")] = None,
        tags: Optional[StrictStr] = None,
        folder_id: Annotated[Optional[StrictInt], Field(description="File the batch into this existing media-bank folder. Omit or 0 for unfiled.")] = None,
        folder_name: Annotated[Optional[StrictStr], Field(description="Create-or-reuse a folder with this name under folder_id and file the batch there.")] = None,
        upload_zip: Annotated[Optional[StrictStr], Field(description="Send one archive as `zipfile` instead of `files`; the server extracts it.")] = None,
        folder_from_zip: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.")] = None,
        folder_from_zip_paths: Annotated[Optional[StrictStr], Field(description="ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.")] = None,
        zipfile: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="With upload_zip=1: the archive to extract.")] = None,
        icontags: Annotated[Optional[StrictStr], Field(description="type=icon only: tags for the icons; overrides `tags` when sent.")] = None,
        properties: Annotated[Optional[StrictStr], Field(description="Comma-separated property ids stamped on every created creative.")] = None,
        skiperrors: Annotated[Optional[StrictStr], Field(description="1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.")] = None,
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
        """Upload creative files.

        `multipart/form-data` upload of one or more real creative files. The server stores each file, creates a `creatives` row and returns the new ids — reference them later via `creative_id` on ad-create or pool-item-add. Field `files` (repeatable) carries the uploads (`files[]`, `files[0]`…, `image`, `image[]`, `image[0]`… and a singular `file` / `file[]` are accepted too); `type` selects the creative kind. `creator` takes a poster image paired with a hover video; `skin` a site-skin image; `html5` takes HTML5 rich-media banners — each file is one .zip with an index.html at the top (or inside one top folder), max 5 MB zipped / 20 MB unpacked / 300 files, only web file types (html, css, js, json, images, fonts, mp4/webm/mp3). The size is `banner_size` or the bundle's `<meta name=\"ad.size\" content=\"width=300,height=250\">`. It is created as a banner creative (content_type `html5`) and served as an iframe with the IAB `clickTag` query parameter (also `clickTAG`, `clicktag`) set to its click URL — open it from the creative's click handler (`window.open(clickTag)`) so the click is counted. `upload_zip=1` is refused for html5 (each zip is one banner). 

        :param files: One or more creative files. (required)
        :type files: List[bytes]
        :param type: audio = audio-ad creatives (mp3, m4a, aac, ogg, opus or wav, 3-120 s): re-encoded to a 128 kbps mp3, stored as <id>.mp3, the duration measured. Use the id as creative_id with video_type=creative on an audio ad (adtype 43).
        :type type: str
        :param banner_size: Banner size id; auto-derived from image dimensions when omitted. An image exactly 2x or 3x a size is kept at full resolution under that size (served at the size, sharp on high-density screens); pass the 1x size id when the 2x dimensions are a size of their own.
        :type banner_size: int
        :param tags:
        :type tags: str
        :param folder_id: File the batch into this existing media-bank folder. Omit or 0 for unfiled.
        :type folder_id: int
        :param folder_name: Create-or-reuse a folder with this name under folder_id and file the batch there.
        :type folder_name: str
        :param upload_zip: Send one archive as `zipfile` instead of `files`; the server extracts it.
        :type upload_zip: str
        :param folder_from_zip: ZIP uploads only: name the folder after the archive (extension dropped), under folder_id / folder_name.
        :type folder_from_zip: str
        :param folder_from_zip_paths: ZIP uploads only: recreate the archive's own directories as subfolders, up to 3 tiers.
        :type folder_from_zip_paths: str
        :param zipfile: With upload_zip=1: the archive to extract.
        :type zipfile: bytes
        :param icontags: type=icon only: tags for the icons; overrides `tags` when sent.
        :type icontags: str
        :param properties: Comma-separated property ids stamped on every created creative.
        :type properties: str
        :param skiperrors: 1 = keep going past a file that fails and report it in `errors`; 0 stops at the first failure.
        :type skiperrors: str
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

        _param = self._api_v1_creatives_upload_post_serialize(
            files=files,
            type=type,
            banner_size=banner_size,
            tags=tags,
            folder_id=folder_id,
            folder_name=folder_name,
            upload_zip=upload_zip,
            folder_from_zip=folder_from_zip,
            folder_from_zip_paths=folder_from_zip_paths,
            zipfile=zipfile,
            icontags=icontags,
            properties=properties,
            skiperrors=skiperrors,
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
            '400': None,
            '409': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_creatives_upload_post_serialize(
        self,
        files,
        type,
        banner_size,
        tags,
        folder_id,
        folder_name,
        upload_zip,
        folder_from_zip,
        folder_from_zip_paths,
        zipfile,
        icontags,
        properties,
        skiperrors,
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
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if type is not None:
            _form_params.append(('type', type))
        if files is not None:
            _files['files'] = files
        if banner_size is not None:
            _form_params.append(('banner_size', banner_size))
        if tags is not None:
            _form_params.append(('tags', tags))
        if folder_id is not None:
            _form_params.append(('folder_id', folder_id))
        if folder_name is not None:
            _form_params.append(('folder_name', folder_name))
        if upload_zip is not None:
            _form_params.append(('upload_zip', upload_zip))
        if folder_from_zip is not None:
            _form_params.append(('folder_from_zip', folder_from_zip))
        if folder_from_zip_paths is not None:
            _form_params.append(('folder_from_zip_paths', folder_from_zip_paths))
        if zipfile is not None:
            _files['zipfile'] = zipfile
        if icontags is not None:
            _form_params.append(('icontags', icontags))
        if properties is not None:
            _form_params.append(('properties', properties))
        if skiperrors is not None:
            _form_params.append(('skiperrors', skiperrors))
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
            resource_path='/api/v1/creatives/upload',
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



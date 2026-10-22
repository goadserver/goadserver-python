# coding: utf-8

"""
    GoAdServer Public API

    Public REST API for advertisers and publishers on the GoAdServer platform.  **Authentication.** All endpoints (except `/api/public/*`) require an API key passed as `Authorization: Bearer gas_live_…`. Create and manage keys in your account settings — each key has its own scopes, optional resource pinning, optional IP allowlist, and per-key rate limit.  **Apps (OAuth 2.0).** A tool other people connect uses an app token instead: authorization code + PKCE at `/oauth/authorize`, tokens from `/api/public/oauth/token`, passed as `Authorization: Bearer oat_…` on the same endpoints with the same scopes. See the [Build an integration](/api/docs/integrations) guide.  **System rules apply over API rules.** The public API never lets a key bypass restrictions the same user faces in the panel:  - **Source names** (`stats_source_names` right). When the user lacks   this right, advertiser stats responses return `{id, name}` with   `name` equal to the id — no human label leaks through. - **SubID encoding** (`modules.global.subid_encoding`). When enabled   for the system, the user only ever sees encoded SubIDs in the panel.   The API mirrors this both ways: `subid_excl`/`subid_incl` filter   endpoints accept the encoded form on write (decoded server-side   before storage) and emit the encoded form on read. A plain SubID   sent on write is stored as sent — a value is decoded only when it is   a genuine encoded token. - **Module gating.** Endpoints whose module is disabled for the   tenant don't appear in the spec or routes.txt at all.  **Rate limits.** Every response to an API key or app token carries the caller's budget for the current one-minute window:  | Header | Meaning | |---|---| | `X-RateLimit-Limit` | Requests per minute for this key (its `rate_limit_rpm`, default 60; an app's per-installation limit for app tokens). | | `X-RateLimit-Remaining` | Calls left in the current window. | | `X-RateLimit-Reset` | Unix seconds at which the window resets. | | `Retry-After` | On `429 rate_limited` only: seconds until a retry can succeed. |  Windows are fixed and start with the first call, so `Reset` is exact. The MCP endpoint (`POST /api/v1/mcp`) is charged per `tools/call` against its own bucket (default 240/min), and its response headers report that bucket; an exhausted MCP bucket answers the tool call with an error result rather than an HTTP 429, and the HTTP response then carries `Retry-After`.  **Idempotent writes.** Send `Idempotency-Key: <1–255 printable ASCII characters>` (a UUID is ideal) on a `POST` or `PATCH` to make a retry safe. For 24 hours per key (per app installation for app tokens):  - the first request runs and its response — status, body, `Content-Type`,   `Location`, `ETag` — is stored; - the same key with the same method, path, query and body replays that   response without running anything, adding `Idempotent-Replayed: true`; - the same key with a different request is `422 idempotency_key_reused`; - the same key while the first request is still running is   `409 idempotency_key_in_progress` (with `Retry-After: 1`).  `5xx` results are not stored — the key is released and a retry runs again. Bodies over 32 MB cannot carry the header (`413`). An invalid key is `400 invalid_idempotency_key`.  **Concurrency control (ETag / If-Match).** Every JSON `GET` response (up to 1 MB) carries a weak `ETag`, a hash of the body. Send it back:  - `If-None-Match: <etag>` on a `GET` — `304 Not Modified` when unchanged; - `If-Match: <etag>` on a `PATCH`, `PUT` or `DELETE` — the server reads the   resource's current representation (the `GET` of the same path, or of the   nearest parent path that has a `GET`: `PATCH …/campaigns/ron/7/active` is   checked against `GET …/campaigns/ron/7`) and answers   `412 precondition_failed` when it no longer matches, with the current tag in   `ETag` and `current_etag`. `If-Match: *` only requires the resource to   exist. A resource with no readable representation is also `412`.  The check is optimistic, not a lock: it closes the read-modify-write window two agents (or an agent and a person in the panel) would otherwise race in. Fields that change on their own (live spend counters) change the tag too — re-read and retry. A write response carries no new ETag; `GET` again.  **Strict fields.** Unknown body fields are a client error, not something to ignore: a request that sends a field the endpoint does not accept gets `422 unknown_fields` naming it. This is the default for keys created from 2026-10-12 (the key's `strict_fields` setting, shown on the key screen); older keys keep ignoring unknown fields (except on the few endpoints that have always refused them — the budget and on/off toggles). Override per request with `?strict=1` (reject) or `?strict=0` (ignore, everywhere). App tokens default to ignoring unknown fields; `?strict=1` opts in.  **Errors.** Every non-2xx response has the same shape:  ```json { \"error\": \"validation_error\", \"message\": \"Name is required.\", \"errors\": { \"name\": [\"Name is required.\"] } } ```  `error` is a stable machine-readable code — branch on it, never on `message`. `errors` (field → messages) appears on field-level validation failures; some codes add their own members (`scope`, `accepted_scopes`, `unknown_fields`, `current_etag`). Codes:  | Status | Codes | |---|---| | 400 | `bad_request`, `invalid_idempotency_key`, `invalid_body` | | 401 | `unauthenticated`, `invalid_api_key`, `revoked_api_key`, `expired_api_key`, `invalid_token`, `revoked_token`, `expired_token`, `user_not_found`, `account_deleted`, `account_disabled`, `admin_key_on_user_api`, `user_key_on_admin_api` | | 403 | `forbidden`, `missing_scope`, `forbidden_resource`, `ip_not_allowed`, `api_disabled`, `systemid_mismatch`, `endpoint_not_api_accessible`, `oauth_token_wrong_surface`, `mcp_not_enabled_for_app` | | 404 | `not_found` (also a disabled module or missing right — see ModuleDisabled) | | 405 | `method_not_allowed` — the `Allow` header (and the message) lists the methods the path does accept | | 409 | `conflict`, `idempotency_key_in_progress`, and resource-specific conflicts (e.g. `email_exists`) | | 412 | `precondition_failed` | | 413 | `payload_too_large` | | 422 | `validation_error`, `unknown_fields`, `idempotency_key_reused` | | 429 | `rate_limited` | | 5xx | `server_error`, `service_unavailable`, `bad_gateway`, `gateway_timeout` |  Endpoint-specific codes are listed on the endpoint. A response that would otherwise lack a code gets the generic one for its status from this table.  **Client SDKs.** Each SDK is generated from this spec and published as a public GitHub repository under the `goadserver` organization. The same tarball is also embedded in the API server and downloadable from `/api/public/sdk/<lang>.tgz` — useful when GitHub is unreachable.  > **Per-network host.** The default `https://up.go-adserver.com` > baked into the published SDKs is a reference host. Every white-label > tenant runs on its own panel domain — override the host on first use > (`setHost()` / `Configuration.host` / `basePath` etc.). Or, fetch the > spec from your own tenant (`/api/public/openapi.yaml` returns it with > *your* hostname as the default) and regenerate the SDK locally — the > regenerated client has your URL baked in.  - **PHP** — `github.com/goadserver/goadserver-php`   (namespace `GoAdServer\\Api`, composer name `goadserver/sdk`).    ```bash   composer config repositories.goadserver vcs https://github.com/goadserver/goadserver-php   composer require goadserver/sdk:dev-main   ```    ```php   $cfg = GoAdServer\\Api\\Configuration::getDefaultConfiguration()           ->setHost('https://up.go-adserver.com')           ->setAccessToken('gas_live_…');   $api = new GoAdServer\\Api\\Api\\AccountAPIApi(null, $cfg);   $me  = $api->apiV1AccountGet();   ```  - **Go** — `github.com/goadserver/goadserver-go`.    ```bash   go get github.com/goadserver/goadserver-go@latest   ```    ```go   import gas \"github.com/goadserver/goadserver-go\"    cfg := gas.NewConfiguration()   cfg.Servers = gas.ServerConfigurations{{URL: \"https://up.go-adserver.com\"}}   cli := gas.NewAPIClient(cfg)   ctx := context.WithValue(context.Background(),       gas.ContextAccessToken, \"gas_live_…\")   me, _, err := cli.AccountAPI.ApiV1AccountGet(ctx).Execute()   ```  - **Python** — `github.com/goadserver/goadserver-python` (package   `goadserver`). Pulls `pydantic` + `urllib3` automatically.    ```bash   pip install git+https://github.com/goadserver/goadserver-python.git   ```    ```python   from goadserver import ApiClient, Configuration   from goadserver.api import AccountApi, CampaignsApi    cfg = Configuration(host=\"https://up.go-adserver.com\")   cfg.access_token = \"gas_live_…\"   client = ApiClient(cfg)    me = AccountApi(client).api_v1_account_get()   camps = CampaignsApi(client).api_v1_campaigns_get(per_page=10)   ```  - **JavaScript / TypeScript** — `github.com/goadserver/goadserver-js`   (npm name `goadserver-sdk`, generator `typescript-fetch`).    ```bash   npm install github:goadserver/goadserver-js   ```    ```ts   import { Configuration, AccountApi, CampaignsApi }     from \"goadserver-sdk\";    const cfg = new Configuration({     basePath: \"https://up.go-adserver.com\",     accessToken: \"gas_live_…\",   });    const me   = await new AccountApi(cfg).apiV1AccountGet();   const list = await new CampaignsApi(cfg).apiV1CampaignsGet({ perPage: 10 });   ```    The CJS build is broadly compatible (Node + bundlers); the ESM   build is missing trailing `.js` extensions in its imports, a known   `typescript-fetch` quirk — most consumers use CJS.  **Offline / firewalled install.** If the customer's network can't reach GitHub, every SDK's source is also served as a tarball from the API host:  ```bash curl -O https://up.go-adserver.com/api/public/sdk/python.tgz tar xzf python.tgz && pip install ./python ```  Round-trip smoke tests for all four SDKs live at `clients/_smoke/` in the platform repo. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AdspaceCreateScreenSettings(BaseModel):
    """
    DOOH screens (screens, adzone type 45): a digital-signage screen. The zone also needs its banner size (adsizeid / banner_settings.sizeid, e.g. 1920x1080). The screen's player pulls a playlist: GET https://<ad domain>/screen.go?spaceid=<zone>&key=<screen_key>[&n=1-20][&format=vast] → {screen:{spaceid, width, height, orientation, venue_type}, open, refresh_seconds, ads:[{id, type: image|video|iframe|html, url, html, width, height, duration, title, proof_url}]} (format=vast: VAST 4 with one Ad per item in play order, Impression = proof_url; iframe/html items are left out). Fire proof_url when an ad has really played — proof of play, counted once per play and only within 3 hours of the pull; it books one impression whose cost is the CPM bid × audience_per_play. Outside opening_hours the playlist is empty (open: false). act=player&spaceid=&key= is a ready full-screen web player for any browser in kiosk mode. Screens play only banner campaigns with options.screens.on (campaign field `screens`). screen_key is generated on create and returned read-only (also in GET /adspaces/{id}/code → screen); rotate_key: true issues a new one. 
    """ # noqa: E501
    venue_type: Optional[StrictStr] = Field(default='other', description="Where the screen hangs; campaigns can target venue types. Anything else is 422 `screen_settings.venue_type`.")
    lat: Optional[Union[Annotated[float, Field(le=90, strict=True, ge=-90)], Annotated[int, Field(le=90, strict=True, ge=-90)]]] = Field(default=0, description="Latitude, for campaign geo-fences (out of range 422).")
    lon: Optional[Union[Annotated[float, Field(le=180, strict=True, ge=-180)], Annotated[int, Field(le=180, strict=True, ge=-180)]]] = Field(default=0, description="Longitude (out of range 422).")
    address: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default='', description="For your own reference; plain text.")
    width: Optional[Annotated[int, Field(le=16384, strict=True, ge=0)]] = Field(default=1920, description="Screen width in px (clamped).")
    height: Optional[Annotated[int, Field(le=16384, strict=True, ge=0)]] = Field(default=1080, description="Screen height in px (clamped).")
    orientation: Optional[StrictStr] = 'landscape'
    audience_per_play: Optional[Union[Annotated[float, Field(le=10000, strict=True, ge=1)], Annotated[int, Field(le=10000, strict=True, ge=1)]]] = Field(default=1, description="People who see one play (clamped). A proof of play costs the CPM bid × this.")
    opening_hours: Optional[StrictStr] = Field(default='', description="Daily on-air window HH:MM-HH:MM in `timezone` (22:00-06:00 spans midnight); empty = always. Malformed 422 `screen_settings.opening_hours`.")
    timezone: Optional[StrictStr] = Field(default='', description="IANA time zone for opening_hours; empty = the ad server's. Unknown 422.")
    slot_seconds: Optional[Annotated[int, Field(le=120, strict=True, ge=5)]] = Field(default=10, description="Seconds an image ad stays on screen (clamped); a video plays to its end.")
    playlist_size: Optional[Annotated[int, Field(le=20, strict=True, ge=1)]] = Field(default=6, description="Ads per pull (clamped).")
    screen_key: Optional[StrictStr] = Field(default=None, description="The key the player sends. Ignored on write.")
    rotate_key: Optional[StrictBool] = Field(default=None, description="true issues a new screen_key (the current player stops).")
    __properties: ClassVar[List[str]] = ["venue_type", "lat", "lon", "address", "width", "height", "orientation", "audience_per_play", "opening_hours", "timezone", "slot_seconds", "playlist_size", "screen_key", "rotate_key"]

    @field_validator('venue_type')
    def venue_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['retail', 'mall', 'supermarket', 'restaurant', 'bar', 'hotel', 'gym', 'office', 'transit', 'airport', 'gas_station', 'pharmacy', 'hospital', 'university', 'cinema', 'outdoor', 'other']):
            raise ValueError("must be one of enum values ('retail', 'mall', 'supermarket', 'restaurant', 'bar', 'hotel', 'gym', 'office', 'transit', 'airport', 'gas_station', 'pharmacy', 'hospital', 'university', 'cinema', 'outdoor', 'other')")
        return value

    @field_validator('orientation')
    def orientation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['landscape', 'portrait']):
            raise ValueError("must be one of enum values ('landscape', 'portrait')")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AdspaceCreateScreenSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "screen_key",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdspaceCreateScreenSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "venue_type": obj.get("venue_type") if obj.get("venue_type") is not None else 'other',
            "lat": obj.get("lat") if obj.get("lat") is not None else 0,
            "lon": obj.get("lon") if obj.get("lon") is not None else 0,
            "address": obj.get("address") if obj.get("address") is not None else '',
            "width": obj.get("width") if obj.get("width") is not None else 1920,
            "height": obj.get("height") if obj.get("height") is not None else 1080,
            "orientation": obj.get("orientation") if obj.get("orientation") is not None else 'landscape',
            "audience_per_play": obj.get("audience_per_play") if obj.get("audience_per_play") is not None else 1,
            "opening_hours": obj.get("opening_hours") if obj.get("opening_hours") is not None else '',
            "timezone": obj.get("timezone") if obj.get("timezone") is not None else '',
            "slot_seconds": obj.get("slot_seconds") if obj.get("slot_seconds") is not None else 10,
            "playlist_size": obj.get("playlist_size") if obj.get("playlist_size") is not None else 6,
            "screen_key": obj.get("screen_key"),
            "rotate_key": obj.get("rotate_key")
        })
        return _obj



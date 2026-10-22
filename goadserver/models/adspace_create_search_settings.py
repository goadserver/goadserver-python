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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from goadserver.models.adspace_create_search_settings_blocked_terms import AdspaceCreateSearchSettingsBlockedTerms
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AdspaceCreateSearchSettings(BaseModel):
    """
    Search Ads zones (search_ads, adzone type 42): native-style ads shown for what visitors type into the publisher's own search box, through the goCtrl `search` plugin. They serve only Search Ads campaigns (ad type 42, `searchads` — a copy of native bought as its own campaign type), never regular natives. The query is matched against campaign keyword targeting; campaigns without keywords serve on any query. Queries on the built-in blocked-term list (minors, non-consent, violence, …) never get an ad and leave no stats row; `blocked_terms` adds the zone's own list. These values are written into the generated embed code (GET /api/v1/adspaces/{id}/code). 
    """ # noqa: E501
    mode: Optional[StrictStr] = Field(default='dropdown', description="chat = AI chat ads: the goCtrl `chatads` plugin watches the site's chat widget (chat_container / chat_answer / chat_prompt) and puts a labelled ad card under a finished answer, matched on the visitor's prompt like a search (impression when half on screen). AI apps without a web widget call the ad server directly — GET https://<ad domain>/chatad.go?spaceid=<zone>&q=<prompt>&a=<answer>&n=1-4&ip=<visitor ip>&agent=<visitor user agent> answers {ads:[{title, description, display_url, image, click_url, impression_url, click_log_url, followup, price}], label}; the prompt and the answer are both checked against the blocked-term list; fire impression_url only when the ad is shown. followup (when the advertiser set one) is a sponsored follow-up question: show it as a chip, and when the user picks it ask your chat that question and fire click_log_url (a click without a redirect). price is for product cards. intext = in-text ads, no search box: the goCtrl `intext` plugin picks the most frequent words and two-word phrases of the article (container_selector), asks the zone for an ad per term as if it were a search, and turns the first occurrence of each term that got an ad into a link with a hover card (impression counted when the card opens), at most max_links per page; the generated code is a single intext init, no placement element. dropdown = the plugin opens its own box under the input (ads + recent searches); panel = ads go into a placement element inside the site's existing suggestions panel; box = the plugin draws the search box itself into a placement div (gcs_box_<id>, in the generated code) and opens the dropdown under it — input_selector is not used; results = the ads are listed in the page itself, in the normal page flow instead of a floating dropdown: in the site's own div id_<id> when the page has one (optional), otherwise right under the search box. The box is the site's own (input_selector) or, with input_selector empty, one the plugin draws (gcs_box_<id>). The list updates as the visitor types and on Enter; a search in the page URL (query_param) is filled in on load.")
    input_selector: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="CSS selector matching exactly one search input.")
    panel_selector: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="panel mode: the site's suggestions panel; ads are only requested while it is visible.")
    container_selector: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="intext mode: the article text to link in; empty = the page's <article>, else <main>, else the body. Links, headings, nav, header, footer and form fields are never touched.")
    max_links: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="intext mode: most ad links per page (clamped).")
    chat_container: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="chat mode: the chat's message list.")
    chat_answer: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="chat mode: the assistant's answer bubbles; the card goes under the newest finished one.")
    chat_prompt: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="chat mode: the visitor's messages; the newest is the prompt.")
    chat_every: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=1, description="chat mode: an ad under every Nth answer (clamped).")
    chat_style: Optional[StrictStr] = Field(default='card', description="chat mode: card = one ad card under the answer; products = a row of chat_products product cards with their price (ad_options.chat.price, filled by product feeds).")
    chat_products: Optional[Annotated[int, Field(le=4, strict=True, ge=2)]] = Field(default=3, description="chat mode, products style: cards in the row (clamped).")
    chat_followups: Optional[Annotated[int, Field(le=2, strict=True, ge=0)]] = Field(default=0, description="chat mode: sponsored follow-up chips per answer, 0 = off. A chip shows an ad's own follow-up question (ad_options.chat.followup); picking it counts a click (no redirect) and asks the chat: a cancelable goctrl-followup event {question, hash, sid} on chat_container first, else the question is typed into chat_input and chat_send clicked (or Enter / the form submitted).")
    chat_input: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="chat mode with follow-ups: the chat's text box.")
    chat_send: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="chat mode with follow-ups: the send button; empty = Enter / the form's submit.")
    results: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=1, description="Ads per search.")
    recent: Optional[Annotated[int, Field(le=10, strict=True, ge=0)]] = Field(default=5, description="dropdown mode: recent searches listed (0 = off).")
    min_chars: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Characters typed before ads are requested.")
    theme: Optional[StrictStr] = Field(default='auto', description="Colour scheme of the dropdown (dropdown and box mode) and of the results-mode ads.")
    label: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default='Ad', description="Disclosure label on every result; HTML and quote characters are stripped.")
    layout: Optional[StrictStr] = Field(default='card', description="A zone created without layout starts as suggestion, and without native_settings.orientation as square; a stored zone that never had the key reads as card. With native_settings.orientation square the card and result images are drawn square. How each ad looks: card = image, title, description and display URL; suggestion = one compact line (small image + title) like a search suggestion; result = reads like an organic search result (label + display URL, the title as a link, the full description, a small image on the right), made for results mode. Picks the tpl_item in the generated code.")
    placeholder: Optional[Annotated[str, Field(strict=True, max_length=60)]] = Field(default='Search', description="box mode, and results mode without input_selector: text in the empty search box; HTML and quote characters are stripped.")
    submit_url: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default='', description="box mode: where a search goes on Enter; {q} = the URL-encoded search text (without {q} it is appended as ?q=). http(s) only — anything else is stored as empty. Empty = the box only shows ads and recent searches.")
    query_param: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default='q', description="results mode: the URL parameter a search is filled in from when the page loads (https://example.com/search?q=… → q). Letters, digits, _ . - only; anything else is stored as q.")
    ad_position: Optional[StrictStr] = Field(default='top', description="dropdown and box mode: the ads above (top) or below (bottom) the recent searches in the plugin's own dropdown. In panel mode the ads go wherever the site put the placement div.")
    on_open: Optional[StrictBool] = Field(default=False, description="dropdown, box and panel mode (in panel mode the ad goes into the slot inside the site's own suggestions panel when the box gets focus): when the visitor opens the box with nothing (or fewer than min_chars characters) typed, show an untargeted ad (campaigns without keywords); the query-matched ad replaces it once the text is long enough. The short text is never sent as keywords, and an ad still on screen is reused rather than asked for again.")
    recent_pick: Optional[StrictStr] = Field(default='submit', description="dropdown and box mode: picking a recent search submits it (submit) or only puts it into the box and shows the ads for it (fill).")
    show_description: Optional[StrictBool] = Field(default=True, description="card and result layouts: show the ad's description. The suggestion layout never does.")
    show_url: Optional[StrictBool] = Field(default=True, description="card and result layouts: show the ad's display URL. The suggestion layout never does.")
    blocked_terms: Optional[AdspaceCreateSearchSettingsBlockedTerms] = None
    runtime: Optional[Dict[str, Any]] = Field(default=None, description="Read-only, derived on every save (search-box modes only; absent for intext and chat): the zone's display settings as the goCtrl search plugin applies them at page load over the values in the pasted code — results, min_chars, recent, theme, ad_position, on_open, recent_pick, placeholder, submit_url, param, tpl_body, tpl_row, tpl_item. A change to those settings reaches pages without new code; selectors and placement still come from the code. Ignored when sent.")
    __properties: ClassVar[List[str]] = ["mode", "input_selector", "panel_selector", "container_selector", "max_links", "chat_container", "chat_answer", "chat_prompt", "chat_every", "chat_style", "chat_products", "chat_followups", "chat_input", "chat_send", "results", "recent", "min_chars", "theme", "label", "layout", "placeholder", "submit_url", "query_param", "ad_position", "on_open", "recent_pick", "show_description", "show_url", "blocked_terms", "runtime"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['dropdown', 'panel', 'box', 'results', 'intext', 'chat']):
            raise ValueError("must be one of enum values ('dropdown', 'panel', 'box', 'results', 'intext', 'chat')")
        return value

    @field_validator('chat_style')
    def chat_style_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['card', 'products']):
            raise ValueError("must be one of enum values ('card', 'products')")
        return value

    @field_validator('theme')
    def theme_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['auto', 'light', 'dark']):
            raise ValueError("must be one of enum values ('auto', 'light', 'dark')")
        return value

    @field_validator('layout')
    def layout_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['card', 'suggestion', 'result']):
            raise ValueError("must be one of enum values ('card', 'suggestion', 'result')")
        return value

    @field_validator('ad_position')
    def ad_position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['top', 'bottom']):
            raise ValueError("must be one of enum values ('top', 'bottom')")
        return value

    @field_validator('recent_pick')
    def recent_pick_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['submit', 'fill']):
            raise ValueError("must be one of enum values ('submit', 'fill')")
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
        """Create an instance of AdspaceCreateSearchSettings from a JSON string"""
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
            "runtime",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of blocked_terms
        if self.blocked_terms:
            _dict['blocked_terms'] = self.blocked_terms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdspaceCreateSearchSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mode": obj.get("mode") if obj.get("mode") is not None else 'dropdown',
            "input_selector": obj.get("input_selector"),
            "panel_selector": obj.get("panel_selector"),
            "container_selector": obj.get("container_selector"),
            "max_links": obj.get("max_links") if obj.get("max_links") is not None else 3,
            "chat_container": obj.get("chat_container"),
            "chat_answer": obj.get("chat_answer"),
            "chat_prompt": obj.get("chat_prompt"),
            "chat_every": obj.get("chat_every") if obj.get("chat_every") is not None else 1,
            "chat_style": obj.get("chat_style") if obj.get("chat_style") is not None else 'card',
            "chat_products": obj.get("chat_products") if obj.get("chat_products") is not None else 3,
            "chat_followups": obj.get("chat_followups") if obj.get("chat_followups") is not None else 0,
            "chat_input": obj.get("chat_input"),
            "chat_send": obj.get("chat_send"),
            "results": obj.get("results") if obj.get("results") is not None else 1,
            "recent": obj.get("recent") if obj.get("recent") is not None else 5,
            "min_chars": obj.get("min_chars") if obj.get("min_chars") is not None else 3,
            "theme": obj.get("theme") if obj.get("theme") is not None else 'auto',
            "label": obj.get("label") if obj.get("label") is not None else 'Ad',
            "layout": obj.get("layout") if obj.get("layout") is not None else 'card',
            "placeholder": obj.get("placeholder") if obj.get("placeholder") is not None else 'Search',
            "submit_url": obj.get("submit_url") if obj.get("submit_url") is not None else '',
            "query_param": obj.get("query_param") if obj.get("query_param") is not None else 'q',
            "ad_position": obj.get("ad_position") if obj.get("ad_position") is not None else 'top',
            "on_open": obj.get("on_open") if obj.get("on_open") is not None else False,
            "recent_pick": obj.get("recent_pick") if obj.get("recent_pick") is not None else 'submit',
            "show_description": obj.get("show_description") if obj.get("show_description") is not None else True,
            "show_url": obj.get("show_url") if obj.get("show_url") is not None else True,
            "blocked_terms": AdspaceCreateSearchSettingsBlockedTerms.from_dict(obj["blocked_terms"]) if obj.get("blocked_terms") is not None else None,
            "runtime": obj.get("runtime")
        })
        return _obj



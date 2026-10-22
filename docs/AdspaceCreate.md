# AdspaceCreate

Adspace create body. The fields below are the common top-level keys every type accepts; the type-specific settings block goes under the body key returned in `settings_block.name` from `GET /api/v1/adspaces/{type}/_schema` (e.g. `banner_settings`, `pop_settings`, `native_settings`, `player_settings`).  Per-type details — including which `*_settings` block to send and the legal fields inside it — live at the runtime `_schema` endpoint, since they vary by tenant config. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**siteid** | **int** | Parent website id from /api/v1/sites. | 
**description** | **str** |  | [optional] 
**ratingid** | **int** |  | [optional] [default to 0]
**main_catid** | **int** |  | [optional] [default to 0]
**catid** | **int** |  | [optional] [default to 0]
**locationid** | **int** |  | [optional] [default to 0]
**adsizeid** | **int** | Banner size id (banner-flavored types only). Also accepted as banner_settings.sizeid. | [optional] [default to 0]
**autoapprove** | **bool** |  | [optional] [default to False]
**isvisible** | **bool** |  | [optional] [default to True]
**sendmails** | **bool** |  | [optional] [default to False]
**useownbanners** | **bool** |  | [optional] [default to False]
**usealtbanner** | **bool** |  | [optional] [default to False]
**usecpmbuys** | **bool** |  | [optional] [default to True]
**allow_iframes** | **bool** |  | [optional] [default to True]
**allow_animation** | **bool** |  | [optional] [default to True]
**skip_ron_if_cpm** | **bool** |  | [optional] [default to False]
**no_promotion** | **bool** |  | [optional] [default to False]
**run_rtb_after_smartzone** | **bool** |  | [optional] [default to False]
**use_pixel_log** | **bool** |  | [optional] [default to False]
**show_about** | **bool** |  | [optional] [default to False]
**hidecopy** | **bool** | Hide the \&quot;Ads by\&quot; copy. Stored as json_settings.hideadsby; &#x60;hideadsby&#x60; is accepted as an alias and wins when both are sent. | [optional] [default to False]
**hideadsby** | **bool** | Alias of hidecopy (the stored name). | [optional] 
**useflatbuys** | **bool** | Accept flat bookings on this zone. | [optional] [default to True]
**parentid** | **int** | Parent ad zone (another live zone of yours) — in-video sub-zones hang under their player zone. 0 &#x3D; top level. | [optional] [default to 0]
**display_type** | **int** | Banner zones: 0 &#x3D; inline, 1 &#x3D; floater (send floater_settings). Forced to 1 for types 17, 19, 20, 22. | [optional] [default to 0]
**new_zoneid** | **int** | Banner zones: forward unfilled traffic to this ad zone id. 0 &#x3D; off. | [optional] [default to 0]
**only_wl_campaigns** | **bool** | Serve only the whitelisted campaigns. Ad Manager tenants only — dropped elsewhere. | [optional] [default to False]
**only_tagged_campaigns** | **bool** | Serve only campaigns in the zone&#39;s campaign groups (&#x60;tags&#x60;). Only where campaign-group targeting is enabled — dropped elsewhere. | [optional] [default to False]
**force_wl_targeting** | **bool** | Apply the whitelisted campaigns&#39; own targeting. Also written by PUT /wl-campaigns. | [optional] [default to False]
**skip_rtb_when_wl** | **bool** | Skip RTB when a whitelisted campaign can fill. Stored in json_settings.options. | [optional] [default to False]
**use_fixed_payouts** | **bool** | Fixed payout instead of revenue share (alias &#x60;fixed_payouts&#x60;). Only where modules.publisher.adzones.options.use_fixed_payouts is on and the tenant is Ad Manager; dropped silently otherwise. | [optional] [default to False]
**fixed_payouts** | **bool** | Alias of use_fixed_payouts (the name the panel sends). | [optional] 
**fixed_payout_data** | **Dict[str, object]** | {type: cpc|cpm, amount (currency units), enddate, amounts: per-country overrides}. Only with use_fixed_payouts. | [optional] 
**rtb_name** | **str** | Name the zone is reported under to RTB partners. | [optional] 
**tags** | **List[int]** | Campaign-group ids (campaign_groups). Empty &#x3D; inherit the site&#39;s groups. | [optional] 
**excl_catids** | **str** | Comma-separated category ids to exclude. | [optional] 
**exclproperties** | **str** |  | [optional] 
**use_subid_list** | **bool** |  | [optional] [default to False]
**subid_list** | **str** | Comma-separated subid allowlist (use_subid_list&#x3D;true required). | [optional] 
**use_domain_list** | **bool** |  | [optional] [default to False]
**domain_list** | **List[str]** |  | [optional] 
**use_costs** | **bool** |  | [optional] [default to False]
**costs_data** | **Dict[str, object]** |  | [optional] 
**use_dynamic_costs** | **bool** |  | [optional] [default to False]
**use_fallback_campaign** | **bool** |  | [optional] [default to False]
**fallback_campaignid** | **int** |  | [optional] [default to 0]
**quality_rank** | **int** |  | [optional] [default to 0]
**banner_settings** | [**AdspaceCreateBannerSettings**](AdspaceCreateBannerSettings.md) |  | [optional] 
**native_settings** | **Dict[str, object]** | Native-flavored zones (nativeads, interstitial_native, creator_widget, search_ads, bot_ads — search_ads and bot_ads read only &#x60;orientation&#x60;). nativeads also takes the infinite content feed: &#x60;infinite&#x60; (boolean; switches GET /api/v1/adspaces/{id}/code to goCtrl&#39;s feed plugin), &#x60;feed_rss&#x60; (your RSS feed: http(s) URL or a path such as /feed/; anything else 422 &#x60;native_settings.feed_rss&#x60;), &#x60;feed_ad_every&#x60; (organic cards before each ad, 0-10, default 2), &#x60;feed_max_pages&#x60; (1-30, default 10), &#x60;feed_title&#x60;, &#x60;feed_label&#x60; (plain text). Ad impressions in the feed are counted when the card is at least half on screen. Full field list: GET /api/v1/adspaces/nativeads/_schema. | [optional] 
**search_settings** | [**AdspaceCreateSearchSettings**](AdspaceCreateSearchSettings.md) |  | [optional] 
**email_settings** | [**AdspaceCreateEmailSettings**](AdspaceCreateEmailSettings.md) |  | [optional] 
**bot_settings** | [**AdspaceCreateBotSettings**](AdspaceCreateBotSettings.md) |  | [optional] 
**screen_settings** | [**AdspaceCreateScreenSettings**](AdspaceCreateScreenSettings.md) |  | [optional] 
**player_settings** | **Dict[str, object]** | Video zones (videoads, interstitial_video, videoslider). videoads also takes rewarded web ads: &#x60;rewarded&#x60; (boolean; GET /api/v1/adspaces/{id}/code then returns goCtrl&#39;s rewarded plugin plus an example button), &#x60;reward_min_seconds&#x60; (5-120, default 10), &#x60;reward_callback&#x60; (your server&#39;s http(s) URL, GET with {uid} {sid} {campaignid} {ts} {token}; anything else 422 &#x60;player_settings.reward_callback&#x60;), &#x60;reward_secret&#x60; (64 hex, generated when rewarded is switched on; the reward token is &#x60;&lt;base64url(payload)&gt;.&lt;hex HMAC-SHA256(reward_secret, payload)&gt;&#x60;, payload &#x60;&lt;sid&gt;.&lt;campaignid&gt;.&lt;uid&gt;.&lt;unix time&gt;&#x60;). CTV / streaming (videoads and audioads): &#x60;pod_size&#x60; (1-6, ads per VAST answer as an ad pod, never the same campaign or advertiser twice; a player can also send &amp;pod&#x3D;N), &#x60;pod_max_seconds&#x60; (0-600, 0 &#x3D; no limit), &#x60;midroll_offsets&#x60; (up to 20 seconds into the stream, array or \&quot;600, 1200\&quot;; out of range 422), &#x60;vmap_no_preroll&#x60;, &#x60;vmap_postroll&#x60;, &#x60;pause_zone_id&#x60; (0 or one of your own banner zones, else 422 &#x60;player_settings.pause_zone_id&#x60;), &#x60;ssai&#x60; (allow server-side ad insertion). The player URLs are in the code answer&#39;s &#x60;ctv&#x60; block. Full field list: GET /api/v1/adspaces/videoads/_schema. | [optional] 
**pop_settings** | **Dict[str, object]** | Pop zones (popads). &#x60;fpa_zoneid&#x60; is the full-page-ad zone served instead of the pop to visitors whose browser is in &#x60;bl_browsers&#x60;: 0 &#x3D; none, otherwise one of YOUR OWN full-page zones (&#x60;fullpageads&#x60;, type 12) — another publisher&#39;s zone, a deleted zone or another type is refused with 422 (&#x60;pop_settings.fpa_zoneid&#x60;). Full field list: GET /api/v1/adspaces/popads/_schema. | [optional] 
**fpa_settings** | **Dict[str, object]** | Full-page ad zones (fullpageads). Shown when the visitor clicks a link, before the link opens. &#x60;link_scope&#x60;: empty &#x3D; any link, &#x60;internal&#x60; &#x3D; vignette (only links to the same site; anything else is refused with 422 &#x60;fpa_settings.link_scope&#x60;). &#x60;start_at&#x60; / &#x60;repeat_at&#x60; count link clicks, &#x60;refreshtime&#x60; caps it to once per N seconds. Full field list: GET /api/v1/adspaces/fullpageads/_schema. | [optional] 
**redirect_settings** | **Dict[str, object]** | Direct-URL zones: redirects (10), legacy types 14/15 and hard links 1-5 (35-39). | [optional] 
**im_settings** | **Dict[str, object]** | In-message popup zones (impopup). | [optional] 
**fixim_banner_settings** | **Dict[str, object]** | Fixed-position banner zones (fixim_banner). | [optional] 
**native_bar_settings** | **Dict[str, object]** | Native bar zones (native_bar). position: top_left | top_right | left_middle | right_middle (the positions the native bar plugin draws); totalitems; topmargin (px, top positions); css. Full field list: GET /api/v1/adspaces/native_bar/_schema. | [optional] 
**native_webpush_settings** | **Dict[str, object]** | Native webpush zones (native_webpush). position: top_left | top_right | center | bottom_left | bottom_right; totalitems; topmargin; css (classic card only); skin: \&quot;\&quot; (classic card) | chat | call | alert — the social bar styles; delay_seconds 0-120 before the first message. Other skins or delays are refused with 422. Full field list: GET /api/v1/adspaces/native_webpush/_schema. | [optional] 
**text_settings** | **Dict[str, object]** | Text-list zones (textads). | [optional] 
**floater_settings** | **Dict[str, object]** | Floater wrapper for interstitial-flavored zones (interstitialads, interstitial_banner, interstitial_native, interstitial_video). &#x60;trigger&#x60;: empty &#x3D; as usual, &#x60;exit&#x60; &#x3D; exit intent (desktop: the mouse leaves the page towards the tab bar; touch: a fast scroll back up after reading at least a screen; never in the first 5 seconds) — banner and native interstitials (17, 20, 21); anything else is refused with 422 &#x60;floater_settings.trigger&#x60;. Floating banners (bannerads with display_type 1, interstitialads) also take &#x60;anchor&#x60; (full-width bottom/top strip with a collapse tab), &#x60;refresh_seconds&#x60; (0, or 30-600 seconds on screen), &#x60;min_width&#x60; / &#x60;max_width&#x60; (screen-width range in px, 0 &#x3D; no limit; e.g. side rails &#x3D; left-middle / right-middle with min_width 1200) — out-of-range values are refused with 422. Full field list: GET /api/v1/adspaces/interstitial_banner/_schema. | [optional] 
**videoslider_settings** | **Dict[str, object]** | Video-slider zones (videoslider). | [optional] 
**invideo_settings** | **Dict[str, object]** | In-video plugin zones (invideo_plugin, type 16): roll slots, the zone each serves, pop-on-close/play. See &#x60;_schema&#x60;. | [optional] 
**dyn_adsettings** | **Dict[str, object]** | Dynamic iframe zones (dyn_iframes). | [optional] 
**inpage_videosettings** | **Dict[str, object]** | In-page video zones (inpage_video). | [optional] 
**carousel_videosettings** | **Dict[str, object]** | Video carousel zones (video_carousel). | [optional] 

## Example

```python
from goadserver.models.adspace_create import AdspaceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreate from a JSON string
adspace_create_instance = AdspaceCreate.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreate.to_json())

# convert the object into a dict
adspace_create_dict = adspace_create_instance.to_dict()
# create an instance of AdspaceCreate from a dict
adspace_create_from_dict = AdspaceCreate.from_dict(adspace_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



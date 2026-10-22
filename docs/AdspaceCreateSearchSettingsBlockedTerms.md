# AdspaceCreateSearchSettingsBlockedTerms

The zone's own blocked terms on top of the built-in list. Send a ';'-separated string or an array; stored as a lowercase ';'-separated string. Whole words and phrases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from goadserver.models.adspace_create_search_settings_blocked_terms import AdspaceCreateSearchSettingsBlockedTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AdspaceCreateSearchSettingsBlockedTerms from a JSON string
adspace_create_search_settings_blocked_terms_instance = AdspaceCreateSearchSettingsBlockedTerms.from_json(json)
# print the JSON string representation of the object
print(AdspaceCreateSearchSettingsBlockedTerms.to_json())

# convert the object into a dict
adspace_create_search_settings_blocked_terms_dict = adspace_create_search_settings_blocked_terms_instance.to_dict()
# create an instance of AdspaceCreateSearchSettingsBlockedTerms from a dict
adspace_create_search_settings_blocked_terms_from_dict = AdspaceCreateSearchSettingsBlockedTerms.from_dict(adspace_create_search_settings_blocked_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



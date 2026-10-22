# SiteSnippetWriteConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **List[str]** | Hosts it applies to; a leading \&quot;.\&quot; &#x3D; domain + subdomains. | [optional] 
**url_patterns** | **List[str]** | Path globs, e.g. /blog/*. | [optional] 

## Example

```python
from goadserver.models.site_snippet_write_conditions import SiteSnippetWriteConditions

# TODO update the JSON string below
json = "{}"
# create an instance of SiteSnippetWriteConditions from a JSON string
site_snippet_write_conditions_instance = SiteSnippetWriteConditions.from_json(json)
# print the JSON string representation of the object
print(SiteSnippetWriteConditions.to_json())

# convert the object into a dict
site_snippet_write_conditions_dict = site_snippet_write_conditions_instance.to_dict()
# create an instance of SiteSnippetWriteConditions from a dict
site_snippet_write_conditions_from_dict = SiteSnippetWriteConditions.from_dict(site_snippet_write_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



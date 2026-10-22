# SiteSnippetWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippet_key** | **str** | Your label for the snippet. | [optional] 
**tag_type** | **str** |  | 
**position** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**attrs** | **Dict[str, str]** | Tag attributes, max 20, each value max 2048 chars. Only the attributes the tag type allows (e.g. meta: name/content/property/http-equiv/charset/itemprop; script: src/type/async/defer/crossorigin/integrity/nonce/id). src/href must be http(s) or protocol-relative. | [optional] 
**content** | **str** | Inline body for script/style; empty for meta/link. | [optional] 
**conditions** | [**SiteSnippetWriteConditions**](SiteSnippetWriteConditions.md) |  | [optional] 
**sortorder** | **int** |  | [optional] 

## Example

```python
from goadserver.models.site_snippet_write import SiteSnippetWrite

# TODO update the JSON string below
json = "{}"
# create an instance of SiteSnippetWrite from a JSON string
site_snippet_write_instance = SiteSnippetWrite.from_json(json)
# print the JSON string representation of the object
print(SiteSnippetWrite.to_json())

# convert the object into a dict
site_snippet_write_dict = site_snippet_write_instance.to_dict()
# create an instance of SiteSnippetWrite from a dict
site_snippet_write_from_dict = SiteSnippetWrite.from_dict(site_snippet_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



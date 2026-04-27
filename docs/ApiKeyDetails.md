# ApiKeyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**ip_allowlist** | **str** | CSV of IPs/CIDRs, empty &#x3D; any | [optional] 
**rate_limit_rpm** | **int** | 0 &#x3D; system default (60) | [optional] 
**expires_at** | **datetime** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**last_used_ip** | **str** |  | [optional] 
**call_count** | **int** |  | [optional] 
**revoked_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from goadserver.models.api_key_details import ApiKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyDetails from a JSON string
api_key_details_instance = ApiKeyDetails.from_json(json)
# print the JSON string representation of the object
print(ApiKeyDetails.to_json())

# convert the object into a dict
api_key_details_dict = api_key_details_instance.to_dict()
# create an instance of ApiKeyDetails from a dict
api_key_details_from_dict = ApiKeyDetails.from_dict(api_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



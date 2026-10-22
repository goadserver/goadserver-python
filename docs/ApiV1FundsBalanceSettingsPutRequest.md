# ApiV1FundsBalanceSettingsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_sendbalancemail** | **int** |  | [optional] 
**ad_minbalance** | **float** | Currency units. | [optional] 

## Example

```python
from goadserver.models.api_v1_funds_balance_settings_put_request import ApiV1FundsBalanceSettingsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FundsBalanceSettingsPutRequest from a JSON string
api_v1_funds_balance_settings_put_request_instance = ApiV1FundsBalanceSettingsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FundsBalanceSettingsPutRequest.to_json())

# convert the object into a dict
api_v1_funds_balance_settings_put_request_dict = api_v1_funds_balance_settings_put_request_instance.to_dict()
# create an instance of ApiV1FundsBalanceSettingsPutRequest from a dict
api_v1_funds_balance_settings_put_request_from_dict = ApiV1FundsBalanceSettingsPutRequest.from_dict(api_v1_funds_balance_settings_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



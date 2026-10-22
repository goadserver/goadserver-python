# ApiV1PublisherFinanceSettingsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payouttype** | **int** |  | [optional] 
**minimum_payout** | **float** | Whole currency units. | [optional] 
**p_currency** | **str** |  | [optional] 
**directpayout** | **int** |  | [optional] 
**payoutmethod** | **int** |  | [optional] 
**paypaladress** | **str** |  | [optional] 
**epaymentsadress** | **str** |  | [optional] 
**paxumadress** | **str** |  | [optional] 
**payoneeradress** | **str** |  | [optional] 
**paymentdata** | **str** | USDT wallet address. | [optional] 
**bankaccountnumber** | **str** |  | [optional] 
**bankaccountname** | **str** |  | [optional] 
**biccode** | **str** |  | [optional] 
**ibancode** | **str** |  | [optional] 
**routingnumber** | **str** |  | [optional] 
**bic_countryid** | **int** |  | [optional] 
**noiban** | **bool** |  | [optional] 
**vatnumber** | **str** |  | [optional] 
**payinfo** | **str** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_settings_put_request import ApiV1PublisherFinanceSettingsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceSettingsPutRequest from a JSON string
api_v1_publisher_finance_settings_put_request_instance = ApiV1PublisherFinanceSettingsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceSettingsPutRequest.to_json())

# convert the object into a dict
api_v1_publisher_finance_settings_put_request_dict = api_v1_publisher_finance_settings_put_request_instance.to_dict()
# create an instance of ApiV1PublisherFinanceSettingsPutRequest from a dict
api_v1_publisher_finance_settings_put_request_from_dict = ApiV1PublisherFinanceSettingsPutRequest.from_dict(api_v1_publisher_finance_settings_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



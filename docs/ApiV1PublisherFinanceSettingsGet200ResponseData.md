# ApiV1PublisherFinanceSettingsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payouttype** | **int** | Payout method id (see payout-types); -1 &#x3D; never set. | [optional] 
**minimum_payout** | **float** | Whole currency units. | [optional] 
**p_currency** | **str** |  | [optional] 
**directpayout** | **int** | 0 &#x3D; no automatic payout, 1 &#x3D; monthly, 2 &#x3D; weekly (needs allowweeklypayments). | [optional] 
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
**noiban** | **int** |  | [optional] 
**routingnumber** | **str** |  | [optional] 
**bic_countryid** | **int** |  | [optional] 
**vatnumber** | **str** |  | [optional] 
**payinfo** | **str** |  | [optional] 
**inv_company** | **str** |  | [optional] 
**inv_adress** | **str** |  | [optional] 
**inv_postalcode** | **str** |  | [optional] 
**inv_city** | **str** |  | [optional] 
**inv_countryid** | **int** |  | [optional] 
**useaccountadress** | **int** |  | [optional] 
**isvalidcompany** | **int** |  | [optional] 
**isvalidbanking** | **int** |  | [optional] 
**last_time_validated** | **str** |  | [optional] 
**allowweeklypayments** | **bool** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_publisher_finance_settings_get200_response_data import ApiV1PublisherFinanceSettingsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PublisherFinanceSettingsGet200ResponseData from a JSON string
api_v1_publisher_finance_settings_get200_response_data_instance = ApiV1PublisherFinanceSettingsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1PublisherFinanceSettingsGet200ResponseData.to_json())

# convert the object into a dict
api_v1_publisher_finance_settings_get200_response_data_dict = api_v1_publisher_finance_settings_get200_response_data_instance.to_dict()
# create an instance of ApiV1PublisherFinanceSettingsGet200ResponseData from a dict
api_v1_publisher_finance_settings_get200_response_data_from_dict = ApiV1PublisherFinanceSettingsGet200ResponseData.from_dict(api_v1_publisher_finance_settings_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AccountBillingAveragesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costs** | **float** | Projected month total in the plan currency (usage, overcharges and modules). | [optional] 
**overcharges** | [**Dict[str, ApiV1AccountBillingAveragesGet200ResponseOverchargesValue]**](ApiV1AccountBillingAveragesGet200ResponseOverchargesValue.md) | Usage above the fixed plan&#39;s included events, keyed by event type. | [optional] 
**modules** | [**List[ApiV1AccountBillingAveragesGet200ResponseModulesInner]**](ApiV1AccountBillingAveragesGet200ResponseModulesInner.md) | Module charges, projected to month end. | [optional] 

## Example

```python
from goadserver.models.api_v1_account_billing_averages_get200_response import ApiV1AccountBillingAveragesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccountBillingAveragesGet200Response from a JSON string
api_v1_account_billing_averages_get200_response_instance = ApiV1AccountBillingAveragesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1AccountBillingAveragesGet200Response.to_json())

# convert the object into a dict
api_v1_account_billing_averages_get200_response_dict = api_v1_account_billing_averages_get200_response_instance.to_dict()
# create an instance of ApiV1AccountBillingAveragesGet200Response from a dict
api_v1_account_billing_averages_get200_response_from_dict = ApiV1AccountBillingAveragesGet200Response.from_dict(api_v1_account_billing_averages_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



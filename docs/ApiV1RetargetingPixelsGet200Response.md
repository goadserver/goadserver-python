# ApiV1RetargetingPixelsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RetargetingPixel]**](RetargetingPixel.md) |  | [optional] 
**total_rows** | **int** |  | [optional] 

## Example

```python
from goadserver.models.api_v1_retargeting_pixels_get200_response import ApiV1RetargetingPixelsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RetargetingPixelsGet200Response from a JSON string
api_v1_retargeting_pixels_get200_response_instance = ApiV1RetargetingPixelsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1RetargetingPixelsGet200Response.to_json())

# convert the object into a dict
api_v1_retargeting_pixels_get200_response_dict = api_v1_retargeting_pixels_get200_response_instance.to_dict()
# create an instance of ApiV1RetargetingPixelsGet200Response from a dict
api_v1_retargeting_pixels_get200_response_from_dict = ApiV1RetargetingPixelsGet200Response.from_dict(api_v1_retargeting_pixels_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



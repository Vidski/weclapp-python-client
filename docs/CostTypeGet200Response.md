# CostTypeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CostType]**](CostType.md) |  | [optional] 

## Example

```python
from openapi_client.models.cost_type_get200_response import CostTypeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CostTypeGet200Response from a JSON string
cost_type_get200_response_instance = CostTypeGet200Response.from_json(json)
# print the JSON string representation of the object
print(CostTypeGet200Response.to_json())

# convert the object into a dict
cost_type_get200_response_dict = cost_type_get200_response_instance.to_dict()
# create an instance of CostTypeGet200Response from a dict
cost_type_get200_response_from_dict = CostTypeGet200Response.from_dict(cost_type_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



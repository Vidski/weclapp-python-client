# PriceCalculationParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**fix_surcharge** | **decimal.Decimal** |  | [optional] 
**from_scale** | **decimal.Decimal** |  | [optional] 
**lower_purchase_price_bound** | **decimal.Decimal** |  | [optional] 
**margin** | **decimal.Decimal** |  | [optional] 
**percent_surcharge** | **decimal.Decimal** |  | [optional] 
**profit** | **decimal.Decimal** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_calculation_parameter import PriceCalculationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PriceCalculationParameter from a JSON string
price_calculation_parameter_instance = PriceCalculationParameter.from_json(json)
# print the JSON string representation of the object
print(PriceCalculationParameter.to_json())

# convert the object into a dict
price_calculation_parameter_dict = price_calculation_parameter_instance.to_dict()
# create an instance of PriceCalculationParameter from a dict
price_calculation_parameter_from_dict = PriceCalculationParameter.from_dict(price_calculation_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



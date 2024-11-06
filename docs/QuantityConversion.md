# QuantityConversion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**conversion_quantity** | **decimal.Decimal** |  | [optional] 
**created_user_id** | **str** |  | [optional] 
**last_edited_user_id** | **str** |  | [optional] 
**opposite_direction** | **bool** |  | [optional] 
**unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quantity_conversion import QuantityConversion

# TODO update the JSON string below
json = "{}"
# create an instance of QuantityConversion from a JSON string
quantity_conversion_instance = QuantityConversion.from_json(json)
# print the JSON string representation of the object
print(QuantityConversion.to_json())

# convert the object into a dict
quantity_conversion_dict = quantity_conversion_instance.to_dict()
# create an instance of QuantityConversion from a dict
quantity_conversion_from_dict = QuantityConversion.from_dict(quantity_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



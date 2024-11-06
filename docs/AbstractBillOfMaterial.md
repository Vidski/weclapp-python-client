# AbstractBillOfMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.abstract_bill_of_material import AbstractBillOfMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractBillOfMaterial from a JSON string
abstract_bill_of_material_instance = AbstractBillOfMaterial.from_json(json)
# print the JSON string representation of the object
print(AbstractBillOfMaterial.to_json())

# convert the object into a dict
abstract_bill_of_material_dict = abstract_bill_of_material_instance.to_dict()
# create an instance of AbstractBillOfMaterial from a dict
abstract_bill_of_material_from_dict = AbstractBillOfMaterial.from_dict(abstract_bill_of_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BillOfMaterial


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
from openapi_client.models.bill_of_material import BillOfMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfMaterial from a JSON string
bill_of_material_instance = BillOfMaterial.from_json(json)
# print the JSON string representation of the object
print(BillOfMaterial.to_json())

# convert the object into a dict
bill_of_material_dict = bill_of_material_instance.to_dict()
# create an instance of BillOfMaterial from a dict
bill_of_material_from_dict = BillOfMaterial.from_dict(bill_of_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SalesOpenItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**amount** | **decimal.Decimal** |  | [optional] 
**amount_discount** | **decimal.Decimal** |  | [optional] 
**amount_open** | **decimal.Decimal** |  | [optional] 
**amount_paid** | **decimal.Decimal** |  | [optional] 
**clearance_date** | **int** |  | [optional] 
**cleared** | **bool** |  | [optional] 
**open_item_number** | **str** |  | [optional] 
**open_item_type** | [**OpenItemType**](OpenItemType.md) |  | [optional] 
**payment_applications** | [**List[PaymentApplication]**](PaymentApplication.md) |  | [optional] 
**sales_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_open_item import SalesOpenItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOpenItem from a JSON string
sales_open_item_instance = SalesOpenItem.from_json(json)
# print the JSON string representation of the object
print(SalesOpenItem.to_json())

# convert the object into a dict
sales_open_item_dict = sales_open_item_instance.to_dict()
# create an instance of SalesOpenItem from a dict
sales_open_item_from_dict = SalesOpenItem.from_dict(sales_open_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



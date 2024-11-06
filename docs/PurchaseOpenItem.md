# PurchaseOpenItem


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
**purchase_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_open_item import PurchaseOpenItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOpenItem from a JSON string
purchase_open_item_instance = PurchaseOpenItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseOpenItem.to_json())

# convert the object into a dict
purchase_open_item_dict = purchase_open_item_instance.to_dict()
# create an instance of PurchaseOpenItem from a dict
purchase_open_item_from_dict = PurchaseOpenItem.from_dict(purchase_open_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



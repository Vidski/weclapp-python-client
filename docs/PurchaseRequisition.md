# PurchaseRequisition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**earliest_required_date** | **int** |  | [optional] 
**internal_shipment_id** | **str** |  | [optional] 
**latest_required_date** | **int** |  | [optional] 
**packaging_unit_to_order_id** | **str** |  | [optional] 
**production_order_id** | **str** |  | [optional] 
**production_order_item_id** | **str** |  | [optional] 
**proposed_date** | **int** |  | [optional] 
**proposed_quantity** | **decimal.Decimal** |  | [optional] 
**purchase_order_id** | **str** |  | [optional] 
**requirement_quantity** | **decimal.Decimal** |  | [optional] 
**requisition_number** | **str** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 
**status** | [**PurchaseRequisitionStatusType**](PurchaseRequisitionStatusType.md) |  | [optional] 
**status_history** | [**List[PurchaseRequisitionStatusHistory]**](PurchaseRequisitionStatusHistory.md) |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_requisition import PurchaseRequisition

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseRequisition from a JSON string
purchase_requisition_instance = PurchaseRequisition.from_json(json)
# print the JSON string representation of the object
print(PurchaseRequisition.to_json())

# convert the object into a dict
purchase_requisition_dict = purchase_requisition_instance.to_dict()
# create an instance of PurchaseRequisition from a dict
purchase_requisition_from_dict = PurchaseRequisition.from_dict(purchase_requisition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PurchaseOrderRequestOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**commercial_language** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disable_email_template** | **bool** |  | [optional] 
**record_comment** | **str** |  | [optional] 
**record_free_text** | **str** |  | [optional] 
**record_opening** | **str** |  | [optional] 
**sent_to_recipient** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**currency_conversion_date** | **int** |  | [optional] 
**currency_conversion_rate** | **decimal.Decimal** |  | [optional] 
**gross_amount** | **decimal.Decimal** |  | [optional] 
**gross_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**header_discount** | **decimal.Decimal** |  | [optional] 
**header_surcharge** | **decimal.Decimal** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**non_standard_tax_id** | **str** |  | [optional] 
**non_standard_tax_name** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**record_currency_id** | **str** |  | [optional] 
**record_currency_name** | **str** |  | [optional] 
**term_of_payment_id** | **str** |  | [optional] 
**term_of_payment_name** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**offer_date** | **int** |  | [optional] 
**planned_delivery_date** | **int** |  | [optional] 
**purchase_order_request_offer_items** | [**List[PurchaseOrderRequestOfferItem]**](PurchaseOrderRequestOfferItem.md) |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**reply_date** | **int** |  | [optional] 
**request_date** | **int** |  | [optional] 
**start_date** | **int** |  | [optional] 
**status** | [**PurchaseOrderRequestSupplierStatusType**](PurchaseOrderRequestSupplierStatusType.md) |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**supplier_number** | **str** |  | [optional] 
**supplier_reference** | **str** |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_offer import PurchaseOrderRequestOffer

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestOffer from a JSON string
purchase_order_request_offer_instance = PurchaseOrderRequestOffer.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestOffer.to_json())

# convert the object into a dict
purchase_order_request_offer_dict = purchase_order_request_offer_instance.to_dict()
# create an instance of PurchaseOrderRequestOffer from a dict
purchase_order_request_offer_from_dict = PurchaseOrderRequestOffer.from_dict(purchase_order_request_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



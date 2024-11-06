# CommissionSalesPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**commission_fix** | **decimal.Decimal** |  | [optional] 
**commission_percentage** | **decimal.Decimal** |  | [optional] 
**commission_type** | [**CommissionType**](CommissionType.md) |  | [optional] 
**sales_partner_supplier_id** | **str** |  | [optional] 
**sales_partner_supplier_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.commission_sales_partner import CommissionSalesPartner

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionSalesPartner from a JSON string
commission_sales_partner_instance = CommissionSalesPartner.from_json(json)
# print the JSON string representation of the object
print(CommissionSalesPartner.to_json())

# convert the object into a dict
commission_sales_partner_dict = commission_sales_partner_instance.to_dict()
# create an instance of CommissionSalesPartner from a dict
commission_sales_partner_from_dict = CommissionSalesPartner.from_dict(commission_sales_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



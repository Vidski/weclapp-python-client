# SupplierGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Supplier]**](Supplier.md) |  | [optional] 

## Example

```python
from openapi_client.models.supplier_get200_response import SupplierGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGet200Response from a JSON string
supplier_get200_response_instance = SupplierGet200Response.from_json(json)
# print the JSON string representation of the object
print(SupplierGet200Response.to_json())

# convert the object into a dict
supplier_get200_response_dict = supplier_get200_response_instance.to_dict()
# create an instance of SupplierGet200Response from a dict
supplier_get200_response_from_dict = SupplierGet200Response.from_dict(supplier_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



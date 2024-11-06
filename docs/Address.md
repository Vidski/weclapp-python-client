# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**company2** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**delivery_address** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**global_location_number** | **str** |  | [optional] 
**invoice_address** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**post_office_box_city** | **str** |  | [optional] 
**post_office_box_number** | **str** |  | [optional] 
**post_office_box_zip_code** | **str** |  | [optional] 
**prime_address** | **bool** |  | [optional] 
**salutation** | [**Salutation**](Salutation.md) |  | [optional] 
**state** | **str** |  | [optional] 
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_id** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



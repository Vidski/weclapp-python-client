# RecordAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**company2** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**global_location_number** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**post_office_box_city** | **str** |  | [optional] 
**post_office_box_number** | **str** |  | [optional] 
**post_office_box_zip_code** | **str** |  | [optional] 
**salutation** | [**Salutation**](Salutation.md) |  | [optional] 
**state** | **str** |  | [optional] 
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_id** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.record_address import RecordAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAddress from a JSON string
record_address_instance = RecordAddress.from_json(json)
# print the JSON string representation of the object
print(RecordAddress.to_json())

# convert the object into a dict
record_address_dict = record_address_instance.to_dict()
# create an instance of RecordAddress from a dict
record_address_from_dict = RecordAddress.from_dict(record_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



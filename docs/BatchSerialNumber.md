# BatchSerialNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**expiration_date** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.batch_serial_number import BatchSerialNumber

# TODO update the JSON string below
json = "{}"
# create an instance of BatchSerialNumber from a JSON string
batch_serial_number_instance = BatchSerialNumber.from_json(json)
# print the JSON string representation of the object
print(BatchSerialNumber.to_json())

# convert the object into a dict
batch_serial_number_dict = batch_serial_number_instance.to_dict()
# create an instance of BatchSerialNumber from a dict
batch_serial_number_from_dict = BatchSerialNumber.from_dict(batch_serial_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



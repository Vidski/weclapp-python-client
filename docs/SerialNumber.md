# SerialNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.serial_number import SerialNumber

# TODO update the JSON string below
json = "{}"
# create an instance of SerialNumber from a JSON string
serial_number_instance = SerialNumber.from_json(json)
# print the JSON string representation of the object
print(SerialNumber.to_json())

# convert the object into a dict
serial_number_dict = serial_number_instance.to_dict()
# create an instance of SerialNumber from a dict
serial_number_from_dict = SerialNumber.from_dict(serial_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



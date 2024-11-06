# SerialNumberGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[SerialNumber]**](SerialNumber.md) |  | [optional] 

## Example

```python
from openapi_client.models.serial_number_get200_response import SerialNumberGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SerialNumberGet200Response from a JSON string
serial_number_get200_response_instance = SerialNumberGet200Response.from_json(json)
# print the JSON string representation of the object
print(SerialNumberGet200Response.to_json())

# convert the object into a dict
serial_number_get200_response_dict = serial_number_get200_response_instance.to_dict()
# create an instance of SerialNumberGet200Response from a dict
serial_number_get200_response_from_dict = SerialNumberGet200Response.from_dict(serial_number_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



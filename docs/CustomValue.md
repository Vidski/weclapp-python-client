# CustomValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.custom_value import CustomValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValue from a JSON string
custom_value_instance = CustomValue.from_json(json)
# print the JSON string representation of the object
print(CustomValue.to_json())

# convert the object into a dict
custom_value_dict = custom_value_instance.to_dict()
# create an instance of CustomValue from a dict
custom_value_from_dict = CustomValue.from_dict(custom_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



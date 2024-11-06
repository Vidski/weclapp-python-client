# Unit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**time_unit_amount** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unit import Unit

# TODO update the JSON string below
json = "{}"
# create an instance of Unit from a JSON string
unit_instance = Unit.from_json(json)
# print the JSON string representation of the object
print(Unit.to_json())

# convert the object into a dict
unit_dict = unit_instance.to_dict()
# create an instance of Unit from a dict
unit_from_dict = Unit.from_dict(unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



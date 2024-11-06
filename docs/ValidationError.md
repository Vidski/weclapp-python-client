# ValidationError

detail information on a validation error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **List[str]** | semantics are dependent on the concrete validation error. | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** | In weclapp, this is the name of the affected parameter or the relative URI to the affected entity. | [optional] 
**location** | **str** |  | [optional] 
**title** | **str** | This will not change from occurrence to occurrence of the problem | 
**type** | [**ValidationErrorType**](ValidationErrorType.md) |  | 

## Example

```python
from openapi_client.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



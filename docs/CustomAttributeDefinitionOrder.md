# CustomAttributeDefinitionOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**override_group_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_order import CustomAttributeDefinitionOrder

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionOrder from a JSON string
custom_attribute_definition_order_instance = CustomAttributeDefinitionOrder.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionOrder.to_json())

# convert the object into a dict
custom_attribute_definition_order_dict = custom_attribute_definition_order_instance.to_dict()
# create an instance of CustomAttributeDefinitionOrder from a dict
custom_attribute_definition_order_from_dict = CustomAttributeDefinitionOrder.from_dict(custom_attribute_definition_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



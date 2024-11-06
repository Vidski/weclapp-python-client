# CustomAttributeDefinitionUpdateOrderPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | 
**order** | [**List[CustomAttributeDefinitionUpdateOrderPostRequestOrderInner]**](CustomAttributeDefinitionUpdateOrderPostRequestOrderInner.md) |  | 

## Example

```python
from openapi_client.models.custom_attribute_definition_update_order_post_request import CustomAttributeDefinitionUpdateOrderPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionUpdateOrderPostRequest from a JSON string
custom_attribute_definition_update_order_post_request_instance = CustomAttributeDefinitionUpdateOrderPostRequest.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionUpdateOrderPostRequest.to_json())

# convert the object into a dict
custom_attribute_definition_update_order_post_request_dict = custom_attribute_definition_update_order_post_request_instance.to_dict()
# create an instance of CustomAttributeDefinitionUpdateOrderPostRequest from a dict
custom_attribute_definition_update_order_post_request_from_dict = CustomAttributeDefinitionUpdateOrderPostRequest.from_dict(custom_attribute_definition_update_order_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



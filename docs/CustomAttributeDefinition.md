# CustomAttributeDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**attribute_description** | **str** |  | [optional] 
**attribute_entity_type** | [**CustomAttributeEntityType**](CustomAttributeEntityType.md) |  | [optional] 
**attribute_key** | **str** |  | [optional] 
**attribute_labels** | [**List[CustomAttributeDefinitionTranslation]**](CustomAttributeDefinitionTranslation.md) |  | [optional] 
**attribute_type** | [**CustomAttributeType**](CustomAttributeType.md) |  | [optional] 
**conditions** | [**CustomAttributeDefinitionConditions**](CustomAttributeDefinitionConditions.md) |  | [optional] 
**default_boolean_value** | **bool** |  | [optional] 
**default_date_value** | **int** |  | [optional] 
**default_number_value** | **decimal.Decimal** |  | [optional] 
**default_string_value** | **str** |  | [optional] 
**entities** | **List[str]** |  | [optional] 
**group_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**legacy_entities** | **List[str]** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**permissions** | [**List[CustomAttributeDefinitionPermission]**](CustomAttributeDefinitionPermission.md) |  | [optional] 
**public_page_types** | [**List[CustomAttributePublicPageType]**](CustomAttributePublicPageType.md) |  | [optional] 
**read_only** | **bool** |  | [optional] 
**selectable_values** | [**List[CustomAttributeDefinitionListValue]**](CustomAttributeDefinitionListValue.md) |  | [optional] 
**show_in_overview** | **bool** |  | [optional] 
**show_on_creation_dialog** | **bool** |  | [optional] 
**system_custom_attribute** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition import CustomAttributeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinition from a JSON string
custom_attribute_definition_instance = CustomAttributeDefinition.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinition.to_json())

# convert the object into a dict
custom_attribute_definition_dict = custom_attribute_definition_instance.to_dict()
# create an instance of CustomAttributeDefinition from a dict
custom_attribute_definition_from_dict = CustomAttributeDefinition.from_dict(custom_attribute_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



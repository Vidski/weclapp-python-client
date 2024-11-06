# LoadingEquipmentIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**loading_equipment_articles** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loading_equipment_identifier import LoadingEquipmentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of LoadingEquipmentIdentifier from a JSON string
loading_equipment_identifier_instance = LoadingEquipmentIdentifier.from_json(json)
# print the JSON string representation of the object
print(LoadingEquipmentIdentifier.to_json())

# convert the object into a dict
loading_equipment_identifier_dict = loading_equipment_identifier_instance.to_dict()
# create an instance of LoadingEquipmentIdentifier from a dict
loading_equipment_identifier_from_dict = LoadingEquipmentIdentifier.from_dict(loading_equipment_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



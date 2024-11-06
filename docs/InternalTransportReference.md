# InternalTransportReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**internal_transport_reference_number** | **str** |  | [optional] 
**loading_equipment_article_id** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**permanent** | **bool** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.internal_transport_reference import InternalTransportReference

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransportReference from a JSON string
internal_transport_reference_instance = InternalTransportReference.from_json(json)
# print the JSON string representation of the object
print(InternalTransportReference.to_json())

# convert the object into a dict
internal_transport_reference_dict = internal_transport_reference_instance.to_dict()
# create an instance of InternalTransportReference from a dict
internal_transport_reference_from_dict = InternalTransportReference.from_dict(internal_transport_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



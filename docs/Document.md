# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_size** | **int** |  | [optional] 
**document_type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**media_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**versions** | [**List[DocumentVersion]**](DocumentVersion.md) |  | [optional] 

## Example

```python
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



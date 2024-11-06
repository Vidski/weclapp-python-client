# DocumentVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**document_size** | **int** |  | [optional] 
**document_version** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.document_version import DocumentVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVersion from a JSON string
document_version_instance = DocumentVersion.from_json(json)
# print the JSON string representation of the object
print(DocumentVersion.to_json())

# convert the object into a dict
document_version_dict = document_version_instance.to_dict()
# create an instance of DocumentVersion from a dict
document_version_from_dict = DocumentVersion.from_dict(document_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



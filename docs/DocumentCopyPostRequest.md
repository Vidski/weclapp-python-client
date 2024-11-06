# DocumentCopyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**entity_name** | **str** |  | 
**source_document_id** | **str** |  | 

## Example

```python
from openapi_client.models.document_copy_post_request import DocumentCopyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyPostRequest from a JSON string
document_copy_post_request_instance = DocumentCopyPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyPostRequest.to_json())

# convert the object into a dict
document_copy_post_request_dict = document_copy_post_request_instance.to_dict()
# create an instance of DocumentCopyPostRequest from a dict
document_copy_post_request_from_dict = DocumentCopyPostRequest.from_dict(document_copy_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



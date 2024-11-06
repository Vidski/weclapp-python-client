# DocumentIdIdCopyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**source_document_id** | **str** |  | 

## Example

```python
from openapi_client.models.document_id_id_copy_post_request import DocumentIdIdCopyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentIdIdCopyPostRequest from a JSON string
document_id_id_copy_post_request_instance = DocumentIdIdCopyPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentIdIdCopyPostRequest.to_json())

# convert the object into a dict
document_id_id_copy_post_request_dict = document_id_id_copy_post_request_instance.to_dict()
# create an instance of DocumentIdIdCopyPostRequest from a dict
document_id_id_copy_post_request_from_dict = DocumentIdIdCopyPostRequest.from_dict(document_id_id_copy_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_user_id** | **str** |  | [optional] 
**author_user_username** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**html_comment** | **str** |  | [optional] 
**last_edit_date** | **int** |  | [optional] 
**parent_comment_id** | **str** |  | [optional] 
**private_comment** | **bool** |  | [optional] 
**public_comment** | **bool** |  | [optional] 
**recipient_users** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**solution** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



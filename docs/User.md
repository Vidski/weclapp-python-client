# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**birth_date** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**licenses** | **List[str]** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**status** | [**BaossUserStatus**](BaossUserStatus.md) |  | [optional] 
**user_roles** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



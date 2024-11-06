# ProjectMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**hourly_cost** | **decimal.Decimal** |  | [optional] 
**team_role** | [**TeamRole**](TeamRole.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_members import ProjectMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembers from a JSON string
project_members_instance = ProjectMembers.from_json(json)
# print the JSON string representation of the object
print(ProjectMembers.to_json())

# convert the object into a dict
project_members_dict = project_members_instance.to_dict()
# create an instance of ProjectMembers from a dict
project_members_from_dict = ProjectMembers.from_dict(project_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CrmEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**call_category_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**event_category_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**opportunity_id** | **str** |  | [optional] 
**party_id** | **str** |  | [optional] 
**start_date** | **int** |  | [optional] 
**subject** | **str** |  | [optional] 
**type** | [**CrmEventType**](CrmEventType.md) |  | [optional] 

## Example

```python
from openapi_client.models.crm_event import CrmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CrmEvent from a JSON string
crm_event_instance = CrmEvent.from_json(json)
# print the JSON string representation of the object
print(CrmEvent.to_json())

# convert the object into a dict
crm_event_dict = crm_event_instance.to_dict()
# create an instance of CrmEvent from a dict
crm_event_from_dict = CrmEvent.from_dict(crm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



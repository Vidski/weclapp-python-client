# CrmEventGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CrmEvent]**](CrmEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.crm_event_get200_response import CrmEventGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CrmEventGet200Response from a JSON string
crm_event_get200_response_instance = CrmEventGet200Response.from_json(json)
# print the JSON string representation of the object
print(CrmEventGet200Response.to_json())

# convert the object into a dict
crm_event_get200_response_dict = crm_event_get200_response_instance.to_dict()
# create an instance of CrmEventGet200Response from a dict
crm_event_get200_response_from_dict = CrmEventGet200Response.from_dict(crm_event_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



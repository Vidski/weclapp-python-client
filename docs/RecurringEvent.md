# RecurringEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**ends_on** | **int** |  | [optional] 
**event_interval** | **int** |  | [optional] 
**event_occurrence_count** | **int** |  | [optional] 
**event_type** | [**RecurringEventType**](RecurringEventType.md) |  | [optional] 
**repeat_on** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.recurring_event import RecurringEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringEvent from a JSON string
recurring_event_instance = RecurringEvent.from_json(json)
# print the JSON string representation of the object
print(RecurringEvent.to_json())

# convert the object into a dict
recurring_event_dict = recurring_event_instance.to_dict()
# create an instance of RecurringEvent from a dict
recurring_event_from_dict = RecurringEvent.from_dict(recurring_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



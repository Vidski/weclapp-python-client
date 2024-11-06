# PartyHabitualExporterLetterOfIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**automatically_suggest_in_invoice** | **bool** |  | [optional] 
**var_date** | **int** |  | [optional] 
**from_supplier** | **bool** |  | [optional] 
**invoices** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**number_declarer** | **str** |  | [optional] 
**number_supplier** | **str** |  | [optional] 
**total_amount** | **decimal.Decimal** |  | [optional] 
**type** | [**PartyHabitualExporterLetterOfIntentType**](PartyHabitualExporterLetterOfIntentType.md) |  | [optional] 

## Example

```python
from openapi_client.models.party_habitual_exporter_letter_of_intent import PartyHabitualExporterLetterOfIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PartyHabitualExporterLetterOfIntent from a JSON string
party_habitual_exporter_letter_of_intent_instance = PartyHabitualExporterLetterOfIntent.from_json(json)
# print the JSON string representation of the object
print(PartyHabitualExporterLetterOfIntent.to_json())

# convert the object into a dict
party_habitual_exporter_letter_of_intent_dict = party_habitual_exporter_letter_of_intent_instance.to_dict()
# create an instance of PartyHabitualExporterLetterOfIntent from a dict
party_habitual_exporter_letter_of_intent_from_dict = PartyHabitualExporterLetterOfIntent.from_dict(party_habitual_exporter_letter_of_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



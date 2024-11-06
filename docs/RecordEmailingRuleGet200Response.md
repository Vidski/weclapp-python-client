# RecordEmailingRuleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[RecordEmailingRule]**](RecordEmailingRule.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_emailing_rule_get200_response import RecordEmailingRuleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RecordEmailingRuleGet200Response from a JSON string
record_emailing_rule_get200_response_instance = RecordEmailingRuleGet200Response.from_json(json)
# print the JSON string representation of the object
print(RecordEmailingRuleGet200Response.to_json())

# convert the object into a dict
record_emailing_rule_get200_response_dict = record_emailing_rule_get200_response_instance.to_dict()
# create an instance of RecordEmailingRuleGet200Response from a dict
record_emailing_rule_get200_response_from_dict = RecordEmailingRuleGet200Response.from_dict(record_emailing_rule_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RecordEmailingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**attach_record_document** | **bool** |  | [optional] 
**bcc_recipients** | **str** |  | [optional] 
**cc_recipients** | **str** |  | [optional] 
**event** | [**RecordEmailingRuleEventType**](RecordEmailingRuleEventType.md) |  | [optional] 
**mail_account_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**other_recipients** | **str** |  | [optional] 
**payment_method_types** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**recipient_type** | [**RecordEmailingRuleRecipientType**](RecordEmailingRuleRecipientType.md) |  | [optional] 
**sales_channels** | [**List[DistributionChannel]**](DistributionChannel.md) |  | [optional] 
**sales_invoice_origin** | [**SalesInvoiceOrigin**](SalesInvoiceOrigin.md) |  | [optional] 
**sales_invoice_types** | [**List[SalesInvoiceType]**](SalesInvoiceType.md) |  | [optional] 
**template_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.record_emailing_rule import RecordEmailingRule

# TODO update the JSON string below
json = "{}"
# create an instance of RecordEmailingRule from a JSON string
record_emailing_rule_instance = RecordEmailingRule.from_json(json)
# print the JSON string representation of the object
print(RecordEmailingRule.to_json())

# convert the object into a dict
record_emailing_rule_dict = record_emailing_rule_instance.to_dict()
# create an instance of RecordEmailingRule from a dict
record_emailing_rule_from_dict = RecordEmailingRule.from_dict(record_emailing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



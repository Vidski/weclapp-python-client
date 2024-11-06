# SepaDirectDebitMandate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 
**cancellation_date** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**first_debit** | **bool** |  | [optional] 
**mandate_reference** | **str** |  | [optional] 
**party_bank_account_id** | **str** |  | [optional] 
**runtime** | [**SepaDirectDebitRuntime**](SepaDirectDebitRuntime.md) |  | [optional] 
**signature_date** | **int** |  | [optional] 
**type** | [**SepaDirectDebitType**](SepaDirectDebitType.md) |  | [optional] 

## Example

```python
from openapi_client.models.sepa_direct_debit_mandate import SepaDirectDebitMandate

# TODO update the JSON string below
json = "{}"
# create an instance of SepaDirectDebitMandate from a JSON string
sepa_direct_debit_mandate_instance = SepaDirectDebitMandate.from_json(json)
# print the JSON string representation of the object
print(SepaDirectDebitMandate.to_json())

# convert the object into a dict
sepa_direct_debit_mandate_dict = sepa_direct_debit_mandate_instance.to_dict()
# create an instance of SepaDirectDebitMandate from a dict
sepa_direct_debit_mandate_from_dict = SepaDirectDebitMandate.from_dict(sepa_direct_debit_mandate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



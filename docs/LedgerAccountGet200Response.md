# LedgerAccountGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[LedgerAccount]**](LedgerAccount.md) |  | [optional] 

## Example

```python
from openapi_client.models.ledger_account_get200_response import LedgerAccountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerAccountGet200Response from a JSON string
ledger_account_get200_response_instance = LedgerAccountGet200Response.from_json(json)
# print the JSON string representation of the object
print(LedgerAccountGet200Response.to_json())

# convert the object into a dict
ledger_account_get200_response_dict = ledger_account_get200_response_instance.to_dict()
# create an instance of LedgerAccountGet200Response from a dict
ledger_account_get200_response_from_dict = LedgerAccountGet200Response.from_dict(ledger_account_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



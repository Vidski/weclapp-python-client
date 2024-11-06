# QuotationStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OfferStatusType**](OfferStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quotation_status_history import QuotationStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of QuotationStatusHistory from a JSON string
quotation_status_history_instance = QuotationStatusHistory.from_json(json)
# print the JSON string representation of the object
print(QuotationStatusHistory.to_json())

# convert the object into a dict
quotation_status_history_dict = quotation_status_history_instance.to_dict()
# create an instance of QuotationStatusHistory from a dict
quotation_status_history_from_dict = QuotationStatusHistory.from_dict(quotation_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



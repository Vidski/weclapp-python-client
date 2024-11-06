# QuotationIdIdAcceptPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_quotation_items** | [**List[QuotationIdIdAcceptPostRequestAcceptQuotationItemsInner]**](QuotationIdIdAcceptPostRequestAcceptQuotationItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.quotation_id_id_accept_post_request import QuotationIdIdAcceptPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuotationIdIdAcceptPostRequest from a JSON string
quotation_id_id_accept_post_request_instance = QuotationIdIdAcceptPostRequest.from_json(json)
# print the JSON string representation of the object
print(QuotationIdIdAcceptPostRequest.to_json())

# convert the object into a dict
quotation_id_id_accept_post_request_dict = quotation_id_id_accept_post_request_instance.to_dict()
# create an instance of QuotationIdIdAcceptPostRequest from a dict
quotation_id_id_accept_post_request_from_dict = QuotationIdIdAcceptPostRequest.from_dict(quotation_id_id_accept_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



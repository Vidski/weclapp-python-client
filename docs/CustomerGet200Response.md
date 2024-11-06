# CustomerGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Customer]**](Customer.md) |  | [optional] 

## Example

```python
from openapi_client.models.customer_get200_response import CustomerGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGet200Response from a JSON string
customer_get200_response_instance = CustomerGet200Response.from_json(json)
# print the JSON string representation of the object
print(CustomerGet200Response.to_json())

# convert the object into a dict
customer_get200_response_dict = customer_get200_response_instance.to_dict()
# create an instance of CustomerGet200Response from a dict
customer_get200_response_from_dict = CustomerGet200Response.from_dict(customer_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



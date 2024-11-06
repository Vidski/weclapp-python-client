# TransportationOrderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TransportationOrder]**](TransportationOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order_get200_response import TransportationOrderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderGet200Response from a JSON string
transportation_order_get200_response_instance = TransportationOrderGet200Response.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderGet200Response.to_json())

# convert the object into a dict
transportation_order_get200_response_dict = transportation_order_get200_response_instance.to_dict()
# create an instance of TransportationOrderGet200Response from a dict
transportation_order_get200_response_from_dict = TransportationOrderGet200Response.from_dict(transportation_order_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



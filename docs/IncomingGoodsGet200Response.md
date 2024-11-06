# IncomingGoodsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[IncomingGoods]**](IncomingGoods.md) |  | [optional] 

## Example

```python
from openapi_client.models.incoming_goods_get200_response import IncomingGoodsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingGoodsGet200Response from a JSON string
incoming_goods_get200_response_instance = IncomingGoodsGet200Response.from_json(json)
# print the JSON string representation of the object
print(IncomingGoodsGet200Response.to_json())

# convert the object into a dict
incoming_goods_get200_response_dict = incoming_goods_get200_response_instance.to_dict()
# create an instance of IncomingGoodsGet200Response from a dict
incoming_goods_get200_response_from_dict = IncomingGoodsGet200Response.from_dict(incoming_goods_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



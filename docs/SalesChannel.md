# SalesChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_channel import SalesChannel

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannel from a JSON string
sales_channel_instance = SalesChannel.from_json(json)
# print the JSON string representation of the object
print(SalesChannel.to_json())

# convert the object into a dict
sales_channel_dict = sales_channel_instance.to_dict()
# create an instance of SalesChannel from a dict
sales_channel_from_dict = SalesChannel.from_dict(sales_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FulfillmentProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**fulfillment_provider_type** | [**FulfillmentProviderType**](FulfillmentProviderType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fulfillment_provider import FulfillmentProvider

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentProvider from a JSON string
fulfillment_provider_instance = FulfillmentProvider.from_json(json)
# print the JSON string representation of the object
print(FulfillmentProvider.to_json())

# convert the object into a dict
fulfillment_provider_dict = fulfillment_provider_instance.to_dict()
# create an instance of FulfillmentProvider from a dict
fulfillment_provider_from_dict = FulfillmentProvider.from_dict(fulfillment_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



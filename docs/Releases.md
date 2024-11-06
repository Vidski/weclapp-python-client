# Releases


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**order_date** | **int** |  | [optional] 
**planned_delivery_date** | **int** |  | [optional] 
**position_number** | **int** |  | [optional] 
**purchase_order_id** | **str** |  | [optional] 
**released_quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.releases import Releases

# TODO update the JSON string below
json = "{}"
# create an instance of Releases from a JSON string
releases_instance = Releases.from_json(json)
# print the JSON string representation of the object
print(Releases.to_json())

# convert the object into a dict
releases_dict = releases_instance.to_dict()
# create an instance of Releases from a dict
releases_from_dict = Releases.from_dict(releases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



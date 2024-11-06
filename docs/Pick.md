# Pick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**confirmed_by_user_id** | **str** |  | [optional] 
**confirmed_date** | **int** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**storage_place_id** | **str** |  | [optional] 
**booked_date** | **int** |  | [optional] 
**order_item_id** | **str** |  | [optional] 
**packaging_unit_base_article_id** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**production_order_item_id** | **str** |  | [optional] 
**shipment_item_id** | **str** |  | [optional] 
**source_internal_transport_reference_id** | **str** |  | [optional] 
**source_storage_place_id** | **str** |  | [optional] 
**transportation_order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pick import Pick

# TODO update the JSON string below
json = "{}"
# create an instance of Pick from a JSON string
pick_instance = Pick.from_json(json)
# print the JSON string representation of the object
print(Pick.to_json())

# convert the object into a dict
pick_dict = pick_instance.to_dict()
# create an instance of Pick from a dict
pick_from_dict = Pick.from_dict(pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



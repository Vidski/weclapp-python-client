# TransportationOrderIdIdPickPickPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_loading_equipment_on_dissolve_of_preferred** | **bool** |  | 
**input_quantity** | **decimal.Decimal** |  | 
**input_serial_numbers** | **List[str]** |  | [optional] 
**pick_id** | **str** |  | 
**preferred_packaging_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order_id_id_pick_pick_post_request import TransportationOrderIdIdPickPickPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderIdIdPickPickPostRequest from a JSON string
transportation_order_id_id_pick_pick_post_request_instance = TransportationOrderIdIdPickPickPostRequest.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderIdIdPickPickPostRequest.to_json())

# convert the object into a dict
transportation_order_id_id_pick_pick_post_request_dict = transportation_order_id_id_pick_pick_post_request_instance.to_dict()
# create an instance of TransportationOrderIdIdPickPickPostRequest from a dict
transportation_order_id_id_pick_pick_post_request_from_dict = TransportationOrderIdIdPickPickPostRequest.from_dict(transportation_order_id_id_pick_pick_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



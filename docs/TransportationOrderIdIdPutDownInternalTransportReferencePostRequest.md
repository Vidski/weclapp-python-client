# TransportationOrderIdIdPutDownInternalTransportReferencePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_loading_equipment_identifier_id** | **str** |  | [optional] 
**target_storage_place_id** | **str** |  | [optional] 
**target_transport_reference_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order_id_id_put_down_internal_transport_reference_post_request import TransportationOrderIdIdPutDownInternalTransportReferencePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderIdIdPutDownInternalTransportReferencePostRequest from a JSON string
transportation_order_id_id_put_down_internal_transport_reference_post_request_instance = TransportationOrderIdIdPutDownInternalTransportReferencePostRequest.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderIdIdPutDownInternalTransportReferencePostRequest.to_json())

# convert the object into a dict
transportation_order_id_id_put_down_internal_transport_reference_post_request_dict = transportation_order_id_id_put_down_internal_transport_reference_post_request_instance.to_dict()
# create an instance of TransportationOrderIdIdPutDownInternalTransportReferencePostRequest from a dict
transportation_order_id_id_put_down_internal_transport_reference_post_request_from_dict = TransportationOrderIdIdPutDownInternalTransportReferencePostRequest.from_dict(transportation_order_id_id_put_down_internal_transport_reference_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



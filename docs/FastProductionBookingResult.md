# FastProductionBookingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**FastProductionBookingResultMessage**](FastProductionBookingResultMessage.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.fast_production_booking_result import FastProductionBookingResult

# TODO update the JSON string below
json = "{}"
# create an instance of FastProductionBookingResult from a JSON string
fast_production_booking_result_instance = FastProductionBookingResult.from_json(json)
# print the JSON string representation of the object
print(FastProductionBookingResult.to_json())

# convert the object into a dict
fast_production_booking_result_dict = fast_production_booking_result_instance.to_dict()
# create an instance of FastProductionBookingResult from a dict
fast_production_booking_result_from_dict = FastProductionBookingResult.from_dict(fast_production_booking_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



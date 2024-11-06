# AbstractBookRecord


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

## Example

```python
from openapi_client.models.abstract_book_record import AbstractBookRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractBookRecord from a JSON string
abstract_book_record_instance = AbstractBookRecord.from_json(json)
# print the JSON string representation of the object
print(AbstractBookRecord.to_json())

# convert the object into a dict
abstract_book_record_dict = abstract_book_record_instance.to_dict()
# create an instance of AbstractBookRecord from a dict
abstract_book_record_from_dict = AbstractBookRecord.from_dict(abstract_book_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



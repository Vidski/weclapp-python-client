# BaseMinimalRecordItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.base_minimal_record_item import BaseMinimalRecordItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseMinimalRecordItem from a JSON string
base_minimal_record_item_instance = BaseMinimalRecordItem.from_json(json)
# print the JSON string representation of the object
print(BaseMinimalRecordItem.to_json())

# convert the object into a dict
base_minimal_record_item_dict = base_minimal_record_item_instance.to_dict()
# create an instance of BaseMinimalRecordItem from a dict
base_minimal_record_item_from_dict = BaseMinimalRecordItem.from_dict(base_minimal_record_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



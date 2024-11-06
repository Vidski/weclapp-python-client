# BaseRecordItem


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
**description** | **str** |  | [optional] 
**description_fixed** | **bool** |  | [optional] 
**manual_quantity** | **bool** |  | [optional] 
**parent_item_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.base_record_item import BaseRecordItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRecordItem from a JSON string
base_record_item_instance = BaseRecordItem.from_json(json)
# print the JSON string representation of the object
print(BaseRecordItem.to_json())

# convert the object into a dict
base_record_item_dict = base_record_item_instance.to_dict()
# create an instance of BaseRecordItem from a dict
base_record_item_from_dict = BaseRecordItem.from_dict(base_record_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



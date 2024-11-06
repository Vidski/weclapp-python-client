# BatchNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**expiration_date** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.batch_number import BatchNumber

# TODO update the JSON string below
json = "{}"
# create an instance of BatchNumber from a JSON string
batch_number_instance = BatchNumber.from_json(json)
# print the JSON string representation of the object
print(BatchNumber.to_json())

# convert the object into a dict
batch_number_dict = batch_number_instance.to_dict()
# create an instance of BatchNumber from a dict
batch_number_from_dict = BatchNumber.from_dict(batch_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



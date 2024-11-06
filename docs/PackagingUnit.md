# PackagingUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** |  | [optional] 
**base_article_quantity** | **int** |  | [optional] 
**packaging_unit_quantity** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.packaging_unit import PackagingUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PackagingUnit from a JSON string
packaging_unit_instance = PackagingUnit.from_json(json)
# print the JSON string representation of the object
print(PackagingUnit.to_json())

# convert the object into a dict
packaging_unit_dict = packaging_unit_instance.to_dict()
# create an instance of PackagingUnit from a dict
packaging_unit_from_dict = PackagingUnit.from_dict(packaging_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



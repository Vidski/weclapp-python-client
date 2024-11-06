# CustomerSpecificArticleAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**customer_article_number** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.customer_specific_article_attributes import CustomerSpecificArticleAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSpecificArticleAttributes from a JSON string
customer_specific_article_attributes_instance = CustomerSpecificArticleAttributes.from_json(json)
# print the JSON string representation of the object
print(CustomerSpecificArticleAttributes.to_json())

# convert the object into a dict
customer_specific_article_attributes_dict = customer_specific_article_attributes_instance.to_dict()
# create an instance of CustomerSpecificArticleAttributes from a dict
customer_specific_article_attributes_from_dict = CustomerSpecificArticleAttributes.from_dict(customer_specific_article_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



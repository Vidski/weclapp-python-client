# CommercialLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.commercial_language import CommercialLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialLanguage from a JSON string
commercial_language_instance = CommercialLanguage.from_json(json)
# print the JSON string representation of the object
print(CommercialLanguage.to_json())

# convert the object into a dict
commercial_language_dict = commercial_language_instance.to_dict()
# create an instance of CommercialLanguage from a dict
commercial_language_from_dict = CommercialLanguage.from_dict(commercial_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



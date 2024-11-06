# WeclappOs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hardware_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**printer_names** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.weclapp_os import WeclappOs

# TODO update the JSON string below
json = "{}"
# create an instance of WeclappOs from a JSON string
weclapp_os_instance = WeclappOs.from_json(json)
# print the JSON string representation of the object
print(WeclappOs.to_json())

# convert the object into a dict
weclapp_os_dict = weclapp_os_instance.to_dict()
# create an instance of WeclappOs from a dict
weclapp_os_from_dict = WeclappOs.from_dict(weclapp_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



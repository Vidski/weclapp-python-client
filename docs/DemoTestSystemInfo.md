# DemoTestSystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_possible** | **bool** |  | [optional] 
**creation_in_progress** | **bool** |  | [optional] 
**demo_instance_url** | **str** |  | [optional] 
**main_instance_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.demo_test_system_info import DemoTestSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DemoTestSystemInfo from a JSON string
demo_test_system_info_instance = DemoTestSystemInfo.from_json(json)
# print the JSON string representation of the object
print(DemoTestSystemInfo.to_json())

# convert the object into a dict
demo_test_system_info_dict = demo_test_system_info_instance.to_dict()
# create an instance of DemoTestSystemInfo from a dict
demo_test_system_info_from_dict = DemoTestSystemInfo.from_dict(demo_test_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



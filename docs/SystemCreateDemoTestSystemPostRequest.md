# SystemCreateDemoTestSystemPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_users** | **bool** |  | [optional] 
**label** | **str** |  | 
**preset** | **str** |  | 

## Example

```python
from openapi_client.models.system_create_demo_test_system_post_request import SystemCreateDemoTestSystemPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemCreateDemoTestSystemPostRequest from a JSON string
system_create_demo_test_system_post_request_instance = SystemCreateDemoTestSystemPostRequest.from_json(json)
# print the JSON string representation of the object
print(SystemCreateDemoTestSystemPostRequest.to_json())

# convert the object into a dict
system_create_demo_test_system_post_request_dict = system_create_demo_test_system_post_request_instance.to_dict()
# create an instance of SystemCreateDemoTestSystemPostRequest from a dict
system_create_demo_test_system_post_request_from_dict = SystemCreateDemoTestSystemPostRequest.from_dict(system_create_demo_test_system_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



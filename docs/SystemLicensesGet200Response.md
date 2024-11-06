# SystemLicensesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[License]**](License.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_licenses_get200_response import SystemLicensesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLicensesGet200Response from a JSON string
system_licenses_get200_response_instance = SystemLicensesGet200Response.from_json(json)
# print the JSON string representation of the object
print(SystemLicensesGet200Response.to_json())

# convert the object into a dict
system_licenses_get200_response_dict = system_licenses_get200_response_instance.to_dict()
# create an instance of SystemLicensesGet200Response from a dict
system_licenses_get200_response_from_dict = SystemLicensesGet200Response.from_dict(system_licenses_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RemotePrintJobGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[RemotePrintJob]**](RemotePrintJob.md) |  | [optional] 

## Example

```python
from openapi_client.models.remote_print_job_get200_response import RemotePrintJobGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemotePrintJobGet200Response from a JSON string
remote_print_job_get200_response_instance = RemotePrintJobGet200Response.from_json(json)
# print the JSON string representation of the object
print(RemotePrintJobGet200Response.to_json())

# convert the object into a dict
remote_print_job_get200_response_dict = remote_print_job_get200_response_instance.to_dict()
# create an instance of RemotePrintJobGet200Response from a dict
remote_print_job_get200_response_from_dict = RemotePrintJobGet200Response.from_dict(remote_print_job_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



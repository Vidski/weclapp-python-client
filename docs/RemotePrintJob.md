# RemotePrintJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**print_status** | [**RemotePrintJobStatus**](RemotePrintJobStatus.md) |  | [optional] 
**printer_name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**weclapp_os_hardware_id** | **str** |  | [optional] 
**weclapp_os_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.remote_print_job import RemotePrintJob

# TODO update the JSON string below
json = "{}"
# create an instance of RemotePrintJob from a JSON string
remote_print_job_instance = RemotePrintJob.from_json(json)
# print the JSON string representation of the object
print(RemotePrintJob.to_json())

# convert the object into a dict
remote_print_job_dict = remote_print_job_instance.to_dict()
# create an instance of RemotePrintJob from a dict
remote_print_job_from_dict = RemotePrintJob.from_dict(remote_print_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



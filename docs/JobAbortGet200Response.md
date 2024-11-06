# JobAbortGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**JobStatus**](JobStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.job_abort_get200_response import JobAbortGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobAbortGet200Response from a JSON string
job_abort_get200_response_instance = JobAbortGet200Response.from_json(json)
# print the JSON string representation of the object
print(JobAbortGet200Response.to_json())

# convert the object into a dict
job_abort_get200_response_dict = job_abort_get200_response_instance.to_dict()
# create an instance of JobAbortGet200Response from a dict
job_abort_get200_response_from_dict = JobAbortGet200Response.from_dict(job_abort_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



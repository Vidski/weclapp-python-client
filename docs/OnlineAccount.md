# OnlineAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**account_type** | [**OnlineAccountType**](OnlineAccountType.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.online_account import OnlineAccount

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineAccount from a JSON string
online_account_instance = OnlineAccount.from_json(json)
# print the JSON string representation of the object
print(OnlineAccount.to_json())

# convert the object into a dict
online_account_dict = online_account_instance.to_dict()
# create an instance of OnlineAccount from a dict
online_account_from_dict = OnlineAccount.from_dict(online_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



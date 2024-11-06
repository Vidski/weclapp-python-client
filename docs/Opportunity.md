# Opportunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**contact_id** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expected_delivery_date** | **int** |  | [optional] 
**expected_signature_date** | **int** |  | [optional] 
**hot_lead** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**next_call_date** | **int** |  | [optional] 
**opportunity_number** | **str** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**responsible_user_username** | **str** |  | [optional] 
**revenue** | **decimal.Decimal** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**sales_probability** | **int** |  | [optional] 
**sales_stage_history** | [**List[SalesStageHistory]**](SalesStageHistory.md) |  | [optional] 
**sales_stage_id** | **str** |  | [optional] 
**sales_stage_name** | **str** |  | [optional] 
**start_date** | **int** |  | [optional] 
**topics** | [**List[Entity]**](Entity.md) |  | [optional] 
**win_loss_description** | **str** |  | [optional] 
**win_loss_reason_id** | **str** |  | [optional] 
**win_loss_reason_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.opportunity import Opportunity

# TODO update the JSON string below
json = "{}"
# create an instance of Opportunity from a JSON string
opportunity_instance = Opportunity.from_json(json)
# print the JSON string representation of the object
print(Opportunity.to_json())

# convert the object into a dict
opportunity_dict = opportunity_instance.to_dict()
# create an instance of Opportunity from a dict
opportunity_from_dict = Opportunity.from_dict(opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



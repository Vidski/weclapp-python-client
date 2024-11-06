# CampaignParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**campaign_number** | **str** |  | [optional] 
**participation** | **bool** |  | [optional] 
**party_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.campaign_participant import CampaignParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignParticipant from a JSON string
campaign_participant_instance = CampaignParticipant.from_json(json)
# print the JSON string representation of the object
print(CampaignParticipant.to_json())

# convert the object into a dict
campaign_participant_dict = campaign_participant_instance.to_dict()
# create an instance of CampaignParticipant from a dict
campaign_participant_from_dict = CampaignParticipant.from_dict(campaign_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



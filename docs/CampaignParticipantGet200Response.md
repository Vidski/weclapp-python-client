# CampaignParticipantGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CampaignParticipant]**](CampaignParticipant.md) |  | [optional] 

## Example

```python
from openapi_client.models.campaign_participant_get200_response import CampaignParticipantGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignParticipantGet200Response from a JSON string
campaign_participant_get200_response_instance = CampaignParticipantGet200Response.from_json(json)
# print the JSON string representation of the object
print(CampaignParticipantGet200Response.to_json())

# convert the object into a dict
campaign_participant_get200_response_dict = campaign_participant_get200_response_instance.to_dict()
# create an instance of CampaignParticipantGet200Response from a dict
campaign_participant_get200_response_from_dict = CampaignParticipantGet200Response.from_dict(campaign_participant_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



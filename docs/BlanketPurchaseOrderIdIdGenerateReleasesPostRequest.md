# BlanketPurchaseOrderIdIdGenerateReleasesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_scheduled_delivery_date** | **int** |  | 
**fix_released_quantity** | **bool** |  | 
**released_quantity** | **decimal.Decimal** |  | [optional] 
**repeat_interval** | **int** |  | 
**repeat_type** | **str** |  | 

## Example

```python
from openapi_client.models.blanket_purchase_order_id_id_generate_releases_post_request import BlanketPurchaseOrderIdIdGenerateReleasesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlanketPurchaseOrderIdIdGenerateReleasesPostRequest from a JSON string
blanket_purchase_order_id_id_generate_releases_post_request_instance = BlanketPurchaseOrderIdIdGenerateReleasesPostRequest.from_json(json)
# print the JSON string representation of the object
print(BlanketPurchaseOrderIdIdGenerateReleasesPostRequest.to_json())

# convert the object into a dict
blanket_purchase_order_id_id_generate_releases_post_request_dict = blanket_purchase_order_id_id_generate_releases_post_request_instance.to_dict()
# create an instance of BlanketPurchaseOrderIdIdGenerateReleasesPostRequest from a dict
blanket_purchase_order_id_id_generate_releases_post_request_from_dict = BlanketPurchaseOrderIdIdGenerateReleasesPostRequest.from_dict(blanket_purchase_order_id_id_generate_releases_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



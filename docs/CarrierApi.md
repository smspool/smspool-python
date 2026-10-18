# smspool_sdk.CarrierApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**carrier_paid_lookup**](CarrierApi.md#carrier_paid_lookup) | **POST** /carrier/paid_lookup | Lookup


# **carrier_paid_lookup**
> object carrier_paid_lookup(phonenumber)

Lookup

This API endpoint is used to perform a paid lookup for a phone number. The request is sent via an HTTP POST method to the following URL: `https://api.smspool.net/carrier/paid_lookup`

``` json
{
  "success": true,
  "phonenumber": "",
  "country": "",
  "carrier": "",
  "carrier_type": "",
  "charge": 0
}

 ```

The `success` field indicates whether the lookup was successful or not. The `phonenumber` field represents the phone number for which the lookup was performed. The `country` field indicates the country associated with the phone number. The `carrier` field provides the name of the carrier associated with the phone number. The `carrier_type` field specifies the type of carrier. The `charge` field represents the cost charged for the lookup operation.

Please note that specific values for `phonenumber`, `country`, `carrier`, and `carrier_type` were not provided in the response, and the `charge` field had a value of 0.

To use this endpoint, send an HTTP POST request to the provided URL with the necessary parameters. The request should include the phone number for which you want to perform the lookup. The response will contain the details of the carrier and associated information.

Make sure to handle any errors that may occur during the lookup process and check the `success` field in the response to determine the outcome of the operation.

### Example

* Bearer Authentication (bearerAuth):

```python
import smspool_sdk
from smspool_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smspool.net
# See configuration.py for a list of all supported configuration parameters.
configuration = smspool_sdk.Configuration(
    host = "https://api.smspool.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = smspool_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with smspool_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smspool_sdk.CarrierApi(api_client)
    phonenumber = 56 # int | 

    try:
        # Lookup
        api_response = api_instance.carrier_paid_lookup(phonenumber)
        print("The response of CarrierApi->carrier_paid_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carrier_paid_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phonenumber** | **int**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Malformed API key |  -  |
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


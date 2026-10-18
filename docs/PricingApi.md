# smspool_sdk.PricingApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_price**](PricingApi.md#request_price) | **POST** /request/price | Retrieve specific price &amp; Success Rate
[**request_pricing**](PricingApi.md#request_pricing) | **POST** /request/pricing | Retrieve all pricing


# **request_price**
> object request_price(country, service, pool=pool, skip_success_rate=skip_success_rate)

Retrieve specific price & Success Rate

### Example


```python
import smspool_sdk
from smspool_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smspool.net
# See configuration.py for a list of all supported configuration parameters.
configuration = smspool_sdk.Configuration(
    host = "https://api.smspool.net"
)


# Enter a context with an instance of the API client
with smspool_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smspool_sdk.PricingApi(api_client)
    country = 'country_example' # str | Country retrieved from ''Country list\\\" endpoint
    service = 'service_example' # str | Service retrieved from ''Service list\\\" endpoint
    pool = 'pool_example' # str | Pool retrieved from ''Pool list\\\" endpoint (optional)
    skip_success_rate = 'skip_success_rate_example' # str |  (optional)

    try:
        # Retrieve specific price & Success Rate
        api_response = api_instance.request_price(country, service, pool=pool, skip_success_rate=skip_success_rate)
        print("The response of PricingApi->request_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->request_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country retrieved from &#39;&#39;Country list\\\&quot; endpoint | 
 **service** | **str**| Service retrieved from &#39;&#39;Service list\\\&quot; endpoint | 
 **pool** | **str**| Pool retrieved from &#39;&#39;Pool list\\\&quot; endpoint | [optional] 
 **skip_success_rate** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_pricing**
> object request_pricing(country=country, service=service, pool=pool, max_price=max_price)

Retrieve all pricing

### Example


```python
import smspool_sdk
from smspool_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smspool.net
# See configuration.py for a list of all supported configuration parameters.
configuration = smspool_sdk.Configuration(
    host = "https://api.smspool.net"
)


# Enter a context with an instance of the API client
with smspool_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smspool_sdk.PricingApi(api_client)
    country = 'country_example' # str | Optional parameter to request services per country (optional)
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint (optional)
    pool = 'pool_example' # str |  (optional)
    max_price = 3.4 # float |  (optional)

    try:
        # Retrieve all pricing
        api_response = api_instance.request_pricing(country=country, service=service, pool=pool, max_price=max_price)
        print("The response of PricingApi->request_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingApi->request_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Optional parameter to request services per country | [optional] 
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | [optional] 
 **pool** | **str**|  | [optional] 
 **max_price** | **float**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


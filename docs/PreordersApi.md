# smspool_sdk.PreordersApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preorder_cancel**](PreordersApi.md#preorder_cancel) | **POST** /preorder/cancel | Cancel
[**preorder_check**](PreordersApi.md#preorder_check) | **POST** /preorder/check | Check
[**preorder_create**](PreordersApi.md#preorder_create) | **POST** /preorder/create | Create
[**preorder_price**](PreordersApi.md#preorder_price) | **POST** /preorder/price | Price
[**preorder_retrieve**](PreordersApi.md#preorder_retrieve) | **POST** /preorder/retrieve | Retrieve


# **preorder_cancel**
> object preorder_cancel(orderid)

Cancel

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
    api_instance = smspool_sdk.PreordersApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Cancel
        api_response = api_instance.preorder_cancel(orderid)
        print("The response of PreordersApi->preorder_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreordersApi->preorder_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderid** | **str**|  | 

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

# **preorder_check**
> object preorder_check(orderid)

Check

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
    api_instance = smspool_sdk.PreordersApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Check
        api_response = api_instance.preorder_check(orderid)
        print("The response of PreordersApi->preorder_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreordersApi->preorder_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderid** | **str**|  | 

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
**401** | Malformed API key |  -  |
**403** | Unknown or revoked API key |  -  |
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preorder_create**
> object preorder_create(service, country, pool, max_price, areacode=areacode)

Create

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
    api_instance = smspool_sdk.PreordersApi(api_client)
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint
    country = 'country_example' # str | Country name or country ID which can be retrieved at the /country/retrieve_all endpoint
    pool = 'pool_example' # str | 
    max_price = 3.4 # float | 
    areacode = 'areacode_example' # str |  (optional)

    try:
        # Create
        api_response = api_instance.preorder_create(service, country, pool, max_price, areacode=areacode)
        print("The response of PreordersApi->preorder_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreordersApi->preorder_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | 
 **country** | **str**| Country name or country ID which can be retrieved at the /country/retrieve_all endpoint | 
 **pool** | **str**|  | 
 **max_price** | **float**|  | 
 **areacode** | **str**|  | [optional] 

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

# **preorder_price**
> object preorder_price(service, country, pool)

Price

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
    api_instance = smspool_sdk.PreordersApi(api_client)
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint
    country = 'country_example' # str | Country name or country ID which can be retrieved at the /country/retrieve_all endpoint
    pool = 'pool_example' # str | 

    try:
        # Price
        api_response = api_instance.preorder_price(service, country, pool)
        print("The response of PreordersApi->preorder_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreordersApi->preorder_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | 
 **country** | **str**| Country name or country ID which can be retrieved at the /country/retrieve_all endpoint | 
 **pool** | **str**|  | 

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
**401** | Malformed API key |  -  |
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preorder_retrieve**
> object preorder_retrieve()

Retrieve

This API endpoint allows you to retrieve preorders from the SMS Pool system. It is an HTTP POST request sent to the URL `https://api.smspool.net/preorder/retrieve`.

### Request Parameters

This endpoint requires the \`key\` parameter which is your API key.

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
    api_instance = smspool_sdk.PreordersApi(api_client)

    try:
        # Retrieve
        api_response = api_instance.preorder_retrieve()
        print("The response of PreordersApi->preorder_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreordersApi->preorder_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Malformed API key |  -  |
**403** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


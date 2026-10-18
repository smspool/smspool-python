# smspool_sdk.SMSApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_sms**](SMSApi.md#purchase_sms) | **POST** /purchase/sms | Order SMS
[**request_active**](SMSApi.md#request_active) | **POST** /request/active | Active orders
[**request_archive**](SMSApi.md#request_archive) | **POST** /request/archive | Archive all orders
[**request_areacodes**](SMSApi.md#request_areacodes) | **POST** /request/areacodes | Request available areacodes
[**request_history**](SMSApi.md#request_history) | **POST** /request/history | Order History
[**sms_activate**](SMSApi.md#sms_activate) | **POST** /sms/activate | Activate SMS
[**sms_all_stock**](SMSApi.md#sms_all_stock) | **POST** /sms/all_stock | One-time stock for all services
[**sms_cancel**](SMSApi.md#sms_cancel) | **POST** /sms/cancel | Cancel SMS
[**sms_cancel_all**](SMSApi.md#sms_cancel_all) | **POST** /sms/cancel_all | Cancel All SMS
[**sms_check**](SMSApi.md#sms_check) | **POST** /sms/check | Check SMS
[**sms_check_resend**](SMSApi.md#sms_check_resend) | **POST** /sms/check_resend | Check Resend
[**sms_clear_cache**](SMSApi.md#sms_clear_cache) | **POST** /sms/clear_cache | Clear SMS Cache
[**sms_missed**](SMSApi.md#sms_missed) | **POST** /sms/missed | Missed SMS
[**sms_reactivate**](SMSApi.md#sms_reactivate) | **POST** /sms/reactivate | Reactivate SMS
[**sms_resend**](SMSApi.md#sms_resend) | **POST** /sms/resend | Resend
[**sms_stock**](SMSApi.md#sms_stock) | **POST** /sms/stock | One-time SMS stock
[**sms_unarchive**](SMSApi.md#sms_unarchive) | **POST** /sms/unarchive | Unarchive order


# **purchase_sms**
> object purchase_sms(service, country=country, pool=pool, max_price=max_price, pricing_option=pricing_option, quantity=quantity, areacode=areacode, exclude=exclude, create_token=create_token, activation_type=activation_type, carrier=carrier, phonenumber=phonenumber, software=software)

Order SMS

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
    api_instance = smspool_sdk.SMSApi(api_client)
    service = 'service_example' # str | The service or number retrieved from the `Service List` endpoint
    country = 'country_example' # str | The country in ISO format or number retrieved from the `Country List` endpoint (optional)
    pool = 'pool_example' # str | The pool or number retrieved from the `Pool List` endpoint (optional) (optional)
    max_price = 3.4 # float | The max price you are willing to pay per number (optional)
    pricing_option = 56 # int | Set to 0 if you'd like the cheapest numbers, set to 1 for highest success rate (optional)
    quantity = 56 # int | Quantity of numbers ordered (optional)
    areacode = 'areacode_example' # str | Areacodes you would like to include or exclude in JSON format (optional)
    exclude = 56 # int | Set exclude to 1 if you would like to exclude all listed area codes. (optional)
    create_token = 56 # int | Optional param; set to 1 if you'd like to create a token link that anyone can access. (optional)
    activation_type = 'activation_type_example' # str | Options: SMS, VOICE, FLASH. SMS will receive regular SMS, VOICE will receive phone calls that mentions the SMS and FLASH is for FLASH calls for verification. (optional)
    carrier = 56 # int | Options: 1 or 2. Pick a carrier (only works for pool Foxtrot US) (optional)
    phonenumber = 56 # int | In case you want to select a specific phone number to order (optional)
    software = 56 # int |  (optional)

    try:
        # Order SMS
        api_response = api_instance.purchase_sms(service, country=country, pool=pool, max_price=max_price, pricing_option=pricing_option, quantity=quantity, areacode=areacode, exclude=exclude, create_token=create_token, activation_type=activation_type, carrier=carrier, phonenumber=phonenumber, software=software)
        print("The response of SMSApi->purchase_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->purchase_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service or number retrieved from the &#x60;Service List&#x60; endpoint | 
 **country** | **str**| The country in ISO format or number retrieved from the &#x60;Country List&#x60; endpoint | [optional] 
 **pool** | **str**| The pool or number retrieved from the &#x60;Pool List&#x60; endpoint (optional) | [optional] 
 **max_price** | **float**| The max price you are willing to pay per number | [optional] 
 **pricing_option** | **int**| Set to 0 if you&#39;d like the cheapest numbers, set to 1 for highest success rate | [optional] 
 **quantity** | **int**| Quantity of numbers ordered | [optional] 
 **areacode** | **str**| Areacodes you would like to include or exclude in JSON format | [optional] 
 **exclude** | **int**| Set exclude to 1 if you would like to exclude all listed area codes. | [optional] 
 **create_token** | **int**| Optional param; set to 1 if you&#39;d like to create a token link that anyone can access. | [optional] 
 **activation_type** | **str**| Options: SMS, VOICE, FLASH. SMS will receive regular SMS, VOICE will receive phone calls that mentions the SMS and FLASH is for FLASH calls for verification. | [optional] 
 **carrier** | **int**| Options: 1 or 2. Pick a carrier (only works for pool Foxtrot US) | [optional] 
 **phonenumber** | **int**| In case you want to select a specific phone number to order | [optional] 
 **software** | **int**|  | [optional] 

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
**422** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_active**
> object request_active()

Active orders

The recommended endpoint to retrieve your current active orders, this will display all your orders at the same time. We recommend using this endpoint to iterate through your active orders to retrieve your SMS messages.

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
    api_instance = smspool_sdk.SMSApi(api_client)

    try:
        # Active orders
        api_response = api_instance.request_active()
        print("The response of SMSApi->request_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->request_active: %s\n" % e)
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
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_archive**
> object request_archive()

Archive all orders

This API endpoint is used to archive a request in the SMS Pool system. The HTTP POST request should be sent to `https://api.smspool.net/request/archive`.

### Request Parameters

The \`key\` parameter is required for this endpoint, this is your API key.

### Response

The response for this API endpoint will have a status code of 200, indicating a successful request. The response body will be in JSON format and will contain the following properties:

- `success` (integer): A flag indicating the success of the request. A value of 0 indicates failure.
- `message` (string): An optional message providing additional information about the request. In this case, the message is empty.
    

Please note that the response may contain additional properties not mentioned here, but they can be ignored for the purpose of this documentation.

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
    api_instance = smspool_sdk.SMSApi(api_client)

    try:
        # Archive all orders
        api_response = api_instance.request_archive()
        print("The response of SMSApi->request_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->request_archive: %s\n" % e)
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
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_areacodes**
> object request_areacodes(service, country, pool)

Request available areacodes

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
    api_instance = smspool_sdk.SMSApi(api_client)
    service = 'service_example' # str | The service or number retrieved from the `Service List` endpoint
    country = 'country_example' # str | The country in ISO format or number retrieved from the `Country List` endpoint
    pool = 'pool_example' # str | The pool or number retrieved from the `Pool List` endpoint (optional)

    try:
        # Request available areacodes
        api_response = api_instance.request_areacodes(service, country, pool)
        print("The response of SMSApi->request_areacodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->request_areacodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service or number retrieved from the &#x60;Service List&#x60; endpoint | 
 **country** | **str**| The country in ISO format or number retrieved from the &#x60;Country List&#x60; endpoint | 
 **pool** | **str**| The pool or number retrieved from the &#x60;Pool List&#x60; endpoint (optional) | 

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
**200** | JSON response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_history**
> object request_history(start=start, length=length, search=search)

Order History

This API endpoint is used to retrieve the history of SMS requests. It is an HTTP POST request that should be made to the following URL: `https://api.smspool.net/request/history`.

The request requires the \`key\` parameter which is your API key.

The response returned by the API is a JSON array. Each element in the array represents a historical SMS request and contains the following properties:

- `cost`: The cost of the SMS request.
- `order_code`: The order code associated with the SMS request.
- `phonenumber`: The phone number to which the SMS was sent.
- `code`: The code associated with the SMS request.
- `full_code`: The full code associated with the SMS request.
- `short_name`: The short name associated with the SMS request.
- `service`: The service associated with the SMS request.
- `status`: The status of the SMS request.
- `pool`: The pool associated with the SMS request.
- `timestamp`: The timestamp of the SMS request.
- `completed_on`: The completion date of the SMS request.
- `expiry`: The expiry time of the SMS request.
- `time_left`: The time left for the SMS request to expire.
    

Please note that the values for the properties are not provided in the response example, so they may be empty or null.

The last execution of this API request returned a response with a status code of 200, indicating a successful execution. The response body contained an array of SMS request history objects.

Please refer to the API documentation for more details on how to use this endpoint and interpret the response.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    start = 56 # int | Which row you'd like to start from (optional)
    length = 56 # int | Max length of all rows (optional)
    search = 'search_example' # str | Search query for phone number, order_code, service or country (optional)

    try:
        # Order History
        api_response = api_instance.request_history(start=start, length=length, search=search)
        print("The response of SMSApi->request_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->request_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Which row you&#39;d like to start from | [optional] 
 **length** | **int**| Max length of all rows | [optional] 
 **search** | **str**| Search query for phone number, order_code, service or country | [optional] 

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
**403** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_activate**
> object sms_activate(orderid)

Activate SMS

This endpoint will forcefully activate an SMS to set it available for future resends, please keep in mind that these orders are NOT eligible for a refund after activating them.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Activate SMS
        api_response = api_instance.sms_activate(orderid)
        print("The response of SMSApi->sms_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_activate: %s\n" % e)
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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_all_stock**
> object sms_all_stock(country=country, service=service, pool=pool)

One-time stock for all services

This API endpoint is used to retrieve one-time SMS stock in the SMSPool system. The HTTP POST request should be sent to `https://api.smspool.net/sms/stock`.

### Request Parameters

The \`key\` parameter is required for this endpoint, this is your API key.

### Response

The response for this API endpoint will have a status code of 200, indicating a successful request. The response body will be in JSON format and will contain the following properties:

- `success` (integer): A flag indicating the success of the request. A value of 0 indicates failure.
    
- `message` (string): An optional message providing additional information about the request. In this case, the message is empty.
    

Please note that the response may contain additional properties not mentioned here, but they can be ignored for the purpose of this documentation.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    country = 'country_example' # str | Country retrieved from ''Country list\\\" endpoint (optional) (optional)
    service = 'service_example' # str | Service retrieved from ''Service list\\\" endpoint (optional) (optional)
    pool = 'pool_example' # str | Pool retrieved from ''Pool list\\\" endpoint (optional) (optional)

    try:
        # One-time stock for all services
        api_response = api_instance.sms_all_stock(country=country, service=service, pool=pool)
        print("The response of SMSApi->sms_all_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_all_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country retrieved from &#39;&#39;Country list\\\&quot; endpoint (optional) | [optional] 
 **service** | **str**| Service retrieved from &#39;&#39;Service list\\\&quot; endpoint (optional) | [optional] 
 **pool** | **str**| Pool retrieved from &#39;&#39;Pool list\\\&quot; endpoint (optional) | [optional] 

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

# **sms_cancel**
> object sms_cancel(orderid=orderid, orderids=orderids, expiry=expiry, ban=ban)

Cancel SMS

# Cancel your SMS order

## Responses

| **Success** | {"success":1} |
| **Fail** | {"success":0} |

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str |  (optional)
    orderids = 'orderids_example' # str |  (optional)
    expiry = 56 # int |  (optional)
    ban = 56 # int |  (optional)

    try:
        # Cancel SMS
        api_response = api_instance.sms_cancel(orderid=orderid, orderids=orderids, expiry=expiry, ban=ban)
        print("The response of SMSApi->sms_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderid** | **str**|  | [optional] 
 **orderids** | **str**|  | [optional] 
 **expiry** | **int**|  | [optional] 
 **ban** | **int**|  | [optional] 

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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_cancel_all**
> object sms_cancel_all()

Cancel All SMS

# Cancel your SMS order

## Responses

| **Success** | {"success":1} |
| **Fail** | {"success":0} |

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
    api_instance = smspool_sdk.SMSApi(api_client)

    try:
        # Cancel All SMS
        api_response = api_instance.sms_cancel_all()
        print("The response of SMSApi->sms_cancel_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_cancel_all: %s\n" % e)
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
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_check**
> object sms_check(orderid)

Check SMS

You may run into ratelimits while using this endpoint for high rate requests, we recommend using /request/active instead as it will list all your orders at the same time.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Check SMS
        api_response = api_instance.sms_check(orderid)
        print("The response of SMSApi->sms_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_check: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_check_resend**
> object sms_check_resend(orderid)

Check Resend

Check if the order can be resent or not.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Check Resend
        api_response = api_instance.sms_check_resend(orderid)
        print("The response of SMSApi->sms_check_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_check_resend: %s\n" % e)
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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_clear_cache**
> object sms_clear_cache()

Clear SMS Cache

# Clear your previous SMS cache to allocate previous numbers again

## Responses

| **Success** | {"success":1} |  
| **Fail** | {"success":0} |

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
    api_instance = smspool_sdk.SMSApi(api_client)

    try:
        # Clear SMS Cache
        api_response = api_instance.sms_clear_cache()
        print("The response of SMSApi->sms_clear_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_clear_cache: %s\n" % e)
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
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_missed**
> object sms_missed(phonenumber=phonenumber, limit=limit)

Missed SMS

Some messages arrive on a number from your one-time orders but cannot finish the order, such as Ticketmaster and Seated codes or Hark reward payouts. This returns those messages, the same ones the Missed SMS tool on the website shows. Only numbers from pool Foxtrot are covered.

The newest messages come first. `url`, `code` and `email` hold the first link, code and email address found in the message, or an empty string.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    phonenumber = 56 # int | Only return messages for this number, including the country code. Leave it out for all your numbers. (optional)
    limit = 56 # int | Maximum number of messages. Defaults to 100, at most 500. (optional)

    try:
        # Missed SMS
        api_response = api_instance.sms_missed(phonenumber=phonenumber, limit=limit)
        print("The response of SMSApi->sms_missed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_missed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phonenumber** | **int**| Only return messages for this number, including the country code. Leave it out for all your numbers. | [optional] 
 **limit** | **int**| Maximum number of messages. Defaults to 100, at most 500. | [optional] 

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

# **sms_reactivate**
> object sms_reactivate(orderid)

Reactivate SMS

This endpoint will reactivate an order, please keep in mind that these orders are NOT eligible for a refund after activating them.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Reactivate SMS
        api_response = api_instance.sms_reactivate(orderid)
        print("The response of SMSApi->sms_reactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_reactivate: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_resend**
> object sms_resend(orderid)

Resend

# Resend

Resend the order. Keep in mind that some pools will have a charge per resend. You can see whether the resend will have a charge using the "Check Resend" endpoint

## Responses

| **Success** | {"success":1,"message":"Number has been requested again","resend":0} |  
| **Fail** | {"success":0,"message":"Phonenumber could not be requested again, try later again.","resend":0} |

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | 

    try:
        # Resend
        api_response = api_instance.sms_resend(orderid)
        print("The response of SMSApi->sms_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_resend: %s\n" % e)
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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_stock**
> object sms_stock(country, service, pool=pool, include_price=include_price)

One-time SMS stock

This API endpoint is used to retrieve one-time SMS stock in the SMSPool system. The HTTP POST request should be sent to `https://api.smspool.net/sms/stock`.

### Request Parameters

The \`key\` parameter is required for this endpoint, this is your API key.

### Response

The response for this API endpoint will have a status code of 200, indicating a successful request. The response body will be in JSON format and will contain the following properties:

- `success` (integer): A flag indicating the success of the request. A value of 0 indicates failure.
    
- `message` (string): An optional message providing additional information about the request. In this case, the message is empty.
    

Please note that the response may contain additional properties not mentioned here, but they can be ignored for the purpose of this documentation.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    country = 'country_example' # str | Country retrieved from ''Country list\\\" endpoint
    service = 'service_example' # str | Service retrieved from ''Service list\\\" endpoint
    pool = 'pool_example' # str | Pool retrieved from ''Pool list\\\" endpoint (optional)
    include_price = 56 # int |  (optional)

    try:
        # One-time SMS stock
        api_response = api_instance.sms_stock(country, service, pool=pool, include_price=include_price)
        print("The response of SMSApi->sms_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country retrieved from &#39;&#39;Country list\\\&quot; endpoint | 
 **service** | **str**| Service retrieved from &#39;&#39;Service list\\\&quot; endpoint | 
 **pool** | **str**| Pool retrieved from &#39;&#39;Pool list\\\&quot; endpoint | [optional] 
 **include_price** | **int**|  | [optional] 

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

# **sms_unarchive**
> object sms_unarchive(orderid)

Unarchive order

Move an archived order back to your active orders, so it shows up in **Active orders** and on your dashboard again. Use **Archive all orders** to archive them.

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
    api_instance = smspool_sdk.SMSApi(api_client)
    orderid = 'orderid_example' # str | The order ID retrieved from /purchase/sms

    try:
        # Unarchive order
        api_response = api_instance.sms_unarchive(orderid)
        print("The response of SMSApi->sms_unarchive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->sms_unarchive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderid** | **str**| The order ID retrieved from /purchase/sms | 

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


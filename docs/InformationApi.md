# smspool_sdk.InformationApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**country_retrieve_all**](InformationApi.md#country_retrieve_all) | **GET** /country/retrieve_all | Country list
[**pool_retrieve_all**](InformationApi.md#pool_retrieve_all) | **POST** /pool/retrieve_all | Pool list
[**pool_retrieve_valid**](InformationApi.md#pool_retrieve_valid) | **POST** /pool/retrieve_valid | Suggested Pools
[**request_balance**](InformationApi.md#request_balance) | **POST** /request/balance | Balance
[**request_history_search**](InformationApi.md#request_history_search) | **POST** /request/history_search | History search
[**request_success_rate**](InformationApi.md#request_success_rate) | **POST** /request/success_rate | Retrieve country success rates per service
[**request_suggested_countries**](InformationApi.md#request_suggested_countries) | **POST** /request/suggested_countries | Suggested Countries
[**service_retrieve_all**](InformationApi.md#service_retrieve_all) | **GET** /service/retrieve_all | Service list


# **country_retrieve_all**
> object country_retrieve_all(show_all=show_all)

Country list

This API endpoint is used to retrieve the full country list for SMSPool requests. It sends an HTTP GET request to the URL `https://api.smspool.net/country/retrieve_all`.

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
    api_instance = smspool_sdk.InformationApi(api_client)
    show_all = 'show_all_example' # str |  (optional)

    try:
        # Country list
        api_response = api_instance.country_retrieve_all(show_all=show_all)
        print("The response of InformationApi->country_retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->country_retrieve_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pool_retrieve_all**
> object pool_retrieve_all()

Pool list

This API endpoint is used to retrieve a list of our active pools for SMSPool requests. It sends an HTTP POST request to the URL `https://api.smspool.net/pool/retrieve_all`.

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
    api_instance = smspool_sdk.InformationApi(api_client)

    try:
        # Pool list
        api_response = api_instance.pool_retrieve_all()
        print("The response of InformationApi->pool_retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->pool_retrieve_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pool_retrieve_valid**
> object pool_retrieve_valid(service, country, web=web, include_stock=include_stock)

Suggested Pools

This API endpoint is used to retrieve suggested pools for SMSPool requests. It sends an HTTP POST request to the URL `https://api.smspool.net/pool/retrieve_valid`.

Please use either the service ID, or the service name as service param.

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
    api_instance = smspool_sdk.InformationApi(api_client)
    service = 'service_example' # str | Service retrieved from ''Service list\\\" endpoint
    country = 'country_example' # str | Country retrieved from ''Country list\\\" endpoint
    web = 'web_example' # str | Return array format (optional)
    include_stock = 'include_stock_example' # str |  (optional)

    try:
        # Suggested Pools
        api_response = api_instance.pool_retrieve_valid(service, country, web=web, include_stock=include_stock)
        print("The response of InformationApi->pool_retrieve_valid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->pool_retrieve_valid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Service retrieved from &#39;&#39;Service list\\\&quot; endpoint | 
 **country** | **str**| Country retrieved from &#39;&#39;Country list\\\&quot; endpoint | 
 **web** | **str**| Return array format | [optional] 
 **include_stock** | **str**|  | [optional] 

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

# **request_balance**
> object request_balance()

Balance

This HTTP POST request is used to retrieve the balance for a specific SMSPool. The request is sent to the URL `https://api.smspool.net/request/balance`.

### Request Parameters

This request require the \`key\` param which is your API key

### Response

The response to this request will have a status code of 200 if the request is successful. The response body will be in JSON format and will include a `balance` field. However, the last execution of this request returned an empty string for the `balance` field.

Please note that the actual value of the `balance` field may vary depending on the user and its configuration.

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
    api_instance = smspool_sdk.InformationApi(api_client)

    try:
        # Balance
        api_response = api_instance.request_balance()
        print("The response of InformationApi->request_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->request_balance: %s\n" % e)
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
**400** | Error |  -  |
**401** | Malformed API key |  -  |
**403** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_history_search**
> object request_history_search(search, cursor=cursor, limit=limit)

History search

_Not documented yet: the parameters below come straight from the code._

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
    api_instance = smspool_sdk.InformationApi(api_client)
    search = 'search_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # History search
        api_response = api_instance.request_history_search(search, cursor=cursor, limit=limit)
        print("The response of InformationApi->request_history_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->request_history_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

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
**200** | JSON response |  -  |
**401** | Malformed API key |  -  |
**403** | Unknown or revoked API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_success_rate**
> object request_success_rate(service, country=country)

Retrieve country success rates per service

This API endpoint is used to retrieve success per country for SMSPool requests. It sends an HTTP POST request to the URL `https://api.smspool.net/request/success_rate`.

Please use either the service ID, or the service name as service param.

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
    api_instance = smspool_sdk.InformationApi(api_client)
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint
    country = 'country_example' # str | Country name or country ID which can be retrieved at the /country/retrieve_all endpoint (optional)

    try:
        # Retrieve country success rates per service
        api_response = api_instance.request_success_rate(service, country=country)
        print("The response of InformationApi->request_success_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->request_success_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | 
 **country** | **str**| Country name or country ID which can be retrieved at the /country/retrieve_all endpoint | [optional] 

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

# **request_suggested_countries**
> object request_suggested_countries(service)

Suggested Countries

This API endpoint is used to retrieve suggested countries for SMS pool requests. It sends an HTTP POST request to the URL `https://api.smspool.net/request/suggested_countries`.

Please use either the service ID, or the service name as service param.

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
    api_instance = smspool_sdk.InformationApi(api_client)
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint

    try:
        # Suggested Countries
        api_response = api_instance.request_suggested_countries(service)
        print("The response of InformationApi->request_suggested_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->request_suggested_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | 

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

# **service_retrieve_all**
> object service_retrieve_all(country=country)

Service list

This API endpoint is used to retrieve the full service list for SMSPool requests. It sends an HTTP GET request to the URL `https://api.smspool.net/service/retrieve_all`.

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
    api_instance = smspool_sdk.InformationApi(api_client)
    country = '1' # str |  (optional)

    try:
        # Service list
        api_response = api_instance.service_retrieve_all(country=country)
        print("The response of InformationApi->service_retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->service_retrieve_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


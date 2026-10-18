# smspool_sdk.ESIMsApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esim_delete**](ESIMsApi.md#esim_delete) | **POST** /esim/delete | Delete eSIM
[**esim_history**](ESIMsApi.md#esim_history) | **POST** /esim/history | View eSIM history
[**esim_label_update**](ESIMsApi.md#esim_label_update) | **POST** /esim/label/update | Update eSIM label
[**esim_plans**](ESIMsApi.md#esim_plans) | **POST** /esim/plans | View eSIM plans per country
[**esim_pricing**](ESIMsApi.md#esim_pricing) | **POST** /esim/pricing | View eSIM countries
[**esim_profile**](ESIMsApi.md#esim_profile) | **POST** /esim/profile | View eSIM profile
[**esim_purchase**](ESIMsApi.md#esim_purchase) | **POST** /esim/purchase | Purchase eSIM
[**esim_topup**](ESIMsApi.md#esim_topup) | **POST** /esim/topup | Top up eSIM
[**esim_topup_plans**](ESIMsApi.md#esim_topup_plans) | **POST** /esim/topup_plans | Top Up Plans


# **esim_delete**
> object esim_delete(transaction_id)

Delete eSIM

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    transaction_id = 'transaction_id_example' # str | transactionId retrieved from /esim/purchase

    try:
        # Delete eSIM
        api_response = api_instance.esim_delete(transaction_id)
        print("The response of ESIMsApi->esim_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transactionId retrieved from /esim/purchase | 

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

# **esim_history**
> object esim_history(start=start, length=length, search=search)

View eSIM history

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    start = 56 # int | Start page (optional)
    length = 56 # int | Amount of rows per page (optional)
    search = 'search_example' # str | Alphanumeric search (optional)

    try:
        # View eSIM history
        api_response = api_instance.esim_history(start=start, length=length, search=search)
        print("The response of ESIMsApi->esim_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start page | [optional] 
 **length** | **int**| Amount of rows per page | [optional] 
 **search** | **str**| Alphanumeric search | [optional] 

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

# **esim_label_update**
> object esim_label_update(transaction_id, label=label)

Update eSIM label

Set or clear the label of one of your eSIMs. The label is returned as `label` by **View eSIM history**, so you can use it to tell your eSIMs apart.

A label can be up to 30 characters long and may only contain letters, numbers and spaces. Leave `label` out, or send it empty, to remove the label.

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    transaction_id = 'transaction_id_example' # str | transactionId retrieved from /esim/purchase
    label = 'label_example' # str | The new label: letters, numbers and spaces, at most 30 characters. Empty or left out removes the label. (optional)

    try:
        # Update eSIM label
        api_response = api_instance.esim_label_update(transaction_id, label=label)
        print("The response of ESIMsApi->esim_label_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_label_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transactionId retrieved from /esim/purchase | 
 **label** | **str**| The new label: letters, numbers and spaces, at most 30 characters. Empty or left out removes the label. | [optional] 

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

# **esim_plans**
> object esim_plans(country)

View eSIM plans per country

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    country = 'country_example' # str | ISO 3166 country code

    try:
        # View eSIM plans per country
        api_response = api_instance.esim_plans(country)
        print("The response of ESIMsApi->esim_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166 country code | 

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

# **esim_pricing**
> object esim_pricing(start=start, length=length, search=search)

View eSIM countries

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    start = 56 # int | Start page (optional)
    length = 56 # int | Amount of rows per page (optional)
    search = 'search_example' # str | Search query for country (optional)

    try:
        # View eSIM countries
        api_response = api_instance.esim_pricing(start=start, length=length, search=search)
        print("The response of ESIMsApi->esim_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start page | [optional] 
 **length** | **int**| Amount of rows per page | [optional] 
 **search** | **str**| Search query for country | [optional] 

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

# **esim_profile**
> object esim_profile(transaction_id=transaction_id)

View eSIM profile

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    transaction_id = 'transaction_id_example' # str | transactionId retrieved from /esim/purchase (optional)

    try:
        # View eSIM profile
        api_response = api_instance.esim_profile(transaction_id=transaction_id)
        print("The response of ESIMsApi->esim_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transactionId retrieved from /esim/purchase | [optional] 

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

# **esim_purchase**
> object esim_purchase(plan)

Purchase eSIM

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    plan = 56 # int | The plan ID which is obtained from /esim/pricing

    try:
        # Purchase eSIM
        api_response = api_instance.esim_purchase(plan)
        print("The response of ESIMsApi->esim_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **int**| The plan ID which is obtained from /esim/pricing | 

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

# **esim_topup**
> object esim_topup(transaction_id, plan)

Top up eSIM

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    transaction_id = 'transaction_id_example' # str | Transaction ID retrieved from eSIM history
    plan = 56 # int | Topup plan retrieved from \\\"Top Up Plans\\\"

    try:
        # Top up eSIM
        api_response = api_instance.esim_topup(transaction_id, plan)
        print("The response of ESIMsApi->esim_topup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_topup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| Transaction ID retrieved from eSIM history | 
 **plan** | **int**| Topup plan retrieved from \\\&quot;Top Up Plans\\\&quot; | 

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

# **esim_topup_plans**
> object esim_topup_plans(plan)

Top Up Plans

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
    api_instance = smspool_sdk.ESIMsApi(api_client)
    plan = 56 # int | `plan` retrieved from eSIM history

    try:
        # Top Up Plans
        api_response = api_instance.esim_topup_plans(plan)
        print("The response of ESIMsApi->esim_topup_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESIMsApi->esim_topup_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **int**| &#x60;plan&#x60; retrieved from eSIM history | 

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


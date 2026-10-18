# smspool_sdk.BusinessApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**business_create**](BusinessApi.md#business_create) | **POST** /business/create | Register user
[**business_user_history**](BusinessApi.md#business_user_history) | **POST** /business/user/history | History
[**business_user_update**](BusinessApi.md#business_user_update) | **POST** /business/user/update | Update
[**business_users**](BusinessApi.md#business_users) | **GET** /business/users | Retrieve users


# **business_create**
> object business_create(username, password, daily_spend_limit=daily_spend_limit)

Register user

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
    api_instance = smspool_sdk.BusinessApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    daily_spend_limit = 3.4 # float | Optional daily spend cap in USD. Omit for no limit. (optional)

    try:
        # Register user
        api_response = api_instance.business_create(username, password, daily_spend_limit=daily_spend_limit)
        print("The response of BusinessApi->business_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->business_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **daily_spend_limit** | **float**| Optional daily spend cap in USD. Omit for no limit. | [optional] 

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

# **business_user_history**
> object business_user_history(id)

History

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
    api_instance = smspool_sdk.BusinessApi(api_client)
    id = 56 # int | User ID retrievd from `Retrieve users` endpoint

    try:
        # History
        api_response = api_instance.business_user_history(id)
        print("The response of BusinessApi->business_user_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->business_user_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID retrievd from &#x60;Retrieve users&#x60; endpoint | 

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

# **business_user_update**
> object business_user_update(id, password=password, balance=balance, active=active, daily_spend_limit=daily_spend_limit)

Update

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
    api_instance = smspool_sdk.BusinessApi(api_client)
    id = 56 # int | User ID retrievd from `Retrieve users` endpoint
    password = 'password_example' # str | Leave empty if you do not wish to update the password (optional)
    balance = 3.4 # float | Leave empty if you do not wish to update the balance, sets the balance by the requested value (optional)
    active = 56 # int | Disable/enable user account (optional) (optional)
    daily_spend_limit = 3.4 # float | Daily spend cap in USD. Leave empty to leave unchanged, send -1 to remove the cap, 0 to block all spending. (optional)

    try:
        # Update
        api_response = api_instance.business_user_update(id, password=password, balance=balance, active=active, daily_spend_limit=daily_spend_limit)
        print("The response of BusinessApi->business_user_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->business_user_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID retrievd from &#x60;Retrieve users&#x60; endpoint | 
 **password** | **str**| Leave empty if you do not wish to update the password | [optional] 
 **balance** | **float**| Leave empty if you do not wish to update the balance, sets the balance by the requested value | [optional] 
 **active** | **int**| Disable/enable user account (optional) | [optional] 
 **daily_spend_limit** | **float**| Daily spend cap in USD. Leave empty to leave unchanged, send -1 to remove the cap, 0 to block all spending. | [optional] 

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

# **business_users**
> object business_users()

Retrieve users

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
    api_instance = smspool_sdk.BusinessApi(api_client)

    try:
        # Retrieve users
        api_response = api_instance.business_users()
        print("The response of BusinessApi->business_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessApi->business_users: %s\n" % e)
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


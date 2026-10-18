# smspool_sdk.RentalApi

All URIs are relative to *https://api.smspool.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_rental**](RentalApi.md#purchase_rental) | **POST** /purchase/rental | Order Rental
[**rental_auto_extend**](RentalApi.md#rental_auto_extend) | **POST** /rental/auto_extend | Enable Auto Extend Rental
[**rental_extend**](RentalApi.md#rental_extend) | **POST** /rental/extend | Extend Rental
[**rental_history**](RentalApi.md#rental_history) | **POST** /rental/history | Rental History
[**rental_info**](RentalApi.md#rental_info) | **POST** /rental/info | Retrieve Rental Info
[**rental_refund**](RentalApi.md#rental_refund) | **POST** /rental/refund | Refund Rental
[**rental_reset**](RentalApi.md#rental_reset) | **POST** /rental/reset | Reset Rental
[**rental_retrieve**](RentalApi.md#rental_retrieve) | **POST** /rental/retrieve | Retrieve Active Rentals
[**rental_retrieve_all**](RentalApi.md#rental_retrieve_all) | **POST** /rental/retrieve_all | Retrieve Rental IDs
[**rental_retrieve_history**](RentalApi.md#rental_retrieve_history) | **POST** /rental/retrieve_history | Retrieve your rentals
[**rental_retrieve_messages**](RentalApi.md#rental_retrieve_messages) | **POST** /rental/retrieve_messages | Retrieve Rental Messages
[**rental_retrieve_pricing**](RentalApi.md#rental_retrieve_pricing) | **POST** /rental/retrieve_pricing | Retrieve Rental Pricing
[**rental_retrieve_services**](RentalApi.md#rental_retrieve_services) | **POST** /rental/retrieve_services | Retrieve Rental Services
[**rental_retrieve_status**](RentalApi.md#rental_retrieve_status) | **POST** /rental/retrieve_status | Retrieve Rental Status
[**rental_service_price**](RentalApi.md#rental_service_price) | **POST** /rental/service_price | Retrieve rental service price
[**rental_stock**](RentalApi.md#rental_stock) | **POST** /rental/stock | Retrieve Rental Stock


# **purchase_rental**
> object purchase_rental(id, days, service_id=service_id, create_token=create_token, city=city, state=state, zipcode=zipcode)

Order Rental

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
    api_instance = smspool_sdk.RentalApi(api_client)
    id = 56 # int | Rental ID retrieved from Retrieve Rental IDs
    days = 56 # int | 
    service_id = 56 # int | Optional value on which service you'd purchase the rental for (optional)
    create_token = 56 # int | Create a rental token which allows you to share this specific rental (optional)
    city = 'city_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    zipcode = 'zipcode_example' # str |  (optional)

    try:
        # Order Rental
        api_response = api_instance.purchase_rental(id, days, service_id=service_id, create_token=create_token, city=city, state=state, zipcode=zipcode)
        print("The response of RentalApi->purchase_rental:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->purchase_rental: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Rental ID retrieved from Retrieve Rental IDs | 
 **days** | **int**|  | 
 **service_id** | **int**| Optional value on which service you&#39;d purchase the rental for | [optional] 
 **create_token** | **int**| Create a rental token which allows you to share this specific rental | [optional] 
 **city** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **zipcode** | **str**|  | [optional] 

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

# **rental_auto_extend**
> object rental_auto_extend(rental_code)

Enable Auto Extend Rental

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Enable Auto Extend Rental
        api_response = api_instance.rental_auto_extend(rental_code)
        print("The response of RentalApi->rental_auto_extend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_auto_extend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_extend**
> object rental_extend(days, rental_code)

Extend Rental

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
    api_instance = smspool_sdk.RentalApi(api_client)
    days = 56 # int | 
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Extend Rental
        api_response = api_instance.rental_extend(days, rental_code)
        print("The response of RentalApi->rental_extend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_extend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | 
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_history**
> object rental_history()

Rental History

Retrieve a history of all your rental actions.

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
    api_instance = smspool_sdk.RentalApi(api_client)

    try:
        # Rental History
        api_response = api_instance.rental_history()
        print("The response of RentalApi->rental_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_history: %s\n" % e)
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

# **rental_info**
> object rental_info(rental_code)

Retrieve Rental Info

Retrieve rental information

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Retrieve Rental Info
        api_response = api_instance.rental_info(rental_code)
        print("The response of RentalApi->rental_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_refund**
> object rental_refund(rental_code)

Refund Rental

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Refund Rental
        api_response = api_instance.rental_refund(rental_code)
        print("The response of RentalApi->rental_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_reset**
> object rental_reset(rental_code)

Reset Rental

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Reset Rental
        api_response = api_instance.rental_reset(rental_code)
        print("The response of RentalApi->rental_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_retrieve**
> object rental_retrieve()

Retrieve Active Rentals

Retrieve a history of all your rental actions.

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
    api_instance = smspool_sdk.RentalApi(api_client)

    try:
        # Retrieve Active Rentals
        api_response = api_instance.rental_retrieve()
        print("The response of RentalApi->rental_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve: %s\n" % e)
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

# **rental_retrieve_all**
> object rental_retrieve_all(type)

Retrieve Rental IDs

Retrieve available rental products. Each listing includes `is_refundable` (`0` or `1`), `refund_within` (hours after purchase a refund is allowed; `0` when not refundable), and `refund_min_days` (minimum duration that is eligible for a refund; `0` when there is no duration floor or the rental is never refundable). Refunds also require that no messages have been received.

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
    api_instance = smspool_sdk.RentalApi(api_client)
    type = 56 # int | Choose whether the rental is extendable or not with a 0 or 1

    try:
        # Retrieve Rental IDs
        api_response = api_instance.rental_retrieve_all(type)
        print("The response of RentalApi->rental_retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| Choose whether the rental is extendable or not with a 0 or 1 | 

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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rental_retrieve_history**
> object rental_retrieve_history()

Retrieve your rentals

List every rental on your account that was not refunded, including expired ones. For the actions taken on your rentals (activations, extensions, refunds) use **Rental History** instead.

- `rental`: the rental ID from **Retrieve Rental IDs**
- `rental_code`: use it with the other rental endpoints, such as **Retrieve Rental Messages**
- `expiration_date`: Unix timestamp
- `source`: the pool the number comes from
- `state`: the US state of the number, or `Unknown`

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
    api_instance = smspool_sdk.RentalApi(api_client)

    try:
        # Retrieve your rentals
        api_response = api_instance.rental_retrieve_history()
        print("The response of RentalApi->rental_retrieve_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_history: %s\n" % e)
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

# **rental_retrieve_messages**
> object rental_retrieve_messages(rental_code)

Retrieve Rental Messages

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Retrieve Rental Messages
        api_response = api_instance.rental_retrieve_messages(rental_code)
        print("The response of RentalApi->rental_retrieve_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_retrieve_pricing**
> object rental_retrieve_pricing(id, service=service)

Retrieve Rental Pricing

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
    api_instance = smspool_sdk.RentalApi(api_client)
    id = 56 # int | The rental ID retrieved from `Retrieve Rental IDs`
    service = 'service_example' # str | Service name or service ID which can be retrieved at the /service/retrieve_all endpoint (optional)

    try:
        # Retrieve Rental Pricing
        api_response = api_instance.rental_retrieve_pricing(id, service=service)
        print("The response of RentalApi->rental_retrieve_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The rental ID retrieved from &#x60;Retrieve Rental IDs&#x60; | 
 **service** | **str**| Service name or service ID which can be retrieved at the /service/retrieve_all endpoint | [optional] 

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

# **rental_retrieve_services**
> object rental_retrieve_services(rental=rental)

Retrieve Rental Services

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental = 56 # int | The rental ID retrieved from `Retrieve Rental IDs` (optional)

    try:
        # Retrieve Rental Services
        api_response = api_instance.rental_retrieve_services(rental=rental)
        print("The response of RentalApi->rental_retrieve_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental** | **int**| The rental ID retrieved from &#x60;Retrieve Rental IDs&#x60; | [optional] 

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

# **rental_retrieve_status**
> object rental_retrieve_status(rental_code)

Retrieve Rental Status

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
    api_instance = smspool_sdk.RentalApi(api_client)
    rental_code = 'rental_code_example' # str | The retrieved rental code from the `Order rental` endpoint.

    try:
        # Retrieve Rental Status
        api_response = api_instance.rental_retrieve_status(rental_code)
        print("The response of RentalApi->rental_retrieve_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_retrieve_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_code** | **str**| The retrieved rental code from the &#x60;Order rental&#x60; endpoint. | 

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

# **rental_service_price**
> object rental_service_price(id, service_id)

Retrieve rental service price

Some rentals are bound to a single service. This returns the price of a rental for that service, with the custom pricing on your account applied.

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
    api_instance = smspool_sdk.RentalApi(api_client)
    id = 56 # int | The rental ID retrieved from `Retrieve Rental IDs`
    service_id = 56 # int | The service ID retrieved from `Retrieve Rental Services`

    try:
        # Retrieve rental service price
        api_response = api_instance.rental_service_price(id, service_id)
        print("The response of RentalApi->rental_service_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_service_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The rental ID retrieved from &#x60;Retrieve Rental IDs&#x60; | 
 **service_id** | **int**| The service ID retrieved from &#x60;Retrieve Rental Services&#x60; | 

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

# **rental_stock**
> object rental_stock(id, days, service_id=service_id)

Retrieve Rental Stock

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
    api_instance = smspool_sdk.RentalApi(api_client)
    id = 56 # int | The rental ID retrieved from `Retrieve Rental IDs`
    days = 56 # int | 
    service_id = 56 # int |  (optional)

    try:
        # Retrieve Rental Stock
        api_response = api_instance.rental_stock(id, days, service_id=service_id)
        print("The response of RentalApi->rental_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalApi->rental_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The rental ID retrieved from &#x60;Retrieve Rental IDs&#x60; | 
 **days** | **int**|  | 
 **service_id** | **int**|  | [optional] 

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


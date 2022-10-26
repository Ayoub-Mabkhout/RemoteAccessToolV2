# swagger_client.RemoteServerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_process_list**](RemoteServerApi.md#get_process_list) | **GET** /remote/processes | 
[**screenshot**](RemoteServerApi.md#screenshot) | **GET** /remote/screenshot | 
[**system_reboot**](RemoteServerApi.md#system_reboot) | **GET** /remote/reboot | 
[**system_shut_down**](RemoteServerApi.md#system_shut_down) | **GET** /remote/shutdown | 

# **get_process_list**
> list[str] get_process_list()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteServerApi()

try:
    api_response = api_instance.get_process_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteServerApi->get_process_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screenshot**
> list[str] screenshot()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteServerApi()

try:
    api_response = api_instance.screenshot()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteServerApi->screenshot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_reboot**
> system_reboot()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteServerApi()

try:
    api_instance.system_reboot()
except ApiException as e:
    print("Exception when calling RemoteServerApi->system_reboot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_shut_down**
> system_shut_down()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteServerApi()

try:
    api_instance.system_shut_down()
except ApiException as e:
    print("Exception when calling RemoteServerApi->system_shut_down: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


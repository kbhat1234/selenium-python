import requests
import json

host_url = "https://reqres.in/api"
end_point_url = "/users"

body = {
    "name": "morpheus",
    "job": "zion resident",
    "age": 43
}

response_code = requests.put(host_url + end_point_url, data=body)

print(response_code.status_code)
print(response_code.content)
print(response_code.headers)

response_result = (json.dumps(response_code.json(), indent=2))
print(response_result)
print(response_code.request)

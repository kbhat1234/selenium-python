import requests
import json

host_url = "https://reqres.in/api"
end_point_url = "/users"

body = {
    "name": "morpheus",
    "job": "leader"
}

response_code = requests.post(host_url+end_point_url,data=body)

print(response_code.status_code)
print(response_code.request)

response_result = (json.dumps(response_code.json(),indent=2))
print(response_result)

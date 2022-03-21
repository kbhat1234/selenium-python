import requests
import json

host_url = "https://reqres.in/api"
end_point_url = "/users/2"

response_code = requests.delete(host_url+end_point_url)
print(response_code.status_code)
print(response_code.request)

#response_result = (json.dumps(response_code.json(),indent=4))
#response_result = response_code.json()
#print(response_result)

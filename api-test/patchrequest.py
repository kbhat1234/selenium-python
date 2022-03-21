import requests
import json

baseUrl = "https://reqres.in/api"
endPointUrl = "/users/2"
body = {
"name": "Karthik"
}

response = requests.patch(url=baseUrl+endPointUrl,data=body)
print(dir(response))
print(vars(response))
print(vars(response).keys())
print(vars(response).values())
print(response.status_code, type(response.status_code))
print(response.ok, type(response.ok))
print(response.url, type(response.url))
print(response.request,type(response.request))
print(response.content, type(response.content))
print(response.headers, type(response.headers))
print(response.cookies, type(response.cookies))
print(response.encoding, type(response.encoding))
print(response.elapsed, type(response.elapsed))
print(response.history, type(response.history))
print(response.text, type(response.text))
r = response.json()
print(r)
print(r['name'])
assert (r['name']) == 'Karthik', "Invalid name"

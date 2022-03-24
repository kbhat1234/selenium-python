import requests
import json

host_url = "https://reqres.in/api"
end_point_url = "/users"
parameters = {
    "page": 2
}

response_code = requests.get(host_url + end_point_url, params=parameters)
# response_code = requests.get(host_url)
print("the response for this GET request is")
print(type(response_code.status_code))
print(response_code.status_code)
print(response_code.encoding)
print(response_code.headers)
print(response_code.text)
print(response_code.content)
print(response_code.cookies)
print(response_code.url)
resp = response_code.json()

print(resp["data"][0]["first_name"])
print(resp["data"][1]["email"])
assert (resp["data"][1]["email"]).endswith("reqres.in"), "Wrong email format"
print(resp["support"]["url"])
assert resp["support"]["url"] == "https://reqres.in/#support-heading", "Wrong support url"
assert resp["data"][1]["email"] == "lindsay.ferguson@reqres.in", "wrong email address"
response_result = (json.dumps(response_code.json(), indent=4))

# print(response_result)

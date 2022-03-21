import requests
import json

base_url = "https://api.github.com/users/kbhat1234"
resp = requests.get(base_url)
#print(resp)
print(type(resp))
r = resp.json()
print(type(r))
print(r)
print(r['id'])
assert r['id'] != None, "ID value is not populated"
print(resp.status_code)
assert resp.status_code == 200 , "Invalid Response code"
print(resp.url)
print(type(resp.url))
print(resp.text)
print(type(resp.text))
print(resp.cookies)
print(type(resp.cookies))
print(resp.headers)
print(type(resp.headers))
print(resp.encoding)
assert resp.encoding == 'utf-8', "not valid format"
print(resp.history)
print(resp.reason, resp.raw)
#print(dir(resp))
print(resp.elapsed)
print(resp.request)
print(resp.ok)
print(resp.links)
import requests
import json

baseUrl = "https://api.github.com"

resp = requests.get(url=baseUrl)
print(type(resp))

r = resp.json()
print(type(r))
print(r)

print(r['feeds_url'])
print(r['emojis_url'])
print(r['starred_gists_url'])

assert (r['feeds_url']).endswith('feeds'), "wrong url"
assert (resp.status_code) == 200, "invalid status code"
print(resp.request)
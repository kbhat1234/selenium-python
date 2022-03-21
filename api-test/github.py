import requests
import json

r = requests.get("https://api.github.com/user", auth=('kbhat1234','Anurag@2376'))
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.json())
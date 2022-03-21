import requests
import json

#base_url = "https://expired.badssl.com/"
base_url = "https://github.com"
verify = "path/to/certfile"
session1 = requests.Session()
print(session1)
session1.get('https://httpbin.org/cookies/set/sessioncookie/0x0000012B373D1840')

resp = session1.get('https://httpbin.org/cookies')

print(resp.cookies)
#print(resp.status_code)
#print(resp.text)
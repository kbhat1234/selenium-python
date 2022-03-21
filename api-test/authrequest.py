import requests
import json
from requests.auth import HTTPBasicAuth

base_url = "https://api.github.com/users/kbhat1234"

resp = requests.get(base_url, auth=HTTPBasicAuth('kbhat1234', 'Anurag@2376'))
print(resp.json())
print(resp.status_code)
import requests

from requests.auth import HTTPBasicAuth, HTTPDigestAuth


def valid_credentials():
    s = requests.session()

    response = s.get("https://api.github.com/users/kbhat1234", auth=HTTPBasicAuth("kbhat1234", "Anurag@2376"))
    print(response.status_code)
    print(response.json())
    s.close()


def httpdigestauth():
    baseurl = "https://httpbin.org/digest-auth/auth/kbhat1234/Anurag@2376"
    response = requests.get(url=baseurl, auth=HTTPDigestAuth("kbhat2376", "Anurag@2376"))
    print(response.status_code)
    print(response.json())


valid_credentials()
httpdigestauth()

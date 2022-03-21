import requests

u = "https://httpbin.org/post"

f = {
    'file': open('rootkey.csv', 'rb')
}

r = requests.post(url=u, files=f)
print(r.status_code)
print(r.text)
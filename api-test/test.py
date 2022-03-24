import requests

u = "https://httpbin.org/post"

f = {
    'file': open('rootkey.csv', 'rb')
}

r = requests.post(url=u, files=f)
print(r.status_code)
for i in r.iter_content():
    print(i)
print(r.is_redirect)
print(r.text)

# Making a GET request
r = requests.get('https://api.github.com/users/kbhat1234')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)
print(r.links)


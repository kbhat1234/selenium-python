import requests

s = requests.session()
print(s)

r = s.get("https://httpbin.org/cookies/set/sessioncookie/1234567")

print(r)
print(r.json())
print(r.text)

r = s.get("https://httpbin.org/cookies")
print(r)
print(r.json)
print(r.text)
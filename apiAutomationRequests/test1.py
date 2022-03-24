import requests

response = requests.get("https://reqres.in/api/users?page=2")

print(response.status_code)
'''
200
'''

print(response.headers)
'''
{'Date': 'Tue, 22 Mar 2022 13:39:23 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Etag': 'W/"406-ut0vzoCuidvyMf8arZpMpJ6ZRDw"', 'Via': '1.1 vegur', 'Cache-Control': 'max-age=14400', 'CF-Cache-Status': 'HIT', 'Age': '655', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=gJFmnE6y8kVfwgUfDXrOkf34XbNPHkaAt7jIAGz%2BhNEst%2FDKCSGAXaaYoRE7BcC5QxEs%2FHjH6%2F8Wv9n%2BVRG03KgmzwibsHgJKjy3b5r10UZgG5nfyiHlLTmhTBI%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '6eff55490f19772c-LHR', 'Content-Encoding': 'gzip', 'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400'}
'''

print(response.json())
'''
{'page': 2, 'per_page': 6, 'total': 12, 'total_pages': 2, 'data': [{'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}, {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}, {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://reqres.in/img/faces/9-image.jpg'}, {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar': 'https://reqres.in/img/faces/10-image.jpg'}, {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://reqres.in/img/faces/11-image.jpg'}, {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}], 'support': {'url': 'https://reqres.in/#support-heading', 'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'}}
'''

print(response.request)
'''
<PreparedRequest [GET]>
'''

print(response.text)
'''
{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
'''

print(response.links)
'''
{}
'''

print(response.ok)
'''
True
'''

print(response.reason)
'''
OK
'''

print(response.content)
'''
b'{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
'''

print(response.history)
'''
[]
'''

print(response.elapsed)
'''
0:00:00.538259
'''

print(response.cookies)
print(response.url)
print(response.encoding)
print(response.is_redirect)
print(response.is_permanent_redirect)
print(response.apparent_encoding)
print(response.next)
print(response.raise_for_status())
print(response.close())
'''
<RequestsCookieJar[]>
https://reqres.in/api/users?page=2
utf-8
False
False
ascii
None
None
None
'''

baseUrl = "https://reqres.in/api"
endPointUrl = "/users"
queryParam = {
    "page": 2
}

# Making a HEAD request
# r1 = requests.head(url=baseUrl + endPointUrl, params=queryParam)
r1 = requests.get(url=baseUrl + endPointUrl, params=queryParam)
# check status code for response received
# success code - 200
print(r1.json())

# print headers of request
print(r1.headers)

# checking if request contains any content
print(r1.content)

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()
print(r.status_code)
print(r.content)


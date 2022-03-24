import requests

# import json

"""
with open('C:\\Users\\admin\\PycharmProjects\\pythonlearning\\api-test\\api.json') as jsonfile:
    parsed = json.load(jsonfile)

print(json.dumps(parsed, indent=2, sort_keys=True))

data = json.loads(open('C:\\Users\\admin\\PycharmProjects\\pythonlearning\\api-test\\api.json').read())

print(type(data))
"""

baseURL = "https://reqres.in/api"

endPointURL1 = "/users"

endPointURL2 = "/register"

endPointURL3 = "/login"

param = {
    "page": 2
}

delayParam = {
    "delay": 5
}

postBody = {
    "name": "morpheus",
    "job": "leader"
}

patchBody = {
    "name": "rini"
}

putBody = {
    "name": "Karthik",
    "job": "Software"
}

registerBodySuccess = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

registerBodyUnsuccessEmail = {
    "email": "sydney@fife"
}

registerBodyUnsuccessPassword = {
    "password": "pistol"
}


def listusers():
    print("GET() method - Getting details of all users")
    response = requests.get(url=baseURL + endPointURL1, params=param)
    r = response.json()

    print(response)

    print(response.status_code)
    print(response.url)
    print(response.ok)
    print(response.headers)
    print(response.content)
    print(response.text)
    print(response.request)
    print(r)
    print(r['total_pages'])
    print(r['data'][0]['first_name'])
    print(r['data'][0]['email'])
    print(r['data'][2])

    assert response.status_code == 200, "Invalid status code"
    assert r['data'][0]['email'] == "george.bluth@reqres.in", "invalid email"


def header_info_reponse():
    response = requests.head(url=baseURL + endPointURL1, params=param)
    print(response.status_code)
    print(response.url)
    print(response.content)
    print(response.headers)


def singleuser():
    print("GET() method - Getting details of single user")
    response = requests.get(url=baseURL + endPointURL1 + "/2")
    r = response.json()

    print(response.status_code)
    print(response.url)
    print(response.ok)
    print(response.text)
    print(response.request)

    print(r['data']['id'])
    print(r['support']['url'])
    print(r['data']['email'])
    print(r)

    assert r['data']['id'] == 2, "invalid id value"
    assert r['data']['email'] == 'janet.weaver@reqres.in', "invalid email"
    assert r['support']['url'] == "https://reqres.in/#support-heading", "invalid support url"


def usernotfound():
    print("GET() method - Searching users with invalid id")
    response = requests.get(url=baseURL + endPointURL1 + "/23")
    r = response.json()

    print(response.status_code)
    print(response.url)
    print(response.request)

    assert response.status_code == 404, "invalid response status"
    print(r)


def createuserpost():
    print("POST() method - Creating the new user")
    response = requests.post(url=baseURL + endPointURL1, data=postBody)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)
    print(r)
    print(r['name'] + " " + r['job'] + " " + r['id'])

    assert r['name'] == "morpheus", "invalid name"
    assert response.status_code == 201, "invalid status code"


def updateuserput():
    print("PUT() method - updating the user details")
    response = requests.put(url=baseURL + endPointURL1 + "/200", data=putBody)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)
    print(r)
    print(r['name'] + " " + r['job'])

    assert r['name'] == "Karthik", "invalid name"
    assert response.status_code == 200, "invalid status code"


def partialupdateuserpatch():
    print("PATCH() method - partial updating the user details")
    response = requests.put(url=baseURL + endPointURL1 + "/33", data=patchBody)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.content)
    print(response.request)
    print(r)
    print(r['name'])

    assert r['name'] == "rini", "invalid name"
    assert response.status_code == 200, "invalid status code"


def deleteuser():
    print("DELETE() method - deleting the user")
    response = requests.delete(url=baseURL + endPointURL1 + "/2")

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    assert response.status_code == 204, "invalid status code"


def userregisterationsuccess():
    print("POST() method - Successful user registration")
    response = requests.post(url=baseURL + endPointURL2, data=registerBodySuccess)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    print(r['id'], r['token'])
    print(r)

    assert response.status_code == 200, "invalid status code"


def registrationuncessfulemail():
    print("POST() method - Unsuccessful user registration with email only")
    response = requests.post(url=baseURL + endPointURL2, data=registerBodyUnsuccessEmail)

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    assert response.status_code == 400, "invalid status code"


def registrationuncessfulpassword():
    print("POST() method - Unsuccessful user registration with password only")
    response = requests.post(url=baseURL + endPointURL2, data=registerBodyUnsuccessPassword)

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    assert response.status_code == 400, "invalid status code"


def loginsuccessful():
    print("POST() method - login successful")
    response = requests.post(url=baseURL + endPointURL3, data=registerBodySuccess)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    print(r)
    print(r['token'])

    assert response.status_code == 200, "invalid status code"


def loginunsuccessfulemail():
    print("POST() method - login successful")
    response = requests.post(url=baseURL + endPointURL3, data=registerBodyUnsuccessEmail)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    print(r['error'])

    assert response.status_code == 400, "invalid status code"


def loginunsuccessfulpassword():
    print("POST() method - login successful")
    response = requests.post(url=baseURL + endPointURL3, data=registerBodyUnsuccessPassword)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    print(r['error'])

    assert response.status_code == 400, "invalid status code"


def delayedresponse():
    print("Delayed response in getting the response")
    response = requests.get(url=baseURL + endPointURL1, params=delayParam)
    r = response.json()

    print(response.status_code)
    print(response.ok)
    print(response.url)
    print(response.request)

    assert r['per_page'] == 6, "invalid contents per page"


# listusers()
header_info_reponse()
# singleuser()
# usernotfound()
# createuserpost()
# updateuserput()
# partialupdateuserpatch()
# deleteuser()

# userregisterationsuccess()
# registrationuncessfulemail()
# registrationuncessfulpassword()
# loginsuccessful()
# loginunsuccessfulemail()
# loginunsuccessfulpassword()
# delayedresponse()

import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post("https://reqres.in/api/register", data = payload)
print(response)
print(response.json())
assert response.json()['token']=='QpwL5tke4Pnpja7X4'
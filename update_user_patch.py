import requests

payload = {
    "name": "API",
}

response = requests.patch("https://reqres.in/api/users/2", data = payload)
print(response)
print(response.json())
assert response.json()['name']=='API'
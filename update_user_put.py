import requests

payload = {
    "name": "API",
    "job": "doctor"
}

response = requests.put("https://reqres.in/api/users/2", data = payload)
print(response)
print(response.json())
assert response.json()['job']=='doctor'
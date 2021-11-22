import requests

payload = {
    "name": "Taras",
    "job": "Automation"
}

response = requests.post("https://reqres.in/api/users", data = payload)
print(response)
print(response.json())
assert response.json()['job']=='Automation'
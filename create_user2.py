import requests
import json

my_data = open("data.json", "r").read()

response = requests.post("https://reqres.in/api/users", data = json.loads(my_data))
print(response)
print(response.json())
print(response.headers.get("Content-Type"))
assert response.json()['job']=='Sfera'
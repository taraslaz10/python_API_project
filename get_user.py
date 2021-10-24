import requests

resp = requests.get('https://reqres.in/api/users?page/2')

json_response = resp.json()

print(json_response['total_pages'])

assert json_response['total_pages'] == 2, "Problem"

print(json_response['data'][0]["email"])

assert (json_response["data"][0]["email"]).endswith("reqres.in"), "email wrong"
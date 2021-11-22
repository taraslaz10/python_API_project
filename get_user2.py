import requests

p = {"page": 2}
resp = requests.get('https://reqres.in/api/users', params=p)

code = resp.status_code

assert code == 200, "Code doesn't match"

print(resp.json())

print(resp.cookies)

print(resp.encoding)

print(resp.url)
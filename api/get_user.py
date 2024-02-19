import requests

# http://127.0.0.1:5000/puppies
# https://reqres.in/api/users?page=2

resp = requests.get("http://127.0.0.1:5000/puppies")
print(f"Response : {resp}")
print(f"Type : {type(resp)}")
print(f"Dir : {dir(resp)}")
print(f"Staus : {resp.status_code}")

# assert resp.status_code==200,f"Status code does not match ! {resp.status_code}"

print(resp.json())
print(resp.headers)

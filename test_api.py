import pytest
import requests
import json

def main_url():
    return "https://reqres.in/"

def test_login():
    url = main_url() + "api/login"
    my_data = {"email": "eve.holt@reqres.in" , "password":"cityslicka"}
    res = requests.get(url,data=my_data)
    my_token = json.loads(res.text)
    print(res.text)
    print(my_token)
    assert res.status_code == 200
    #assert my_token["token"]=="QpwL5tke4Pnpja7X4"

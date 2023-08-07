import requests
import pytest


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = f"{self.base_address}{path}"
        response = requests.post(url=url, params=params, data=data, headers=headers)
        return response

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        response = requests.get(url=url, params=params, headers=headers)
        return response


@pytest.fixture
def reqres_api():
    return ApiClient(base_address='https://reqres.in/')

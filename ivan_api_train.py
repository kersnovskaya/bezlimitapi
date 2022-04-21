import requests
from lkapi.configuration.config import TOKEN_IVAN

class Test:
    token = TOKEN_IVAN

    def test_authorize(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {
            "phone": 9696588825,
            "password": "Takkurwatak1"
        }

        request_url = f"{lktest_url}/user/auth/login"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)

        desertialized_response = response.json()
        print(desertialized_response)

        assert response.status_code == 200


    def test_authorize_wrong_passwrod(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        lktest_url = "https://lktest.bezlimit.ru/v1"

        expected_response = [{
            "field": "password",
            "message": "Пароль для аккаунта указан не верно."
        }
        ]

        data = {
            "phone": 9696588825,
            "password": "WrongPassword"
        }

        request_url = f"{lktest_url}/user/auth/login"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)

        desertialized_response = response.json()
        print(desertialized_response)

        assert desertialized_response == expected_response
        assert response.status_code == 422


    def test_authorize_wrong_number(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        lktest_url = "https://lktest.bezlimit.ru/v1"

        expected_response = [{
            "field": "phone",
            "message": "Введенный номер не обслуживается в Безлимит!"
        }
        ]

        data = {
            "phone": 9000000000,
            "password": "Takkurwatak1"
        }

        request_url = f"{lktest_url}/user/auth/login"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)

        desertialized_response = response.json()
        print(desertialized_response)

        assert desertialized_response == expected_response
        assert response.status_code == 422



    def test_get_account_phone(self):
        token = TOKEN_IVAN
        headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"

        expected_response = [{
                  "phone": 9696588825,
                  "name": None,
                  "is_disable_delete": True,
                  "is_adding_confirmed": True
                }]

        request_url = f"{lktest_url}/account/phone"
        response = requests.get(request_url, headers=headers)
        print(response)

        phone_list = response.json()
        print(phone_list)

        assert phone_list == expected_response
        assert response.status_code == 200


    def test_get_account_phone_correct_phone(self):
        token = TOKEN_IVAN
        headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9696588825

        expected_response = {
                  "phone": 9696588825,
                  "name": None,
                  "is_disable_delete": True,
                  "is_adding_confirmed": True
                }


        request_url = f"{lktest_url}/account/phone/{phone}"
        response = requests.get(request_url, headers=headers)
        print(response)
        desertialized_response = response.json()
        print(desertialized_response)

        assert desertialized_response == expected_response
        assert response.status_code == 200


    def test_get_account_phone_false_phone(self):
        token = TOKEN_IVAN
        headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000000
        data = {
            "expand": "phoneinfo"
        }
        request_url = f"{lktest_url}/account/phone/{phone}"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.json() is None
        assert response.status_code == 200


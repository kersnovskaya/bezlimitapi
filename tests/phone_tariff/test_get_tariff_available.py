import requests


class TestProd:

    def test_successful_getting_available_tariffs_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9006471111
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert type(i['id']) == int
            assert i['name']


    def test_successful_getting_available_tariffs_for_second_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9682220793
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert type(i['id']) == int
            assert i['name']


    def test_unsuccessful_getting_available_tariffs_for_side_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9696588825
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.'


    def test_unsuccessful_getting_available_tariffs_for_wrong_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 917980661313
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Введите номер телефона в формате 9001112233.'


    def test_unsuccessful_getting_available_tariffs_not_bezlimit_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!'


    def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'


class TestDev:

    def test_successful_getting_available_tariffs_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9006471111
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert type(i['id']) == int
            assert i['name']


    def test_successful_getting_available_tariffs_for_second_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9682220793
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert type(i['id']) == int
            assert i['name']


    def test_unsuccessful_getting_available_tariffs_for_side_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9696588825
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.'


    def test_unsuccessful_getting_available_tariffs_for_wrong_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 917980661313
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Введите номер телефона в формате 9001112233.'


    def test_unsuccessful_getting_available_tariffs_not_bezlimit_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert type(response.json) == dict
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!'


    def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

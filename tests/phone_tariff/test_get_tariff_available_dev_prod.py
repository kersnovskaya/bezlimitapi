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

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных тела ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert type(i['id']) == int, f'Тип данных параметра "id" не "int".'
            assert i['name'] is not None


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

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных тела ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert type(i['id']) == int, f'Тип данных параметра "id" не "int".'
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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.', 'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Введите номер телефона в формате 9001112233.', \
                                             'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!', \
                                             'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


    def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
        token = 'kurwa'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401, f'Код ответа {response.status_code}, а не 401.'
        assert response.reason == 'Unauthorized', f'Причина ошибки {response.reason}, а не "Unauthorized".'
        assert response.json()['message'] == 'Your request was made with invalid credentials.', \
                                             'Ошибка в параметре "message".'


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

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных тела ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert type(i['id']) == int, f'Тип данных параметра "id" не "int".'
            assert i['name'] is not None


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

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных тела ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert type(i['id']) == int, f'Тип данных параметра "id" не "int".'
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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.', 'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Введите номер телефона в формате 9001112233.', \
                                             'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


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

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!', \
                                             'Ошибка в параметре "message".'
        assert type(response.json()) == dict, f'Тип данных тела ответа {type(response.json())}, а не "dict".'


    def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
        token = 'kurwa'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        number = 9000000000
        request_url = f"{lktest_url}/phone/tariff/available/{number}"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401, f'Код ответа {response.status_code}, а не 401.'
        assert response.reason == 'Unauthorized', f'Причина ошибки {response.reason}, а не "Unauthorized".'
        assert response.json()['message'] == 'Your request was made with invalid credentials.', \
                                             'Ошибка в параметре "message".'


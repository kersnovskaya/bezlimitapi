import requests
import random


class TestDev:

    def test_successful_getting_tariff_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert type(response.json()['id']) == int, 'Тип данных в параметре "id" не "int".'
        assert response.json()['name'] is not None, 'В параметре "name" передаётся None.'

    def test_successful_getting_tariff_for_second_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9682220854"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert type(response.json()['id']) == int, 'Тип данных в параметре "id" не "int".'
        assert response.json()['name'] is not None, 'В параметре "name" передаётся None.'

    def test_successful_getting_tariff_with_one_random_field_at_lk(self):
        queries_fields = ['id', 'name', 'subscription_fee', 'packet_minutes', 'packet_sms', 'packet_internet']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'fields': random_field}

        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert len(response.json()) == 1, f'Количество элементов в ответе превышает 1.'
        assert response.json()[random_field], f'В ответе отдаётся параметр, не соответствующий параметру ' \
                                              f'в запросе{random_field}.'


    def test_successful_getting_tariff_with_adding_random_expand_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        queries_fields = ['description']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'expand': random_field}

        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()[random_field], f'В ответе отдаётся параметр, не соответствующий параметру ' \
                                              f'в запросе{random_field}.'

    def test_unsuccessful_getting_tariff_for_side_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9696588825"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.', 'Ошибка в параметре "message".'


    def test_unsuccessful_getting_tariff_for_not_bezlimit_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9000000000"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!', \
                                             'Ошибка в параметре "message".'

    def test_unsuccessful_getting_tariff_at_lk_without_token(self):
        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 401, f'Код ответа {response.status_code}, а не 401.'
        assert response.reason == 'Unauthorized', f'Причина ошибки {response.reason}, а не "Unauthorized".'
        assert response.json()['message'] == 'Your request was made with invalid credentials.', \
                                             'Ошибка в параметре "message".'




class TestProd:

    def test_successful_getting_tariff_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert type(response.json()['id']) == int, 'Тип данных в параметре "id" не "int".'
        assert response.json()['name'] is not None, 'В параметре "name" передаётся None.'

    def test_successful_getting_tariff_for_second_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9682220854"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}

        response = requests.get(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert type(response.json()['id']) == int, 'Тип данных в параметре "id" не "int".'
        assert response.json()['name'] is not None, 'В параметре "name" передаётся None.'

    def test_successful_getting_tariff_with_one_random_field_at_lk(self):
        queries_fields = ['id', 'name', 'subscription_fee', 'packet_minutes', 'packet_sms', 'packet_internet']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'fields': random_field}

        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert len(response.json()) == 1, f'Количество элементов в ответе превышает 1.'
        assert response.json()[random_field], f'В ответе отдаётся параметр, не соответствующий параметру ' \
                                              f'в запросе{random_field}.'


    def test_successful_getting_tariff_with_adding_random_expand_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        queries_fields = ['description']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'expand': random_field}

        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()[random_field], f'В ответе отдаётся параметр, не соответствующий параметру ' \
                                              f'в запросе{random_field}.'

    def test_unsuccessful_getting_tariff_for_side_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9696588825"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.', 'Ошибка в параметре "message".'


    def test_unsuccessful_getting_tariff_for_not_bezlimit_phone_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9000000000"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 404, f'Код ответа {response.status_code}, а не 404.'
        assert response.reason == 'Not Found', f'Причина ошибки {response.reason}, а не "Not Found".'
        assert type(response.json()) == dict, f'Тип данных в ответе {type(response.json())}, вместо "dict".'
        assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!', \
                                             'Ошибка в параметре "message".'

    def test_unsuccessful_getting_tariff_at_lk_without_token(self):
        token = 12345678910
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/tariff/9006471111"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {}

        response = requests.get(request_url, headers=headers, params=params)
        print(response)
        print(response.json())

        assert response.status_code == 401, f'Код ответа {response.status_code}, а не 401.'
        assert response.reason == 'Unauthorized', f'Причина ошибки {response.reason}, а не "Unauthorized".'
        assert response.json()['message'] == 'Your request was made with invalid credentials.', \
                                             'Ошибка в параметре "message".'


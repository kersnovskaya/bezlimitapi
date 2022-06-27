import requests
import datetime
from datetime import datetime


class TestDev:

    def test_get_phone_service_connected_invalid_token(self):
        message = ['Подключенные услуги. Неавторизован.']
        expected_message = ['Подключенные услуги. Неавторизован.']

        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = 9006471111
        request_url = f"{lktest_url}/phone/service/connected"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в тексте ошибки.')

        assert message == expected_message, message

    def test_get_phone_service_connected_invalid_status(self):
        message = ['Подключенные услуги. Некорректный status.']
        expected_message = ['Подключенные услуги. Некорректный status.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        status = ['connected']
        request_url = f"{lktest_url}/phone/service/connected"

        params = {'phone': phone,
                  'status': status}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 500
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 500.")
        try:
            assert response.reason == 'Internal Server Error'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Internal Server Error'.")
        try:
            assert 'status must be array, string used' in response.json()['message']
        except AssertionError:
            message.append('Ошибка в тексте ошибки.')

        assert message == expected_message, message

    def test_get_phone_service_connected_incorrect_phone(self):
        message = ['Подключенные услуги. Запрос для стороннего номера.']
        expected_message = ['Подключенные услуги. Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9696588825
        request_url = f"{lktest_url}/phone/service/connected"

        params = {'phone': phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Номер телефона не привязан к аккаунту."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_get_phone_service_connected_not_bezlimit_phone(self):
        message = ['Подключенные услуги. Запрос для стороннего номера.']
        expected_message = ['Подключенные услуги. Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000000
        request_url = f"{lktest_url}/phone/service/connected"

        params = {'phone': phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        for i in response.json():
            try:
                assert i['message'] == 'Введенный номер не обслуживается в Безлимит!'
            except AssertionError:
                message.append('Ошибка в параметре "message".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')

        assert message == expected_message, message

    def test_get_phone_service_connected_correct_without_status(self):
        message = ['Подключенные услуги. Корректный запрос без статуса.']
        expected_message = ['Подключенные услуги. Корректный запрос без статуса.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        request_url = f"{lktest_url}/phone/service/connected"

        params = {'phone': phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i["id"]) == int
                assert type(i["title"]) == str
                assert type(i["short_description"]) == str
                assert type(i["description"]) == str
                assert type(i["type"]) == dict
                assert type(i["payment_period"]) == str
                assert type(i["connection_cost"]) == str
                assert type(i["subscription_fee"]) == str
                assert type(i["can_be_deferred"]) == bool
                assert type(i["cannot_be_disabled"]) == bool
                assert type(i["is_hit"]) == bool
            except AssertionError:
                message.append(f'В "услуге {i["title"]}" параметрах ответа некорректные типы данных.')

        assert message == expected_message, message


    def test_get_phone_service_connected_correct_with_status_connected(self):
        message = ['Подключенные услуги. Статус connected - есть услуга.']
        expected_message = ['Подключенные услуги. Статус connected - есть услуга.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=connected"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json() != []
        except AssertionError:
            message.append(f'На номере {phone} нет услуг.')
        try:
            assert type(response.json()) == list
        except:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert datetime.strptime(i['connected_date'], '%Y-%m-%d %H:%M:%S') <= datetime.now()
            except AssertionError:
                message.append(f'В услуге {i["title"]} указана некорректная дата подключения.')
            try:
                assert type(i["id"]) == int
                assert type(i["title"]) == str
                assert type(i["short_description"]) == str
                assert type(i["description"]) == str
                assert type(i["type"]) == dict
                assert type(i["payment_period"]) == str
                assert type(i["connection_cost"]) == str
                assert type(i["subscription_fee"]) == str
                assert type(i["can_be_deferred"]) == bool
                assert type(i["cannot_be_disabled"]) == bool
                assert type(i["is_hit"]) == bool
            except AssertionError:
                message.append(f'В "услуге {i["title"]}" параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_service_connected_correct_with_status_connected_deferred(self):
        message = ['Подключенные услуги. Статус connected-deferred - есть услуга.']
        expected_message = ['Подключенные услуги. Статус connected-deferred - есть услуга.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=connected-deferred"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json() != []
        except AssertionError:
            message.append(f'На номере {phone} нет услуг.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            for j in i['connectionTask']:
                try:
                    assert j is not None
                except AssertionError:
                    message.append(f'В "услуге {i["title"]}" пустой "connectionTask".')
                try:
                    assert datetime.strptime(j['date'], '%Y-%m-%d %H:%M:%S') > datetime.now()
                except AssertionError:
                    message.append(f'В услуге {i["title"]} указана некорректная дата подключения.')
            try:
                assert type(i["id"]) == int
                assert type(i["title"]) == str
                assert type(i["short_description"]) == str
                assert type(i["description"]) == str
                assert type(i["type"]) == dict
                assert type(i["payment_period"]) == str
                assert type(i["connection_cost"]) == str
                assert type(i["subscription_fee"]) == str
                assert type(i["can_be_deferred"]) == bool
                assert type(i["cannot_be_disabled"]) == bool
                assert type(i["is_hit"]) == bool
            except AssertionError:
                message.append(f'В "услуге {i["title"]}" параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_service_connected_correct_with_status_disconnected_deferred(self):
        message = ['Подключенные услуги. Статус disconnected-deferred - есть услуга.']
        expected_message = ['Подключенные услуги. Статус disconnected-deferred - есть услуга.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=disconnected-deferred"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json() != []
        except AssertionError:
            message.append(f'На номере {phone} нет услуг.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            for j in i['disconnectionTask']:
                try:
                    assert j is not None
                except AssertionError:
                    message.append(f'В "услуге {i["title"]}" пустой "disconnectionTask".')
                try:
                    assert datetime.strptime(j['date'], '%Y-%m-%d %H:%M:%S') > datetime.now()
                except AssertionError:
                    message.append(f'В услуге {i["title"]} указана некорректная дата подключения.')
            try:
                assert type(i["id"]) == int
                assert type(i["title"]) == str
                assert type(i["short_description"]) == str
                assert type(i["description"]) == str
                assert type(i["type"]) == dict
                assert type(i["payment_period"]) == str
                assert type(i["connection_cost"]) == str
                assert type(i["subscription_fee"]) == str
                assert type(i["can_be_deferred"]) == bool
                assert type(i["cannot_be_disabled"]) == bool
                assert type(i["is_hit"]) == bool
            except AssertionError:
                message.append(f'В "услуге {i["title"]}" параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_service_connected_correct_with_status_connected_deferred_no_services(self):
        message = ['Подключенные услуги. Статус connected-deferred - нет услуг.']
        expected_message = ['Подключенные услуги. Статус connected-deferred - нет услуг.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9618880491
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=connected-deferred"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")

        assert message == expected_message, message

    def test_get_phone_service_connected_correct_with_status_connected_no_services(self):
        message = ['Подключенные услуги. Статус connected - нет услуг.']
        expected_message = ['Подключенные услуги. Статус connected - нет услуг.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9618880491
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=connected"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")

        assert message == expected_message, message


    def test_get_phone_service_connected_correct_with_status_disconnected_deferred_no_services(self):
        message = ['Подключенные услуги. Статус disconnected-deferred - нет услуг.']
        expected_message = ['Подключенные услуги. Статус disconnected-deferred - нет услуг.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9618880491
        request_url = f"{lktest_url}/phone/service/connected/{phone}?status%5B%5D=disconnected-deferred"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")

        assert message == expected_message, message

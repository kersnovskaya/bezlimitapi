import requests
import random


class TestProd:

    def test_get_phone_finance_payments_invalid_token(self):
        message = ['Список платежей за период. Неавторизован.']
        expected_message = ['Список платежей за период. Неавторизован.']

        token = 12345678910
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments"

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

    def test_get_phone_finance_payments_incorrect_phone(self):
        message = ['Список платежей за период. Запрос для стороннего номера.']
        expected_message = ['Список платежей за период. Запрос для стороннего номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 9696588825}
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

    def test_get_phone_finance_payments_shitty_phone(self):
        message = ['Список платежей за период. Запрос для стороннего номера.']
        expected_message = ['Список платежей за период. Запрос для стороннего номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 1545}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введите номер телефона в формате 9001112233."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_week(self):
        message = ['Список платежей за период. Корректный запрос, неделя.']
        expected_message = ['Список платежей за период. Корректный запрос, неделя.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 9006471111,
                  'dateStart': '2022-04-15',
                  'dateEnd': '2022-04-21'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            for i in response.json():
                assert type(i['amount']) == int
                assert type(i['payment_date']) == str
                assert type(i['created_at']) == str
        except AssertionError:
            message.append(f'В параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_month(self):
        message = ['Список платежей за период. Корректный запрос, месяц.']
        expected_message = ['Список платежей за период. Корректный запрос, месяц.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 9006471111,
                  'dateStart': '2022-05-01',
                  'dateEnd': '2022-06-01'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            for i in response.json():
                assert type(i['amount']) == int
                assert type(i['payment_date']) == str
                assert type(i['created_at']) == str
        except AssertionError:
            message.append(f'В параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_month_more(self):
        message = ['Список платежей за период. Корректный запрос, другой период.']
        expected_message = ['Список платежей за период. Корректный запрос, другой период.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 9006471111,
                  'dateStart': '2022-04-10',
                  'dateEnd': '2022-06-08'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            for i in response.json():
                assert type(i['amount']) == int
                assert type(i['payment_date']) == str
                assert type(i['created_at']) == str
        except AssertionError:
            message.append(f'В параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_random_page(self):
        message = ['Список платежей за период. Параметры "page", "per-page".']
        expected_message = ['Список платежей за период. Параметры "page", "per-page".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"

        page = [1, 2, 3]
        per_page = [5, 4, 6]
        for i in per_page:
            for j in page:
                headers = {'accept': 'application/json',
                           'Authorization': f'Bearer {token}'}
                params = {'phone': 9006471111,
                          'dateStart': '2022-04-10',
                          'dateEnd': '2022-06-08',
                          'per-page': i,
                          'page': j}
                response = requests.get(request_url, headers=headers, params=params)

                try:
                    assert response.status_code == 200
                except AssertionError:
                    message.append(f"Код ответа {response.status_code}, а не 200.")
                try:
                    for i in response.json():
                        assert type(i['amount']) == int
                        assert type(i['payment_date']) == str
                        assert type(i['created_at']) == str
                except AssertionError:
                    message.append(f'В параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_fields(self):
        message = ['Список платежей за период. Параметры "fields".']
        expected_message = ['Список платежей за период. Параметры "fields".']

        fields = ['amount', 'payment_date', 'created_at']
        for field in fields:
            token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
            lktest_url = "https://api.lk.bezlimit.ru/v1"
            request_url = f"{lktest_url}/phone/finance/payments/"
            headers = {'accept': 'application/json',
                       'Authorization': f'Bearer {token}'}
            params = {'phone': 9006471111,
                      'dateStart': '2022-04-10',
                      'dateEnd': '2022-06-08',
                      'fields': field}
            response = requests.get(request_url, headers=headers, params=params)

            try:
                assert response.status_code == 200
            except AssertionError:
                message.append(f"Код ответа {response.status_code}, а не 200.")

            for i in response.json():
                if field == 'amount':
                    assert type(i[field]) == int
                else:
                    assert type(i[field]) == str
                short_fields = fields[:]
                short_fields.remove(field)
                try:
                    assert i not in short_fields
                except AssertionError:
                    message.append(f'В параметрах ответа присутствуют исключённые типы данных.')
                    break

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_expand(self):
        message = ['Список платежей за период. Параметры "expand".']
        expected_message = ['Список платежей за период. Параметры "expand".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/finance/payments/"
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        params = {'phone': 9006471111,
                  'dateStart': '2022-04-10',
                  'dateEnd': '2022-06-08',
                  'expand': 'category'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            for i in response.json():
                assert type(i['category']) == dict
                assert type(i['category']['name']) == str
        except AssertionError:
            message.append('Некорректный ответ в параметре "category".')

        assert message == expected_message, message

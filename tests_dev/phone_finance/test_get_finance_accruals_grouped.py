from datetime import datetime, timedelta

import requests
import random

req_url = 'https://lktest.bezlimit.ru/v1/phone/finance/accruals-grouped'
acc_token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
fake_acc_token = 12345678910


def date_generate(days):
    """
    Данная функция генерирует случайные даты в промежутке с 2202-03-01 по текущую дату.
    В переменной функции передаётся количество дней между начальной и конечной датой.
    """
    start = datetime.today() + (datetime.today() - datetime(year=2021, month=3, day=1)) * random.random()
    maxdate = str(start).split()[0]
    maxfiledate = maxdate.split('-')
    maxfiledate.reverse()
    endfiledate = '.'.join(maxfiledate)

    end = start - timedelta(days=days)
    mindate = str(end).split()[0]
    minfiledate = mindate.split('-')
    minfiledate.reverse()
    startfiledate = '.'.join(minfiledate)

    return maxdate, endfiledate, mindate, startfiledate


def sexy_bitches_fucking_with_huge_black_cocks():
    """
    Пример использования сгенерированных дат:
    """
    dates = date_generate(7)
    print(f'\nКонечная дата "maxdate": {dates[0]}'
          f'\nКонечная дата файла "endfiledate": {dates[1]}'
          f'\nНачальная дата "mindate": {dates[2]}'
          f'\nНачальная дата файла "startfiledate": {dates[3]}')


class TestValidation:
    def test_invalid_acc_token(self):
        message = ['Список платежей за период. Неавторизован.']
        expected_message = ['Список платежей за период. Неавторизован.']

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {fake_acc_token}'}
        response = requests.get(req_url, headers=headers)

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

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 9696588825}
        response = requests.get(req_url, headers=headers, params=params)

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

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 1545}
        response = requests.get(req_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введите Номер телефона в формате 9001112233."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_week(self):
        message = ['Список платежей за период. Корректный запрос, неделя.']
        expected_message = ['Список платежей за период. Корректный запрос, неделя.']

        dates = date_generate(7)

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 9006471111,
                  'dateStart': dates[2],
                  'dateEnd': dates[0]}
        response = requests.get(req_url, headers=headers, params=params)

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

        dates = date_generate(30)

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 9006471111,
                  'dateStart': dates[2],
                  'dateEnd': dates[0]}
        response = requests.get(req_url, headers=headers, params=params)

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

        dates = date_generate(71)

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 9006471111,
                  'dateStart': dates[2],
                  'dateEnd': dates[0]}
        response = requests.get(req_url, headers=headers, params=params)

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

        page = [1, 2, 3]
        per_page = [5, 4, 6]
        for i in per_page:
            for j in page:
                headers = {'accept': 'application/json',
                           'Authorization': f'Bearer {acc_token}'}
                params = {'phone': 9006471111,
                          'dateStart': '2022-04-10',
                          'dateEnd': '2022-06-08',
                          'per-page': i,
                          'page': j}
                response = requests.get(req_url, headers=headers, params=params)

                try:
                    assert response.status_code == 200
                except AssertionError:
                    message.append(f"Код ответа {response.status_code}, а не 200.")
                try:
                    for i_s in response.json():
                        assert type(i_s['amount']) == int
                        assert type(i_s['payment_date']) == str
                        assert type(i_s['created_at']) == str
                except AssertionError:
                    message.append(f'В параметрах ответа некорректные типы данных.')

        assert message == expected_message, message

    def test_get_phone_finance_payments_correct_fields(self):
        message = ['Список платежей за период. Параметры "fields".']
        expected_message = ['Список платежей за период. Параметры "fields".']

        fields = ['amount', 'payment_date', 'created_at']
        for field in fields:
            headers = {'accept': 'application/json',
                       'Authorization': f'Bearer {acc_token}'}
            params = {'phone': 9006471111,
                      'dateStart': '2022-04-10',
                      'dateEnd': '2022-06-08',
                      'fields': field}
            response = requests.get(req_url, headers=headers, params=params)

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

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}'}
        params = {'phone': 9006471111,
                  'dateStart': '2022-04-10',
                  'dateEnd': '2022-06-08',
                  'expand': 'category'}
        response = requests.get(req_url, headers=headers, params=params)

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

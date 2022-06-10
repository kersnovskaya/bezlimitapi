import requests


class Test:

    def test_post_phone_finance_payment_sber_invalid_token(self):
        message = ['Пополнение баланса на номере через Сбербанк. Неавторизован.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

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



    def test_post_phone_finance_payment_sber_empty_data(self):
        message = ['Пополнение баланса на номере через Сбербанк. Запрос без данных.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Запрос без данных.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Необходимо заполнить «Phone».'},
                                       {'field': 'amount', 'message': 'Необходимо заполнить «Amount».'}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_finance_payment_sber_lower_summa(self):
        message = ['Пополнение баланса на номере через Сбербанк. Менее 30 р.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Менее 30 р.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 29
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        try:
            assert response.json() == [{"field": "amount",
                                        "message": "Сумма платежа должна быть не менее 30 руб."}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_finance_payment_sber_higher_summa(self):
        message = ['Пополнение баланса на номере через Сбербанк. Более 15000 р.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Более 15000 р.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 15001
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        try:
            assert response.json() == [{"field": "amount",
                                        "message": "Сумма платежа должна быть не более 15000 руб."}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_finance_payment_sber_not_bezlimit_phone(self):
        message = ['Пополнение баланса на номере через Сбербанк. Номер не Безлимит.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Номер не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9000000000,
            "amount": 50
        }

        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

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


    def test_post_phone_finance_payment_sber_side_phone(self):
        message = ['Пополнение баланса на номере через Сбербанк. '
                   'Корректный запрос для стороннего номера аккаунта.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. '
                            'Корректный запрос для стороннего номера аккаунта.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9696588825,
            "amount": 30
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                                   "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True
        except AssertionError:
            message.append('В ответе не отдаётся ссылка на оплату.')

        assert message == expected_message, message


    def test_post_phone_finance_payment_sber_main_phone(self):
        message = ['Пополнение баланса на номере через Сбербанк. Корректный запрос.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Корректный запрос.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                                   "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True
        except AssertionError:
            message.append('В ответе не отдаётся ссылка на оплату.')

        assert message == expected_message, message


    def test_post_phone_finance_payment_sber_with_url(self):
        message = ['Пополнение баланса на номере через Сбербанк. Корректный запрос.']
        expected_message = ['Пополнение баланса на номере через Сбербанк. Корректный запрос.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30,
            "successUrl": "https://bezlimit.ru/payment/?page=success&phone=9006471111&amount=30",
            "failUrl": "https://bezlimit.ru/payment/?page=error&phone=9006471111&amount=30"
        }
        request_url = f"{lktest_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                                   "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True
        except AssertionError:
            message.append('В ответе не отдаётся ссылка на оплату.')

        assert message == expected_message, message

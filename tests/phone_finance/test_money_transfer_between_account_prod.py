import requests


class Test:

    def test_post_phone_finance_money_transfer_between_account_invalid_token(self):
        message = ['Запрос на перевод денег между номерами аккаунта.Неавторизован.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9006471111,
            "phoneTo": 9006471111,
            "amount": 30
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
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
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_both(self):
        message = ['Запрос на перевод денег между номерами аккаунта.Оба номера не Безлимит.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.Оба номера не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9000000000,
            "phoneTo": 9000000000,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneFrom",
                                        "message": "Введенный номер не обслуживается в Безлимит!"},
                                       {"field": "phoneTo",
                                        "message": "Введенный номер не обслуживается в Безлимит!"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_phone_from(self):
        message = ['Запрос на перевод денег между номерами аккаунта.Номер "phone_from" не Безлимит.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Номер "phone_from" не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9000000000,
            "phoneTo": 9006471111,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneFrom",
                                        "message": "Введенный номер не обслуживается в Безлимит!"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_phone_to(self):
        message = ['Запрос на перевод денег между номерами аккаунта.Номер "phone_to" не Безлимит.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Номер "phone_to" не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9000000000,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneTo",
                                        "message": "Введенный номер не обслуживается в Безлимит!"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_in_account_both(self):
        message = ['Запрос на перевод денег между номерами аккаунта.Оба номера не привязаны к аккаунту.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Оба номера не привязаны к аккаунту.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9696588825,
            "phoneTo": 9696588825,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneFrom",
                                        "message": "Номер телефона не привязан к аккаунту."},
                                       {"field": "phoneTo",
                                        "message": "Номер телефона не привязан к аккаунту."}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_in_account_phone_from(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Номер "phone_from" не привязан к аккаунту.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Номер "phone_from" не привязан к аккаунту.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9696588825,
            "phoneTo": 9006471111,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneFrom",
                                        "message": "Номер телефона не привязан к аккаунту."}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_in_account_phone_to(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Номер "phone_to" не привязан к аккаунту.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Номер "phone_to" не привязан к аккаунту.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682224036,
            "phoneTo": 9696588825,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneTo",
                                        "message": "Номер телефона не привязан к аккаунту."}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_without_passport_phone_from(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Номер "phoneFrom" без паспортных данных.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Номер "phoneFrom" без паспортных данных.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682221928,
            "phoneTo": 9682224036,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneFrom",
                                        "message": "Отсутствуют паспортные данные"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_empty_params(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Пустые "params".']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Пустые "params".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'phoneFrom',
                                        'message': 'Необходимо заполнить «Phone From».'},
                                       {'field': 'phoneTo',
                                        'message': 'Необходимо заполнить «Phone To».'},
                                       {'field': 'sum',
                                        'message': 'Необходимо заполнить «Sum».'}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_min_sum(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Сумма в запросе менее 100 р.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Сумма в запросе менее 100 р.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 99
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'sum',
                                        'message': 'Минимальная сумма перевода 100 руб'}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_max_sum(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Сумма в запросе более 3000 р.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Сумма в запросе более 3000 р.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 3001
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'sum',
                                        'message': 'Максимальная сумма перевода 3000 руб'}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_enough_money(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'На балансе недостаточно средств.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'На балансе недостаточно средств.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 3000
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'sum',
                                        'message': 'Не достаточно средств для перевода'}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_not_100(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'После перевода на балансе останется менее 100 р.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'После перевода на балансе останется менее 100 р.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682224036,
            "phoneTo": 9682223055,
            "sum": 351
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'sum',
                                        'message': 'На номере должно остаться больше 100 рублей'}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_same_phones(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   '"phoneFrom" и "phoneTo" совпадают.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            '"phoneFrom" и "phoneTo" совпадают.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682224036,
            "phoneTo": 9682224036,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phoneTo",
                                        "message": "Номер, с которого переводить, "
                                                   "совпадает с номером, которому будет перевод"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_correct(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Корректный запрос.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Корректный запрос.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682224036,
            "phoneTo": 9682223055,
            "sum": 150
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert str(response.json()).startswith("{'money_transfer_token': ")
        except AssertionError:
            message.append('В ответе не отдаётся token.')

        assert message == expected_message, message

    def test_post_phone_finance_money_transfer_between_account_correct_again(self):
        message = ['Запрос на перевод денег между номерами аккаунта.'
                   'Повторный корректный запрос.']
        expected_message = ['Запрос на перевод денег между номерами аккаунта.'
                            'Повторный корректный запрос.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682224036,
            "phoneTo": 9682223055,
            "sum": 150
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert str(response.json()).startswith("{'money_transfer_token': ")
        except AssertionError:
            message.append('В ответе не отдаётся token.')

        assert message == expected_message, message

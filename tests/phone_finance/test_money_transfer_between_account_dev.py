import requests


class Test:

    def test_post_phone_finance_money_transfer_between_account_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9006471111,
            "phoneTo": 9006471111,
            "amount": 30
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {'code': 0,
                                   'message': 'Your request was made with invalid credentials.',
                                   'name': 'Unauthorized',
                                   'status': 401,
                                   'type': 'yii\\web\\UnauthorizedHttpException'}


    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_both(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9000000000,
            "phoneTo": 9000000000,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneFrom",
                                    "message": "Введенный номер не обслуживается в Безлимит!"},
                                   {"field": "phoneTo",
                                    "message": "Введенный номер не обслуживается в Безлимит!"}]


    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_phone_from(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9000000000,
            "phoneTo": 9006471111,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneFrom",
                                    "message": "Введенный номер не обслуживается в Безлимит!"}]


    def test_post_phone_finance_money_transfer_between_account_not_bezlimit_phone_to(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9000000000,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneTo",
                                    "message": "Введенный номер не обслуживается в Безлимит!"}]


    def test_post_phone_finance_money_transfer_between_account_not_in_account_both(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9696588825,
            "phoneTo": 9696588825,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneFrom",
                                    "message": "Номер телефона не привязан к аккаунту."},
                                   {"field": "phoneTo",
                                    "message": "Номер телефона не привязан к аккаунту."}]


    def test_post_phone_finance_money_transfer_between_account_not_in_account_phone_from(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9696588825,
            "phoneTo": 9006471111,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneFrom",
                                    "message": "Номер телефона не привязан к аккаунту."}]


    def test_post_phone_finance_money_transfer_between_account_not_in_account_phone_to(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9696588825,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneTo",
                                    "message": "Номер телефона не привязан к аккаунту."}]


    def test_post_phone_finance_money_transfer_between_account_without_passport_phone_from(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9682221451,
            "phoneTo": 9006471111,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneFrom",
                                    "message": "Отсутствуют паспортные данные"}]


    def test_post_phone_finance_money_transfer_between_account_empty_params(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phoneFrom',
                                    'message': 'Необходимо заполнить «Phone From».'},
                                   {'field': 'phoneTo',
                                    'message': 'Необходимо заполнить «Phone To».'},
                                   {'field': 'sum',
                                    'message': 'Необходимо заполнить «Sum».'}]


    def test_post_phone_finance_money_transfer_between_account_min_sum(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 99
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'sum',
                                    'message': 'Минимальная сумма перевода 100 руб'}]


    def test_post_phone_finance_money_transfer_between_account_max_sum(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 3001
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'sum',
                                    'message': 'Максимальная сумма перевода 3000 руб'}]


    def test_post_phone_finance_money_transfer_between_account_not_enough_money(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 3000
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'sum',
                                    'message': 'Не достаточно средств для перевода'}]


    def test_post_phone_finance_money_transfer_between_account_not_100(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 750
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'sum',
                                    'message': 'На номере должно остаться больше 100 рублей'}]


    def test_post_phone_finance_money_transfer_between_account_same_phones(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9032417766,
            "sum": 100
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phoneTo",
                                    "message": "Номер, с которого переводить, "
                                               "совпадает с номером, которому будет перевод"}]


    def test_post_phone_finance_money_transfer_between_account_correct(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 150
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert str(response.json()).startswith("{'money_transfer_token': ")


    def test_post_phone_finance_money_transfer_between_account_correct_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phoneFrom": 9032417766,
            "phoneTo": 9006471111,
            "sum": 150
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-between-account-phones"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert str(response.json()).startswith("{'money_transfer_token': ")

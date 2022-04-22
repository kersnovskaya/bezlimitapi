import requests


class Test:

    def test_post_phone_finance_payment_sber_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {
                                    'name': 'Unauthorized',
                                    'message': 'Your request was made with invalid credentials.',
                                    'code': 0,
                                    'status': 401
                                    }


    def test_post_phone_finance_payment_sber_empty_data(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Необходимо заполнить «Phone».'},
                                   {'field': 'amount', 'message': 'Необходимо заполнить «Amount».'}]


    def test_post_phone_finance_payment_sber_lower_summa(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 29
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "amount",
                                    "message": "Сумма платежа должна быть не менее 30 руб."}]



    def test_post_phone_finance_payment_sber_higher_summa(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 15001
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "amount",
                                    "message": "Сумма платежа должна быть не более 15000 руб."}]


    def test_post_phone_finance_payment_sber_invalid_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9000000000,
            "amount": 50
        }

        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': "Введенный номер не обслуживается в Безлимит!"}]


    def test_post_phone_finance_payment_sber_side_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9696588825,
            "amount": 30
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(str(response.json()))

        assert response.status_code == 200
        assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                               "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True


    def test_post_phone_finance_payment_sber_main_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(str(response.json()))

        assert response.status_code == 200
        assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                               "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True


    def test_post_phone_finance_payment_sber_with_url(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "amount": 30,
            "successUrl": "https://bezlimit.ru/payment/?page=success&phone=9006471111&amount=30",
            "failUrl": "https://bezlimit.ru/payment/?page=error&phone=9006471111&amount=30"
        }
        request_url = f"{lk_url}/phone/finance/payment-sber"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(str(response.json()))

        assert response.status_code == 200
        assert str(response.json()).startswith("{'redirectUrl': 'https://securepayments.sberbank.ru/payment"
                                               "/merchants/sbersafe_sberid/payment_ru.html?mdOrder=") is True

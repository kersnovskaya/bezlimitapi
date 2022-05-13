import requests

class Test:

    def test_put_phone_tariff_change_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930,
            "tariffId": 8014
        }
        request_url = f"{lktest_url}/phone/tariff/change"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {
                                    'name': 'Unauthorized',
                                    'message': 'Your request was made with invalid credentials.',
                                    'code': 0,
                                    'status': 401
                                    }


    def test_put_phone_tariff_change_invalid_tariff_id(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930,
            "tariffId": 1488
        }
        request_url = f"{lktest_url}/phone/tariff/change"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "tariffId",
                                    "message": "Нельзя перейти на этот тариф."
                                    }]


    def test_put_phone_tariff_change_invalid_phone(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9696588825,
            "tariffId": 8014
        }
        request_url = f"{lktest_url}/phone/tariff/change"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phone",
                                    "message": "Номер не привязан к аккаунту."
                                    }]


    def test_put_phone_tariff_change_valid_credentials(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930,
            "tariffId": 8014
        }
        request_url = f"{lktest_url}/phone/tariff/change"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert response.json() is not None


    def test_put_phone_tariff_change_valid_credentials_duplicate(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930,
            "tariffId": 8014
        }
        request_url = f"{lktest_url}/phone/tariff/change"
        response = requests.get(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'tariffId',
                                    'message': 'Заявка на смену тарифного плана была отправлена ранее. Смена '
                                    'тарифного плана будет осуществлена с 1 по 5-е число месяца. На '
                                    'момент смены тарифного плана номер должен быть активен. В случае '
                                    'если на момент смены тарифного плана номер находился в статусе '
                                    '"Блокирован", заявка на смену тарифного плана будет отклонена. О '
                                    'смене тарифного плана поступит SMS-уведомление.'}]


    def test_put_phone_tariff_cancel_invalid_token(self):
        token = 12345678910
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930
        }
        request_url = f"{lktest_url}/phone/tariff/cancel-change"
        response = requests.put(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {
                                    'name': 'Unauthorized',
                                    'message': 'Your request was made with invalid credentials.',
                                    'code': 0,
                                    'status': 401
                                    }


    def test_put_phone_tariff_cancel_invalid_credentials(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9696588825
        }
        request_url = f"{lktest_url}/phone/tariff/cancel-change"
        response = requests.put(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phone",
                                    "message": "Номер телефона не привязан к аккаунту."
                                    }]


    def test_put_phone_tariff_cancel_valid_credentials(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930
        }
        request_url = f"{lktest_url}/phone/tariff/cancel-change"
        response = requests.put(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 200
        assert response.json() is None


    def test_put_phone_tariff_cancel_without_application(self):
        token = 'g6w9Csyh-yhrZQTcXjDEJ9-5kLqqJDNDKpAllfprIG3J8fk2WX8rqCRFIJxD3cJ6'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9612224930
        }
        request_url = f"{lktest_url}/phone/tariff/cancel-change"
        response = requests.put(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phone",
                                    "message": "Заявка на смену тарифа не найдена"}]



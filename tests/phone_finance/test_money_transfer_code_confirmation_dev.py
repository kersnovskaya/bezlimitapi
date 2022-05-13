import requests


def get_transfer_token(phone_from, phone_to):
    token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
    headers = {'accept': 'application/json',
                'Authorization': f'Bearer {token}',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    lktest_url = "https://lktest.bezlimit.ru/v1"
    data = {
        "phoneFrom": phone_from,
        "phoneTo": phone_to,
        "sum": 150
    }
    request_url = f"{lktest_url}/phone/finance/money-transfer-client-bezlimit"
    response = requests.post(request_url, headers=headers, data=data)
    money_transfer_token = str(response.json()['money_transfer_token'])

    return money_transfer_token


def get_code(phone_from):
    token = 'Z1RseVcn9twtKLY84eYQf57Pw8ENZ1yks436TJHXaC2dJhcRZLJ2mGsgRBpTuFp7'
    url = "https://api.bezlimit.ru/v1"
    headers = {'accept': 'application/json',
               'Api-Token': token}
    params = {'phone': int(phone_from)}
    request_url = f"{url}/queue/sms"
    response = requests.get(request_url, headers=headers, params=params)
    asshole = response.json()

    for i in asshole['items']:
        raw_code = i['text']
        code = raw_code[-6::]
        break

    return code


class TestDev:


    def test_post_transfer_code_confirmation_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "moneyTransferToken": '',
            "code": 123456
        }
        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {'code': 0,
                                   'message': 'Your request was made with invalid credentials.',
                                   'name': 'Unauthorized',
                                   'status': 401,
                                   'type': 'yii\\web\\UnauthorizedHttpException'}


    def test_post_transfer_code_confirmation_invalid_data(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "moneyTransferToken": 123546,
            "code": '123456'
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)

        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'money_transfer_token',
                                    'message': 'Запрос на перевод денег не найден.'}]


    def test_post_transfer_code_confirmation_invalid_code(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "moneyTransferToken": 123546,
            "code": '123456'
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)

        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'money_transfer_token',
                                    'message': 'Запрос на перевод денег не найден.'}]



    def test_post_transfer_code_confirmation_correct_and_incorrect(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        transfer_token = get_transfer_token(9682223055, 9682224036)
        code = get_code(9682223055)

        data1 = {
            "moneyTransferToken": transfer_token,
            "code": 100000
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data1)

        print(response.json())
        assert response.status_code == 422
        assert response.json() == [{"field": "code", "message": "Неправильный код подтверждения."}]

        data2 = {
            "moneyTransferToken": transfer_token,
            "code": code
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data2)

        print(response)
        assert response.status_code == 204

    def test_post_transfer_code_confirmation_correct_and_incorrect_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        transfer_token = get_transfer_token(9682224036, 9682223055)
        code = get_code(9682224036)

        data1 = {
            "moneyTransferToken": transfer_token,
            "code": 100000
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data1)

        print(response.json())
        assert response.status_code == 422
        assert response.json() == [{"field": "code", "message": "Неправильный код подтверждения."}]

        data2 = {
            "moneyTransferToken": transfer_token,
            "code": code
        }

        request_url = f"{lktest_url}/phone/finance/money-transfer-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data2)

        print(response)

        assert response.status_code == 204

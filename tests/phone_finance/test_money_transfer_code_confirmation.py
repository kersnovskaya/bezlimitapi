import requests


def get_code():
    phone = 9682220854
    token = 'Z1RseVcn9twtKLY84eYQf57Pw8ENZ1yks436TJHXaC2dJhcRZLJ2mGsgRBpTuFp7'
    url = "https://api.bezlimit.ru/v1"
    headers = {'accept': 'application/json',
               'Api-Token': token}
    params = {'phone': int(phone)}
    request_url = f"{url}/queue/sms"
    response = requests.get(request_url, headers=headers, params=params)
    asshole = response.json()
    print(asshole)
    for i in asshole['items']:
        raw_code = i['text']
        code = raw_code[-6::]
        break

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

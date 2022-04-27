import requests

class Test:

    def test_post_phone_finance_money_transfer_between_account_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/finance/money-transfer-allowed-phones-from"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {'code': 0,
                                   'message': 'Your request was made with invalid credentials.',
                                   'name': 'Unauthorized',
                                   'status': 401,
                                   'type': 'yii\\web\\UnauthorizedHttpException'}


    def test_post_phone_finance_money_transfer_between_account(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/finance/money-transfer-allowed-phones-from"
        response = requests.post(request_url, headers=headers)
        des_response = response.json()
        print(response)
        print(des_response)

        assert response.status_code == 200
        for i in des_response:
            assert type(i["phone"]) == int
            assert i["phone"] >= 200
            assert type(i["balance"]) == float or type(i["balance"]) == int
            assert type(i["name"]) == str or type(i["name"]) is not None


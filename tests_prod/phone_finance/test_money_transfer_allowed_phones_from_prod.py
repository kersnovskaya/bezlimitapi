import requests


class TestProd:

    def test_post_phone_finance_money_transfer_between_account_invalid_token(self):
        message = ['Список номеров из аккаунта, с которых можно переводить деньги. Неавторизован.']
        expected_message = ['Список номеров из аккаунта, с которых можно переводить деньги. Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/finance/money-transfer-allowed-phones-from"
        response = requests.post(request_url, headers=headers)

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


    def test_post_phone_finance_money_transfer_between_account(self):
        message = ['Список номеров из аккаунта, с которых можно переводить деньги. Корректный запрос.']
        expected_message = ['Список номеров из аккаунта, с которых можно переводить деньги. Корректный запрос.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/finance/money-transfer-allowed-phones-from"
        response = requests.post(request_url, headers=headers)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            for i in des_response:
                assert type(i["phone"]) == int
                assert i["phone"] >= 200
                assert type(i["balance"]) == float or type(i["balance"]) == int
                assert type(i["name"]) == str or type(i["name"]) is not None
        except AssertionError:
            message.append('Некорректные типы данных в параметре ответа.')

        assert message == expected_message, message

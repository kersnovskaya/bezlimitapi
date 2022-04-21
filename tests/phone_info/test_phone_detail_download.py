import requests
from lkapi.configuration.config import TOKEN_9006471111


class Test:

    def test_get_phone_detail_download_correct_credentials_type_0(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)

        assert response.status_code == 200


    def test_get_phone_detail_download_correct_credentials_type_1(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2021-12-01",
            "periodEnd": "2022-02-01",
            "type": "1"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)

        assert response.status_code == 200


    def test_get_phone_detail_download_correct_credentials_type_2(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2022-03-07",
            "periodEnd": "2022-04-19",
            "type": "2"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)

        assert response.status_code == 200


    def test_get_phone_detail_download_non_bezlimit_number(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9000000000,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Введенный номер не обслуживается в Безлимит!'}]


    def test_get_phone_detail_download_wrong_number(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9696588825,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Номер телефона не привязан к аккаунту.'}]


    def test_get_phone_detail_download_over_three_months(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-04-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'periodEnd',
                                    'message': 'Период детализации не должен превышать 3 месяца.'}]


    def test_get_phone_detail_download_wrong_params(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 806471111,
            "periodStart": "01-01-2022",
            "periodEnd": "04-2022-01",
            "type": "5"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Введите номер телефона в формате 9001112233.'},
                                   {'field': 'periodStart', 'message': 'Дата должна быть в формате Y-m-d'},
                                   {'field': 'periodEnd', 'message': 'Дата должна быть в формате Y-m-d'},
                                   {'field': 'type', 'message': 'Разрешенные типы детализаций: 0, 1, 2'}]


    def test_get_phone_detail_download_empty_params(self):
        token = TOKEN_9006471111
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": "",
            "periodStart": "",
            "periodEnd": "",
            "type": ""
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 400
        assert response.json() == {'name': 'Bad Request',
                                   'message': 'Неправильное значение параметра "phone".',
                                   'code': 0,
                                   'status': 400,
                                   'type': 'yii\\web\\BadRequestHttpException'}

import requests


class Test:

    def test_post_phone_download_agreement_invalid_token(self):
        token = 12345678910
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {"phone": 9006471111}
        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {
                                    'name': 'Unauthorized',
                                    'message': 'Your request was made with invalid credentials.',
                                    'code': 0,
                                    'status': 401
                                    }


    def test_post_phone_download_agreement_empty_params(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 400
        assert response.json() == {'code': 0,
                                   'message': 'Отсутствуют обязательные параметры: phone',
                                   'name': 'Bad Request',
                                   'status': 400}


    def test_post_phone_download_agreement_incorrect_number(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {"phone": 9000000000}
        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone',
                                    'message': 'Введенный номер не обслуживается в Безлимит!'}]


    def test_post_phone_download_agreement_non_account_number(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {"phone": 9696588825}
        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{"field": "phone",
                                    "message": "Номер телефона не привязан к аккаунту."}]


    def test_post_phone_download_agreement_correct_number(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {"phone": 9006471111}
        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers, params=data)
        print(response.status_code)

        assert response.status_code == 200


    def test_post_phone_download_agreement_too_long_number(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {token}'}
        lk_url = "https://api.lk.bezlimit.ru/v1"
        data = {"phone": 9006471111566481516846165168461}
        request_url = f"{lk_url}/phone/info/download-user-service-agreement"
        response = requests.post(request_url, headers=headers, params=data)
        print(response)
        print(response.json())

        assert response.status_code == 400
        assert response.json() == {'code': 0,
                                   'message': 'Неправильное значение параметра "phone".',
                                   'name': 'Bad Request',
                                   'status': 400}

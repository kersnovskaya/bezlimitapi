import requests

class Test:

    def test_successful_getting_state_at_lk(self):
        phone = 9006471111
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['channel'] in ('telegram', 'viber', 'push')
            assert i['name'] in ('Telegram', 'Viber', 'Push-уведомления')
            assert i['isConnected'] is not None
            assert i['isAwaitingConfirmation'] is not None


    def test_validation_getting_state_to_side_phone_at_lk(self):
        phone = 9696588825
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Номер телефона не привязан к аккаунту.'


    def test_validation_getting_state_to_wrong_phone_at_lk(self):
        phone = 9696588
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'


    def test_validation_getting_state_to_not_numeric_phone_at_lk(self):
        phone = '♂CUM♂mit'
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert type(response.json()) == dict
        assert response.json()['message'] == 'Неправильное значение параметра "phone".'


    def test_unsuccessful_getting_notifications_without_token_at_lk(self):
        phone = '♂CUM♂mit'
        token = 12345678910
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'




import requests


class TestDev:

    def test_successful_request_for_reset_password_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 201
        assert type(response.json()) == dict
        assert type(response.json()['sending_repeated_notify']) == int

    def test_validation_request_for_reset_password_to_side_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9614828609  # side_phone аккаунта 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, ' \
                                                'с которого зарегистрирован аккаунт.'

    def test_validation_request_for_reset_password_to_second_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9654513918  # side_phone аккаунта 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, ' \
                                                'с которого зарегистрирован аккаунт.'

    def test_validation_request_for_reset_password_to_not_bezlimit_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000000
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_validation_request_for_reset_password_to_wrong_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_validation_request_for_reset_password_to_non_numeric_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        params = {'phone': 'dick'}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert type(response.json()) == dict
        assert response.json()['message'] == 'Неправильное значение параметра "phone".'

    def test_validation_request_for_reset_password_to_empty_phone_at_lk(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert type(response.json()) == dict
        assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'


class TestProd:

    def test_successful_request_for_reset_password_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 201
        assert type(response.json()) == dict
        assert type(response.json()['sending_repeated_notify']) == int

    def test_validation_request_for_reset_password_to_side_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        phone = 9614828609  # side_phone аккаунта 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, ' \
                                                'с которого зарегистрирован аккаунт.'

    def test_validation_request_for_reset_password_to_second_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        phone = 9654513918  # side_phone аккаунта 9006471111
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, ' \
                                                'с которого зарегистрирован аккаунт.'

    def test_validation_request_for_reset_password_to_not_bezlimit_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000000
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_validation_request_for_reset_password_to_wrong_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        phone = 9000000
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert response.json()[0]['field'] == 'phone'
        assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_validation_request_for_reset_password_to_non_numeric_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        params = {'phone': 'dick'}
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert type(response.json()) == dict
        assert response.json()['message'] == 'Неправильное значение параметра "phone".'

    def test_validation_request_for_reset_password_to_empty_phone_at_lk(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        headers = {"accept": "application/json"}

        request_url = f'{lk_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert type(response.json()) == dict
        assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'

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
        phone = 9614828609
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
        params = {'phone': self.second_phone}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'

    def test_validation_request_for_reset_password_to_not_bezlimit_phone_at_lk(self):
        params = {'phone': 9159601590}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_validation_request_for_reset_password_to_wrong_phone_at_lk(self):
        params = {'phone': 96822249181}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_validation_request_for_reset_password_to_non_numeric_phone_at_lk(self):
        params = {'phone': 'dick'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 400
        assert res.get_reason() == 'Bad Request'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Неправильное значение параметра "phone".'

    def test_validation_request_for_reset_password_to_empty_phone_at_lk(self):
        params = {'phone': None}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 400
        assert res.get_reason() == 'Bad Request'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Отсутствуют обязательные параметры: phone'

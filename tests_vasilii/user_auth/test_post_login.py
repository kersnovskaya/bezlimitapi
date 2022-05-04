from lkapi.base_app.baseapp import Request
from lkapi.configuration.config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/user/auth/login'

    def test_successful_authorization_at_lk(self):
        data = {'phone': self.phone,
                'password': self.password}

        req = Request('POST', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_content()['access_token']

    def test_authorization_without_password_at_lk(self):
        data = {'phone': self.phone}

        req = Request('POST', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_content()[0]['field'] == 'password'
        assert res.get_content()[0]['message'] == 'Введите пароль'

    def test_authorization_with_wrong_password_at_lk(self):
        data = {'phone': self.phone,
                'password': self.password + 'dick'}

        req = Request('POST', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_content()[0]['field'] == 'password'
        assert res.get_content()[0]['message'] == 'Пароль для аккаунта указан не верно.'

    def test_authorization_without_phone_and_password_at_lk(self):
        data = {}

        req = Request('POST', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Не указан номер телефона.'
        assert res.get_content()[1]['field'] == 'password'
        assert res.get_content()[1]['message'] == 'Введите пароль'

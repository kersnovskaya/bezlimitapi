import pytest

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE, TEST_SECOND_PHONE


class Test:

    phone = TEST_PHONE
    side_phone = TEST_SIDE_PHONE
    second_phone = TEST_SECOND_PHONE
    password = PASSWORD
    endpoint = '/user/auth/request-password-reset/'

    def test_successful_request_for_reset_password_at_lk(self):
        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 201
        assert type(res.get_content()) == dict
        assert type(res.get_content()['sending_repeated_notify']) == int

    def test_validation_request_for_reset_password_to_side_phone_at_lk(self):
        params = {'phone': 9682224918}  # Было: self.side_phone
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'

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

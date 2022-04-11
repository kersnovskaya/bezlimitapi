import pytest

from baseApp import Request
from config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/user/auth/is-registered-phone/'

    def test_successful_check_main_phone_registration_at_lk(self):
        params = {'phone': TEST_PHONE}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Номер был найден в системе "Безлимит ID". ' \
                                               'Если вы являетесь пользователем Store Безлимит ' \
                                               'вы можете авторизоваться используя данный пароль.'

    def test_successful_check_side_phone_registration_at_lk(self):
        params = {'phone': 9682224918}  # Потом необходимо будет заменить
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 201
        assert type(res.get_content()) == dict
        assert type(res.get_content()['sending_repeated_notify']) == int

    def test_validation_check_not_bezlimit_phone_registration_at_lk(self):
        params = {'phone': 9159601590}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_validation_check_wrong_format_phone_registration_at_lk(self):
        params = {'phone': 89159601590}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Введите номер телефона в формате 9001112233.'

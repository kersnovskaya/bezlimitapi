import pytest

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE, TEST_SECOND_PHONE


class Test:

    endpoint = '/system/check-version'
    actual_version = '1.7.0'

    def test_successful_check_actual_ios_version_at_lk(self):
        params = {'system': 'ios',
                  'version': self.actual_version}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert res.get_content()['force_update'] is False
        assert res.get_content()['remind_about_updates'] == 0

    def test_successful_check_actual_android_version_at_lk(self):
        params = {'system': 'android',
                  'version': self.actual_version}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert res.get_content()['force_update'] is False
        assert res.get_content()['remind_about_updates'] == 0

    def test_successful_check_not_actual_version_at_lk(self):
        params = {'system': 'android',
                  'version': '0.9.0'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert res.get_content()['force_update'] is True
        assert type(res.get_content()['remind_about_updates']) == int

    def test_validation_check_version_with_wrong_system_at_lk(self):
        params = {'system': 'androidick',
                  'version': '0.9.0'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'system'
        assert res.get_content()[0]['message'] == 'Значение «System» неверно.'

    def test_validation_check_version_without_system_at_lk(self):
        params = {'system': None,
                  'version': '0.9.0'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'system'
        assert res.get_content()[0]['message'] == 'Укажите тип ОС приложения.'

    def test_validation_check_version_without_version_at_lk(self):
        params = {'system': 'android',
                  'version': None}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'version'
        assert res.get_content()[0]['message'] == 'Укажите версию приложения.'

    def test_validation_check_version_with_wrong_version_at_lk(self):
        params = {'system': 'android',
                  'version': '0'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'version'
        assert res.get_content()[0]['message'] == 'Версия приложения должна быть в диапазоне от 1.0.0 до 99.999.999.'

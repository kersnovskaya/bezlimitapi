import pytest
import random

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD, TEST_SECOND_PHONE, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    second_phone = TEST_SECOND_PHONE
    side_phone = TEST_SIDE_PHONE
    password = PASSWORD
    endpoint = '/phone/tariff/available/'

    def test_successful_getting_available_tariffs_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(self.phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert type(i['id']) == int
            assert i['name']

    def test_successful_getting_available_tariffs_for_second_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(self.second_phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert type(i['id']) == int
            assert i['name']

    def test_unsuccessful_getting_available_tariffs_for_side_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(self.side_phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Номер телефона не подтвержден.'

    def test_unsuccessful_getting_available_tariffs_for_wrong_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(917980661313)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_unsuccessful_getting_available_tariffs_not_bezlimit_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(9179806613)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
        self.endpoint += str(self.side_phone)
        headers = {}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

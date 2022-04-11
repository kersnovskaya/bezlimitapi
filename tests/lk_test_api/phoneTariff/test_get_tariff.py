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
    endpoint = '/phone/tariff/'

    def test_successful_getting_tariff_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(self.phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert type(res.get_content()['id']) == int
        assert res.get_content()['name'] is not None

    def test_successful_getting_tariff_for_second_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(self.second_phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert type(res.get_content()['id']) == int
        assert res.get_content()['name'] is not None

    def test_successful_getting_tariff_with_one_random_field_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        queries_fields = ['id', 'name', 'subscription_fee', 'packet_minutes', 'packet_sms', 'packet_internet']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        self.endpoint += str(self.second_phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {'fields': random_field}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert len(res.get_content()) == 1
        assert res.get_content()[random_field]

    def test_successful_getting_tariff_with_adding_random_expand_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        queries_fields = ['description']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        self.endpoint += str(self.second_phone)
        headers = {'Authorization': f'Bearer {token}'}
        params = {'expand': random_field}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        assert res.get_content()[random_field]

    def test_unsuccessful_getting_tariff_for_side_phone_at_lk(self):
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

    def test_unsuccessful_getting_tariff_for_not_bezlimit_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        self.endpoint += str(9169743241)
        headers = {'Authorization': f'Bearer {token}'}
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_unsuccessful_getting_tariff_at_lk_without_token(self):
        self.endpoint += str(self.side_phone)
        params = {}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

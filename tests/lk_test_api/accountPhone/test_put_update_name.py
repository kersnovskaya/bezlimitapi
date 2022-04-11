import pytest
import random

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD, TEST_SECOND_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    second_phone = TEST_SECOND_PHONE
    endpoint = '/account/phone/update-name'

    def test_successful_change_random_name_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        names = ['GYM', 'DUNGEON', 'CUM', 'FISTING IS 300 BUCKS', 'DEEP DARK FANTASY']
        random_name = names[random.randrange(0, len(names), 1)]
        data = {'phone': self.phone,
                'name': random_name}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert res.get_content()['name'] == random_name

    def test_successful_change_empty_name_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.phone}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert res.get_content()['name'] is None

    def test_validation_change_name_with_too_long_name_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.phone,
                'name': 'FISTING IS 300 BUCKS FOR SLAVES'}  # 31 chars

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'name'
        assert res.get_content()[0]['message'] == 'Максимум 30 символов.'

    def test_validation_change_name_with_wrong_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.second_phone+1,
                'name': 'FISTING IS 300 BUCKS FOR SLAVE'}  # 30 chars

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Номер телефона не привязан к аккаунту.'

    def test_validation_change_name_with_no_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'name': 'FISTING IS 300 BUCKS FOR SLAVE'}  # 30 chars

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Не указан номер телефона.'

    def test_change_name_without_token_at_lk(self):
        data = {'phone': self.second_phone,
                'name': 'GYM'}

        req = Request('PUT', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

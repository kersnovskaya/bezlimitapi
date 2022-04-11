import random

from api.baseapp import Request
from api.get_token import get_access_token
from config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/phone/manage/secret-key'

    def test_successful_change_secret_key_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        data_fields = ['DICK', 'FAT_COCK', 'SEMEN', 'DEEP_DARK_FANTASY', 'ASS', 'FISTING_IS_300_BUCKS']
        random_field = data_fields[random.randrange(0, len(data_fields), 1)]

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.phone,
                'secretKey': random_field}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert res.get_content()['phoneInfo']['secret_key'] == random_field

    def test_validation_change_secret_key_with_empty_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': None,
                'secretKey': 'SEMEN'}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Не указан номер телефона.'

    def test_validation_change_secret_key_with_empty_key_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.phone,
                'secretKey': None}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'secretKey'
        assert res.get_content()[0]['message'] == 'Необходимо заполнить «Секретное слово».'

    def test_validation_change_secret_key_with_too_short_key_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.phone,
                'secretKey': 'AS'}  # 2 chars

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'secretKey'
        assert res.get_content()[0]['message'] == 'Значение «Секретное слово» должно содержать минимум 3 символа.'

    def test_change_secret_key_without_token_at_lk(self):
        data_fields = ['DICK', 'FAT_COCK', 'SEMEN', 'DEEP_DARK_FANTASY', 'ASS', 'FISTING_IS_300_BUCKS']
        random_field = data_fields[random.randrange(0, len(data_fields), 1)]

        data = {'phone': self.phone,
                'secretKey': random_field}

        req = Request('PUT', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

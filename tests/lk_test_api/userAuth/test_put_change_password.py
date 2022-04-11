import pytest

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/user/auth/change-password'

    def test_successful_change_password_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'password': self.password,
                'newPassword': self.password+'dick',
                'newPasswordRepeat': self.password+'dick'}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200

        data = {'password': self.password+'dick',
                'newPassword': self.password,
                'newPasswordRepeat': self.password}

        req_return_password = Request('PUT', endpoint=self.endpoint,
                                      headers=headers, data=data)

        res2 = req_return_password.make_request_to_endpoint()

        assert res2.get_status_code() == 200

    def test_validation_change_password_with_no_repeat_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'password': self.password,
                'newPassword': self.password+'dick',
                'newPasswordRepeat': self.password+'pussy'}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'newPassword'
        assert res.get_content()[0]['message'] == 'Введеные пароли не совпадают!'

    def test_validation_change_password_with_wrong_password_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'password': self.password+'dick',
                'newPassword': self.password+'dick',
                'newPasswordRepeat': self.password+'dick'}

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'password'
        assert res.get_content()[0]['message'] == 'Неверно указан старый пароль.'

    def test_validation_change_password_with_too_short_password_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'password': self.password,
                'newPassword': 'Dick123',
                'newPasswordRepeat': 'Dick123'}  # 7 chars

        req = Request('PUT', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'newPassword'
        assert res.get_content()[0]['message'] == 'Пароль должен быть не менее 8 символов.'
        assert res.get_content()[1]['field'] == 'newPasswordRepeat'
        assert res.get_content()[1]['message'] == 'Пароль должен быть не менее 8 символов.'

    def test_change_password_without_token_at_lk(self):
        data = {'password': self.password,
                'newPassword': self.password+'dick',
                'newPasswordRepeat': self.password+'dick'}

        req = Request('PUT', endpoint=self.endpoint,
                      data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

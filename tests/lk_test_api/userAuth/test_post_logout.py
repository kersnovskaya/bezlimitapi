import pytest

from baseapp import Request
from get_token import get_access_token
from config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/user/auth/logout'

    def test_successful_logout_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200

    def test_unsuccessful_logout_without_token_at_lk(self):
        req = Request('POST', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

    def test_logout_with_wrong_token_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers)

        res1 = req.make_request_to_endpoint()

        res2 = req.make_request_to_endpoint()

        assert res1.get_content() == res2.get_content()

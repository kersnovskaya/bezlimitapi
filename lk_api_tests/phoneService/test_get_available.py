import pytest

from baseapp import Request
from get_token import get_access_token
from config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    side_phone = TEST_SIDE_PHONE
    endpoint = '/phone/service/available/'

    def test_successful_getting_available_service_list_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert type(i['id']) == int
            assert type(i['title']) == str
            assert type(i['short_description']) == str
            assert type(i['description']) == str
            assert type(i['connection_cost']) == str

    def test_unsuccessful_getting_available_service_list_without_token_at_lk(self):
        req = Request('GET', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

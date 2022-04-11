import pytest

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    side_phone = TEST_SIDE_PHONE
    endpoint = '/phone/notify/count-new-notifications'

    def test_successful_getting_count_new_notifications_to_one_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_without_token_at_lk(self):
        req = Request('GET', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

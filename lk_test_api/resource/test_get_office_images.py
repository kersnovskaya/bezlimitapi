import pytest

from baseapp import Request
from get_token import get_access_token
from config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE, TEST_SECOND_PHONE


class Test:

    endpoint = '/resource/office-images'

    def test_successful_check_actual_ios_version_at_lk(self):
        req = Request('GET', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert i['url'] is not None


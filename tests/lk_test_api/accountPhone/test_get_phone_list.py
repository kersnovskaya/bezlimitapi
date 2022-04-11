import pytest
import random

from lkapi.baseapp import Request
from lkapi.get_token import get_access_token
from lkapi.config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/account/phone'

    def test_successful_getting_phone_list_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        assert res.get_content()[0]['phone'] == TEST_PHONE

        head = res.get_headers()
        assert head['X-Pagination-Total-Count'] and \
               head['X-Pagination-Page-Count'] and \
               head['X-Pagination-Current-Page']
        assert head['X-Pagination-Per-Page'] == '10'

    def test_getting_phone_list_with_one_random_query_field_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        queries_fields = ['phone', 'name', 'is_disable_delete', 'is_adding_confirmed']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        headers = {'Authorization': f'Bearer {token}'}
        params = {'fields': random_field}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        assert set([len(i) for i in res.get_content()]) == {1}
        assert all([i.get(random_field, None) for i in res.get_content()]) is not None

    def test_getting_phone_list_with_one_query_expand_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        params = {'expand': 'phoneInfo'}

        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        assert all([i.get('phoneInfo', None) for i in res.get_content()]) is not None

    def test_unsuccessful_getting_phone_list_without_token_at_lk(self):
        req = Request('GET', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

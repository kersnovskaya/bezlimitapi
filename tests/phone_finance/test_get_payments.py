from lkapi.base_app.baseapp import Request
from lkapi.tokenmethod.get_token import get_access_token
from lkapi.configuration.config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/phone/finance/payments/'

    def test_successful_getting_payments_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list

    def test_unsuccessful_getting_payments_without_token_at_lk(self):
        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

    """
    Продолжение следует
    """

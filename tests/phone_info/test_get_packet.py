from api.baseapp import Request
from api.get_token import get_access_token
from config import TEST_PHONE, PASSWORD


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    endpoint = '/phone/info/packet/'

    def test_successful_getting_packet_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == dict
        for i in res.get_content():
            assert res.get_content()[i]['value'] is not None
            assert res.get_content()[i]['limit'] is not None

    def test_validation_getting_packet_to_not_bezlimit_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': 9159601590}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_validation_getting_packet_to_wrong_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': 96822249181}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 404
        assert res.get_reason() == 'Not Found'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_validation_getting_packet_to_non_numeric_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': 'dick'}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 400
        assert res.get_reason() == 'Bad Request'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Неправильное значение параметра "phone".'

    def test_validation_getting_packet_to_empty_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': None}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 400
        assert res.get_reason() == 'Bad Request'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Отсутствуют обязательные параметры: phone'

    def test_unsuccessful_getting_phone_list_without_token_at_lk(self):
        req = Request('GET', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

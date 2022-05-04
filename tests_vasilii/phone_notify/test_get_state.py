from lkapi.base_app.baseapp import Request
from lkapi.tokenmethod.get_token import get_access_token
from lkapi.configuration.config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    side_phone = TEST_SIDE_PHONE
    endpoint = '/phone/notify/state/'

    def test_successful_getting_state_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      headers=headers, params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 200
        assert type(res.get_content()) == list
        for i in res.get_content():
            assert i['channel'] in ('telegram', 'viber', 'push')
            assert i['name'] in ('Telegram', 'Viber', 'Push-уведомления')
            assert i['isConnected'] is not None
            assert i['isAwaitingConfirmation'] is not None

    def test_validation_getting_state_to_side_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': self.side_phone}
        req = Request('GET', endpoint=self.endpoint,
                      params=params, headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Номер телефона не подтвержден.'

    def test_validation_getting_state_to_wrong_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': 96822249181}
        req = Request('GET', endpoint=self.endpoint,
                      params=params, headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_validation_getting_state_to_not_numeric_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}

        params = {'phone': 'dick'}
        req = Request('GET', endpoint=self.endpoint,
                      params=params, headers=headers)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 400
        assert res.get_reason() == 'Bad Request'
        assert type(res.get_content()) == dict
        assert res.get_content()['message'] == 'Неправильное значение параметра "phone".'

    def test_unsuccessful_getting_notifications_without_token_at_lk(self):
        params = {'phone': self.phone}
        req = Request('GET', endpoint=self.endpoint,
                      params=params)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

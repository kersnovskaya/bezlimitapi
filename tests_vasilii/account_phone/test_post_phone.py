from lkapi.base_app.baseapp import Request
from lkapi.tokenmethod.get_token import get_access_token
from lkapi.configuration.config import TEST_PHONE, PASSWORD, TEST_SIDE_PHONE


class Test:

    phone = TEST_PHONE
    password = PASSWORD
    side_phone = TEST_SIDE_PHONE
    endpoint = '/account/phone'

    def test_successful_adding_phone_to_account_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        name = 'test_adding_phone'
        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.side_phone,
                'name': name}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 201
        assert type(res.get_content()) == dict
        assert len(res.get_content()) == 5
        assert res.get_content()['phone'] == self.side_phone
        assert res.get_content()['name'] == name

    def test_validation_adding_phone_to_account_with_empty_name_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.side_phone}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 201
        assert type(res.get_content()) == dict
        assert len(res.get_content()) == 5
        assert res.get_content()['phone'] == self.side_phone
        assert res.get_content()['name'] is None

    def test_validation_adding_phone_to_account_with_empty_phone_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        headers = {'Authorization': f'Bearer {token}'}
        data = {}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'phone'
        assert res.get_content()[0]['message'] == 'Необходимо заполнить «Номер телефона».'

    def test_validation_adding_phone_to_account_with_too_long_name_at_lk(self):
        token = get_access_token(phone=self.phone, password=self.password)

        name = 'test_validation_too_long_name_1'  # 31 chars
        headers = {'Authorization': f'Bearer {token}'}
        data = {'phone': self.side_phone,
                'name': name}

        req = Request('POST', endpoint=self.endpoint,
                      headers=headers, data=data)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 422
        assert res.get_reason() == 'Data Validation Failed.'
        assert res.get_content()[0]['field'] == 'name'
        assert res.get_content()[0]['message'] == 'Значение «Название телефона» должно содержать максимум 30 символов.'

    def test_unsuccessful_getting_phone_list_without_token_at_lk(self):
        req = Request('POST', endpoint=self.endpoint)

        res = req.make_request_to_endpoint()

        assert res.get_status_code() == 401
        assert res.get_reason() == 'Unauthorized'
        assert res.get_content()['message'] == 'Your request was made with invalid credentials.'

import requests


url = 'https://api.store.dev.bezlimit.ru/v2/users/restore-password'
email = 'api_store_autotest@bezlimit.ru'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

class TestValidation:
    def test_empty_params(self):
        params = {
            'email': None,
            'phone': None,
            'code': None
        }

        response = requests.put(url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'email', 'message': 'Укажите email'}]

    def test_email_integer(self):
        params = {
            'email': 123456,
            'phone': None,
            'code': None
        }

        response = requests.put(url, headers=headers, data=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'email', 'message': 'Неверный формат email'}]

    def test_phone_small(self):
        params = {
            'email': None,
            'phone': 969658,
            'code': None
        }

        response = requests.put(url, headers=headers, data=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Указанный номер телефона не найден в системе'}]

    def test_phone_large(self):
        params = {
            'email': None,
            'phone': 9000000000000000000,
            'code': None
        }

        response = requests.put(url, headers=headers, data=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Указанный номер телефона не найден в системе'}]

class TestNegative:
    def test_email_incorrect(self):
        params = {
            'email': 'billy@herrington.gm',
            'phone': None,
            'code': None
        }

        response = requests.put(url, headers=headers, data=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'email', 'message': 'Указанный email не найден в системе'}]

    def test_phone_incorrect(self):
        params = {
            'email': None,
            'phone': 9000000000,
            'code': None
        }

        response = requests.put(url, headers=headers, data=params)

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone', 'message': 'Указанный номер телефона не найден в системе'}]


class TestPositive:
    def test_anal(self):
        pass

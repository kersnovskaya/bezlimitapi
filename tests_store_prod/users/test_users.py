import requests


url = 'https://api.store.bezlimit.ru/v2/users'
token = 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq'

fields = ['id', 'login', 'profile', 'personal_data', 'level', 'dealer']
expand = ('profile', 'personal_data', 'level', 'dealer')
headers = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Api-Token': token
}


class TestNegative:
    shitty_token = 'allahakbar'

    def test_unauthorized(self):
        shitty_headers = {
            'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
            'accept': 'application/json',
            'Api-Token': self.shitty_token
        }
        response = requests.get(url, headers=shitty_headers)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401
        }

    def test_shitty_expand_and_fields(self):
        params = {
            'fields': 12345,
            'expand': 12345
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 200
        assert response.json() == []


class TestPositive:
    def test_simple(self):
        response = requests.get(url, headers=headers)

        assert response.status_code == 200
        assert response.json() == {
            "id": 285986,
            "login": "autotest"
        }

    def test_expand(self):
        for exp_field in expand:
            params = {
                'expand': exp_field
            }

            response = requests.get(url, headers=headers, params=params)
            des_res = response.json()

            assert response.status_code == 200, 'Всё плохо.'
            assert exp_field in des_res.keys()

    def test_fields(self):
        for field in fields:
            pass
import requests

url = 'https://api.store.bezlimit.ru/v2/users'
token = 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq'

fields = ('id', 'login')
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

    def test_all_expand(self):
        params = {
            'expand': 'profile, personal_data, level, dealer, loyalty'
        }

        response = requests.get(url, params=params, headers=headers)

        assert response.status_code == 200
        assert response.json() == {
            "id": 285986,
            "login": "autotest",
            "profile":
                {
                    "id": 285965,
                    "email": "api_store_autotest@bezlimit.ru",
                    "email_status": "confirmed",
                    "avatar": ""
                },
            "personal_data":
                {
                    "id": 107095,
                    "user_id": 285986,
                    "phone": 9696588825,
                    "phone_status": "reject",
                    "is_phone_bezlimit": 1,
                    "first_name": "",
                    "second_name": "",
                    "last_name": "",
                    "gender": None,
                    "birthday": "1970-01-01",
                    "series": "",
                    "number": "",
                    "department_code": "",
                    "issued_by": "",
                    "issue_date": "1970-01-01",
                    "passport_status": "reject",
                    "passport_comment": ""
                },
            "level":
                {
                    "id": 136875,
                    "user_id": 285986,
                    "login": "autotest",
                    "name": "autotest",
                    "phone": 9696588825,
                    "level": 1
                },
            "dealer":
                {
                    "id": 365151,
                    "sas_user_id": 285986,
                    "path": "ID 4001: Дистрибьюторская Сеть / ID 141875: Поддержка продаж / ID 22434: Store Bezlimit / ID 43949: Аккаунт для теста / ID 365151: autotest"
                },
            "loyalty":
                {
                    "id": 5,
                    "code": "bronze",
                    "name": "Бронза"
                }
        }

    def test_fields(self):
        for field in fields:
            params = {
                'fields': field
            }

            response = requests.get(url, headers=headers, params=params)

            assert len(response.json()) == 1
            assert list(response.json().keys()) == [field]

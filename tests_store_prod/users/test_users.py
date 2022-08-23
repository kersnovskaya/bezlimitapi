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
        assert response.json() == {'dealer': {'id': 365151,
                                              'path': 'ID 4001: Дистрибьюторская Сеть / ID 141875: Поддержка '
                                                      'продаж / ID 22434: Store Bezlimit / ID 43949: Аккаунт для '
                                                      'теста / ID 365151: autotest',
                                              'sas_user_id': 285986},
                                   'id': 285986,
                                   'level': {'id': 136875,
                                             'level': 1,
                                             'login': 'autotest',
                                             'name': 'autotest',
                                             'phone': 9621110832,
                                             'user_id': 285986},
                                   'login': 'autotest',
                                   'loyalty': {'code': 'bronze', 'id': 5, 'name': 'Бронза'},
                                   'personal_data': {'birthday': '1989-04-13',
                                                     'department_code': '113-112',
                                                     'first_name': '',
                                                     'gender': 0,
                                                     'id': 107095,
                                                     'is_phone_bezlimit': 1,
                                                     'issue_date': '1999-06-13',
                                                     'issued_by': 'человеком',
                                                     'last_name': '',
                                                     'number': '150148',
                                                     'passport_comment': 'Фотографии паспорта не загружены.',
                                                     'passport_status': 'reject',
                                                     'phone': 9621110832,
                                                     'phone_status': 'confirmed',
                                                     'second_name': '',
                                                     'series': '1455',
                                                     'user_id': 285986},
                                   'profile': {
                                       'avatar': 'https://bl-data.ams3.digitaloceanspaces.com/sas/avatars/285965/77c0fe9dc254edf145db6548b122c6fd.jpg',
                                       'email': 'api_store_autotest@bezlimit.ru',
                                       'email_status': 'confirmed',
                                       'id': 285965}}

    def test_fields(self):
        for field in fields:
            params = {
                'fields': field
            }

            response = requests.get(url, headers=headers, params=params)

            assert len(response.json()) == 1
            assert list(response.json().keys()) == [field]

import requests

token = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
headers_castrate = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
}
headers = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Api-Token': token
}
url = 'https://api.store.dev.bezlimit.ru/v2/phones'
pages = ['1', '52', '2', '6', '20']

class TestNegative:
    def test_unauthorized(self):
        response = requests.get(url, headers=headers_castrate)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401,
            'type': 'yii\\web\\UnauthorizedHttpException'
        }

    def test_wrong_params(self):
        params = {
            'type': 'фддфрфлифк',
            'phone': 'фддфрфлифк',
            'phone_pattern': 'фддфрфлифк',
            'phone_combs': 'фддфрфлифк',
            'mask_category': 'фддфрфлифк',
            'mask_pattern': 'фддфрфлифк',
            'service_limit': 'фддфрфлифк',
            'region_id': 'фддфрфлифк',
            'is_reserved': 'фддфрфлифк',
            'sort': 'фддфрфлифк',
            'fields': 'фддфрфлифк',
            'expand': 'фддфрфлифк',
            'page': 'asshole',
            'per_page': 'penis'
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'is_reserved',
                'message': 'Значение «Is Reserved» должно быть равно «1» или «0».'
            },
            {
                'field': 'phone',
                'message': 'Значение «phone» должно быть целым числом.'
            },
            {
                'field': 'type',
                'message': 'Значение "type" может быть standard, internet, paid'
            }
        ]

class TestPositive:
    def test_type_standard(self):
        for page in pages:
            params = {
                'type': 'standard',
                'page': page
            }

            response = requests.get(url, headers=headers, params=params)

            assert response.status_code == 200
            assert response.headers['x-pagination-current-page'] == page
            for shit in response.json()['items']:
                assert shit['type_category'] == 'standard'

    def test_type_internet(self):
        for page in pages:
            params = {
                'type': 'internet',
                'page': page
            }

            response = requests.get(url, headers=headers, params=params)

            assert response.status_code == 200
            assert response.headers['x-pagination-current-page'] == page
            for shit in response.json()['items']:
                assert shit['type_category'] == 'internet'

    def test_type_paid(self):
        for page in pages:
            params = {
                'type': 'paid',
                'page': page
            }

            response = requests.get(url, headers=headers, params=params)

            assert response.status_code == 200
            assert response.headers['x-pagination-current-page'] == page
            for shit in response.json()['items']:
                assert shit['type_category'] == 'paid'

    def test_phone(self):
        for page in pages:
            params = {
                'phone': 666,
                'page': page
            }

            response = requests.get(url, headers=headers, params=params)

            assert response.status_code == 200
            assert response.headers['x-pagination-current-page'] == page
            for shit in response.json()['items']:
                assert '666' in str(shit['phone'])

    def test_sex(self):
        pass

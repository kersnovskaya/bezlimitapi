import requests


url = 'https://api.store.bezlimit.ru/v2/users/levels'
token = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'

fields = ['id', 'user_id', 'login', 'name', 'phone', 'level']
expand = ('loyalty', 'activation')
headers = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Api-Token': token
}


class TestNegative:
    def test_unauthorized(self):
        del headers['Api-Token']

        response = requests.get(url, headers=headers)

        assert response.status_code == 401
        assert response.json() == {
            'name': 'Unauthorized',
            'message': 'Your request was made with invalid credentials.',
            'code': 0,
            'status': 401
        }

class TestPositive:
    def test_correct_fields(self):
        for field in fields:
            params = {
                'fields': field
            }

            response = requests.get(url, headers=headers, params=params)
            for little_shit in response.json()['items']:
                assert len(little_shit) == 1
                assert list(little_shit.keys()) == [field]

    def test_correct_simple(self):
        response = requests.get(url, headers=headers)

        for pity_shit in response.json()['items']:
            assert list(pity_shit.keys()) == fields
            for field in fields:
                assert pity_shit[field] == 'little_dick'

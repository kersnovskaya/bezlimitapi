import requests


url = 'https://api.store.bezlimit.ru/v2/users/levels'
token = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'

fields = ['id', 'user_id', 'login', 'name', 'phone', 'level']
expand = ('loyalty', 'activation')
headers_castrate = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
}
headers = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Api-Token': token
}

class TestNegative:
    def test_unauthorized(self):
        response = requests.get(url, headers=headers_castrate)

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
                if field == 'id' or field == 'user_id' or field == 'phone' or field == 'level':
                    assert type(pity_shit[field]) == int
                else:
                    assert type(pity_shit[field]) == str

    def test_correct_expand(self):
        data = {
            'expand': 'loyalty, activation'
        }
        response = requests.get(url, headers=headers, data=data)

        for pity_shit in response.json()['items']:
            assert list(pity_shit.keys()) == fields
            for field in fields:
                if field == 'id' or field == 'user_id' or field == 'phone' or field == 'level':
                    assert type(pity_shit[field]) == int
                else:
                    assert type(pity_shit[field]) == str



ass = {
  "items": [
    {
      "id": 145609,
      "user_id": 361405,
      "login": "408499",
      "name": "татвовььв --",
      "phone": 9999999999,
      "level": 1,
      "activation": {
        "total_cnt": 0,
        "total_personal_cnt": 0,
        "total_level_cnt": 0,
        "current_month_cnt": 0,
        "current_month_personal_cnt": 0,
        "current_month_level_cnt": 0,
        "previous_month_cnt": 0,
        "previous_month_personal_cnt": 0,
        "previous_month_level_cnt": 0,
        "last_month_cnt": 0,
        "last_month_personal_cnt": 0,
        "last_month_level_cnt": 0,
        "last_date": ""
      },
      "loyalty": {
        "id": 5,
        "code": "bronze",
        "name": "Бронза"
      }
    }
  ]
}

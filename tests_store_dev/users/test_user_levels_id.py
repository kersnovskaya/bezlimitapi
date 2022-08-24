import requests

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
        url = 'https://api.store.dev.bezlimit.ru/v2/users/levels/1'

        response = requests.get(url, headers=headers_castrate)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401,
            'type': 'yii\\web\\UnauthorizedHttpException'
        }

    def test_incorrect_id(self):
        url = 'https://api.store.dev.bezlimit.ru/v2/users/levels/1488'
        response = requests.get(url, headers=headers)

        assert response.status_code == 404
        assert response.json() == {
            'name': 'Not Found',
            'message': 'Уровень "1488" не найден',
            'code': 0,
            'status': 404,
            'type': 'yii\\web\\NotFoundHttpException'
        }


class TestPositive:
    def test_correct_fields(self):
        url = 'https://api.store.dev.bezlimit.ru/v2/users/levels/146050'

        for field in fields:
            params = {
                'fields': field
            }

            response = requests.get(url, headers=headers, params=params)
            assert len(response.json()) == 1
            assert list(response.json().keys()) == [field]

    def test_correct_simple(self):
        url = 'https://api.store.dev.bezlimit.ru/v2/users/levels/146050'

        response = requests.get(url, headers=headers)

        assert list(response.json().keys()) == fields
        for field in fields:
            if field == 'id' or field == 'user_id' or field == 'phone' or field == 'level':
                assert type(response.json()[field]) == int
            else:
                assert type(response.json()[field]) == str

    def test_correct_expand(self):
        url = 'https://api.store.dev.bezlimit.ru/v2/users/levels/146050'

        params = {
            'expand': 'loyalty, activation'
        }
        response = requests.get(url, headers=headers, params=params)

        for field in fields:
            if field == 'id' or field == 'user_id' or field == 'phone' or field == 'level':
                assert type(response.json()[field]) == int
            else:
                assert type(response.json()[field]) == str
        assert type(response.json()['activation']["total_cnt"]) == int
        assert type(response.json()['activation']["total_personal_cnt"]) == int
        assert type(response.json()['activation']["total_level_cnt"]) == int
        assert type(response.json()['activation']["current_month_cnt"]) == int
        assert type(response.json()['activation']["current_month_personal_cnt"]) == int
        assert type(response.json()['activation']["current_month_level_cnt"]) == int
        assert type(response.json()['activation']["previous_month_cnt"]) == int
        assert type(response.json()['activation']["previous_month_personal_cnt"]) == int
        assert type(response.json()['activation']["previous_month_level_cnt"]) == int
        assert type(response.json()['activation']["last_month_cnt"]) == int
        assert type(response.json()['activation']["last_month_personal_cnt"]) == int
        assert type(response.json()['activation']["last_month_level_cnt"]) == int
        assert type(response.json()['activation']["last_date"]) == str
        assert type(response.json()['loyalty']["id"]) == int
        assert type(response.json()['loyalty']["code"]) == str
        assert type(response.json()['loyalty']["name"]) == str

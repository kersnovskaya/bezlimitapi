import requests


url = 'https://api.store.bezlimit.ru/v2/loyalty'
token0 = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
token1 = 'jxrOOpE33Zb944m8w5KUXhgIHPGHS1V0zO1wbphFnXNZSjL-Sa5_KGwYwndejafJ'
token2 = 'plq-rqmPaSlZ1bpN-LFYZX_WMQOjiuWVK8-2WnUG8n-AyBhprQgSVdXfE58Al9nW'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json'
}


class TestNegative:
    def test_unauthorized(self):
        message = ['Список возможных статусов лояльности. Не авторизован.']
        expected_message = ['Список возможных статусов лояльности. Не авторизован.']

        response = requests.get(url, headers=headers)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f'Код ответа: "{response.status_code}", а не "401"')

        assert message == expected_message, message


class TestPositive:
    def test_lvl_0(self):
        message = ['Список возможных статусов лояльности. Уровень 0.']
        expected_message = ['Список возможных статусов лояльности. Уровень 0.']
        headers.update({'Api-Token': token0})

        response = requests.get(url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа: "{response.status_code}", а не "200"')
        try:
            assert response.json() == [
                {
                    "level": 0,
                    "code": "bronze",
                    "name": "Бронза",
                    "min_cnt": 0,
                    "max_cnt": 9,
                    "rate_personal": 0,
                    "rate_level": 0
                },
                {
                    "level": 0,
                    "code": "silver",
                    "name": "Серебро",
                    "min_cnt": 10,
                    "max_cnt": 19,
                    "rate_personal": 5,
                    "rate_level": 0
                },
                {
                    "level": 0,
                    "code": "gold",
                    "name": "Золото",
                    "min_cnt": 20,
                    "max_cnt": 49,
                    "rate_personal": 25,
                    "rate_level": 5
                },
                {
                    "level": 0,
                    "code": "top",
                    "name": "ТОП",
                    "min_cnt": 50,
                    "max_cnt": 10000000,
                    "rate_personal": 40,
                    "rate_level": 10
                }
            ]
        except AssertionError:
            message.append('В теле ответа указаны некорректные статусы лояльности.')
        assert message == expected_message, message

    def test_lvl_1(self):
        message = ['Список возможных статусов лояльности. Уровень 1.']
        expected_message = ['Список возможных статусов лояльности. Уровень 1.']
        headers.update({'Api-Token': token1})

        response = requests.get(url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа: "{response.status_code}", а не "200"')
        try:
            assert response.json() == [
                {
                    "level": 1,
                    "code": "bronze",
                    "name": "Бронза",
                    "min_cnt": 0,
                    "max_cnt": 9,
                    "rate_personal": 0,
                    "rate_level": 0
                },
                {
                    "level": 1,
                    "code": "silver",
                    "name": "Серебро",
                    "min_cnt": 10,
                    "max_cnt": 19,
                    "rate_personal": 15,
                    "rate_level": 0
                },
                {
                    "level": 1,
                    "code": "gold",
                    "name": "Золото",
                    "min_cnt": 20,
                    "max_cnt": 49,
                    "rate_personal": 35,
                    "rate_level": 5
                },
                {
                    "level": 1,
                    "code": "top",
                    "name": "ТОП",
                    "min_cnt": 50,
                    "max_cnt": 10000000,
                    "rate_personal": 50,
                    "rate_level": 10
                }
            ]
        except AssertionError:
            message.append('В теле ответа указаны некорректные статусы лояльности.')
        assert message == expected_message, message

    def test_lvl_2(self):
        message = ['Список возможных статусов лояльности. Уровень 2.']
        expected_message = ['Список возможных статусов лояльности. Уровень 2.']
        headers.update({'Api-Token': token2})

        response = requests.get(url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа: "{response.status_code}", а не "200"')
        try:
            assert response.json() == [
                {
                    "level": 2,
                    "code": "bronze",
                    "name": "Бронза",
                    "min_cnt": 0,
                    "max_cnt": 9,
                    "rate_personal": 0,
                    "rate_level": 0
                },
                {
                    "level": 2,
                    "code": "silver",
                    "name": "Серебро",
                    "min_cnt": 10,
                    "max_cnt": 19,
                    "rate_personal": 20,
                    "rate_level": 0
                },
                {
                    "level": 2,
                    "code": "gold",
                    "name": "Золото",
                    "min_cnt": 20,
                    "max_cnt": 49,
                    "rate_personal": 30,
                    "rate_level": 0
                },
                {
                    "level": 2,
                    "code": "top",
                    "name": "ТОП",
                    "min_cnt": 50,
                    "max_cnt": 10000000,
                    "rate_personal": 40,
                    "rate_level": 0
                }
            ]
        except AssertionError:
            message.append('В теле ответа указаны некорректные статусы лояльности.')
        assert message == expected_message, message

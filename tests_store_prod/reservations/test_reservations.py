import requests


url = 'https://api.store.dev.bezlimit.ru/v2/reservations'
token0 = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
token1 = 'jxrOOpE33Zb944m8w5KUXhgIHPGHS1V0zO1wbphFnXNZSjL-Sa5_KGwYwndejafJ'
token2 = 'plq-rqmPaSlZ1bpN-LFYZX_WMQOjiuWVK8-2WnUG8n-AyBhprQgSVdXfE58Al9nW'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json'
}


class TestNegative:
    def test_unauthorized(self):
        response = requests.get(url, headers=headers)

        assert response.status_code == 401
        assert response.json() == {
            "name": "Unauthorized",
            "message": "Your request was made with invalid credentials.",
            "code": 0,
            "status": 401,
            "type": "yii\\web\\UnauthorizedHttpException"
        }

    def test_incorrect_data(self):
        headers.update({'Api-Token': token0})
        params = {
            'activated_from': 2,
            'activated_to': 1
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.json() == [
            {
                "field": "activated_from",
                "message": "Неверный формат даты. Возможный вариант: Y-m-d H:i:s"
            },
            {
                "field": "activated_to",
                "message": "Неверный формат даты. Возможный вариант: Y-m-d H:i:s"
            }
        ]

    def test_phone(self):
        headers.update({'Api-Token': token1})
        params = {
            'phone_number': 'False'
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'phone_number',
                'message': 'Значение "phone_number" может быть целым числом'
            }
        ]


class TestPositive:
    def test_is_activated_true(self):
        headers.update({'Api-Token': token1})
        params = {
            'is_activated': True
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 200
        for i_dict in response.json()['items']:
            assert i_dict['is_activated'] is True

    def test_is_activated_false(self):
        headers.update({'Api-Token': token1})
        params = {
            'is_activated': False
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 200
        for i_dict in response.json()['items']:
            assert i_dict['is_activated'] is False

    def test_phone_number(self):
        headers.update({'Api-Token': token2})
        phone = 968
        params = {
            'phone_number': phone,
            'is_activated': True
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 200
        for i_dict in response.json()['items']:
            assert str(phone) in str(i_dict['phone_number'])

    def test_page(self):
        headers.update({'Api-Token': token2})
        params = {
            'is_activated': True,
            'page': 2,
            'per_page': 1
        }

        response = requests.get(url, headers=headers, params=params)

        assert response.status_code == 200
        assert len(response.json()['items']) == 1
        assert response.json()['_meta']['currentPage'] == 2
        assert response.json()['_meta']['perPage'] == 1

    def test_sort(self):
        pass

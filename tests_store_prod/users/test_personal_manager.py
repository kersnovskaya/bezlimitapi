import requests


url = 'https://api.store.bezlimit.ru/v2/users/personal-manager'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json'
}


class TestNegative:
    def test_unauthorized(self):
        response = requests.get(url, headers=headers)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401
        }


class TestPositive:

    token0 = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
    token1 = 'jxrOOpE33Zb944m8w5KUXhgIHPGHS1V0zO1wbphFnXNZSjL-Sa5_KGwYwndejafJ'
    token2 = 'plq-rqmPaSlZ1bpN-LFYZX_WMQOjiuWVK8-2WnUG8n-AyBhprQgSVdXfE58Al9nW'

    def test_correct_level_0(self):
        headers.update({'Api-Token': self.token0})

        response = requests.get(url, headers=headers)

        assert response.json() is None

    def test_correct_level_1(self):
        headers.update({'Api-Token': self.token1})

        response = requests.get(url, headers=headers)

        assert response.json() == {
            "name": "Test AutoInp0",
            "phone": 9686244447
        }

    def test_correct_level_2(self):
        headers.update({'Api-Token': self.token2})

        response = requests.get(url, headers=headers)

        assert response.json() == {
            "name": "тест Рахимов",
            "phone": 9682229543
        }
